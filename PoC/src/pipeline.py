"""The PoC's single-lane DAT orchestrator.

    retrieve -> synthesize -> VERIFY (deterministic gate) -> generate

This is the only entry point the notebook and the Streamlit app need. It returns
every intermediate stage as well as the final answer, so the whole chain stays
inspectable - which is the point of the PoC.
"""

from __future__ import annotations

import time

import config

from . import generate as generate_stage
from . import retrieve as retrieve_stage
from . import synthesize as synthesize_stage
from . import verify as verify_stage


def answer_question(
    question: str,
    top_k: int | None = None,
    threshold: float | None = None,
) -> dict:
    started = time.time()

    passages = retrieve_stage.retrieve(question, top_k=top_k)
    synthesis = synthesize_stage.synthesize(question, passages)
    verdict = verify_stage.verify_claims(
        synthesis["claims"], passages, threshold=threshold
    )
    written = generate_stage.generate(question, verdict["verified"], passages)

    return {
        "question": question,
        "passages": passages,
        "claims": synthesis["claims"],
        "synthesis_notes": synthesis.get("notes", ""),
        "verified": verdict["verified"],
        "rejected": verdict["rejected"],
        "threshold": verdict["threshold"],
        "answer": written["answer"],
        "citations": written["citations"],
        "grounded": written["grounded"],
        "elapsed_sec": round(time.time() - started, 2),
        "config": config.summary(),
    }


def format_result(result: dict) -> str:
    """Plain-text rendering for the CLI / notebook."""
    lines = [result["answer"], ""]
    if result["citations"]:
        lines.append("Sources")
        for citation in result["citations"]:
            pages = (
                f"p.{citation['page']}"
                if citation["page"] == citation["page_end"]
                else f"pp.{citation['page']}-{citation['page_end']}"
            )
            lines.append(f"  [{citation['marker']}] {citation['book_title']}, {pages}")
    if result["rejected"]:
        lines.append("")
        lines.append(f"Dropped by the verification gate ({len(result['rejected'])}):")
        for claim in result["rejected"]:
            lines.append(f"  - ({claim['reason']}, score={claim['score']}) {claim['text']}")
    lines.append("")
    lines.append(
        f"[{result['elapsed_sec']}s | {len(result['verified'])} verified / "
        f"{len(result['claims'])} claims | threshold {result['threshold']}]"
    )
    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    question = " ".join(sys.argv[1:]).strip()
    if not question:
        question = input("Clinical question: ").strip()
    print()
    print(format_result(answer_question(question)))
