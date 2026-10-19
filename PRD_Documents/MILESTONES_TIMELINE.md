# Product Milestones & Execution Timeline — Veterinary Clinical Intelligence Platform

**Document status:** Draft v1.0 · Management-ready execution roadmap
**Date:** 2026-09-30
**Owner:** Product / Program Management (TPM + Clinical AI Delivery Lead)
**Source of truth:** [`MASTER_PRD.md`](./MASTER_PRD.md). **Basis for sequencing:** [`BACKLOG_EXECUTION_PLAN.md`](./BACKLOG_EXECUTION_PLAN.md) (epics, critical path, DoR/DoD), [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md) (gates), [`SECURITY_SAFETY_SPEC.md`](./SECURITY_SAFETY_SPEC.md), [`TESTING_QA_STRATEGY.md`](./TESTING_QA_STRATEGY.md), [`ENGINEERING_SPEC.md`](./ENGINEERING_SPEC.md).

**What this document is.** The milestone/timeline view — where the project is, what happens next, what blocks progress, and what must pass before clinical production. It does **not** redesign the product, add scope, duplicate the backlog/specs, or invent calendar dates. Durations are **relative** (Week/Month) and marked **`PROPOSED`**; all are conditional on the blocking decisions (§6) being resolved on time. Labels: **CONFIRMED / PROPOSED / TBD / FUTURE**.

> **Timeline caveat (read first).** Every duration below is **`PROPOSED`** and assumes the `DECISION REQUIRED` items (models, vector DB, orchestration runtime, cloud, auth/vet-verification, pharmacology source, licences, evaluation thresholds, clinical panel, regulatory scope) are resolved **before** the milestone that needs them. Until those are owned and dated, the timeline is indicative, not committed.

---

## 1 · Milestone Map (aligned to Master PRD phases)

| Milestone | Maps to PRD phase | One-line objective |
|---|---|---|
| **M0 · Product Definition** | Foundation (docs) | Approved, consistent specification set + resolved blocking decisions. |
| **M1 · Architecture & Foundation** | Phase 0 | Secure platform skeleton, environments, auth, stores, audit. |
| **M2 · Knowledge / Data Foundation** | Phase 1 | All four knowledge families ingested, versioned, with provenance. |
| **M3 · Core Clinical Intelligence** | Phase 2 (build) | Understanding layer + DAT + retrieval producing evidence. |
| **M4 · AI / RAG / DAT Integration** | Phase 2 (assemble) | Full pipeline: synthesis → verification gate → safety → grounded answer. |
| **M5 · Safety & Clinical Validation** | Phase 3 | Evals + safety suite + expert clinical validation passed. |
| **M6 · Sandbox** | Phase 3 | Full flows on synthetic data; no fabricated answers. |
| **M7 · Pilot** | Phase 4 | Controlled real use, monitored, no critical incident. |
| **M8 · Production Launch** | Phase 5 | General availability with full ops + governance. |
| **M9 · Scale & Continuous Improvement** | Phase 6 | Safe evolution, additional species/specialists (FUTURE). |

---

## 2 · Milestone Detail

Each milestone: Objective · Deliverables · Key activities (by team) · Dependencies · Entry → Exit criteria · Risks · Approval.

### M0 · Product Definition — *largely COMPLETE*
- **Objective:** an approved, internally consistent specification set and an owned decision log.
- **Deliverables:** the 12-document set (Master PRD + specs); consolidated open-decision list.
- **Key activities:** Product — finalize Master PRD; assign owner + date to each `DECISION REQUIRED` item; confirm V1 specialist = Internal Medicine (OQ-9); confirm user scope (UD-1: Vet Doctors only for MVP).
- **Dependencies:** none.
- **Entry:** specs drafted. **Exit:** specs consistent (validation doc); blocking decisions have owners + target dates.
- **Risks:** decisions left unowned → everything downstream slips.
- **Approval:** Product + Leadership sign the decision log.

### M1 · Architecture & Foundation — *PROPOSED Month 1*
- **Objective:** secure skeleton every clinical capability sits on.
- **Deliverables:** environments (Dev/Test/Sandbox/Staging/Prod) with data isolation; API gateway + auth + session; RBAC; the eight data stores stood up; audit + secrets/CI baseline.
- **Key activities:** DEVOPS — environments, CI/CD, secrets; BE/SEC — gateway, auth, RBAC, store separation; BE — pluggable service interfaces (so `TBD` models/DBs slot in).
- **Dependencies:** auth mechanism + vet verification decisions (SD-1/2); cloud choice (D-10-adjacent).
- **Entry:** M0 decisions for auth/cloud resolved. **Exit:** authenticated request routes end-to-end; no real PHI outside Prod; audit writes.
- **Risks:** auth/cloud undecided blocks the start.
- **Approval:** Security + Eng sign the foundation review.

### M2 · Knowledge / Data Foundation — *PROPOSED Month 1–2 (parallel with M1)*
- **Objective:** trusted knowledge base, offline, before any live answering.
- **Deliverables:** Textbook KG; PMC vector index + provenance; ontology store (SNOMED/VeNom/LOINC); pharmacology DB; all versioned with dates.
- **Key activities:** DATA — ingestion pipelines (parse/clean/chunk); ML — embeddings + index build; DATA — ontology/pharmacology load + versioning.
- **Dependencies:** embedding model + vector DB (D-2/D-3); KG engine (D-4); pharmacology source (D-5); source licences (D-11).
- **Entry:** model/DB/licence decisions resolved. **Exit:** stores populated, versioned, provenance + dates present; mapping/retrieval measurable.
- **Risks:** **pharmacology source (D-5)** and **licences (D-11)** are the likely blockers; ingestion quality (OCR/extraction).
- **Approval:** Data + AI/ML sign ingestion quality review.

### M3 · Core Clinical Intelligence — *PROPOSED Month 2–3*
- **Objective:** understand a question and gather real evidence.
- **Deliverables:** query understanding + scope guardrail; species detection + clarification; concept mapping; decomposition; DAT Root + children (reasoning, literature, ontology, pharmacology, provenance) + IM specialist; retrieval + local re-rank.
- **Key activities:** ML — understanding/species/concept + retrieval; BE/ML — DAT orchestration + routing contract; ML/CLIN — IM specialist; FE — query UI against mocks (parallel).
- **Dependencies:** M2 stores; routing mechanism (D-1); degradation values (D-3-values).
- **Entry:** M2 exit. **Exit:** a query fans out and returns structured evidence with provenance; DAT shows parent↔child only.
- **Risks:** routing undefined → divergent orchestrators; latency of parallel retrieval.
- **Approval:** AI/ML + Eng sign component evals at dev bar.

### M4 · AI / RAG / DAT Integration — *PROPOSED Month 3–4*
- **Objective:** the full trust core — a cited, verified, grounded answer.
- **Deliverables:** synthesis + uncertainty aggregation; **deterministic citation-verification gate**; safety/grounding (**fail closed**); grounded LLM generation; response contract `{answer, citations[], confidence, flags[]}`; basic SOAP + review/save + edit-provenance.
- **Key activities:** ML — synthesis/uncertainty, verification, grounded generation; SEC/ML — safety layer + fail-closed; ML/FE/BE — SOAP; BE — assemble Clinical Query Service end-to-end.
- **Dependencies:** M3; Foundation LLM (D-7); uncertainty thresholds (D-5-values).
- **Entry:** M3 exit. **Exit:** end-to-end pipeline runs; verifier deterministic; context-strip yields no claims; fail-closed proven internally.
- **Risks:** **faithfulness** hard to reach; fail-open under partial outage.
- **Approval:** **Gate — MVP Ready** (see §3).

### M5 · Safety & Clinical Validation — *PROPOSED Month 4–5*
- **Objective:** prove clinical trustworthiness.
- **Deliverables:** eval harness + datasets; E-series results; safety suite S-1..S-10; expert-scored clinical case set; faithfulness result; harm-severity log.
- **Key activities:** ML — evals; QA/Safety — safety suite; CLIN — case authoring + dual review + scoring.
- **Dependencies:** thresholds incl. faithfulness gate (VD-1); clinical panel + case volumes (VD-2); validation data policy (VD-3/SD-8).
- **Entry:** MVP Ready. **Exit:** faithfulness ≥ gate; **0 critical** clinical/safety errors; 0 zero-tolerance safety failures; expert sign-off.
- **Risks:** panel/case-set not ready; faithfulness below gate.
- **Approval:** **Gates — AI/ML Validation Complete + Clinical Validation Complete + Security/Safety Approved**.

### M6 · Sandbox — *PROPOSED Month 5–6*
- **Objective:** exercise full flows on synthetic data.
- **Deliverables:** sandbox environment run logs; latency report; UX of citations/uncertainty.
- **Key activities:** QA/Product — full journeys on synthetic patients; DEVOPS — sandbox; SEC — security basics verified.
- **Dependencies:** M5 gates; latency target (NFR-001, `TBD`).
- **Entry:** validation gates green. **Exit:** flows complete; **no fabricated answers**; latency within `TBD`.
- **Risks:** latency; UX gaps in uncertainty display.
- **Approval:** **Gate — Sandbox Ready**.

### M7 · Pilot — *PROPOSED Month 6–8*
- **Objective:** limited real use, closely monitored.
- **Deliverables:** live monitoring (3 layers); rollback drilled; incident process; feedback capture; pilot metrics + incident log.
- **Key activities:** DEVOPS/AI-Ops — monitoring + rollback; Clinical Governance — clinical-safety monitoring + incident handling; Product — pilot cohort.
- **Dependencies:** pilot cohort + data policy; regulatory posture for real data (D-10).
- **Entry:** Sandbox Ready. **Exit:** no critical safety incident; faithfulness holds live; feedback acceptable.
- **Risks:** first live safety incident; data-policy/regulatory blockers.
- **Approval:** **Gate — Pilot Ready → Pilot Complete**.

### M8 · Production Launch — *PROPOSED Month 8+*
- **Objective:** general availability with full operations.
- **Deliverables:** production readiness pack; security review; rollback drill; full audit/monitoring; sign-offs.
- **Key activities:** SEC — full security review; DEVOPS — scale/rollback; Product/Leadership — go/no-go.
- **Dependencies:** regulatory scope resolved (D-10); all prior gates.
- **Entry:** Pilot complete, no critical incident. **Exit:** stable production operation + governance.
- **Risks:** regulatory/retention unresolved; scale degrading verification.
- **Approval:** **Gate — Production Ready** (joint sign-off).

### M9 · Scale & Continuous Improvement — *ongoing, FUTURE items*
- **Objective:** safe evolution.
- **Deliverables:** additional species (validated per species); additional specialists (FUTURE); model/knowledge improvements via classified changes.
- **Key activities:** all teams under change-management + re-eval triggers (Prod Ops §4, AI/ML §6).
- **Dependencies:** governance approvals.
- **Entry:** stable production. **Exit:** n/a (ongoing).
- **Risks:** a change weakening a safety control.
- **Approval:** governance per change class.

---

## 3 · Milestone Gates (evidence required to pass)

| Gate | Required evidence / approvals |
|---|---|
| **MVP Ready** (end M4) | full pipeline runs end-to-end; verification gate + fail-closed proven; response contract live; no fabricated answers internally; Eng + AI/ML sign-off. |
| **Engineering Complete** (end M4, all P0 epics) | all P0 backlog epics feature-complete + integrated; NFR instrumentation in place; QA integration/system pass. |
| **AI/ML Validation Complete** (M5) | E-series measured; **faithfulness (E-3) ≥ gate**; verifier determinism proven; AI/ML sign-off. |
| **Clinical Validation Complete** (M5) | expert-scored held-out set; **0 critical** errors; Clinical Lead + panel sign-off. |
| **Security/Safety Approved** (M5) | safety suite S-1..S-10 pass (0 zero-tolerance); security tests pass; Security + Safety sign-off. |
| **Sandbox Ready** (M6) | full flows on synthetic data; latency within `TBD`; no fabricated answers; Eng + Product sign-off. |
| **Pilot Ready** (M7) | monitoring + rollback + incident process live; pilot cohort + data policy approved; Clinical + Safety + Product sign-off. |
| **Production Ready** (M8) | all prior gates green; full security review; rollback drilled; audit complete; regulatory scope resolved; **joint Safety + Security + Clinical + Eng + Product** sign-off. |

---

## 4 · Consolidated Roadmap

`Milestone → Timeline (PROPOSED) → Deliverables → Owner → Dependencies → Exit criteria → Next`

| Milestone | Timeline | Key deliverables | Owner | Depends on | Exit criteria | Next |
|---|---|---|---|---|---|---|
| M0 Product Definition | done | spec set + decision log | Product | — | decisions owned + dated | M1 |
| M1 Architecture & Foundation | Month 1 | envs, auth, stores, audit | DEVOPS/SEC | auth/cloud decisions | secure request end-to-end | M2/M3 |
| M2 Knowledge/Data | Month 1–2 (∥ M1) | 4 knowledge stores + provenance | Data/ML | models, DB, licences, pharma source | stores versioned + provenance | M3 |
| M3 Core Clinical Intelligence | Month 2–3 | understanding + DAT + retrieval | AI-ML/BE | M2, routing (D-1) | evidence returned w/ provenance | M4 |
| M4 AI/RAG/DAT Integration | Month 3–4 | synthesis→verify→safety→answer + SOAP | AI-ML/BE/SEC | M3, LLM (D-7) | pipeline + fail-closed proven | **MVP Ready** → M5 |
| M5 Safety & Clinical Validation | Month 4–5 | evals, safety suite, clinical validation | AI-ML/CLIN/QA | thresholds, panel (VD-1/2) | faithfulness ≥ gate; 0 critical | M6 |
| M6 Sandbox | Month 5–6 | full flows on synthetic data | QA/Product | M5, latency target | no fabricated answers | M7 |
| M7 Pilot | Month 6–8 | monitored controlled launch | Clinical/Product/DEVOPS | cohort, data policy, D-10 | no critical incident | M8 |
| M8 Production Launch | Month 8+ | GA + full ops + governance | Product/SEC/DEVOPS | D-10, all gates | stable production | M9 |
| M9 Scale & Improvement | ongoing | evolution (FUTURE items) | all | governance | n/a | — |

---

## 5 · Critical Path

`M0 decisions → M2 knowledge (esp. PMC index + pharmacology + provenance) → M3 retrieval → M4 synthesis + verification gate + grounded generation → M5 evals + clinical validation → M6 Sandbox → M7 Pilot → M8 Production.`

This is the **trust core**; nothing ships without it. **Parallelizable:** M1 (foundation) alongside M2; FE query UI on mocks during M3–M4; the DAT children (ontology, pharmacology, specialist) in parallel within M3.

---

## 6 · Key Decisions (gate the timeline)

- **Blocking M1:** auth mechanism + vet verification (SD-1/2); cloud/deployment (D-10-adjacent).
- **Blocking M2:** embedding/re-ranker/LLM (D-2/D-7); vector DB (D-3); KG engine (D-4); **pharmacology source (D-5)**; **licences (D-11)**.
- **Blocking M3:** DAT routing mechanism (D-1); degradation values (D-3-values).
- **Blocking M5:** faithfulness + eval thresholds (VD-1); clinical panel + case volumes (VD-2); validation/pilot data policy (VD-3/SD-8); confirm V1 specialist = IM (OQ-9); intent-ambiguity handling (D-4).
- **Blocking M7/M8:** regulatory scope + retention/residency (D-10); incident owners/SLAs (SD-10/PD-3).
- **User scope:** UD-1 (Vet Nurses/Students) — decide before it affects roles/permissions; MVP stays Vet-Doctors-only until then.

Each needs an **owner + target date**. Until then, all `PROPOSED` durations are indicative.

---

## 7 · Major Dependencies

- **Knowledge before intelligence:** M3/M4 cannot start meaningfully until M2 stores exist.
- **Verification before validation:** the deterministic verifier (M4) must exist before faithfulness can be measured (M5).
- **Clinical panel readiness:** M5 clinical validation depends on recruiting the expert panel and building the case set — start this **in parallel with build**, not after.
- **Regulatory clarity:** M7/M8 depend on the data-policy and regulatory decisions (D-10).

---

## 8 · Major Risks (timeline impact)

| Risk | Milestone | Impact | Mitigation |
|---|---|---|---|
| Blocking decisions unowned | M0→all | whole timeline slips | assign owners + dates at M0 |
| Pharmacology source / licences unresolved | M2 | knowledge foundation stalls | decide D-5/D-11 first |
| Faithfulness below gate | M4/M5 | no clinical release | prototype verification early; treat as top risk |
| Clinical panel/case-set not ready | M5 | validation gate blocked | recruit + build in parallel from M2 |
| Latency too high | M4/M6 | Sandbox slip / abandonment | parallelize DAT; set/measure NFR-001 |
| Regulatory/data policy | M7/M8 | Pilot/Prod blocked | resolve D-10 before Pilot |
| Scope creep (nurses/students/extra specialists pulled into MVP) | any | delay + risk | hold to Master PRD boundary; UD-1/OQ-9 are decisions, not defaults |

---

## 9 · Production Launch Checklist

- [ ] All milestone gates green (MVP → Engineering → AI/ML Validation → Clinical Validation → Security/Safety → Sandbox → Pilot → Production).
- [ ] Faithfulness (E-3) ≥ gate on held-out **and** live samples.
- [ ] Safety suite S-1..S-10 pass; **0 zero-tolerance failures**; fail-closed proven.
- [ ] **0 critical** clinical/safety errors in validation and pilot; no critical incident in pilot.
- [ ] Full security review passed (authn/z, encryption, secrets, RBAC, store isolation, no PHI in logs).
- [ ] Audit reconstructs any query; monitoring (3 layers) + alerts + rollback live and drilled.
- [ ] Incident process operational with named owners; regulatory scope resolved (D-10).
- [ ] All blocking `DECISION REQUIRED` items closed; open items explicitly accepted with an owner.
- [ ] Joint sign-off recorded: Safety + Security + Clinical + Eng + Product.

---

*This document converts the approved plans into a milestone-driven, dependency-aware execution roadmap with gates, a critical path, and a launch checklist. It invents no calendar dates — durations are `PROPOSED` and conditional on the key decisions being resolved — and duplicates neither the backlog nor the technical specs; those remain the detailed sources. CONFIRMED/PROPOSED/TBD/FUTURE are distinguished throughout.*
