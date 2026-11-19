# LLM comparison (checklist §5) — 2026-11-19

Same 40 questions, **same frozen passages** for every model (exact retrieval, top-6, per-book cap 2;
verified identical to the Phase 4 run). Same verification gate. Models run one at a time.
Blind judges: `openai:gpt-5-mini` and `openai:gpt-5.5`. Prices: `config.LLM_PRICES` (OpenAI pages, 2026-11-19).
`openai:gpt-5.5` is the Phase 4 run, shown as a quality reference. Judge spend for all runs: $2.28.

## Held-out test set (31 questions)

| Model | n | Fact recall (small / big judge) | Overall /5 (small / big) | Contradicted facts | Invented claims (big judge) | Citations supported in PDF | Printed page ok | Multi-book Qs citing ≥2 books | Required books cited | Claims passing the gate | Conflict shown | Correct refusal | Wrong refusal | Median s | p90 s | $ / answer | $ total |
| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `openai:gpt-5-mini` | 31 | 79% / 71% | 3.97 / 3.97 | 3 | 4 | 98% | 100% | 100% | 55% | 95% | 50% | 100% | 0% | 36 | 59 | 0.0069 | 0.21 |
| `openai:gpt-4o-mini` | 31 | 52% / 51% | 3.32 / 3.29 | 3 | 4 | 100% | 100% | 55% | 37% | 79% | 0% | 100% | 19% | 6 | 10 | 0.0008 | 0.03 |
| `openai:gpt-5.5` | 31 | 72% / 70% | 3.81 / 3.87 | 3 | 3 | 100% | 100% | 86% | 54% | 95% | 0% | 100% | 0% | 13 | 29 | 0.0566 | 1.75 |

### Overall score by question type (big judge, test)

| Type | `openai:gpt-5-mini` | `openai:gpt-4o-mini` | `openai:gpt-5.5` |
| --- | ---: | ---: | ---: |
| two-book | 3.90 | 3.20 | 3.70 |
| three-book | 3.62 | 2.25 | 3.62 |
| conflict | 2.75 | 1.75 | 2.25 |
| single-book | 4.75 | 5.00 | 5.00 |
| unanswerable | 5.00 | 5.00 | 5.00 |

## Dev set (9 questions)

| Model | n | Fact recall (small / big judge) | Overall /5 (small / big) | Contradicted facts | Invented claims (big judge) | Citations supported in PDF | Printed page ok | Multi-book Qs citing ≥2 books | Required books cited | Claims passing the gate | Conflict shown | Correct refusal | Wrong refusal | Median s | p90 s | $ / answer | $ total |
| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `openai:gpt-5-mini` | 9 | 51% / 44% | 3.00 / 2.89 | 2 | 4 | 100% | 100% | 71% | 50% | 91% | 100% | 100% | 12% | 41 | 49 | 0.0061 | 0.06 |
| `openai:gpt-4o-mini` | 9 | 39% / 40% | 2.89 / 2.78 | 0 | 2 | 100% | 100% | 57% | 44% | 75% | 0% | 100% | 25% | 6 | 8 | 0.0008 | 0.01 |
| `openai:gpt-5.5` | 9 | 58% / 51% | 3.22 / 3.22 | 2 | 2 | 100% | 100% | 71% | 50% | 100% | 100% | 100% | 12% | 12 | 23 | 0.0532 | 0.48 |

### Notes on the columns

- *Invented claims* — statements the big judge flagged as wrong/made up (correct extra facts are not counted).
- *Claims passing the gate* — share of the model's proposed claims that the deterministic verification
  gate accepted; a low value means the model paraphrased or added things the passages do not support.
- *gpt-5-mini is also a judge*: compare its rows under both judges for self-preference.
- Cost is answering only (2 LLM calls per question); local models will show $0.
