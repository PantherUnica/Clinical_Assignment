"""Phase 4/5 reports from the multi-book runs (no API calls).

    python -m eval.multibook_report multibook  --model openai:gpt-5.5   # -> reports/multibook_<date>.md
    python -m eval.multibook_report spotcheck  --model openai:gpt-5.5   # -> reports/citation_spotcheck.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import random
import statistics
from collections import defaultdict

import config
from eval.run_multibook import (
    _avg, _pct, _read_rows, judge_path, load_questions, pipeline_path,
)

JUDGE_SMALL, JUDGE_BIG = "openai:gpt-5-mini", "openai:gpt-5.5"
REPORTS = config.POC_ROOT / "eval" / "reports"
TYPES = ("two_book", "three_book", "conflict", "single_book", "unanswerable")


def load_run(model: str, splits=("dev", "test")) -> dict[str, dict]:
    """id -> {q, answer, judges{judge: row}} for every question with a successful answer."""
    qs = {q["id"]: q for q in load_questions()}
    out: dict[str, dict] = {}
    for split in splits:
        for a in _read_rows(pipeline_path(model, split)):
            if "error" not in a:
                out[a["id"]] = {"q": qs[a["id"]], "answer": a, "judges": {}}
        for j in _read_rows(judge_path(model, split)):
            if j["id"] in out and "error" not in j:
                out[j["id"]]["judges"][j["judge"]] = j
    return out


def metrics(item: dict) -> dict:
    """Per-question numbers used by every table."""
    q, a, js = item["q"], item["answer"], item["judges"]
    cited = {c["book_id"] for c in a["citations"]}
    valid = set(q["required_books"]) | set(q.get("also_valid_books", {}))
    checks = a["citation_checks"]
    m = {
        "id": q["id"], "type": q["type"], "split": q["split"],
        "seconds": a["seconds"], "cost": a["cost_usd"],
        "grounded": a["grounded"],
        "required_cited": (len(cited & set(q["required_books"])) / len(q["required_books"])) if q["required_books"] else None,
        "valid_cited": (len(cited & valid) / len(cited)) if cited else None,
        "n_books_cited": len(cited),
        "required_retrieved": (len({p["book_id"] for p in a["passages"]} & set(q["required_books"]))
                               / len(q["required_books"])) if q["required_books"] else None,
        "supported": _avg(float(c["supported"]) for c in checks),
        "page_ok": _avg(None if c["page_ok"] is None else float(c["page_ok"]) for c in checks),
        "n_citation_checks": len(checks),
    }
    for name, key in ((JUDGE_SMALL, "s"), (JUDGE_BIG, "b")):
        j = js.get(name, {})
        m[f"recall_{key}"] = j.get("fact_recall")
        m[f"overall_{key}"] = j.get("overall")
        m[f"refused_{key}"] = j.get("refused")
        m[f"conflict_{key}"] = j.get("conflict_handled")
        m[f"contradicted_{key}"] = j.get("contradicted")
        m[f"unsupported_{key}"] = len(j.get("unsupported_claims") or [])
    # refusal: deterministic (no grounded answer) OR the big judge says the answer declined
    m["refused"] = (not a["grounded"]) or bool(m["refused_b"])
    return m


def _mean(vals) -> float | None:
    v = [x for x in vals if x is not None]
    return statistics.mean(v) if v else None


def _num(v, d=1) -> str:
    return "—" if v is None else f"{v:.{d}f}"


def group_table(rows: list[dict]) -> list[str]:
    L = ["| Group | n | Required books cited | ≥2 books cited | Citations supported in PDF | Printed page ok "
         "| Fact recall (small / big judge) | Overall /5 (small / big) | Conflict shown | Correct refusal | Wrong refusal | Median s | $ / answer |",
         "| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |"]

    def line(label, rs):
        if not rs:
            return
        ans = [r for r in rs if r["type"] != "unanswerable"]
        un = [r for r in rs if r["type"] == "unanswerable"]
        multi = [r for r in ans if r["type"] in ("two_book", "three_book", "conflict")]
        conf = [r for r in rs if r["type"] == "conflict"]
        L.append(
            f"| {label} | {len(rs)} | {_pct(_mean(r['required_cited'] for r in ans))} | "
            f"{_pct(_mean(float(r['n_books_cited'] >= 2) for r in multi)) if multi else '—'} | "
            f"{_pct(_mean(r['supported'] for r in ans))} | {_pct(_mean(r['page_ok'] for r in ans))} | "
            f"{_pct(_mean(r['recall_s'] for r in ans))} / {_pct(_mean(r['recall_b'] for r in ans))} | "
            f"{_num(_mean(r['overall_s'] for r in rs))} / {_num(_mean(r['overall_b'] for r in rs))} | "
            f"{_pct(_mean(None if r['conflict_b'] is None else float(r['conflict_b']) for r in conf)) if conf else '—'} | "
            f"{_pct(_mean(float(r['refused']) for r in un)) if un else '—'} | "
            f"{_pct(_mean(float(r['refused']) for r in ans)) if ans else '—'} | "
            f"{_num(statistics.median(r['seconds'] for r in rs), 0)} | "
            f"{_num(_mean(r['cost'] for r in rs), 3)} |"
        )

    by_type = defaultdict(list)
    for r in rows:
        by_type[r["type"]].append(r)
    for t in TYPES:
        line(t.replace("_", "-"), by_type[t])
    line("**all**", rows)
    return L


def agreement(rows: list[dict], items: dict) -> list[str]:
    both = [r for r in rows if r["overall_s"] is not None and r["overall_b"] is not None]
    if not both:
        return ["No questions with both judges."]
    exact = _mean(float(r["overall_s"] == r["overall_b"]) for r in both)
    within1 = _mean(float(abs(r["overall_s"] - r["overall_b"]) <= 1) for r in both)
    refuse = _mean(float(bool(r["refused_s"]) == bool(r["refused_b"])) for r in both)
    fact_pairs = []
    for r in both:
        js = items[r["id"]]["judges"]
        vs = {f["n"]: f["verdict"] for f in js[JUDGE_SMALL].get("facts", [])}
        vb = {f["n"]: f["verdict"] for f in js[JUDGE_BIG].get("facts", [])}
        fact_pairs += [float(vs.get(n) == vb.get(n)) for n in vb]
    bias = _mean(r["overall_s"] - r["overall_b"] for r in both)
    return [
        f"- Overall score identical: **{_pct(exact)}**; within 1 point: **{_pct(within1)}** ({len(both)} answers)",
        f"- Same per-fact verdict: **{_pct(_mean(fact_pairs))}** ({len(fact_pairs)} facts)",
        f"- Same refusal decision: **{_pct(refuse)}**",
        f"- Small judge minus big judge, mean overall: **{bias:+.2f}** (positive = small judge is more generous)",
    ]


def build_multibook(model: str) -> str:
    items = load_run(model)
    rows = [metrics(it) for it in items.values()]
    test = [r for r in rows if r["split"] == "test"]
    dev = [r for r in rows if r["split"] == "dev"]
    cost_ans = sum(r["cost"] or 0 for r in rows)
    cost_judge = sum((j.get("cost_usd") or 0) for it in items.values() for j in it["judges"].values())
    L = [
        f"# Multi-book testing (checklist §4) — {model}",
        "",
        f"Generated {dt.datetime.now():%Y-%m-%d %H:%M} · library index (36,224 chunks, 17 books) · exact retrieval "
        f"top-6 with per-book cap 2 (chosen on dev) · answers by `{model}` · blind judges `{JUDGE_SMALL}` and `{JUDGE_BIG}`.",
        f"Questions: {len(test)} held-out test + {len(dev)} dev. Spend: answers ${cost_ans:.2f}, judges ${cost_judge:.2f}.",
        "",
        "## Held-out test set (headline)",
        "",
        *group_table(test),
        "",
        "## Dev set (used to choose settings — not a clean estimate)",
        "",
        *group_table(dev),
        "",
        "### How to read the columns",
        "",
        "- **Required books cited** — share of the books the question was designed around that the answer cites.",
        "- **≥2 books cited** — multi-book questions whose answer cites at least two books.",
        "- **Citations supported in PDF** — claim's content words found on the cited page, re-read from the original PDF.",
        "- **Printed page ok** — the printed page shown matches the PDF's page label / printed number (Ettinger prints none).",
        "- **Fact recall** — key facts judged present (partial = ½). The key lists only some valid books, so answers using",
        "  other correct books can score lower here without being wrong.",
        "- **Correct refusal** — unanswerable questions answered with \"not in the books\". **Wrong refusal** — answerable ones refused.",
        "",
        "## Judge agreement (small vs big judge, all answers)",
        "",
        *agreement(rows, items),
        "",
        "## Retrieval vs answer (test)",
        "",
        f"- Required books present in the top-6 passages: **{_pct(_mean(r['required_retrieved'] for r in test if r['type'] != 'unanswerable'))}**",
        f"- Required books cited in the answer: **{_pct(_mean(r['required_cited'] for r in test if r['type'] != 'unanswerable'))}**",
        f"- Cited books that are on the question's valid list (required + also-valid): "
        f"**{_pct(_mean(r['valid_cited'] for r in test))}**",
        "",
        "## Per question (test)",
        "",
        "| Q | Type | Books cited | Required cited | Supported | Fact recall s / b | Overall s / b | Refused | Notes (big judge) |",
        "| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |",
    ]
    for r in sorted(test, key=lambda r: r["id"]):
        reason = (items[r["id"]]["judges"].get(JUDGE_BIG, {}).get("reason") or "").replace("|", "/")[:160]
        L.append(f"| {r['id']} | {r['type']} | {r['n_books_cited']} | {_pct(r['required_cited'])} | {_pct(r['supported'])} | "
                 f"{_pct(r['recall_s'])} / {_pct(r['recall_b'])} | {r['overall_s']} / {r['overall_b']} | "
                 f"{'yes' if r['refused'] else 'no'} | {reason} |")
    weak = [r for r in test if r["type"] != "unanswerable" and (r["recall_b"] or 0) < 0.5]
    L += ["", "## Where it fell short (test, big-judge fact recall < 50%)", ""]
    for r in sorted(weak, key=lambda r: r["id"]):
        it = items[r["id"]]
        missing = [it["q"]["required_books"][i] for i in range(len(it["q"]["required_books"]))
                   if it["q"]["required_books"][i] not in {p["book_id"] for p in it["answer"]["passages"]}]
        cause = f"required book(s) not retrieved: {', '.join(missing)}" if missing else "required books were retrieved"
        L.append(f"- **{r['id']}** ({r['type']}) — {cause}. Judge: {it['judges'].get(JUDGE_BIG, {}).get('reason', '')}")
    if not weak:
        L.append("- none")
    return "\n".join(L) + "\n"


def build_spotcheck(model: str, n: int = 30, seed: int = 7) -> str:
    items = load_run(model)
    rows = []
    for it in items.values():
        for c in it["answer"]["citation_checks"]:
            rows.append((it["q"]["id"], c))
    random.Random(seed).shuffle(rows)
    from src import library

    titles = {b["book_id"]: b["title"] for b in library.load_manifest()}
    L = [
        "# Citation spot-check — verify against the original PDFs",
        "",
        f"{min(n, len(rows))} random citations (seed {seed}) out of {len(rows)} from the `{model}` run. For each row:",
        "open the PDF at the **PDF page**, check the claim is supported there, and that the printed page",
        "number matches. Put ✔ or ✘ in the last two columns. The `Auto` columns are the script's own check.",
        "",
        "| # | Q | Book | PDF page | Printed page | Claim | Auto: supported | Auto: page | You: supported | You: page |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for k, (qid, c) in enumerate(rows[:n], 1):
        pages = c["pdf_pages"]
        pdf = f"{pages[0]}" if pages[0] == pages[1] else f"{pages[0]}–{pages[1]}"
        claim = c["claim"].replace("|", "/")
        auto_page = "n/a" if c["page_ok"] is None else ("✔" if c["page_ok"] else "✘")
        L.append(f"| {k} | {qid} | {titles.get(c['book_id'], c['book_id'])} | {pdf} | {c['printed_page'] or '—'} | "
                 f"{claim} | {'✔' if c['supported'] else '✘'} ({c['coverage']}) | {auto_page} |  |  |")
    return "\n".join(L) + "\n"


def recheck(model: str) -> None:
    """Recompute the deterministic citation checks in saved runs (no API calls)."""
    import json

    from eval.citation_check import check_result

    for split in ("dev", "test"):
        path = pipeline_path(model, split)
        rows = _read_rows(path)
        for r in rows:
            if "error" not in r:
                r["citation_checks"] = check_result(r["verified"], r["passages"])
        path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
        print(f"rechecked {path.name}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["multibook", "spotcheck", "recheck"])
    p.add_argument("--model", default=f"openai:{config.OPENAI_MODEL}")
    args = p.parse_args()
    config.set_profile("library")
    REPORTS.mkdir(parents=True, exist_ok=True)
    if args.cmd == "recheck":
        recheck(args.model)
        return
    if args.cmd == "multibook":
        out = REPORTS / f"multibook_{dt.date.today().isoformat()}.md"
        out.write_text(build_multibook(args.model), encoding="utf-8")
    else:
        out = REPORTS / "citation_spotcheck.md"
        out.write_text(build_spotcheck(args.model), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
