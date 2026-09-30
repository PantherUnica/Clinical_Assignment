# MVP Product Backlog & Execution Plan — Veterinary Clinical Intelligence Platform

**Document status:** Draft v1.0 · Execution plan
**Date:** 2026-09-27
**Owner:** Product / Program Management (with all delivery teams)
**Source of truth:** [`VALIDATION_AND_BASELINE.md`](./VALIDATION_AND_BASELINE.md) §12 + [`ENGINEERING_SPEC.md`](./ENGINEERING_SPEC.md) §20 (MVP boundary). **Companions:** [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md), [`SECURITY_SAFETY_SPEC.md`](./SECURITY_SAFETY_SPEC.md).

**What this document answers:** *"What exactly does each team need to build, validate, and complete to get the MVP into controlled clinical use?"* It does **not** repeat the architecture, engineering, or security specs — it turns them into executable work. Every epic traces to an approved requirement/decision. No new features. Dates are **not** invented; sequencing is by dependency. Undecided items are `TBD` and gate the work that needs them.

**Teams:** PM (Product), BE (Backend), FE (Frontend), ML (AI/ML), DATA (Data/Ingestion), CLIN (Clinical), QA, SEC (Security), DEVOPS.

---

## 1 · MVP Scope & Boundaries

**MUST build (MVP) — from Engineering Spec §20 / Baseline §12.7:** auth + vet verification; API gateway; clinical query service; patient context; query understanding + scope guardrail; species detection + clarification gate; concept mapping; decomposition; DAT root + core children (Clinical Reasoning, Literature/PMC, Ontology/Concept, Pharmacology, Provenance Capture) + **one specialist (Internal Medicine)**; retrieval + all knowledge stores; synthesis + uncertainty; **citation verification gate**; safety layer (**fail closed**); LLM generation; response contract `{answer, citations[], confidence, flags[]}`; basic SOAP + review/edit/save + edit provenance; audit + core monitoring; offline ingestion for all four knowledge families.

**NOT in MVP (deferred):** additional specialists (Oncology/Dentistry/Anesthesia); image interpretation (attach-only in MVP); PMS/EHR export; concrete retention/residency automation (policy hook only); multi-language; governance analytics.

**Boundary rule:** if a piece of work does not serve a MUST item above, it is out of this backlog.

---

## 2 · Workstreams (→ Epics)

| Epic | Workstream | Primary team(s) | Traces to |
|---|---|---|---|
| **EP-1** | Platform foundation & infrastructure | DEVOPS, BE | Eng §1/§14, NFRs |
| **EP-2** | Authentication & veterinarian verification | SEC, BE | FR-001, DP-001/002, SD-1/2/3 |
| **EP-3** | Clinical query experience (app/UI) | FE, PM | FR-002/015, UX-001..010 |
| **EP-4** | Knowledge ingestion (offline) | DATA, ML | FR ingestion, Eng §7 |
| **EP-5** | RAG & retrieval services | ML, BE | FR-008, E-1/E-2 |
| **EP-6** | Concept mapping & ontology | ML, DATA | FR-005, routing (D-1) |
| **EP-7** | DAT orchestration | BE, ML | FR-007, AI-005/006, GAP-5 |
| **EP-8** | Pharmacology intelligence | DATA, ML | FR-010, SAF-002 |
| **EP-9** | Evidence synthesis, citations & verification | ML, BE | FR-012/013, AI-007 |
| **EP-10** | Specialist capability (Internal Medicine) | ML, CLIN | FR-011 |
| **EP-11** | SOAP generation & review | ML, FE, BE | FR-016/017/018 |
| **EP-12** | Clinical safety layer | SEC, ML, CLIN | SAF-001..009, Sec §4 |
| **EP-13** | Auditability & observability | BE, DEVOPS | FR-022, Eng §11 |
| **EP-14** | AI/ML evaluation & clinical validation harness | ML, CLIN, QA | AI/ML spec §3..§7 |
| **EP-15** | Security, privacy & governance controls | SEC, DEVOPS | Security spec §2/§9 |

---

## 3 · Backlog (Epics → Features → representative User Stories → Task clusters)

Stories are implementation-ready, not micro-split. Each carries acceptance criteria (AC), owner, priority (P0 = MVP-blocking, P1 = MVP, P2 = should), and key dependencies.

### EP-1 · Platform foundation & infrastructure — *P0, DEVOPS/BE*
- **F1.1 Environments & isolation** — Dev/Test/Sandbox/Staging/Prod with no real PHI outside Prod. *Stories:* stand up environments; enforce data-isolation policy. *AC:* lower envs use synthetic data only; promotion path exists. *Dep:* SD-5 (residency) for Prod.
- **F1.2 Service scaffolding & interfaces** — pluggable interfaces so model/store choices (`TBD`) can slot in. *AC:* components swappable without rewrite (NFR-010).
- **F1.3 CI/CD & config/secrets baseline** — pipeline + secrets manager. *AC:* no secrets in code/logs; deploys reproducible.

### EP-2 · Authentication & vet verification — *P0, SEC/BE*
- **F2.1 AuthN/session at gateway.** *Story:* as a vet I sign in and get a scoped session. *AC:* unauthenticated calls rejected; 100% clinical calls authed. *Dep:* SD-1.
- **F2.2 RBAC.** *AC:* role limits clinical + C1/C2/C3 access. *Dep:* SD-3.
- **F2.3 Veterinarian credential verification.** *AC:* only credentialed vets use clinical functions. *Dep:* **SD-2 (blocking decision)**.

### EP-3 · Clinical query experience — *P0/P1, FE/PM*
- **F3.1 Patient/species/context capture + reuse.** *AC:* context stored, reused on follow-ups (FR-002/003). *Dep:* EP-13 store.
- **F3.2 Ask/submit + progress states.** *AC:* stage feedback ("understanding→retrieving→verifying→writing"), no frozen screen (UX-002).
- **F3.3 Cited answer view.** *AC:* each claim shows an openable, **dated** citation; confidence + flags visible (FR-015, C-2 contract, C-8).
- **F3.4 Species chip + clarification prompt.** *AC:* species shown/correctable; clarification prompt on low confidence (UX-003, GAP-1).
- **F3.5 Uncertainty/scope messaging.** *AC:* low/conflicting evidence and out-of-scope shown plainly (UX-004/010).

### EP-4 · Knowledge ingestion (offline) — *P0, DATA/ML*
- **F4.1 Textbook pipeline → KG.** *AC:* facts/relations extracted; bad docs quarantined; corpus versioned. *Dep:* source licences (D-11).
- **F4.2 PMC RAG pipeline.** *Stories:* ingest→clean→chunk→embed→index; write `chunk→source_id+date` to Citation store. *AC:* index built; provenance + dates present. *Dep:* embedding model (D-2), vector DB (D-3).
- **F4.3 Ontology load (SNOMED/VeNom/LOINC).** *AC:* codes normalized, versioned. *Dep:* licences.
- **F4.4 Pharmacology load.** *AC:* species dosing/interactions structured; "no data" representable. *Dep:* pharmacology source (D-5).
- **F4.5 Versioning & freshness.** *AC:* every store versioned; dates retained (AI-009).

### EP-5 · RAG & retrieval services — *P0, ML/BE*
- **F5.1 Literature retrieval + local re-rank.** *AC:* top-k + re-rank; passages carry source_ids/scores (FR-008, CON-3). *Dep:* EP-4.2, models `TBD`.
- **F5.2 Textbook/factual retrieval.** *AC:* facts returned with source refs (FR-009).
- **F5.3 Retrieval degradation.** *AC:* empty+low-confidence+flag on gap; no fabrication.

### EP-6 · Concept mapping & ontology — *P0, ML/DATA*
- **F6.1 Term→code mapping.** *AC:* recognised terms mapped; unmapped flagged (FR-005).
- **F6.2 Concept expansion (DAT child).** *AC:* synonyms/related codes returned (CON-2).
- **F6.3 Routing contract.** *AC:* selection = f(concepts + subquery labels), deterministic set (C-3). *Dep:* **D-1 mechanism**.

### EP-7 · DAT orchestration — *P0, BE/ML*
- **F7.1 Root/Router fan-out + collect.** *AC:* parallel dispatch; parent↔child only; structured returns (FR-007, AI-005).
- **F7.2 Barrier + synthesis trigger.** *AC:* synthesis only after barrier (AI-006).
- **F7.3 Degradation policy.** *AC:* timeout/quorum → partial+flag or graceful error (GAP-5). *Dep:* **D-3 values**.
- **F7.4 Provenance Capture child.** *AC:* `source_id↔span` written at retrieval (C-1).
- **F7.5 Agent-state + audit hooks.** *AC:* run graph reconstructable.

### EP-8 · Pharmacology intelligence — *P0 (safety-critical), DATA/ML*
- **F8.1 Species-keyed lookup.** *AC:* `{drug,species}`→dosing/interactions+sources; missing→`{no_data}`, never substitute (FR-010).
- **F8.2 Drug/species safety feed.** *AC:* feeds safety layer's dose block (SAF-002).

### EP-9 · Synthesis, citations & verification — *P0, ML/BE*
- **F9.1 Cross-source synthesis + uncertainty.** *AC:* candidate answer + claim→source map + confidence + conflicts (FR-012, GAP-3).
- **F9.2 Deterministic citation verification gate.** *AC:* claims matched to source; unverified dropped; reproducible; **fail closed** (FR-013, AI-007, C-6). *Dep:* EP-4.2 provenance.
- **F9.3 Grounded generation.** *AC:* LLM writes over verified context only; context-strip yields no claims (FR-014, AI-001). *Dep:* LLM `TBD` (D-1/7).

### EP-10 · Specialist capability (Internal Medicine) — *P1, ML/CLIN*
- **F10.1 IM specialist agent.** *AC:* domain findings + sources + confidence; species-conditioned (FR-011). *Dep:* EP-7, CLIN review.
- **F10.2 Disagreement handling.** *AC:* specialist vs literature disagreement surfaced as conflict (C-5).

### EP-11 · SOAP generation & review — *P1, ML/FE/BE*
- **F11.1 SOAP from verified answer.** *AC:* S/O/A/P populated; citations preserved; no fabricated section (FR-016).
- **F11.2 Review/edit + mandatory review-before-save.** *AC:* cannot save without review (SAF-006).
- **F11.3 Edit provenance.** *AC:* AI-vs-vet content recorded on save (FR-017, GAP-2).

### EP-12 · Clinical safety layer — *P0, SEC/ML/CLIN*
- **F12.1 Scope guardrail.** *AC:* out-of-scope rejected pre-retrieval (FR-021, GAP-4).
- **F12.2 Grounding + species/drug safety enforcement.** *AC:* ungrounded dropped; no dose without species (SAF-001/002/005).
- **F12.3 Fail-closed behaviour.** *AC:* verifier/safety unavailable → block generation (C-6).
- **F12.4 Uncertainty surfacing.** *AC:* low/conflicting evidence flagged in response (FR-020). *Dep:* **D-5 thresholds**.

### EP-13 · Auditability & observability — *P0, BE/DEVOPS*
- **F13.1 Audit of every query.** *AC:* inputs/retrieval/verify/output reconstructable (FR-022).
- **F13.2 Core monitoring.** *AC:* latency, retrieval, agent exec, citation coverage, verify/safety failures, errors, SOAP failures (Eng §11).
- **F13.3 No PHI in metrics.** *AC:* metrics contain no C1 data.

### EP-14 · AI/ML evaluation & clinical validation harness — *P0, ML/CLIN/QA*
- **F14.1 Eval harness + datasets.** *AC:* val/test separation; versioned; leakage prevention (AI/ML §6).
- **F14.2 Component + pipeline evals.** *AC:* E-1..E-12 runnable; faithfulness (E-3) measurable.
- **F14.3 Safety scenario suite.** *AC:* S-1..S-10 automated where possible.
- **F14.4 Clinical case set + expert review.** *AC:* species/specialty/hard-case coverage; dual review (AI/ML §4). *Dep:* **VD-1/VD-2 decisions**, CLIN panel.

### EP-15 · Security, privacy & governance — *P0, SEC/DEVOPS*
- **F15.1 Encryption in transit + at rest.** *AC:* TLS/mTLS; at-rest per policy (DP-001). *Dep:* SD-4.
- **F15.2 Store separation + access control.** *AC:* C1/C4/agent-state/audit isolated; least privilege (DP-003/004).
- **F15.3 Retention/deletion hook.** *AC:* policy hook active; cascade defined (DP-007). *Dep:* **SD-5/D-10**.
- **F15.4 Incident process.** *AC:* report→investigate→escalate→rollback→corrective→re-validate operational (Sec §5). *Dep:* SD-10.

---

## 4 · Dependencies & Critical Path

**Foundational (must exist early, unblock most work):** EP-1 (envs/scaffolding), EP-13 (stores/audit), EP-15 (security baseline), EP-4 (ingestion → the stores everything reads).

**Critical path (the longest must-finish-in-order chain):**
`EP-4 ingestion (esp. PMC index + provenance) → EP-5 retrieval → EP-9 synthesis + verification gate + grounded generation → EP-12 safety layer → EP-14 evals + clinical validation → gates`.
This chain is the trust core; nothing ships without it.

**Parallelizable once foundations exist:**
- FE (EP-3) can build against mocked responses while BE/ML build the pipeline.
- EP-2 (auth) parallel to the query pipeline.
- EP-6 (concept/ontology), EP-8 (pharmacology), EP-10 (specialist) parallel as DAT children, all feeding EP-7/EP-9.
- EP-11 (SOAP) starts once EP-9 produces verified answers.

**Hard blockers (decisions that gate build, not just polish):**
- **D-1 routing mechanism** → EP-6.3 / EP-7.1 selection.
- **D-2/D-3/D-7 models + vector DB** → EP-4.2 / EP-5 / EP-9.3.
- **D-5 pharmacology source** → EP-8.
- **SD-2 vet verification** → EP-2.3.
- **SD-5/D-10 regulatory scope** → EP-15.3 / Production only.
- **VD-1/VD-2 thresholds + clinical panel** → EP-14.4 / Clinical Validation gate.

---

## 5 · MVP Execution Sequence (by dependency, not dates)

1. **Foundations:** environments, scaffolding, security baseline, stores, audit (EP-1/13/15).
2. **Knowledge preparation:** ingest all four families; build PMC index + provenance; version everything (EP-4). *Blocked by model/DB decisions.*
3. **Pipeline build (parallel where possible):** understanding/scope/species/concept/decomposition → DAT + children (reasoning, literature, ontology, pharmacology, provenance, IM specialist) → synthesis → **verification gate** → safety → generation (EP-5/6/7/8/9/10/12). FE builds query experience against mocks (EP-3).
4. **AI/ML evaluation:** stand up harness; run component + pipeline evals; iterate to dev bar (EP-14.1-3).
5. **Integration + system testing:** wire real components; internal testing incl. all safety scenarios; verifier determinism proven (QA).
6. **SOAP + review:** once verified answers exist (EP-11).
7. **Sandbox validation:** full flows on synthetic data; latency; no fabricated answers (Gate: Sandbox).
8. **Clinical validation:** expert-scored held-out set; faithfulness ≥ gate; 0 critical (EP-14.4; Gate: Clinical Validation).
9. **Pilot preparation:** monitoring + rollback + incident process live; cohort/data policy approved (Gate: Pilot).
10. **Production readiness:** security review, rollback drill, audit complete, regulatory scope resolved, sign-offs (Gate: Production).

---

## 6 · Definition of Ready / Definition of Done

**Definition of Ready (a story may start when):** it traces to an approved requirement; acceptance criteria are written; dependencies (incl. any blocking decision) are resolved or explicitly stubbed; test approach is known; for clinical/AI work, the eval/validation method is identified.

**Definition of Done (general):** code complete + reviewed; unit/integration tests pass; meets acceptance criteria; observability/audit emitted; no secrets/PHI leakage; documentation updated.

**Definition of Done — clinical & AI features (CONFIRMED, stricter):** engineering completion is **not sufficient**. In addition:
- the relevant **evaluation metric(s)** are measured and meet the agreed bar (E-series);
- the relevant **safety scenarios** (S-series) pass, with **0 zero-tolerance failures**;
- for answer-path features, **clinical review** has signed off (no critical errors);
- behaviour is **reproducible** where required (verification) and **fails closed** where required (safety/verification).
A clinical/AI story that is "code complete" but unmeasured or unreviewed is **Not Done**.

---

## 7 · MVP Readiness Checklist

- [ ] All P0 epics feature-complete and integrated.
- [ ] Ingestion complete for all four knowledge families; stores versioned; provenance + dates present.
- [ ] Full pipeline runs end-to-end; **verification gate + fail-closed** proven.
- [ ] Response contract `{answer, citations[], confidence, flags[]}` + clarification/out-of-scope live.
- [ ] Eval harness live; E-series measured; **faithfulness (E-3) ≥ gate**.
- [ ] Safety suite (S-1..S-10) passing; **0 zero-tolerance failures**.
- [ ] Clinical case set validated by experts; **0 critical** errors; sign-off.
- [ ] Auth + vet verification + RBAC enforced; encryption; store separation; no PHI in logs/metrics.
- [ ] Audit reconstructs any query; monitoring + alerts live.
- [ ] Rollback drilled; incident process operational.
- [ ] Open decisions blocking build are resolved (§8).

---

## 8 · Critical Dependencies & Open Decisions (must be owned/dated)

**Blocking build:** D-1 (routing), D-2/D-3/D-7 (embedding/re-ranker/LLM/vector DB), D-5 (pharmacology source), SD-2 (vet verification), source licences (D-11).
**Blocking gates:** VD-1 (thresholds incl. faithfulness), VD-2 (clinical panel + case volumes), SD-5/D-10 (regulatory scope, retention/residency), D-9/OQ-9 (confirm V1 specialist = IM), D-4 (intent-ambiguity handling).
**Blocking Production only:** SD-4 (encryption-at-rest specifics), SD-7 (audit retention), SD-10 (incident SLA/owners).

Each needs an **owner + target date** (dates not set here by design). Until resolved, dependent stories stay in "blocked."

---

## 9 · Major Risks (execution)

| Risk | Impact | Mitigation |
|---|---|---|
| Model/DB/tech decisions slip | critical-path stall (EP-4/5/9) | decide D-1/2/3/5/7 first; interface isolation lets build start against stubs |
| Faithfulness can't reach gate | no clinical release | prototype verification early on a clinician set; treat as top risk |
| Clinical panel/case set not ready | Clinical Validation gate blocked | stand up EP-14.4 + recruit panel in parallel with build |
| Cross-species dose defect | patient harm | EP-8 + EP-12 safety tests are P0; zero-tolerance |
| Ingestion quality poor | bad facts downstream | quarantine + validation in EP-4; version + re-eval |
| Scope creep (deferred features pulled in) | timeline + risk | enforce §1 boundary rule |
| Reference diagrams/docs drift from corrected baseline | team builds wrong model | regenerate reference diagrams; keep baseline authoritative |

---

## 10 · What must be complete before each gate

**Before Sandbox:** foundations (EP-1/13/15) + ingestion (EP-4) + pipeline (EP-5..9,12) integrated; eval harness up; **all zero-tolerance safety scenarios pass in Internal Testing**; verifier deterministic; no fabricated answers; security basics (auth, store separation, no real PHI).

**Before Pilot:** Sandbox passed; **Clinical Validation gate met** (faithfulness ≥ gate, 0 critical, expert sign-off); SOAP (EP-11) complete; monitoring + rollback + incident process live; pilot cohort + data policy approved; blocking decisions resolved.

**Before Production:** Pilot completed with no critical safety incident; faithfulness + safety hold on live samples; full security review (encryption, secrets, RBAC, audit, retention hook); regulatory scope resolved (SD-5/6); rollback drilled; audit complete; **joint Safety + Security + Clinical + Eng + Product sign-off**.

---

*This plan translates the approved specifications into executable work for every team, traces each epic to a requirement/decision, sequences by dependency (no invented dates), and holds clinical/AI features to a stricter Definition of Done than engineering completion. It repeats none of the architecture, engineering, or security detail — it says what to build, in what order, and what "complete" means to reach controlled clinical use.*
