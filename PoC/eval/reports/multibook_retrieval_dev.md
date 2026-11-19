# Multi-book retrieval — dev set (step 2)

Generated 2026-11-19 · library index `9d20669390229515` (36,224 chunks) · **exact** cosine search
(`eval/exact_search.py`) · 9 dev questions (8 answerable + 1 unanswerable) · no LLM calls.

**Reproducible:** repeated runs produce byte-identical result files.

## Per-book cap comparison (answerable dev questions, top-6 = what the pipeline uses)

| Cap | Required-book cov @6 | All required @6 | Key-fact quote @6 | On-topic chunks @6 | Books w/ on-topic @6 | Multi-book Qs with ≥2 on-topic books @6 | Quote @20 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| off | 57% | 12% | 33% | 60% | 1.9 | 71% | 61% |
| 2 | 67% | 25% | 34% | 54% | 2.5 | 71% | 46% |
| 3 | 57% | 12% | 33% | 50% | 1.9 | 71% | 52% |

- **Required-book cov** — share of the question's designed books (`required_books`) in the top-6.
- **Key-fact quote** — the key fact's verbatim quote is inside a retrieved chunk (strict: one page per fact).
- **On-topic chunks** — share of the top-6 chunks matching the question's topic keywords, from *any* book.
- **Books w/ on-topic** — distinct books contributing on-topic chunks (multi-book evidence).

**Locked for the test run: cap = 2.** It brings more books into the top-6 (2.5 vs 1.9; required
coverage 57→67%) at the cost of some precision (on-topic 60→54%) and depth (quote@20). This
project is about multi-book answers, so breadth wins. Decided on dev only.

## Finding: the original answer key under-counted valid sources

Retrieval often returned a different book that also answers the question (cat meloxicam doses
appear in 7 books; ethylene glycol + fomepizole in 8). Fix, approved by the user: each question now
has `topic_groups` (keywords chosen from the question, not from retrieval output) and
`also_valid_books` found by keyword search over all 17 books. The strict required-book numbers
are still reported next to the book-agnostic on-topic numbers.

## Other notes

- Unanswerable mb-30: top similarity 0.576, below every answerable dev question (0.61–0.77) —
  a similarity floor may help refusals; to be checked in the pipeline step, not tuned on test.
- Strict key-fact metrics are low (≈34%): one page per fact, while several pages often state the
  same thing. The LLM judge in step 4 measures whether the *answer* contains the fact.
