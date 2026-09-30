# Veterinary Clinical Intelligence Platform — Engineering & Technical Specification

**Document status:** Draft v1.0 · Engineering-ready
**Date:** 2026-09-27
**Owner:** Engineering (with AI/ML, Backend, Frontend, Data, QA, Security)
**Primary source of truth:** the **Baseline Product Specification** in [`VALIDATION_AND_BASELINE.md`](./VALIDATION_AND_BASELINE.md) §12.
**Upstream references:** [`PRD.md`](./PRD.md), [`ARCHITECTURE_SPEC.md`](./ARCHITECTURE_SPEC.md), [`PRODUCT_FLOW_SPEC.md`](./PRODUCT_FLOW_SPEC.md).

**What this document is.** It translates the approved baseline into exactly what each engineering team needs to build. It does **not** redesign the product, add features, or invent technologies. Anything not yet chosen is written as **`TBD`** (undecided), **`PROPOSED`** (specific but unratified — mainly API paths), or **`FUTURE`** (deferred past MVP). Where the baseline fixed a decision, it is **CONFIRMED** here.

**Plain-English promise.** Technical terms are explained the first time they appear. The reader does not need to be an engineer to follow the *what* and *why*; the *how* is precise enough for engineers to start breaking work into epics, APIs, database designs, and tests.

**Two rules that override everything below** (from the baseline): (1) **retrieve and verify before writing** — the language model only ever writes over evidence that has been retrieved and verified; (2) **the vet decides** — the system supports, never replaces, the veterinarian, and never saves a clinical record without human review.

---

## 1 · System Scope

**What the MVP must deliver:** a secure web/app tool where a credentialed veterinarian asks a clinical question about a specific animal and receives a clear, **species-aware, fully cited** answer whose every claim can be opened to its source, and can optionally turn that answer into a reviewed SOAP note that is saved to the case.

**In scope for MVP (MUST build):**
- Authenticated access for verified veterinary users.
- Capture and reuse of patient + species + clinical context within a case.
- Understanding the question, detecting species, mapping to standard codes (SNOMED CT / VeNom / LOINC), and breaking it into sub-questions.
- **DAT orchestration** (one Root/Router coordinating parallel child agents; parent↔child only).
- Retrieval from four knowledge families: veterinary textbooks (factual), PubMed Central (research, via RAG), clinical ontologies, and pharmacology (species-specific).
- Evidence ranking, synthesis, **deterministic citation verification (a post-synthesis gate)**, safety/grounding checks, and grounded answer generation.
- Uncertainty/low-evidence handling; out-of-scope handling; species clarification.
- Basic SOAP generation with human review/edit/save and AI-vs-vet edit provenance.
- Full audit logging and core monitoring.
- One specialist agent (proposed: Internal Medicine).

**Out of scope for MVP (see §20 and §15):** PMS/EHR integration, image *interpretation* (images are attached but not analysed), additional specialist agents, and concrete data-retention/residency rules beyond a policy hook.

**Explicitly not building:** an autonomous decision-maker, a general chatbot, or anything that answers from the model's memory instead of retrieved evidence.

---

## 2 · System Components

Each component below lists Responsibility · Inputs · Outputs · Dependencies · Data handled · Failure behaviour · Owner. "Owner" is the team accountable for building it. Endpoints in `code` are `PROPOSED`; technologies are `TBD` per the baseline.

**2.1 Web/App Interface**
- **Responsibility:** let the vet log in, enter context, ask questions, read cited answers (with openable sources and visible confidence/flags), review/edit/save SOAP notes.
- **Inputs:** vet actions; server responses.
- **Outputs:** query requests; SOAP save requests.
- **Dependencies:** API Gateway.
- **Data handled:** question text, patient/species context, attached image reference (not interpreted in MVP), displayed answers/citations.
- **Failure behaviour:** show clear progress states; on server error show a plain message and preserve entered data; never fabricate an answer client-side.
- **Owner:** Frontend.

**2.2 Authentication & Veterinarian Verification**
- **Responsibility:** confirm identity and that the user is an authorised veterinary professional; issue a session; enforce role.
- **Inputs:** credentials/token.
- **Outputs:** authenticated session + role; allow/deny.
- **Dependencies:** identity mechanism (`TBD`).
- **Data handled:** account identity, role, session token.
- **Failure behaviour:** deny by default; 401/403 on failure; never allow clinical calls without a valid session.
- **Owner:** Security / Backend.

**2.3 API Gateway**
- **Responsibility:** single secured entry point; authenticate/authorise; rate-limit; encrypt transport; route to internal services; emit audit.
- **Inputs:** HTTPS requests (`POST /api/v1/clinical/query`, `/soap/generate` — `PROPOSED`).
- **Outputs:** internal requests; final responses.
- **Dependencies:** Auth, Clinical Query Service, Audit.
- **Data handled:** all request/response payloads (in transit).
- **Failure behaviour:** 401/403/429 as appropriate; no request reaches internal services unauthenticated.
- **Owner:** Backend / Security.

**2.4 Clinical Query Service**
- **Responsibility:** orchestrate one clinical query end-to-end: call understanding → context → mapping → decomposition → DAT → synthesis → verification → safety → generation; assemble the response.
- **Inputs:** `{query_id, text, patient_ctx, image_ref?}`.
- **Outputs:** `{answer, citations[], confidence, flags[]}` or `{needs_clarification, options[]}` or `{out_of_scope, reason}`.
- **Dependencies:** all orchestrator + DAT + safety components.
- **Data handled:** the full query working set (transient).
- **Failure behaviour:** on any downstream failure, degrade honestly (partial + flags) or return a graceful error; never fabricate.
- **Owner:** Backend.

**2.5 Patient Context Service**
- **Responsibility:** create/load a case; store and retrieve patient + species + clinical context; retain across follow-ups.
- **Inputs:** patient/species/signs/labs; image reference.
- **Outputs:** `{patient_ctx}`.
- **Dependencies:** Patient/Context Store.
- **Data handled:** patient identity, species, signs, lab values, attached image reference (PHI-equivalent; access-controlled).
- **Failure behaviour:** if context unavailable, prompt the vet rather than proceed blind; never lose entered data.
- **Owner:** Backend / Data.

**2.6 Query Understanding (+ Scope Guardrail)**
- **Responsibility:** extract intent and clinical entities; reject out-of-scope/non-clinical requests before any retrieval.
- **Inputs:** `{query_id, text, patient_ctx}`.
- **Outputs:** `{intent, entities[]}` or `{out_of_scope, reason}`.
- **Dependencies:** understanding model (`MODEL — TBD`); scope classifier (`MODEL — TBD`).
- **Data handled:** question text.
- **Failure behaviour:** if uncertain about scope, prefer to proceed as clinical but flag; never answer an out-of-scope request as if clinical.
- **Owner:** AI/ML.

**2.7 Species Detection (+ Clarification Gate)**
- **Responsibility:** determine species with a confidence value; if confidence is below the threshold, ask the vet before proceeding.
- **Inputs:** intent + entities + context.
- **Outputs:** `{species, confidence}` or `{needs_clarification, options[]}`.
- **Dependencies:** species detector (`MODEL — TBD`); threshold (`TBD`).
- **Data handled:** species signals from text/context.
- **Failure behaviour:** low confidence → clarify (never silently guess); species is required before any dosing.
- **Owner:** AI/ML.

**2.8 Clinical Concept Mapping**
- **Responsibility:** map everyday clinical terms to standard codes (SNOMED CT, VeNom, LOINC) so terminology is consistent and drives retrieval routing.
- **Inputs:** `{terms[], species}`.
- **Outputs:** `{snomed[], venom[], loinc[]}`; unmapped terms flagged.
- **Dependencies:** Ontology Store; `POST /api/v1/ontology/map` (`PROPOSED`); concept model (`MODEL — TBD`).
- **Data handled:** clinical terms and codes.
- **Failure behaviour:** unmapped terms are flagged, never dropped.
- **Owner:** AI/ML / Data.

**2.9 DAT Orchestrator (Root/Router)**
- **Responsibility:** receive decomposed sub-questions; **select** which child agents to run (routing); dispatch them in parallel; collect structured results; enforce timeout/quorum; trigger synthesis. Communication is parent↔child only.
- **Inputs:** `{subqueries[], concepts[], species, patient_ctx}`.
- **Outputs:** collected evidence set → synthesis.
- **Dependencies:** all child agents; Agent-State Store; routing contract (§4; mechanism `TBD`).
- **Data handled:** run graph, per-node status/results (transient + audited).
- **Failure behaviour:** if children time out, proceed with a flagged partial answer if quorum met, else graceful error (`T`, `Q` = `TBD`).
- **Owner:** Backend / AI/ML.

**2.10 Specialist Agents**
- **Responsibility:** domain analysis (MVP: Internal Medicine) over textbook facts, conditioned on species.
- **Inputs:** `{subquery, concepts[], species}`.
- **Outputs:** `{specialist_findings[], source_ids[], confidence}`.
- **Dependencies:** Textbook KG; specialist reasoning model (`MODEL — TBD`).
- **Data handled:** domain facts + provenance.
- **Failure behaviour:** if unavailable, skip and flag that domain; disagreement with other findings is surfaced as conflicting evidence (not silently reconciled).
- **Owner:** AI/ML.

**2.11 Retrieval Services** (Literature/PMC; Clinical Reasoning; Ontology/Concept expansion)
- **Responsibility:** fetch real evidence: Literature embeds the sub-question, does top-k search on the PMC index, and re-ranks locally; Clinical Reasoning queries the Textbook KG; Ontology expands concepts.
- **Inputs:** scoped subquery + concepts + species.
- **Outputs:** `{passages[]/facts[], source_ids[], scores[], confidence}`.
- **Dependencies:** Vector Index, Textbook KG, Ontology Store; Embedding + Re-ranker models (`MODEL — TBD`); `POST /api/v1/retrieval/search` (`PROPOSED`).
- **Data handled:** evidence passages/facts + provenance.
- **Failure behaviour:** return fewer/none + low confidence + flag; never fabricate to fill a gap.
- **Owner:** AI/ML / Backend.

**2.12 Knowledge Stores** (Textbook KG, PMC Vector Index, Ontology Store, Pharmacology DB, Citation/Evidence Store)
- **Responsibility:** hold ingested knowledge and provenance for fast, read-only online retrieval; written only by offline ingestion.
- **Inputs (offline):** ingested corpora. **Inputs (online):** read queries.
- **Outputs:** facts, passages, codes, drug records, source spans.
- **Dependencies:** ingestion pipelines; store engines (`TBD`).
- **Data handled:** non-patient knowledge + citation provenance.
- **Failure behaviour:** on read failure the calling agent degrades + flags.
- **Owner:** Data / AI/ML.

**2.13 Pharmacology Service**
- **Responsibility:** return drug info keyed by drug **and species**: dosing, side effects, interactions; feed drug/species safety checks.
- **Inputs:** `{drug, species}`.
- **Outputs:** `{dose_by_species, side_effects[], interactions[], source_ids[]}` or `{no_data}`.
- **Dependencies:** Pharmacology DB (`TBD`).
- **Data handled:** drug/species/dose data + provenance.
- **Failure behaviour:** missing species entry returns `{no_data}` — **never** a cross-species or substituted dose.
- **Owner:** Data / AI/ML.

**2.14 Evidence Ranking**
- **Responsibility:** order evidence by relevance — local re-rank inside Literature; cross-source ranking inside Synthesis.
- **Inputs:** retrieved passages/findings.
- **Outputs:** ranked evidence.
- **Dependencies:** Re-ranker model (`MODEL — TBD`).
- **Data handled:** evidence + scores.
- **Failure behaviour:** fall back to retrieval scores; flag reduced ranking quality.
- **Owner:** AI/ML.

**2.15 Synthesis (+ Uncertainty Aggregation)**
- **Responsibility:** after the DAT barrier, combine ranked evidence into a candidate answer + a claim→source map; compute answer-level confidence and conflict flags.
- **Inputs:** all collected evidence/findings.
- **Outputs:** `{candidate_answer, claim_source_map, confidence, conflicts[]}`.
- **Dependencies:** `POST /api/v1/synthesis` (`PROPOSED`); optional re-ranker.
- **Data handled:** candidate claims + provenance.
- **Failure behaviour:** partial synthesis is flagged; conflicting evidence is surfaced, not reconciled.
- **Owner:** AI/ML.

**2.16 LLM Layer (Foundation LLM)**
- **Responsibility:** write the final answer using **only** verified, approved evidence and citations; add no facts of its own.
- **Inputs:** `{grounded_context, approved_citations[], prompt}`.
- **Outputs:** `{draft_answer, confidence, flags[]}`.
- **Dependencies:** Foundation LLM (`MODEL — TBD`); `invoke_llm()` (`PROPOSED`).
- **Data handled:** grounded context + citations.
- **Failure behaviour:** on model failure, retry then graceful error; never emit an ungrounded answer.
- **Owner:** AI/ML.

**2.17 Citation Service** (Provenance Capture + Citation Verification gate)
- **Responsibility:** **Provenance Capture** (a DAT child) records `source_id ↔ span/DOI/passage` at retrieval time; **Citation Verification** (a post-synthesis gate) deterministically checks each claim against its cited source and drops/flags unverified claims.
- **Inputs:** retrieved evidence (capture); `{claims[], claim_source_map}` (verify).
- **Outputs:** provenance rows; `{verified[], unverified[], citations[]}`.
- **Dependencies:** Citation/Evidence Store; `POST /api/v1/citations/verify` (`PROPOSED`).
- **Data handled:** claim↔source provenance.
- **Failure behaviour:** **fail closed** — if verification is unavailable, block generation and return a graceful error; unverified claims never presented as fact.
- **Owner:** Backend / AI/ML.

**2.18 Safety / Guardrail Layer**
- **Responsibility:** drop ungrounded claims; enforce species/drug safety; enforce scope; surface uncertainty; block generation if unsafe/unverified.
- **Inputs:** verified claims + citations; species/drug context.
- **Outputs:** `{grounded_context, approved_citations[], rejects[]}` or block.
- **Dependencies:** Citation Service; safety rules.
- **Data handled:** claims, rejects, safety flags.
- **Failure behaviour:** **fail closed** — if the safety layer is unavailable, generation is blocked.
- **Owner:** Security / AI/ML.

**2.19 SOAP Generator**
- **Responsibility:** turn a verified, cited answer + context into an editable S/O/A/P note; preserve citations; never fabricate a section.
- **Inputs:** `{answer, patient_ctx, citations[]}`.
- **Outputs:** `{soap:{S,O,A,P}, citations[]}`.
- **Dependencies:** LLM (optional); `POST /api/v1/soap/generate` (`PROPOSED`).
- **Data handled:** answer, context, note content.
- **Failure behaviour:** if generation fails, vet writes manually; empty-evidence sections are flagged, not invented.
- **Owner:** AI/ML / Backend.

**2.20 Audit / Logging**
- **Responsibility:** record, per query, what was asked, retrieved, verified/rejected, shown, and (for SOAP) AI-vs-vet edit provenance.
- **Inputs:** events from every component.
- **Outputs:** durable audit records.
- **Dependencies:** Audit/Observability Store.
- **Data handled:** trace IDs, actions, verification outcomes, edit deltas.
- **Failure behaviour:** alert on logging failure; treat audit as required, not optional.
- **Owner:** Backend / Security.

**2.21 Monitoring**
- **Responsibility:** collect metrics/traces for latency, retrieval quality, agent execution, model usage, citation coverage, verification/safety failures, error rates, SOAP failures, user feedback (see §11).
- **Inputs:** telemetry from all services.
- **Outputs:** dashboards/alerts.
- **Dependencies:** observability stack (`TBD`).
- **Data handled:** operational telemetry (no PHI in metrics).
- **Failure behaviour:** degraded monitoring alerts on itself; never blocks the clinical path.
- **Owner:** Backend / SRE.

**2.22 External Integrations**
- **Responsibility:** none active in MVP. (FUTURE: PMS/EHR export adapter; image interpretation.)
- **Failure behaviour:** N/A in MVP.
- **Owner:** Backend (FUTURE).

---

## 3 · End-to-End System Flow

The complete runtime path, step by step. (Matches the baseline canonical path and the authoritative sequence in the flow spec.)

1. **Veterinarian → Application.** The vet enters patient/species/context and a question, and submits.
2. **Application → API Gateway.** The app sends `POST /api/v1/clinical/query` (`PROPOSED`). The gateway authenticates, authorises, rate-limits, and audits the access.
3. **Query Understanding (+ Scope Guardrail).** The service extracts intent and clinical entities. If the request is not clinical/in-scope, it returns `{out_of_scope, reason}` immediately — no retrieval runs.
4. **Patient/Species Context.** The Patient Context Service loads the case context. Species Detection computes species + confidence; if confidence is low, the system returns `{needs_clarification, options[]}` and waits for the vet — no retrieval yet.
5. **Concept Mapping.** Terms are mapped to SNOMED/VeNom/LOINC. These codes both standardise terminology and **drive routing** (which agents are relevant).
6. **Decomposition → DAT Root/Router.** The question is split into sub-questions (e.g. causes, diagnostics, staging, therapeutics). Root selects the relevant child agents and dispatches them in parallel.
7. **Retrieval + Specialist Analysis (parallel).** Each child fetches real evidence: Literature (embed → search → local re-rank on the PMC index), Clinical Reasoning and the Specialist (Textbook KG), Ontology (concept expansion), Pharmacology (species-keyed drug data). Provenance Capture writes source spans to the Citation/Evidence Store. Children report only to Root.
8. **Evidence Synthesis (+ Uncertainty).** After the barrier, Synthesis cross-ranks and combines everything into a candidate answer + claim→source map, and computes answer confidence + conflict flags.
9. **Citation Verification (gate).** Each claim is deterministically checked against its cited source. Unverified claims are dropped/flagged. If nothing survives, the system returns a no-evidence response.
10. **Safety Checks.** Ungrounded content is removed; species/drug safety is enforced. If the verification or safety component is unavailable, generation is **blocked** (fail closed).
11. **Clinical Response (generation).** The LLM writes the answer over verified context only, producing `{answer, citations[], confidence, flags[]}`. The gateway audits the result and returns it. The vet can open any citation to its exact source (and its date).
12. **Optional SOAP.** If requested, the SOAP Generator builds an editable S/O/A/P note from the verified answer; the vet reviews/edits; on save, the note is persisted and AI-vs-vet edit provenance is recorded. (Export = FUTURE.)

---

## 4 · DAT Engineering Design

**Execution model.** The DAT is a **tree with one parent (Root/Router)** and a set of **child agents**. Work travels **down** (Root → children) as scoped dispatches; results travel **up** (children → Root) as structured returns. There is **no child-to-child communication**. Root runs children **in parallel**, waits at a **barrier**, then hands everything to Synthesis. This ordering guarantees "synthesize after retrieval, verify before generate."

**Information down / results up:**
- **Down:** Root sends each child `{subquery, concepts[], species}`.
- **Up:** each child returns `{evidence[]/findings[], source_ids[], confidence, metadata}`.
- Root never lets a child call another child; cross-cutting needs (provenance, state) go through stores, not peer calls.

**Routing (child selection) — the contract (mechanism `TBD`, D-1).** Root selects children from `{mapped concepts, subquery labels}`. The **contract is CONFIRMED** (input = concepts + subquery labels; output = the set of agents to run); the **mechanism** (fixed rules vs. learned routing) is `TBD`.

**Node specification** (Purpose · Input · Output · Parent · Children · Data passed · Retrieval · Model · Failure):

| Node | Purpose | Input | Output | Parent | Children | Data passed | Retrieval | Model | Failure handling |
|---|---|---|---|---|---|---|---|---|---|
| **Root/Router** | select + dispatch + collect + barrier + trigger synthesis | subqueries, concepts, species | collected evidence | — | all below | down: subquery+concepts+species; up: structured returns | — | — | timeout/quorum → partial+flag or graceful error |
| Clinical Reasoning | differentials from established facts | subquery+species | evidence+source_ids+confidence | Root | — | facts + provenance | Textbook KG | reasoning model `TBD` | reduced coverage flagged |
| Literature/PMC | research retrieval + local re-rank | subquery | passages+doc_ids+scores+confidence | Root | — | passages + provenance | Vector Index | Embedding + Re-ranker `TBD` | fewer/none + flag |
| Ontology/Concept | concept expansion | concepts+species | expanded_codes+concept_ids | Root | — | codes | Ontology Store | — | base concepts only |
| Pharmacology | species-specific drug data | drug+species | dosing+interactions+source_ids | Root | — | drug data + provenance | Pharmacology DB | — | `{no_data}`, never substitute |
| Specialist (IM) | domain analysis | subquery+species | findings+source_ids+confidence | Root | — | domain facts + provenance | Textbook KG | specialist model `TBD` | skip+flag; disagreement → conflict |
| Provenance Capture | record source↔span | retrieved evidence | provenance rows | Root | — | source spans | Citation/Evidence Store (write) | — | retry+alert |

**Not a child (post-synthesis):** Synthesis, Citation Verification (gate), Safety/Grounding, LLM. These run **after** the tree returns, in order.

---

## 5 · API Specification

All paths are **`PROPOSED`** unless ratified (baseline D-8/OQ-8). Fields are indicative; exact types `TBD`. Auth = valid session at the Gateway unless noted.

**5.1 `POST /api/v1/clinical/query` — `PROPOSED`**
- **Purpose:** submit a clinical query; return a cited answer (or clarification / out-of-scope).
- **Auth:** required (vet session + role).
- **Request:** `{vet_id, patient, species?, text, image_ref?}`.
- **Response:** `{answer, citations[], confidence, flags[], soap?}` | `{needs_clarification, options[]}` | `{out_of_scope, reason}`.
- **Errors:** 401/403 (auth), 429 (rate limit), 503 (verification/safety unavailable → fail closed), 500 (unexpected).
- **Calling → Called:** App → Gateway → Clinical Query Service.

**5.2 `POST /api/v1/ontology/map` — `PROPOSED`**
- **Purpose:** map terms to SNOMED/VeNom/LOINC.
- **Request:** `{terms[], species}`. **Response:** `{snomed[], venom[], loinc[], unmapped[]}`.
- **Errors:** 400 (bad terms), 503 (store unavailable).
- **Calling → Called:** Concept Mapping → Ontology Store.

**5.3 `POST /api/v1/agents/route` — `PROPOSED`**
- **Purpose:** start a DAT run over sub-questions.
- **Request:** `{subqueries[], concepts[], species, patient_ctx}`. **Response:** `{run_id}` then collected evidence.
- **Errors:** 424 (no children could run), 504 (quorum not met).
- **Calling → Called:** Clinical Query Service → DAT Root.

**5.4 `POST /api/v1/retrieval/search` — `PROPOSED`**
- **Purpose:** top-k semantic search on the PMC index.
- **Request:** `{query_vector, k, filters}`. **Response:** `{passages[], doc_ids[], scores[]}`.
- **Errors:** 503 (index unavailable) → caller degrades + flags.
- **Calling → Called:** Literature Agent → Vector Index.

**5.5 `POST /api/v1/synthesis` — `PROPOSED`**
- **Purpose:** combine evidence into a candidate answer + claim→source map + uncertainty.
- **Request:** `{ranked_evidence[], findings[], source_ids[]}`. **Response:** `{candidate_answer, claim_source_map, confidence, conflicts[]}`.
- **Errors:** 422 (insufficient evidence) → low/no-evidence path.
- **Calling → Called:** DAT Root → Synthesis.

**5.6 `POST /api/v1/citations/verify` — `PROPOSED`**
- **Purpose:** deterministically verify claims against sources.
- **Request:** `{claims[], claim_source_map}`. **Response:** `{verified[], unverified[], citations[]}`.
- **Errors:** 503 (verification unavailable) → **fail closed** (block generation).
- **Calling → Called:** Clinical Query Service → Citation Verification.

**5.7 `POST /api/v1/soap/generate` — `PROPOSED`**
- **Purpose:** build a SOAP note from a verified answer.
- **Request:** `{answer, patient_ctx, citations[]}`. **Response:** `{soap:{S,O,A,P}, citations[]}`.
- **Errors:** 409 (no verified answer to base on).
- **Calling → Called:** App → Gateway → SOAP Generator.

**5.8 Session/SOAP save & context — `PROPOSED`**
- Endpoints for login/session, context read/write, and SOAP save are **`PROPOSED — TBD`**; save must record edit provenance.

**Internal model calls** (`embed_query()`, `invoke_llm()`, `rerank_evidence()`) are internal interfaces, `PROPOSED`, not public endpoints.

---

## 6 · Data Architecture

For each object: Purpose · Key fields · Relationships · Source · Storage · Retention. Storage engines are `TBD`; retention specifics are `FUTURE`/regulatory (D-10). PHI-equivalent = veterinary patient/client data treated with the same care as human PHI.

| Object | Purpose | Key fields (indicative) | Relationships | Source | Storage | Retention |
|---|---|---|---|---|---|---|
| **User/Account** | who the vet is + role | user_id, role, credential status | owns cases/queries | Auth | account store (`TBD`) | while active + audit window (`TBD`) |
| **Patient** | the animal | patient_id, species, breed?, age? | belongs to a client/case | vet input | Patient/Context Store | per policy (`FUTURE`) |
| **Clinical Encounter/Case** | a visit/thread | case_id, patient_id, vet_id, context | groups queries + SOAP | Session/Case Service | Patient/Context Store | per policy |
| **Clinical Concept** | standardised term | concept_id, snomed/venom/loinc codes | maps symptoms/diagnoses | Ontology load | Ontology Store | corpus-versioned |
| **Species Info** | species attributes | species_id, name | conditions reasoning/dosing | ontology/config | Ontology Store | corpus-versioned |
| **Symptom** | presenting sign | code, description | part of encounter/query | vet input + codes | Patient/Context + Ontology | per policy |
| **Diagnosis (differential)** | candidate condition | concept_id, confidence | output of reasoning | agents | transient + audit | audit window |
| **Laboratory Data** | measured results | loinc_code, value, unit | part of encounter | vet input | Patient/Context Store | per policy |
| **Imaging Finding** | attached image ref | image_ref (no interpretation MVP) | part of encounter | vet upload | Patient/Context Store | per policy |
| **Medication** | drug + species dosing | drug_id, species, dose, interactions, source_ids | used by pharmacology/safety | Pharmacology load | Pharmacology DB | corpus-versioned |
| **Evidence Document** | textbook/PMC content | doc_id, chunks, dates | cited by citations | ingestion | KG / Vector Index | corpus-versioned |
| **Citation** | claim↔source link | source_id, span/DOI, doc_id, date | links claim ↔ evidence | Provenance Capture | Citation/Evidence Store | with answer/audit |
| **Agent Output** | a child's result | run_id, node, evidence, confidence | feeds synthesis | DAT children | Agent-State (transient) + audit | audit window |
| **SOAP Note** | clinical record | note_id, case_id, S/O/A/P, citations, edit_provenance | belongs to case | SOAP Generator + vet | Patient/Context Store | per policy |
| **Audit Record** | what happened | trace_id, events, verify/reject counts, edit deltas | spans a query/case | all components | Audit/Observability Store | audit window (`TBD`) |

---

## 7 · Knowledge & RAG Engineering

Each source enters and is used **differently** — they are not one generic database.

**Textbooks (25–30) → structured clinical knowledge.** Offline: parse/OCR → clean → extract facts and relationships → **Textbook Knowledge Graph**. Online: Clinical Reasoning and the Specialist query it for *established facts*. Purpose: the factual backbone ("what is generally true").

**PubMed Central → RAG pipeline.** Offline: ingest → parse/clean → **chunk** (split into passages) → **embed** (turn each passage into a vector so it can be searched by meaning) → **index** (store vectors in the Vector Index) → also write `chunk → source_id + date` to the Citation/Evidence Store. Online: the Literature agent embeds the sub-question, does **top-k** search (the k best-matching passages), then **locally re-ranks** them. Purpose: current research, always dated and verifiable.

**SNOMED CT / VeNom / LOINC → mapping + routing.** Offline: normalise codes → **Ontology Store**. Online: Concept Mapping turns the vet's words into codes (the shared language); those codes and their relationships **drive retrieval routing** (which agents/sources are relevant) and let the Ontology agent expand concepts. Purpose: consistent terminology + routing, not "answers."

**Pharmacology → safety-critical lookup.** Offline: structure drugs, **species-specific dosing**, side effects, interactions → **Pharmacology DB**. Online: the Pharmacology agent looks up `{drug, species}`; results feed drug/species safety checks. Purpose: correct, species-aware drug info; a missing species entry returns "no data," never a substitute.

**How they interact:** the DAT keeps them separate lanes — textbooks for settled facts, PMC for current evidence, ontologies for language/routing, pharmacology for drugs. Synthesis combines their outputs *after* retrieval; provenance is preserved to the passage level so verification can be deterministic.

---

## 8 · Model Architecture

Where models are needed and what each does. All specific model choices are **`MODEL — TBD`** (baseline D-7/D-8; chosen against requirements, not popularity).

| Model role | Responsibility | MVP? | Status |
|---|---|---|---|
| Query understanding | extract intent/entities | Yes | `MODEL — TBD` |
| Concept/entity | help map terms → codes | Yes | `MODEL — TBD` (may be rules + model) |
| Embedding | turn text into vectors for meaning search | Yes | `MODEL — TBD` |
| Re-ranking | reorder retrieved passages by relevance | Yes | `MODEL — TBD` |
| Specialist reasoning | domain analysis (IM) | Yes (1 domain) | `MODEL — TBD` |
| Foundation LLM | write the answer over verified context only | Yes | `MODEL — TBD` |
| Citation/verification | **deterministic** claim↔source matching | Yes | rule-based/deterministic preferred; `TBD` |
| Vision | interpret images | **No (FUTURE)** | `MODEL — TBD` (FUTURE) |
| SOAP generation | structure a note (may reuse Foundation LLM) | Yes | `MODEL — TBD` |

**Note:** citation verification is **deterministic by requirement** (reproducible, not a model's judgment) — if a model assists, it cannot be the final arbiter.

---

## 9 · Clinical Safety Architecture

Concrete engineering behaviour for each risk (not "add guardrails"):

- **Unsupported claims:** the Safety layer drops any claim that did not pass verification; generation runs only over approved citations. *System does:* remove the claim; if it was central, flag the answer as reduced.
- **Missing evidence:** if a lane returns nothing, the answer omits that dimension and flags it; if nothing survives verification, return a no-evidence response ("not covered by our sources").
- **Conflicting evidence:** Uncertainty Aggregation records `conflicts[]`; the answer presents both positions with citations, never silently picks one.
- **Species mismatch:** no dose is shown without a confirmed species; Pharmacology returns `{no_data}` for an unknown species combination; the Safety layer blocks any cross-species dose.
- **Drug/dose uncertainty:** if dosing data is absent or conflicting, show "no reliable species-specific dosing found" — never an estimated dose.
- **Citation failure (verification unavailable):** **fail closed** — block generation, return 503-style graceful error; do not answer.
- **Model failure:** retry per policy; if still failing, graceful error; never emit an ungrounded answer.
- **Retrieval failure:** child returns empty + low confidence; Root proceeds with quorum + flags or errors gracefully.
- **Agent disagreement:** treated as conflicting evidence (above), surfaced via `conflicts[]`.
- **Low-confidence answers:** below the uncertainty threshold (`TBD`), the answer is visibly marked "limited evidence."
- **Human review:** SOAP/records cannot be saved without explicit vet review; edit provenance (AI vs vet) is recorded.

---

## 10 · Security & Privacy

- **Authentication:** all access via the Gateway with a valid session (`OIDC/JWT` `PROPOSED`; mechanism `TBD`).
- **Authorization:** role-based; clinical functions and patient context limited by role.
- **Veterinarian verification:** only credentialed veterinary users may use clinical functions (verification method `TBD`).
- **Patient/client data:** stored in a dedicated, access-controlled store; never sent to any external service in MVP; not placed in URLs/query strings.
- **Encryption:** in transit (TLS; `PROPOSED`) externally and on the internal channel (mTLS; `PROPOSED`); at rest per store policy (`TBD`).
- **Access control:** least privilege; store separation (knowledge vs patient vs agent-state vs audit).
- **Audit logs:** every query's inputs/retrieval/verification/output + SOAP edit provenance; protected and retained.
- **Data retention:** policy hook in MVP; concrete periods `FUTURE`/regulatory (D-10).
- **Data deletion:** supported per policy; deletion of patient data must cascade appropriately (`TBD` specifics).
- **Environment separation & production vs sandbox:** real patient data only in production; see §14.

---

## 11 · Observability

Must be monitored (targets in §12; PHI never in metrics):
- **API latency** (per endpoint, p50/p95/p99).
- **Retrieval quality** (offline relevance on a curated set; online proxies).
- **Agent execution** (success/timeout/duration per child).
- **Model latency** (per model role).
- **Citation coverage** (% of claims with a citation).
- **Citation verification failures** (unverified/rejected counts, verification errors).
- **Safety failures** (blocked generations, fail-closed events).
- **Error rates** (per service, by class).
- **Token/model usage** (per query, per model).
- **SOAP generation failures.**
- **User feedback** (usefulness rating, citation-open/confirm).
- **Clinical validation metrics** (citation faithfulness on clinician-reviewed samples — the launch gate).

---

## 12 · Non-Functional Requirements

Measurable; unknown targets marked `TBD — PERFORMANCE TARGET` etc.

- **Performance:** p95 end-to-end query latency `TBD — PERFORMANCE TARGET` (must account for parallel retrieval + verification). Measured at the Gateway.
- **Availability:** service uptime `TBD — AVAILABILITY TARGET`.
- **Scalability:** support `TBD` concurrent vets without loss of citation integrity; parallel DAT must not degrade verification.
- **Security:** auth on 100% of clinical calls; 0 unauthenticated internal access; encryption everywhere (§10).
- **Reliability:** graceful degradation on component failure; **0 fabricated answers** under failure.
- **Auditability:** 100% of queries reconstructable end-to-end.
- **Maintainability:** components pluggable behind interfaces so a model/store can be swapped without rewrites (baseline NFR-010).
- **Observability:** every run emits traces/metrics sufficient to debug and audit.
- **Data integrity:** provenance (`source_id ↔ span`) never lost through ingestion → retrieval → synthesis → verification → SOAP.

---

## 13 · Failure & Recovery Design

For each critical service: Normal → Failure → Detection → Fallback → User-visible → Logging → Recovery.

| Service | Normal | Failure | Detection | Fallback | User-visible | Logging | Recovery |
|---|---|---|---|---|---|---|---|
| Gateway/Auth | authenticate + route | auth outage | health check/errors | none (deny) | "sign in again" | auth error events | restore auth; sessions re-issued |
| Clinical Query Service | orchestrate query | orchestration error | timeouts/exceptions | partial/graceful error | "couldn't complete — retry" | trace with failing step | retry idempotently |
| DAT child (retrieval) | fetch evidence | source/index down | timeout/error | proceed w/ quorum + flag | "based on partial evidence" | per-node failure | source restored → normal |
| Synthesis | combine evidence | insufficient/err | 422/exception | low/no-evidence path | "limited/no evidence" | synthesis event | re-run on retry |
| Citation Verification | verify claims | verifier down | health/timeout | **fail closed** (block) | graceful error, no answer | fail-closed event | restore verifier |
| Safety layer | ground + safety | layer down | health/timeout | **fail closed** (block) | graceful error | safety-block event | restore layer |
| LLM | write answer | model down | error/timeout | retry → graceful error | "temporarily unable — retry" | model failure event | provider/model restored |
| Pharmacology | drug lookup | DB down / no data | error / `no_data` | "no reliable dosing found" | explicit no-dose note | lookup event | DB restored |
| SOAP Generator | build note | gen failure | error | vet writes manually | "draft unavailable — edit manually" | soap failure event | retry |
| Stores (patient/audit) | read/write | write failure | error | retry; preserve local | error; data not lost | store error event | restore; reconcile |

---

## 14 · Environment Architecture

Progression and what each allows:

- **Development:** engineers build/iterate. **No real patient data.** Synthetic/seed data only. Models/stores may be stubs.
- **Testing:** automated tests (unit/integration). **No real patient data.** Deterministic fixtures; verification testable.
- **Sandbox:** integrated demo/trial with **synthetic** patients and a controlled slice of the knowledge corpora. **No real patient data.** Safe to explore full flows including SOAP.
- **Staging:** production-like; pre-release validation and clinician review of citation faithfulness. **No real patient data** (or strictly de-identified, per policy `TBD`).
- **Production:** real, credentialed vets and real patient/client data. Full security, audit, retention. Only environment where real PHI-equivalent data exists.

**Rule:** real patient data never leaves production; lower environments use synthetic/seed data.

---

## 15 · Integrations

- **Current (MVP):** **none external.** The platform is self-contained: it reads only its own ingested knowledge stores and its own patient-context store. (Identity provider for auth is the only external dependency, mechanism `TBD`.)
- **Future:** **PMS/EHR export** (write saved SOAP notes to clinic systems) and **image interpretation** — both `FUTURE`, gated on regulatory scope (D-10) and validation (D-4/OQ-14). **These must not be treated as MVP dependencies.**

---

## 16 · Requirement Traceability

Product Requirement → System Requirement → Architecture Component → API/Service → Data → Test Case (test IDs are `PROPOSED` placeholders for QA).

| Product req | System requirement | Component | API/Service | Data | Test case |
|---|---|---|---|---|---|
| FR-001 Auth | only verified vets access clinical fns | Auth, Gateway | `/clinical/query` auth | User/Account | T-AUTH-01 |
| FR-002/003 Context | capture + retain patient/species | Patient Context Service | context read/write (`PROPOSED`) | Patient, Case | T-CTX-01/02 |
| FR-004 Species | detect + clarify on low confidence | Species Detection + Clarification Gate | `/clinical/query` | Species | T-SPE-01 |
| FR-005 Concept map | map to SNOMED/VeNom/LOINC | Concept Mapping | `/ontology/map` | Clinical Concept | T-ONT-01 |
| FR-006 Decompose | split into subqueries | Decomposition | internal | — | T-DEC-01 |
| FR-007 DAT | parallel, parent↔child only | DAT Root + children | `/agents/route` | Agent Output | T-DAT-01/02 |
| FR-008 RAG/PMC | retrieve + re-rank | Literature Agent | `/retrieval/search` | Evidence Doc | T-RET-01 |
| FR-009 Textbook | factual retrieval | Reasoning/Specialist | internal (KG) | Evidence Doc | T-KG-01 |
| FR-010 Pharmacology | species-specific; no substitute | Pharmacology Service | internal | Medication | T-PHA-01/02 |
| FR-011 Specialist | domain analysis (IM) | Specialist Agent | `/agents/route` | Agent Output | T-SPC-01 |
| FR-012 Synthesis | rank + combine + uncertainty | Synthesis | `/synthesis` | Agent Output | T-SYN-01 |
| FR-013 Verify | deterministic gate | Citation Verification | `/citations/verify` | Citation | T-CIT-01/02 |
| FR-014 Grounded gen | LLM over verified only | Safety + LLM | `invoke_llm()` | — | T-GEN-01 |
| FR-015 Cited answer | show + open citations + date | App + Output | `/clinical/query` resp | Citation | T-UI-01 |
| FR-016/017/018 SOAP | generate + review + save + provenance | SOAP Generator | `/soap/generate`, save | SOAP Note, Audit | T-SOAP-01/02 |
| FR-020 Uncertainty | low/no/conflicting evidence | Uncertainty Aggregation | `/synthesis`, resp `flags[]` | — | T-UNC-01 |
| FR-021 Out-of-scope | reject cleanly | Scope Guardrail | `/clinical/query` | — | T-SCO-01 |
| FR-022 Audit | reconstruct any query | Audit/Logging | all | Audit Record | T-AUD-01 |
| SAF-001..009 | safety behaviours (§9) | Safety layer | multiple | — | T-SAF-01..09 |
| DP-001..008 | security/privacy (§10) | Security | Gateway | Patient/User | T-SEC-01.. |

Every major requirement has a component, a service/API, data, and a test hook.

---

## 17 · Acceptance Criteria (Given / When / Then)

Selected, testable criteria per major capability (QA expands into full suites):

- **Auth:** *Given* an unauthenticated request, *When* it hits any clinical endpoint, *Then* it is rejected (401/403) and no query runs.
- **Species safety:** *Given* a dosing question with ambiguous species, *When* submitted, *Then* the system asks for species and shows no dose until confirmed.
- **No cross-species dose:** *Given* a drug with no feline data, *When* asked for a feline dose, *Then* the system returns "no species-specific data," never a substitute.
- **Grounded generation:** *Given* retrieved context is removed, *When* generation runs, *Then* no clinical claim is produced.
- **Deterministic verification:** *Given* identical inputs, *When* verification runs twice, *Then* the results are identical; unsupported claims are absent from the answer.
- **Fail closed:** *Given* the verification/safety component is unavailable, *When* a query runs, *Then* generation is blocked and a graceful error is returned (no answer).
- **DAT topology:** *Given* a multi-part query, *When* the DAT runs, *Then* children run in parallel and the execution graph shows only parent↔child edges.
- **Low/no evidence:** *Given* little/no retrievable evidence, *When* answered, *Then* the response is explicitly marked "limited/no evidence" and nothing is fabricated.
- **Conflict:** *Given* conflicting sources, *When* synthesised, *Then* both positions are shown with citations and a conflict flag.
- **Citations openable + dated:** *Given* a cited answer, *When* the vet opens a citation, *Then* the exact source passage and its date are shown.
- **SOAP review:** *Given* a generated SOAP note, *When* the vet has not reviewed it, *Then* it cannot be saved; on save, AI-vs-vet provenance is recorded.
- **Auditability:** *Given* any completed query, *When* a reviewer inspects it, *Then* inputs, retrieved sources, verification outcomes, and output can be reconstructed.

---

## 18 · Technical Decisions (register)

Decision · Why it matters · Options · Recommendation/Status · Dependencies · Owner · Status label.

| Decision | Why it matters | Options | Recommendation / status | Depends on | Owner | Status |
|---|---|---|---|---|---|---|
| Foundation LLM | writes every answer | (several; unranked) | choose against grounding/latency/cost eval | eval harness | AI/ML | `TBD` |
| Embedding + Re-ranker | retrieval quality | (several) | choose against retrieval eval | curated set | AI/ML | `TBD` |
| Vector DB | PMC index | (several) | choose against scale/latency | corpus size | Data | `TBD` |
| Textbook KG engine | factual store | (several) | choose against query needs | extraction design | Data | `TBD` |
| Pharmacology DB + source | drug data | (several) | choose against licensing/coverage | licences | Data | `TBD` |
| Orchestration runtime | runs the DAT | (several) | choose against routing needs | routing contract | Backend | `TBD` |
| Cloud provider | hosting | (several) | choose against security/residency | regulatory scope | Platform | `TBD` |
| API paths | client/API contract | as listed | ratify the `PROPOSED` set | — | Backend | `PROPOSED` |
| Auth mechanism | security | (several) | choose against verification needs | vet verification | Security | `TBD` |
| DAT routing mechanism | agent selection | rules vs learned | contract CONFIRMED; mechanism open | — | AI/ML | `TBD` (D-1) |
| Clarification/uncertainty/quorum thresholds | safety/UX | numeric | set from data/baselines | pilot data | AI/ML | `TBD` (D-2/3/5) |
| Intent-ambiguity handling | UX/safety | clarify vs low-conf answer | record decision | UX input | Product | `TBD` (D-4) |
| DAT verification placement | correctness | child vs gate | **gate** (post-synthesis) | — | AI/ML | **CONFIRMED** |
| Response contract | client build | as in §5.1 | superset w/ confidence+flags | — | Backend | **CONFIRMED** |
| Fail-closed safety | patient safety | closed vs open | **fail closed** | — | Security | **CONFIRMED** |
| V1 specialist set | scope | which domains | 1 domain (IM proposed) | — | Product | `TBD` (D-9/OQ-9) |
| PMS/EHR + image interp. | scope | — | deferred | regulatory | Product | `FUTURE` |

---

## 19 · Engineering Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Deterministic verification hard to achieve at needed fidelity | core trust fails | prototype early on a clinician-reviewed set; treat as launch gate; keep it deterministic/reproducible |
| Latency from parallel retrieval + verification too high | abandonment | parallelise DAT; cache embeddings; set/measure NFR-001; progress UI |
| Cross-species dosing leak | patient harm | species carried end-to-end; `{no_data}` contract; safety-layer block; targeted tests (T-PHA-02, T-SAF) |
| Undecided models/DB/cloud cause rework | delivery slip | interface isolation (NFR-010); decide via §18 before dependent builds |
| Routing mechanism undefined → divergent orchestrators | inconsistent behaviour, untestable | ratify routing contract now (D-1); pick mechanism before build |
| Knowledge gaps mistaken for answers | misleading confidence | bounded-knowledge honesty; low/no-evidence path; freshness display |
| Provenance lost in the pipeline | verification impossible | data-integrity requirement (NFR); provenance carried at every stage |
| Fail-open under partial outage | unsafe answers | fail-closed rule for verification/safety; chaos tests |
| Ingestion quality (OCR/extraction) poor | bad facts in KG | quarantine + validation in ingestion; version corpora |
| PHI handling gaps | compliance exposure | store separation; access control; audit; resolve retention/residency (D-10) |

---

## 20 · Final MVP Technical Boundary

**MUST BUILD (MVP core — the product is not viable without these):**
- Auth + veterinarian verification; API Gateway; Clinical Query Service.
- Patient Context Service + Patient/Context Store.
- Query Understanding + Scope Guardrail; Species Detection + Clarification Gate; Concept Mapping; Decomposition.
- DAT Root/Router + core children (Clinical Reasoning, Literature/PMC, Ontology/Concept, Pharmacology, Provenance Capture) + **one specialist (IM)**; routing contract.
- Retrieval services + all knowledge stores (Textbook KG, PMC Vector Index, Ontology, Pharmacology, Citation/Evidence).
- Synthesis + Uncertainty Aggregation; **Citation Verification gate**; Safety layer (**fail closed**); LLM generation.
- Response contract `{answer, citations[], confidence, flags[]}` + clarification/out-of-scope variants.
- Basic SOAP + review/edit/save + edit provenance.
- Audit/Logging; core Monitoring; offline ingestion for all four knowledge families.

**SHOULD BUILD (MVP if capacity allows; else fast-follow):**
- Richer uncertainty/conflict presentation; freshness display polish.
- Configurable degradation thresholds surfaced to ops.
- Broader monitoring dashboards and user-feedback capture.

**NOT IN MVP:**
- Additional specialists (Oncology/Dentistry/Anesthesia).
- Image interpretation (attach-only in MVP).
- Concrete data-retention/residency automation (policy hook only).

**FUTURE:**
- PMS/EHR export integration.
- Vision model / image findings.
- Multi-language; governance analytics; advanced conflict tooling.

---

## Readiness statement

This specification is ready for engineering to begin **architecture breakdown, API design, database design, development planning, and test authoring**, provided the three CONFIRMED baseline corrections are honoured (verification gate; response contract; fail-closed safety) and the `TBD` decisions in §18 are owned and scheduled before their dependent components are built. It introduces no product change, no new feature, and no invented technology — every open choice is marked `TBD`, `PROPOSED`, or `FUTURE`, consistent with the approved Baseline Product Specification.
