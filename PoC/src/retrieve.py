"""Retrieval lane: question -> embedding -> top-k book passages.

The PoC's single DAT lane. Returns passages carrying their provenance
(chunk_id, book, page - and, on the library profile, chapter, section and
printed page) so every downstream stage can cite them.

Optional per-book cap (MAX_PER_BOOK / max_per_book): at most N passages from
any one book, so a 9,000-page book cannot fill the whole top-k. Off (0) by
default; whether it helps gets measured in the multi-book testing plan.
"""

from __future__ import annotations

import config

from . import embeddings
from .embed_index import get_collection

# Extra metadata stored on library chunks. Chroma stores missing values as "".
_LIBRARY_KEYS = ("book_id", "edition", "chapter", "section", "printed_page", "printed_page_end", "ocr")
_CAP_OVERFETCH = 5  # with a cap on, fetch top_k * this many candidates to choose from


def retrieve(question: str, top_k: int | None = None, max_per_book: int | None = None) -> list[dict]:
    top_k = top_k or config.TOP_K
    max_per_book = config.MAX_PER_BOOK if max_per_book is None else max_per_book
    collection = get_collection()

    available = collection.count()
    if available == 0:
        raise RuntimeError(
            "The vector index is empty. Build it first: python -m src.embed_index"
        )

    n_fetch = top_k * _CAP_OVERFETCH if max_per_book else top_k
    result = collection.query(
        query_embeddings=[embeddings.embed_one(question)],
        n_results=min(n_fetch, available),
        include=["documents", "metadatas", "distances"],
    )

    passages: list[dict] = []
    per_book: dict[str, int] = {}
    for position, chunk_id in enumerate(result["ids"][0]):
        meta = result["metadatas"][0][position] or {}
        book = meta.get("book_title", "unknown")
        if max_per_book and per_book.get(book, 0) >= max_per_book:
            continue
        per_book[book] = per_book.get(book, 0) + 1
        distance = float(result["distances"][0][position])
        passage = {
            "chunk_id": chunk_id,
            "text": result["documents"][0][position],
            "book_title": book,
            "page": meta.get("page"),
            "page_end": meta.get("page_end"),
            "similarity": round(max(0.0, 1.0 - distance), 4),
        }
        for key in _LIBRARY_KEYS:
            if key in meta:
                passage[key] = meta[key] if meta[key] != "" else None
        passages.append(passage)
        if len(passages) >= top_k:
            break
    return passages
