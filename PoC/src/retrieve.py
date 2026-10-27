"""Retrieval lane: question -> embedding -> top-k book passages.

The PoC's single DAT lane. Returns passages carrying their provenance
(chunk_id, book, page) so every downstream stage can cite them.
"""

from __future__ import annotations

import config

from . import embeddings
from .embed_index import get_collection


def retrieve(question: str, top_k: int | None = None) -> list[dict]:
    top_k = top_k or config.TOP_K
    collection = get_collection()

    available = collection.count()
    if available == 0:
        raise RuntimeError(
            "The vector index is empty. Build it first: python -m src.embed_index"
        )

    result = collection.query(
        query_embeddings=[embeddings.embed_one(question)],
        n_results=min(top_k, available),
        include=["documents", "metadatas", "distances"],
    )

    passages: list[dict] = []
    for position, chunk_id in enumerate(result["ids"][0]):
        meta = result["metadatas"][0][position] or {}
        distance = float(result["distances"][0][position])
        passages.append(
            {
                "chunk_id": chunk_id,
                "text": result["documents"][0][position],
                "book_title": meta.get("book_title", "unknown"),
                "page": meta.get("page"),
                "page_end": meta.get("page_end"),
                "similarity": round(max(0.0, 1.0 - distance), 4),
            }
        )
    return passages
