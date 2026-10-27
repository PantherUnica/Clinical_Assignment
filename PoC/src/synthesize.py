"""Synthesis: retrieved passages -> discrete claims, each tagged with its source.

The LLM is deliberately kept on a short leash here: it sees only the retrieved
passages and must emit separate factual claims, each carrying the chunk_id(s) it
came from. It is NOT trusted - whatever it produces is then put through the
deterministic verification gate in verify.py.
"""

from __future__ import annotations

import config

from . import llm

SYSTEM = (
    "You are a veterinary evidence analyst. You answer ONLY from the passages you are given. "
    "You never use outside knowledge and never guess. "
    "You break an answer into short, self-contained factual claims. "
    "Every claim must cite the chunk_id(s) of the passage(s) it came from. "
    "If the passages do not answer the question, return an empty claims list."
)

PROMPT = """Passages retrieved from the veterinary books:

{passages}

Question from the veterinarian:
{question}

Return a single JSON object with exactly this shape:
{{
  "answerable": true or false,
  "claims": [
    {{"text": "one short factual claim", "sources": ["chunk_id", "..."]}}
  ],
  "notes": "optional short note about gaps or conflicts in the evidence"
}}

Rules:
- Every claim MUST be supported by the passage(s) it cites. Do not cite a passage that does not state it.
- Use the exact chunk_id strings shown above.
- Do not add clinical facts, drugs or doses that are absent from the passages.
- Stay close to the source's own wording. Keep its terms, units and abbreviations
  exactly as written (for example keep "q12h", "PO", "mg/kg", "SID" - do not expand
  them into prose), and keep its species labels. A claim a veterinarian can match
  word-for-word against the passage is the goal.
- Copy numbers, doses and units verbatim. Never convert, round or reformat them.
- If the passages are insufficient, set "answerable" to false and return "claims": [].
"""


def _format_passages(passages: list[dict]) -> str:
    blocks = []
    for passage in passages:
        header = (
            f"[chunk_id: {passage['chunk_id']}] "
            f"({passage['book_title']}, p.{passage['page']})"
        )
        blocks.append(f"{header}\n{passage['text']}")
    return "\n\n---\n\n".join(blocks)


def synthesize(question: str, passages: list[dict]) -> dict:
    """Produce {answerable, claims:[{text, sources}], notes}."""
    if not passages:
        return {"answerable": False, "claims": [], "notes": "no passages retrieved"}

    raw = llm.complete(
        SYSTEM,
        PROMPT.format(passages=_format_passages(passages), question=question),
        json_mode=True,
    )

    try:
        data = llm.parse_json(raw)
    except ValueError:
        return {
            "answerable": False,
            "claims": [],
            "notes": "synthesis returned unparseable output",
        }

    claims: list[dict] = []
    for item in data.get("claims") or []:
        if not isinstance(item, dict):
            continue
        text = str(item.get("text") or "").strip()
        if not text:
            continue
        sources = [s for s in (item.get("sources") or []) if isinstance(s, str)]
        claims.append({"text": text, "sources": sources})

    return {
        "answerable": bool(data.get("answerable", bool(claims))),
        "claims": claims,
        "notes": str(data.get("notes") or ""),
        "model": config.summary()["llm_model"],
    }
