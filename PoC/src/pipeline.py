"""The PoC's single-lane DAT orchestrator.

    retrieve -> synthesize -> VERIFY (deterministic gate) -> generate

This is the only entry point the notebook and the Streamlit app need. It returns
every intermediate stage as well as the final answer, so the whole chain stays
inspectable - which is the point of the PoC.
"""

from __future__ import annotations

import time
from typing import Callable

import config

from . import generate as generate_stage
from . import retrieve as retrieve_stage
from . import synthesize as synthesize_stage
from . import verify as verify_stage


def answer_question(
    question: str,
    top_k: int | None = None,
    threshold: float | None = None,
    on_stage: Callable[[str], None] | None = None,
    max_per_book: int | None = None,
) -> dict:
    """Run the pipeline end to end.

    `on_stage` is called with a label as each stage begins, so a UI can report
    progress - a full run takes tens of seconds and is otherwise opaque.
    """
    started = time.time()
    report = on_stage or (lambda _label: None)

    report("Retrieving passages from the books")
    passages = retrieve_stage.retrieve(question, top_k=top_k, max_per_book=max_per_book)

    report(f"Reading {len(passages)} passages and extracting claims")
    synthesis = synthesize_stage.synthesize(question, passages)

    report(f"Verifying {len(synthesis['claims'])} claims against their sources")
    verdict = verify_stage.verify_claims(
        synthesis["claims"], passages, threshold=threshold
    )

    report(f"Writing the answer from {len(verdict['verified'])} verified claims")
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
            lines.append(f"  [{citation['marker']}] {citation['label']}")
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
    import argparse

    parser = argparse.ArgumentParser(description="Ask the VetAI pipeline a clinical question.")
    parser.add_argument("question", nargs="*", help="the question (prompted for if omitted)")
    parser.add_argument("--profile", choices=list(config.PROFILES), default=config.KB_PROFILE,
                        help="eval2 = the 2 eval books, library = all 17 books")
    parser.add_argument("--top-k", type=int, default=None)
    parser.add_argument("--max-per-book", type=int, default=None, help="0 = no cap")
    args = parser.parse_args()
    config.set_profile(args.profile)

    question = " ".join(args.question).strip() or input("Clinical question: ").strip()
    print(f"[knowledge base: {config.KB_PROFILE}]\n")
    print(format_result(answer_question(question, top_k=args.top_k, max_per_book=args.max_per_book)))
