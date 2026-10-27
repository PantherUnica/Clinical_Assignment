"""Build the vector index: PDFs -> chunks.jsonl -> embeddings -> ChromaDB.

Run this once (and again whenever you change the books or the chunk settings):
    python -m src.embed_index
"""

from __future__ import annotations

import chromadb

import config

from . import embeddings, ingest

_INDEX_BATCH = 128


def _client():
    config.INDEX_DIR.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(config.INDEX_DIR))


def get_collection():
    """The collection used for retrieval. Created empty if it does not exist."""
    return _client().get_or_create_collection(
        name=config.CHROMA_COLLECTION, metadata={"hnsw:space": "cosine"}
    )


def build_index(chunks: list[dict] | None = None, reset: bool = True):
    client = _client()
    if reset:
        try:
            client.delete_collection(config.CHROMA_COLLECTION)
        except Exception:
            pass  # nothing to delete on a first run
    collection = client.get_or_create_collection(
        name=config.CHROMA_COLLECTION, metadata={"hnsw:space": "cosine"}
    )

    chunks = ingest.load_chunks() if chunks is None else chunks
    for i in range(0, len(chunks), _INDEX_BATCH):
        part = chunks[i : i + _INDEX_BATCH]
        texts = [c["text"] for c in part]
        collection.add(
            ids=[c["chunk_id"] for c in part],
            embeddings=embeddings.embed_texts(texts),
            documents=texts,
            metadatas=[
                {
                    "book_title": c["book_title"],
                    "page": c["page"],
                    "page_end": c["page_end"],
                }
                for c in part
            ],
        )
        print(f"  indexed {min(i + _INDEX_BATCH, len(chunks)):,}/{len(chunks):,}")
    return collection


if __name__ == "__main__":
    config.ensure_dirs()
    print("1/2  Ingesting PDFs ...")
    produced = ingest.ingest_all()
    ingest.write_chunks(produced)
    print(f"     {len(produced):,} chunks -> {config.CHUNKS_PATH}")

    print("2/2  Embedding + indexing ...")
    built = build_index(produced)
    print(
        f"\nDone. Collection '{config.CHROMA_COLLECTION}' holds {built.count():,} vectors "
        f"({config.EMBED_PROVIDER})."
    )
