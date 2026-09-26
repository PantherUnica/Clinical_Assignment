# Simple Flow — The Full Picture, Made Easy

This shows **everything the system does**, but in plain language — no technical wiring.
Read it left to right: the vet asks, a team of helpers gathers trusted facts, the facts are
checked, and the AI writes a clear, sourced answer.

```mermaid
flowchart LR
  classDef user  fill:#E3F2FD,stroke:#1565C0,color:#0D47A1,stroke-width:1px;
  classDef app   fill:#E8F5E9,stroke:#2E7D32,color:#1B5E20,stroke-width:1px;
  classDef team  fill:#F3E5F5,stroke:#6A1B9A,color:#4A148C,stroke-width:1px;
  classDef know  fill:#FCE4EC,stroke:#AD1457,color:#880E4F,stroke-width:1px;
  classDef fin   fill:#FFF3E0,stroke:#EF6C00,color:#E65100,stroke-width:1px;
  classDef model fill:#E0F7FA,stroke:#00838F,color:#006064,stroke-width:1px;
  classDef out   fill:#F1F8E9,stroke:#558B2F,color:#33691E,stroke-width:1px;

  VET["🩺 Vet asks a question<br/>question + patient details + image"]:::user

  subgraph APP["Step 1 — Front desk"]
    direction TB
    LOGIN["Check login<br/>(who are you?)"]:::app
    UNDERSTAND["Understand the question<br/>• which animal? (cat, dog…)<br/>• what topic? (e.g. kidney disease)<br/>• match to medical terms"]:::app
    LOGIN --> UNDERSTAND
  end

  subgraph TEAM["Step 2 — The helper team"]
    direction TB
    ROUTER["👑 Team Leader<br/>gives out the tasks"]:::team
    REASON["Reasoning helper<br/>(possible causes)"]:::team
    RESEARCH["Research helper<br/>(finds papers)"]:::team
    ONTO["Terms helper<br/>(medical codes)"]:::team
    PHARM["Medicine helper<br/>(drugs & doses)"]:::team
    SPEC["Specialist helpers<br/>Internal Medicine · Oncology ·<br/>Anesthesia · Dentistry"]:::team
    CITE["Source checker<br/>(are the facts real?)"]:::team
    ROUTER --> REASON & RESEARCH & ONTO & PHARM & SPEC & CITE
  end

  subgraph KNOW["Step 3 — Trusted knowledge"]
    direction TB
    BOOKS["📚 Vet textbooks"]:::know
    PAPERS["🔬 Research papers"]:::know
    CODES["🏷️ Medical codes<br/>SNOMED · VeNom · LOINC"]:::know
    DRUGS["💊 Drug database<br/>doses per animal, side effects"]:::know
  end

  subgraph FINISH["Step 4 — Build the answer"]
    direction TB
    COMBINE["Combine & sort the evidence<br/>(best facts first)"]:::fin
    SAFE["Check sources + safety<br/>keep ONLY verified facts"]:::fin
    LLM["🤖 AI writes the answer<br/>(AI model — TBD)<br/>uses only the verified facts"]:::model
    COMBINE --> SAFE --> LLM
  end

  ANSWER["✅ Vet gets a clear answer<br/>with sources shown"]:::out
  SOAP["📝 Optional: SOAP note<br/>(a tidy medical record)"]:::out

  VET ==> LOGIN
  UNDERSTAND ==> ROUTER
  TEAM ==>|"look up trusted sources"| KNOW
  KNOW ==>|"send back real facts"| TEAM
  TEAM ==> COMBINE
  LLM ==> ANSWER ==> SOAP
```

---

## The whole story in a few lines

> A vet asks a question. The system checks who they are and works out **which animal** and
> **what topic** it's about. A **team of helpers** (led by one leader) goes and looks things up
> in **trusted sources** — vet textbooks, research papers, medical code lists, and a drug database.
> The helpers bring back real facts, the system **keeps only what's verified**, and then the
> **AI writes the final answer using just those facts** — with the sources shown. If the vet wants,
> it can also make a **SOAP note** (a neat medical record).

## What each step does (plain words)

**Step 1 — Front desk**
- **Check login:** makes sure the person is allowed to use the system.
- **Understand the question:** works out the animal, the topic, and matches everyday words to
  official medical terms so nothing gets confused.

**Step 2 — The helper team**
- A **Team Leader** hands out jobs and collects the results. The helpers work **at the same time**:
  - *Reasoning* — thinks about possible causes.
  - *Research* — finds relevant papers.
  - *Terms* — handles medical codes.
  - *Medicine* — looks up drugs and correct doses for that animal.
  - *Specialists* — expert helpers for Internal Medicine, Cancer, Anesthesia, and Dentistry.
  - *Source checker* — makes sure every fact is real and traceable.
- The helpers only report to the **leader** — this keeps things simple and organized.

**Step 3 — Trusted knowledge**
- The real facts come from **textbooks, research papers, medical code lists, and a drug database**.
- Important: facts come from **these trusted sources**, *not* from the AI's imagination.

**Step 4 — Build the answer**
- **Combine & sort:** put the most useful facts first.
- **Check sources + safety:** throw away anything not backed by a real source.
- **AI writes the answer:** the AI model turns the verified facts into a clear reply.
  It is **only the writer** — it can't add facts of its own. *(Which exact AI model to use is still to be decided.)*

**Final**
- **The vet gets a clear answer** with the sources shown, so they can trust and double-check it.
- **Optional SOAP note:** the answer can be saved as a standard medical record.

## The one rule that keeps it safe

> **Find the real facts first — then let the AI write.**
> Every fact in the answer can be traced back to a trusted source.
