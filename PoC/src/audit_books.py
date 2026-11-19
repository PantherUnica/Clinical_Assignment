"""Book audit report (checklist §1): is every PDF readable and complete?

    python -m src.audit_books            -> reports/book_audit.md

Part A reads every PDF in books/ (including skipped ones): opens?, pages,
text-layer coverage, image-only pages, page labels, TOC size, md5, duplicates.
Part B summarises the cleaning results from data/library/pages/*.stats.json
(written by `python -m src.ingest --profile library`).
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from collections import defaultdict

try:
    import pymupdf
except ImportError:
    import fitz as pymupdf

import config

from . import library


def _md5(path) -> str:
    h = hashlib.md5()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def audit_pdf(path) -> dict:
    row = {"file": path.name, "mb": round(path.stat().st_size / 1e6, 1), "md5": _md5(path)}
    try:
        doc = pymupdf.open(path)
    except Exception as exc:
        row.update(opens=False, error=str(exc))
        return row
    try:
        n = doc.page_count
        text_pages = labelled = 0
        broken = 0
        for page in doc:
            try:
                if len((page.get_text("text") or "").strip()) >= config.OCR_MIN_CHARS:
                    text_pages += 1
            except Exception:
                broken += 1
            if page.get_label():
                labelled += 1
        row.update(
            opens=True,
            pages=n,
            text_pages=text_pages,
            image_only=n - text_pages - broken,
            unreadable_pages=broken,
            labelled=labelled,
            toc=len(doc.get_toc()),
            encrypted=doc.is_encrypted,
        )
    finally:
        doc.close()
    return row


def _short(text: str, n: int = 48) -> str:
    return text if len(text) <= n else text[: n - 1] + "…"


def build_report() -> str:
    books = library.load_manifest(include_skipped=True)
    print(f"Auditing {len(books)} PDFs ...")
    audits = {}
    for b in books:
        print(f"  {b['book_id']}")
        audits[b["book_id"]] = audit_pdf(b["path"])

    by_md5 = defaultdict(list)
    for b in books:
        by_md5[audits[b["book_id"]]["md5"]].append(b["book_id"])

    lines = [
        "# Book audit",
        "",
        f"Generated {dt.datetime.now():%Y-%m-%d %H:%M}. Source list: `books/library_manifest.json`.",
        "",
        "## A. Are the PDFs readable and complete?",
        "",
        "| Book | Pages | Opens | Text-layer pages | Image-only pages | Page labels | TOC entries | Size MB | Status |",
        "|---|---:|:---:|---:|---:|---:|---:|---:|---|",
    ]
    for b in books:
        a = audits[b["book_id"]]
        if not a.get("opens"):
            lines.append(f"| {_short(b['title'])} | - | NO | - | - | - | - | {a['mb']} | **cannot open**: {a['error']} |")
            continue
        dupes = [x for x in by_md5[a["md5"]] if x != b["book_id"]]
        if b.get("skip"):
            status = f"skipped - {b.get('skip_reason', '')}"
        elif a["image_only"] > 0.5 * a["pages"]:
            status = "scanned - OCR'd"
        elif a["image_only"]:
            status = f"OK ({a['image_only']} image pages OCR'd)"
        else:
            status = "OK"
        if dupes and not b.get("skip"):
            status += f" (identical to {', '.join(dupes)})"
        lines.append(
            f"| {_short(b['title'])} | {a['pages']:,} | yes | {a['text_pages']:,} | {a['image_only']:,} | "
            f"{a['labelled']:,} | {a['toc']:,} | {a['mb']} | {status} |"
        )

    lines += [
        "",
        "## B. Cleaning and metadata results (books that get indexed)",
        "",
        "| Book | Pages kept / total | OCR pages | Header/footer lines removed | Printed page numbers | Printed-page coverage | Chapter coverage |",
        "|---|---:|---:|---:|---|---:|---:|",
    ]
    total_kept = total_pages = total_chars = 0
    notes = []
    for b in books:
        if b.get("skip"):
            continue
        sp = library.stats_path(b["book_id"])
        if not sp.exists():
            lines.append(f"| {_short(b['title'])} | not extracted yet | | | | | |")
            continue
        s = json.loads(sp.read_text(encoding="utf-8"))
        total_kept += s["pages_kept"]
        total_pages += s["pages_total"]
        total_chars += s["chars_kept"]
        lines.append(
            f"| {_short(b['title'])} | {s['pages_kept']:,} / {s['pages_total']:,} | {s['ocr_pages']:,} | "
            f"{s['header_lines_removed']:,} | {s['printed_page_method']} | {s['printed_page_coverage']:.0%} | "
            f"{s['chapter_coverage']:.0%} |"
        )
        skipped = ", ".join(f"{k} ({v})" for k, v in sorted(s["pages_skipped"].items(), key=lambda kv: -kv[1]))
        removed = ", ".join(f"`{k[:40]}` ×{c}" for k, c in s["top_removed_lines"][:5])
        notes.append(f"- **{b['title']}** — pages dropped: {skipped or 'none'}. Most-removed lines: {removed or 'none'}.")
    lines += [
        "",
        f"**Total:** {total_kept:,} of {total_pages:,} pages kept, ~{total_chars / 4 / 1e6:.1f}M tokens of text "
        f"(≈ {total_chars / 4 / 500 / 1000:.0f}k chunks at stride 500).",
        "",
        "### What was dropped, per book",
        "",
        *notes,
        "",
        "### Known limitations",
        "",
        "- **OCR text** (Muller & Kirk, and the Color Atlas whose built-in text layer is itself old OCR) contains "
        "spelling errors; chunks from OCR'd pages carry `ocr: true`.",
        "- **Printed page = None** means the book shows no page numbers we could read; citations then show the PDF page.",
        "- **Chapter = None** means the PDF has no bookmarks (TOC) and no recognisable running head.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    config.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = config.REPORTS_DIR / "book_audit.md"
    out.write_text(build_report(), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
