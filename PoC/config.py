"""Central configuration for the VetAI PoC.

Everything tunable lives here. Values come from .env (copy .env.example), with
sensible defaults so the PoC runs with only OPENAI_API_KEY set.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

POC_ROOT = Path(__file__).resolve().parent
load_dotenv(POC_ROOT / ".env")

# --- Paths ---
BOOKS_DIR = POC_ROOT / "books"
DATA_DIR = POC_ROOT / "data"
CHUNKS_PATH = DATA_DIR / "chunks.jsonl"
INDEX_DIR = DATA_DIR / "index"
CHROMA_COLLECTION = "vetai_books"

# --- LLM (answer generation) ---
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").strip().lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-opus-5")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.3")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
# Generous because on gpt-5.x reasoning tokens are drawn from this same budget.
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "6000"))

# --- Embeddings (retrieval) ---
EMBED_PROVIDER = os.getenv("EMBED_PROVIDER", "openai").strip().lower()
OPENAI_EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")
LOCAL_EMBED_MODEL = os.getenv("LOCAL_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
EMBED_BATCH_SIZE = int(os.getenv("EMBED_BATCH_SIZE", "64"))

# --- Chunking ---
# stride = CHUNK_SIZE - CHUNK_OVERLAP ; n_chunks ~= total_tokens / stride
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "600"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "100"))

# A page yielding fewer than this many characters is treated as image-only
# and sent to the OCR fallback.
OCR_MIN_CHARS = int(os.getenv("OCR_MIN_CHARS", "80"))

# --- Retrieval ---
TOP_K = int(os.getenv("TOP_K", "6"))

# --- Citation verification gate (deterministic) ---
# A claim is verified when:
#   score = LEXICAL_WEIGHT * lexical_coverage + (1 - LEXICAL_WEIGHT) * cosine
# reaches VERIFY_THRESHOLD against at least one of its cited chunks.
VERIFY_THRESHOLD = float(os.getenv("VERIFY_THRESHOLD", "0.65"))
VERIFY_LEXICAL_WEIGHT = float(os.getenv("VERIFY_LEXICAL_WEIGHT", "0.5"))

if CHUNK_OVERLAP >= CHUNK_SIZE:
    raise ValueError(
        f"CHUNK_OVERLAP ({CHUNK_OVERLAP}) must be smaller than CHUNK_SIZE ({CHUNK_SIZE})"
    )


def stride() -> int:
    """How far the chunker advances per chunk."""
    return CHUNK_SIZE - CHUNK_OVERLAP


def ensure_dirs() -> None:
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def summary() -> dict:
    """Human-readable view of the active settings (shown in the UI/notebook)."""
    return {
        "llm_provider": LLM_PROVIDER,
        "llm_model": {
            "openai": OPENAI_MODEL,
            "claude": CLAUDE_MODEL,
            "ollama": OLLAMA_MODEL,
        }.get(LLM_PROVIDER, "unknown"),
        "embed_provider": EMBED_PROVIDER,
        "embed_model": OPENAI_EMBED_MODEL if EMBED_PROVIDER == "openai" else LOCAL_EMBED_MODEL,
        "chunk_size": CHUNK_SIZE,
        "chunk_overlap": CHUNK_OVERLAP,
        "stride": stride(),
        "top_k": TOP_K,
        "verify_threshold": VERIFY_THRESHOLD,
    }
