"""Full-library extraction: PDF -> cleaned page text + metadata (KB_PROFILE=library).

    python -m src.ingest --profile library [--only book_id ...] [--force]

For every book in books/library_manifest.json (skip=true entries ignored) this
writes data/library/pages/<book_id>.jsonl, one row per kept page:

    {book_id, book_title, edition, pdf_page, printed_page, chapter, section, ocr, text}

and data/library/pages/<book_id>.stats.json (what was removed and why), which the
audit report reads. A book whose pages file already exists is skipped unless
--force, so a crash part-way through only redoes the book it was on.

Cleaning, in order:
  1. OCR  - force_ocr books: every page; others: only pages with < OCR_MIN_CHARS
            of text. OCR text is cached per page in data/library/ocr_cache/.
  2. Junk pages - pages under TOC entries like Index / Copyright / Contents /
            Dedication / Contributors, and blank pages, are dropped.
  3. Headers/footers - among the first/last 3 lines of each page, a line whose
            digit-masked form recurs on >= HEADER_MIN_PAGES pages is a running
            head/foot and is removed; bare page numbers are always removed.
  4. Normalise - the existing ingest._normalize (hyphen rejoin, whitespace).

Printed page numbers: the PDF's own page label when it has one; otherwise the
per-page (pdf_page - number) offset voted locally from numbers in header/footer lines;
otherwise None (citations then fall back to the PDF page).
"""

from __future__ import annotations

import json
import re
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

try:
    import pymupdf
except ImportError:
    import fitz as pymupdf

import config

from .ingest import _normalize

EDGE_LINES = 3
HEADER_MIN_PAGES = 4
HEADER_MIN_SHARE = 0.005  # big books: must recur on >= 0.5% of pages too
HEADER_MAX_LEN = 100
HEADER_MIDDLE_MAX_SHARE = 0.25  # a running head may appear mid-page at most this often (OCR reorders lines)
_HEADER_CHAPTER = re.compile(r"^\s*(section|chapter)\s+[\divxlc]+\b", re.I)
OFFSET_WINDOW = 15  # pages either side that vote on a page's printed-number offset
OFFSET_MIN_VOTES = 4  # agreeing pages needed in that window
OFFSET_MIN_CONFIRMED = 0.30  # below this share of self-confirmed pages, don't trust the numbers
JUNK_MAX_SHARE = 0.10  # a "junk" TOC section larger than this share of the book is kept

_JUNK_TITLES = re.compile(
    r"(index|index (of|by) .*|subject index|drug index|general index|copyright( page)?|contents|table of contents|"
    r"dedication|contributors?|list of contributors|front cover|cover|back cover|title page|"
    r"half title page|front matter|acknowledg(e)?ments?|about the (author|authors|editors|"
    r"companion website)|editors?|section facilitators|consulting editors|editorial panel|"
    r"reviewers|other .* books|es1|prelims|this page intentionally left blank)",
    re.I,
)
_WRAPPER_TITLE = re.compile(
    # "Two Soft Tissue Surgery" = Fossum's "Part Two" with the word "Part" missing
    r"^\s*((part|section|volume|unit|book|one|two|three|four|five|six)\b.*|[a-z]|[a-z]\s*[-–]\s*[a-z])\s*$",
    re.I,
)
# "123", "- 12 -", "xiv", "\x01" - a line that is only a page number / roman numeral / symbols
_BARE_NUMBER = re.compile(
    r"[\W_]*(\d{1,4}|m{0,3}(cm|cd|d?c{0,3})(xc|xl|l?x{0,3})(ix|iv|v?i{0,3}))?[\W_]*", re.I
)
_EDGE_NUMBER = re.compile(r"^\s*(\d{1,4})\b|\b(\d{1,4})\s*$")


# --- manifest ---------------------------------------------------------------


def load_manifest(include_skipped: bool = False) -> list[dict]:
    data = json.loads(config.LIBRARY_MANIFEST.read_text(encoding="utf-8"))
    books = data["books"]
    for b in books:
        b["path"] = config.BOOKS_DIR / b["file"]
    return books if include_skipped else [b for b in books if not b.get("skip")]


def pages_path(book_id: str) -> Path:
    return config.LIBRARY_PAGES_DIR / f"{book_id}.jsonl"


def stats_path(book_id: str) -> Path:
    return config.LIBRARY_PAGES_DIR / f"{book_id}.stats.json"


def load_pages(book_id: str) -> list[dict]:
    with pages_path(book_id).open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


# --- OCR (cached, parallel) -------------------------------------------------


def _ocr_cache_file(book_id: str, pdf_page: int) -> Path:
    return config.OCR_CACHE_DIR / book_id / f"page_{pdf_page:05d}.txt"


def _ocr_worker(pdf_path: str, page_numbers: list[int], book_id: str, dpi: int, cmd: str) -> int:
    """Runs in a child process: OCR the given 1-based pages into the cache."""
    import pytesseract
    from PIL import Image

    pytesseract.pytesseract.tesseract_cmd = cmd
    doc = pymupdf.open(pdf_path)
    try:
        for n in page_numbers:
            out = _ocr_cache_file(book_id, n)
            if out.exists():
                continue
            pix = doc[n - 1].get_pixmap(dpi=dpi, colorspace=pymupdf.csRGB, alpha=False)
            image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            text = pytesseract.image_to_string(image)
            tmp = out.with_suffix(".tmp")
            tmp.write_text(text, encoding="utf-8")
            tmp.replace(out)  # atomic: a killed run never leaves a half-written page
    finally:
        doc.close()
    return len(page_numbers)


def ocr_pages(pdf_path: Path, book_id: str, page_numbers: list[int]) -> dict[int, str]:
    todo = [n for n in page_numbers if not _ocr_cache_file(book_id, n).exists()]
    (config.OCR_CACHE_DIR / book_id).mkdir(parents=True, exist_ok=True)
    if todo:
        if not Path(config.TESSERACT_CMD).exists():
            raise RuntimeError(
                f"Tesseract not found at {config.TESSERACT_CMD}; {len(todo)} pages of {book_id} need OCR."
            )
        workers = max(1, min(config.OCR_WORKERS, len(todo)))
        batches = [todo[i::workers] for i in range(workers)]
        print(f"    OCR {len(todo)} pages with {workers} workers (cached: {len(page_numbers) - len(todo)}) ...")
        started, done = time.time(), 0
        # Small batches so progress is visible and a crash loses little.
        small = [b[i : i + 10] for b in batches for i in range(0, len(b), 10)]
        with ProcessPoolExecutor(max_workers=workers) as pool:
            futures = [
                pool.submit(_ocr_worker, str(pdf_path), b, book_id, config.OCR_DPI, config.TESSERACT_CMD)
                for b in small
            ]
            for f in as_completed(futures):
                done += f.result()
                if done % 100 < 10 or done == len(todo):
                    rate = done / max(1e-6, time.time() - started)
                    eta = (len(todo) - done) / max(rate, 1e-6) / 60
                    print(f"      {done}/{len(todo)} pages  ({rate:.1f} p/s, ~{eta:.0f} min left)")
    return {n: _ocr_cache_file(book_id, n).read_text(encoding="utf-8") for n in page_numbers}


# --- structure: TOC, junk ranges, printed pages -----------------------------


def _clean_title(title: str) -> str:
    title = re.sub(r"\.pdf$", "", title.strip(), flags=re.I)
    title = title.replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", title).strip(" ,")


def toc_entries(doc) -> list[tuple[int, str, int]]:
    """[(level, title, start_page)] with titles cleaned and invalid pages dropped."""
    out = []
    for level, title, page in doc.get_toc(simple=True):
        if 1 <= page <= doc.page_count:
            out.append((level, _clean_title(title), page))
    return out


def junk_ranges(toc: list[tuple[int, str, int]], n_pages: int) -> list[tuple[int, int, str]]:
    """Page ranges under junk TOC titles. Oversized ranges are ignored (safety)."""
    ranges = []
    for i, (level, title, start) in enumerate(toc):
        if not _JUNK_TITLES.fullmatch(title.strip(" .:")):
            continue
        end = n_pages
        for level2, _, start2 in toc[i + 1 :]:
            if level2 <= level and start2 > start:
                end = start2 - 1
                break
        if (end - start + 1) <= max(3, JUNK_MAX_SHARE * n_pages):
            ranges.append((start, end, title))
    return ranges


# a line ending in a page reference: "toxicity 3043", "Exophthalmos, 107–108, 116f"
_INDEX_LINE = re.compile(r"[a-z\)][\s,]+\d{1,4}[eft]?(\s*[–-]\s*\d{1,4}[eft]?)?\s*$", re.I)


_INDEX_REF = re.compile(r",\s*\d{1,4}[eft]?\b")  # ", 885" / ", 904f" anywhere in a line


def _looks_like_index(text: str) -> bool:
    """Index pages: many lines end in a page reference (Merck style, no comma)
    or many ', 123' references overall (comma style; survives garbled OCR)."""
    lines = [l for l in text.splitlines() if l.strip()]
    if not lines:
        return False
    line_ends = sum(1 for l in lines if _INDEX_LINE.search(l)) / len(lines)
    comma_refs = len(_INDEX_REF.findall(text)) / len(lines)
    return line_ends > 0.3 or comma_refs > 0.3


def trim_index_end(raw: list[str], start: int, end: int) -> int:
    """The TOC says 'Index' runs to `end`, but appendices often follow it without
    a TOC entry. Stop the range at the first two consecutive non-index pages."""
    for p in range(start + 1, end):
        if not _looks_like_index(raw[p - 1]) and not _looks_like_index(raw[p]):
            return p - 1
    return end


_NUMBERED_TITLE = re.compile(r"^\s*(chapter\s+)?\d+\s*([.:\-–]|\s+[a-z])", re.I)


def _is_wrapper(title: str) -> bool:
    """Grouping titles that are not a chapter: 'Volume 1', 'Section II …', 'Part Two', 'A'."""
    return bool(_WRAPPER_TITLE.match(title))


def page_structure(toc, n_pages: int) -> list[tuple[str | None, str | None]]:
    """(chapter, section) for every page 1..n_pages (index 0 = page 1).

    Keeps the current TOC path (title per level). chapter = the shallowest
    title on that path that is not a wrapper (Volume / Part / Section / a bare
    letter); section = the deepest non-wrapper title below it.
    """
    out: list[tuple[str | None, str | None]] = []
    path: dict[int, str] = {}
    ordered = sorted(toc, key=lambda t: t[2])  # stable: parents stay before children
    i = 0
    for page in range(1, n_pages + 1):
        while i < len(ordered) and ordered[i][2] <= page:
            level, title, _ = ordered[i]
            path = {lv: t for lv, t in path.items() if lv < level}
            path[level] = title
            i += 1
        real = [path[lv] for lv in sorted(path) if not _is_wrapper(path[lv])]
        # Prefer a numbered title as the chapter: Ettinger nests "53. Polyuria and
        # Polydipsia" under an un-numbered group ("Urogenital").
        numbered = [i for i, t in enumerate(real) if _NUMBERED_TITLE.match(t)]
        ch_idx = numbered[0] if numbered else 0
        chapter = real[ch_idx] if real else None
        section = real[-1] if len(real) > ch_idx + 1 else None
        out.append((chapter, section))
    return out


def _edge_key(line: str) -> str:
    """Digit-masked, symbol-free form, so OCR variants of one running head
    ('Bacterial Skin Diseases * 295' / '© 294') compare equal."""
    key = re.sub(r"\d+", "#", line.lower())
    key = re.sub(r"[^a-z#]+", " ", key)
    return re.sub(r"\s+", " ", key).strip()


def _edges(lines: list[str]) -> list[str]:
    return lines[:EDGE_LINES] + lines[-EDGE_LINES:] if len(lines) > 2 * EDGE_LINES else lines


def detect_headers(page_lines: list[list[str]]) -> set[str]:
    """Running heads/feet: recur at page edges and (almost) never mid-page.

    The mid-page test is what keeps real content headings ("Doses", "Adverse
    Effects", "Subcutaneous") that just happen to land at a page edge.
    """
    min_pages = max(HEADER_MIN_PAGES, round(HEADER_MIN_SHARE * len(page_lines)))
    edge: Counter[str] = Counter()
    middle: Counter[str] = Counter()
    for lines in page_lines:
        edge.update({_edge_key(l) for l in _edges(lines) if len(l.strip()) <= HEADER_MAX_LEN})
        if len(lines) > 2 * EDGE_LINES:
            middle.update({_edge_key(l) for l in lines[EDGE_LINES:-EDGE_LINES]})
    return {
        k
        for k, c in edge.items()
        if k and c >= min_pages and middle[k] <= HEADER_MIDDLE_MAX_SHARE * c
    }


def detect_page_offsets(page_lines: list[list[str]]) -> tuple[list[int | None], float]:
    """Per-page (pdf_page - printed_number), decided locally.

    Each page votes for the offsets implied by numbers on its header/footer
    lines. A page's offset is the most common vote among pages within
    +-OFFSET_WINDOW of it (needing OFFSET_MIN_VOTES agreeing pages). Local, not
    global, because merged PDFs (e.g. Muller & Kirk, built from per-chapter
    files) shift the offset from chapter to chapter.

    Returns (offsets, confirmed) where confirmed = share of text pages whose own
    header/footer number matches the offset assigned to them.
    """
    n = len(page_lines)
    cands: list[set[int]] = []
    for idx, lines in enumerate(page_lines, start=1):
        seen = set()
        for line in _edges(lines):
            m = _EDGE_NUMBER.search(line.strip())
            if m:
                num = int(m.group(1) or m.group(2))
                if 0 < num <= idx + 50:
                    seen.add(idx - num)
        cands.append(seen)

    offsets: list[int | None] = []
    for i in range(n):
        window: Counter[int] = Counter()
        for j in range(max(0, i - OFFSET_WINDOW), min(n, i + OFFSET_WINDOW + 1)):
            window.update(cands[j])
        best = window.most_common(1)
        offsets.append(best[0][0] if best and best[0][1] >= OFFSET_MIN_VOTES else None)

    text_pages = sum(1 for lines in page_lines if lines)
    confirmed = sum(1 for i in range(n) if offsets[i] is not None and offsets[i] in cands[i])
    return offsets, confirmed / max(1, text_pages)


# --- one book ---------------------------------------------------------------


def extract_book(book: dict) -> dict:
    pdf_path: Path = book["path"]
    doc = pymupdf.open(pdf_path)
    n = doc.page_count
    try:
        raw = [doc[i].get_text("text") or "" for i in range(n)]
        labels = [doc[i].get_label() or "" for i in range(n)]
        toc = toc_entries(doc)
    finally:
        doc.close()

    force_ocr = bool(book.get("force_ocr"))
    need_ocr = [i + 1 for i, t in enumerate(raw) if force_ocr or len(t.strip()) < config.OCR_MIN_CHARS]
    ocr_used: set[int] = set()
    if need_ocr:
        ocr_text = ocr_pages(pdf_path, book["book_id"], need_ocr)
        for p, text in ocr_text.items():
            if force_ocr or len(text.strip()) > len(raw[p - 1].strip()):
                raw[p - 1] = text
                ocr_used.add(p)

    page_lines = [[l for l in t.splitlines() if l.strip()] for t in raw]
    headers = detect_headers(page_lines)
    has_labels = sum(1 for l in labels if l) >= 0.5 * n
    offsets, support = ([None] * n, 0.0) if has_labels else detect_page_offsets(page_lines)
    use_offsets = not has_labels and support >= OFFSET_MIN_CONFIRMED
    junk = [
        # Only a plain "Index" is trimmed: specific ones ("Index of trade names")
        # are exactly what their TOC range says, and may not look index-like.
        (start, trim_index_end(raw, start, end) if title.strip(" .:").lower() == "index" else end, title)
        for start, end, title in junk_ranges(toc, n)
    ]
    junk_page = {}
    for start, end, title in junk:
        for p in range(start, end + 1):
            junk_page[p] = title
    structure = page_structure(toc, n)

    rows, skipped = [], Counter()
    removed_lines: Counter[str] = Counter()
    heads_chapter: str | None = None  # no-TOC books: chapter carried forward from running heads
    for p in range(1, n + 1):
        if p in junk_page:
            skipped[f"toc:{junk_page[p]}"] += 1
            continue
        lines = page_lines[p - 1]
        kept = []
        edge_idx = set(range(min(EDGE_LINES, len(lines)))) | set(range(max(0, len(lines) - EDGE_LINES), len(lines)))
        for j, line in enumerate(lines):
            if j in edge_idx:
                key = _edge_key(line)
                if key in headers or _BARE_NUMBER.fullmatch(line.strip()):
                    removed_lines[key] += 1
                    continue
            kept.append(line)
        if not toc:
            for line in _edges(lines):
                if _HEADER_CHAPTER.match(line) and _edge_key(line) in headers:
                    heads_chapter = re.sub(r"\s+\d+\s*$", "", _clean_title(line))
                    break
        text = _normalize("\n".join(kept))
        if len(text) < config.OCR_MIN_CHARS or "intentionally left blank" in text.lower()[:200]:
            skipped["blank/near-empty"] += 1
            continue

        if has_labels:
            printed = labels[p - 1] or None
        elif use_offsets and offsets[p - 1] is not None and p - offsets[p - 1] >= 1:
            printed = str(p - offsets[p - 1])
        else:
            printed = None
        chapter, section = structure[p - 1]
        if not toc:
            chapter = heads_chapter
        rows.append(
            {
                "book_id": book["book_id"],
                "book_title": book["title"],
                "edition": book.get("edition", ""),
                "pdf_page": p,
                "printed_page": printed,
                "chapter": chapter,
                "section": section,
                "ocr": p in ocr_used,
                "text": text,
            }
        )

    if has_labels:
        method = "pdf page labels"
    elif use_offsets:
        distinct = sorted({o for o in offsets if o is not None})
        shown = ", ".join(map(str, distinct[:6])) + (" ..." if len(distinct) > 6 else "")
        method = f"read from header/footer numbers ({support:.0%} of pages confirmed; offsets {shown})"
    else:
        method = f"none found - citations use PDF page ({support:.0%} of pages had a usable number)"

    stats = {
        "book_id": book["book_id"],
        "title": book["title"],
        "pages_total": n,
        "pages_kept": len(rows),
        "pages_skipped": dict(skipped),
        "ocr_pages": len(ocr_used),
        "printed_page_method": method,
        "printed_page_coverage": round(sum(1 for r in rows if r["printed_page"]) / max(1, len(rows)), 3),
        "toc_entries": len(toc),
        "chapter_coverage": round(sum(1 for r in rows if r["chapter"]) / max(1, len(rows)), 3),
        "header_lines_removed": sum(removed_lines.values()),
        "top_removed_lines": removed_lines.most_common(12),
        "chars_kept": sum(len(r["text"]) for r in rows),
    }
    return {"rows": rows, "stats": stats}


def extract_all(only: list[str] | None = None, force: bool = False) -> None:
    config.LIBRARY_PAGES_DIR.mkdir(parents=True, exist_ok=True)
    books = load_manifest()
    if only:
        books = [b for b in books if b["book_id"] in set(only)]
    for k, book in enumerate(books, 1):
        out = pages_path(book["book_id"])
        if out.exists() and stats_path(book["book_id"]).exists() and not force:
            print(f"[{k}/{len(books)}] {book['book_id']}: already extracted, skipping")
            continue
        print(f"[{k}/{len(books)}] {book['book_id']}: reading {book['path'].name} ...")
        started = time.time()
        result = extract_book(book)
        tmp = out.with_suffix(".tmp")
        with tmp.open("w", encoding="utf-8") as handle:
            for row in result["rows"]:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        tmp.replace(out)
        st = result["stats"]
        stats_path(book["book_id"]).write_text(json.dumps(st, indent=2, ensure_ascii=False), encoding="utf-8")
        print(
            f"    kept {st['pages_kept']}/{st['pages_total']} pages, ocr={st['ocr_pages']}, "
            f"headers removed={st['header_lines_removed']}, printed pages: {st['printed_page_method']} "
            f"({time.time() - started:.0f}s)"
        )


# --- chunking (Phase 2) -----------------------------------------------------


def chunks_path(book_id: str) -> Path:
    return config.LIBRARY_CHUNKS_DIR / f"{book_id}.jsonl"


def chunk_book(rows: list[dict]) -> list[dict]:
    """Cleaned pages -> chunks, with the same sentence packing as the eval index
    (ingest.pack_windows: CHUNK_SIZE tokens, CHUNK_OVERLAP overlap)."""
    from .ingest import pack_windows, split_units

    # Chunks never cross a chapter boundary, so a chunk's chapter label is true
    # for all of its text (a chunk starting at the end of "52. Flatulence" and
    # running into "53. Polyuria and Polydipsia" was cited as Flatulence).
    groups: list[list[tuple[int, str, int]]] = []
    previous = object()
    for i, row in enumerate(rows):
        key = (row["chapter"], row["section"]) if _SPLIT_ON_SECTION else row["chapter"]
        if key != previous:
            groups.append([])
            previous = key
        for piece, tokens in split_units(row["text"], config.CHUNK_SIZE):
            groups[-1].append((i, piece, tokens))

    chunks = []
    for units in groups:
        for start, end, total in pack_windows([u[2] for u in units], config.CHUNK_SIZE, config.CHUNK_OVERLAP):
            chunks.append(_make_chunk(rows, units[start:end], total, len(chunks)))
    return chunks


_SPLIT_ON_SECTION = False  # sections are often a page or less - splitting there makes tiny chunks


def _make_chunk(rows: list[dict], window: list[tuple[int, str, int]], total: int, n: int) -> dict:
    first, last = rows[window[0][0]], rows[window[-1][0]]
    return {
        "chunk_id": f"{first['book_id']}_p{first['pdf_page']:05d}_{n:05d}",
        "chunker": CHUNKER_VERSION,
        "book_id": first["book_id"],
        "book_title": first["book_title"],
        "edition": first["edition"],
        # page/page_end = PDF pages, same meaning as in the eval index
        "page": first["pdf_page"],
        "page_end": last["pdf_page"],
        "printed_page": first["printed_page"],
        "printed_page_end": last["printed_page"],
        "chapter": first["chapter"],
        "section": first["section"],
        "ocr": any(rows[u[0]]["ocr"] for u in window),
        "text": " ".join(u[1] for u in window),
        "token_count": total,
    }


# Bump when chunk_book's output changes, so cached chunk files are rebuilt.
CHUNKER_VERSION = "2-chapter-boundaries"


def load_or_make_chunks(book_id: str) -> list[dict]:
    """Chunks for one book, rebuilt if its pages file is newer or the chunker changed."""
    out, src = chunks_path(book_id), pages_path(book_id)
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        with out.open(encoding="utf-8") as handle:
            cached = [json.loads(line) for line in handle if line.strip()]
        if cached and cached[0].get("chunker") == CHUNKER_VERSION:
            return cached
    chunks = chunk_book(load_pages(book_id))
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        for c in chunks:
            handle.write(json.dumps(c, ensure_ascii=False) + "\n")
    tmp.replace(out)
    return chunks


def load_all_chunks() -> list[dict]:
    out = []
    for book in load_manifest():
        out.extend(load_or_make_chunks(book["book_id"]))
    return out
