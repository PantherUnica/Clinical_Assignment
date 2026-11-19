"""One place that turns a passage/citation into a human-readable source label.

Library passages (they carry `book_id`):
    Plumb's Veterinary Drug Handbook, Systemic Monographs › Carvedilol, p. 580
    Ettinger's Textbook of Veterinary Internal Medicine, Urogenital › 53. Polyuria and Polydipsia, PDF p. 1149
  - printed page when the book prints one, otherwise "PDF p." so nobody mistakes
    a PDF page for a book page.

Eval2 passages (no `book_id`) keep the original format exactly, so the 2-book
baseline prompts and reports do not change:
    Blackwell's Five Minute Veterinary Consult   Canine and Feline, p.12
"""

from __future__ import annotations


def is_library(item: dict) -> bool:
    return bool(item.get("book_id"))


def page_label(item: dict) -> str:
    if not is_library(item):
        if item.get("page") == item.get("page_end") or item.get("page_end") is None:
            return f"p.{item.get('page')}"
        return f"pp.{item['page']}-{item['page_end']}"
    start, end = item.get("printed_page"), item.get("printed_page_end")
    if start:
        return f"p. {start}" if not end or end == start else f"pp. {start}–{end}"
    start, end = item.get("page"), item.get("page_end")
    return f"PDF p. {start}" if not end or end == start else f"PDF pp. {start}–{end}"


def location_label(item: dict) -> str:
    """'Chapter › Section' (either part may be missing)."""
    parts = [item.get("chapter"), item.get("section")]
    return " › ".join(p for p in parts if p)


def source_label(item: dict) -> str:
    parts = [item.get("book_title", "unknown"), location_label(item), page_label(item)]
    return ", ".join(p for p in parts if p)
