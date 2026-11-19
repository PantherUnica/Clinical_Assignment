"""Check citations against the ORIGINAL PDFs (checklist §4: "verify every citation against
the original PDF", "check that cited page numbers are correct").

For every verified claim and each chunk it cites:
  - supported   : the claim's content words are on the cited PDF page(s), read fresh
                  from the PDF (OCR cache for scanned books) - not from our chunk text.
  - page_ok     : the printed page we show is the page's PDF label, or the number
                  printed in its header/footer. None when the book prints no numbers.
"""

from __future__ import annotations

import re
from functools import lru_cache

try:
    import pymupdf
except ImportError:
    import fitz as pymupdf

import config
from src import library
from src.verify import lexical_coverage

SUPPORT_MIN = 0.5  # share of the claim's content words found on the cited pages


@lru_cache(maxsize=None)
def _book(book_id: str) -> dict:
    return {b["book_id"]: b for b in library.load_manifest()}[book_id]


@lru_cache(maxsize=4096)
def raw_page(book_id: str, pdf_page: int) -> tuple[str, str]:
    """(text, label) of one page, straight from the PDF (or the OCR cache for force_ocr books)."""
    book = _book(book_id)
    doc = pymupdf.open(book["path"])
    try:
        page = doc[pdf_page - 1]
        label = page.get_label() or ""
        text = page.get_text("text") or ""
    finally:
        doc.close()
    ocr_file = library._ocr_cache_file(book_id, pdf_page)
    if (book.get("force_ocr") or len(text.strip()) < config.OCR_MIN_CHARS) and ocr_file.exists():
        text = ocr_file.read_text(encoding="utf-8")
    return text, label


def _edge_numbers(book_id: str, pdf_page: int) -> list[str]:
    text, _ = raw_page(book_id, pdf_page)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return re.findall(r"\d{1,4}", " ".join(lines[:3] + lines[-3:]))


def printed_page_ok(book_id: str, pdf_page: int, printed: str | None) -> bool | None:
    """True = confirmed, False = contradicted, None = cannot be verified (or no printed page).

    Figure-only pages often print no number; then a neighbour that prints
    printed±1 confirms it. A page with numbers that disagree is a contradiction.
    """
    if not printed:
        return None
    _, label = raw_page(book_id, pdf_page)
    if label:
        return label == printed
    here = _edge_numbers(book_id, pdf_page)
    if printed in here:
        return True
    if printed.isdigit():
        n = int(printed)
        for delta in (-1, 1):
            try:
                if str(n + delta) in _edge_numbers(book_id, pdf_page + delta):
                    return True
            except (IndexError, ValueError):
                continue
    plausible = [int(x) for x in here if x.isdigit() and abs(int(x) - pdf_page) < 200]
    return False if plausible else None


def check_claim(claim_text: str, passage: dict) -> dict:
    book_id, start, end = passage["book_id"], passage["page"], passage["page_end"]
    text = " ".join(raw_page(book_id, p)[0] for p in range(start, end + 1))
    coverage = lexical_coverage(claim_text, text)
    return {
        "chunk_id": passage["chunk_id"],
        "book_id": book_id,
        "pdf_pages": [start, end],
        "printed_page": passage.get("printed_page"),
        "coverage": round(coverage, 3),
        "supported": coverage >= SUPPORT_MIN,
        "page_ok": printed_page_ok(book_id, start, passage.get("printed_page")),
    }


def check_result(verified: list[dict], passages: list[dict]) -> list[dict]:
    by_id = {p["chunk_id"]: p for p in passages}
    out = []
    for claim in verified:
        for cid in claim.get("sources") or []:
            if cid in by_id:
                row = check_claim(claim["text"], by_id[cid])
                row["claim"] = claim["text"]
                out.append(row)
    return out
