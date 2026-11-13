"""Evaluation metrics. Pure functions: no API calls, no corpus access.

Retrieval metrics (spec E-1 / E-2) take a ranked list of retrieved chunk_ids and
the set of chunk_ids a human confirmed as containing the answer. An empty
relevant set means "the answer was not found among the reviewed candidates",
which scores as a miss (0), not as "skip" - skipping would hide retrieval
failures. Questions with no label at all are excluded by the caller.
"""

from __future__ import annotations

import statistics
from typing import Iterable, Sequence

from src.verify import _content_words, _numbers


def first_relevant_rank(retrieved: Sequence[str], relevant: Iterable[str]) -> int | None:
    """1-based rank of the first relevant item, or None if none was retrieved."""
    relevant = set(relevant)
    for rank, item in enumerate(retrieved, start=1):
        if item in relevant:
            return rank
    return None


def recall_at_k(retrieved: Sequence[str], relevant: Iterable[str], k: int) -> float:
    """Hit rate: 1.0 if any relevant item is in the top k, else 0.0."""
    rank = first_relevant_rank(retrieved[:k], relevant)
    return 1.0 if rank is not None else 0.0


def reciprocal_rank(retrieved: Sequence[str], relevant: Iterable[str]) -> float:
    rank = first_relevant_rank(retrieved, relevant)
    return 0.0 if rank is None else 1.0 / rank


def precision_at_k(retrieved: Sequence[str], relevant: Iterable[str], k: int) -> float:
    """Share of the top-k slots holding a relevant item (divides by k, not by hits)."""
    if k <= 0:
        raise ValueError("k must be positive")
    relevant = set(relevant)
    return sum(1 for item in retrieved[:k] if item in relevant) / k


def citation_precision(cited: Iterable[str], relevant: Iterable[str]) -> float | None:
    """Share of cited chunk_ids that are confirmed-relevant. None if nothing cited."""
    cited = set(cited)
    if not cited:
        return None
    return len(cited & set(relevant)) / len(cited)


Span = tuple[str, int, int]  # (book_title, page, page_end)


def spans_overlap(a: Span, b: Span) -> bool:
    return a[0] == b[0] and a[1] <= b[2] and b[1] <= a[2]


def page_citation_precision(cited: Iterable[Span], relevant: Iterable[Span]) -> float | None:
    """Share of citations landing on the same book and an overlapping page range
    as a relevant chunk. More forgiving than chunk-exact matching, because
    neighbouring chunks overlap by CHUNK_OVERLAP tokens and can both hold the answer.
    """
    cited = list(cited)
    if not cited:
        return None
    relevant = list(relevant)
    hits = sum(1 for c in cited if any(spans_overlap(c, r) for r in relevant))
    return hits / len(cited)


def page_citation_hit(cited: Iterable[Span], relevant: Iterable[Span]) -> float | None:
    """1.0 if at least one citation lands on a confirmed answer page, else 0.0.
    Unlike precision, extra citations to other (possibly valid) passages are not penalised."""
    cited = list(cited)
    if not cited:
        return None
    relevant = list(relevant)
    return 1.0 if any(spans_overlap(c, r) for c in cited for r in relevant) else 0.0


def number_recall(reference: str, candidate: str) -> float | None:
    """Share of the reference answer's numbers that appear in the candidate.
    None when the reference states no numbers (metric not applicable)."""
    ref = _numbers(reference)
    if not ref:
        return None
    return len(ref & _numbers(candidate)) / len(ref)


def term_recall(reference: str, candidate: str) -> float | None:
    """Share of the reference answer's content words present in the candidate."""
    ref = _content_words(reference)
    if not ref:
        return None
    return len(ref & _content_words(candidate)) / len(ref)


def mean(values: Iterable[float | None]) -> tuple[float | None, int]:
    """Mean over non-None values, with the count actually averaged."""
    kept = [v for v in values if v is not None]
    if not kept:
        return None, 0
    return sum(kept) / len(kept), len(kept)


def percentile(values: Sequence[float], pct: float) -> float | None:
    if not values:
        return None
    if len(values) == 1:
        return float(values[0])
    return statistics.quantiles(sorted(values), n=100, method="inclusive")[int(pct) - 1]
