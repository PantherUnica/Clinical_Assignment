# Veterinary Clinical Intelligence Platform — End‑to‑End Architecture

> **Source of truth:** the architecture specification for this platform (RAG grounding, SNOMED CT / VeNom / LOINC ontologies, species‑specific pharmacology, specialist avatars, deterministic citation, and **DAT** — hierarchical *Directed‑Acyclic‑Tree* parent→child orchestration, **not** a flat multi‑agent mesh and **not** a simple sequential RAG pipeline).
>
> **`PROPOSED — TBD` rule:** where the source does **not** define a production endpoint, model, framework, cloud provider, vector database or storage technology, it is labelled `PROPOSED` / `TBD` rather than invented. The LLM is **never** the knowledge source — it *generates over retrieved, verified context*.

This document contains **exactly 5 diagrams**:

| # | Diagram | Purpose |
|---|---------|---------|
| 1 | **High‑Level Architecture** | Layered system view: User → API → Orchestrator → DAT → Knowledge → Stores → Models → Safety → Output |
| 2 | **Low‑Level / Detailed Architecture** | Every connection labelled with protocol, payloads, sync/async, auth boundary, retrieval mechanism, model invocation, store accessed |
| 3 | **E2E System Flow** | Two distinct flows — (A) **Offline Knowledge Ingestion** (dashed) and (B) **Online Clinical Query** (solid) |
| 4 | **Sequential Diagram** | Chronological trace for *"likely causes and diagnostic approach for kidney disease in a cat"* |
| 5 | **Veterinarian User Flow** | The vet's real journey from login to SOAP export |

---

## Legend (applies to all diagrams)

![diagram](./out-1.svg)

**Line semantics:** `═══▶` **solid** = runtime / online query flow &nbsp;•&nbsp; `– – ▶` **dashed** = offline ingestion flow &nbsp;•&nbsp; dashed‑border boxes = **FUTURE / PROPOSED — TBD**.

---

## 1 · High‑Level Architecture

Left‑to‑right primary flow. Each visual group is a bounded layer. The **DAT** block expands fully in Diagram 2.

![diagram](./out-2.svg)

---

## 2 · Low‑Level / Detailed Architecture

**True DAT hierarchy** shown explicitly: `Root/Router → child specialist/retrieval agents → back to Root`. Communication is **only** parent↔child; there is **no** arbitrary agent‑to‑agent traffic. Every child returns **structured evidence + source IDs + confidence/metadata** to its parent. Synthesis runs **after** retrieval. All undefined endpoints/models/tech are `PROPOSED / TBD`.

![diagram](./out-3.svg)

### 2a · Connection register (every runtime edge, fully attributed)

| # | Source → Destination | Protocol / Interface | Request payload | Response payload | Sync / Async | Format | Auth boundary | Retrieval mech. | Model invoked | Store / index |
|---|----------------------|----------------------|-----------------|------------------|--------------|--------|---------------|-----------------|---------------|---------------|
| 1 | Vet client → API Gateway | `POST /api/v1/clinical/query` **[PROPOSED]** | `{vet_id, patient, species?, text, image_ref?}` | `{answer, citations[], soap?}` | sync | JSON/HTTPS | **External→Internal** (OIDC/JWT, RBAC, TLS) | — | — | — |
| 2 | Gateway → Query Understanding | gRPC/HTTP internal (mTLS) | `{query_id, text, image_ref, patient_ctx}` | `{intent, entities[]}` | sync | JSON/protobuf | internal | — | — | Patient/Context Store (read) |
| 3 | Query Understanding → Embedding Model | `embed_query()` **[PROPOSED]** | `{text}` | `{vector[float]}` | async | tensor/JSON | internal | — | **Embedding — MODEL TBD** | — |
| 4 | Concept Mapping → Ontology Store | `POST /api/v1/ontology/map` **[PROPOSED]** | `{terms[], species}` | `{snomed[], venom[], loinc[]}` | sync | JSON | internal | code lookup | — | Clinical Ontology Store |
| 5 | Query Decomposition → Root/Router | `POST /api/v1/agents/route` **[PROPOSED]** | `{subqueries[], concepts[], species, patient_ctx}` | `{run_id}` (children dispatched) | sync‑await | JSON | internal | — | — | Agent State/Execution Store (write) |
| 6 | Root → each child agent | task dispatch **[PROPOSED]** (queue/RPC) | `{subquery, concepts[], species}` | — (async task) | **async fan‑out** | JSON | internal | — | — | Agent State Store |
| 7 | Literature Agent → Vector Index | `POST /api/v1/retrieval/search` **[PROPOSED]** | `{query_vector, k, filters}` | `{passages[], doc_ids[], scores[]}` | sync | JSON | internal | **ANN top‑k** | (Embedding upstream) | **PMC Vector Index — TECH TBD** |
| 8 | Literature Agent → Re‑ranker | `rerank_evidence()` **[PROPOSED]** | `{query, passages[]}` | `{ranked[], scores[]}` | sync | JSON | internal | cross‑encode rerank | **Re‑ranker — MODEL TBD** | — |
| 9 | Clinical Reasoning / Specialist → Knowledge Graph | graph/factual query **[PROPOSED]** | `{concepts[], relations[]}` | `{facts[], node_ids[]}` | sync | JSON/Cypher‑like | internal | graph traversal / factual lookup | — | Textbook Knowledge Store / KG |
| 10 | Ontology Agent → Ontology Store | code lookup | `{term}` | `{code_ids[], concept_ids[]}` | sync | JSON | internal | code lookup | — | Clinical Ontology Store |
| 11 | Pharmacology Agent → Pharmacology DB | SQL/REST **[PROPOSED]** | `{drug, species}` | `{generic, dose_by_species, side_effects[], interactions[]}` | sync | JSON/SQL | internal | keyed lookup | — | Pharmacology Database |
| 12 | Each child → Root (return) | structured return | — | `{evidence[], source_ids[], confidence, metadata}` | async→collected | JSON | internal | — | — | Agent State Store (write) |
| 13 | Root → Synthesis Service | `POST /api/v1/synthesis` **[PROPOSED]** | `{ranked_evidence[], findings[], source_ids[]}` | `{candidate_answer, claim_source_map}` | sync | JSON | internal | — | — | — |
| 14 | Synthesis → Citation Verification | `POST /api/v1/citations/verify` **[PROPOSED]** | `{claims[], claim_source_map}` | `{verified[], unverified[], citations[]}` | sync | JSON | internal | **deterministic span↔claim match** | — | Citation / Evidence Store (read) |
| 15 | Citation Verification → Safety/Grounding | internal call | `{verified_claims[], citations[]}` | `{grounded_context, rejects[]}` | sync | JSON | internal | grounding filter | — | — |
| 16 | Safety/Grounding → Foundation LLM | `invoke_llm()` **[PROPOSED]** | `{grounded_context, approved_citations[], prompt}` | `{draft_answer}` | sync | JSON | internal | — | **Foundation LLM — MODEL TBD** (generates over context only) | — |
| 17 | LLM → Final Answer → Gateway | internal → `POST /api/v1/clinical/query` resp | `{answer, citations[]}` | `{answer, citations[]}` | sync | JSON | Internal→External | — | — | — |
| 18 | Final Answer → SOAP Generator | `POST /api/v1/soap/generate` **[PROPOSED]** / `generate_soap()` | `{answer, patient_ctx, citations[]}` | `{soap:{S,O,A,P}, citations[]}` | sync (optional) | JSON | internal | — | (LLM optional) | — |
| X‑1 | Root ↔ Agent State/Execution Store | read/write DAT run graph | `{run_id, node, status}` | `{state}` | async | JSON | internal | — | — | Agent State/Execution Store |
| X‑2 | Retrieval agents → Citation/Evidence Store | write spans/DOIs | `{source_id, span, doc_id, uri}` | ack | async | JSON | internal | — | — | Citation / Evidence Store |
| X‑3 | Gateway / Root → Audit/Observability Store | emit traces & logs | `{trace_id, spans[], event}` | ack | async | JSON/OTLP | internal | — | — | Audit / Observability Store |

---

## 3 · E2E System Flow — two distinct flows

**Flow A (dashed)** = OFFLINE knowledge ingestion. **Flow B (solid)** = ONLINE clinical query. They meet only at the shared **Data Stores / Indexes**.

![diagram](./out-4.svg)

---

## 4 · Sequential Diagram

**Example query:** *"What are the likely causes and recommended diagnostic approach for kidney disease in a cat?"*
Every message shows the actual interface/action; `[PROPOSED]` marks undefined implementations. Species = **feline**; concept = **chronic kidney disease (CKD) / renal disease**.

![diagram](./out-5.svg)

---

## 5 · Veterinarian User Flow

The vet's real journey, from credential verification to (future) PMS/EHR export. Decision points and the deterministic citation review are shown explicitly.

![diagram](./out-6.svg)

---

## Appendix A — `PROPOSED — TBD` register

Everything below is **not** defined in the source and is therefore explicitly marked, never invented.

| Category | Item | Status |
|----------|------|--------|
| Endpoint | `POST /api/v1/clinical/query` | **PROPOSED** |
| Endpoint | `POST /api/v1/retrieval/search` | **PROPOSED** |
| Endpoint | `POST /api/v1/agents/route` | **PROPOSED** |
| Endpoint | `POST /api/v1/synthesis` | **PROPOSED** |
| Endpoint | `POST /api/v1/citations/verify` | **PROPOSED** |
| Endpoint | `POST /api/v1/soap/generate` | **PROPOSED** |
| Endpoint | `POST /api/v1/ontology/map` | **PROPOSED** |
| Model | Foundation LLM | **MODEL TBD** (generator over verified context, **not** knowledge source) |
| Model | Embedding model | **MODEL TBD** |
| Model | Re‑ranker model | **MODEL TBD** |
| Technology | Vector database (PMC index) | **TECHNOLOGY TBD** |
| Technology | Knowledge Graph / textbook store engine | **TECHNOLOGY TBD** |
| Technology | Pharmacology DB engine | **TECHNOLOGY TBD** |
| Technology | Agent framework / orchestration runtime | **TECHNOLOGY TBD** |
| Technology | Cloud provider / deployment target | **TBD** |
| Data source | Veterinary clinical / PMS / EHR integration | **FUTURE** |

## Appendix B — Data store catalog (shown separately, per requirement)

| Store | Contents | Written by (offline) | Read by (online) |
|-------|----------|----------------------|------------------|
| **Textbook Knowledge Store / Knowledge Graph** | Extracted facts, concepts & relationships from 25–30 textbooks | Textbook pipeline | Clinical Reasoning & Specialist agents |
| **PMC Vector Index** *(Vector DB — TECH TBD)* | Embedded PMC research chunks + doc IDs | PMC pipeline (chunk → embed) | Literature/PMC Retrieval Agent (`retrieve_top_k`) |
| **Clinical Ontology Store** | SNOMED CT, VeNom, LOINC codes & mappings | Ontology load | Concept Mapping + Ontology/Concept Agent |
| **Pharmacology Database** | Generic drugs, species‑specific dosing, side effects, interactions | Pharmacology load | Pharmacology Agent |
| **Citation / Evidence Store** | `source_id ↔ span / DOI / passage` provenance | PMC pipeline | Citation Verification Agent (deterministic) |
| **Patient / Clinical Context Store** | Case/patient/species context | Session service / (FUTURE PMS) | Orchestrator (patient ctx) |
| **Agent State / Execution Store** | DAT run graph, task status, per‑node results | — | Root/Router + all agents (state) |
| **Audit / Observability Store** | Traces, logs, metrics, access logs | — | Gateway + orchestrator (write) |

## Appendix C — DAT communication contract

- **Topology:** a true **Directed Acyclic Tree** — one **Root/Router** parent; children are leaves/sub‑trees. **No arbitrary agent‑to‑agent edges.**
- **Parent → child:** Root dispatches a scoped sub‑query (`{subquery, concepts[], species}`) to each child **in parallel (async)**.
- **Child → parent:** each child returns a **structured** result: `{evidence[], source_ids[], confidence, metadata}`. Children never talk to each other.
- **Synthesis after retrieval:** specialist synthesis then parent synthesis run **only after** all children return; ranking/re‑ranking precedes synthesis.
- **Verification before generation:** citation mapping + deterministic verification and safety/grounding checks gate the LLM. The **LLM generates over verified context only** and is not treated as a knowledge source.
