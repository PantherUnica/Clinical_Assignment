"""VetAI PoC - Streamlit demo.

Run from the PoC folder:
    python -m streamlit run app/streamlit_app.py

Use `python -m streamlit`, not bare `streamlit` - pip installs the script outside
PATH on this machine. If port 8501 is already taken, Streamlit silently moves to
8502, so trust the URL printed in your terminal over any remembered one.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st

import config
from src import pipeline
from src.embed_index import get_collection

st.set_page_config(page_title="VetAI PoC", layout="wide")


# --- Resources -------------------------------------------------------------
# Cached so the ChromaDB client is opened once per process rather than once per
# rerun. Streamlit reruns the whole script on every widget interaction, and
# reopening the index each time made the page visibly hang.


@st.cache_resource(show_spinner=False)
def _collection():
    return get_collection()


@st.cache_data(ttl=30, show_spinner=False)
def _index_count() -> int:
    return _collection().count()


def _explain(exc: Exception) -> tuple[str, str]:
    """Turn an exception into (what happened, what to do about it)."""
    name = type(exc).__name__
    text = str(exc)
    lowered = text.lower()

    if "does not have access to model" in lowered or "model_not_found" in lowered:
        return (
            f"Your API key cannot access the model `{config.summary()['llm_model']}`.",
            "Set `OPENAI_MODEL` in `PoC/.env` to a model your key allows - the README "
            "has a one-liner that lists them.",
        )
    if "api_key" in lowered or "OPENAI_API_KEY" in text:
        return (
            "No usable API key was found.",
            "Copy `PoC/.env.example` to `PoC/.env` and set `OPENAI_API_KEY`.",
        )
    if name in {"APIConnectionError", "APITimeoutError"} or "connection error" in lowered:
        return (
            "Could not reach the OpenAI API.",
            f"This is usually a network blip. The app already retried "
            f"{config.API_MAX_RETRIES} times - check your connection and press Ask again.",
        )
    if name == "RateLimitError" or "rate limit" in lowered or "quota" in lowered:
        return (
            "The API rejected the request for rate limit or quota reasons.",
            "Wait a moment and try again, or check the billing and usage limits on your "
            "OpenAI account.",
        )
    if "index" in lowered and ("empty" in lowered or "not found" in lowered):
        return (
            "The vector index is missing or empty.",
            "Build it from the PoC folder with `python -m src.embed_index`.",
        )
    return (f"{name}: {text}", "")


def _pages(citation: dict) -> str:
    if citation["page"] == citation["page_end"]:
        return f"p.{citation['page']}"
    return f"pp.{citation['page']}-{citation['page_end']}"


# --- Header ----------------------------------------------------------------

st.title("VetAI - Evidence-Grounded Clinical Answers")
st.caption(
    "Proof of concept. Every claim is verified against the source books before it is "
    "written - unsupported claims are dropped, not softened."
)

settings = config.summary()

with st.sidebar:
    st.header("Configuration")
    st.markdown(f"**LLM** &nbsp; `{settings['llm_provider']}` / `{settings['llm_model']}`")
    st.markdown(
        f"**Embeddings** &nbsp; `{settings['embed_provider']}` / `{settings['embed_model']}`"
    )
    st.markdown(
        f"**Chunking** &nbsp; {settings['chunk_size']} tokens, "
        f"overlap {settings['chunk_overlap']} (stride {settings['stride']})"
    )

    st.divider()
    top_k = st.slider("Passages retrieved (top-k)", 1, 20, int(settings["top_k"]))
    threshold = st.slider(
        "Verification threshold", 0.0, 1.0, float(settings["verify_threshold"]), 0.01
    )
    st.caption("Raise the threshold to be stricter about what counts as supported evidence.")

    st.divider()
    try:
        indexed = _index_count()
        if indexed:
            st.success(f"Index ready: {indexed:,} chunks")
        else:
            st.error("Index is empty. Run `python -m src.embed_index`")
    except Exception as exc:
        headline, remedy = _explain(exc)
        st.error(headline)
        if remedy:
            st.caption(remedy)

# --- Ask -------------------------------------------------------------------
# A form so Ctrl+Enter submits, and so the question is sent together with the
# slider values instead of firing a rerun on every keystroke.

with st.form("ask", clear_on_submit=False):
    question = st.text_area(
        "Clinical question",
        placeholder="e.g. What are the common causes of chronic kidney disease in cats?",
        height=90,
    )
    submitted = st.form_submit_button("Ask", type="primary")

if submitted:
    if not question.strip():
        st.warning("Type a clinical question first.")
    else:
        with st.status("Working...", expanded=True) as status:
            try:
                result = pipeline.answer_question(
                    question.strip(),
                    top_k=top_k,
                    threshold=threshold,
                    on_stage=status.write,
                )
            except Exception as exc:
                status.update(label="Failed", state="error", expanded=False)
                st.session_state["result"] = None
                st.session_state["error"] = _explain(exc)
            else:
                status.update(
                    label=f"Done in {result['elapsed_sec']}s",
                    state="complete",
                    expanded=False,
                )
                # Held in session_state so the answer survives later reruns -
                # moving a slider or opening a panel must not wipe it.
                st.session_state["result"] = result
                st.session_state["error"] = None
                st.session_state["settings_used"] = (top_k, threshold)

# --- Render from state, never from the submit event ------------------------

if st.session_state.get("error"):
    headline, remedy = st.session_state["error"]
    st.error(headline)
    if remedy:
        st.info(remedy)

result = st.session_state.get("result")

if result:
    used = st.session_state.get("settings_used")
    if used and used != (top_k, threshold):
        st.warning(
            f"Settings changed since this answer was produced (it used top-k {used[0]}, "
            f"threshold {used[1]:.2f}). Press Ask to apply the new ones."
        )

    st.divider()

    if result["grounded"]:
        st.subheader("Answer")
        st.markdown(result["answer"])
    else:
        st.subheader("No supported answer")
        st.warning(result["answer"])

    st.caption(f"Question: {result['question']}")

    columns = st.columns(4)
    columns[0].metric("Claims proposed", len(result["claims"]))
    columns[1].metric("Verified", len(result["verified"]))
    columns[2].metric("Dropped", len(result["rejected"]))
    columns[3].metric("Time", f"{result['elapsed_sec']}s")

    if result["citations"]:
        st.subheader("Sources")
        st.caption("Open a citation to read the exact passage the claim came from.")
        for citation in result["citations"]:
            label = f"[{citation['marker']}] {citation['book_title']} - {_pages(citation)}"
            with st.expander(label):
                st.markdown(f"> {citation['text']}")
                st.caption(
                    f"chunk_id `{citation['chunk_id']}` | "
                    f"retrieval similarity {citation['similarity']}"
                )

    if result["rejected"]:
        with st.expander(f"Dropped by the verification gate ({len(result['rejected'])})"):
            st.caption(
                "These claims were proposed but could not be matched to a supporting "
                "passage, so they never reached the answer."
            )
            for claim in result["rejected"]:
                extra = ""
                if claim.get("unsourced_numbers"):
                    extra = f" - figures absent from the source: {claim['unsourced_numbers']}"
                st.markdown(
                    f"- `{claim['reason']}` (score {claim['score']}) - {claim['text']}{extra}"
                )

    with st.expander(f"Retrieved passages ({len(result['passages'])})"):
        for passage in result["passages"]:
            st.markdown(
                f"**{passage['similarity']}** - `{passage['chunk_id']}` - "
                f"{passage['book_title']}, p.{passage['page']}"
            )
            st.caption(passage["text"][:400] + ("..." if len(passage["text"]) > 400 else ""))

    if result["synthesis_notes"]:
        st.info(f"Synthesis note: {result['synthesis_notes']}")
