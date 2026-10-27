"""Grounded generation: write the answer over verified claims only.

If nothing survived the verification gate we return the honest "no evidence"
answer WITHOUT calling the LLM at all - so there is no path by which an
unsupported answer can be produced.
"""

from __future__ import annotations

from . import llm

NO_EVIDENCE = (
    "I could not find evidence in the indexed books to support an answer to this question. "
    "Rather than guess, I am reporting that the evidence is missing. "
    "Nothing here is stated without a verified source."
)

SYSTEM = (
    "You write the final answer for a practising veterinarian. "
    "You may use ONLY the verified claims provided. "
    "You must not add any clinical fact, differential, drug or dose that is not in those claims. "
    "Keep every citation marker exactly where it belongs, immediately after the statement it supports. "
    "Be concise and clinical. The veterinarian makes the decision, not you."
)

PROMPT = """Verified claims (each already checked against its source):

{claims}

Question from the veterinarian:
{question}

Write a clear, well-organised answer to the question using only the claims above.
Carry the [n] citation markers through into your prose, immediately after the
statement each one supports. Do not introduce any new facts. Do not add a
reference list - that is rendered separately. If the claims only partially answer
the question, say plainly what is not covered by the evidence.
"""


def build_citations(verified: list[dict], passages: list[dict]) -> tuple[list[dict], dict]:
    """Assign [1], [2]... to each distinct cited chunk, in order of first use."""
    by_id = {p["chunk_id"]: p for p in passages}
    citations: list[dict] = []
    marker_by_id: dict[str, int] = {}

    for claim in verified:
        for chunk_id in claim.get("sources") or []:
            if chunk_id in marker_by_id or chunk_id not in by_id:
                continue
            passage = by_id[chunk_id]
            marker = len(citations) + 1
            marker_by_id[chunk_id] = marker
            citations.append(
                {
                    "marker": marker,
                    "chunk_id": chunk_id,
                    "book_title": passage["book_title"],
                    "page": passage["page"],
                    "page_end": passage["page_end"],
                    "text": passage["text"],
                    "similarity": passage.get("similarity"),
                }
            )
    return citations, marker_by_id


def generate(question: str, verified: list[dict], passages: list[dict]) -> dict:
    if not verified:
        return {"answer": NO_EVIDENCE, "citations": [], "grounded": False}

    citations, marker_by_id = build_citations(verified, passages)

    lines = []
    for claim in verified:
        markers = sorted({marker_by_id[c] for c in claim["sources"] if c in marker_by_id})
        tags = "".join(f"[{m}]" for m in markers)
        lines.append(f"- {claim['text']} {tags}")

    answer = llm.complete(
        SYSTEM, PROMPT.format(claims="\n".join(lines), question=question)
    )

    return {
        "answer": answer.strip() or NO_EVIDENCE,
        "citations": citations,
        "grounded": True,
    }
