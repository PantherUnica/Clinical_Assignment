"""Run the evaluation and write the baseline report.

    python -m eval.run_eval retrieval            # top-50 retrieval for all 200 Qs (no LLM)
    python -m eval.run_eval pipeline [--workers 4] [--limit N]
                                                 # full pipeline for all 200 Qs (2 LLM calls each)
    python -m eval.run_eval report               # join raw runs + labels -> reports/*.md

Raw per-question results go to eval/runs/<pass>_<variant>.jsonl so the report can
be regenerated (e.g. after labels change) without re-paying for the runs.
`pipeline` resumes: questions already in the raw file are skipped.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import config
from eval import cache, dataset
from eval import metrics as M

RUNS_DIR = dataset.EVAL_DIR / "runs"
REPORTS_DIR = dataset.EVAL_DIR / "reports"
VARIANT = "vector"  # future retrieval variants (bm25, hybrid, ...) get their own files
RETRIEVAL_DEPTH = 50
RECALL_KS = (1, 3, 5, config.TOP_K, 10, 20, 50)
STAGES = ("retrieve", "synthesize", "verify", "generate")


def _runs_path(kind: str) -> Path:
    return RUNS_DIR / f"{kind}_{VARIANT}.jsonl"


def _passage_row(p: dict) -> dict:
    return {k: p.get(k) for k in ("chunk_id", "book_title", "page", "page_end", "similarity")}


# --- retrieval pass ---------------------------------------------------------


def run_retrieval() -> None:
    from src import llm
    from src.retrieve import retrieve

    def _no_llm(*_a, **_k):
        raise AssertionError("retrieval pass must not call the LLM")

    llm.complete = _no_llm  # proves the retrieval metrics cost no LLM calls
    emb_cache = cache.install()
    questions = dataset.load_questions()
    rows = []
    for n, q in enumerate(questions, 1):
        started = time.perf_counter()
        ranked = retrieve(q["question"], top_k=RETRIEVAL_DEPTH)
        rows.append({
            "id": q["id"],
            "seconds": round(time.perf_counter() - started, 3),
            "retrieved": [_passage_row(p) for p in ranked],
        })
        if n % 25 == 0:
            print(f"  retrieved {n}/{len(questions)}")
    dataset.write_jsonl(_runs_path("retrieval"), rows)
    print(f"Wrote {_runs_path('retrieval')}  (embedding cache: {emb_cache.hits} hits, "
          f"{emb_cache.misses} new)")


# --- pipeline pass ----------------------------------------------------------


def _run_one(q: dict) -> dict:
    from src import pipeline

    marks: list[float] = []
    started = time.perf_counter()
    for attempt in (1, 2):
        marks.clear()
        try:
            result = pipeline.answer_question(
                q["question"], on_stage=lambda _label: marks.append(time.perf_counter())
            )
            break
        except Exception as exc:  # noqa: BLE001 - record and move on
            if attempt == 2:
                return {"id": q["id"], "error": f"{type(exc).__name__}: {exc}"}
    ended = time.perf_counter()

    edges = marks + [ended]
    stage_seconds = {
        name: round(edges[i + 1] - edges[i], 3) for i, name in enumerate(STAGES) if i + 1 < len(edges)
    }
    keep = ("text", "sources", "best_source", "score", "lexical", "cosine", "reason",
            "unsourced_numbers")
    return {
        "id": q["id"],
        "grounded": result["grounded"],
        "answer": result["answer"],
        "citations": [{k: c.get(k) for k in ("marker", "chunk_id", "book_title", "page", "page_end")}
                      for c in result["citations"]],
        "passages": [_passage_row(p) for p in result["passages"]],
        "n_claims": len(result["claims"]),
        "verified": [{k: c.get(k) for k in keep if k in c} for c in result["verified"]],
        "rejected": [{k: c.get(k) for k in keep if k in c} for c in result["rejected"]],
        "synthesis_notes": result["synthesis_notes"],
        "threshold": result["threshold"],
        "seconds": round(ended - started, 3),
        "stage_seconds": stage_seconds,
    }


def run_pipeline(workers: int, limit: int | None) -> None:
    emb_cache = cache.install()
    path = _runs_path("pipeline")
    done = {row["id"] for row in dataset.read_jsonl(path) if "error" not in row}
    todo = [q for q in dataset.load_questions() if q["id"] not in done]
    if limit:
        todo = todo[:limit]
    print(f"{len(done)} already done, running {len(todo)} with {workers} workers")
    if not todo:
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    lock = threading.Lock()

    def save(row: dict) -> None:
        with lock, path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    # First question alone: initialises the lazily-created API/Chroma clients
    # before threads race to create them.
    first = _run_one(todo[0])
    save(first)
    print(f"  [1/{len(todo)}] {first['id']}  {first.get('seconds', 'ERR')}s")

    finished = 1
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_run_one, q): q for q in todo[1:]}
        for future in as_completed(futures):
            row = future.result()
            save(row)
            finished += 1
            status = "ERR " + row["error"][:60] if "error" in row else f"{row['seconds']}s"
            print(f"  [{finished}/{len(todo)}] {row['id']}  {status}")
    print(f"Done. Embedding cache: {emb_cache.hits} hits, {emb_cache.misses} new")


# --- report -----------------------------------------------------------------


def _pct(value: float | None) -> str:
    return "—" if value is None else f"{100 * value:.0f}%"


def _num(value: float | None, digits: int = 2) -> str:
    return "—" if value is None else f"{value:.{digits}f}"


def _latest_by_id(rows: list[dict]) -> dict[str, dict]:
    """Last successful row per question id (a resumed run may append retries)."""
    out: dict[str, dict] = {}
    for row in rows:
        if "error" not in row or row["id"] not in out:
            out[row["id"]] = row
    return out


def _refusal_cause(row: dict) -> str | None:
    if row.get("grounded"):
        return None
    if "error" in row:
        return "run error"
    return "no claims proposed" if row["n_claims"] == 0 else "all claims rejected by gate"


def build_report() -> Path:
    from src.ingest import load_chunks

    questions = {q["id"]: q for q in dataset.load_questions()}
    labels = {k: v for k, v in dataset.load_labels().items() if v["status"] in ("found", "miss")}
    retrieval = _latest_by_id(dataset.read_jsonl(_runs_path("retrieval")))
    pipeline = _latest_by_id(dataset.read_jsonl(_runs_path("pipeline")))
    if not retrieval and not pipeline:
        sys.exit("No runs found. Run `retrieval` and/or `pipeline` first.")

    chunks = load_chunks()
    book_counts = Counter(c["book_title"] for c in chunks)
    today = dt.date.today().isoformat()
    L: list[str] = []
    add = L.append

    def table(header: list[str], rows: list[list[str]]) -> None:
        add("| " + " | ".join(header) + " |")
        add("|" + "|".join("---" for _ in header) + "|")
        for r in rows:
            add("| " + " | ".join(str(x) for x in r) + " |")
        add("")

    # ---- retrieval metrics over labelled questions
    ret_rows = []
    for qid, lab in labels.items():
        if qid not in retrieval:
            continue
        ids = [p["chunk_id"] for p in retrieval[qid]["retrieved"]]
        rel = lab["relevant_chunk_ids"]
        ret_rows.append({
            "id": qid, "q": questions[qid], "rank": M.first_relevant_rank(ids, rel),
            **{f"r@{k}": M.recall_at_k(ids, rel, k) for k in RECALL_KS},
            "rr": M.reciprocal_rank(ids, rel), "p@5": M.precision_at_k(ids, rel, 5),
        })

    def agg(rows: list[dict], key: str) -> float | None:
        return M.mean(r[key] for r in rows)[0]

    # ---- pipeline metrics over all questions
    pipe_rows = []
    for qid, row in pipeline.items():
        q = questions[qid]
        grounded = bool(row.get("grounded"))
        cite_books = [c["book_title"] for c in row.get("citations", [])]
        pipe_rows.append({
            "id": qid, "q": q, "row": row, "grounded": grounded,
            "cause": _refusal_cause(row),
            "book_cite": (sum(dataset.book_matches(q["book"], b) for b in cite_books) / len(cite_books))
                         if cite_books else None,
            "num_recall": M.number_recall(q["book_answer"], row["answer"]) if grounded else None,
            "term_recall": M.term_recall(q["book_answer"], row["answer"]) if grounded else None,
        })
    answered = M.mean(1.0 if r["grounded"] else 0.0 for r in pipe_rows)[0]
    n_claims = sum(r["row"].get("n_claims", 0) for r in pipe_rows)
    n_verified = sum(len(r["row"].get("verified", [])) for r in pipe_rows)

    # E-3 proxy on labelled questions that were answered
    cite_hit, cite_page = [], []
    for r in pipe_rows:
        lab = labels.get(r["id"])
        if not lab or not r["grounded"]:
            continue
        spans = [(c["book_title"], c["page"], c["page_end"]) for c in r["row"]["citations"]]
        relevant = [tuple(s) for s in lab["relevant_spans"]]
        cite_hit.append(M.page_citation_hit(spans, relevant))
        cite_page.append(M.page_citation_precision(spans, relevant))

    totals = [r["row"]["seconds"] for r in pipe_rows if "seconds" in r["row"]]

    add(f"# Baseline evaluation — vector-only retrieval ({today})")
    add("")
    add("Generated by `python -m eval.run_eval report`. Metric IDs follow "
        "`PRD_Documents/AI_ML_VALIDATION_SPEC.md` (E-1 retrieval, E-2 relevance, "
        "E-3 citation faithfulness, E-12 latency).")
    add("")
    add("## Setup")
    add("")
    table(["Item", "Value"], [
        *[[f"Indexed book", f"{t} — {n:,} chunks"] for t, n in book_counts.items()],
        ["Embedding model", f"{config.EMBED_PROVIDER} / {config.OPENAI_EMBED_MODEL if config.EMBED_PROVIDER == 'openai' else config.LOCAL_EMBED_MODEL}"],
        ["LLM", f"{config.LLM_PROVIDER} / {config.summary()['llm_model']}"],
        ["Chunking", f"{config.CHUNK_SIZE} tokens, overlap {config.CHUNK_OVERLAP}"],
        ["Pipeline top-k / verify threshold / lexical weight",
         f"{config.TOP_K} / {config.VERIFY_THRESHOLD} / {config.VERIFY_LEXICAL_WEIGHT}"],
        ["Questions (full pipeline)", f"{len(pipe_rows)} of {len(questions)}"],
        ["Labelled questions (retrieval metrics)",
         f"{len(ret_rows)} ({sum(l['status'] == 'found' for l in labels.values())} found, "
         f"{sum(l['status'] == 'miss' for l in labels.values())} not found by reviewer)"],
    ])

    add("## KPI scorecard")
    add("")
    table(["KPI", "Value", "n", "Spec", "What it tells you"], [
        [f"Recall@{config.TOP_K} (pipeline window)", _pct(agg(ret_rows, f"r@{config.TOP_K}")), len(ret_rows), "E-1",
         "Was the right passage among the passages the LLM actually reads?"],
        ["Recall@10", _pct(agg(ret_rows, "r@10")), len(ret_rows), "E-1", "Right passage in top 10?"],
        ["MRR", _num(agg(ret_rows, "rr")), len(ret_rows), "E-1", "1.0 = right passage always ranked first"],
        ["Precision@5", _pct(agg(ret_rows, "p@5")), len(ret_rows), "E-2", "Share of top-5 that is relevant"],
        ["Answer rate", _pct(answered), len(pipe_rows), "—", "Questions that got a grounded answer"],
        ["Claims surviving the gate", _pct(n_verified / n_claims if n_claims else None), n_claims, "E-3/E-5",
         "Verified ÷ proposed claims"],
        ["Cited the confirmed answer passage", _pct(M.mean(cite_hit)[0]), M.mean(cite_hit)[1], "E-3 proxy",
         "Answered labelled Qs: at least one citation lands on a page the reviewer confirmed"],
        ["Share of citations on answer pages", _pct(M.mean(cite_page)[0]), M.mean(cite_page)[1], "E-3 proxy",
         "Lower bound: extra citations to other valid passages count as misses"],
        ["Answer number recall", _pct(M.mean(r["num_recall"] for r in pipe_rows)[0]),
         M.mean(r["num_recall"] for r in pipe_rows)[1], "proxy",
         "Answered Qs with numeric book answers: share of the book's numbers present in the AI answer"],
        ["Answer term recall", _pct(M.mean(r["term_recall"] for r in pipe_rows)[0]),
         M.mean(r["term_recall"] for r in pipe_rows)[1], "proxy",
         "Answered Qs: share of the book answer's key words present in the AI answer"],
        ["Latency p50 / p95", f"{_num(M.percentile(totals, 50), 1)}s / {_num(M.percentile(totals, 95), 1)}s",
         len(totals), "E-12", "End-to-end, per question"],
    ])

    if ret_rows:
        add("## Retrieval detail (labelled questions)")
        add("")
        table(["k"] + [str(k) for k in RECALL_KS],
              [["Recall@k"] + [_pct(agg(ret_rows, f"r@{k}")) for k in RECALL_KS]])
        buckets = Counter()
        for r in ret_rows:
            rank = r["rank"]
            buckets["1" if rank == 1 else f"2–{config.TOP_K}" if rank and rank <= config.TOP_K
                    else f"{config.TOP_K + 1}–10" if rank and rank <= 10 else "11–50" if rank
                    else "not in top 50"] += 1
        order = ["1", f"2–{config.TOP_K}", f"{config.TOP_K + 1}–10", "11–50", "not in top 50"]
        table(["Rank of first correct passage"] + order, [["Questions"] + [buckets[b] for b in order]])
        groups = defaultdict(list)
        for r in ret_rows:
            groups[("book", r["q"]["book"])].append(r)
            groups[("category", r["q"]["category"])].append(r)
        table(["Group", "n", f"Recall@{config.TOP_K}", "Recall@10", "MRR"],
              [[f"{kind}: {name}", len(rs), _pct(agg(rs, f"r@{config.TOP_K}")), _pct(agg(rs, "r@10")),
                _num(agg(rs, "rr"))] for (kind, name), rs in sorted(groups.items())])

    if retrieval:
        sims = {k: [row["retrieved"][k - 1]["similarity"] for row in retrieval.values()
                    if len(row["retrieved"]) >= k] for k in (1, config.TOP_K, 10, 50)}
        add("**Similarity spread** (all questions, median cosine similarity by rank) — a small gap "
            "between rank 1 and rank 50 means the embedding barely separates relevant from irrelevant text:")
        add("")
        table(["Rank"] + [str(k) for k in sims], [["Median similarity"] + [_num(M.percentile(v, 50), 3) for v in sims.values()]])

    if pipe_rows:
        add("## Pipeline detail (all questions)")
        add("")
        groups = defaultdict(list)
        for r in pipe_rows:
            groups[("book", r["q"]["book"])].append(r)
            groups[("category", r["q"]["category"])].append(r)
            groups[("numeric answer", str(r["q"]["has_numbers"]))].append(r)
        table(["Group", "n", "Answered", "Refused: no claims proposed", "Refused: all claims rejected",
               "Claims proposed", "Claims verified"],
              [[f"{kind}: {name}", len(rs), _pct(M.mean(1.0 if r['grounded'] else 0.0 for r in rs)[0]),
                sum(r["cause"] == "no claims proposed" for r in rs),
                sum(r["cause"] == "all claims rejected by gate" for r in rs),
                sum(r["row"].get("n_claims", 0) for r in rs),
                sum(len(r["row"].get("verified", [])) for r in rs)]
               for (kind, name), rs in sorted(groups.items())])

        reasons = Counter(c["reason"] for r in pipe_rows for c in r["row"].get("rejected", []))
        add("**Why claims were dropped** (verification gate, all rejected claims):")
        add("")
        if not reasons:
            add("No claims were rejected.")
            add("")
        else:
            meaning = {
                "no_citation": "LLM proposed a claim without citing a passage",
                "unknown_citation": "Cited a passage that was never retrieved",
                "number_not_in_source": "A number in the claim is not in the cited passage",
                "unsupported_by_source": f"Support score below threshold {config.VERIFY_THRESHOLD}",
            }
            table(["Reason", "Claims", "Meaning"],
                  [[reason, n, meaning.get(reason, "")] for reason, n in reasons.most_common()])

        scores = [c["score"] for r in pipe_rows for c in r["row"].get("rejected", [])
                  if c.get("reason") == "unsupported_by_source"]
        if scores:
            edges = [0.0, 0.4, 0.5, 0.55, 0.6, config.VERIFY_THRESHOLD]
            labels_ = [f"{a:.2f}–{b:.2f}" for a, b in zip(edges, edges[1:])]
            counts = [sum(a <= s < b for s in scores) for a, b in zip(edges, edges[1:])]
            add(f"**Near-misses**: support scores of `unsupported_by_source` claims "
                f"(threshold {config.VERIFY_THRESHOLD}; the last bucket is just below it):")
            add("")
            table(["Score"] + labels_, [["Claims"] + counts])

        add("**Cross-book citations**: share of citations pointing at the answer key's own book "
            f"(both books overlap, so a cross-book citation can still be correct): "
            f"{_pct(M.mean(r['book_cite'] for r in pipe_rows)[0])}")
        add("")

    # ---- root cause matrix (labelled + piped)
    joined = [(r, next((x for x in ret_rows if x["id"] == r["id"]), None)) for r in pipe_rows]
    joined = [(p, rr) for p, rr in joined if rr is not None]
    if joined:
        add("## Root-cause matrix (labelled questions)")
        add("")
        add(f"Rows: was a confirmed passage inside the top {config.TOP_K} the pipeline reads? "
            "Columns: did the question get a grounded answer?")
        add("")
        cell = Counter((rr[f"r@{config.TOP_K}"] == 1.0, p["grounded"]) for p, rr in joined)
        table(["", "Answered", "Refused"], [
            [f"Evidence in top {config.TOP_K}", cell[(True, True)], cell[(True, False)]],
            [f"Evidence NOT in top {config.TOP_K}", cell[(False, True)], cell[(False, False)]],
        ])
        add(f"- **Evidence in top {config.TOP_K} but refused** → the problem is downstream of retrieval "
            "(claim extraction or the verification gate).")
        add(f"- **Evidence not in top {config.TOP_K} and refused** → retrieval problem "
            "(what BM25 / hybrid / reranking would target).")
        add("")

    if pipe_rows:
        add("## Latency by stage (E-12)")
        add("")
        table(["Stage", "Mean", "p50", "p95"], [
            [stage, *[f"{_num(fn(vals), 2)}s" for fn in (lambda v: M.mean(v)[0],
                                                          lambda v: M.percentile(v, 50),
                                                          lambda v: M.percentile(v, 95))]]
            for stage in STAGES + ("total",)
            for vals in [[r["row"]["stage_seconds"].get(stage) for r in pipe_rows
                          if r["row"].get("stage_seconds", {}).get(stage) is not None]
                         if stage != "total" else totals]
        ])

        add("## Per-question results")
        add("")
        rank_by_id = {r["id"]: r["rank"] for r in ret_rows}
        rows = []
        for r in sorted(pipe_rows, key=lambda x: x["id"]):
            rej = Counter(c["reason"] for c in r["row"].get("rejected", []))
            rows.append([
                r["id"], r["q"]["category"],
                ("—" if r["id"] not in rank_by_id else (rank_by_id[r["id"]] or ">50")),
                "yes" if r["grounded"] else f"no ({r['cause']})",
                f"{len(r['row'].get('verified', []))}/{r['row'].get('n_claims', 0)}",
                rej.most_common(1)[0][0] if rej else "",
                _pct(r["num_recall"]),
            ])
        table(["Question", "Category", "Correct passage rank", "Answered", "Verified/claims",
               "Top drop reason", "Number recall"], rows)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORTS_DIR / f"baseline_{VARIANT}_{today}.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote {out}")
    return out


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(prog="python -m eval.run_eval")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("retrieval")
    p = sub.add_parser("pipeline")
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--limit", type=int)
    sub.add_parser("report")
    args = parser.parse_args()
    if args.command == "retrieval":
        run_retrieval()
    elif args.command == "pipeline":
        run_pipeline(args.workers, args.limit)
    else:
        build_report()


if __name__ == "__main__":
    main()
