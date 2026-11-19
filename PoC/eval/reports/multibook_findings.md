# Multi-book testing — key findings (Phase 4)

Run 2026-11-19 · answers `openai:gpt-5.5` · 31 held-out test + 9 dev questions · exact retrieval
top-6, per-book cap 2 · full numbers in `multibook_2026-11-19.md`, citations to hand-check in
`citation_spotcheck.md`. Spend $3.03 (answers $2.23, judges $0.80).

## What works

1. **Citations are trustworthy.** 100% of cited claims were found on the cited page when re-read
   from the original PDF; printed page numbers: 191 confirmed, **0 wrong**, 32 not verifiable
   (Ettinger prints no page numbers; a few figure pages).
2. **No invented answers.** All 6 unanswerable questions (Librela, Zenrelia, Varenzin, tirzepatide,
   injectable fluralaner, NexGard COMBO) were refused without a made-up dose — 5/5 from both judges.
3. **Multi-book answers.** 90% of two-book and 100% of three-book test answers cite ≥2 books;
   every cited book is one that actually covers the topic.
4. **Single-book control** questions: 4/4 fully correct (no harm from the multi-book setup).

## What does not work yet

1. **Conflicts are not surfaced (0/4 on test).** Answers give one source's value (e.g. parvo
   booster "every 3 years" only, Schirmer value for cats only). Main cause is retrieval: the second
   book of the conflict is often not in the top-6 (Vaccination Schedule, Blackwell/Ettinger for
   Schirmer). The answer prompt also does not ask the model to look for disagreement.
2. **Retrieval misses required books.** Required books in the top-6: 69% (test); cited: 54%.
   When a book is missing, the answer is correct but incomplete (fact recall ≈ 70%, overall ≈ 3.8/5).
3. **One wrong refusal (dev, mb-08 pancreatitis).** Half the answer was in the passages, but the
   synthesize step marked the whole question "not answerable". Not seen on the test set (0/26).

## Judges

Small (gpt-5-mini) and big (gpt-5.5) judges: within 1 point on 100% of answers, identical score on
55%, same per-fact verdict 76%, same refusal decision 100%, no systematic leniency (−0.05).
→ The cheaper judge is usable for routine runs; keep the big judge for final numbers.

## Ideas for the next iteration (not applied — would be decided on dev, then re-tested)

- Retrieve more widely for conflict / multi-book questions (top-10 into the prompt, or one query per book).
- Tell the synthesis prompt to report disagreements between books explicitly.
- Allow partial answers: "answerable" for the parts the passages support, instead of all-or-nothing.
