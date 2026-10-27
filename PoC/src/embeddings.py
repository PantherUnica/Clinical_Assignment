"""Embedding provider: OpenAI (default) or local sentence-transformers.

Used by indexing, retrieval and the verification gate, so every stage compares
vectors from the same model.
"""

from __future__ import annotations

import config

_openai_client = None
_local_model = None


def _openai():
    global _openai_client
    if _openai_client is None:
        from openai import OpenAI

        if not config.OPENAI_API_KEY:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Copy PoC/.env.example to PoC/.env and add your key."
            )
        # Retry transient connection blips rather than surfacing them as failures.
        _openai_client = OpenAI(
            api_key=config.OPENAI_API_KEY,
            max_retries=config.API_MAX_RETRIES,
            timeout=config.API_TIMEOUT_SECONDS,
        )
    return _openai_client


def _local():
    global _local_model
    if _local_model is None:
        from sentence_transformers import SentenceTransformer

        _local_model = SentenceTransformer(config.LOCAL_EMBED_MODEL)
    return _local_model


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed a list of texts. Order of the result matches the input."""
    if not texts:
        return []

    # Embedding APIs reject empty strings.
    clean = [t if t and t.strip() else " " for t in texts]

    if config.EMBED_PROVIDER == "local":
        vectors = _local().encode(clean, normalize_embeddings=True)
        return [list(map(float, v)) for v in vectors]

    client = _openai()
    out: list[list[float]] = []
    for i in range(0, len(clean), config.EMBED_BATCH_SIZE):
        batch = clean[i : i + config.EMBED_BATCH_SIZE]
        resp = client.embeddings.create(model=config.OPENAI_EMBED_MODEL, input=batch)
        out.extend(item.embedding for item in resp.data)
    return out


def embed_one(text: str) -> list[float]:
    return embed_texts([text])[0]


def cosine(a: list[float], b: list[float]) -> float:
    """Cosine similarity, clamped to [0, 1] for use as a support score."""
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    if na == 0 or nb == 0:
        return 0.0
    return max(0.0, min(1.0, dot / (na * nb)))
