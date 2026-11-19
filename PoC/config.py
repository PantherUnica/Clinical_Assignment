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

# --- Full 17-book library (separate from the 2-book eval index above) ---
LIBRARY_MANIFEST = BOOKS_DIR / "library_manifest.json"
LIBRARY_DIR = DATA_DIR / "library"
LIBRARY_PAGES_DIR = LIBRARY_DIR / "pages"  # cleaned page text + metadata, one file per book
OCR_CACHE_DIR = LIBRARY_DIR / "ocr_cache"  # OCR text per page, so OCR runs only once
LIBRARY_CHUNKS_DIR = LIBRARY_DIR / "chunks"  # one chunks file per book
LIBRARY_INDEX_DIR = LIBRARY_DIR / "index"
LIBRARY_COLLECTION = "vetai_library"
REPORTS_DIR = POC_ROOT / "reports"
OCR_DPI = int(os.getenv("OCR_DPI", "300"))
OCR_WORKERS = int(os.getenv("OCR_WORKERS", str(max(1, (os.cpu_count() or 2) - 2))))
TESSERACT_CMD = os.getenv("TESSERACT_CMD", r"C:\Program Files\Tesseract-OCR\tesseract.exe")

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

# Transient connection blips should be retried, not surfaced as a failure.
API_MAX_RETRIES = int(os.getenv("API_MAX_RETRIES", "5"))
API_TIMEOUT_SECONDS = float(os.getenv("API_TIMEOUT_SECONDS", "60"))

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
# At most this many passages per book in the top-k (0 = no cap, the default).
MAX_PER_BOOK = int(os.getenv("MAX_PER_BOOK", "0"))

# --- Citation verification gate (deterministic) ---
# A claim is verified when:
#   score = LEXICAL_WEIGHT * lexical_coverage + (1 - LEXICAL_WEIGHT) * cosine
# reaches VERIFY_THRESHOLD against at least one of its cited chunks.
VERIFY_THRESHOLD = float(os.getenv("VERIFY_THRESHOLD", "0.65"))
VERIFY_LEXICAL_WEIGHT = float(os.getenv("VERIFY_LEXICAL_WEIGHT", "0.5"))

# --- Knowledge-base profile ---
# eval2   : the frozen 2-book eval index (data/index, collection vetai_books)
# library : all 17 books (data/library/index, collection vetai_library)
# Set KB_PROFILE in .env, or pass --profile on the command line (calls set_profile).
PROFILES = {
    "eval2": {"index_dir": INDEX_DIR, "collection": CHROMA_COLLECTION, "chunks": CHUNKS_PATH},
    "library": {"index_dir": LIBRARY_INDEX_DIR, "collection": LIBRARY_COLLECTION, "chunks": LIBRARY_CHUNKS_DIR},
}
KB_PROFILE = "eval2"


def set_profile(name: str) -> None:
    """Point INDEX_DIR / CHROMA_COLLECTION / CHUNKS_PATH at a profile.

    Everything reads these module attributes at call time, so switching here
    switches the whole pipeline.
    """
    global KB_PROFILE, INDEX_DIR, CHROMA_COLLECTION, CHUNKS_PATH
    if name not in PROFILES:
        raise ValueError(f"Unknown KB_PROFILE {name!r}. Use one of: {', '.join(PROFILES)}")
    p = PROFILES[name]
    KB_PROFILE, INDEX_DIR, CHROMA_COLLECTION, CHUNKS_PATH = name, p["index_dir"], p["collection"], p["chunks"]


set_profile(os.getenv("KB_PROFILE", "eval2").strip().lower())

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
        "kb_profile": KB_PROFILE,
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
        "max_per_book": MAX_PER_BOOK,
        "verify_threshold": VERIFY_THRESHOLD,
    }
