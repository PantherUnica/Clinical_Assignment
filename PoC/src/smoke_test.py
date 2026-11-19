"""Retrieval smoke test for the full library (checklist §2: "test retrieval with sample questions").

    python -m src.smoke_test [--k 5]     -> reports/smoke_test_library.md

Each question targets a specific book. A question passes when at least one of
its expected books appears in the top-k. This is a sanity check that every
book is indexed and reachable - not an accuracy evaluation.
"""

from __future__ import annotations

import argparse
import datetime as dt
import time

import config

QUESTIONS = [
    ("What is the dose of meloxicam for cats?", ["plumbs-drug-handbook", "bsava-formulary"]),
    ("Clinical signs and diagnosis of hyperadrenocorticism in dogs", ["ettinger-internal-medicine", "blackwell-5min-canine-feline"]),
    ("Treatment of sarcoptic mange in dogs", ["muller-kirk-dermatology", "dermatology-color-atlas", "blackwell-5min-dermatology", "saunders-solutions-dermatology"]),
    ("How to position a dog for a lateral thoracic radiograph", ["radiography-dog-cat"]),
    ("Causes of anterior uveitis in cats", ["slatter-ophthalmology"]),
    ("Gastropexy technique for gastric dilatation-volvulus", ["fossum-small-animal-surgery"]),
    ("Definition of azotemia", ["saunders-vet-dictionary"]),
    ("Vaccination schedule for dogs against canine parvovirus", ["vaccination-schedule", "wsava-essential-medicines", "merck-vet-manual"]),
    ("Ethylene glycol poisoning in animals", ["merck-vet-manual", "ettinger-internal-medicine"]),
    ("Core list of essential antimicrobial drugs for cats and dogs", ["wsava-essential-medicines"]),
    ("Differential diagnosis for polyuria and polydipsia", ["differential-diagnosis-lists"]),
    ("Routes of drug administration and dosage forms for veterinary technicians", ["applied-pharmacology-vet-tech"]),
]


def _page(meta: dict) -> str:
    printed = meta.get("printed_page")
    return f"p. {printed}" if printed else f"PDF p. {meta.get('page')}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args()
    config.set_profile("library")

    from . import embeddings
    from .embed_index import get_collection

    collection = get_collection()
    total = collection.count()
    lines = [
        "# Library retrieval smoke test",
        "",
        f"Generated {dt.datetime.now():%Y-%m-%d %H:%M} · collection `{config.CHROMA_COLLECTION}` "
        f"({total:,} vectors) · top-{args.k} · embedding `{config.OPENAI_EMBED_MODEL}`",
        "",
    ]
    passed = 0
    for n, (question, expected) in enumerate(QUESTIONS, 1):
        started = time.perf_counter()
        res = collection.query(
            query_embeddings=[embeddings.embed_one(question)],
            n_results=args.k,
            include=["metadatas", "distances", "documents"],
        )
        ms = (time.perf_counter() - started) * 1000
        metas, dists, docs = res["metadatas"][0], res["distances"][0], res["documents"][0]
        books = [m["book_id"] for m in metas]
        ok = any(b in expected for b in books)
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {question}")
        lines += [
            f"## {n}. {question} — {'PASS' if ok else '**FAIL**'}",
            "",
            f"Expected one of: {', '.join(expected)} · {ms:.0f} ms",
            "",
            "| # | Book | Chapter | Section | Page | Similarity | Text |",
            "|---|---|---|---|---|---:|---|",
        ]
        for rank, (m, d, doc) in enumerate(zip(metas, dists, docs), 1):
            mark = " ✅" if m["book_id"] in expected else ""
            snippet = " ".join(doc.split())[:110].replace("|", "/")
            lines.append(
                f"| {rank} | {m['book_title']}{mark} | {(m.get('chapter') or '—')[:40]} | "
                f"{(m.get('section') or '—')[:30]} | {_page(m)} | {1 - d:.3f} | {snippet}… |"
            )
        lines.append("")
    summary = f"**{passed}/{len(QUESTIONS)} questions found an expected book in the top-{args.k}.**"
    lines.insert(4, summary + "\n")
    config.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = config.REPORTS_DIR / "smoke_test_library.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n{passed}/{len(QUESTIONS)} passed -> {out}")


if __name__ == "__main__":
    main()
