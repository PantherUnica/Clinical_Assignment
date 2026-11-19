# Multi-book pipeline — pilot (step 3)

2026-11-19 · 3 dev questions · answering model `openai:gpt-5.5` · exact retrieval top-6, cap 2 ·
judges `openai:gpt-5-mini` + `openai:gpt-5.5` (blind).

| Q | Type | Time s | Answer $ | Claims kept | Cited books | Citations supported (PDF) | Printed page ok | Judge gpt-5-mini | Judge gpt-5.5 | Judges $ |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |
| mb-01 | two_book | 23 | 0.0644 | 8/8 | 3 | 100% | 100% | 3/5, facts 50% | 3/5, facts 50% | 0.024 |
| mb-15 | three_book | 20 | 0.0726 | 7/7 | 2 | 100% | 100% | 4/5, facts 83% | 4/5, facts 83% | 0.022 |
| mb-30 | unanswerable | 2 | 0.0238 | 0/0 | 0 | — | — | 5/5 refused | 5/5 refused | 0.009 |

Tokens per answered question ≈ 4.7k in / 1.5k out; time is mostly the synthesize stage (10–15 s).

## What the pilot caught

1. **Judge rubric bug (fixed):** the large judge marked mb-01 as "refused" because the answer said
   the dose was not in the evidence. Rubric now says a refusal means declining the whole question.
   After the fix both judges agree on all three.
2. **Retrieval miss, handled honestly:** for mb-01 the top-6 had no Plumb's fomepizole dose page,
   so the answer said the dose was not in the evidence instead of inventing one.
3. **Unanswerable (Librela):** refused without an invented dose — 5/5 from both judges.

## Cost projection (prices in `config.LLM_PRICES`, OpenAI pages checked 2026-11-19)

| Run | Estimate |
| --- | ---: |
| Phase 4 rest (37 questions, gpt-5.5 + both judges) | ≈ $3.1 |
| Phase 5 (40 questions × gpt-5-mini + gpt-4o-mini + both judges) | ≈ $2.0 |
| **Total** | **≈ $5** |

Time ≈ 15 min answering + 10 min judging per model run.
