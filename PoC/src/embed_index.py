"""Build the vector index: PDFs -> chunks -> embeddings -> ChromaDB.

    python -m src.embed_index                     # eval2: rebuild the 2-book index from scratch
    python -m src.embed_index --profile library   # all 17 books, RESUMABLE

The library build never wipes the collection: per book it adds only the chunk
ids that are not in the index yet (and removes ids that no longer exist), so a
crash or Ctrl+C part-way through just continues on the next run. --reset forces
a full rebuild of the library collection.
"""

from __future__ import annotations

import argparse
import time
from concurrent.futures import ThreadPoolExecutor

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


# --- full library (resumable) ----------------------------------------------

_META_KEYS = (
    "book_id", "book_title", "edition", "page", "page_end",
    "printed_page", "printed_page_end", "chapter", "section", "ocr",
)


def _fingerprint(chunk: dict) -> str:
    """Hash of everything stored for a chunk: if the text or any metadata changes,
    the vector is rebuilt even though the chunk_id stayed the same."""
    import hashlib
    import json

    payload = json.dumps([chunk["text"]] + [chunk.get(k) for k in _META_KEYS], ensure_ascii=False)
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]


def _meta(chunk: dict) -> dict:
    # Chroma metadata values must be str/int/float/bool - None becomes "".
    meta = {k: ("" if chunk.get(k) is None else chunk[k]) for k in _META_KEYS}
    meta["fp"] = _fingerprint(chunk)
    return meta


def build_library_index(only: list[str] | None = None, reset: bool = False, workers: int = 4):
    from . import library

    client = _client()
    if reset:
        try:
            client.delete_collection(config.CHROMA_COLLECTION)
            print(f"  --reset: deleted collection {config.CHROMA_COLLECTION}")
        except Exception:
            pass
    collection = client.get_or_create_collection(
        name=config.CHROMA_COLLECTION, metadata={"hnsw:space": "cosine"}
    )

    books = library.load_manifest()
    if only:
        books = [b for b in books if b["book_id"] in set(only)]
    started = time.time()
    for k, book in enumerate(books, 1):
        bid = book["book_id"]
        if not library.stats_path(bid).exists():
            print(f"[{k}/{len(books)}] {bid}: pages not extracted yet - extracting ...")
            library.extract_all(only=[bid])
        chunks = library.load_or_make_chunks(bid)
        wanted = {c["chunk_id"]: _fingerprint(c) for c in chunks}
        got = collection.get(where={"book_id": bid}, include=["metadatas"])
        # current = present AND unchanged; anything else is stale and re-embedded
        have = {i for i, m in zip(got["ids"], got["metadatas"]) if wanted.get(i) == (m or {}).get("fp")}
        stale = sorted(set(got["ids"]) - have)
        if stale:
            for i in range(0, len(stale), 5000):
                collection.delete(ids=stale[i : i + 5000])
            print(f"[{k}/{len(books)}] {bid}: removed {len(stale):,} stale vectors")
        todo = [c for c in chunks if c["chunk_id"] not in have]
        if not todo:
            print(f"[{k}/{len(books)}] {bid}: all {len(chunks):,} chunks already indexed, skipping")
            continue
        print(f"[{k}/{len(books)}] {bid}: embedding {len(todo):,} of {len(chunks):,} chunks ...")
        batches = [todo[i : i + _INDEX_BATCH] for i in range(0, len(todo), _INDEX_BATCH)]
        done = 0
        # Embedding calls run in parallel threads; Chroma writes stay on this thread.
        with ThreadPoolExecutor(max_workers=workers) as pool:
            vectors_iter = pool.map(lambda part: embeddings.embed_texts([c["text"] for c in part]), batches)
            for part, vectors in zip(batches, vectors_iter):
                collection.add(
                    ids=[c["chunk_id"] for c in part],
                    embeddings=vectors,
                    documents=[c["text"] for c in part],
                    metadatas=[_meta(c) for c in part],
                )
                done += len(part)
                if done % 1024 < _INDEX_BATCH or done == len(todo):
                    print(f"    {done:,}/{len(todo):,}  ({time.time() - started:.0f}s elapsed)")
    return collection


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the vector index.")
    parser.add_argument("--profile", choices=list(config.PROFILES), default=config.KB_PROFILE)
    parser.add_argument("--only", nargs="*", help="library: only these book_ids")
    parser.add_argument("--reset", action="store_true", help="library: wipe and rebuild the collection")
    parser.add_argument("--workers", type=int, default=4, help="library: parallel embedding requests")
    args = parser.parse_args()
    config.set_profile(args.profile)
    config.ensure_dirs()

    if args.profile == "library":
        print(f"Building library index -> {config.INDEX_DIR} (collection '{config.CHROMA_COLLECTION}')")
        built = build_library_index(only=args.only, reset=args.reset, workers=args.workers)
        print(f"\nDone. Collection '{config.CHROMA_COLLECTION}' holds {built.count():,} vectors.")
        return

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


if __name__ == "__main__":
    main()
