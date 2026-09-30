# Product–Architecture Consistency & Validation + Baseline Product Specification

**Document status:** Draft v1.0 · Cross-review of the three specification documents
**Date:** 2026-09-27
**Owner:** Product / Architecture (joint)
**Documents reviewed together as one product specification:**
1. **Product Foundation & Requirements** → [`PRD.md`](./PRD.md)
2. **Clinical Intelligence System Architecture** → [`ARCHITECTURE_SPEC.md`](./ARCHITECTURE_SPEC.md) (with reference diagrams in [`ARCHITECTURE.md`](./ARCHITECTURE.md))
3. **User & System Interaction Specification** → [`PRODUCT_FLOW_SPEC.md`](./PRODUCT_FLOW_SPEC.md)

**Scope of this document.** This is a validation pass, not a redesign. It does **not** create a new product, add features, redesign the architecture, or assume undecided technical choices. It checks whether the three documents are internally consistent and engineering-ready, classifies every issue, and consolidates the agreed behaviour into one baseline. **It does not modify the three source documents** — where a correction is needed, it is *recommended* here (Section 11) and reflected in the Baseline (Section 12), to be applied to the source docs as a separate, explicit step.

**Issue classification used throughout:** `CONTRADICTION` · `MISSING` · `DUPLICATE` · `UNCLEAR` · `DECISION REQUIRED — TBD` · `FUTURE` · `CORRECT`.

**Maturity labels:** **CONFIRMED** (fixed design decision) · **PROPOSED** (specific but unratified) · **TBD** (genuinely undecided) · **FUTURE** (deferred beyond V1).

---

## 1 · Executive Consistency Review

The three documents are **substantially consistent and close to engineering-ready.** They share one spine — *authenticate → understand → (clarify/scope) → decompose → DAT parallel retrieval → synthesize → verify → ground → generate → cited answer → optional SOAP* — and the same non-negotiable rules (parent↔child only, retrieve before write, verify before generate, vet decides, nothing invented). The `PROPOSED — TBD` discipline is applied uniformly.

The consistency is not accidental: the architecture spec was derived from the PRD (with an explicit traceability matrix), and the flow spec was derived from both. The most valuable output of that chain is that the **architecture spec already found and resolved three contradictions (CON-1/2/3) and seven gaps (GAP-1..7) in the reference material** — but those resolutions live only in documents 2 and 3. They have **not been reflected back into document 1 (the PRD)**, which still shows the pre-resolution picture in a few places. That back-propagation is the main body of work before this can be a clean baseline.

**Headline findings:**
- **3 issues that block engineering** (Section 2) — all are reconciliations, not new design: the verification-child-vs-gate contradiction still visible in the PRD, the output/response contract drift, and the undefined DAT routing/selection logic.
- **No feature is missing from the product itself.** The gaps are specification-consistency gaps (a resolution recorded in one doc but not another), plus a small number of genuinely undecided policies already correctly marked TBD.
- **The MVP is buildable as scoped**, provided the ~7 gap-closing components are correctly sorted into MVP vs FUTURE (Section 9) — most are MVP because the requirements they serve are MVP.
- **The full clinical query chain validates end-to-end** (Section 8), with two link-level clarifications required (routing selection; specialist-disagreement handling).

**Overall verdict:** **GO to engineering after the Section 2 blockers are closed and the Section 11 corrections are applied to the source docs.** Nothing here requires rethinking the product.

---

## 2 · Critical Issues Blocking Engineering

These must be resolved before epics are written, because engineers would otherwise build to conflicting descriptions.

**V-1 · Citation verification: child vs. gate — `CONTRADICTION`**
- **Where:** PRD §13 DAT tree still lists **"Evidence & Citation Verification"** as a *child node* Root dispatches in parallel. ARCHITECTURE_SPEC §0.3 (CON-1) and §3, and PRODUCT_FLOW_SPEC Flow 7, make verification a **single post-synthesis gate**, with a renamed child **"Provenance Capture"** doing only retrieval-time source tracking.
- **Why it matters:** these are different execution orders. If verification is a parallel child, it runs *before* synthesis on partial evidence; the PRD's own rules (AI-006 synthesis-after-retrieval, AI-007 verify-before-generate) require it to run *after* synthesis and *before* generation. Building the PRD §13 version would violate the PRD §11 rules.
- **What to change:** adopt the architecture resolution everywhere. PRD §13 tree should show **Provenance Capture** as the child and **Citation Verification (gate)** as a post-synthesis step. (Documents affected: **PRD** — correction C-1.)

**V-2 · Response/output contract drift — `CONTRADICTION` / `MISSING`**
- **Where:** PRD (ARCHITECTURE.md connection register #1, and §27) states the query response as `{answer, citations[], soap?}`. ARCHITECTURE_SPEC and PRODUCT_FLOW_SPEC use `{answer, citations[], confidence, flags[]}` and add the variants `{needs_clarification}` and `{out_of_scope}`.
- **Why it matters:** the response schema is the first thing the client team and API team build against. `confidence` and `flags[]` are required to satisfy FR-020/AI-004 (uncertainty) and the early-exit flows; if they are absent from the agreed contract, those requirements cannot be delivered.
- **What to change:** adopt the superset contract as CONFIRMED: `{answer, citations[], confidence, flags[], soap?}` plus the alternate responses `{needs_clarification, options[]}` and `{out_of_scope, reason}`. (Documents affected: **PRD**, and align **ARCHITECTURE_SPEC** wording — correction C-2. Exact field types remain `PROPOSED — TBD`.)

**V-3 · DAT routing / child-selection logic undefined — `UNCLEAR` / `DECISION REQUIRED — TBD`**
- **Where:** All three docs say Root dispatches to "relevant" children/specialists (PRD §13, ARCH §3, FLOW Flow 5/6), but none defines **how relevance is decided** — i.e. how decomposition output + concept mapping determine which specialists and retrieval children are invoked.
- **Why it matters:** this is the heart of "DAT orchestration, not a chatbot." Without a defined selection rule, two engineers will build two different orchestrators, and test coverage for "which agents fire for query X" is impossible.
- **What to change:** specify the routing input→selection contract (e.g. mapped concepts + subquery labels → a deterministic or ruled set of child agents). The *mechanism* (rules vs. learned) is a genuine **DECISION REQUIRED — TBD** (relates to PRD OQ-6 orchestration runtime), but the **contract** (what routing consumes and produces) should be CONFIRMED. (Documents affected: **ARCHITECTURE_SPEC** §3 — correction C-3.)

---

## 3 · Important Improvements (non-blocking, do before or during early engineering)

**V-4 · Two sequence diagrams for the same scenario — `DUPLICATE` / `UNCLEAR`**
- **Where:** PRD §27 and PRODUCT_FLOW_SPEC both trace "kidney disease in a cat." The FLOW version is fuller (adds Scope Guardrail, Clarification Gate, Provenance Capture, Agent-State, audit writes); the PRD version is simpler and omits them.
- **Why it matters:** a reader comparing them may think the simpler one is authoritative. **What to change:** declare the FLOW sequence the authoritative trace; mark PRD §27 as an intentional simplified illustration. (Documents affected: **PRD** note — correction C-4.) Classification for the pair: `CORRECT` individually, `DUPLICATE` in combination.

**V-5 · Specialist disagreement not explicitly handled — `MISSING`**
- **Where:** Failure handling covers "specialist unavailable" (FLOW Flow 6/12) but not "two specialists (or a specialist and the literature) disagree."
- **Why it matters:** the reviewer explicitly asked for this failure mode, and clinicians will hit it. **What to change:** state that disagreement is treated as **conflicting evidence** and surfaced through Uncertainty Aggregation (`conflicts[]`, FLOW Flow 8) rather than silently reconciled — this is *supported by existing FR-020*, so it is a clarification, not a new feature. (Documents affected: **ARCHITECTURE_SPEC** §5 / **PRODUCT_FLOW_SPEC** Flow 8 — correction C-5.)

**V-6 · Safety/grounding must fail closed — `UNCLEAR`**
- **Where:** Flow 12 handles component failure generically; it does not state explicitly that if the **safety/grounding or verification component itself is unavailable**, generation must be **blocked** (fail closed), not skipped.
- **Why it matters:** failing open would let an ungrounded answer through — a direct violation of SAF-001/SAF-005. **What to change:** add an explicit "verification/safety unavailable → block generation, return graceful error" rule. Supported by SAF-001/005, so a clarification. (Documents affected: **PRODUCT_FLOW_SPEC** Flow 12 / **ARCHITECTURE_SPEC** §7 — correction C-6.)

**V-7 · Ambiguous (non-species) question handling — `MISSING` / `DECISION REQUIRED — TBD`**
- **Where:** Clarification exists only for **species** confidence (Clarification Gate). A vague or under-specified *clinical* question has no clarification path; it would proceed to a low-confidence answer.
- **Why it matters:** "ambiguous clinical question" is a listed failure mode. **What to change / decide:** either (a) extend the Clarification Gate to intent ambiguity, or (b) accept proceeding with a low-confidence, flagged answer. Both are consistent with the PRD; **which one** is a `DECISION REQUIRED — TBD`. (Documents affected: **ARCHITECTURE_SPEC** §5 / **PRD** FR-004 scope — correction C-7 records the decision.)

**V-8 · Evidence freshness not surfaced in the UI flows — `UNCLEAR`**
- **Where:** AI-009 requires freshness signalling and the Citation/Evidence Store carries dates (ARCH §4/§7), but no flow shows the date being *displayed* to the vet.
- **Why it matters:** freshness only helps if the vet sees it. **What to change:** add "citation shows source date" to the answer-presentation flow (UX-001 already implies openable citations). Supported by AI-009/UX-001. (Documents affected: **PRODUCT_FLOW_SPEC** Flow 1/11 — correction C-8.)

---

## 4 · Missing Requirements

These are requirements implied by the architecture/flows but not written as PRD requirements. They should be added to the PRD so QA can test them. None is a new feature — each already exists as behaviour in documents 2/3.

| ID | Missing requirement | Evidence it already exists | Class |
|---|---|---|---|
| M-1 | Output contract must include `confidence` and `flags[]`, plus `needs_clarification` / `out_of_scope` responses | ARCH §1/§5, FLOW Flow 2/8 | `MISSING` (→ add to PRD FR-015/§27; see V-2) |
| M-2 | DAT degradation policy (timeout `T`, quorum `Q`) must exist and be configurable | ARCH §3 GAP-5, FLOW Flow 5/12 | `MISSING` (values `DECISION REQUIRED — TBD`) |
| M-3 | Specialist/agent disagreement handled as conflicting evidence | FLOW Flow 8 | `MISSING` (see V-5) |
| M-4 | Verification/safety components fail closed | SAF-001/005 imply it | `MISSING` (see V-6) |
| M-5 | SOAP edit-provenance (AI vs vet) is recorded | ARCH §6 GAP-2, FLOW Flow 10 | `MISSING` (add explicit PRD line under FR-017) |
| M-6 | Image/report accepted but **not interpreted** in V1 (attach-only) | ARCH §8 GAP-7, FLOW Flow 3 | `MISSING`/`FUTURE` (add PRD note under FR-002) |

---

## 5 · Architecture Gaps

The architecture spec already enumerated GAP-1..7 and resolved them with PROPOSED components. Re-validated here against the flows:

| Arch gap | Status after cross-review | Class |
|---|---|---|
| GAP-1 Clarification Gate (species) | Present in ARCH §5 and FLOW Flow 2; threshold `TBD` | `CORRECT` (threshold `DECISION REQUIRED — TBD`) |
| GAP-2 SOAP edit-provenance | Present ARCH §6 / FLOW Flow 10; add to PRD (M-5) | `CORRECT` (needs PRD line) |
| GAP-3 Uncertainty Aggregation | Present ARCH §5 / FLOW Flow 8; feeds output contract (V-2) | `CORRECT` |
| GAP-4 Scope Guardrail | Present ARCH §5/§7 / FLOW Flow 2/12; classifier `TBD` | `CORRECT` (classifier `DECISION REQUIRED — TBD`) |
| GAP-5 Degradation policy | Present ARCH §3 / FLOW Flow 5/12; values `TBD` | `CORRECT` (values `DECISION REQUIRED — TBD`) |
| GAP-6 Retention/residency lifecycle | Present ARCH §7; gated on regulatory scope | `FUTURE` for specifics; policy hook is MVP |
| GAP-7 Image attach-only in V1 | Present ARCH §8 / FLOW Flow 3 | `FUTURE` (interpretation), MVP (attach) |
| **New:** DAT routing/selection contract | Not specified anywhere | `UNCLEAR` (see V-3) — the one genuine architecture gap |

**Only one new architecture gap** surfaced in cross-review: the routing/selection contract (V-3). Everything else the architecture spec already caught.

---

## 6 · User / System Flow Gaps

| Flow area | Finding | Class |
|---|---|---|
| Scope early-exit | Flow 2 + Flow 12 consistent; output contract needs `out_of_scope` (V-2) | `CORRECT` pending C-2 |
| Species clarification | Flow 2 consistent; only species, not intent (V-7) | `MISSING` for intent ambiguity |
| Follow-up context | Flow 9 consistent with FR-003; correctly notes "context reused, not memory-answered" | `CORRECT` |
| Low/No-evidence | Flow 8 thorough; covers thin, conflicting, and absent evidence | `CORRECT` |
| Specialist disagreement | Not explicit (V-5) | `MISSING` |
| Failure: verification/safety outage | Fail-closed not explicit (V-6) | `UNCLEAR` |
| Freshness display | Not shown in a flow (V-8) | `UNCLEAR` |
| SOAP review-before-save | Flow 10/11 enforce it | `CORRECT` |
| Human-in-control | Flow 11 explicit; matches SAF-003/006 | `CORRECT` |

---

## 7 · DAT Validation

Checking the DAT hierarchy against agent responsibilities and orchestration rules across all three docs.

- **Topology (parent↔child only, no peer-to-peer):** consistent across PRD §13, ARCH §3, FLOW Flow 5. — `CORRECT`
- **Parallel fan-out + barrier + synthesis-after-retrieval:** consistent (PRD AI-006, ARCH §3, FLOW Flow 5). — `CORRECT`
- **Structured child return `{evidence[], source_ids[], confidence, metadata}`:** consistent. — `CORRECT`
- **Child roster:** Clinical Reasoning, Literature/PMC, Ontology/Concept (expansion), Pharmacology, Specialists, **Provenance Capture**. — `CORRECT` in ARCH/FLOW; PRD still shows the old "Citation Verification" child (V-1). — `CONTRADICTION` (PRD only)
- **Verification placement:** post-synthesis gate. — `CORRECT` in ARCH/FLOW; contradicts PRD §13 (V-1).
- **Child selection / routing:** undefined (V-3). — `UNCLEAR`
- **Degradation (timeout/quorum):** defined as policy, values TBD (M-2). — `CORRECT` (values `DECISION REQUIRED — TBD`)
- **Ontology duplication (CON-2):** resolved — orchestrator maps, child expands. — `CORRECT`
- **Re-ranking placement (CON-3):** resolved — local (Literature) vs cross-source (Synthesis). — `CORRECT`

**DAT verdict:** internally sound once V-1 (PRD tree) and V-3 (routing contract) are closed.

---

## 8 · End-to-End Clinical Query Validation

Validating every connection in the chain the reviewer specified. Each link is classified.

| # | Chain link | Owning component(s) | Consistent across docs? | Class |
|---|---|---|---|---|
| 1 | Veterinarian → Input | Application/UI | Yes | `CORRECT` |
| 2 | Input → Patient/Species Context | Session/Case Service + Patient/Context Store | Yes (FR-002/003; Flow 3) | `CORRECT` |
| 3 | Context → Query Understanding | Gateway → Query Understanding (+ Scope Guardrail) | Yes; add `out_of_scope` to contract | `CORRECT` pending C-2 |
| 4 | Query Understanding → Clinical Concept Mapping | Species Detection (+ Clarification Gate) → Concept Mapping | Yes; species-only clarification (V-7) | `CORRECT` / `MISSING` (intent) |
| 5 | Concept Mapping → DAT Root/Router | Query Decomposition → Root | Yes, but **routing selection undefined** (V-3) | `UNCLEAR` |
| 6 | Root/Router → Specialist/Retrieval Agents | Root fan-out | Yes (parallel, parent↔child) | `CORRECT` |
| 7 | Agents → Knowledge Retrieval | Literature/VIDX, Reasoning/KG, Ontology/ONTS, Pharmacology/PHDB | Yes (Flow 4) | `CORRECT` |
| 8 | Knowledge Retrieval → Evidence Ranking | Literature local re-rank; Synthesis cross-source rank | Yes (CON-3 resolved) | `CORRECT` |
| 9 | Ranking → Specialist Analysis | Specialist children | Yes (Flow 6) | `CORRECT` |
| 10 | Specialist Analysis → Parent-Level Synthesis | Root → Synthesis + Uncertainty | Yes (Flow 5→8); disagreement handling implicit (V-5) | `CORRECT` / `MISSING` (disagreement) |
| 11 | Synthesis → Citation Verification | Synthesis → Citation Verification gate | Yes in ARCH/FLOW; PRD tree conflicts (V-1) | `CONTRADICTION` (PRD only) |
| 12 | Citation Verification → Safety/Grounding | Verification → Safety/Grounding | Yes; fail-closed not explicit (V-6) | `CORRECT` / `UNCLEAR` (fail-closed) |
| 13 | Safety/Grounding → Final Clinical Response | Safety → LLM → Output | Yes (verify-before-generate) | `CORRECT` |
| 14 | Final Response → Optional SOAP | Output → SOAP Generator | Yes (Flow 10) | `CORRECT` |

**Chain verdict:** every link is present and traceable. Only **link 11** carries a true contradiction (PRD tree vs. gate) and only **link 5** is genuinely under-specified (routing). Links 4, 10, 12 need small clarifications (intent ambiguity, disagreement, fail-closed) that are all supported by existing requirements.

### 8.1 Failure-scenario validation

| Failure scenario | Handled where | Class |
|---|---|---|
| No relevant evidence | Flow 8 (no-evidence response); SAF-008 | `CORRECT` |
| Weak / contradictory evidence | Flow 8 (low-evidence flag; conflicts shown); FR-020 | `CORRECT` |
| Unknown species | Flow 2 Clarification Gate; FR-004 | `CORRECT` (threshold `TBD`) |
| Ambiguous clinical question | Species only; intent ambiguity not handled | `MISSING` (V-7, `DECISION REQUIRED — TBD`) |
| Retrieval failure | Flow 12 (source down → reduced + flag) | `CORRECT` |
| Specialist-agent disagreement | Implicit via conflicts[]; not explicit | `MISSING` (V-5) |
| Citation verification failure | Flow 7/8 (unverified dropped; none → no-evidence) | `CORRECT` |
| Pharmacology uncertainty | "No data" (Flow 4); conflict/low-confidence otherwise | `CORRECT` |
| Model failure | Flow 12 (retry → graceful error, no fabrication) | `CORRECT` |
| Safety check failure | Generic in Flow 12; fail-closed not explicit | `UNCLEAR` (V-6) |

**Failure verdict:** 7 of 10 fully covered; 3 (ambiguous question, specialist disagreement, safety fail-closed) need the small clarifications noted — all supported by existing requirements, none requiring new design.

---

## 9 · MVP Boundary

Validating MVP scope (PRD §23) against the architecture complexity introduced in documents 2/3. The question: does the architecture demand more than the MVP requires?

**MVP includes (CONFIRMED, all serve MVP requirements):**
- Gateway + Auth; Session/Case + Patient/Context; Query Understanding **+ Scope Guardrail** (FR-021); Species Detection **+ Clarification Gate** (FR-004); Concept Mapping; Decomposition.
- DAT Root + core children (Clinical Reasoning, Literature/PMC, Ontology/Concept, Pharmacology, **Provenance Capture**) + **one specialist** (proposed Internal Medicine).
- Synthesis **+ Uncertainty Aggregation** (FR-020); Citation Verification gate (FR-013); Safety/Grounding (FR-014); LLM generation.
- **Degradation policy** (AI-008) — required for a safe MVP.
- Basic SOAP + review/edit/save **+ edit-provenance** (FR-016–018).
- All 8 data stores (each is on the core path).
- Audit/Observability (FR-022).

**Deferred from MVP (FUTURE):**
- Additional specialists (Oncology/Dentistry/Anesthesia) — `FUTURE` (OQ-9 chooses V1 set).
- PMS/EHR export; image **interpretation** (attach-only is MVP) — `FUTURE`.
- Retention/residency **specifics** — policy hook is MVP; concrete rules `FUTURE` pending OQ-10.

**Boundary verdict:** the architecture is **not over-built for MVP.** Every "new" gap-closing component maps to an MVP-level requirement, except retention specifics, extra specialists, and image interpretation, which are correctly FUTURE. The one scoping decision to confirm: **intent-ambiguity clarification (V-7)** — in or out of MVP. — `DECISION REQUIRED — TBD`.

---

## 10 · Decisions Required (`DECISION REQUIRED — TBD`)

Consolidated list of genuinely undecided items surfaced by this review (superset of the PRD's OQ-1..14, adding the ones this cross-review found). None may be silently assumed.

**From cross-review:**
- **D-1** DAT routing/selection contract mechanism (rules vs. learned) — V-3 (relates OQ-6).
- **D-2** Species-confidence clarification threshold — GAP-1.
- **D-3** Degradation policy values (timeout `T`, quorum `Q`) — GAP-5.
- **D-4** Whether intent-ambiguity gets a clarification path or a low-confidence answer — V-7.
- **D-5** Uncertainty thresholds (what confidence/conflict level triggers a "limited evidence" flag) — GAP-3.
- **D-6** Scope-guardrail classifier approach — GAP-4.

**Inherited from PRD (still open):**
- **D-7..D-20** = PRD OQ-1..14: Foundation LLM, Embedding/Re-ranker models, Vector DB, KG engine, Pharmacology DB+source, orchestration runtime, cloud, exact API contracts, V1 specialist set, regulatory scope, source licences/cadence, accessibility target, metric thresholds, image handling extent.

All are `TBD` and must be owned and dated before the components that depend on them are built.

---

## 11 · Final Recommended Corrections

Corrections to apply to the **source documents** (as a separate, explicit step — not done here). Each is supported by existing requirements; none adds a feature or a technology.

| ID | Correction | Document(s) | Resolves | Type |
|---|---|---|---|---|
| **C-1** | Replace the "Evidence & Citation Verification" *child* in the DAT tree with **Provenance Capture** (child) + **Citation Verification (gate)** post-synthesis | **PRD** §13 (and §10 wording) | V-1 | `CONTRADICTION` |
| **C-2** | Define the query response as `{answer, citations[], confidence, flags[], soap?}` + `{needs_clarification, options[]}` + `{out_of_scope, reason}` (field types `TBD`) | **PRD** §27/FR-015; align **ARCH_SPEC** | V-2, M-1 | `CONTRADICTION`/`MISSING` |
| **C-3** | Specify the DAT routing contract: what child-selection consumes (mapped concepts + subquery labels) and produces (agent set); mechanism `TBD` | **ARCH_SPEC** §3 | V-3, D-1 | `UNCLEAR` |
| **C-4** | Mark PRD §27 sequence as a simplified illustration; name the FLOW sequence authoritative | **PRD** §27 | V-4 | `DUPLICATE` |
| **C-5** | State that specialist/agent disagreement is handled as conflicting evidence via Uncertainty Aggregation (`conflicts[]`) | **ARCH_SPEC** §5 / **FLOW** Flow 8 | V-5, M-3 | `MISSING` |
| **C-6** | Add explicit fail-closed rule: verification/safety unavailable → block generation, graceful error | **FLOW** Flow 12 / **ARCH_SPEC** §7 | V-6, M-4 | `UNCLEAR` |
| **C-7** | Record the decision on intent-ambiguity handling (clarify vs. low-confidence answer) | **PRD** FR-004 / **ARCH_SPEC** §5 | V-7, D-4 | `DECISION REQUIRED — TBD` |
| **C-8** | Add "citation displays source date" to answer presentation | **FLOW** Flow 1/11 | V-8 | `UNCLEAR` |
| **C-9** | Add PRD requirement lines for: degradation policy (M-2), SOAP edit-provenance (M-5), image attach-only in V1 (M-6) | **PRD** §10 | M-2/5/6 | `MISSING` |

**Sequencing:** apply C-1, C-2, C-3 first (they unblock engineering — Section 2); C-4..C-9 can follow during epic breakdown.

> **Applied status (2026-09-27):** **C-1, C-2, C-3 have been applied to the source documents** — C-1 and C-2 to [`PRD.md`](./PRD.md) (§13 tree + node table + verification-gate note; FR-015 response contract), and C-3 to [`ARCHITECTURE_SPEC.md`](./ARCHITECTURE_SPEC.md) (§3 routing/child-selection contract). A partial C-4 note was added to PRD §27 (marking it a simplified illustration). **C-5..C-9 remain open** for epic breakdown.

---

## 12 · BASELINE PRODUCT SPECIFICATION

The single, consolidated source of truth for the agreed product behaviour, architecture, and flows — after the Section 11 corrections are accepted. Where a correction is pending, the **corrected** statement is given here and the source doc is noted for update. Labels: **CONFIRMED / PROPOSED / TBD / FUTURE**.

### 12.1 Product (agreed behaviour)
- **CONFIRMED —** A decision-support tool for credentialed veterinarians that returns citation-grounded, species-aware clinical answers and optional SOAP notes. The vet always decides; the system never acts autonomously. (PRD §1–§9.)
- **CONFIRMED —** Every clinical claim is traceable to a specific, openable source; nothing unsupported is presented as fact. (FR-013/014/015, AI-001/002.)
- **CONFIRMED —** Knowledge is bounded by ingested sources; the system says so honestly and surfaces uncertainty. (SAF-008, FR-020.)

### 12.2 Architecture (agreed shape)
- **CONFIRMED —** Layered: Application/Gateway → Clinical Intelligence Orchestrator → DAT Orchestrator → Knowledge & Retrieval → Model Layer → Safety & Citation → Output → SOAP → (FUTURE) External Integration.
- **CONFIRMED —** Eight separated data stores: Textbook KG, PMC Vector Index, Ontology, Pharmacology, Citation/Evidence, Patient/Context, Agent-State, Audit/Observability.
- **CONFIRMED —** DAT topology: one Root/Router; children in parallel; **parent↔child only**; structured returns; synthesis after retrieval; verification before generation.
- **CONFIRMED (corrected, C-1) —** DAT children are: Clinical Reasoning, Literature/PMC Retrieval, Ontology/Concept (expansion), Pharmacology, Specialist(s), and **Provenance Capture**. **Citation Verification is a post-synthesis gate, not a child.**
- **PROPOSED —** Gap-closing components: Scope Guardrail, Clarification Gate, Uncertainty Aggregation, degradation policy, edit-provenance writer, retention lifecycle hook.
- **PROPOSED —** All API endpoints (`/clinical/query`, `/agents/route`, `/synthesis`, `/citations/verify`, `/soap/generate`, `/ontology/map`, `/retrieval/search`).
- **TBD —** Foundation LLM, Embedding, Re-ranker models; Vector DB; KG engine; Pharmacology DB + source; orchestration runtime; cloud; auth mechanism; DAT routing mechanism; all thresholds/policy values.
- **FUTURE —** PMS/EHR export; image interpretation; retention/residency specifics; specialists beyond the V1 set.

### 12.3 Canonical clinical query path (agreed, corrected)
**CONFIRMED —**
Veterinarian → Input → Patient/Species Context (read) → Query Understanding **+ Scope Guardrail** → Species Detection **+ Clarification Gate** → Clinical Concept Mapping (initial term→code) → Query Decomposition → **DAT Root/Router** → *(parallel)* Specialist/Retrieval children + Provenance Capture → Knowledge Retrieval → **Evidence Ranking** (local re-rank in Literature; cross-source in Synthesis) → Specialist Analysis → **Parent-Level Synthesis + Uncertainty Aggregation** → **Citation Verification (deterministic gate)** → **Safety/Grounding (fail closed)** → **LLM generation over verified context only** → Final Cited Response `{answer, citations[], confidence, flags[]}` → *(optional)* SOAP Generation → review → save → *(FUTURE)* export.

### 12.4 Response contract (agreed, corrected C-2)
- **CONFIRMED (shape) —** Success: `{answer, citations[], confidence, flags[], soap?}`. Alternates: `{needs_clarification, options[]}`, `{out_of_scope, reason}`.
- **TBD —** exact field types and value ranges.

### 12.5 Safety & trust baseline
- **CONFIRMED —** Verify-before-generate; deterministic and reproducible verification; unverified claims never presented as fact; species/drug safety (no dose without confirmed species; "no data" never substituted); human review before any record is saved; full auditability.
- **CONFIRMED (corrected C-6) —** Verification/safety components **fail closed**: if unavailable, generation is blocked and a graceful error returned.

### 12.6 Failure behaviour baseline
- **CONFIRMED —** No relevant / weak / contradictory evidence → honest low/no-evidence response, conflicts shown, no fabrication.
- **CONFIRMED —** Unknown species → clarify. Retrieval/model/component failure → degrade honestly (partial + flags if quorum met; else graceful error). Verification finds nothing → no-evidence response.
- **CONFIRMED (corrected C-5) —** Specialist disagreement → treated as conflicting evidence, surfaced via `conflicts[]`.
- **DECISION REQUIRED — TBD (C-7) —** Ambiguous (non-species) question → clarify vs. low-confidence answer.

### 12.7 MVP baseline
- **CONFIRMED —** MVP = the full trust core + one specialist + basic reviewed SOAP + all 8 stores + audit + degradation policy + the PROPOSED gap-closing components that serve MVP requirements (Scope Guardrail, Clarification Gate, Uncertainty Aggregation, Provenance Capture, edit-provenance).
- **FUTURE —** extra specialists, PMS/EHR export, image interpretation, retention specifics.

### 12.8 Baseline readiness statement
- **This baseline is engineering-ready once corrections C-1, C-2, C-3 are applied to the source documents** and the decisions D-1..D-6 (plus the inherited PRD open questions) have owners. The product, architecture, and flows are otherwise internally consistent: one spine, one set of rules, one clinical query path, one failure philosophy.

---

## Consolidated issue register (quick reference)

| ID | Class | Title | Blocking? | Correction |
|---|---|---|---|---|
| V-1 | CONTRADICTION | Verification child vs. gate (PRD tree) | **Yes** | C-1 |
| V-2 | CONTRADICTION/MISSING | Response contract drift | **Yes** | C-2 |
| V-3 | UNCLEAR/TBD | DAT routing/selection undefined | **Yes** | C-3 |
| V-4 | DUPLICATE | Two sequence diagrams | No | C-4 |
| V-5 | MISSING | Specialist disagreement | No | C-5 |
| V-6 | UNCLEAR | Safety must fail closed | No | C-6 |
| V-7 | MISSING/TBD | Intent-ambiguity handling | No | C-7 |
| V-8 | UNCLEAR | Freshness not displayed | No | C-8 |
| M-1..M-6 | MISSING | Requirements implied but unwritten | No | C-2/C-9 |
| CON-1/2/3 | (resolved in ARCH) | Verification/ontology/re-rank ambiguities | — | already resolved (C-1 propagates to PRD) |
| GAP-1..7 | (resolved in ARCH) | Homeless requirements | — | validated `CORRECT`/`FUTURE` |

---

*This document reviews the three specifications together, does not modify them, identifies each inconsistency before proposing any change, and proposes corrections only where the existing product requirements and architecture already support them. It is the pre-engineering consistency gate; the Baseline (Section 12) becomes the source of truth once Sections 2 and 11 are actioned.*
