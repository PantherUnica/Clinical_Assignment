# Veterinary Clinical Intelligence Platform — Documentation

A decision-support platform for **credentialed veterinarians**. A vet asks a real clinical question
about a specific animal and receives a clear, **species-aware, fully cited** answer whose every claim
can be opened to its source — and can optionally turn it into a reviewed SOAP note. It is **not** a
general chatbot and **not** an autonomous veterinarian: it **retrieves and verifies real evidence
before writing**, and **the vet always decides**.

Built on: RAG grounding over PubMed Central, factual knowledge from 25–30 veterinary textbooks,
SNOMED CT / VeNom / LOINC ontologies, species-specific pharmacology, deterministic citation
verification, SOAP generation, and **DAT** (Directed-Acyclic-Tree) parent→child→parent agent
orchestration.

> All specification documents live in [`PRD_Documents/`](./PRD_Documents/); rendered diagrams are in
> [`output/`](./output/).

> **Source-of-Truth Rule.** [`MASTER_PRD.md`](./PRD_Documents/MASTER_PRD.md) is the Product Source of
> Truth. Every other document implements, deepens, tests, secures, or operates the requirements
> defined there. **No document may change product scope or introduce new product behaviour without an
> approved PRD change** (Master PRD §M).

---

## 📚 Document set (read in this order)

**Start with the Master PRD, then follow the product lifecycle.**

| # | Document | What it is |
|---|----------|------------|
| ⭐ | [`MASTER_PRD.md`](./PRD_Documents/MASTER_PRD.md) | **Product Source of Truth.** Consolidated, phase-wise PRD with the stable OBJ→PR→UR→CAP→AC requirement hierarchy, seven-phase evolution, end-to-end journey, clinical-AI behaviour, MVP/FUTURE boundary, governance, traceability map, and change management. |
| 1 | [`PRD.md`](./PRD_Documents/PRD.md) | Product Foundation & Requirements — 28 sections (personas, use cases, FR/NFR/AI/SAF/DP/UX requirements with acceptance criteria, roadmap, open decisions). Foundational input, consolidated into the Master PRD. |
| 2 | [`ARCHITECTURE_SPEC.md`](./PRD_Documents/ARCHITECTURE_SPEC.md) | Clinical Intelligence System Architecture — requirements→component traceability, gaps/contradictions resolved, and 8 architecture views with per-component and per-connection detail. |
| 3 | [`PRODUCT_FLOW_SPEC.md`](./PRD_Documents/PRODUCT_FLOW_SPEC.md) | User & System Interaction — 12 product flows (User action → System action → Decision → Next step → Result) + a full non-collapsed "cat with suspected kidney disease" sequence. |
| 4 | [`VALIDATION_AND_BASELINE.md`](./PRD_Documents/VALIDATION_AND_BASELINE.md) | Consistency Validation + **Baseline Product Specification** — cross-review of docs 1–3, every issue classified, clinical chain + failure scenarios validated, recommended corrections, and the reconciled baseline. |
| 5 | [`ENGINEERING_SPEC.md`](./PRD_Documents/ENGINEERING_SPEC.md) | Engineering & Technical Specification — 20 sections: components (with owners), DAT execution model, API surface (PROPOSED), data architecture, RAG engineering, model roles (TBD), NFRs, failure/recovery, traceability, decision register, MVP boundary. |
| 6 | [`AI_ML_VALIDATION_SPEC.md`](./PRD_Documents/AI_ML_VALIDATION_SPEC.md) | AI/ML & Clinical Validation — evaluation framework (E-series), expert clinical validation, 10-scenario safety framework (S-series), datasets/versioning, lifecycle gates, monitoring, and validation matrices. |
| 7 | [`SECURITY_SAFETY_SPEC.md`](./PRD_Documents/SECURITY_SAFETY_SPEC.md) | Security, Privacy & Clinical Safety — data classification, security/privacy model, AI clinical-safety architecture, defence-in-depth pipeline controls, incident/rollback process, risk register, production-readiness. |
| 8 | [`BACKLOG_EXECUTION_PLAN.md`](./PRD_Documents/BACKLOG_EXECUTION_PLAN.md) | MVP Product Backlog & Execution Plan — 15 workstream epics (Epics→Features→stories→tasks, all traced), critical path, dependency-ordered sequence, DoR/DoD (stricter for clinical/AI), gate criteria. |
| 9 | [`TESTING_QA_STRATEGY.md`](./PRD_Documents/TESTING_QA_STRATEGY.md) | Testing & QA Strategy — testing levels + environments, clinical test-case categories, defect/regression, Requirement→Test→…→Release traceability, QA/Clinical/AI-ML matrices, security coverage, release gates. |
| 10 | [`PRODUCTION_OPS_PLAN.md`](./PRD_Documents/PRODUCTION_OPS_PLAN.md) | Production, Monitoring & Continuous Improvement — production lifecycle, three monitoring layers, incident management (incl. AI-clinical-safety handling), change management, feedback loop, governance, evolution. |

### Reference material (diagrams)
| Document | What it is |
|----------|------------|
| [`ARCHITECTURE.md`](./PRD_Documents/ARCHITECTURE.md) | The 5 Mermaid diagrams (High-Level, Low-Level + connection register, E2E flow, sequence, user flow). Updated for correction C-1 (verification is a post-synthesis gate; the DAT child is Provenance Capture). |
| [`DIAGRAMS_EXPLAINED.md`](./PRD_Documents/DIAGRAMS_EXPLAINED.md) | Plain-English walkthrough of the high-level and low-level diagrams. |
| [`output/out.md`](./output/out.md) + `output/out-*.svg` | Rendered SVG exports of the diagrams. |

---

## 🧭 Reading paths by role

- **New to the project / Leadership:** Master PRD → PRD (§1) → skim the diagrams.
- **Product Manager:** Master PRD → Validation & Baseline (4) → Backlog (8).
- **Engineer / Architect:** Master PRD → Architecture Spec (2) → Engineering Spec (5) → Backlog (8).
- **AI/ML Engineer:** Master PRD → Architecture Spec (2) → AI/ML & Clinical Validation (6).
- **Clinical Lead:** Master PRD → Product Flow (3) → AI/ML & Clinical Validation (6) → Security & Safety (7).
- **QA Lead:** Master PRD → Testing & QA (9) → Engineering Spec (5) §17.
- **Security / Compliance:** Master PRD → Security & Safety (7) → Production & Ops (10).
- **DevOps / SRE:** Master PRD → Engineering Spec (5) §14 → Production & Ops (10).

---

## 🎯 Design rules honored across all documents

- **DAT, not a mesh.** One Root/Router parent; children run in parallel; **only** parent↔child communication; each child returns structured `{evidence, source_ids, confidence, metadata}`; synthesis runs **after** retrieval.
- **Verify before generate.** Deterministic citation verification is a **post-synthesis gate** (not a DAT child); the safety/verification layer **fails closed** — it blocks generation rather than passing an unverified answer.
- **LLM is not the knowledge source.** It generates over retrieved, citation-verified, safety-grounded context only.
- **Species is a safety property.** Carried end-to-end; no drug dose without a confirmed species; a missing species entry returns "no data," never a substitute.
- **The vet decides.** The product supports judgment and never saves a clinical record without human review.
- **No invented specifics.** Undefined endpoints/models/technologies are marked `PROPOSED` / `MODEL TBD` / `TECHNOLOGY TBD`; deferred work is marked `FUTURE`.
- **Data stores shown separately** — Textbook KG, PMC Vector Index, Ontology Store, Pharmacology DB, Citation/Evidence Store, Patient/Context Store, Agent State/Execution Store, Audit/Observability Store.

---

## ⚠️ Known open items

- **Applied corrections:** C-1 (verification is a post-synthesis gate + Provenance Capture child), C-2 (response contract `{answer, citations[], confidence, flags[]}`), and C-3 (DAT routing contract) are applied to the source docs. **C-5..C-9 remain open** (tracked in [`VALIDATION_AND_BASELINE.md`](./PRD_Documents/VALIDATION_AND_BASELINE.md) §11).
- **Reference diagrams:** [`ARCHITECTURE.md`](./PRD_Documents/ARCHITECTURE.md), [`output/out.md`](./output/out.md), and the `output/out-*.svg` files have been regenerated for correction C-1 (verification shown as a post-synthesis gate; Provenance Capture as the DAT child), so they now match the Master PRD.
- **Decisions pending:** all `DECISION REQUIRED — TBD` items (models, vector DB, orchestration runtime, cloud, auth mechanism, vet verification, regulatory scope, evaluation thresholds, clinical panel) are consolidated in Master PRD §J. They gate the work that depends on them.

---

## 🛠️ Regenerating the diagrams

Diagrams render inline on GitHub. To export images locally:

```bash
npx -y @mermaid-js/mermaid-cli -i PRD_Documents/ARCHITECTURE.md -o output/out.md
```
