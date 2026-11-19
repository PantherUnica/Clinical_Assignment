"""Exact (brute-force) cosine search over the library index - for reproducible eval numbers.

Chroma's HNSW search is approximate: the same query on the same index can return
different results at deep ranks from run to run (seen in Phase 3: ~10% of
questions differ in the top-50). For testing we score every vector instead, so
the same input always gives the same ranking. The app keeps using Chroma.

The vectors are pulled from the Chroma collection once and cached in
eval/.cache/ (invalidated automatically when any chunk's fingerprint changes).
Passages come back in exactly the shape src.retrieve returns.
"""

from __future__ import annotations

import hashlib
import json

import numpy as np

import config

from . import cache as emb_cache

CACHE_DIR = emb_cache.DEFAULT_PATH.parent
_LIBRARY_KEYS = ("book_id", "edition", "chapter", "section", "printed_page", "printed_page_end", "ocr")


class ExactIndex:
    def __init__(self, profile: str = "library"):
        config.set_profile(profile)
        from src.embed_index import get_collection

        col = get_collection()
        self.ids: list[str] = []
        self.metas: list[dict] = []
        self.docs: list[str] = []
        total = col.count()
        for offset in range(0, total, 5000):
            part = col.get(limit=5000, offset=offset, include=["metadatas", "documents"])
            self.ids += part["ids"]
            self.metas += part["metadatas"]
            self.docs += part["documents"]
        # Fingerprint of the whole index: ids + per-chunk fp (text+metadata hash).
        digest = hashlib.sha1(
            json.dumps(sorted(zip(self.ids, [m.get("fp", "") for m in self.metas]))).encode()
        ).hexdigest()[:16]
        path = CACHE_DIR / f"exact_{profile}_{digest}.npy"
        order_path = path.with_suffix(".ids.json")
        if path.exists() and order_path.exists():
            cached_ids = json.loads(order_path.read_text(encoding="utf-8"))
            pos = {cid: i for i, cid in enumerate(cached_ids)}
            matrix = np.load(path)[[pos[i] for i in self.ids]]
        else:
            rows = []
            for offset in range(0, total, 2000):
                part = col.get(limit=2000, offset=offset, include=["embeddings"])
                rows.append((part["ids"], np.asarray(part["embeddings"], dtype=np.float32)))
            pos = {cid: i for i, cid in enumerate(self.ids)}
            matrix = np.zeros((total, rows[0][1].shape[1]), dtype=np.float32)
            for ids, emb in rows:
                matrix[[pos[i] for i in ids]] = emb
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            np.save(path, matrix)
            order_path.write_text(json.dumps(self.ids), encoding="utf-8")
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        self.matrix = matrix / np.where(norms == 0, 1, norms)
        self.book_titles = [m.get("book_title", "unknown") for m in self.metas]
        self.digest = digest

    def search(self, question: str, top_k: int = 6, max_per_book: int = 0) -> list[dict]:
        emb_cache.install()
        from src import embeddings

        q = np.asarray(embeddings.embed_one(question), dtype=np.float32)
        q /= np.linalg.norm(q) or 1.0
        sims = self.matrix @ q
        # Stable tie-break on chunk id so the order never depends on memory layout.
        order = sorted(range(len(sims)), key=lambda i: (-float(sims[i]), self.ids[i]))[: max(top_k * 10, 200)]
        out, per_book = [], {}
        for i in order:
            book = self.book_titles[i]
            if max_per_book and per_book.get(book, 0) >= max_per_book:
                continue
            per_book[book] = per_book.get(book, 0) + 1
            meta = self.metas[i]
            passage = {
                "chunk_id": self.ids[i],
                "text": self.docs[i],
                "book_title": book,
                "page": meta.get("page"),
                "page_end": meta.get("page_end"),
                "similarity": round(float(sims[i]), 4),
            }
            for key in _LIBRARY_KEYS:
                if key in meta:
                    passage[key] = meta[key] if meta[key] != "" else None
            out.append(passage)
            if len(out) >= top_k:
                break
        return out
