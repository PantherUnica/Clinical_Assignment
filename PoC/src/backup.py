"""Back up and restore the vector store (Chroma index + chunks).

    python -m src.backup create <name> [--profile library]   # zip index + chunks + manifest
    python -m src.backup list                     # show all backups
    python -m src.backup verify <folder>          # check zip integrity + counts
    python -m src.backup restore <folder> [--force]

Backups go to PoC/backups/vector_store/<date>_<name>/ :
    index.zip      - the Chroma persistent directory
    chunks.zip     - chunks.jsonl (or the per-book chunks folder)
    manifest.json  - embedding model, chunk settings, per-book chunk counts,
                     book file hashes, sha256 of both zips

`restore` never overwrites silently: without --force it refuses if the target
already exists; with --force the current copy is moved aside, not deleted.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import shutil
import sys
import zipfile
from collections import Counter
from pathlib import Path

import config

BACKUP_ROOT = config.POC_ROOT / "backups" / "vector_store"


def _sha256(path: Path, block: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(block), b""):
            h.update(chunk)
    return h.hexdigest()


def _zip_path(source: Path, destination: Path) -> int:
    """Zip a file or a directory; returns the number of files written."""
    count = 0
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        if source.is_file():
            zf.write(source, source.name)
            return 1
        for file in sorted(source.rglob("*")):
            if file.is_file():
                zf.write(file, file.relative_to(source).as_posix())
                count += 1
    return count


def _iter_chunks(source: Path):
    files = [source] if source.is_file() else sorted(source.glob("*.jsonl"))
    for file in files:
        with file.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    yield json.loads(line)


def _book_hashes() -> list[dict]:
    rows = []
    for pdf in sorted(config.BOOKS_DIR.rglob("*.pdf")):
        rows.append(
            {
                "file": pdf.relative_to(config.POC_ROOT).as_posix(),
                "bytes": pdf.stat().st_size,
                "md5": hashlib.md5(pdf.read_bytes()).hexdigest(),
            }
        )
    return rows


def _collection_count(index_dir: Path, collection: str) -> int | None:
    try:
        import chromadb

        client = chromadb.PersistentClient(path=str(index_dir))
        return client.get_collection(collection).count()
    except Exception as exc:  # report, don't fail the backup over it
        print(f"  [warn] could not open collection to count vectors: {exc}")
        return None


def create(name: str, index_dir: Path, chunks_src: Path, collection: str) -> Path:
    if not index_dir.exists():
        sys.exit(f"Index folder not found: {index_dir}")
    if not chunks_src.exists():
        sys.exit(f"Chunks not found: {chunks_src}")

    folder = BACKUP_ROOT / f"{dt.date.today().isoformat()}_{name}"
    if folder.exists():
        sys.exit(f"Backup already exists: {folder}  (pick another name)")
    folder.mkdir(parents=True)

    print(f"Backing up to {folder}")
    print("  zipping index ...")
    n_index_files = _zip_path(index_dir, folder / "index.zip")
    print("  zipping chunks ...")
    _zip_path(chunks_src, folder / "chunks.zip")

    per_book = Counter(c["book_title"] for c in _iter_chunks(chunks_src))
    manifest = {
        "name": name,
        "created": dt.datetime.now().isoformat(timespec="seconds"),
        "source": {
            "index_dir": index_dir.relative_to(config.POC_ROOT).as_posix(),
            "chunks": chunks_src.relative_to(config.POC_ROOT).as_posix(),
            "chunks_is_dir": chunks_src.is_dir(),
            "collection": collection,
        },
        "embedding": {
            "provider": config.EMBED_PROVIDER,
            "model": config.OPENAI_EMBED_MODEL
            if config.EMBED_PROVIDER == "openai"
            else config.LOCAL_EMBED_MODEL,
        },
        "chunking": {"chunk_size": config.CHUNK_SIZE, "chunk_overlap": config.CHUNK_OVERLAP},
        "counts": {
            "chunks": sum(per_book.values()),
            "vectors": _collection_count(index_dir, collection),
            "index_files": n_index_files,
            "per_book": dict(sorted(per_book.items())),
        },
        "zips": {
            "index.zip": _sha256(folder / "index.zip"),
            "chunks.zip": _sha256(folder / "chunks.zip"),
        },
        "books": _book_hashes(),
    }
    (folder / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        f"Done. chunks={manifest['counts']['chunks']:,} vectors={manifest['counts']['vectors']}"
    )
    return folder


def _resolve(folder: str) -> Path:
    path = Path(folder)
    if not path.is_absolute() and not path.exists():
        path = BACKUP_ROOT / folder
    if not (path / "manifest.json").exists():
        sys.exit(f"Not a backup folder (no manifest.json): {path}")
    return path


def verify(folder: str) -> bool:
    path = _resolve(folder)
    manifest = json.loads((path / "manifest.json").read_text(encoding="utf-8"))
    ok = True
    for zname, expected in manifest["zips"].items():
        actual = _sha256(path / zname)
        good = actual == expected
        with zipfile.ZipFile(path / zname) as zf:
            bad = zf.testzip()
        print(f"  {zname}: sha256 {'OK' if good else 'MISMATCH'}, zip {'OK' if bad is None else 'CORRUPT: ' + bad}")
        ok &= good and bad is None
    n = 0
    with zipfile.ZipFile(path / "chunks.zip") as zf:
        for member in zf.namelist():
            with zf.open(member) as handle:
                n += sum(1 for line in handle if line.strip())
    expected = manifest["counts"]["chunks"]
    print(f"  chunks in zip: {n:,} (manifest says {expected:,}) {'OK' if n == expected else 'MISMATCH'}")
    ok &= n == expected
    print("VERIFIED" if ok else "PROBLEM FOUND")
    return ok


def list_backups() -> None:
    if not BACKUP_ROOT.exists():
        print("No backups yet.")
        return
    for folder in sorted(BACKUP_ROOT.iterdir()):
        mf = folder / "manifest.json"
        if not mf.exists():
            continue
        m = json.loads(mf.read_text(encoding="utf-8"))
        size = sum(f.stat().st_size for f in folder.iterdir()) / 1e6
        print(
            f"{folder.name:40s} chunks={m['counts']['chunks']:>7,} vectors={m['counts']['vectors']} "
            f"books={len(m['counts']['per_book'])} {size:,.0f} MB  ({m['embedding']['model']})"
        )


def restore(folder: str, force: bool) -> None:
    path = _resolve(folder)
    if not verify(folder):
        sys.exit("Backup failed verification - not restoring.")
    manifest = json.loads((path / "manifest.json").read_text(encoding="utf-8"))
    src = manifest["source"]
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    targets = [
        ("index.zip", config.POC_ROOT / src["index_dir"], True),
        ("chunks.zip", config.POC_ROOT / src["chunks"], src["chunks_is_dir"]),
    ]
    for _, target, _ in targets:
        if target.exists() and not force:
            sys.exit(f"{target} already exists. Re-run with --force (it will be moved aside, not deleted).")
    for zname, target, is_dir in targets:
        if target.exists():
            aside = target.with_name(f"{target.name}.before_restore_{stamp}")
            shutil.move(str(target), str(aside))
            print(f"  moved current {target.name} -> {aside.name}")
        with zipfile.ZipFile(path / zname) as zf:
            zf.extractall(target if is_dir else target.parent)
        print(f"  restored {target}")
    print("Restore done.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("create")
    c.add_argument("name")
    c.add_argument("--profile", choices=list(config.PROFILES), default=config.KB_PROFILE)
    sub.add_parser("list")
    v = sub.add_parser("verify")
    v.add_argument("folder")
    r = sub.add_parser("restore")
    r.add_argument("folder")
    r.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if args.cmd == "create":
        config.set_profile(args.profile)
        create(args.name, config.INDEX_DIR, config.CHUNKS_PATH, config.CHROMA_COLLECTION)
    elif args.cmd == "list":
        list_backups()
    elif args.cmd == "verify":
        sys.exit(0 if verify(args.folder) else 1)
    elif args.cmd == "restore":
        restore(args.folder, args.force)


if __name__ == "__main__":
    main()
