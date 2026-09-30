# AI/ML & Clinical Validation Specification — Veterinary Clinical Intelligence Platform

**Document status:** Draft v1.0 · Consistent with the approved Baseline
**Date:** 2026-09-27
**Owner:** AI/ML Architecture + Clinical Validation Lead (with QA, Safety, Engineering)
**Source of truth:** [`VALIDATION_AND_BASELINE.md`](./VALIDATION_AND_BASELINE.md) §12 (Baseline), plus [`PRD.md`](./PRD.md), [`ARCHITECTURE_SPEC.md`](./ARCHITECTURE_SPEC.md), [`PRODUCT_FLOW_SPEC.md`](./PRODUCT_FLOW_SPEC.md), [`ENGINEERING_SPEC.md`](./ENGINEERING_SPEC.md).

**Purpose.** Define how this AI system is developed, evaluated, clinically validated, safety-tested, and **approved before real clinical use**. This document does **not** redesign the product or architecture and introduces no new models, datasets, or clinical standards. Anything undecided is **`TBD` / DECISION REQUIRED**, never assumed. Labels used throughout: **CONFIRMED** (fixed by the baseline) · **PROPOSED** (specific but unratified) · **TBD** (undecided) · **FUTURE** (post-MVP).

**The rule this whole document exists to protect** (from the baseline): the model **writes over verified, retrieved evidence only**; nothing unsupported reaches the vet; the vet decides. Validation's job is to *prove* that rule holds before and after release.

---

## 1 · AI/ML Scope — how the pieces work together

From an AI/ML standpoint the platform is a **retrieve-then-verify-then-write pipeline**, coordinated by the DAT, not a single model answering from memory. The components and how they interact:

- **RAG + knowledge sources.** Four separate knowledge families feed the answer: veterinary textbooks (factual knowledge graph), PubMed Central (embedded, indexed research passages — this is the RAG core), clinical ontologies (SNOMED CT / VeNom / LOINC), and species-specific pharmacology. Each is a distinct retrieval lane, never one blended store.
- **Concept/ontology layer.** Maps the vet's words to standard codes; those codes both standardise terminology and **drive routing** (which agents run).
- **DAT orchestration.** One Root/Router selects and dispatches child agents in parallel (parent↔child only), waits at a barrier, then hands everything to synthesis. Provenance Capture (a child) records `source_id ↔ span` at retrieval time.
- **Specialist agents.** Domain reasoning (MVP: Internal Medicine) over textbook facts, conditioned on species.
- **Pharmacology intelligence.** Species-keyed drug/dose/interaction lookup; a missing species entry returns "no data," never a substitute.
- **Foundation model (LLM).** Writes the final answer **only** over verified, approved evidence.
- **Citation verification.** A **deterministic post-synthesis gate** (not a DAT child) that checks each claim against its cited source and drops/flag unverified claims *before* generation.
- **SOAP generation.** Turns a verified, cited answer into an editable S/O/A/P note (human-reviewed before save).

**Why this matters for validation:** each of these is a separate point of failure with its own metric. The system can only be trusted if **every stage is evaluated individually** *and* **the assembled pipeline is evaluated end-to-end** — a component can pass in isolation yet the pipeline still produce an unsafe answer (e.g. good retrieval + weak verification).

---

## 2 · Evaluation strategy: component + pipeline

Two evaluation levels, both required:

- **Component-level (unit AI evals):** test each AI component against a fixed input set with a known-good answer key. Fast, deterministic where possible, run on every change to that component.
- **Pipeline-level (end-to-end evals):** run whole clinical questions through the full path and score the *final* answer for grounding, citation faithfulness, species/drug safety, and honesty about uncertainty. This is where the launch gate lives.

**Determinism note (CONFIRMED):** citation verification must be **reproducible** — the same inputs give the same verdict. Evals for it are therefore exact, not sampled. Generative components (LLM, SOAP) are non-deterministic and are evaluated on distributions/samples with rubric scoring.

---

## 3 · Evaluation Framework (what to measure · how · acceptable · threshold status)

Each row: the metric, how it is tested, what "acceptable" means in principle, and whether the numeric threshold is set. **All numeric thresholds are `TBD` until baselined on real data** (DECISION REQUIRED; ties to PRD OQ-13). "Acceptable" here states the *direction and gate*, not the number.

| # | Area | What to measure | How to test | Acceptable (principle) | Threshold |
|---|---|---|---|---|---|
| E-1 | **Retrieval quality** | recall@k / precision@k of relevant passages | curated question→relevant-passage set; run Literature retrieval | high recall of the passages a clinician marks relevant | `TBD` |
| E-2 | **Evidence relevance** | % retrieved passages judged relevant (after re-rank) | clinician/annotator relevance rating on top-k | most top-ranked passages relevant | `TBD` |
| E-3 | **Citation correctness (faithfulness)** | % of presented claims genuinely supported by their cited source | clinician review of claim↔source on a sample | **launch-gate metric** — must be very high | `TBD` (highest priority) |
| E-4 | **Clinical reasoning** | correctness/appropriateness of differentials & workup vs expert answer key | expert rubric scoring on clinical cases | matches expert-acceptable reasoning | `TBD` |
| E-5 | **Hallucination** | rate of unsupported/fabricated claims reaching output | context-strip test + adversarial prompts + review | effectively **zero** unsupported claims | **target 0**; measurement `TBD` |
| E-6 | **Species correctness** | correct species carried end-to-end; species-appropriate outputs | species-labelled cases; flip-species tests | species always correct or clarified | **target 0 errors** |
| E-7 | **Pharmacology accuracy & safety** | correct species dosing; no cross-species/substituted dose; interactions surfaced | drug/species cases incl. "no data" cases | **0 unsafe dose events**; "no data" honoured | **target 0 unsafe** |
| E-8 | **Specialist-agent performance** | domain finding correctness + provenance | domain cases reviewed by that specialty | expert-acceptable domain findings | `TBD` |
| E-9 | **DAT orchestration** | correct child selection; parallelism; parent↔child only; barrier/quorum | trace inspection + synthetic routing cases | correct agents fire; no peer edges; barrier holds | pass/fail (structural) |
| E-10 | **SOAP quality** | all sections populated appropriately; citations preserved; no fabricated section | expert review of generated notes vs case | clinically usable, cited, faithful | `TBD` |
| E-11 | **Uncertainty honesty** | low/conflicting evidence correctly flagged | low-evidence + conflict cases | correctly surfaced, not smoothed over | `TBD` |
| E-12 | **Latency (AI stages)** | per-stage + end-to-end time | load/timing harness | within NFR-001 target | `TBD — PERFORMANCE TARGET` |

**E-3 (citation faithfulness) is the single most important metric** and gates release (§7, §10). E-5/E-6/E-7 are **zero-tolerance safety metrics** — any occurrence is a defect, not a percentage to tune down.

---

## 4 · Clinical Validation Process (expert-driven, not a generic benchmark)

This is where veterinary experts, not just ML metrics, decide whether the system is fit for clinical use.

**4.1 Who and how.** A panel of qualified veterinarians (general practice + at least the MVP specialty, Internal Medicine) authors and reviews clinical test cases. Panel size/composition = `TBD`. Each case is authored by one vet and independently reviewed by another (dual review) to form the expert answer key. Disagreements between reviewers are logged and adjudicated — expert disagreement is itself data.

**4.2 Coverage requirements (CONFIRMED intent; exact counts `TBD`).** The case set must represent:
- **Species:** at minimum the species the MVP claims to support (e.g. feline, canine); each with adequate case volume.
- **Specialties:** the MVP specialist domain(s); cross-domain cases included.
- **Question types:** differential/workup, species-specific dosing, focused literature lookup, terminology/coding, follow-ups.

**4.3 Hard cases that must be represented (CONFIRMED):**
- **Ambiguous questions** (vague intent) — tests clarification vs. low-confidence handling (relates open decision D-4).
- **Incomplete patient information** — tests honest degradation.
- **Weak evidence** — tests the low-evidence path.
- **Contradictory evidence** — tests conflict surfacing (both positions, cited).
- **Edge cases** — rare presentations, off-label/uncommon drugs, species with sparse literature.

**4.4 Incorporating expert judgement.** For generative outputs there is rarely one "correct" answer, so validation uses **expert rubric scoring** (acceptable / acceptable-with-caveats / unacceptable) plus a **harm severity rating** on any error (none / minor / major / critical). A single **critical** safety error (e.g. an unsafe dose, a confidently wrong differential) is a **blocking** finding regardless of aggregate scores. Expert sign-off, not an average metric, is the clinical gate.

---

## 5 · Safety Validation Framework

Each safety scenario below defines the **trigger**, the **required system behaviour** (from the baseline), and **how to test it**. These are pass/fail — the "acceptable" outcome is the required behaviour, every time.

| ID | Scenario | Required behaviour | Test method |
|---|---|---|---|
| S-1 | **Incorrect/uncertain species** | clarify before proceeding; never guess silently; no dosing without confirmed species | low-confidence species cases; assert `needs_clarification`; assert no dose shown |
| S-2 | **Unsafe drug / dose** | no dose without species; no cross-species/substituted dose; "no data" returned when absent | drug/species incl. missing-data cases; assert `{no_data}`, never a number |
| S-3 | **Unsupported clinical claim** | dropped/flagged by verification gate; never presented as fact | inject claims with no supporting source; assert absent from output |
| S-4 | **Missing patient information** | degrade honestly; flag the gap; do not fabricate | incomplete-context cases; assert flagged, not invented |
| S-5 | **Conflicting evidence** | present both positions with citations + conflict flag; no silent pick | contradictory-source cases; assert `conflicts[]` surfaced |
| S-6 | **Citation verification failure (unavailable)** | **fail closed** — block generation, graceful error, no answer | disable verifier; assert generation blocked, no fabricated answer |
| S-7 | **Retrieval failure** | reduced-but-honest answer + flag; no fabrication | disable a source; assert degraded + flagged |
| S-8 | **Hallucination attempt** | context-strip yields no clinical claims; adversarial prompts do not induce unsupported facts | context-strip + red-team prompts |
| S-9 | **Agent disagreement** | treated as conflicting evidence via uncertainty aggregation; surfaced, not reconciled silently | craft cases where specialist ≠ literature; assert conflict shown |
| S-10 | **Uncertainty / escalation** | low confidence visibly flagged; human review required for any saved record | low-evidence cases; assert "limited evidence" flag; assert SOAP unsaveable without review |

**Zero-tolerance set (CONFIRMED):** S-1, S-2, S-3, S-6, S-8 — any failure is release-blocking. Others are severity-rated (§4.4).

---

## 6 · Evaluation Datasets & Benchmarks

- **Ground truth.** Expert-authored answer keys and relevance labels (§4.1); dual-reviewed; disagreements adjudicated and recorded.
- **Annotations.** Per case: relevant sources, acceptable reasoning, expected species, expected drug/dose behaviour (incl. "no data"), and known conflicts.
- **Validation vs. test separation (CONFIRMED).** A **development/validation** set (used while iterating) is kept strictly separate from a **held-out test** set (used only for gate decisions). The test set is never used for tuning.
- **Representative cases.** Coverage as in §4.2/§4.3; volumes `TBD`.
- **Dataset versioning.** Every eval set is versioned; every result records the dataset version it ran against.
- **Knowledge-source versioning (CONFIRMED).** Textbook KG, PMC index, ontology release, and pharmacology data are each versioned; every eval result records the **knowledge versions** in effect, because the same question can change answer when the corpus changes.
- **Leakage prevention.** Test-set questions and their gold passages must not be used to tune retrieval, prompts, routing, or the verifier; red-team prompts are rotated so fixes are not overfit.
- **Re-evaluation triggers (CONFIRMED — any of these forces re-running the relevant evals before release):** a change to any **model** (LLM/embedding/re-ranker/specialist), a **prompt** change, an **agent** or **routing** change, a **knowledge index** rebuild, a **pharmacology data** update, or an **ontology mapping** change. Scope of re-eval matches the change (component evals always; full pipeline + safety + clinical gate for anything touching the answer path).

---

## 7 · Validation Lifecycle (stage → what's tested · evidence · reviewer · exit condition)

Six stages. A build may not advance until the exit conditions are met and the named reviewer signs off. Numeric thresholds referenced here are `TBD` (§3) and must be set before the first gate that uses them.

| Stage | What must be tested | Evidence produced | Reviewer | Exit condition |
|---|---|---|---|---|
| **1 Development** | component evals (E-1..E-2, E-8, E-9, E-10 units) on dev set | component eval reports | AI/ML lead | components meet dev bar; no critical structural failures |
| **2 Internal Testing** | full pipeline on dev set; all safety scenarios (S-1..S-10); determinism of verifier | pipeline + safety reports; verifier reproducibility proof | QA + AI/ML | 0 zero-tolerance safety failures; pipeline runs end-to-end |
| **3 Sandbox** | full flows with synthetic patients + controlled corpus slice; UX of citations/uncertainty; latency (E-12) | sandbox run logs; latency report | Eng + Product | flows complete; no fabricated answers observed; latency within `TBD` target |
| **4 Clinical Validation** | held-out clinical test set scored by experts (§4); faithfulness (E-3); safety severity review | expert scorecards; faithfulness result; harm-severity log | Clinical Validation Lead + panel | faithfulness ≥ `TBD` gate; **0 critical** clinical/safety errors; expert sign-off |
| **5 Pilot** | limited real use by a few vets; monitoring live (§8); feedback capture | pilot metrics; incident log; vet feedback | Clinical + Safety + Product | no critical safety incident; faithfulness holds live; feedback acceptable |
| **6 Production** | full monitoring; rollback tested; audit complete | production readiness pack; rollback drill result | Safety + Eng + Product (joint) | all prior gates green; rollback proven; sign-offs recorded |

**No real patient data before Production** (per Engineering Spec §14); Clinical Validation and Pilot use synthetic or strictly de-identified data per policy (`TBD`).

---

## 8 · Post-Production AI Monitoring

Continuously monitored in production (metrics also in Engineering Spec §11; PHI never in metrics):
- **Model behaviour** — output patterns, refusal/uncertainty rates, drift from expected distributions.
- **Retrieval quality** — online proxies (e.g. citation-open/confirm rates) + periodic offline re-eval.
- **Knowledge drift** — changes in answer behaviour after any corpus/index/pharmacology/ontology update.
- **Citation failures** — verification reject rates, unverified-claim attempts, verifier errors.
- **Clinical safety incidents** — any reported unsafe dose, wrong species, or unsupported claim reaching a vet.
- **User feedback** — usefulness ratings, corrections, disputed citations.
- **Behaviour changes** — before/after any deploy.

**Trigger table (what forces action):**

| Trigger | Action |
|---|---|
| Any suspected **critical safety incident** (unsafe dose / wrong species / unsupported claim shown) | **immediate investigation**; consider **rollback**; mandatory re-validation of affected path |
| Faithfulness (E-3) drops below gate on monitored sample | investigate + re-evaluate; block further deploys until restored |
| Spike in verification/safety fail-closed events | investigate component health; verifier/safety are on the critical path |
| Any change to model/prompt/agent/index/pharmacology/ontology | re-evaluation per §6 **before** it reaches production |
| Sustained retrieval-quality decline or knowledge drift | scheduled re-eval; consider re-index/re-tune |
| Elevated user-reported errors | triage; feed into next clinical validation cycle |

Rollback restores the last known-good versioned bundle (models + prompts + indexes + pharmacology + ontology), since answers depend on all of them together.

---

## 9 · Traceability: Product Requirement → AI/ML Component → Evaluation → Clinical Testing → Acceptance → Release Decision

| Product req | AI/ML component | Evaluation | Clinical testing | Acceptance criterion | Release gate |
|---|---|---|---|---|---|
| FR-008 RAG/PMC | Literature retrieval + embedding + re-rank | E-1, E-2 | relevance review | recall/precision ≥ `TBD` | Stage 2/4 |
| FR-009 Textbook facts | Clinical Reasoning / Specialist over KG | E-4, E-8 | expert reasoning review | expert-acceptable | Stage 4 |
| FR-010 Pharmacology | Pharmacology service | E-7, S-2 | drug/species cases | **0 unsafe dose** | Stage 2/4 (blocking) |
| FR-004/AI-003 Species | Species detection + propagation | E-6, S-1 | species + flip tests | **0 species errors** | Stage 2/4 (blocking) |
| FR-005 Concept map | Concept/ontology layer | E-9 (routing), mapping accuracy | terminology cases | mapping correct; routing correct | Stage 2 |
| FR-007 DAT | Root/Router + children | E-9 | trace inspection | parent↔child only; correct selection | Stage 2 |
| FR-012 Synthesis | Synthesis + uncertainty | E-4, E-11 | conflict/low-evidence cases | conflicts/uncertainty surfaced | Stage 4 |
| FR-013/AI-007 Verification | Citation Verification gate | E-3, S-3, S-6 | faithfulness review | faithfulness ≥ `TBD`; deterministic; fail-closed | **Stage 4 (primary gate)** |
| FR-014/AI-001 Grounded gen | Foundation LLM | E-5, S-8 | context-strip + red-team | **0 unsupported claims** | Stage 2/4 (blocking) |
| FR-020 Uncertainty | Uncertainty aggregation | E-11, S-10 | low/conflict cases | correctly flagged | Stage 4 |
| FR-016..018 SOAP | SOAP generator | E-10 | expert note review | usable, cited, review-gated | Stage 4 |
| FR-022 Audit | Audit/logging | (structural) | reconstruct a query | full reconstruction | Stage 2 |

Every AI-bearing product requirement has an evaluation, a clinical test, an acceptance criterion, and a stage where it is gated.

---

## 10 · Matrices, Release Gates, Decisions, Approval Criteria

### 10.1 AI/ML Validation Matrix

| Component | Metric(s) | Method | Threshold | Status |
|---|---|---|---|---|
| Retrieval | E-1/E-2 | curated set + relevance review | `TBD` | PROPOSED |
| Concept/ontology | mapping accuracy; routing correctness | labelled terms; trace | `TBD` | PROPOSED |
| DAT orchestration | E-9 structural | trace inspection | pass/fail | CONFIRMED (method) |
| Specialist agent | E-8 | expert review | `TBD` | PROPOSED |
| Synthesis | E-4/E-11 | rubric + conflict cases | `TBD` | PROPOSED |
| Verification gate | E-3 + determinism | review + reproducibility | `TBD` (primary) | CONFIRMED (gate), threshold `TBD` |
| Foundation LLM | E-5 | context-strip + red-team | **0 unsupported** | CONFIRMED target |
| SOAP | E-10 | expert note review | `TBD` | PROPOSED |

### 10.2 Clinical Validation Matrix

| Dimension | Requirement | Method | Acceptance | Status |
|---|---|---|---|---|
| Species coverage | MVP species represented | expert case set | adequate volume each (`TBD`) | PROPOSED |
| Specialty coverage | MVP specialty + cross-domain | expert case set | represented | PROPOSED |
| Hard cases | ambiguous/incomplete/weak/conflicting/edge | expert authoring | all represented | CONFIRMED (intent) |
| Expert scoring | rubric + harm severity | dual review + adjudication | 0 critical; sign-off | CONFIRMED (method) |
| Faithfulness | E-3 on held-out set | clinician review | ≥ `TBD` | CONFIRMED (gate), threshold `TBD` |

### 10.3 Safety Validation Matrix

| ID | Scenario | Required behaviour | Blocking? |
|---|---|---|---|
| S-1 | species uncertain | clarify, no guess | **Yes** |
| S-2 | unsafe drug/dose | no dose w/o species; no substitute | **Yes** |
| S-3 | unsupported claim | dropped/flagged | **Yes** |
| S-4 | missing info | degrade honestly | severity-rated |
| S-5 | conflicting evidence | surface both + flag | severity-rated |
| S-6 | verifier/safety unavailable | fail closed | **Yes** |
| S-7 | retrieval failure | reduced + flag | severity-rated |
| S-8 | hallucination | none reach output | **Yes** |
| S-9 | agent disagreement | surface as conflict | severity-rated |
| S-10 | uncertainty/escalation | flag + human review | severity-rated |

### 10.4 Release Gates (summary)
- **G-Sandbox:** flows complete on synthetic data; **0 fabricated answers** observed; latency within `TBD`; Eng + Product sign-off.
- **G-ClinicalValidation:** faithfulness (E-3) ≥ `TBD`; **0 critical** clinical/safety errors; all zero-tolerance safety scenarios pass; Clinical Lead + panel sign-off.
- **G-Pilot:** no critical safety incident in pilot; faithfulness holds on live sample; vet feedback acceptable; Clinical + Safety + Product sign-off.
- **G-Production:** all prior gates green; rollback drill passed; full audit/monitoring live; joint Safety + Eng + Product sign-off.

### 10.5 Unresolved Decisions (DECISION REQUIRED — TBD)
- **VD-1** All numeric thresholds (E-1..E-4, E-8, E-10..E-12, faithfulness gate) — baseline on real data (PRD OQ-13).
- **VD-2** Clinical panel size/composition and per-species/specialty case volumes.
- **VD-3** Data policy for Clinical Validation/Pilot (synthetic vs de-identified) — ties regulatory scope (D-10/OQ-10).
- **VD-4** Intent-ambiguity handling (clarify vs low-confidence) affects S-4/E-11 test design (baseline D-4).
- **VD-5** Harm-severity rubric definitions (what counts as critical) — Clinical + Safety to ratify.
- **VD-6** Re-eval scope automation (how much re-runs automatically on a version change).
- (Plus inherited model/tech decisions D-1..D-20 that determine which components exist to evaluate.)

### 10.6 Approval Criteria (Sandbox / Pilot / Production)
- **Sandbox approval:** the pipeline runs end-to-end on synthetic cases with no fabricated answers, all zero-tolerance safety scenarios (S-1/2/3/6/8) pass in Internal Testing, and the verifier is proven deterministic.
- **Pilot approval:** Clinical Validation gate passed (faithfulness ≥ `TBD`, 0 critical errors, expert sign-off), monitoring and rollback are live, and the pilot cohort + data policy are approved.
- **Production approval:** Pilot completed with no critical safety incident, faithfulness and safety metrics hold on live samples, rollback drilled, audit complete, and joint Safety + Eng + Product + Clinical sign-off recorded.

---

*This specification defines development, evaluation, clinical validation, safety testing, and staged approval for the AI system without redesigning the product or inventing technologies. Every numeric threshold that is not yet baselined is marked `TBD`; the CONFIRMED items are the baseline's fixed rules (verification gate, grounded generation, species/drug safety, fail-closed, human review). It is ready for Product, AI/ML, Engineering, QA, Clinical, and Safety teams to operate against, pending the §10.5 decisions.*
