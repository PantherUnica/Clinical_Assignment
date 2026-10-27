"""The deterministic citation-verification gate.

This is the component that makes the product trustworthy, and it is NOT an LLM.
Given the same claim and the same cited passage it always returns the same
verdict - the reproducibility the spec demands of verification (metric E-3).

A claim must clear three checks, in this order:

  1. STRUCTURAL - it cites at least one chunk_id that was actually retrieved.
     Pure code, no embedding call, so this half of the gate cannot be disabled
     by an unavailable embedding service. Rejects: no_citation, unknown_citation.

  2. NUMERIC - every number the claim states occurs in the passage it cites.
     Word overlap cannot catch a fabricated dose, because an invented figure
     reuses the source's wording exactly; doses are the highest-harm thing this
     system can get wrong. Rejects: number_not_in_source.

  3. SUPPORT - score = w * lexical_coverage + (1 - w) * best_window_cosine
     reaches VERIFY_THRESHOLD for at least one cited passage. The cosine term
     uses the best-matching sentence window inside the passage rather than the
     whole passage, which would ask "is this passage entirely about the claim?"
     instead of "does it contain something supporting it?".
     Rejects: unsupported_by_source.

Anything rejected is dropped with a reason and never reaches generation. Only
claims surviving checks 1-2 are embedded, so cost tracks the survivors. Every
verdict carries claim_index, keeping it traceable to the claim that produced it
even when two claims read identically.
"""

from __future__ import annotations

import re

import config

from . import embeddings

_STOPWORDS = {
    "the", "and", "for", "are", "but", "not", "you", "all", "any", "can", "had",
    "her", "was", "one", "our", "out", "has", "him", "his", "how", "its", "may",
    "new", "now", "old", "see", "two", "who", "did", "get", "use", "with", "this",
    "that", "from", "they", "been", "have", "more", "will", "them", "then", "than",
    "when", "which", "their", "there", "these", "those", "would", "could", "should",
    "also", "into", "such", "some", "most", "other", "often", "usually",
    "both", "each", "while", "being", "were", "does", "about", "after", "before",
}


def _stem(word: str) -> str:
    """Crude singular form so 'dogs' matches the book's 'Dog'."""
    if len(word) > 3 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("es") and not word.endswith("ses"):
        return word[:-2]
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def _content_words(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {_stem(w) for w in words if len(w) > 2 and w not in _STOPWORDS}


def lexical_coverage(claim_text: str, passage_text: str) -> float:
    """Fraction of the claim's content words that appear in the passage."""
    claim_words = _content_words(claim_text)
    if not claim_words:
        return 0.0
    return len(claim_words & _content_words(passage_text)) / len(claim_words)


_WINDOW_SENTENCES = 3
_WINDOW_STEP = 1
_MAX_WINDOWS = 40


def sentence_windows(text: str, size: int = _WINDOW_SENTENCES) -> list[str]:
    """Overlapping sentence windows within a passage.

    A chunk is ~600 tokens and often covers a whole topic (cause, diagnosis and
    several treatments). Comparing a single claim against the whole chunk asks
    "is this passage entirely about this claim?" when the question that matters
    is "does this passage contain something that supports it?". Scoring against
    the best window asks the right one.
    """
    sentences = [s.strip() for s in re.split(r"(?<=[.!?;])\s+", text) if s.strip()]
    if len(sentences) <= size:
        return [text]
    windows = [
        " ".join(sentences[i : i + size])
        for i in range(0, len(sentences) - size + 1, _WINDOW_STEP)
    ]
    if len(windows) > _MAX_WINDOWS:  # keep the embedding call bounded
        stride_n = len(windows) / _MAX_WINDOWS
        windows = [windows[int(i * stride_n)] for i in range(_MAX_WINDOWS)]
    return windows


def _numbers(text: str) -> set[float]:
    """Numeric values in the text, dash variants normalised ('10-30' -> 10, 30)."""
    flat = text.replace("–", "-").replace("—", "-")
    found = set()
    for token in re.findall(r"\d+(?:\.\d+)?", flat):
        try:
            found.add(float(token))
        except ValueError:
            continue
    return found


def unsourced_numbers(claim_text: str, passage_text: str) -> set[float]:
    """Numbers asserted by the claim that do not occur in the passage.

    Word overlap alone cannot catch a fabricated dose: "Dog: 500 mg/kg PO q4h"
    reuses the source's exact wording and only the figures are invented. Doses
    are the highest-harm thing this system can get wrong, so any number the
    claim states must actually appear in the passage it cites.
    """
    return _numbers(claim_text) - _numbers(passage_text)


def verify_claims(
    claims: list[dict],
    passages: list[dict],
    threshold: float | None = None,
    lexical_weight: float | None = None,
) -> dict:
    """Split claims into verified / rejected. Deterministic."""
    threshold = config.VERIFY_THRESHOLD if threshold is None else threshold
    lexical_weight = (
        config.VERIFY_LEXICAL_WEIGHT if lexical_weight is None else lexical_weight
    )

    by_id = {p["chunk_id"]: p for p in passages}
    verified: list[dict] = []
    rejected: list[dict] = []

    # Pass 1 - structural checks. Pure code: no embeddings, no API call, so a
    # claim that cites nothing (or cites something never retrieved) is rejected
    # even if the embedding service is unavailable.
    # claim_index keeps every verdict traceable to the claim that produced it,
    # even when two claims have identical text (needed for the audit trail).
    candidates: list[tuple[int, dict, list[str]]] = []
    for index, claim in enumerate(claims):
        cited = claim.get("sources") or []

        if not cited:
            rejected.append(
                {**claim, "claim_index": index, "reason": "no_citation", "score": 0.0}
            )
            continue

        known = [cid for cid in cited if cid in by_id]
        if not known:
            rejected.append(
                {**claim, "claim_index": index, "reason": "unknown_citation", "score": 0.0}
            )
            continue

        candidates.append((index, claim, known))

    if not candidates:
        return {"verified": verified, "rejected": rejected, "threshold": threshold}

    # Pass 2 - support scoring. Embeds only the surviving claims and the
    # passages they actually cite.
    claim_vectors = embeddings.embed_texts([claim["text"] for _, claim, _ in candidates])
    cited_ids = sorted({cid for _, _, known in candidates for cid in known})

    # Embed each cited passage plus its sentence windows, in one batched call.
    window_index: list[tuple[str, str]] = [(cid, by_id[cid]["text"]) for cid in cited_ids]
    for cid in cited_ids:
        for window in sentence_windows(by_id[cid]["text"]):
            if window != by_id[cid]["text"]:
                window_index.append((cid, window))

    window_vectors: dict[str, list[list[float]]] = {}
    for (cid, _), vector in zip(
        window_index, embeddings.embed_texts([text for _, text in window_index])
    ):
        window_vectors.setdefault(cid, []).append(vector)

    for (index, claim, known), claim_vector in zip(candidates, claim_vectors):
        best = {"chunk_id": None, "score": -1.0, "lexical": 0.0, "cosine": 0.0}
        missing_numbers: set[float] = set()

        for chunk_id in known:
            unsourced = unsourced_numbers(claim["text"], by_id[chunk_id]["text"])
            if unsourced:
                # This passage does not state the figures the claim asserts, so
                # it cannot support it however well the wording matches.
                missing_numbers |= unsourced
                continue

            lexical = lexical_coverage(claim["text"], by_id[chunk_id]["text"])
            # Best-matching window, not the diluted whole-passage average.
            cosine = max(
                embeddings.cosine(claim_vector, vector)
                for vector in window_vectors[chunk_id]
            )
            score = lexical_weight * lexical + (1.0 - lexical_weight) * cosine
            if score > best["score"]:
                best = {
                    "chunk_id": chunk_id,
                    "score": score,
                    "lexical": lexical,
                    "cosine": cosine,
                }

        if best["chunk_id"] is None:
            rejected.append(
                {
                    **claim,
                    "claim_index": index,
                    "sources": known,
                    "reason": "number_not_in_source",
                    "score": 0.0,
                    "unsourced_numbers": sorted(missing_numbers),
                }
            )
            continue

        record = {
            **claim,
            "claim_index": index,
            "sources": known,
            "best_source": best["chunk_id"],
            "score": round(best["score"], 4),
            "lexical": round(best["lexical"], 4),
            "cosine": round(best["cosine"], 4),
        }

        if best["score"] >= threshold:
            verified.append(record)
        else:
            rejected.append({**record, "reason": "unsupported_by_source"})

    return {"verified": verified, "rejected": rejected, "threshold": threshold}
