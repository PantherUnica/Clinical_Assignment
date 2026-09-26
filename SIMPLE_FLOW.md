# Simple Flow — How It Works (Step by Step)

A clean, easy version of the architecture. Just follow the arrows from top to bottom.

```mermaid
flowchart TD
  classDef user  fill:#E3F2FD,stroke:#1565C0,color:#0D47A1,stroke-width:1px;
  classDef sys   fill:#FFF3E0,stroke:#EF6C00,color:#E65100,stroke-width:1px;
  classDef agent fill:#F3E5F5,stroke:#6A1B9A,color:#4A148C,stroke-width:1px;
  classDef know  fill:#FCE4EC,stroke:#AD1457,color:#880E4F,stroke-width:1px;
  classDef model fill:#E0F7FA,stroke:#00838F,color:#006064,stroke-width:1px;
  classDef out   fill:#F1F8E9,stroke:#558B2F,color:#33691E,stroke-width:1px;

  S1["1 · Vet asks a question<br/>(text · patient info · image)"]:::user
  S2["2 · App / API<br/>checks login, receives the question"]:::sys
  S3["3 · Understand the question<br/>which animal? what topic?"]:::sys
  S4["4 · Agent (the team leader)<br/>decides what to look up"]:::agent
  S5["5 · Search trusted knowledge<br/>textbooks · research · drug info"]:::know
  S6["6 · Collect & check evidence<br/>keep only real, verified facts"]:::agent
  S7["7 · LLM writes the answer<br/>(the AI model — MODEL TBD)<br/>uses ONLY the verified facts"]:::model
  S8["8 · Vet gets a clear answer<br/>with sources / citations"]:::out
  S9["9 · Optional: make a SOAP note"]:::out

  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9
```

---

## In one sentence

> The vet asks → the app understands the question → the **Agent** looks up trusted sources →
> the evidence is checked → the **LLM (AI model)** writes the answer using only that evidence →
> the vet gets a clear, cited answer (and can save it as a SOAP note).

## The 9 steps in plain words

1. **Vet asks a question.** They can add the animal's details or a photo/lab report.
2. **App / API.** The front door — checks who you are and takes in the question.
3. **Understand the question.** Works out the animal (cat, dog…) and the topic (e.g. kidney disease).
4. **Agent (team leader).** Decides what needs to be looked up to answer well.
5. **Search trusted knowledge.** Looks in vet textbooks, research papers, and drug data —
   **not** from the AI's memory.
6. **Collect & check evidence.** Gathers the findings and keeps only facts that are real and verified.
7. **LLM writes the answer.** The AI model turns the verified facts into a clear reply.
   It is **only the writer** — it can't add facts of its own. *(Which exact model to use is still TBD.)*
8. **Vet gets the answer.** Clear, with the sources shown so the vet can trust and check it.
9. **Optional SOAP note.** Turn the answer into a standard medical record if wanted.

**The golden rule:** *find the facts first, then let the AI write.* This keeps the answers safe and trustworthy.
