# Testing & Quality Assurance Strategy — Veterinary Clinical Intelligence Platform

**Document status:** Draft v1.0 · Execution-focused
**Date:** 2026-09-27
**Owner:** QA Lead (with Engineering, AI/ML, Clinical, Security, Product)
**Source of truth:** [`VALIDATION_AND_BASELINE.md`](./VALIDATION_AND_BASELINE.md) §12. **Companions:** [`ENGINEERING_SPEC.md`](./ENGINEERING_SPEC.md) (§16 traceability, §17 acceptance criteria), [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md) (E-/S- IDs, gates), [`SECURITY_SAFETY_SPEC.md`](./SECURITY_SAFETY_SPEC.md), [`BACKLOG_EXECUTION_PLAN.md`](./BACKLOG_EXECUTION_PLAN.md).

**What this document answers:** *how do we prove each part works before release, and what evidence is required?* It does **not** redesign the product or repeat the architecture. Every important test traces to a product/system/safety requirement or acceptance criterion. Thresholds not yet baselined are `TBD` (they reuse the AI/ML spec's decisions, not new numbers). Labels: **CONFIRMED / PROPOSED / TBD / FUTURE**.

**The distinction that shapes everything here:** three kinds of testing, judged differently.
1. **Conventional software testing** — deterministic pass/fail (does the code do what the spec says).
2. **AI/ML evaluation** — measured on distributions/samples against thresholds (E-series); some parts deterministic (verification).
3. **Clinical validation** — expert judgement, not a metric alone; a critical safety error blocks release regardless of averages.
A clinical/AI capability is **never "done" on engineering tests alone** (DoD, backlog §6).

---

## 1 · Testing Scope by Area (what kind of testing applies)

| Area | Conventional | AI/ML eval | Clinical validation | Security |
|---|---|---|---|---|
| Frontend / query experience | ✅ unit/e2e/UX | — | usability (vet) | ✅ authz UI |
| Backend / Clinical Query Service | ✅ unit/integration | — | — | ✅ |
| APIs (gateway + internal) | ✅ contract/integration | — | — | ✅ authn/z, rate limit |
| Data pipelines / ingestion | ✅ pipeline tests | quality of extraction | corpus spot-check | ✅ licence/PII |
| RAG retrieval | ✅ plumbing | ✅ E-1/E-2 | relevance review | — |
| Concept mapping | ✅ mapping unit | mapping accuracy | terminology review | — |
| DAT orchestration | ✅ E-9 structural | routing correctness | — | — |
| Specialist agents | ✅ interface | ✅ E-8 | expert domain review | — |
| Pharmacology | ✅ lookup unit | ✅ E-7 | **drug/species safety review** | — |
| Citation verification | ✅ **determinism** | ✅ E-3 | faithfulness review | — |
| LLM behaviour | — | ✅ E-5 (hallucination) | grounded-answer review | red-team |
| SOAP generation | ✅ structure | ✅ E-10 | note quality review | — |
| Security / privacy | ✅ | — | — | ✅ full |
| Performance / reliability | ✅ load/chaos | latency (E-12) | — | — |
| Integrations (MVP = none ext.) | ✅ internal only | — | — | ✅ |

---

## 2 · Testing Levels & Environments

Levels map to the lifecycle stages (AI/ML §7, Engineering §14). Environments: Dev → Test → Sandbox → Staging → Pilot(prod-limited) → Production. **No real PHI outside Production.**

| Level | Purpose | Where | Owner |
|---|---|---|---|
| **Unit** | component logic correct | Dev/Test | dev of the component |
| **Integration** | components work together (API contracts, DAT ↔ children ↔ stores) | Test | BE/ML + QA |
| **System** | full assembled pipeline behaves | Test | QA |
| **End-to-end (E2E)** | real user journeys (login→answer→SOAP) | Test/Sandbox | QA + FE |
| **Regression** | nothing broke after a change | all | QA (automated) |
| **AI/ML evaluation** | E-1..E-12 on datasets | Test | ML + QA |
| **Clinical validation** | expert-scored held-out cases | Clinical Validation | CLIN + QA |
| **Safety testing** | S-1..S-10 scenarios | Test/Sandbox | Safety + QA |
| **Security testing** | authn/z, encryption, secrets, injection, access | Test/Staging | SEC |
| **Performance testing** | latency, load, scalability | Staging | DEVOPS + QA |
| **Sandbox testing** | full flows on synthetic data | Sandbox | QA + Product |
| **Pilot validation** | live use, few vets, monitored | Pilot | Clinical + Product |
| **Production verification** | post-deploy smoke + monitoring | Production | DEVOPS + QA |

---

## 3 · Clinical Test Cases (creation, maintenance, expected outcomes)

**Who/how (from AI/ML §4).** Vets author cases; a second vet reviews to form the expected-outcome key (dual review); disagreements adjudicated and logged. Cases are versioned with the knowledge-source versions they assume.

**Case categories that must exist (CONFIRMED):**

| Category | What it tests | Expected outcome (principle) |
|---|---|---|
| Normal cases | typical clinical questions | correct, cited, species-appropriate answer |
| Edge cases | rare presentations, uncommon drugs, sparse-literature species | correct or honest low-evidence |
| Ambiguous questions | vague intent | clarify or low-confidence + flag (decision D-4) |
| Incomplete information | missing signs/labs | honest degradation + flag |
| Wrong / uncertain species | mislabeled or unclear | clarify; **no dose without species** |
| Conflicting evidence | sources disagree | both shown, cited, conflict flag |
| Low-evidence | thin support | "limited evidence" flag; no false confidence |
| Pharmacology risks | cross-species/missing dose | `{no_data}`, never a substitute dose |
| Hallucination | adversarial / context-strip | no unsupported claim in output |
| Citation failure | claim not supported by source | claim dropped/flagged |
| System failure | source/model/verifier down | degrade honestly or fail closed |

**Expected outcomes & expert review.** For deterministic behaviours (verification, species/dose blocking) the expected outcome is exact. For generative outputs, experts score **acceptable / acceptable-with-caveats / unacceptable** plus a **harm severity** (none/minor/major/critical). **One critical = blocking.** Cases are maintained: every production incident adds a regression case (§5).

---

## 4 · Test Data, Environments, Ownership

- **Test data (CONFIRMED):** synthetic patients and a controlled corpus slice below Production; **no real PHI** in Dev/Test/Sandbox/Staging; Pilot/Clinical Validation data policy (synthetic vs de-identified) = `TBD` (SD-8/VD-3).
- **Eval datasets:** versioned; strict **validation/test separation**; **leakage prevention** (test questions/gold passages never used to tune); knowledge-source versions recorded per run (AI/ML §6).
- **Environment ownership:** DEVOPS owns environments + isolation; QA owns test execution + defect flow; ML owns eval harness; CLIN owns clinical case set; SEC owns security tests.
- **Determinism note:** citation-verification tests are **exact and reproducible**; generative tests are sample/distribution-based with rubric scoring.

---

## 5 · Defect Management, Severity & Regression

**Severity (CONFIRMED):**
- **S1 / Critical** — any safety violation (unsafe/absent-species dose, unsupported claim shown, fail-open, PHI exposure). **Release-blocking; in production, a rollback trigger.**
- **S2 / Major** — wrong-but-not-unsafe clinical content, broken core flow, security weakness.
- **S3 / Minor** — degraded UX, non-blocking inaccuracy.
- **S4 / Cosmetic.**

**Flow:** log → triage/severity → assign owner → fix → **add a regression test/eval/clinical case** → re-test → close. A critical defect additionally triggers investigation + re-validation of the affected path (Security §5).

**Regression strategy (CONFIRMED):** automated regression on every change; **every fixed defect becomes a permanent test**; the safety suite (S-1..S-10) and the faithfulness eval (E-3) run on every answer-path change (AI/ML §6 re-eval triggers). A change to any model/prompt/agent/index/pharmacology/ontology forces the matching evals to re-run before release.

---

## 6 · Traceability: Requirement → Test Case → Expected → Actual → Defect → Resolution → Release

Representative rows (QA maintains the full matrix; test IDs are `PROPOSED` placeholders).

| Requirement | Test case | Expected result | Actual | Defect | Resolution | Release gate |
|---|---|---|---|---|---|---|
| FR-001 auth | T-AUTH-01 | unauthenticated call rejected | (run) | (if any) | (fix + regression) | Prod (security) |
| FR-004/AI-003 species | T-SPE-01 | low confidence → clarify; no silent guess | | | | Internal/Clinical |
| FR-010/SAF-002 pharmacology | T-PHA-02 | no feline data → `{no_data}`, no substitute | | | | Clinical (blocking) |
| FR-013/AI-007 verification | T-CIT-01/02 | unsupported claim dropped; identical inputs → identical result | | | | Clinical (primary) |
| FR-014/AI-001 grounded gen | T-GEN-01 | context-strip → no clinical claims | | | | Clinical (blocking) |
| SAF-001/006 (fail closed) | T-SAF-06 | verifier unavailable → generation blocked | | | | Internal (blocking) |
| FR-007/AI-005 DAT | T-DAT-01/02 | parallel; parent↔child only; correct selection | | | | Internal |
| FR-020 uncertainty | T-UNC-01 | low/conflicting evidence flagged | | | | Clinical |
| FR-016/017 SOAP | T-SOAP-01/02 | S/O/A/P + citations; unsaveable without review; edit provenance | | | | Internal/Clinical |
| FR-022 audit | T-AUD-01 | any query reconstructable | | | | Internal |
| DP-001..008 privacy | T-SEC-* | encryption; store isolation; no PHI in logs | | | | Prod (security) |

Each requirement thus has a test, an expected result, a place for the actual result, a defect link, a resolution, and the gate it feeds.

---

## 7 · QA Test Matrix (conventional)

| Level | Coverage target | Pass condition | Automated? |
|---|---|---|---|
| Unit | core logic of each component | all pass; coverage bar `TBD` | yes |
| Integration | API contracts; DAT↔children↔stores | all pass | yes |
| System | full pipeline behaviour | all pass; no S1/S2 open | mostly |
| E2E | login→context→query→answer→SOAP→save | journeys pass | yes (+ manual UX) |
| Regression | full suite incl. prior defects | 100% pass | yes |
| Performance | latency/load | within NFR-001 (`TBD`) | yes |
| Reliability/chaos | component failure → graceful/fail-closed | required behaviour every time | yes |

---

## 8 · Clinical Test Matrix

| Dimension | Coverage | Method | Acceptance |
|---|---|---|---|
| Species | MVP species, adequate volume (`TBD`) | expert case set | correct/clarified; 0 species errors |
| Specialty | IM + cross-domain | expert case set | expert-acceptable |
| Case categories | all 11 (§3) represented | dual-authored | all present |
| Faithfulness | E-3 on held-out set | clinician review | ≥ `TBD` gate |
| Harm severity | every error rated | expert | **0 critical** |
| Sign-off | Clinical Lead + panel | review meeting | recorded |

---

## 9 · AI/ML Test Matrix

| Component | Eval | Method | Threshold | Determinism |
|---|---|---|---|---|
| Retrieval | E-1/E-2 | curated set + relevance | `TBD` | sampled |
| Concept/routing | mapping acc.; E-9 routing | labelled terms; trace | `TBD` / pass-fail | mixed |
| Specialist | E-8 | expert review | `TBD` | sampled |
| Synthesis/uncertainty | E-4/E-11 | rubric + conflict cases | `TBD` | sampled |
| **Verification** | E-3 + reproducibility | review + repeat-run | `TBD` (primary) | **exact** |
| LLM (hallucination) | E-5 | context-strip + red-team | **0 unsupported** | sampled |
| SOAP | E-10 | expert note review | `TBD` | sampled |
| Latency | E-12 | timing harness | `TBD — PERF TARGET` | measured |

---

## 10 · Security Test Coverage

| Control | Test | Pass condition |
|---|---|---|
| Authentication | unauth/expired/rate-limit | rejected (401/403/429) |
| Authorization/RBAC | cross-role access attempts | denied by role |
| Vet verification | non-vet access | blocked |
| Encryption | transit + at rest | enforced; no plaintext sensitive data |
| Secrets | scan code/logs | no secrets present |
| Store isolation | cross-store access | denied; no PHI in corpora/metrics |
| Injection / malicious input | fuzz + injection | rejected; scope guardrail holds |
| Audit integrity | tamper attempt | audit reconstructable, protected |
| Data deletion | delete request | cascades per policy (`TBD` specifics) |

---

## 11 · Release Gates (what must pass to advance)

| Transition | Must pass |
|---|---|
| **Development → Test** | unit + component evals green; no S1 open |
| **Test → Sandbox** | integration + system + E2E pass; **safety suite S-1..S-10 pass with 0 zero-tolerance failures**; verifier determinism proven; no fabricated answers |
| **Sandbox → Pilot** | Sandbox flows pass on synthetic data; latency within `TBD`; **Clinical Validation gate met** (faithfulness ≥ `TBD`, 0 critical, expert sign-off); security tests pass; monitoring + rollback live |
| **Pilot → Production** | no critical safety incident in pilot; faithfulness + safety hold on live sample; full security review; rollback drilled; audit complete; regulatory scope resolved; joint sign-off |

---

## 12 · Critical Defects (definition & handling)

A **Critical (S1)** defect is any of: an unsafe or absent-species dose surfaced; an unsupported/hallucinated claim presented as fact; verification/safety failing open; PHI exposure; audit gap that prevents reconstruction. **Handling:** immediate stop-the-line for that release path; investigation via audit; fix + permanent regression case; re-validation of the affected path before it can advance; in Production, a **rollback trigger**. **Zero open S1 defects** is a precondition for every gate from Sandbox onward.

---

## 13 · Open Testing Gaps (`TBD` / DECISION REQUIRED)

- **TG-1** Numeric thresholds for E-1/2/3/4/8/10/11/12 and coverage bars — `TBD` (VD-1/OQ-13).
- **TG-2** Clinical panel + per-species/specialty case volumes — `TBD` (VD-2).
- **TG-3** Pilot/Clinical-Validation data policy (synthetic vs de-identified) — `TBD` (SD-8/VD-3).
- **TG-4** Harm-severity definitions ("what is critical") — `TBD` (VD-5/SD-9).
- **TG-5** Performance/availability targets to test against — `TBD` (NFR-001/002).
- **TG-6** How much regression/eval re-runs automatically on a version change — `TBD` (VD-6).
- **TG-7** Intent-ambiguity expected behaviour (clarify vs low-confidence) affects ambiguous-case expected results — `TBD` (D-4).
- **TG-8** Security test depth (pen-test scope) and vet-verification test method — pending SD-2/SD-6.

---

## 14 · Production Readiness Checklist (QA sign-off)

- [ ] All conventional levels pass (unit → E2E → regression); coverage bar met (`TBD`).
- [ ] AI/ML evals measured; **faithfulness (E-3) ≥ gate**; latency within target (`TBD`).
- [ ] **Safety suite S-1..S-10 pass; 0 zero-tolerance failures.**
- [ ] Clinical validation complete; **0 critical** errors; expert sign-off recorded.
- [ ] Security coverage (§10) all pass; no secrets/PHI leakage.
- [ ] **Zero open S1 defects**; all S2 triaged with a plan.
- [ ] Every requirement has a passing traced test (§6).
- [ ] Regression suite includes all prior defects; re-eval triggers wired.
- [ ] Monitoring + rollback + incident process verified live.
- [ ] Open testing gaps (§13) resolved or explicitly accepted with owner.

---

*This strategy defines how the platform is proven correct, clinically reliable, safe, and secure before controlled deployment. It separates conventional testing from AI/ML evaluation and clinical validation, traces every important test to a requirement, and makes clinical/AI features un-releasable on engineering tests alone. It repeats none of the architecture/engineering/security detail — it says how we test, what evidence is required, and what must pass at each gate. Pending items are the §13 gaps, all `TBD`/decision-linked, none inventing a number.*
