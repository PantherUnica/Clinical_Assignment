"""VetAI PoC - Streamlit demo.

Run from the PoC folder:
    streamlit run app/streamlit_app.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st

import config
from src import pipeline
from src.embed_index import get_collection

st.set_page_config(page_title="VetAI PoC", layout="wide")

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
        indexed = get_collection().count()
        if indexed:
            st.success(f"Index ready: {indexed:,} chunks")
        else:
            st.error("Index is empty. Run `python -m src.embed_index`")
    except Exception as exc:  # index dir missing, deps missing, etc.
        st.error(f"Index unavailable: {exc}")

question = st.text_area(
    "Clinical question",
    placeholder="e.g. What are the common causes of chronic kidney disease in cats?",
    height=90,
)

if st.button("Ask", type="primary") and question.strip():
    with st.spinner("Retrieving evidence, verifying claims, writing answer ..."):
        try:
            result = pipeline.answer_question(
                question.strip(), top_k=top_k, threshold=threshold
            )
        except Exception as exc:
            st.error(f"{exc}")
            st.stop()

    st.divider()

    if result["grounded"]:
        st.subheader("Answer")
        st.markdown(result["answer"])
    else:
        st.subheader("No supported answer")
        st.warning(result["answer"])

    columns = st.columns(4)
    columns[0].metric("Claims proposed", len(result["claims"]))
    columns[1].metric("Verified", len(result["verified"]))
    columns[2].metric("Dropped", len(result["rejected"]))
    columns[3].metric("Time", f"{result['elapsed_sec']}s")

    if result["citations"]:
        st.subheader("Sources")
        st.caption("Open a citation to read the exact passage the claim came from.")
        for citation in result["citations"]:
            pages = (
                f"p.{citation['page']}"
                if citation["page"] == citation["page_end"]
                else f"pp.{citation['page']}-{citation['page_end']}"
            )
            label = f"[{citation['marker']}] {citation['book_title']} - {pages}"
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
                st.markdown(
                    f"- `{claim['reason']}` (score {claim['score']}) - {claim['text']}"
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
