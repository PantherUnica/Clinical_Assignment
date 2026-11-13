"""Semi-manual ground-truth labelling for the retrieval metrics.

    python -m eval.build_labels propose   # writes data/labels_review.md
    (edit the ticks in labels_review.md)
    python -m eval.build_labels apply     # writes data/labels.jsonl

For each subset question, `propose` lists the vector top-10 plus up to 3 passages
from a full-text scan of the expected book that the vector search did NOT rank in
its top 10. That second group is what tells "retrieval missed it" apart from
"the text is not in the book". Candidates are scored against the known book
answer (term + number overlap) and the best ones are pre-ticked as suggestions.
"""

from __future__ import annotations

import json
import re
import sys

from eval import cache, dataset
from eval.metrics import number_recall, term_recall
from src.ingest import load_chunks
from src.verify import _content_words

REVIEW_PATH = dataset.DATA_DIR / "labels_review.md"
VECTOR_K = 10
SCAN_EXTRA = 3
SNIPPET_CHARS = 420


def match_score(question: dict, text: str) -> float:
    """Overlap between a passage and the known answer (question terms + answer)."""
    terms = term_recall(f"{question['question']} {question['book_answer']}", text) or 0.0
    numbers = number_recall(question["book_answer"], text)
    return terms if numbers is None else 0.6 * terms + 0.4 * numbers


def snippet(question: dict, text: str) -> str:
    """The ~420-char window of the passage that best matches the answer."""
    if len(text) <= SNIPPET_CHARS:
        return text
    wanted = _content_words(question["book_answer"]) | _content_words(question["question"])
    numbers = set(re.findall(r"\d+(?:\.\d+)?", question["book_answer"]))
    best_start, best_hits = 0, -1
    for start in range(0, len(text) - SNIPPET_CHARS + 1, 100):
        window = text[start : start + SNIPPET_CHARS]
        hits = len(_content_words(window) & wanted) + 2 * sum(n in window for n in numbers)
        if hits > best_hits:
            best_start, best_hits = start, hits
    prefix = "…" if best_start else ""
    suffix = "…" if best_start + SNIPPET_CHARS < len(text) else ""
    return prefix + text[best_start : best_start + SNIPPET_CHARS].strip() + suffix


def _short_book(title: str) -> str:
    return "BSAVA" if "bsava" in title.lower() else "Blackwell's"


def _pages(c: dict) -> str:
    return f"p.{c['page']}" if c["page"] == c["page_end"] else f"pp.{c['page']}-{c['page_end']}"


def propose() -> None:
    from src.retrieve import retrieve

    cache.install()
    subset = dataset.read_jsonl(dataset.SUBSET_PATH)
    if not subset:
        subset = dataset.make_subset(dataset.load_questions())
        dataset.write_jsonl(dataset.SUBSET_PATH, subset)
        print(f"Wrote {len(subset)} questions to {dataset.SUBSET_PATH}")

    chunks = load_chunks()
    by_book = {key: [c for c in chunks if dataset.book_matches(key, c["book_title"])]
               for key in dataset.SOURCES}

    out = [
        f"# Label review — {len(subset)} questions",
        "",
        "For each question, tick `[x]` on **every** passage that contains the answer "
        "(compare with the book answer shown).",
        "",
        "- Pre-ticked boxes are the harness's **guesses** (keyword/number overlap with the "
        "book answer). Please check and correct them.",
        "- Passages marked **outside vector top-10** were found by scanning the whole book. "
        "Ticking one means the answer exists but vector search missed it.",
        "- If no passage contains the answer, tick `NONE`.",
        "- To add a passage that isn't listed, put its chunk_id after `ADD:` "
        "(comma-separated).",
        "",
        "When finished, run: `python -m eval.build_labels apply`",
        "",
    ]

    for n, q in enumerate(subset, start=1):
        ranked = retrieve(q["question"], top_k=VECTOR_K)
        vector_ids = {p["chunk_id"] for p in ranked}
        scored = [(match_score(q, p["text"]), rank, p) for rank, p in enumerate(ranked, 1)]

        scan = sorted(
            ((match_score(q, c["text"]), c) for c in by_book[q["book"]]
             if c["chunk_id"] not in vector_ids),
            key=lambda pair: pair[0], reverse=True,
        )[:SCAN_EXTRA]

        best = max([s for s, _, _ in scored] + [s for s, _ in scan], default=0.0)
        tick = lambda s: s >= 0.5 and s >= best - 0.15  # noqa: E731

        out += [f"## {q['id']} · {q['category']}", "",
                f"**Q:** {q['question']}  ", f"**Book answer:** {q['book_answer']}", ""]
        for s, rank, p in scored:
            out.append(
                f"- [{'x' if tick(s) else ' '}] `{p['chunk_id']}` · {_short_book(p['book_title'])} "
                f"{_pages(p)} · vector rank {rank} · sim {p['similarity']:.3f} · match {s:.2f}"
            )
            out.append(f"  > {snippet(q, p['text'])}")
        for s, c in scan:
            out.append(
                f"- [{'x' if tick(s) else ' '}] `{c['chunk_id']}` · {_short_book(c['book_title'])} "
                f"{_pages(c)} · **outside vector top-10** · match {s:.2f}"
            )
            out.append(f"  > {snippet(q, c['text'])}")
        out += ["- [ ] NONE of these contain the answer", "- ADD:", ""]
        print(f"  [{n}/{len(subset)}] {q['id']}  best match {best:.2f}")

    REVIEW_PATH.write_text("\n".join(out), encoding="utf-8")
    print(f"\nWrote {REVIEW_PATH}\nReview it, then run: python -m eval.build_labels apply")


_SECTION = re.compile(r"^## (\S+)")
_TICKED_CHUNK = re.compile(r"^- \[[xX]\] `([^`]+)`")
_TICKED_NONE = re.compile(r"^- \[[xX]\] NONE")
_ADD = re.compile(r"^- ADD:(.*)$")


def apply() -> None:
    if not REVIEW_PATH.exists():
        sys.exit(f"{REVIEW_PATH} not found. Run: python -m eval.build_labels propose")

    chunk_by_id = {c["chunk_id"]: c for c in load_chunks()}
    parsed: dict[str, dict] = {}
    current = None
    for line in REVIEW_PATH.read_text(encoding="utf-8").splitlines():
        if m := _SECTION.match(line):
            current = parsed.setdefault(m.group(1), {"ids": [], "none": False})
        elif current is None:
            continue
        elif m := _TICKED_CHUNK.match(line):
            current["ids"].append(m.group(1))
        elif _TICKED_NONE.match(line):
            current["none"] = True
        elif m := _ADD.match(line):
            current["ids"] += [x.strip().strip("`") for x in m.group(1).split(",") if x.strip()]

    rows, problems = [], []
    for qid, entry in parsed.items():
        unknown = [cid for cid in entry["ids"] if cid not in chunk_by_id]
        if unknown:
            problems.append(f"{qid}: unknown chunk_id(s) {unknown}")
        ids = list(dict.fromkeys(cid for cid in entry["ids"] if cid in chunk_by_id))
        if ids and entry["none"]:
            problems.append(f"{qid}: has ticked passages AND 'NONE' - using the passages")
        status = "found" if ids else ("miss" if entry["none"] else "unlabeled")
        rows.append({
            "id": qid,
            "status": status,
            "relevant_chunk_ids": ids,
            "relevant_spans": [[chunk_by_id[c]["book_title"], chunk_by_id[c]["page"],
                                chunk_by_id[c]["page_end"]] for c in ids],
        })

    dataset.write_jsonl(dataset.LABELS_PATH, rows)
    counts = {s: sum(r["status"] == s for r in rows) for s in ("found", "miss", "unlabeled")}
    print(f"Wrote {len(rows)} labels to {dataset.LABELS_PATH}  {json.dumps(counts)}")
    for p in problems:
        print("  warning:", p)
    if counts["unlabeled"]:
        print("  note: 'unlabeled' questions (nothing ticked) are excluded from retrieval metrics.")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    if command == "propose":
        propose()
    elif command == "apply":
        apply()
    else:
        sys.exit("usage: python -m eval.build_labels propose|apply")
