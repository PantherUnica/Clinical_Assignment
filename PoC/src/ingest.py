"""PDF -> page text (+ OCR fallback) -> token-based chunks with page provenance.

Chunking maths (see README):
    stride   = CHUNK_SIZE - CHUNK_OVERLAP
    n_chunks ~= total_tokens / stride

Chunks never split mid-word and are cut on sentence boundaries, so a citation
points at a readable passage. Each chunk records the page it starts on (and the
page it ends on, when it spans a boundary) - that is what makes citations
resolve to "book, page, passage".
"""

from __future__ import annotations

import json
import re
from pathlib import Path

try:
    import pymupdf
except ImportError:  # older PyMuPDF releases only expose the `fitz` name
    import fitz as pymupdf

import config

try:
    import tiktoken

    _ENC = tiktoken.get_encoding("cl100k_base")
except Exception:  # tiktoken missing or no network for the BPE file
    _ENC = None

_ocr_warned = False


def count_tokens(text: str) -> int:
    """Exact token count when tiktoken is available, ~chars/4 otherwise."""
    if _ENC is not None:
        return len(_ENC.encode(text))
    return max(1, len(text) // 4)


def _token_slices(text: str, max_tokens: int) -> list[str]:
    """Split text that is longer than one chunk (tables, unpunctuated runs)."""
    if count_tokens(text) <= max_tokens:
        return [text]
    if _ENC is not None:
        ids = _ENC.encode(text)
        # Slicing token ids can cut a multi-byte character in half, and decoding
        # the partial bytes yields U+FFFD - strip those, not the PDF's own text.
        return [
            _ENC.decode(ids[i : i + max_tokens]).replace("�", "")
            for i in range(0, len(ids), max_tokens)
        ]
    step = max_tokens * 4
    return [text[i : i + step] for i in range(0, len(text), step)]


def _normalize(text: str) -> str:
    text = text.replace("\r", "\n")
    text = text.replace("�", "")  # drop undecodable glyphs from the PDF
    text = re.sub(r"-\n(\w)", r"\1", text)  # rejoin words hyphenated across lines
    text = re.sub(r"\s*\n\s*", " ", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def _split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def _ocr_page(page) -> str:
    """OCR fallback for image-only pages. Returns '' if OCR is unavailable."""
    global _ocr_warned
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        if not _ocr_warned:
            print("    [warn] OCR skipped - pip install pytesseract pillow to read scanned pages.")
            _ocr_warned = True
        return ""
    try:
        pix = page.get_pixmap(dpi=200, colorspace=pymupdf.csRGB, alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        return pytesseract.image_to_string(image)
    except Exception as exc:
        if not _ocr_warned:
            print(f"    [warn] OCR unavailable ({exc}). Install the Tesseract binary to enable it.")
            _ocr_warned = True
        return ""


def extract_pages(pdf_path: Path) -> tuple[list[tuple[int, str]], int]:
    """Return [(page_number, text), ...] and how many pages needed OCR."""
    doc = pymupdf.open(pdf_path)
    pages: list[tuple[int, str]] = []
    ocr_pages = 0
    try:
        for number, page in enumerate(doc, start=1):
            raw = page.get_text("text") or ""
            if len(raw.strip()) < config.OCR_MIN_CHARS:
                ocr_text = _ocr_page(page)
                if len(ocr_text.strip()) > len(raw.strip()):
                    raw = ocr_text
                    ocr_pages += 1
            pages.append((number, _normalize(raw)))
    finally:
        doc.close()
    return pages, ocr_pages


def _book_title(pdf_path: Path) -> str:
    return re.sub(r"[_\-]+", " ", pdf_path.stem).strip() or pdf_path.stem


def _slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "book"


def chunk_pages(
    pages: list[tuple[int, str]],
    book_title: str,
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[dict]:
    """Greedily pack sentences into ~chunk_size token windows with overlap."""
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = config.CHUNK_OVERLAP if overlap is None else overlap
    slug = _slug(book_title)

    units: list[tuple[int, str, int]] = []  # (page, sentence, tokens)
    for page_number, page_text in pages:
        for piece, tokens in split_units(page_text, chunk_size):
            units.append((page_number, piece, tokens))

    chunks: list[dict] = []
    for start, end, total in pack_windows([u[2] for u in units], chunk_size, overlap):
        window = units[start:end]
        chunks.append(
            {
                "chunk_id": f"{slug}_p{window[0][0]}_{len(chunks):04d}",
                "book_title": book_title,
                "page": window[0][0],
                "page_end": window[-1][0],
                "text": " ".join(u[1] for u in window),
                "token_count": total,
            }
        )
    return chunks


def split_units(text: str, chunk_size: int) -> list[tuple[str, int]]:
    """Text -> [(sentence-or-slice, tokens)], the units that chunks are packed from."""
    out = []
    for sentence in _split_sentences(text):
        for piece in _token_slices(sentence, chunk_size):
            piece = piece.strip()
            if piece:
                out.append((piece, count_tokens(piece)))
    return out


def pack_windows(token_counts: list[int], chunk_size: int, overlap: int) -> list[tuple[int, int, int]]:
    """Greedy packing shared by both profiles: [(start, end, tokens)] unit windows.

    Each window takes units until it reaches chunk_size tokens; the next window
    steps back far enough to repeat ~overlap tokens.
    """
    windows = []
    start, n = 0, len(token_counts)
    while start < n:
        end, total = start, 0
        while end < n and total < chunk_size:
            total += token_counts[end]
            end += 1
        windows.append((start, end, total))
        if end >= n:
            break
        back, cursor = 0, end
        while cursor > start + 1 and back < overlap:
            cursor -= 1
            back += token_counts[cursor]
        start = cursor if cursor > start else end
    return windows


def ingest_all(books_dir: Path | str | None = None) -> list[dict]:
    books_dir = Path(books_dir) if books_dir else config.BOOKS_DIR
    pdfs = sorted(books_dir.glob("*.pdf"))
    if not pdfs:
        raise FileNotFoundError(
            f"No PDFs found in {books_dir}. Drop your two books there and re-run."
        )

    all_chunks: list[dict] = []
    for pdf in pdfs:
        title = _book_title(pdf)
        print(f"  Reading {pdf.name} ...")
        pages, ocr_pages = extract_pages(pdf)
        total_tokens = sum(count_tokens(text) for _, text in pages)
        chunks = chunk_pages(pages, title)
        all_chunks.extend(chunks)
        predicted = total_tokens // max(1, config.stride())
        print(
            f"    pages={len(pages)}  ocr_pages={ocr_pages}  tokens~{total_tokens:,}\n"
            f"    chunks={len(chunks)}  (formula: {total_tokens:,} / stride {config.stride()} "
            f"~= {predicted:,})"
        )
    return all_chunks


def write_chunks(chunks: list[dict], path: Path | str | None = None) -> Path:
    path = Path(path) if path else config.CHUNKS_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for chunk in chunks:
            handle.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    return path


def load_chunks(path: Path | str | None = None) -> list[dict]:
    path = Path(path) if path else config.CHUNKS_PATH
    if not path.exists():
        raise FileNotFoundError(f"{path} not found. Run: python -m src.embed_index")
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract book text.")
    parser.add_argument("--profile", choices=["eval2", "library"], default="eval2")
    parser.add_argument("--only", nargs="*", help="library: only these book_ids")
    parser.add_argument("--force", action="store_true", help="library: re-extract even if cached")
    args = parser.parse_args()
    config.ensure_dirs()
    if args.profile == "library":
        from . import library

        library.extract_all(only=args.only, force=args.force)
        raise SystemExit(0)
    produced = ingest_all()
    destination = write_chunks(produced)
    print(f"\nWrote {len(produced):,} chunks to {destination}")
