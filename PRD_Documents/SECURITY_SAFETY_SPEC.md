# Security, Privacy & Clinical Safety Specification — Veterinary Clinical Intelligence Platform

**Document status:** Draft v1.0 · Consistent with the approved Baseline
**Date:** 2026-09-27
**Owner:** Security + Clinical Safety Lead (with Engineering, AI/ML, QA, Compliance)
**Source of truth:** [`VALIDATION_AND_BASELINE.md`](./VALIDATION_AND_BASELINE.md) §12. **Companion controls:** [`ENGINEERING_SPEC.md`](./ENGINEERING_SPEC.md) (§10 security, §13 failure/recovery, §14 environments), [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md) (§5 safety scenarios, §7 lifecycle gates).

**Purpose.** Define the controls that protect veterinarians, patients/clients, clinical data, knowledge sources, AI outputs, and the platform across its lifecycle. This document does **not** redesign the architecture or repeat the engineering spec — it states the *security, privacy, trust, clinical-safety, governance, and risk* controls and how they are gated. Anything undecided is **`TBD` / DECISION REQUIRED**; labels: **CONFIRMED / PROPOSED / TBD / FUTURE**.

> **Lifecycle note:** there is no separate "Product/Project/SDLC" document in this set; the lifecycle stages referenced here are those already defined in [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md) §7 (Development → Internal Testing → Sandbox → Clinical Validation → Pilot → Production) and the environments in [`ENGINEERING_SPEC.md`](./ENGINEERING_SPEC.md) §14.

**Two principles above all:** (1) **least privilege + fail closed** — access is denied by default and safety/verification components block rather than bypass when unavailable; (2) **nothing unsupported reaches the vet, and the vet decides** — clinical safety is a property of the whole pipeline, not a final filter.

---

## 1 · Data Classification — what is sensitive and who may access it

| Class | Examples | Sensitivity | Who may access | Controls |
|---|---|---|---|---|
| **C1 — Patient/Client (PHI-equivalent)** | patient identity, species, signs, lab values, attached images, SOAP notes | **Highest** | the owning vet + role-authorised staff | RBAC, encryption, store isolation, audit, retention policy |
| **C2 — Vet/Account identity** | user identity, role, credential/verification status | High | the user; admins (limited) | RBAC, encryption, audit |
| **C3 — Clinical AI outputs** | answers, citations, confidence/flags, agent outputs, verification results | High (tied to a patient) | owning vet; safety/governance review | audit, access control, provenance retained |
| **C4 — Knowledge corpora** | textbooks, PMC, ontologies, pharmacology data | Medium (licensing-bound) | system (read); ingestion (write) | licence compliance, version control, store separation |
| **C5 — Audit/Observability** | trace IDs, actions, verification/reject counts, edit provenance | High (contains references to C1/C3) | governance/security reviewers | tamper-resistant, access-controlled, retained |
| **C6 — Secrets** | keys, tokens, model/provider credentials | Highest | automated systems only | secrets manager, never in code/logs/URLs |
| **C7 — Operational telemetry/metrics** | latency, error rates, usage | Low | Eng/SRE | **no PHI in metrics** (CONFIRMED) |

**Store separation (CONFIRMED):** C1 (patient/context), C4 (knowledge), agent-state, and C5 (audit) live in **separate stores** with independent access policies, so clinical data is never commingled with corpora and audit cannot be altered by application paths.

---

## 2 · Security & Privacy Model

**2.1 Authentication (CONFIRMED requirement; mechanism `TBD`).** All access passes the single API Gateway with a valid session; deny by default. Mechanism (`OIDC/JWT` `PROPOSED`) — **DECISION REQUIRED**.

**2.2 Authorization / RBAC (CONFIRMED).** Role-based least privilege. Clinical functions and C1/C2/C3 access are limited by role. Exact role model (roles, permissions) — **`TBD`**.

**2.3 Veterinarian identity & credential verification (CONFIRMED requirement; method `TBD`).** Only credentialed veterinary professionals may use clinical functions. How credentials are verified (registry check, manual, third-party) — **DECISION REQUIRED** (ties regulatory scope, §8/D-10).

**2.4 Patient & client data protection (CONFIRMED).** C1 stored in the dedicated, access-controlled Patient/Context Store; **never sent to any external service in MVP**; never placed in URLs/query strings; images stored as attached context only (no interpretation in MVP).

**2.5 Encryption (CONFIRMED requirement; specifics `PROPOSED/TBD`).** In transit externally (TLS `PROPOSED`) and internally (mTLS `PROPOSED`); at rest per store policy (`TBD`). No sensitive data in plaintext logs.

**2.6 Secrets management (CONFIRMED principle).** All C6 secrets in a managed secrets store; never in source, config committed to VCS, logs, or client code; rotation policy `TBD`.

**2.7 API security (CONFIRMED).** Single gateway entry; authN/authZ on 100% of clinical calls; rate limiting; input validation; internal services not reachable externally. Endpoints are `PROPOSED` (baseline OQ-8).

**2.8 Audit logging (CONFIRMED).** Every query records inputs, retrieval, verification/rejection outcomes, output, and (for SOAP) AI-vs-vet edit provenance. Audit is **required, tamper-resistant, and access-controlled**; retention `TBD` (§8).

**2.9 Data retention & deletion (CONFIRMED hook; specifics `FUTURE`/regulatory).** A retention/deletion policy applies to C1 and C5; concrete periods and residency depend on regulatory scope — **DECISION REQUIRED (D-10/OQ-10)**. Deletion of patient data must cascade appropriately (specifics `TBD`).

**2.10 Environment isolation (CONFIRMED).** Real C1 data exists **only in Production**; Development/Testing/Sandbox/Staging use synthetic or strictly de-identified data (Engineering §14). No cross-environment data flow.

**2.11 Third-party integrations.** **MVP: none external** except the identity provider for auth (mechanism `TBD`). PMS/EHR export and image interpretation are **FUTURE** and must pass this spec's controls before use — not MVP dependencies.

**2.12 Access controls (CONFIRMED).** Least privilege across all stores; store separation (§1); access to C1/C5 limited to authorised roles and logged.

**2.13 Security incident handling.** See §5 (unified incident process for security *and* clinical safety).

---

## 3 · Clinical Safety Architecture (for the AI system)

For each risk: the **required behaviour** and **when the system communicates uncertainty / refuses / requests info / requires human review**. These mirror the baseline and the AI/ML safety scenarios (S-1…S-10) and are enforced as pipeline controls (§4), not a single filter.

| Risk | Required behaviour | Communicate uncertainty | Refuse / no-answer | Request info | Human review |
|---|---|---|---|---|---|
| **Incorrect/uncertain species** | clarify before proceeding; never guess | — | — | **yes** (ask species) | — |
| **Incomplete patient info** | degrade honestly; flag the gap | **yes** | — | **yes** (if answer needs it) | — |
| **Unsupported claims** | dropped/flagged by verification gate | — | **yes** (claim removed) | — | — |
| **Weak evidence** | low-evidence flag; no false confidence | **yes** | — | optional | — |
| **Conflicting evidence** | present both, cited, with conflict flag | **yes** | — | — | — |
| **Hallucination** | grounded-only generation; context-strip yields no claims | — | **yes** (block) | — | — |
| **Pharmacology uncertainty** | "no reliable species dosing found"; never estimate | **yes** | **yes** (no dose) | — | — |
| **Dosage risk (species mismatch)** | no dose without confirmed species; block cross-species | — | **yes** (block dose) | **yes** (confirm species) | — |
| **Citation failure (verifier unavailable)** | **fail closed** — block generation | — | **yes** (graceful error) | — | — |
| **Retrieval failure** | reduced-but-honest answer + flag | **yes** | — | — | — |
| **Agent disagreement** | treat as conflicting evidence; surface | **yes** | — | — | — |
| **Out-of-scope question** | decline/redirect; no fabricated clinical answer | — | **yes** (out_of_scope) | — | — |
| **Any saved record (SOAP)** | cannot be saved without vet review | — | — | — | **yes (mandatory)** |

**Human review is mandatory before any clinical record is saved** (CONFIRMED, SAF-006). The system never presents a diagnosis or prescription as its own decision.

---

## 4 · Safety Controls Across the Pipeline (defence in depth)

Safety is applied at **each stage**, not only at the end. Control per stage:

| Pipeline stage | Safety control at this point |
|---|---|
| **User input** | input validation; **Scope Guardrail** rejects out-of-scope before any work |
| **Patient/species context** | require species (or clarify); access-control C1; carry species forward |
| **Concept mapping** | flag unmapped terms (don't drop); codes drive correct routing |
| **DAT orchestration** | parent↔child only (no rogue agent traffic); correct child selection; timeout/quorum degradation; state audited |
| **Retrieval** | return "nothing" honestly on a gap; capture provenance (`source_id ↔ span`) for later verification |
| **Specialist reasoning** | species-conditioned; disagreement surfaced as conflict, not reconciled silently |
| **Pharmacology** | species-keyed; `{no_data}` never substituted; feeds drug/species safety check |
| **Evidence synthesis** | uncertainty aggregation → answer confidence + conflict flags |
| **Citation verification** | **deterministic gate**: unverified claims dropped/flagged; **fail closed** if unavailable |
| **Safety/grounding** | drop ungrounded content; enforce species/drug safety; **fail closed** if unavailable |
| **Final response** | grounded generation only; expose confidence + flags; citations openable + dated |
| **SOAP generation** | built from verified answer only; no fabricated section; **mandatory human review before save**; edit provenance recorded |

**Fail-closed rule (CONFIRMED):** if the verification or safety component is unavailable, generation is **blocked** and a graceful error is returned — never a bypassed or unverified answer.

---

## 5 · Safety Gates + Incident Process

**5.1 Environment safety gates** (what must be reviewed/approved to progress; aligns with AI/ML §7):

| Gate | Must be reviewed/approved before entry |
|---|---|
| **Sandbox** | pipeline runs on synthetic data; all zero-tolerance safety scenarios (S-1/2/3/6/8) pass in Internal Testing; verifier proven deterministic; **no fabricated answers**; security basics (auth, store separation, no PHI) in place; Eng + Product sign-off |
| **Clinical Validation** | expert clinical review passed; citation faithfulness ≥ `TBD`; **0 critical** clinical/safety errors; privacy controls for validation data confirmed; Clinical Lead + Safety sign-off |
| **Pilot** | monitoring + rollback live; incident process operational; pilot cohort + data policy approved; no unresolved blocking risk; Clinical + Safety + Product sign-off |
| **Production** | all prior gates green; security review complete (authn/z, encryption, secrets, audit, retention hook); rollback drilled; full audit/monitoring live; joint Safety + Security + Eng + Product sign-off |

**5.2 Incident process (security *and* clinical safety, unified):**
- **Report:** any suspected unsafe output (wrong species, unsafe dose, unsupported claim shown), data exposure, or access violation is logged and raised immediately.
- **Investigate:** reconstruct the query end-to-end from the audit store (inputs, retrieval, verification outcomes, output, versions in effect).
- **Escalate:** severity-rated (minor/major/critical); a **critical clinical-safety or data-exposure incident** escalates to Safety + Security leads at once.
- **Rollback:** restore the last known-good **versioned bundle** (models + prompts + indexes + pharmacology + ontology), since answers depend on all of them.
- **Corrective action:** root-cause fix; add a regression test/eval case that would have caught it.
- **Re-validation:** re-run the affected evals/safety scenarios (and the clinical gate if the answer path changed) before the fix reaches Production (AI/ML §6 triggers).

---

## 6 · Traceability — Risk → Control → Requirement → Implementation → Test → Clinical Validation → Release → Monitoring

| Risk | Safety control | Requirement | Implementation (component) | Test | Clinical validation | Release gate | Monitoring |
|---|---|---|---|---|---|---|---|
| Unsupported claim shown | verification gate + grounding | FR-013/014, AI-007, SAF-001/005 | Citation Verification + Safety layer | E-3, S-3, S-8 | faithfulness review | Clinical Validation | reject rates; faithfulness sample |
| Cross-species dose | species carried; `{no_data}`; block | FR-010, AI-003, SAF-002 | Pharmacology + Safety | E-7, S-2 | drug/species cases | Clinical Validation (blocking) | safety-incident metric |
| Wrong species | clarify on low confidence | FR-004, UX-003 | Species Detection + Clarification Gate | E-6, S-1 | species/flip cases | Internal/Clinical | species-error monitoring |
| Verifier/safety outage → unsafe answer | fail closed | SAF-001/005 | Verification + Safety | S-6 | — | Internal (blocking) | fail-closed event rate |
| Hallucination | grounded-only generation | FR-014, AI-001 | LLM contract | E-5, S-8 | context-strip/red-team | Clinical Validation (blocking) | behaviour drift |
| Conflicting/weak evidence hidden | uncertainty aggregation + flags | FR-020, AI-004 | Synthesis + Uncertainty | E-11, S-5/S-4 | conflict/low-evidence cases | Clinical Validation | uncertainty-flag rates |
| Out-of-scope answered | Scope Guardrail | FR-021 | Query Understanding | S-3 scope | scope cases | Internal | out-of-scope handling rate |
| Record saved without review | mandatory review | SAF-006 | SOAP + UI | S-10 | note review | Internal/Clinical | save-without-review = 0 |
| PHI exposure | RBAC, encryption, store isolation, no PHI in logs | DP-001..008 | Gateway + stores | T-SEC-* | privacy review | Production (security) | access-violation alerts |
| Unauthorised access | authn/z, least privilege | FR-001, DP-002 | Auth + Gateway | T-AUTH-* | — | Production | auth failure/anomaly |
| Untraceable query | audit logging | FR-022, SAF-007 | Audit store | T-AUD-* | reconstruct a query | Internal | audit-write failures |

Every risk has a control, a requirement, an implementation, a test, a validation step, a release gate, and a monitoring signal.

---

## 7 · Risk Register (security + clinical safety), concise

| ID | Risk | Type | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|---|---|
| RS-1 | Unsafe/unsupported claim reaches vet | Clinical | med (unmitigated) | critical | verification gate + grounding + faithfulness gate | mitigated by design; validate |
| RS-2 | Cross-species/absent-data dosing error | Clinical | med | critical | species end-to-end; `{no_data}`; block | mitigated by design; validate |
| RS-3 | Fail-open under component outage | Clinical/Sec | low | critical | fail-closed rule; chaos tests | CONFIRMED control |
| RS-4 | PHI exposure / commingling | Privacy | low-med | high | store separation; encryption; RBAC; no PHI in logs | mitigated; verify |
| RS-5 | Unauthorised / non-vet access | Security | med | high | authn/z; vet verification; least privilege | mechanism `TBD` |
| RS-6 | Secret leakage | Security | low-med | high | secrets manager; no secrets in code/logs | CONFIRMED principle |
| RS-7 | Audit tampering / gaps | Governance | low | high | tamper-resistant, access-controlled audit | verify implementation |
| RS-8 | Knowledge drift → stale/wrong answers | Clinical | med | high | versioning; re-eval triggers; freshness signalling | CONFIRMED process |
| RS-9 | Licence/regulatory non-compliance | Governance | med | high | licence compliance; resolve regulatory scope | `TBD` (D-10) |
| RS-10 | Over-reliance / automation bias | Clinical | med | high | "you decide" framing; mandatory review; uncertainty shown | CONFIRMED control |
| RS-11 | Retention/residency non-compliance | Privacy | med | high | retention hook; resolve specifics | `TBD` (D-10) |
| RS-12 | Injection / malicious input | Security | med | med | input validation; scope guardrail; no external calls (MVP) | verify |

---

## 8 · Open Decisions (DECISION REQUIRED — TBD)

- **SD-1** Authentication mechanism (OIDC/JWT `PROPOSED`) and session policy.
- **SD-2** Veterinarian credential-verification method.
- **SD-3** RBAC role/permission model.
- **SD-4** Encryption-at-rest specifics; secret rotation policy.
- **SD-5** Data retention periods, deletion cascade, and residency — ties **regulatory scope (D-10/OQ-10)**.
- **SD-6** Regulatory classification of the product as veterinary decision-support (jurisdictions, obligations).
- **SD-7** Audit retention window and tamper-resistance mechanism.
- **SD-8** Data policy for Clinical Validation/Pilot (synthetic vs de-identified) — also VD-3.
- **SD-9** Harm-severity rubric definitions (what counts as "critical") — also VD-5.
- **SD-10** Incident SLA/escalation thresholds and responsible owners.
- (Plus inherited model/tech decisions D-1..D-20 where they affect the security surface.)

---

## 9 · Production-Readiness Requirements (security + safety)

Before Production, all must be true:
1. **Security:** authn/z on 100% of clinical calls; encryption in transit + at rest; secrets in a manager; least-privilege RBAC; store separation verified; no PHI in logs/metrics/URLs.
2. **Privacy:** patient data isolated and access-controlled; retention/deletion policy active (SD-5); vet verification enforced (SD-2).
3. **Clinical safety:** all zero-tolerance scenarios (S-1/2/3/6/8) pass; fail-closed proven; faithfulness ≥ gate; **0 critical** errors in Clinical Validation and Pilot.
4. **Governance:** audit complete and tamper-resistant; every query reconstructable; incident process operational with owners (SD-10).
5. **Resilience:** rollback drilled to the last known-good versioned bundle; monitoring + alerts live (AI/ML §8).
6. **Compliance:** regulatory scope resolved (SD-5/SD-6); source licences confirmed.
7. **Sign-off:** joint Safety + Security + Clinical + Eng + Product approval recorded.

---

## 10 · Final Approval Criteria

- **Sandbox approval:** security basics in place (auth, store separation, no real PHI); zero-tolerance safety scenarios pass in Internal Testing; verifier deterministic; no fabricated answers; Eng + Product + Safety sign-off.
- **Clinical Validation approval:** faithfulness ≥ `TBD`; **0 critical** clinical/safety errors; privacy controls for validation data confirmed; Clinical + Safety sign-off.
- **Pilot approval:** monitoring + rollback + incident process live; cohort and data policy approved; no unresolved blocking security/safety risk; Clinical + Safety + Product sign-off.
- **Production approval:** §9 fully satisfied; rollback drilled; regulatory scope resolved; joint Safety + Security + Clinical + Eng + Product sign-off recorded.

**Any critical clinical-safety or data-exposure incident is release-blocking and, in production, a rollback trigger.**

---

*This specification defines the security, privacy, trust, clinical-safety, governance, and risk controls for the platform without redesigning the architecture or repeating the engineering spec. Undecided security/privacy/regulatory/safety items are marked `TBD / DECISION REQUIRED`; the CONFIRMED controls are the baseline's fixed rules (least privilege, fail closed, verification gate, species/drug safety, human review, store separation, auditability). It is ready for Security, Clinical, Engineering, QA, and Compliance teams to operate against, pending the §8 decisions.*
