# Veterinary Clinical Intelligence Platform — Architecture

Technically accurate, implementation-specific end-to-end architecture for the
veterinary **Clinical Intelligence** platform: RAG grounding over PubMed Central,
factual knowledge from 25–30 veterinary textbooks, SNOMED CT / VeNom / LOINC
ontologies, species-specific pharmacology, deterministic citation verification,
SOAP generation, and **DAT** (Directed-Acyclic-Tree) hierarchical parent→child→parent
agent orchestration.

## 📐 [`ARCHITECTURE.md`](./ARCHITECTURE.md) — the 5 diagrams

All diagrams are **Mermaid** (render natively on GitHub) and were validated with
`@mermaid-js/mermaid-cli`.

1. **High-Level Architecture** — layered User → API → Orchestrator → DAT → Knowledge → Stores → Models → Safety → Output.
2. **Low-Level / Detailed Architecture** — every connection labelled (protocol, request/response payload, sync/async, auth boundary, retrieval mechanism, model invocation, store accessed) plus a full connection register table.
3. **E2E System Flow** — two distinct flows: **(A) offline knowledge ingestion** (dashed) and **(B) online clinical query** (solid).
4. **Sequential Diagram** — chronological trace for *"likely causes and recommended diagnostic approach for kidney disease in a cat"*.
5. **Veterinarian User Flow** — login → query → understand → retrieve → DAT → synthesize → cited answer → review → SOAP → export (FUTURE).

## Design rules honored

- **DAT, not a mesh.** True Directed Acyclic Tree — one Root/Router parent; children run in parallel; **only** parent↔child communication; each child returns structured `{evidence, source_ids, confidence, metadata}`; synthesis runs **after** retrieval.
- **LLM is not the knowledge source.** It generates over retrieved, citation-verified, safety-grounded context only.
- **No invented specifics.** Undefined endpoints/models/technologies are marked `PROPOSED` / `MODEL TBD` / `TECHNOLOGY TBD`; future integrations (PMS/EHR) marked `FUTURE`.
- **Data stores shown separately** — Textbook KG, PMC Vector Index, Ontology Store, Pharmacology DB, Citation/Evidence Store, Patient/Context Store, Agent State/Execution Store, Audit/Observability Store.

> Diagrams render inline on GitHub. To export images locally:
> `npx -y @mermaid-js/mermaid-cli -i ARCHITECTURE.md -o out.md`
