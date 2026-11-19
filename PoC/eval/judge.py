"""LLM-as-judge for the multi-book test set.

Blind: the judge sees the question, the answer key and the candidate answer with its
source labels - never which model wrote the answer. The answer key reaches the
judge only here, after the answer exists (it is never in the answering prompt).

Two judges (a small and a large model) score every answer; the report shows both
and how often they agree. Additional correct facts are not penalised, because the
key lists only some of the books that answer a question.
"""

from __future__ import annotations

from src import llm

JUDGES = ("openai:gpt-5-mini", "openai:gpt-5.5")

SYSTEM = """You are a strict, fair veterinary examiner grading an AI assistant's answer.
You are given the question, an answer key written from veterinary reference books, and the
candidate answer. Grade only what the candidate answer actually says. Return JSON only."""

PROMPT = """QUESTION
{question}

QUESTION TYPE: {qtype}
EXPECTED BEHAVIOUR: {behaviour}
{conflict}
ANSWER KEY - facts a complete answer should contain (each from the named book):
{facts}

CANDIDATE ANSWER
{answer}

CANDIDATE'S CITED SOURCES
{sources}

Grade the candidate answer:
1. For EACH numbered key fact: "present" (stated, same meaning; numbers/units must match),
   "partial" (some of it, or less specific), "missing", or "contradicted" (answer says
   something incompatible).
2. "refused": true ONLY if the answer declines to answer the question as a whole (e.g. "the
   books do not cover this"). An answer that gives substantive content and merely notes that one
   detail is missing from the evidence is NOT a refusal.
3. "conflict_handled" (only for conflict questions, else null): true if the answer shows that the
   sources give different values/recommendations and attributes them, rather than giving one value.
4. "unsupported_claims": list any statements that are clearly wrong or invented for veterinary
   medicine (do NOT list correct extra information that simply is not in the key).
5. "overall": 1-5 (5 = complete and correct, 3 = partly useful, 1 = wrong or useless).
   For an unanswerable question, a clear refusal without invented doses scores 5.

Return exactly:
{{"facts": [{{"n": 1, "verdict": "present|partial|missing|contradicted"}}],
  "refused": false, "conflict_handled": null, "unsupported_claims": [], "overall": 3,
  "reason": "one or two sentences"}}"""


def build_prompt(q: dict, answer: str, source_labels: list[str]) -> str:
    facts = "\n".join(f"{i}. {f['fact']}" for i, f in enumerate(q["key_facts"], 1)) or \
        "(none - the books do not cover this; the correct behaviour is to say so)"
    conflict = f"CONFLICT TO DETECT: {q['conflict']}\n" if q.get("conflict") else ""
    return PROMPT.format(
        question=q["question"], qtype=q["type"], behaviour=q["expected_behaviour"],
        conflict=conflict, facts=facts, answer=answer.strip() or "(empty)",
        sources="\n".join(f"- {s}" for s in source_labels) or "(none)",
    )


def judge(q: dict, answer: str, source_labels: list[str], judge_model: str) -> dict:
    with llm.use_model(judge_model), llm.track_usage() as usage:
        raw = llm.complete(SYSTEM, build_prompt(q, answer, source_labels), json_mode=True)
    try:
        out = llm.parse_json(raw)
    except Exception as exc:  # noqa: BLE001 - keep the raw text for inspection
        out = {"error": f"unparseable judge output: {exc}", "raw": raw[:2000]}
    out["judge"] = judge_model
    out["usage"] = usage
    return normalise(out, len(q["key_facts"]))


def normalise(out: dict, n_facts: int) -> dict:
    """Derived scores: fact_recall = (present + 0.5*partial) / n_facts."""
    if "error" in out:
        out["fact_recall"] = None
        return out
    verdicts = {int(f.get("n", 0)): str(f.get("verdict", "missing")).lower() for f in out.get("facts", [])}
    if n_facts:
        score = sum(1.0 if verdicts.get(i) == "present" else 0.5 if verdicts.get(i) == "partial" else 0.0
                    for i in range(1, n_facts + 1))
        out["fact_recall"] = round(score / n_facts, 3)
        out["contradicted"] = sum(1 for v in verdicts.values() if v == "contradicted")
    else:
        out["fact_recall"] = None
        out["contradicted"] = 0
    return out
