"""On-disk embedding cache for eval runs.

install() swaps src.embeddings.embed_texts for a caching wrapper at runtime.
retrieve.py, verify.py and embed_one() all resolve embed_texts through that
module attribute at call time, so the whole pipeline is cached without editing
src/. Re-running the eval then costs no new embedding calls for text already seen.
Vectors are stored as float32 - well within cosine-similarity tolerance.
"""

from __future__ import annotations

import hashlib
import sqlite3
import threading
from array import array
from pathlib import Path

import config
from src import embeddings

DEFAULT_PATH = Path(__file__).resolve().parent / ".cache" / "embeddings.sqlite"


def _model_name() -> str:
    if config.EMBED_PROVIDER == "local":
        return f"local:{config.LOCAL_EMBED_MODEL}"
    return f"openai:{config.OPENAI_EMBED_MODEL}"


class EmbeddingCache:
    def __init__(self, path: Path = DEFAULT_PATH):
        path.parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(path, check_same_thread=False)
        self._db.execute("CREATE TABLE IF NOT EXISTS vec (key TEXT PRIMARY KEY, data BLOB)")
        self._lock = threading.Lock()
        self._model = _model_name()
        self.hits = 0
        self.misses = 0

    def key(self, text: str) -> str:
        return hashlib.sha256(f"{self._model}\x00{text}".encode("utf-8")).hexdigest()

    def get_many(self, keys: list[str]) -> dict[str, list[float]]:
        found: dict[str, list[float]] = {}
        with self._lock:
            for start in range(0, len(keys), 500):
                batch = keys[start : start + 500]
                marks = ",".join("?" * len(batch))
                for key, blob in self._db.execute(
                    f"SELECT key, data FROM vec WHERE key IN ({marks})", batch
                ):
                    found[key] = array("f", blob).tolist()
        return found

    def put_many(self, items: dict[str, list[float]]) -> None:
        with self._lock:
            self._db.executemany(
                "INSERT OR REPLACE INTO vec (key, data) VALUES (?, ?)",
                [(k, array("f", v).tobytes()) for k, v in items.items()],
            )
            self._db.commit()


_installed: EmbeddingCache | None = None


def install(path: Path = DEFAULT_PATH) -> EmbeddingCache:
    """Route all embedding calls through the cache. Idempotent."""
    global _installed
    if _installed is not None:
        return _installed

    cache = EmbeddingCache(path)
    original = embeddings.embed_texts

    def cached_embed_texts(texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        keys = [cache.key(t) for t in texts]
        found = cache.get_many(list(set(keys)))
        missing: dict[str, str] = {}
        for key, text in zip(keys, texts):
            if key not in found and key not in missing:
                missing[key] = text
        if missing:
            fresh = dict(zip(missing.keys(), original(list(missing.values()))))
            cache.put_many(fresh)
            found.update(fresh)
        with cache._lock:
            cache.misses += len(missing)
            cache.hits += len(texts) - len(missing)
        return [found[k] for k in keys]

    embeddings.embed_texts = cached_embed_texts
    _installed = cache
    return cache
