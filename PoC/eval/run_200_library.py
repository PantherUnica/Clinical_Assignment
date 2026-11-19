"""The original 200 BSAVA + Blackwell questions, answered over the full 17-book index.

    python -m eval.run_200_library run [--model openai:gpt-5-mini] [--workers 4]   # resumable
    python -m eval.run_200_library export [--model openai:gpt-5-mini]

Same pipeline settings as the multi-book tests: exact retrieval, top-6 passages, max 2
per book, then synthesize -> verify -> generate. Output files use the same layout as
*_100_QA_results.md (question, topic, book answer, AI answer, citations) - no scores.
"""

from __future__ import annotations

import argparse
import json
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import config
from eval import dataset

RUNS = dataset.EVAL_DIR / "runs"
OUT_DIR = dataset.EVAL_DIR / "reports"
TOP_K, CAP = 6, 2
TITLES = {
    "bsava": ("BSAVA_formulary_100_QA_results_all_17_books", "BSAVA Small Animal Formulary"),
    "blackwell": ("Blackwells_5min_consult_100_QA_results_all_17_books",
                  "Blackwell's Five-Minute Veterinary Consult: Canine and Feline"),
}


def _tag(model: str) -> str:
    return model.split(":", 1)[-1].replace(":", "_")


def run_path(model: str):
    return RUNS / f"library17_200q_{_tag(model)}.jsonl"


def _rows(path) -> list[dict]:
    return [json.loads(l) for l in path.open(encoding="utf-8")] if path.exists() else []


def run(model: str, workers: int) -> None:
    from eval import cache
    from eval.exact_search import ExactIndex
    from src import cite, llm
    from src.pipeline import answer_from_passages

    cache.install()
    path = run_path(model)
    done = {r["id"] for r in _rows(path) if "error" not in r}
    todo = [q for q in dataset.load_questions() if q["id"] not in done]
    print(f"{model}: {len(done)} done, {len(todo)} to run -> {path.name}")
    if not todo:
        return
    index = ExactIndex("library")
    lock = threading.Lock()

    def one(q: dict) -> dict:
        passages = index.search(q["question"], top_k=TOP_K, max_per_book=CAP)
        started = time.perf_counter()
        for attempt in (1, 2):
            try:
                with llm.use_model(model):  # context vars do not cross threads: set inside the worker
                    result = answer_from_passages(q["question"], passages)
                break
            except Exception as exc:  # noqa: BLE001 - retry once, then record
                if attempt == 2:
                    return {"id": q["id"], "model": model, "error": f"{type(exc).__name__}: {exc}"}
        return {
            "id": q["id"], "model": model, "grounded": result["grounded"], "answer": result["answer"],
            "synthesis_notes": result.get("synthesis_notes", ""),
            "citations": [{"marker": c["marker"], "label": cite.source_label(c), "chunk_id": c["chunk_id"]}
                          for c in result["citations"]],
            "n_claims": len(result["claims"]), "n_verified": len(result["verified"]),
            "seconds": round(time.perf_counter() - started, 2),
        }

    finished = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(one, q) for q in todo]
        for fut in as_completed(futures):
            row = fut.result()
            with lock, path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            finished += 1
            status = "ERR " + row["error"][:70] if "error" in row else f"{row['seconds']:.0f}s"
            print(f"  [{finished}/{len(todo)}] {row['id']} {status}", flush=True)


def _flatten_headings(text: str) -> str:
    return re.sub(r"^#{1,6}\s+(.+)$", r"**\1**", text, flags=re.M)


def export(model: str) -> None:
    runs = {}
    for r in _rows(run_path(model)):
        if "error" not in r or r["id"] not in runs:
            runs[r["id"]] = r
    questions = dataset.load_questions()
    name = _tag(model)
    for book, (stem, title) in TITLES.items():
        L = [
            f"# {title}: AI answers vs book answers (all 17 books indexed, {name})",
            "",
            "Each question was run through the VetAI PoC pipeline (retrieve → synthesize → verify → generate) "
            f"with `{model}`, over the index of all 17 reference books (top-6 passages, at most 2 from any one "
            "book). The **book answer** is the answer key; the **AI answer** and **citations** are what the "
            "system produced. Citations show the book, chapter/section and page of the passage each claim was "
            "verified against (\"PDF p.\" where the book prints no page numbers).",
            "",
        ]
        answered = 0
        for q in (x for x in questions if x["book"] == book):
            row = runs.get(q["id"])
            L += [f"**{q['number']}. {q['question']}**", f"_[{q['topic']}]_", "",
                  f"**Book answer:** {q['book_answer']}", ""]
            if row is None or "error" in row:
                L += ["**AI answer:** [NOT RUN OR FAILED]", "", "**Citation(s):** none", ""]
                continue
            if row["grounded"]:
                answered += 1
                L += ["**AI answer:**", "", _flatten_headings(row["answer"].strip()), ""]
                L += ["**Citation(s):** " + "; ".join(f"[{c['marker']}] {c['label']}" for c in row["citations"]), ""]
            else:
                note = f" (Synthesis note: {row['synthesis_notes']})" if row.get("synthesis_notes") else ""
                L += [f"**AI answer:** No supported answer. \"{row['answer']}\"{note}", "",
                      "**Citation(s):** none (no claim cleared the verification gate)", ""]
        total = sum(1 for x in questions if x["book"] == book)
        L.insert(3, f"**Answered with citations: {answered} of {total}.**\n")
        out = OUT_DIR / f"{stem}_{name}.md"
        out.write_text("\n".join(L), encoding="utf-8")
        print(f"Wrote {out} ({answered}/{total} answered)")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", choices=["run", "export"])
    p.add_argument("--model", default="openai:gpt-5-mini")
    p.add_argument("--workers", type=int, default=4)
    args = p.parse_args()
    config.set_profile("library")
    if args.cmd == "run":
        run(args.model, args.workers)
    else:
        export(args.model)


if __name__ == "__main__":
    main()
