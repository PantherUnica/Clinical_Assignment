# Multi-book testing (checklist §4) — openai:gpt-5.5

Generated 2026-11-19 07:58 · library index (36,224 chunks, 17 books) · exact retrieval top-6 with per-book cap 2 (chosen on dev) · answers by `openai:gpt-5.5` · blind judges `openai:gpt-5-mini` and `openai:gpt-5.5`.
Questions: 31 held-out test + 9 dev. Spend: answers $2.23, judges $0.80.

## Held-out test set (headline)

| Group | n | Required books cited | ≥2 books cited | Citations supported in PDF | Printed page ok | Fact recall (small / big judge) | Overall /5 (small / big) | Conflict shown | Correct refusal | Wrong refusal | Median s | $ / answer |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| two-book | 10 | 55% | 90% | 100% | 100% | 72% / 68% | 3.6 / 3.7 | — | — | 0% | 15 | 0.068 |
| three-book | 8 | 46% | 100% | 100% | 100% | 69% / 73% | 3.1 / 3.6 | — | — | 0% | 16 | 0.082 |
| conflict | 4 | 21% | 50% | 100% | 100% | 48% / 42% | 3.0 / 2.2 | 0% | — | 0% | 9 | 0.040 |
| single-book | 4 | 100% | — | 100% | 100% | 100% / 100% | 5.0 / 5.0 | — | — | 0% | 6 | 0.034 |
| unanswerable | 5 | — | — | — | — | — / — | 5.0 / 5.0 | — | 100% | — | 3 | 0.026 |
| **all** | 31 | 54% | 86% | 100% | 100% | 72% / 70% | 3.8 / 3.9 | 0% | 100% | 0% | 13 | 0.057 |

## Dev set (used to choose settings — not a clean estimate)

| Group | n | Required books cited | ≥2 books cited | Citations supported in PDF | Printed page ok | Fact recall (small / big judge) | Overall /5 (small / big) | Conflict shown | Correct refusal | Wrong refusal | Median s | $ / answer |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| two-book | 4 | 38% | 75% | 100% | 100% | 44% / 31% | 2.5 / 2.2 | — | — | 25% | 17 | 0.057 |
| three-book | 2 | 50% | 50% | 100% | 100% | 75% / 67% | 3.5 / 4.0 | — | — | 0% | 13 | 0.052 |
| conflict | 1 | 50% | 100% | 100% | 100% | 38% / 50% | 3.0 / 2.0 | 100% | — | 0% | 23 | 0.091 |
| single-book | 1 | 100% | — | 100% | 100% | 100% / 100% | 4.0 / 5.0 | — | — | 0% | 7 | 0.033 |
| unanswerable | 1 | — | — | — | — | — / — | 5.0 / 5.0 | — | 100% | — | 2 | 0.024 |
| **all** | 9 | 50% | 71% | 100% | 100% | 58% / 51% | 3.2 / 3.2 | 100% | 100% | 12% | 12 | 0.053 |

### How to read the columns

- **Required books cited** — share of the books the question was designed around that the answer cites.
- **≥2 books cited** — multi-book questions whose answer cites at least two books.
- **Citations supported in PDF** — claim's content words found on the cited page, re-read from the original PDF.
- **Printed page ok** — the printed page shown matches the PDF's page label / printed number (Ettinger prints none).
- **Fact recall** — key facts judged present (partial = ½). The key lists only some valid books, so answers using
  other correct books can score lower here without being wrong.
- **Correct refusal** — unanswerable questions answered with "not in the books". **Wrong refusal** — answerable ones refused.

## Judge agreement (small vs big judge, all answers)

- Overall score identical: **55%**; within 1 point: **100%** (40 answers)
- Same per-fact verdict: **76%** (76 facts)
- Same refusal decision: **100%**
- Small judge minus big judge, mean overall: **-0.05** (positive = small judge is more generous)

## Retrieval vs answer (test)

- Required books present in the top-6 passages: **69%**
- Required books cited in the answer: **54%**
- Cited books that are on the question's valid list (required + also-valid): **100%**

## Per question (test)

| Q | Type | Books cited | Required cited | Supported | Fact recall s / b | Overall s / b | Refused | Notes (big judge) |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| mb-02 | two_book | 2 | 50% | 100% | 75% / 50% | 4 / 4 | no | The answer correctly states that daily oral ivermectin can be effective and identifies the main sensitive breeds, including Collies, Australian Shepherds, Shelt |
| mb-03 | two_book | 3 | 50% | 100% | 50% / 50% | 3 / 3 | no | The answer gives some relevant vaccination concepts such as modified-live vaccine starting at/after 6 weeks, but it does not give the required exact 6, 10, and  |
| mb-05 | two_book | 2 | 50% | 100% | 75% / 75% | 3 / 4 | no | The candidate correctly gives the 20 mm Hg decision threshold in substance and identifies oral glycerin for acute IOP reduction. It omits the key qualifier that |
| mb-06 | two_book | 3 | 50% | 100% | 100% / 50% | 5 / 4 | no | The answer gives the normal Schirmer value of at least 15 mm/min but does not state that values under 15 mm/min suggest KCS or that interpretation should consid |
| mb-07 | two_book | 3 | 50% | 100% | 75% / 75% | 4 / 3 | no | The answer gives an epinephrine dose that is numerically related to the expected dose, but it does not state the required 1:1,000 concentration or 0.01 mL/kg pa |
| mb-09 | two_book | 3 | 100% | 100% | 50% / 75% | 3 / 4 | no | The answer correctly gives the borderline UPC ranges for dogs and cats. It only partially describes IRIS staging because it omits that staging should use two or |
| mb-10 | two_book | 2 | 50% | 100% | 100% / 100% | 5 / 5 | no | The answer correctly states that primidone is metabolized/converted to phenobarbital and identifies hepatic injury/hepatotoxicity as the shared organ toxicity c |
| mb-11 | two_book | 2 | 0% | 100% | 75% / 50% | 3 / 3 | no | The answer includes feline-relevant thin/fragile skin and alopecia, and gives the correct feline LDDS dexamethasone dose of 0.1 mg/kg IV higher than dogs. Howev |
| mb-13 | two_book | 3 | 100% | 100% | 75% / 75% | 3 / 4 | no | The answer correctly identifies 1:30 bleach disinfection and the two key antiemetics, ondansetron and maropitant. It is incomplete for kennel disinfection becau |
| mb-14 | two_book | 1 | 50% | 100% | 50% / 75% | 3 / 3 | no | The anaesthetic hypotension/renal perfusion warning and liver disease accumulation risk are stated correctly. However, the handling by the body is largely incom |
| mb-16 | three_book | 2 | 67% | 100% | 83% / 83% | 3 / 4 | no | The meloxicam regimen and the core infectious causes FeLV/FIV/FIP are correctly given. However, the main feline uveitis differential list is incomplete because  |
| mb-17 | three_book | 2 | 33% | 100% | 50% / 67% | 3 / 3 | no | The answer correctly identifies ACTH stimulation, UCCR, LDDST/dexamethasone suppression testing, and the higher feline dexamethasone dose, but it omits the oral |
| mb-18 | three_book | 4 | 0% | 100% | 83% / 83% | 3 / 4 | no | The answer correctly explains the carbimazole-to-methimazole relationship, methimazole's inhibition of thyroid hormone synthesis, and that methimazole can be co |
| mb-20 | three_book | 3 | 67% | 100% | 83% / 83% | 3 / 4 | no | The answer correctly identifies levothyroxine/T4 as preferred and reserves T3 for poor response to T4, and gives the standard 0.02 mg/kg PO twice daily starting |
| mb-21 | three_book | 2 | 67% | 100% | 50% / 33% | 3 / 3 | no | The answer correctly describes the PSPP-style grouping of primary/secondary causes and predisposing/perpetuating factors. However, it omits the required dog/cat |
| mb-22 | three_book | 2 | 67% | 100% | 67% / 83% | 3 / 4 | no | The answer correctly explains the several-day monitoring rationale using the 24-hour half-life and 97% decline after 5 days, and it identifies liver disease as  |
| mb-23 | three_book | 4 | 33% | 100% | 83% / 100% | 4 / 5 | no | The answer states that skin scrapings are often false-negative and may detect mites in only about 20% of cases. It also includes the required selamectin topical |
| mb-24 | three_book | 3 | 33% | 100% | 50% / 50% | 3 / 2 | no | The answer identifies Notoedres cati and partially covers household management by saying all in-contact cats should be treated, but it omits the required iverme |
| mb-26 | conflict | 1 | 0% | 100% | 25% / 25% | 3 / 2 | no | The answer only provides the feline STT-1 range/median and omits the Blackwell >=15 mm/min cutoff and the Ettinger canine value of 21 +/- 4 mm/min. It also does |
| mb-27 | conflict | 1 | 0% | 100% | 50% / 25% | 3 / 2 | no | The answer gives only the 1-year booster followed by every-3-years recommendation and does not identify the conflicting yearly booster recommendation from the V |
| mb-28 | conflict | 2 | 50% | 100% | 50% / 50% | 3 / 3 | no | The Saunders regimen is stated accurately, including the alternative three applications at 14-day intervals. However, the Merck recommendation of monthly topica |
| mb-29 | conflict | 2 | 33% | 100% | 67% / 67% | 3 / 2 | no | The answer gives only the 0.2 mg/kg loading then 0.1 mg/kg q24h regimen and does not identify the conflicting recommendations from Blackwell uveitis or Merck. I |
| mb-31 | unanswerable | 0 | — | — | — / — | 5 / 5 | yes | The candidate clearly states that the indexed books do not provide evidence for a dose and does not invent a recommendation. This is the expected behavior for a |
| mb-32 | unanswerable | 0 | — | — | — / — | 5 / 5 | yes | The candidate clearly states that the indexed books do not cover molidustat/Varenzin use for anaemia in cats with CKD and avoids inventing a dose or recommendat |
| mb-33 | unanswerable | 0 | — | — | — / — | 5 / 5 | yes | The candidate clearly states that the indexed books do not provide evidence for a tirzepatide dose and avoids inventing a recommendation. This is the expected b |
| mb-34 | unanswerable | 0 | — | — | — / — | 5 / 5 | yes | The candidate clearly states that the indexed books do not provide evidence for the answer and avoids inventing a duration, dose, or recommendation. |
| mb-35 | unanswerable | 0 | — | — | — / — | 5 / 5 | yes | The candidate clearly states that the indexed books do not provide evidence for a dose and declines to invent one. This is the expected behavior for an unanswer |
| mb-37 | single_book | 2 | 100% | 100% | 100% / 100% | 5 / 5 | no | The answer correctly defines azotemia as an excess of nitrogen-containing compounds in the blood, matching the required fact. The additional clarification about |
| mb-38 | single_book | 1 | 100% | 100% | 100% / 100% | 5 / 5 | no | The answer states the first Marek's disease vaccination is at 1 day old in the hatchery, given subcutaneously at 0.2 ml, matching the required fact completely. |
| mb-39 | single_book | 1 | 100% | 100% | 100% / 100% | 5 / 5 | no | The answer correctly defines nephrogenic diabetes insipidus as polyuria due to nonresponsiveness to ADH and identifies Huskies as having a primary familial form |
| mb-40 | single_book | 2 | 100% | 100% | 100% / 100% | 5 / 5 | no | The answer correctly defines gastropexy as surgical fixation of the stomach, usually to the abdominal wall, and states its main purpose is preventing recurrence |

## Where it fell short (test, big-judge fact recall < 50%)

- **mb-21** (three_book) — required book(s) not retrieved: fossum-small-animal-surgery. Judge: The answer correctly describes the PSPP-style grouping of primary/secondary causes and predisposing/perpetuating factors. However, it omits the required dog/cat prevalence and otitis media figures, gives the feline ear mite proportion incompatibly with the key, and fails to mention selamectin.
- **mb-26** (conflict) — required book(s) not retrieved: blackwell-5min-canine-feline, ettinger-internal-medicine. Judge: The answer only provides the feline STT-1 range/median and omits the Blackwell >=15 mm/min cutoff and the Ettinger canine value of 21 +/- 4 mm/min. It also does not identify or reconcile the conflicting source values.
- **mb-27** (conflict) — required book(s) not retrieved: vaccination-schedule. Judge: The answer gives only the 1-year booster followed by every-3-years recommendation and does not identify the conflicting yearly booster recommendation from the Vaccination Schedule. It also omits the Merck puppy-series timing and fails to attribute the differing recommendations to the required books.
