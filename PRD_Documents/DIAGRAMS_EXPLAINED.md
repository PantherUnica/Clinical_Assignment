# Understanding the Diagrams — Simple Explanation

This file explains the **High-Level Diagram** and the **Low-Level Diagram** in easy English.
Think of the whole system as a smart helper for a **vet (animal doctor)**. The vet asks a
question, and the system finds trusted answers from books and research, then writes a clear,
cited reply.

Two important ideas to remember:

1. **RAG = "look it up first, then answer."** The system does **not** answer from memory.
   It first *finds* real evidence (from books and research), and only then writes the answer.
2. **The AI (LLM) is only the writer, not the source of truth.** It puts the found evidence
   into nice, readable sentences. It is not allowed to make up facts.

---

## PART 1 — The High-Level Diagram (the "big picture")

The high-level diagram shows the system in **10 layers**, read from **left to right**.
Each layer is one job. Here is what each one does, in order.

### 1. USER
The **veterinarian**. They type a question, and can also add the animal's details
(species, age, symptoms) or upload an image or lab report.

### 2. API / BACKEND (the front door)
This is the **entry gate**.
- It checks **who you are** (login) and **what you're allowed to do** (permissions).
- It keeps the **case/patient information** for this visit.
- Think of it like the reception desk at a clinic — you check in here first.

### 3. CLINICAL INTELLIGENCE ORCHESTRATOR (the "understand the question" step)
Before searching, the system must **understand** what the vet is really asking. It does four things:
- **Query Understanding** — reads the question.
- **Species Detection** — figures out the animal (cat, dog, etc.). This matters a lot,
  because medicine and drug doses are different for different animals.
- **Concept Mapping** — turns everyday words into official medical codes using
  **SNOMED CT, VeNom, and LOINC** (standard medical dictionaries). For example,
  "kidney disease" becomes a proper medical code that all systems agree on.
- **Query Decomposition** — breaks a big question into smaller parts
  (causes, tests, treatment, etc.), so each part can be handled properly.

### 4. DAT AGENTS (the team of specialists)
**DAT** means **Directed Acyclic Tree** — a fancy name for a **team with one boss and several helpers**.
It works like a hospital team:
- **Root / Router Agent** = the **team leader**. It hands out tasks.
- The helpers (children) each have one job, and they all work **at the same time**:
  - **Clinical Reasoning Agent** — thinks about possible causes.
  - **Literature / PMC Retrieval Agent** — searches research papers.
  - **Ontology / Concept Agent** — handles medical codes.
  - **Pharmacology Agent** — handles drugs and doses.
  - **Specialist Agents** — expert "avatars": Internal Medicine, Oncology (cancer),
    Anesthesia, Dentistry.
  - **Provenance Capture Agent** — records exactly where each retrieved fact came from (source → passage), so it can be checked later. (The actual **citation verification** is a separate, deterministic step that runs **after** the team reports back — see Part 2, step 7 — not one of the parallel helpers.)

**Key rule:** helpers only talk to the **leader**, never to each other. Each helper finishes
its task and **reports back to the leader** with its findings, its **sources**, and a
**confidence score** (how sure it is). This keeps things clean and organized.

### 5. EVIDENCE / SYNTHESIS (combining the findings)
Once all helpers report back, the system:
- **Ranks / re-ranks** the evidence — puts the most useful facts on top.
- **Specialist synthesis** — each specialist's findings are summarized.
- **Parent synthesis** — the leader combines everything into one draft answer.

### 6. KNOWLEDGE SOURCES (where the real facts come from)
These are the **trusted origins** of information:
- **25–30 Veterinary Textbooks** — solid, established facts.
- **PubMed Central (PMC)** — the latest research papers.
- **SNOMED CT, VeNom, LOINC** — the standard medical dictionaries/codes.
- **Pharmacology DB source** — drug names, doses per species, side effects, interactions.
- **Clinical / PMS / EHR data** — clinic records. Marked **(FUTURE)** = planned, not built yet.

### 7. DATA STORES / INDEXES (the organized memory shelves)
The raw sources above are cleaned and stored in **separate shelves** so they're fast to search:
- **Textbook Knowledge Store / Knowledge Graph** — facts and how they connect.
- **PMC Vector Index** — research papers stored in a way that makes "search by meaning" fast.
- **Clinical Ontology Store** — the medical codes.
- **Pharmacology Database** — the drug data.
- **Citation / Evidence Store** — keeps track of exactly which sentence came from which source.
- **Patient / Clinical Context Store** — the current animal's details.
- **Agent State / Execution Store** — keeps track of what the team is doing right now.
- **Audit / Observability Store** — a logbook of everything that happened (for safety/checking).

### 8. MODELS (the AI tools)
- **Foundation LLM** — the AI that **writes** the final answer. It only writes using the
  evidence it was given. (Exact model **not yet decided → "MODEL TBD".**)
- **Embedding Model** — turns text into numbers so the system can "search by meaning".
- **Re-ranker Model** — sorts search results so the best ones come first.

### 9. SAFETY / GOVERNANCE (the double-check)
- **Citation Mapping + Verification** — makes sure every claim in the answer really matches a real source.
- **Clinical Safety / Grounding Checks** — throws away anything not backed by evidence.
  This stops the AI from "making things up".

### 10. OUTPUT (what the vet receives)
- **Final Cited Clinical Answer** — the answer, with sources shown.
- **SOAP Generator** — can turn the answer into a **SOAP note** (a standard vet/medical
  record format: Subjective, Objective, Assessment, Plan).
- **Export to PMS / EHR** — sending it to clinic software. Marked **(FUTURE)**.

### The one-line summary of the high-level flow
> **Vet asks → system checks login → understands the question → the agent team searches trusted
> sources → combines the findings → double-checks the sources → the AI writes the cited answer →
> the vet gets the answer (and optionally a SOAP note).**

### About the arrows and colors
- **Solid arrows** = the live flow when a vet asks a question (runtime).
- **Dashed arrows** = the "loading the library" flow that happens **beforehand** (ingestion).
- **Dashed-border boxes** = **future** or **not-yet-decided** parts.
- Each color is just one group (User, API, Agents, Knowledge, Stores, Models, Safety, Output).

---

## PART 2 — The Low-Level Diagram (the "technical close-up")

The low-level diagram shows the **same system**, but now with the **wiring details**:
which part talks to which, **how** they talk, and **what data** they send. It's for engineers
who will actually build it.

A few words that appear a lot:
- **API / endpoint** — a specific "address" one part calls, like `POST /api/v1/clinical/query`.
  (`POST` just means "send some data".)
- **[PROPOSED]** — this exact address/name is **not final yet**; it's a sensible suggestion.
- **sync** (synchronous) = "wait for the reply before moving on."
- **async** (asynchronous) = "send it and keep going; the reply comes later."
- **payload** — the actual data being sent (shown in `{curly braces}`).
- **Auth boundary** — the security line between the outside world and the inside system.

### The security line (very important)
- The **vet's app is outside**. Everything else is **inside** a protected zone.
- The **API Gateway + Auth Service** is the **only door in**. It checks the login (OIDC/JWT),
  checks permissions (RBAC), and uses encryption (TLS).
- Inside, the services talk to each other over a private, secured network (mTLS).
- **Meaning:** strangers can't reach the internal parts directly — they must pass the gate.

### Step-by-step, what actually happens

**1) Vet → Gateway**
The vet's app sends the question to `POST /api/v1/clinical/query`.
- It sends: `{vet_id, patient, species?, text, image?}`
- It gets back: `{answer, citations[], soap?}`
- This waits for the reply (**sync**).

**2) Gateway → Orchestrator (understanding chain)**
The gateway passes the question inward, and it flows through:
`Query Understanding → Species Detection → Concept Mapping → Ontology mapping → Query Decomposition`.
- Ontology mapping calls `POST /api/v1/ontology/map` to turn words into **SNOMED / VeNom / LOINC** codes.

**3) Orchestrator → DAT Root/Router**
The understood, broken-down question is handed to the **team leader** via `POST /api/v1/agents/route`.
- It sends: `{subqueries[], concepts[], species, patient_ctx}`.

**4) Root → child agents (fan-out)**
The leader sends each helper its task **at the same time** (**async fan-out**). Then each helper
does its own lookup:
- **Literature Agent** → asks the **Embedding Model** to turn the query into numbers →
  searches the **PMC Vector Index** via `POST /api/v1/retrieval/search` (this is the "top-k" search =
  "give me the k best matches") → then uses the **Re-ranker** to sort them best-first.
- **Clinical Reasoning Agent** and **Internal Medicine specialist** → look up facts in the
  **Textbook Knowledge Graph**.
- **Ontology Agent** → looks up codes in the **Ontology Store**.
- **Pharmacology Agent** → looks up drug + dose info in the **Pharmacology Database**
  (sends `{drug, species}`, gets back `{dose_by_species, side_effects[], interactions[]}`).

**5) Children → Root (report back)**
Every helper returns a **structured report** to the leader:
`{evidence[], source_ids[], confidence, metadata}`.
- `source_ids[]` = exactly where each fact came from.
- `confidence` = how sure the helper is.
- **Again: helpers report only to the leader, never to each other.**

**6) Root → Synthesis**
The leader sends all the collected evidence to the **Synthesis Service** (`POST /api/v1/synthesis`),
which combines it into a **draft answer** plus a map of "which claim came from which source".

**7) Synthesis → Citation Verification**
The draft goes to `POST /api/v1/citations/verify`. This step **deterministically** (meaning: by
strict matching, not by guessing) checks that each claim truly matches a real source in the
**Citation / Evidence Store**. Anything that doesn't match is flagged.

**8) Verification → Safety / Grounding**
Then a safety check removes any claim that isn't backed by evidence ("grounding"). Only
**verified, safe** content passes.

**9) Safety → LLM (write the answer)**
Now — and only now — the **Foundation LLM** is called with `invoke_llm(grounded_context, approved_citations)`.
- The LLM **writes** the answer using **only** the approved evidence and citations.
- It does **not** add facts of its own. (This is the whole point: no made-up medicine.)

**10) LLM → Gateway → Vet**
The finished, cited answer travels back out through the gateway to the vet (`200 OK` = success).

**11) Optional: SOAP note**
If the vet wants a record, `POST /api/v1/soap/generate` turns the answer into a **SOAP note**
`{soap:{S,O,A,P}, citations[]}`.

### The quiet helpers in the background (cross-cutting)
Some stores are used the whole time, quietly:
- **Agent State / Execution Store** — remembers what the team is doing (so nothing gets lost).
- **Patient / Clinical Context Store** — holds the current animal's details.
- **Citation / Evidence Store** — the source-tracking notebook.
- **Audit / Observability Store** — the logbook that records everything for safety and review.

### The connection table (2a in ARCHITECTURE.md)
Right under the low-level diagram there is a **table** listing **every single connection** with:
source, destination, the API used, what's sent, what's returned, sync or async, the format,
the security boundary, how it searches, which AI model it uses, and which store it reads.
That table is the **engineer's checklist** for building the system exactly right.

---

## High-Level vs Low-Level — what's the difference?

| | **High-Level** | **Low-Level** |
|---|---|---|
| **Who it's for** | Everyone (managers, vets, new team members) | Engineers who build it |
| **What it shows** | The big picture: the 10 layers and the overall flow | The exact wiring: APIs, data sent, security, sync/async |
| **Detail** | "What happens and in what order" | "How each part talks to each other, precisely" |
| **Best question it answers** | "How does the whole thing work?" | "What do I need to actually build each connection?" |

---

## Two golden rules (true in both diagrams)

1. **Find first, then write.** The system always gathers real evidence **before** the AI writes anything.
2. **The AI is the writer, not the knowledge.** Every fact in the answer is traced back to a real,
   verified source — the AI just phrases it clearly. This is what makes the answers **safe and trustworthy**
   for real animal care.
