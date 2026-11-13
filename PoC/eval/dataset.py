"""Load the 200-question set and the labeled subset.

Questions come straight from the two answer-key files at the repo root, so the
eval always uses the exact wording and book answers the user supplied.
"""

from __future__ import annotations

import json
import random
import re
from collections import defaultdict
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = EVAL_DIR.parents[1]
DATA_DIR = EVAL_DIR / "data"
SUBSET_PATH = DATA_DIR / "questions_subset.jsonl"
LABELS_PATH = DATA_DIR / "labels.jsonl"

# book key -> (answer-key file, id prefix, substring identifying the indexed book_title)
SOURCES = {
    "bsava": (REPO_ROOT / "BSAVA_formulary_100_QA.md", "bsava", "bsava"),
    "blackwell": (REPO_ROOT / "Blackwells_5min_consult_100_QA.md", "bw", "blackwell"),
}

_ENTRY = re.compile(
    r"\*\*(\d+)\.\s*(.+?)\*\*\s*\n_\[(.+?)\]_\s*\n(.+?)(?=\n\n\*\*\d+\.|\Z)",
    re.DOTALL,
)

_CATEGORY_RULES = [
    ("dose", ("dose", "dosed", "dosing", "protocol", "regimen", "mac of", "how often",
              "how long is", "how long can", "how is", "how are")),
    ("predisposition", ("breed", "predisposed", "susceptible", "at risk", "signalment",
                        "which dogs", "which cats", "which animals", "what age",
                        "at what age", "mean age", "typical age")),
    ("contraindication", ("avoid", "contraindicat", "not be used", "not be given",
                          "should not", "must not", "not recommended", "why must",
                          "why should")),
]


def categorize(question: str) -> str:
    """Heuristic question category, used only for the per-category breakdown."""
    q = question.lower()
    for name, cues in _CATEGORY_RULES:
        if any(cue in q for cue in cues):
            return name
    return "concept"


def book_matches(book_key: str, book_title: str) -> bool:
    return SOURCES[book_key][2] in book_title.lower()


def load_questions() -> list[dict]:
    """All 200 questions as {id, book, number, question, topic, book_answer, category, has_numbers}."""
    questions: list[dict] = []
    for book_key, (path, prefix, _) in SOURCES.items():
        entries = list(_ENTRY.finditer(path.read_text(encoding="utf-8")))
        if len(entries) != 100:
            raise ValueError(f"{path.name}: parsed {len(entries)} entries, expected 100")
        for match in entries:
            number = int(match.group(1))
            question = " ".join(match.group(2).split())
            answer = " ".join(match.group(4).split())
            questions.append(
                {
                    "id": f"{prefix}-{number:03d}",
                    "book": book_key,
                    "number": number,
                    "question": question,
                    "topic": match.group(3).strip(),
                    "book_answer": answer,
                    "category": categorize(question),
                    "has_numbers": bool(re.search(r"\d", answer)),
                }
            )
    return questions


def make_subset(questions: list[dict], per_book: int = 20, seed: int = 42) -> list[dict]:
    """Stratified sample: per_book questions from each book, spread across categories."""
    rng = random.Random(seed)
    subset: list[dict] = []
    for book_key in SOURCES:
        by_cat: dict[str, list[dict]] = defaultdict(list)
        for q in questions:
            if q["book"] == book_key:
                by_cat[q["category"]].append(q)
        pools = {cat: rng.sample(items, len(items)) for cat, items in sorted(by_cat.items())}
        picked: list[dict] = []
        while len(picked) < per_book and any(pools.values()):
            for cat in sorted(pools):  # round-robin keeps categories balanced
                if pools[cat] and len(picked) < per_book:
                    picked.append(pools[cat].pop())
        subset.extend(sorted(picked, key=lambda q: q["number"]))
    return subset


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def load_subset() -> list[dict]:
    rows = read_jsonl(SUBSET_PATH)
    if not rows:
        raise FileNotFoundError(f"{SUBSET_PATH} missing. Run: python -m eval.build_labels propose")
    return rows


def load_labels() -> dict[str, dict]:
    """question id -> {relevant_chunk_ids: [...], status: 'found' | 'miss'}."""
    return {row["id"]: row for row in read_jsonl(LABELS_PATH)}
