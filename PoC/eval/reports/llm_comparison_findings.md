# LLM comparison — findings and recommendation (Phase 5)

Run 2026-11-19 · 31 held-out test questions · identical frozen passages for every model ·
blind judges gpt-5-mini + gpt-5.5 · full tables in `llm_comparison_2026-11-19.md`.

| | gpt-5-mini | gpt-4o-mini | gpt-5.5 (reference) |
| --- | ---: | ---: | ---: |
| Overall /5 (big judge) | **3.97** | 3.29 | 3.87 |
| Fact recall (big judge) | **71%** | 51% | 70% |
| Multi-book Qs citing ≥2 books | **100%** | 55% | 86% |
| Three-book questions, overall /5 | 3.62 | 2.25 | 3.62 |
| Conflict shown (4 questions) | **2/4** | 0/4 | 0/4 |
| Wrong refusals (answerable refused) | 0% | **19%** | 0% |
| Correct refusals (unanswerable) | 100% | 100% | 100% |
| Citations supported in PDF / printed page ok | 98% / 100% | 100% / 100% | 100% / 100% |
| Median / p90 response time | 36 s / 59 s | **6 s / 10 s** | 13 s / 29 s |
| Cost per answer | $0.0069 | **$0.0008** | $0.057 |

## Recommendation (among the GPT models tested)

**gpt-5-mini** — same or better answer quality than gpt-5.5 at about **1/8 of the cost**, and the
best multi-book synthesis. Two caveats:

1. **Slow:** median 36 s per answer (it is a reasoning model) — about 3x gpt-5.5 and 6x gpt-4o-mini.
   Acceptable for a clinical reference tool; not for chat-speed use.
2. **Deprecated:** OpenAI's model page marks gpt-5-mini as deprecated. It still works today, but
   plan for its newer replacement and re-run this comparison (one command) when switching.

**gpt-4o-mini is not recommended** as the answer model: fastest and cheapest, but it refuses 19% of
answerable questions, rarely combines books (55%), and scores lowest on three-book and conflict questions.

## How much to trust these numbers

- 31 questions: differences of ~0.1–0.2 points (gpt-5-mini vs gpt-5.5) are within noise; the gap to
  gpt-4o-mini (~0.7 points, 19% wrong refusals) is clear.
- Conflict results rest on 4 questions. All models are limited by retrieval: the second book of a
  conflict is often missing from the top-6 (see `multibook_findings.md`).
- **No judge self-preference seen:** gpt-5-mini's answers score 3.97 from itself and 3.97 from gpt-5.5.

## Not yet done (checklist §5)

Local Hugging Face models (Qwen, Llama, Gemma, Mistral) — the runner supports them already:
`python -m eval.compare_llms run --models ollama:qwen2.5:7b` (then `judge` and `report`).
The final model choice should wait for that run.
