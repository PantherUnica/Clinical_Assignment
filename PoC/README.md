# VetAI - Proof of Concept

A working slice of the VetAI platform: vectorize two veterinary textbooks, then answer
clinical questions with answers whose **every claim is cited back to a book and page** -
and whose unsupported claims are **dropped before the answer is written**.

```
retrieve  ->  synthesize  ->  VERIFY (deterministic gate)  ->  generate
```

The two rules from the specs this PoC exists to prove:

1. **Retrieve and verify before writing** - the model only writes over evidence that has
   been retrieved and verified.
2. **The vet decides** - every claim can be opened to its source passage.

---

## 1 · Setup

From the `PoC` folder:

```bash
pip install -r requirements.txt

cp .env.example .env     # Windows: copy .env.example .env
# then edit .env and set OPENAI_API_KEY
```

Drop your **two textbook PDFs** into `PoC/books/`.

## 2 · Build the index (once)

```bash
python -m src.embed_index
```

This extracts text from the PDFs (OCR fallback for scanned pages), chunks it, embeds every
chunk, and writes a persistent vector store to `data/index/`. It prints the chunk maths as
it goes so you can see what happened.

## 3 · Run it

**Notebook** - see every stage, one at a time:

```bash
jupyter notebook notebooks/vetai_poc_walkthrough.ipynb
```

**Streamlit** - the demo UI with clickable citations:

```bash
python -m streamlit run app/streamlit_app.py
```

Use `python -m streamlit`, not bare `streamlit` - pip installs its script outside PATH on
Windows. **Run only one instance**, and open the URL the terminal prints: if port 8501 is
already in use Streamlit moves to 8502 without making much noise about it, so a remembered
URL can leave you looking at a different (older) copy of the app.

**CLI** - quickest sanity check:

```bash
python -m src.pipeline "What are the common causes of chronic kidney disease in cats?"
```

---

## How it works

| Stage | File | What it does |
|---|---|---|
| Ingest | `src/ingest.py` | PDF -> page text (+OCR) -> token chunks with page provenance |
| Index | `src/embed_index.py` | chunks -> embeddings -> ChromaDB |
| Retrieve | `src/retrieve.py` | question -> embedding -> top-k passages |
| Synthesize | `src/synthesize.py` | passages -> discrete claims, each tagged with its `chunk_id` |
| **Verify** | `src/verify.py` | **deterministic gate** - drops claims not supported by their source |
| Generate | `src/generate.py` | writes the answer over verified claims only |
| Orchestrate | `src/pipeline.py` | wires the four stages; used by the notebook and the app |

### The verification gate

This is the part that makes the output trustworthy, and it is **not** an LLM. A claim must
clear three checks, in order:

**1. Structural (pure code, no API call).** It must cite a `chunk_id` that was actually
retrieved. No citation -> `no_citation`; a citation that was never retrieved ->
`unknown_citation`. This runs first and needs no embeddings, so it cannot be disabled by an
embedding-service outage.

**2. Numeric.** Every number the claim states must appear in the passage it cites, otherwise
`number_not_in_source`. Word overlap alone cannot catch a fabricated dose - `Dog: 500 mg/kg
PO q4h` reuses the source's exact wording and only the figures are invented. Doses are the
highest-harm thing this system can get wrong, so figures are checked literally. This also
catches subtle alterations: a real `10-30 mg/kg` changed to `10-40 mg/kg` is rejected.

**3. Support scoring.**

```
score = VERIFY_LEXICAL_WEIGHT * lexical_coverage
      + (1 - VERIFY_LEXICAL_WEIGHT) * best_window_cosine
```

must reach `VERIFY_THRESHOLD` for at least one cited passage, else `unsupported_by_source`.
The cosine term is taken against the **best-matching sentence window inside** the passage,
not the passage as a whole: a chunk is ~600 tokens and often covers an entire topic, so
whole-chunk cosine asks "is this passage *entirely* about this claim?" when the question
that matters is "does it *contain* something that supports it?". On these books that change
moved genuine claims from 0.74 to 0.91 and removed a ~50% false-negative rate, while
fabricated claims stayed at or below 0.38.

Same claim + same passage always produces the same verdict - the reproducibility the spec
requires of verification (metric E-3). Every verdict carries a `claim_index`, so it is
traceable back to the claim that produced it even when two claims read identically.

If **no** claim survives, the pipeline returns an honest "no evidence" answer **without
calling the LLM at all**. There is no code path that produces an unsupported answer.

### Chunking maths

```
stride   = CHUNK_SIZE - CHUNK_OVERLAP
#chunks ~= total_tokens / stride
```

A token is ~3/4 of a word (~4 characters), so the default 600-token chunk is roughly one
textbook page, and `tokens ~= words * 1.33`.

Worked example for a ~400-page book:

```
400 pages x ~500 words/page = 200,000 words
200,000 x 1.33              ~ 266,000 tokens
CHUNK_SIZE 600, OVERLAP 100 -> stride 500
266,000 / 500               ~ 530 chunks
```

Two such books land around **1,060 vectors** - trivial for ChromaDB.

Why 500-800 tokens: small enough that a match is precise and a citation points at a tight
passage; large enough to carry a complete idea. Chunks are cut on sentence boundaries, never
mid-word, and each records the page it starts (and ends) on - that is what makes citations
resolve to `{book, page, passage}`.

---

## Swapping models

Everything is config. Edit `.env` (or `config.py` defaults):

| Want | Set |
|---|---|
| OpenAI (default) | `LLM_PROVIDER=openai`, `OPENAI_MODEL=gpt-5.5` |
| Claude | `LLM_PROVIDER=claude`, `ANTHROPIC_API_KEY=...`, `pip install anthropic` |
| Local / free | `LLM_PROVIDER=ollama`, `OLLAMA_MODEL=llama3.3` (run `ollama serve`) |
| Local embeddings (free) | `EMBED_PROVIDER=local`, `pip install sentence-transformers` |

Changing the **embedding** provider or the **chunk settings** requires a re-index
(`python -m src.embed_index`). Changing the **LLM** does not.

## Tuning

| Lever | Where | Effect |
|---|---|---|
| `TOP_K` | `.env` / UI slider | how much evidence synthesis sees |
| `VERIFY_THRESHOLD` | `.env` / UI slider | strictness of the gate (higher = fewer, safer claims) |
| `CHUNK_SIZE`, `CHUNK_OVERLAP` | `.env` | retrieval precision vs context (re-index needed) |
| `VERIFY_LEXICAL_WEIGHT` | `.env` | balance of word-overlap vs semantic similarity |

## Verifying it actually works

1. **Citation test** - ask an in-scope question, open each citation, confirm the passage
   really supports the claim.
2. **Grounding test** - ask something absent from the books (the notebook includes one).
   A grounded system reports missing evidence instead of inventing an answer.
3. **Threshold sweep** - the last notebook cell raises the threshold and shows claims being
   dropped; proves the gate is doing work rather than rubber-stamping.
4. **Fabrication test** - take a real claim, alter only a number, and feed it to
   `verify.verify_claims()` citing the genuine passage. It must come back
   `number_not_in_source`.

Measured on the two indexed books (1,478 chunks, `threshold=0.65`):

| Question | Claims | Verified |
|---|---|---|
| Clinical signs of dermatophytosis in cats | 12 | 12 |
| Dose of sulfasalazine in dogs and cats | 2 | 2 |
| Causes and treatment of feline acne | 12 | 12 |
| Diagnosis and management of canine otitis externa | 28 | 28 |
| Tyre pressure of a Boeing 747 (off-topic) | 0 | 0, refused |

Against a 9-case adversarial set (fabricated doses, subtly altered figures, wrong drug,
invented indications, bogus and missing citations) all 7 fabrications were rejected and both
genuine claims accepted - genuine scores 0.87-0.91 against a worst-case fabrication of 0.38.

## Troubleshooting

**`403 model_not_found`** - your key cannot access that model. List what it can:

```bash
python -c "import config; from openai import OpenAI; print(sorted(m.id for m in OpenAI(api_key=config.OPENAI_API_KEY).models.list().data))"
```

then set `OPENAI_MODEL` in `.env` to one of those.

**Answer comes back empty on a gpt-5.x model** - reasoning tokens are drawn from
`LLM_MAX_TOKENS`. Raise it (6000 is the default here).

**`The vector index is empty`** - run `python -m src.embed_index`.

**`'streamlit' is not recognized`** - use `python -m streamlit run app/streamlit_app.py`.

**The app looks like an older version, or two apps disagree** - you probably have more than
one instance running and are viewing the wrong port. Check with
`netstat -ano | findstr 850`, stop the extras, and use the URL your terminal prints.

**A red error box in the browser** - the message now names the cause and the fix (model
access, missing key, network, rate limit, empty index). Transient network failures are
retried `API_MAX_RETRIES` times before being reported, so a red box means it genuinely could
not complete - read the second line for what to do.

**Everything is dropped as `unsupported_by_source`** - lower `VERIFY_THRESHOLD` a little, or
check the retrieved passages in the notebook to see whether retrieval found the right pages
at all. Diagnose before loosening the gate.

## OCR (optional)

Scanned/image pages need OCR:

```bash
pip install pytesseract pillow
```

plus the Tesseract binary on your OS. Without it, image-only pages are skipped with a
warning and text pages still work.

---

## Deliberately out of scope

This PoC proves the cited-answer core only. Not included (all in the full spec):
image *interpretation*, ontology/SNOMED mapping, species-specific pharmacology lookup,
multiple specialist agents, authentication, SOAP note generation, and the audit store.
