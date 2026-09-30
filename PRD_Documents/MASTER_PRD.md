# Master Product Requirements Document (PRD) — Veterinary Clinical Intelligence Platform

**Document status:** v1.0 · **Product Source of Truth**
**Date:** 2026-09-30
**Owner:** Product Management (Principal PM)
**Consolidates:** [`PRD.md`](./PRD.md), [`ARCHITECTURE_SPEC.md`](./ARCHITECTURE_SPEC.md), [`PRODUCT_FLOW_SPEC.md`](./PRODUCT_FLOW_SPEC.md), [`VALIDATION_AND_BASELINE.md`](./VALIDATION_AND_BASELINE.md), [`ENGINEERING_SPEC.md`](./ENGINEERING_SPEC.md), [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md), [`SECURITY_SAFETY_SPEC.md`](./SECURITY_SAFETY_SPEC.md), [`BACKLOG_EXECUTION_PLAN.md`](./BACKLOG_EXECUTION_PLAN.md), [`TESTING_QA_STRATEGY.md`](./TESTING_QA_STRATEGY.md), [`PRODUCTION_OPS_PLAN.md`](./PRODUCTION_OPS_PLAN.md).

> **Source-of-Truth Rule.** This PRD is the Product Source of Truth. Supporting documents may expand, implement, test, secure, or operate the requirements defined here, but **they must not independently change product scope or introduce new product behaviour without an approved PRD change** (§M). Where the source documents disagreed, this PRD uses the reconciliation in [`VALIDATION_AND_BASELINE.md`](./VALIDATION_AND_BASELINE.md) and flags anything still unresolved (§L).

**Purpose & audience.** A new PM, Engineer, AI/ML Engineer, Clinical Lead, QA Lead, Security Lead, or Leadership stakeholder should be able to read this and understand *what the product is, why it exists, what is being built, in what order, what each phase delivers, how success is measured, and where the boundaries are* — without reading the technical specs first. It stays product-level; the supporting documents hold the deeper detail.

**Labels used throughout:** **CONFIRMED** · **PROPOSED** · **TBD** · **DECISION REQUIRED** · **FUTURE**.

---

## A · What the product is (in one place)

A decision-support platform for **credentialed veterinarians**. A vet asks a real clinical question about a specific animal and receives a clear, **species-aware, fully cited** answer whose every claim can be opened to its source, and can optionally turn it into a reviewed SOAP note. It is **not** a general chatbot and **not** an autonomous veterinarian: it retrieves and verifies real evidence *before* writing, and the vet always decides.

**Two rules govern the whole product (CONFIRMED):**
1. **Evidence before words** — the AI writes only over retrieved, verified evidence; nothing unsupported reaches the vet.
2. **The vet decides** — the product supports judgment, never replaces it, and never saves a clinical record without human review.

**Primary users:** general-practice vet (primary), referral/specialist vet, early-career vet, and a clinical-governance/practice lead (oversight). Full personas in [`PRD.md`](./PRD.md) §3.

---

## B · Requirement Hierarchy & ID scheme (stable, traceable)

Requirements cascade so any lower item traces to a business objective, and any supporting document traces back to an ID here. **IDs are stable across versions** — they are never renumbered; deprecated items are marked, not deleted.

`Business/Product Objective (OBJ) → Product Requirement (PR) → User Requirement (UR) → System/Capability Requirement (CAP) → Acceptance Criteria (AC)`

- **OBJ-n** — why we build (business/product objective).
- **PR-n** — what the product must deliver.
- **UR-n** — what the user needs to experience.
- **CAP-n** — the capability the system must provide. **CAP items map to the detailed IDs already in the specs** (FR-/AI-/SAF-/DP-/NFR-/UX-), which remain the fine-grained requirement layer.
- **AC** — how we know it's met (testable; QA/AI-ML/Clinical own the evidence).

### B.1 Product Objectives (OBJ)
- **OBJ-1** Give vets fast, species-aware, evidence-grounded answers they can *trust and verify*. (→ PR-1, PR-2, PR-3)
- **OBJ-2** Make clinical decision-support *safe* — never unsupported, never a silent decision. (→ PR-4, PR-6)
- **OBJ-3** Fit the vet's workflow — cited answers and reviewed documentation without extra work. (→ PR-3, PR-5)
- **OBJ-4** Be operable and improvable as a real clinical product — auditable, monitored, safely evolved. (→ PR-7, PR-8)

### B.2 Product Requirements (PR) → mapped capabilities
| PR | Product requirement | User req (UR) | Capability IDs (spec layer) |
|---|---|---|---|
| **PR-1** | Understand a clinical question in context (species, patient, concepts) | UR-1 ask naturally; UR-2 set context | FR-002/003/004/005/006, AI-003 |
| **PR-2** | Retrieve & combine real evidence via DAT, then verify it | UR-3 trustworthy answer | FR-007/008/009/010/011/012/013, AI-005/006/007 |
| **PR-3** | Present a cited, confidence-flagged answer the vet can verify | UR-4 open the source; UR-5 see uncertainty | FR-014/015, AI-001/002/004/009, UX-001..010 |
| **PR-4** | Behave safely on every hard case (see §E) | UR-6 honest limits | SAF-001..009, FR-020/021 |
| **PR-5** | Produce a reviewed, cited SOAP note | UR-7 documentation | FR-016/017/018 |
| **PR-6** | Keep the vet in control; require human review of records | UR-8 I decide | SAF-003/006 |
| **PR-7** | Be auditable, secure, and privacy-preserving | UR-9 my data is safe | FR-022, DP-001..008, SAF-007 |
| **PR-8** | Be validated, released, monitored, and improved responsibly | UR-10 reliable over time | NFR-001..010, AI/ML + QA + Prod docs |

*(UR-1..UR-10 are the user-experience statements behind each PR; the detailed CAP/FR items live in the specs and are traced in §K.)*

---

## C · Phase-wise Product Evolution

The product evolves through **seven phases**. Each phase is understandable on its own and continues the previous one. Phases are outcome-based; **dates are not set** (they depend on the open decisions in §J) — progression is by exit criteria.

### Phase 0 · Product Foundation
- **Objective:** establish the secure, credentialed foundation every clinical capability sits on.
- **User value:** a vet can trust that only verified professionals access the tool and their data is protected.
- **Capabilities introduced:** authenticated access + veterinarian verification; patient/species/context capture and reuse; the secured single entry point; audit foundation. (PR-1 partial, PR-7)
- **Clinical intelligence:** none yet (foundation only).
- **Knowledge sources:** none online; environments and data isolation stood up.
- **System behaviour:** deny by default; no clinical function without a valid session; context stored, reused on follow-ups.
- **UX:** login, patient/context entry, empty query workspace.
- **Dependencies:** auth mechanism (DECISION REQUIRED, §J), environment setup.
- **Validation:** security tests (authn/z, isolation); no real PHI outside production.
- **Safety:** access control; store separation; audit on.
- **Measurable outcomes:** 100% clinical calls authenticated; 0 unauthenticated internal access. Targets `TBD`.
- **Exit criteria:** secure foundation + context service operational; security basics verified.
- **Into next phase:** the platform can safely accept a query; now it needs knowledge to answer.

### Phase 1 · Knowledge & Clinical Intelligence Foundation
- **Objective:** build the trusted knowledge base and the understanding layer, offline, before any live answering.
- **User value:** answers will be grounded in real veterinary knowledge, not model memory.
- **Capabilities introduced:** offline ingestion of the four knowledge families (textbooks → knowledge graph; PMC → RAG index + provenance; SNOMED/VeNom/LOINC → ontology store; pharmacology → species-keyed DB); concept mapping; query understanding + scope guardrail; species detection + clarification; decomposition. (PR-1, PR-2 partial)
- **Clinical intelligence:** the system can understand a question, detect species, map concepts, and break the question into parts — but does not yet answer.
- **Knowledge sources:** all four, versioned, with dates retained (freshness).
- **System behaviour:** out-of-scope rejected before retrieval; low species confidence → clarify; unmapped terms flagged.
- **UX:** progress feedback for understanding; species chip + clarification prompt.
- **Dependencies:** embedding model, vector DB, KG engine, pharmacology source, ontology licences (DECISION REQUIRED, §J); routing contract (D-1).
- **Validation:** ingestion quality; concept-mapping accuracy; retrieval plumbing.
- **Safety:** provenance captured at ingestion (enables later verification); "no data" representable for pharmacology.
- **Measurable outcomes:** stores built + versioned; mapping accuracy measured (`TBD`).
- **Exit criteria:** knowledge stores populated & versioned; understanding layer works on test questions.
- **Into next phase:** with knowledge in place, assemble the answering pipeline.

### Phase 2 · Core Clinical Intelligence MVP
- **Objective:** deliver the first usable clinical answer — cited, species-aware, verified.
- **User value:** a vet asks a real question and gets a trustworthy, sourced answer, and can make a reviewed SOAP note.
- **Capabilities introduced:** **DAT orchestration** (Root/Router + parallel children: Clinical Reasoning, Literature/PMC, Ontology/Concept, Pharmacology, Provenance Capture, + **one specialist — Internal Medicine**); retrieval + local re-rank; synthesis + uncertainty aggregation; **deterministic citation-verification gate**; safety/grounding (**fail closed**); grounded LLM generation; cited response `{answer, citations[], confidence, flags[]}`; basic SOAP + review/edit/save + edit provenance. (PR-2, PR-3, PR-4, PR-5, PR-6)
- **Clinical intelligence:** full retrieve → synthesize → verify → ground → generate path; species-conditioned reasoning; species-specific pharmacology; conflict/uncertainty surfaced.
- **Knowledge sources:** all four, read online.
- **System behaviour:** the complete clinical AI behaviour in §E (strong/weak/conflicting/absent evidence, unknown species, incomplete info, pharmacology uncertainty, agent disagreement, unverifiable citations, uncertainty/human review).
- **UX:** cited answer with openable, dated sources; visible confidence/flags; follow-ups reuse context; reviewable SOAP.
- **Dependencies:** all Phase-1 decisions; Foundation LLM (DECISION REQUIRED); degradation/uncertainty thresholds (`TBD`).
- **Validation:** component + pipeline AI evals; safety suite; verifier determinism (internal).
- **Safety:** verify-before-generate; no dose without species; grounded-only generation; human review before save.
- **Measurable outcomes:** end-to-end cited answer; faithfulness measurable; 0 zero-tolerance safety failures internally. Thresholds `TBD`.
- **Exit criteria:** pipeline runs end-to-end; internal safety scenarios pass; no fabricated answers.
- **Into next phase:** the MVP works internally — now prove it clinically.

### Phase 3 · Clinical Validation & Sandbox
- **Objective:** prove the MVP is clinically trustworthy on synthetic data and expert-scored cases.
- **User value:** confidence (for the org) that the product is safe enough to put in front of real vets.
- **Capabilities introduced:** none new — validation of Phase 2. Eval harness + clinical case set operational.
- **Clinical intelligence:** unchanged; measured.
- **Knowledge sources:** controlled corpus slice; synthetic patients.
- **System behaviour:** unchanged; observed under full flows.
- **UX:** full journeys exercised (login → answer → SOAP) in sandbox.
- **Dependencies:** clinical panel + case volumes (DECISION REQUIRED, VD-2); thresholds incl. faithfulness gate (VD-1); validation data policy (VD-3/SD-8).
- **Validation:** Sandbox gate (flows complete, latency, no fabricated answers) then Clinical Validation gate (faithfulness ≥ `TBD`, **0 critical** errors, expert sign-off).
- **Safety:** all zero-tolerance safety scenarios pass; fail-closed proven.
- **Measurable outcomes:** faithfulness (E-3) ≥ gate; 0 critical clinical/safety errors; latency within target (`TBD`).
- **Exit criteria:** Sandbox + Clinical Validation gates passed with sign-off.
- **Into next phase:** validated → controlled real-world exposure.

### Phase 4 · Pilot & Controlled Launch
- **Objective:** limited real use by a few vets, closely monitored.
- **User value:** real vets get real value while risk is contained.
- **Capabilities introduced:** live monitoring (three layers), rollback, incident process, feedback capture.
- **Clinical intelligence:** unchanged; observed live.
- **Knowledge sources:** production-controlled; data policy per §J.
- **System behaviour:** as MVP, under monitoring; degrade honestly; fail closed.
- **UX:** production-quality query + SOAP + feedback affordance.
- **Dependencies:** monitoring + rollback + incident process live; pilot cohort + data policy approved.
- **Validation:** Pilot gate — no critical safety incident; faithfulness holds on live sample; feedback acceptable.
- **Safety:** clinical-safety monitoring; AI-incident special handling ready (Prod §3).
- **Measurable outcomes:** adoption/usefulness/citation-open + confirm; live faithfulness; 0 critical incidents. Targets `TBD`.
- **Exit criteria:** pilot completed without critical incident; metrics hold.
- **Into next phase:** controlled → general production.

### Phase 5 · Production & Scale
- **Objective:** operate reliably for the broader vet population.
- **User value:** dependable, everyday clinical support.
- **Capabilities introduced:** full production operations; scalability; governance reviews.
- **Clinical intelligence:** unchanged core; potential additional species (FUTURE) validated per species.
- **Knowledge sources:** maintained on a cadence (`TBD`).
- **System behaviour:** unchanged rules at scale; parallel DAT must not degrade verification.
- **UX:** stable, accessible, performant.
- **Dependencies:** regulatory scope resolved (DECISION REQUIRED, D-10); full security review; rollback drilled.
- **Validation:** Production gate (all prior green, security review, rollback, audit, sign-offs).
- **Safety:** all controls live; incident/rollback proven.
- **Measurable outcomes:** availability, latency, reliability (0 fabricated answers), auditability = 100%. Targets `TBD`.
- **Exit criteria:** stable production operation with governance in place.
- **Into next phase:** operate → continuously improve.

### Phase 6 · Continuous Improvement (ongoing)
- **Objective:** improve and safely evolve without weakening safety.
- **User value:** the product gets better — more knowledge, better answers, new capabilities — without new risk.
- **Capabilities introduced (as classified changes):** performance, knowledge expansion, additional species/specialists (FUTURE), PMS/EHR integration (FUTURE), image interpretation (FUTURE), model improvements.
- **Clinical intelligence:** expanded via validated changes only.
- **System behaviour:** every answer-path change re-runs AI eval + safety suite (+ clinical re-validation); feedback never changes clinical behaviour directly.
- **Dependencies:** governance approvals; validation per change class.
- **Validation:** change-management matrix (Prod §4); re-eval triggers (AI/ML §6).
- **Safety:** no evolution lowers a safety control without Clinical + Safety sign-off.
- **Measurable outcomes:** improvement without regression; safety metrics hold.
- **Exit criteria:** n/a (ongoing).

---

## D · Complete End-to-End Clinical Journey (product view)

Authenticate → select patient & set species/context → ask the question → system understands (intent, species, concepts) and scope-checks → (clarify species if unsure) → decompose → **DAT** dispatches parallel children (reasoning, literature, ontology, pharmacology, specialist, provenance) → retrieve real evidence → rank → synthesize + uncertainty → **verify citations (deterministic gate)** → safety/grounding (**fail closed**) → LLM generates over verified context only → **cited answer + confidence + flags** shown, each source openable and dated → vet reviews sources → follow-up (context retained) → optional **SOAP** → review/edit → save → *(FUTURE)* export to PMS/EHR. Authoritative step-by-step trace: [`PRODUCT_FLOW_SPEC.md`](./PRODUCT_FLOW_SPEC.md).

---

## E · Clinical AI Product Behaviour (what the product must do)

Product-level behaviour on every important case (CONFIRMED; detailed enforcement in the specs):

| Situation | Required product behaviour |
|---|---|
| **Strong evidence** | answer confidently, every claim cited + dated |
| **Weak evidence** | answer with a visible "limited evidence" flag; no false confidence |
| **Conflicting evidence** | present both positions, each cited, with a conflict flag; never silently pick |
| **No/absent evidence** | honest "not covered by our current sources"; no fabrication |
| **Outdated evidence** | expose source dates so the vet judges currency |
| **Unknown/uncertain species** | ask the vet; never guess; no dose without confirmed species |
| **Incomplete patient info** | degrade honestly; flag the gap; proceed only where supportable |
| **Pharmacology uncertainty** | "no reliable species-specific dosing found"; never estimate or substitute |
| **Agents disagree** | treat as conflicting evidence; surface, don't reconcile silently |
| **Citations cannot be verified** | drop/flag the claim; if none survive, no-evidence response |
| **Verifier/safety unavailable** | **fail closed** — block generation, graceful error, no answer |
| **Communicate uncertainty / require human review** | flag low confidence; require vet review before any record is saved |

---

## F · MVP / Pilot / Production / Scale / FUTURE Boundary

So future ideas cannot accidentally become current requirements:

- **MVP (Phase 2–3):** the trust core + one specialist (IM) + basic reviewed SOAP + all four knowledge families + audit + core monitoring. (CONFIRMED)
- **Pilot (Phase 4):** MVP under live monitoring with a small cohort. (CONFIRMED)
- **Production/Scale (Phase 5):** broad availability + full operations + possible additional species (each validated). (CONFIRMED path; species expansion FUTURE)
- **FUTURE:** additional specialists (Oncology/Dentistry/Anesthesia), PMS/EHR export, image interpretation, multi-language, governance analytics. (FUTURE — not MVP dependencies)

---

## G · Product-Level Requirements for Cross-Cutting Concerns

The PRD states *what the product requires*; the named document holds the detail. No cross-cutting behaviour exists unless it traces to a PR here.

- **Security & privacy (PR-7):** authenticated, role-limited access; credentialed-vet only; patient data isolated and encrypted; no external data egress in MVP; auditable. Detail: [`SECURITY_SAFETY_SPEC.md`](./SECURITY_SAFETY_SPEC.md).
- **Clinical safety (PR-4/PR-6):** verify-before-generate; species/drug safety; fail closed; uncertainty surfaced; human review before records. Detail: [`SECURITY_SAFETY_SPEC.md`](./SECURITY_SAFETY_SPEC.md), [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md).
- **AI validation (PR-2/PR-3):** component + pipeline evals; faithfulness as launch gate; expert clinical validation; determinism for verification. Detail: [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md).
- **QA (all PRs):** every requirement has a traced test; clinical/AI features can't pass on engineering tests alone. Detail: [`TESTING_QA_STRATEGY.md`](./TESTING_QA_STRATEGY.md).
- **Release, monitoring, governance, improvement (PR-8):** bundle-based releases/rollback; three monitoring layers; incident handling; controlled feedback. Detail: [`PRODUCTION_OPS_PLAN.md`](./PRODUCTION_OPS_PLAN.md).

---

## H · Metrics & Success Criteria (by phase)

Only metrics already established are listed; **numeric targets are `TBD`** (baseline on data; do not invent).

| Phase | Product/adoption | Clinical usefulness | Evidence/citation | AI performance | Safety | Reliability/ops |
|---|---|---|---|---|---|---|
| 0 Foundation | — | — | — | — | 0 unauth access | availability `TBD` |
| 1 Knowledge | — | — | provenance present | mapping/retrieval acc. `TBD` | — | ingestion success |
| 2 MVP | — | usefulness rating `TBD` | citation coverage; faithfulness (E-3) `TBD` | E-series `TBD` | 0 zero-tolerance failures | latency `TBD` |
| 3 Validation | — | expert acceptance | **faithfulness ≥ gate** | evals meet bar | **0 critical** errors | latency within target |
| 4 Pilot | adoption; retention | usefulness; citation open+confirm | faithfulness (live) | holds live | 0 critical incidents | monitoring healthy |
| 5 Production | broader adoption | sustained usefulness | faithfulness (sampled) | stable | 0 critical incidents | availability/latency `TBD` |
| 6 Improvement | growth | improved usefulness | maintained | improved w/o regression | maintained | maintained |

Metric definitions: [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md) §3, [`ENGINEERING_SPEC.md`](./ENGINEERING_SPEC.md) §11, [`PRODUCTION_OPS_PLAN.md`](./PRODUCTION_OPS_PLAN.md) §2.

---

## I · Product Decision & Governance Model

Who owns which decisions (CONFIRMED ownership; specific names `TBD`):

| Decision area | Owner | Consulted |
|---|---|---|
| Product scope, phase gates, roadmap, PRD changes | **Product** | all |
| Architecture & technology choices | **Engineering** | AI/ML, Security |
| Models, evals, routing, thresholds | **AI/ML** | Clinical, Product |
| Clinical acceptability, validation, safety sign-off | **Clinical Governance** | Safety, Product |
| Test strategy, release-quality sign-off | **QA** | all |
| Security, privacy, regulatory posture | **Security** | Compliance, Product |
| Go/No-go to Pilot & Production | **Leadership** (joint sign-off) | Safety, Clinical, Security, Eng, Product |

**Answer-path or safety-rule changes require Clinical + Safety sign-off; product-scope changes require Product approval via §M.**

---

## J · Consolidated Open Decisions & Status

Single view of decisions from across the set (detail in each source doc). None may be silently assumed.

- **DECISION REQUIRED (blocking build):** Foundation LLM, embedding/re-ranker (D-2/D-7); vector DB, KG engine, pharmacology DB+source (D-3/4/5); DAT routing mechanism (D-1); auth mechanism + vet verification (SD-1/2); source licences (D-11).
- **DECISION REQUIRED (blocking gates):** thresholds incl. faithfulness gate (VD-1/OQ-13); clinical panel + case volumes (VD-2); validation/pilot data policy (VD-3/SD-8); confirm V1 specialist = IM (OQ-9); intent-ambiguity handling (D-4).
- **DECISION REQUIRED (blocking production):** regulatory scope + retention/residency (D-10); encryption-at-rest specifics (SD-4); audit retention (SD-7); incident SLA/owners (SD-10/PD-3); governance owners (PD-7); deployment strategy + monitoring thresholds (PD-1/PD-2).
- **PROPOSED:** all API paths; the gap-closing components (Scope Guardrail, Clarification Gate, Uncertainty Aggregation, Provenance Capture, degradation policy, edit-provenance).
- **CONFIRMED:** the two governing rules; DAT topology; verification-as-gate; species/drug safety; fail-closed; human review; store separation; auditability; MVP boundary.
- **FUTURE:** additional specialists; PMS/EHR; image interpretation; multi-language; governance analytics.

---

## K · Traceability & Source-of-Truth Map

`Master PRD → Architecture → Engineering → AI/ML & Clinical Validation → Security & Safety → Backlog → QA → Production & Monitoring`

| Master PRD element | Architecture | Engineering | AI/ML & Clinical | Security & Safety | Backlog | QA | Production |
|---|---|---|---|---|---|---|---|
| PR-1 Understand in context | ARCH §5 | ENG §2 | E-6/E-9 | S-1 | EP-3/6 | Clinical/AI matrices | monitor drift |
| PR-2 Retrieve+verify (DAT) | ARCH §2/§3 | ENG §4/§5 | E-1..E-3/E-7..E-9 | S-2/3/6 | EP-4..9 | AI matrix | retrieval/citation monitoring |
| PR-3 Cited, flagged answer | ARCH §1/§5 | ENG §5/§6 | E-3/E-5/E-11 | — | EP-3/9 | traceability | faithfulness (live) |
| PR-4 Safe on hard cases | ARCH §7 | ENG §9 | S-1..S-10 | §3/§4 | EP-12 | safety matrix | clinical-safety monitoring |
| PR-5 Reviewed SOAP | ARCH §6 | ENG §6 | E-10 | §3 | EP-11 | clinical matrix | — |
| PR-6 Vet in control | ARCH §7 | ENG §9 | §4.4 | §3 | EP-11/12 | clinical matrix | governance |
| PR-7 Auditable/secure/private | ARCH §7 | ENG §10 | — | §1/§2/§9 | EP-13/15 | security coverage | audit/monitoring |
| PR-8 Validated/released/operated | — | ENG §12/§13 | §7/§8 | §5 | EP-14 | release gates | full plan |

**Rule:** every supporting-document item should trace up to a PR/CAP here; if it doesn't, it is either out of scope or requires a PRD change (§M).

---

## L · Remaining Unresolved Issues (flagged, not silently fixed)

Per the Source-of-Truth Rule, unresolved items are surfaced, not papered over:
- **Corrections C-1/C-2/C-3 are applied** to the source docs (verification gate; response contract; routing contract). **C-5..C-9 remain open** in the source docs (specialist-disagreement wording, explicit fail-closed in the flow doc, intent-ambiguity decision, freshness-display, and extra PRD requirement lines) — tracked in [`VALIDATION_AND_BASELINE.md`](./VALIDATION_AND_BASELINE.md) §11; this Master PRD already states the *intended* behaviour for each.
- **Reference diagrams:** [`ARCHITECTURE.md`](./ARCHITECTURE.md) and the rendered `output/out.md` / `out-*.svg` have been regenerated for C-1 (verification as a post-synthesis gate; Provenance Capture as the DAT child) and now match this PRD.
- All `DECISION REQUIRED` items in §J are unresolved by definition and gate the work that needs them.

---

## M · PRD Change Management

**Principle:** no downstream document may introduce a product requirement that does not exist in this PRD.

**Process for a product-requirement change:**
1. **Propose** — a change request stating the affected OBJ/PR/UR/CAP, the reason, and the expected downstream impact.
2. **Review** — Product leads; consult the owners of any affected area (Eng, AI/ML, Clinical, QA, Security, Ops).
3. **Approve** — Product approves scope; **answer-path or safety changes also require Clinical + Safety sign-off**; go/no-go for major changes per §I.
4. **Version** — bump the PRD version; record the change, rationale, and decision in a change log; **IDs are never reused or renumbered** (deprecate, don't delete).
5. **Propagate** — update the dependent documents (Architecture → Engineering → AI/ML → Security → Backlog → QA → Production) and re-run the validation/re-eval triggers the change class requires (Prod §4, AI/ML §6).
6. **Verify** — confirm downstream docs and tests reflect the change before it is considered done.

**Emergency/production changes** still follow the classified change + validation path (Prod §4); a hotfix never bypasses the safety suite or clinical gate for answer-path behaviour.

---

*This Master PRD is the Product Source of Truth: it consolidates the eleven supporting documents phase-wise, uses a stable OBJ→PR→UR→CAP→AC hierarchy that traces to their detailed IDs, reconciles disagreements via the validation document, states product behaviour without reproducing technical depth, distinguishes CONFIRMED/PROPOSED/TBD/DECISION REQUIRED/FUTURE, and governs its own change process. Supporting documents implement and deepen these requirements; they do not change product scope without an approved PRD change.*
