"""Export the pipeline run as readable markdown, one file per answer-key book.

    python -m eval.export_md

Reads eval/runs/pipeline_vector.jsonl and the two answer-key files; writes to
eval/reports/. Does not touch the older (wrong-book) *_results.md files.
"""

from __future__ import annotations

import re
import sys

from eval import dataset

OUT_DIR = dataset.EVAL_DIR / "reports"
RUN_PATH = dataset.EVAL_DIR / "runs" / "pipeline_vector.jsonl"

TITLES = {
    "bsava": ("BSAVA_formulary_100_QA_results_correct_books.md",
              "BSAVA Small Animal Formulary"),
    "blackwell": ("Blackwells_5min_consult_100_QA_results_correct_books.md",
                  "Blackwell's Five-Minute Veterinary Consult: Canine and Feline"),
}


def _pages(c: dict) -> str:
    return f"p.{c['page']}" if c["page"] == c["page_end"] else f"pp.{c['page']}-{c['page_end']}"


def _flatten_headings(text: str) -> str:
    """Keep each entry's own structure: turn '### Title' inside an answer into bold."""
    return re.sub(r"^#{1,6}\s+(.+)$", r"**\1**", text, flags=re.M)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    runs = {}
    for row in dataset.read_jsonl(RUN_PATH):
        if "error" not in row or row["id"] not in runs:
            runs[row["id"]] = row
    questions = dataset.load_questions()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for book, (filename, title) in TITLES.items():
        lines = [
            f"# {title}: AI answers vs book answers (correct books indexed)",
            "",
            "Each question was run through the VetAI PoC pipeline (retrieve → synthesize → "
            "verify → generate) with the index built from only the BSAVA formulary and "
            "Blackwell's Canine & Feline. The **book answer** is the answer key; the **AI "
            "answer** and **citations** are what the system produced. Citations show the "
            "book and page of the passage each claim was verified against.",
            "",
        ]
        answered = 0
        for q in (x for x in questions if x["book"] == book):
            row = runs.get(q["id"])
            lines += [f"**{q['number']}. {q['question']}**", f"_[{q['topic']}]_", "",
                      f"**Book answer:** {q['book_answer']}", ""]
            if row is None or "error" in row:
                lines += ["**AI answer:** [NOT RUN OR FAILED]", "", "**Citation(s):** none", ""]
                continue
            if row["grounded"]:
                answered += 1
                lines += ["**AI answer:**", "", _flatten_headings(row["answer"].strip()), ""]
                cites = "; ".join(f"[{c['marker']}] {c['book_title']} - {_pages(c)}"
                                  for c in row["citations"])
                lines += [f"**Citation(s):** {cites}", ""]
            else:
                note = f" (Synthesis note: {row['synthesis_notes']})" if row.get("synthesis_notes") else ""
                lines += [f"**AI answer:** No supported answer. \"{row['answer']}\"{note}", "",
                          "**Citation(s):** none (no claim cleared the verification gate)", ""]
            dropped = len(row.get("rejected", []))
            lines += [f"_Claims: {len(row['verified'])} verified / {row['n_claims']} proposed"
                      f"{f', {dropped} dropped by the gate' if dropped else ''} · "
                      f"{row['seconds']}s_", ""]
        total = sum(1 for x in questions if x["book"] == book)
        lines.insert(3, f"**Answered with citations: {answered} of {total}.**\n")
        (OUT_DIR / filename).write_text("\n".join(lines), encoding="utf-8")
        print(f"Wrote {OUT_DIR / filename}  ({answered}/{total} answered)")


if __name__ == "__main__":
    main()
