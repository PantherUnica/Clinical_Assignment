"""Multi-book test set (checklist §4).

    python -m eval.run_multibook check-keys      # every key fact's quote is on its cited page
    python -m eval.run_multibook check-leakage   # questions not copied from / not inside the index
    python -m eval.run_multibook review          # -> eval/multibook/questions_review.md

(retrieval / pipeline / report subcommands are added in the next steps.)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict

from eval.multibook.build_questions import on_topic
from pathlib import Path

import config

MB_DIR = Path(__file__).resolve().parent / "multibook"
QUESTIONS = MB_DIR / "questions.jsonl"
NGRAM = 8  # a question may not share this many consecutive words with any book page


def load_questions(split: str | None = None) -> list[dict]:
    rows = [json.loads(l) for l in QUESTIONS.open(encoding="utf-8") if l.strip()]
    return [r for r in rows if split in (None, "all", r["split"])]


def _norm(text: str) -> str:
    text = text.lower().replace("­", "").replace("ﬁ", "fi").replace("ﬂ", "fl")
    return re.sub(r"\s+", " ", text).strip()


def _pages_by_book() -> dict[str, dict[int, dict]]:
    from src import library

    out: dict[str, dict[int, dict]] = {}
    for book in library.load_manifest():
        out[book["book_id"]] = {r["pdf_page"]: r for r in library.load_pages(book["book_id"])}
    return out


# --- check-keys ---------------------------------------------------------------


def check_keys() -> bool:
    """Each fact's quote must be on its pdf_page (or the next page, for text that
    runs over), and the stored printed_page must match the library's."""
    pages = _pages_by_book()
    ok = True
    n = 0
    for q in load_questions():
        for f in q["key_facts"]:
            n += 1
            book = pages.get(f["book_id"])
            if book is None:
                print(f"FAIL {q['id']}: unknown book {f['book_id']}")
                ok = False
                continue
            page = book.get(f["pdf_page"])
            if page is None:
                print(f"FAIL {q['id']}: {f['book_id']} pdf {f['pdf_page']} not in cleaned pages")
                ok = False
                continue
            here = _norm(f["quote"]) in _norm(page["text"])
            nxt = book.get(f["pdf_page"] + 1)
            spill = not here and nxt is not None and _norm(f["quote"]) in _norm(page["text"] + " " + nxt["text"])
            if not (here or spill):
                print(f"FAIL {q['id']}: quote not on {f['book_id']} pdf {f['pdf_page']}: {f['quote']!r}")
                ok = False
            if (page.get("printed_page") or None) != (f.get("printed_page") or None):
                print(f"FAIL {q['id']}: printed page {f.get('printed_page')!r} != library {page.get('printed_page')!r} "
                      f"({f['book_id']} pdf {f['pdf_page']})")
                ok = False
    print(f"check-keys: {n} facts, {'all OK' if ok else 'PROBLEMS above'}")
    return ok


# --- check-leakage --------------------------------------------------------------


def _ngrams(text: str, n: int) -> set[tuple[str, ...]]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {tuple(words[i : i + n]) for i in range(len(words) - n + 1)}


def check_leakage() -> bool:
    ok = True
    questions = load_questions()

    # 1. not copied: no 8-word run shared with any cleaned page
    qgrams = {q["id"]: _ngrams(q["question"], NGRAM) for q in questions}
    all_q = set().union(*qgrams.values())
    hits: dict[str, list] = defaultdict(list)
    for book_id, book in _pages_by_book().items():
        for page in book.values():
            shared = all_q & _ngrams(page["text"], NGRAM)
            if shared:
                for qid, grams in qgrams.items():
                    if grams & shared:
                        hits[qid].append((book_id, page["pdf_page"]))
    for qid, where in hits.items():
        print(f"FAIL {qid}: shares {NGRAM}+ consecutive words with {where[:3]}")
        ok = False
    print(f"  copy check ({NGRAM}-gram vs all pages): {'OK' if not hits else f'{len(hits)} questions FAIL'}")

    # 2. never indexed: no chunk text contains a question; nothing indexed from eval/
    from src import library

    chunks = library.load_all_chunks()
    texts = [_norm(c["text"]) for c in chunks]
    inside = [q["id"] for q in questions if any(_norm(q["question"]) in t for t in texts)]
    manifest_files = [b["file"] for b in library.load_manifest(include_skipped=True)]
    eval_in_manifest = [f for f in manifest_files if "eval" in f.lower() or "multibook" in f.lower()]
    if inside or eval_in_manifest:
        ok = False
        print(f"FAIL questions found inside indexed chunks: {inside} / eval files in manifest: {eval_in_manifest}")
    print(f"  index check ({len(chunks):,} chunks): {'OK' if not inside and not eval_in_manifest else 'FAIL'}")

    # 3. unanswerable really absent from every book
    pages_text = [_norm(p["text"]) for b in _pages_by_book().values() for p in b.values()]
    for q in questions:
        for term in q["absent_terms"]:
            n = sum(1 for t in pages_text if _norm(term) in t)
            if n:
                ok = False
                print(f"FAIL {q['id']}: '{term}' appears on {n} pages - not unanswerable")
    print(f"  absence check (unanswerable terms): {'OK' if ok else 'see FAIL lines'}")
    print("check-leakage:", "all OK" if ok else "PROBLEMS above")
    return ok


# --- review sheet -------------------------------------------------------------


def write_review() -> Path:
    from src import library

    titles = {b["book_id"]: b["title"] for b in library.load_manifest()}
    rows = load_questions()
    L = [
        "# Multi-book test set — review sheet",
        "",
        "Written by Claude from the cleaned book pages. Please check each question and its key facts.",
        "Every fact gives the book, the **PDF page** (open the PDF at this page) and the printed page.",
        "Mark anything wrong in the `Reviewer` line; the test only runs after this sheet is approved.",
        "",
        "**Leakage rules:** this folder is never indexed or shown to the answering model; questions are",
        "paraphrased (checked: no 8-word overlap with any book page); `test` questions are run once only.",
        "",
        "| Type | Count |",
        "| --- | ---: |",
    ]
    from collections import Counter

    for t, c in Counter(r["type"] for r in rows).items():
        L.append(f"| {t} | {c} |")
    L += ["", f"Split: {sum(r['split'] == 'dev' for r in rows)} dev / {sum(r['split'] == 'test' for r in rows)} test", ""]
    for r in rows:
        L.append(f"## {r['id']} · {r['type']} · {r['split']}")
        L.append("")
        L.append(f"**Q:** {r['question']}")
        L.append("")
        if r["type"] == "unanswerable":
            L.append(f"Expected: say the books do not cover it. Absent terms checked across all books: "
                     f"{', '.join(r['absent_terms'])}.")
        else:
            L.append(f"Required books: {', '.join(titles.get(b, b) for b in r['required_books'])}")
            L.append("")
            for f in r["key_facts"]:
                page = f"p. {f['printed_page']} (PDF p. {f['pdf_page']})" if f["printed_page"] else f"PDF p. {f['pdf_page']}"
                L.append(f"- {f['fact']}  \n  _{titles.get(f['book_id'], f['book_id'])}, {page}_ — “{f['quote']}”")
            if r.get("also_valid_books"):
                also = "; ".join(f"{titles.get(b, b)} (PDF p. {', '.join(map(str, pages))})"
                                 for b, pages in r["also_valid_books"].items())
                L.append("")
                L.append(f"Also valid (keyword match {r['topic_groups']}): {also}")
            if r.get("conflict"):
                L.append("")
                L.append(f"**Conflict:** {r['conflict']}")
        L += ["", "Reviewer: ☐ OK ☐ Change: ……", ""]
    out = MB_DIR / "questions_review.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return out


# --- retrieval (no LLM) ---------------------------------------------------------

RUNS_DIR = MB_DIR / "runs"
KS = (6, 10, 20)


def fact_hit(fact: dict, passages: list[dict]) -> bool:
    """A key fact is retrieved when a passage from its book covers its PDF page."""
    return any(
        p.get("book_id") == fact["book_id"] and p["page"] <= fact["pdf_page"] <= p["page_end"]
        for p in passages
    )


def book_coverage(required: list[str], passages: list[dict]) -> float | None:
    if not required:
        return None
    found = {p.get("book_id") for p in passages}
    return len(set(required) & found) / len(required)


def score_retrieval(q: dict, ranked: list[dict]) -> dict:
    row = {"id": q["id"], "type": q["type"], "split": q["split"],
           "top1_similarity": ranked[0]["similarity"] if ranked else None,
           "retrieved": [{k: p.get(k) for k in ("chunk_id", "book_id", "page", "page_end", "similarity")}
                         for p in ranked]}
    for k in KS:
        top = ranked[:k]
        cov = book_coverage(q["required_books"], top)
        row[f"book_cov@{k}"] = cov
        row[f"all_books@{k}"] = None if cov is None else float(cov == 1.0)
        facts = q["key_facts"]
        row[f"fact_hit@{k}"] = (sum(fact_hit(f, top) for f in facts) / len(facts)) if facts else None
        # Quote-based: the fact's verbatim quote is inside a retrieved chunk (any page).
        texts = [_norm(p["text"]) for p in top]
        row[f"quote_hit@{k}"] = (
            sum(any(_norm(f["quote"]) in t for t in texts) for f in facts) / len(facts) if facts else None
        )
        # Lenient, book-agnostic: on-topic chunks (keyword groups) from ANY book.
        groups = q.get("topic_groups") or []
        if groups:
            relevant = [p for p in top if on_topic(p["text"], groups)]
            row[f"rel_prec@{k}"] = len(relevant) / len(top) if top else 0.0
            row[f"rel_books@{k}"] = len({p.get("book_id") for p in relevant})
        else:
            row[f"rel_prec@{k}"] = row[f"rel_books@{k}"] = None
    return row


def run_retrieval(split: str, caps: list[int]) -> dict[int, list[dict]]:
    from eval.exact_search import ExactIndex

    index = ExactIndex("library")
    questions = load_questions(split)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    results: dict[int, list[dict]] = {}
    for cap in caps:
        rows = [score_retrieval(q, index.search(q["question"], top_k=max(KS), max_per_book=cap))
                for q in questions]
        # cap applies to the whole ranked list, so top-6 under cap=2 is still capped
        path = RUNS_DIR / f"retrieval_{split}_cap{cap}.jsonl"
        with path.open("w", encoding="utf-8") as handle:
            for r in rows:
                handle.write(json.dumps(r, ensure_ascii=False) + "\n")
        results[cap] = rows
    print(f"index {index.digest} · {len(questions)} {split} questions · caps {caps}")
    return results


def _avg(values) -> float | None:
    vals = [v for v in values if v is not None]
    return sum(vals) / len(vals) if vals else None


def _pct(v) -> str:
    return "—" if v is None else f"{100 * v:.0f}%"


def retrieval_table(results: dict[int, list[dict]]) -> list[str]:
    """Top-6 is what the pipeline uses; @10/@20 show headroom."""
    L = ["| Cap | Required-book cov @6 | All required @6 | Key-fact quote @6 | On-topic chunks @6 "
         "| Books w/ on-topic @6 | Multi-book Qs with ≥2 on-topic books @6 | Quote @20 |",
         "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for cap, rows in results.items():
        a = [r for r in rows if r["type"] != "unanswerable"]
        multi = [r for r in a if r["type"] in ("two_book", "three_book", "conflict")]
        L.append(
            f"| {cap or 'off'} | {_pct(_avg(r['book_cov@6'] for r in a))} | {_pct(_avg(r['all_books@6'] for r in a))} | "
            f"{_pct(_avg(r['quote_hit@6'] for r in a))} | {_pct(_avg(r['rel_prec@6'] for r in a))} | "
            f"{_avg(r['rel_books@6'] for r in a) or 0:.1f} | "
            f"{_pct(_avg(float((r['rel_books@6'] or 0) >= 2) for r in multi))} | "
            f"{_pct(_avg(r['quote_hit@20'] for r in a))} |"
        )
    return L


# --- pipeline + judges (LLM) ----------------------------------------------------

PIPELINE_TOP_K = 6
PIPELINE_CAP = 2  # locked on the dev set in step 2
STAGES = ("synthesize", "verify", "generate")


def model_tag(spec: str) -> str:
    return re.sub(r"[^a-zA-Z0-9.-]+", "_", spec)


def usage_cost(usage: list[dict]) -> float | None:
    """USD for a list of llm.track_usage records; None if any model has no price."""
    total = 0.0
    for u in usage:
        price = config.LLM_PRICES.get(u["model"])
        if price is None or u["input_tokens"] is None:
            return None
        total += u["input_tokens"] * price[0] / 1e6 + (u["output_tokens"] or 0) * price[1] / 1e6
    return round(total, 5)


def _read_rows(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.open(encoding="utf-8")] if path.exists() else []


def _append(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def pipeline_path(model: str, split: str) -> Path:
    return RUNS_DIR / f"pipeline_{model_tag(model)}_{split}.jsonl"


def judge_path(model: str, split: str) -> Path:
    return RUNS_DIR / f"judge_{model_tag(model)}_{split}.jsonl"


def _select(split: str, ids: list[str] | None) -> list[dict]:
    qs = load_questions(split)
    if ids:
        qs = [q for q in qs if q["id"] in set(ids)]
    return qs


def run_pipeline(split: str, ids: list[str] | None, model: str, passages_by_id: dict | None = None) -> Path:
    """Answer each question with `model`. Passages come from exact search (top-6, cap 2)
    unless `passages_by_id` (frozen contexts) is given. Resumable."""
    import time

    from eval import cache
    from eval.citation_check import check_result
    from src import cite, llm
    from src.pipeline import answer_from_passages

    cache.install()
    path = pipeline_path(model, split)
    done = {r["id"] for r in _read_rows(path) if "error" not in r}
    todo = [q for q in _select(split, ids) if q["id"] not in done]
    print(f"{model}: {len(done)} done, {len(todo)} to run -> {path.name}")
    index = None
    for n, q in enumerate(todo, 1):
        if passages_by_id is not None:
            passages = passages_by_id[q["id"]]
        else:
            if index is None:
                from eval.exact_search import ExactIndex

                index = ExactIndex("library")
            passages = index.search(q["question"], top_k=PIPELINE_TOP_K, max_per_book=PIPELINE_CAP)
        marks: list[float] = []
        started = time.perf_counter()
        try:
            with llm.use_model(model), llm.track_usage() as usage:
                result = answer_from_passages(q["question"], passages, on_stage=lambda _l: marks.append(time.perf_counter()))
        except Exception as exc:  # noqa: BLE001 - record and continue; resumable
            _append(path, {"id": q["id"], "model": model, "error": f"{type(exc).__name__}: {exc}"})
            print(f"  [{n}/{len(todo)}] {q['id']} ERROR {type(exc).__name__}: {str(exc)[:120]}")
            continue
        ended = time.perf_counter()
        edges = marks + [ended]
        row = {
            "id": q["id"], "model": model, "split": q["split"], "type": q["type"],
            "grounded": result["grounded"], "answer": result["answer"],
            "citations": [{k: c.get(k) for k in ("marker", "label", "chunk_id", "book_id", "page", "page_end",
                                                  "printed_page", "chapter")} for c in result["citations"]],
            "passages": [{k: p.get(k) for k in ("chunk_id", "book_id", "page", "page_end", "printed_page",
                                                 "chapter", "similarity")} for p in passages],
            "n_claims": len(result["claims"]),
            "verified": [{k: c.get(k) for k in ("text", "sources", "score")} for c in result["verified"]],
            "n_rejected": len(result["rejected"]),
            "seconds": round(ended - started, 3),
            "stage_seconds": {s: round(edges[i + 1] - edges[i], 3) for i, s in enumerate(STAGES) if i + 1 < len(edges)},
            "usage": usage, "cost_usd": usage_cost(usage),
            "citation_checks": check_result(result["verified"], passages),
        }
        row["source_labels"] = [cite.source_label(c) for c in result["citations"]]
        _append(path, row)
        print(f"  [{n}/{len(todo)}] {q['id']} {row['seconds']:.0f}s ${row['cost_usd']} "
              f"claims {len(row['verified'])}/{row['n_claims']} grounded={row['grounded']}")
    return path


def run_judges(split: str, ids: list[str] | None, model: str, judges: tuple[str, ...]) -> Path:
    from eval import judge as J

    answers = {r["id"]: r for r in _read_rows(pipeline_path(model, split)) if "error" not in r}
    path = judge_path(model, split)
    done = {(r["id"], r["judge"]) for r in _read_rows(path) if "error" not in r}
    qs = {q["id"]: q for q in _select(split, ids)}
    for qid, a in answers.items():
        if qid not in qs:
            continue
        for jm in judges:
            if (qid, jm) in done:
                continue
            out = J.judge(qs[qid], a["answer"], a.get("source_labels", []), jm)
            out.update({"id": qid, "answer_model": model, "cost_usd": usage_cost(out["usage"])})
            _append(path, out)
            print(f"  judge {jm:18s} {qid}: overall={out.get('overall')} fact_recall={out.get('fact_recall')} "
                  f"refused={out.get('refused')} ${out['cost_usd']}")
    return path


def summary(split: str, model: str, ids: list[str] | None = None) -> list[str]:
    answers = [r for r in _read_rows(pipeline_path(model, split)) if "error" not in r and (not ids or r["id"] in ids)]
    judges = _read_rows(judge_path(model, split))
    L = [f"### {model} · {split} · {len(answers)} answers", "",
         "| Q | Type | Time s | Answer $ | Claims kept | Cited books | Citations supported | Printed page ok "
         "| Judge gpt-5-mini | Judge gpt-5.5 | Judges $ |",
         "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |"]
    for a in answers:
        checks = a["citation_checks"]
        sup = _avg(float(c["supported"]) for c in checks)
        pok = _avg(None if c["page_ok"] is None else float(c["page_ok"]) for c in checks)
        js = {j["judge"]: j for j in judges if j["id"] == a["id"]}

        def jtxt(name):
            j = js.get(name)
            if not j:
                return "—"
            if "error" in j:
                return "ERR"
            fr = "" if j.get("fact_recall") is None else f" facts {_pct(j['fact_recall'])}"
            return f"{j.get('overall')}/5{fr}{' refused' if j.get('refused') else ''}"

        jcost = sum(j.get("cost_usd") or 0 for j in js.values())
        L.append(f"| {a['id']} | {a['type']} | {a['seconds']:.0f} | {a['cost_usd']} | "
                 f"{len(a['verified'])}/{a['n_claims']} | {len({c['book_id'] for c in a['citations']})} | "
                 f"{_pct(sup)} | {_pct(pok)} | {jtxt('openai:gpt-5-mini')} | {jtxt('openai:gpt-5.5')} | {jcost:.4f} |")
    return L


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("cmd", choices=["check-keys", "check-leakage", "review", "retrieval",
                                        "pipeline", "judge", "summary"])
    parser.add_argument("--split", default="dev", choices=["dev", "test", "all"])
    parser.add_argument("--caps", default="0,2,3", help="per-book caps to compare, 0 = off")
    parser.add_argument("--ids", default=None, help="comma-separated question ids (e.g. a pilot)")
    parser.add_argument("--model", default=None, help="answering model, e.g. openai:gpt-5.5 (default: .env)")
    args = parser.parse_args()
    config.set_profile("library")
    ids = args.ids.split(",") if args.ids else None
    model = args.model or f"{config.LLM_PROVIDER}:{config.OPENAI_MODEL if config.LLM_PROVIDER == 'openai' else ''}"
    if args.cmd == "pipeline":
        run_pipeline(args.split, ids, model)
        return
    if args.cmd == "judge":
        from eval.judge import JUDGES

        run_judges(args.split, ids, model, JUDGES)
        return
    if args.cmd == "summary":
        print("\n".join(summary(args.split, model, ids)))
        return
    if args.cmd == "check-keys":
        sys.exit(0 if check_keys() else 1)
    if args.cmd == "check-leakage":
        sys.exit(0 if check_leakage() else 1)
    if args.cmd == "retrieval":
        results = run_retrieval(args.split, [int(c) for c in args.caps.split(",")])
        print("\n".join(retrieval_table(results)))
        for cap, rows in results.items():
            print(f"\n cap {cap or 'off'} per question (book cov@6 / fact hit@6 / top1 sim):")
            for r in rows:
                print(f"   {r['id']} {r['type']:13s} {_pct(r['book_cov@6']):>5} {_pct(r['fact_hit@6']):>5}  {r['top1_similarity']}")
        return
    write_review()


if __name__ == "__main__":
    main()
