"""LLM comparison on frozen contexts (checklist §5).

    python -m eval.compare_llms freeze                 # passages -> eval/multibook/frozen_contexts.jsonl
    python -m eval.compare_llms run  [--models ...]    # answer all 40 questions per model (resumable)
    python -m eval.compare_llms judge [--models ...]   # both judges, blind
    python -m eval.compare_llms report                 # -> eval/reports/llm_comparison_<date>.md

Every model gets EXACTLY the same passages (frozen once, verified identical to the
Phase 4 run), so differences come from the model, not retrieval. Models run one
after another (not in parallel) so response times are comparable.
Add local models later by name, e.g. --models ollama:qwen2.5:7b (llm.py speaks Ollama).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import statistics

import config
from eval.multibook_report import JUDGE_BIG, JUDGE_SMALL, REPORTS, load_run, metrics
from eval.run_multibook import (
    MB_DIR, PIPELINE_CAP, PIPELINE_TOP_K, _pct, _read_rows, load_questions, pipeline_path, run_judges, run_pipeline,
)

FROZEN = MB_DIR / "frozen_contexts.jsonl"
MODELS = ("openai:gpt-5-mini", "openai:gpt-4o-mini")
REFERENCE = "openai:gpt-5.5"  # Phase 4 run on the same passages


def freeze() -> None:
    from eval.exact_search import ExactIndex

    index = ExactIndex("library")
    rows = []
    for q in load_questions():
        passages = index.search(q["question"], top_k=PIPELINE_TOP_K, max_per_book=PIPELINE_CAP)
        rows.append({"id": q["id"], "index": index.digest, "passages": passages})
    # Must equal what the Phase 4 (reference) run used.
    ref = {r["id"]: [p["chunk_id"] for p in r["passages"]]
           for s in ("dev", "test") for r in _read_rows(pipeline_path(REFERENCE, s)) if "error" not in r}
    mismatch = [r["id"] for r in rows if r["id"] in ref and ref[r["id"]] != [p["chunk_id"] for p in r["passages"]]]
    if mismatch:
        raise SystemExit(f"Frozen passages differ from the {REFERENCE} run for {mismatch} - not freezing.")
    FROZEN.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    print(f"Froze {len(rows)} contexts -> {FROZEN} (identical to the {REFERENCE} run for {len(ref)} questions)")


def frozen() -> dict[str, list[dict]]:
    if not FROZEN.exists():
        raise SystemExit("Run `python -m eval.compare_llms freeze` first.")
    return {r["id"]: r["passages"] for r in map(json.loads, FROZEN.open(encoding="utf-8"))}


def run(models) -> None:
    contexts = frozen()
    for model in models:
        for split in ("dev", "test"):
            run_pipeline(split, None, model, passages_by_id=contexts)


def judge(models) -> None:
    from eval.judge import JUDGES

    for model in models:
        for split in ("dev", "test"):
            run_judges(split, None, model, JUDGES)


def _m(vals):
    v = [x for x in vals if x is not None]
    return statistics.mean(v) if v else None


def _q(vals, pct):
    v = sorted(x for x in vals if x is not None)
    if not v:
        return None
    return v[min(len(v) - 1, int(round(pct / 100 * (len(v) - 1))))]


def model_row(model: str, split: str | None = "test") -> dict | None:
    items = load_run(model)
    rows = [metrics(it) for it in items.values() if split in (None, it["q"]["split"])]
    if not rows:
        return None
    ans = [r for r in rows if r["type"] != "unanswerable"]
    un = [r for r in rows if r["type"] == "unanswerable"]
    multi = [r for r in ans if r["type"] in ("two_book", "three_book", "conflict")]
    conf = [r for r in rows if r["type"] == "conflict"]
    cost_by_q = [r["cost"] for r in rows]
    return {
        "model": model, "n": len(rows),
        "recall_s": _m(r["recall_s"] for r in ans), "recall_b": _m(r["recall_b"] for r in ans),
        "overall_s": _m(r["overall_s"] for r in rows), "overall_b": _m(r["overall_b"] for r in rows),
        "contradicted": sum((r["contradicted_b"] or 0) for r in rows),
        "unsupported": sum(r["unsupported_b"] for r in rows),
        "supported": _m(r["supported"] for r in ans), "page_ok": _m(r["page_ok"] for r in ans),
        "multi2": _m(float(r["n_books_cited"] >= 2) for r in multi),
        "required_cited": _m(r["required_cited"] for r in ans),
        "conflict": _m(None if r["conflict_b"] is None else float(r["conflict_b"]) for r in conf),
        "refuse_ok": _m(float(r["refused"]) for r in un), "refuse_bad": _m(float(r["refused"]) for r in ans),
        "median_s": _q([r["seconds"] for r in rows], 50), "p90_s": _q([r["seconds"] for r in rows], 90),
        "cost_per_answer": _m(cost_by_q), "cost_total": sum(c or 0 for c in cost_by_q),
        "claims_kept": _m((len(items[r["id"]]["answer"]["verified"]) / items[r["id"]]["answer"]["n_claims"])
                          if items[r["id"]]["answer"]["n_claims"] else None for r in ans),
    }


def table(rows: list[dict]) -> list[str]:
    L = ["| Model | n | Fact recall (small / big judge) | Overall /5 (small / big) | Contradicted facts | Invented claims (big judge) "
         "| Citations supported in PDF | Printed page ok | Multi-book Qs citing ≥2 books | Required books cited "
         "| Claims passing the gate | Conflict shown | Correct refusal | Wrong refusal | Median s | p90 s | $ / answer | $ total |",
         "| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for r in rows:
        L.append(
            f"| `{r['model']}` | {r['n']} | {_pct(r['recall_s'])} / {_pct(r['recall_b'])} | "
            f"{r['overall_s']:.2f} / {r['overall_b']:.2f} | {r['contradicted']} | {r['unsupported']} | "
            f"{_pct(r['supported'])} | {_pct(r['page_ok'])} | {_pct(r['multi2'])} | {_pct(r['required_cited'])} | "
            f"{_pct(r['claims_kept'])} | {_pct(r['conflict'])} | {_pct(r['refuse_ok'])} | {_pct(r['refuse_bad'])} | "
            f"{r['median_s']:.0f} | {r['p90_s']:.0f} | {r['cost_per_answer']:.4f} | {r['cost_total']:.2f} |"
        )
    return L


def per_type(models: list[str]) -> list[str]:
    types = ("two_book", "three_book", "conflict", "single_book", "unanswerable")
    L = ["| Type | " + " | ".join(f"`{m}`" for m in models) + " |", "| --- |" + " ---: |" * len(models)]
    data = {m: [metrics(it) for it in load_run(m).values() if it["q"]["split"] == "test"] for m in models}
    for t in types:
        cells = []
        for m in models:
            rs = [r for r in data[m] if r["type"] == t]
            ov = _m(r["overall_b"] for r in rs)
            cells.append("—" if ov is None else f"{ov:.2f}")
        L.append(f"| {t.replace('_', '-')} | " + " | ".join(cells) + " |")
    return L


def report(models) -> str:
    all_models = [m for m in (*models, REFERENCE) if _read_rows(pipeline_path(m, "test"))]
    test_rows = [r for m in all_models if (r := model_row(m, "test"))]
    dev_rows = [r for m in all_models if (r := model_row(m, "dev"))]
    judge_spend = sum((j.get("cost_usd") or 0) for m in all_models for it in load_run(m).values()
                      for j in it["judges"].values())
    L = [
        f"# LLM comparison (checklist §5) — {dt.date.today().isoformat()}",
        "",
        "Same 40 questions, **same frozen passages** for every model (exact retrieval, top-6, per-book cap 2;",
        "verified identical to the Phase 4 run). Same verification gate. Models run one at a time.",
        f"Blind judges: `{JUDGE_SMALL}` and `{JUDGE_BIG}`. Prices: `config.LLM_PRICES` (OpenAI pages, 2026-11-19).",
        f"`{REFERENCE}` is the Phase 4 run, shown as a quality reference. Judge spend for all runs: ${judge_spend:.2f}.",
        "",
        "## Held-out test set (31 questions)",
        "",
        *table(test_rows),
        "",
        "### Overall score by question type (big judge, test)",
        "",
        *per_type(all_models),
        "",
        "## Dev set (9 questions)",
        "",
        *table(dev_rows),
        "",
        "### Notes on the columns",
        "",
        "- *Invented claims* — statements the big judge flagged as wrong/made up (correct extra facts are not counted).",
        "- *Claims passing the gate* — share of the model's proposed claims that the deterministic verification",
        "  gate accepted; a low value means the model paraphrased or added things the passages do not support.",
        "- *gpt-5-mini is also a judge*: compare its rows under both judges for self-preference.",
        "- Cost is answering only (2 LLM calls per question); local models will show $0.",
    ]
    return "\n".join(L) + "\n"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", choices=["freeze", "run", "judge", "report"])
    p.add_argument("--models", nargs="*", default=list(MODELS))
    args = p.parse_args()
    config.set_profile("library")
    if args.cmd == "freeze":
        freeze()
    elif args.cmd == "run":
        run(args.models)
    elif args.cmd == "judge":
        judge(args.models)
    else:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out = REPORTS / f"llm_comparison_{dt.date.today().isoformat()}.md"
        out.write_text(report(args.models), encoding="utf-8")
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
