"""Swappable LLM layer.

One `complete()` function over OpenAI (default), Claude or a local Ollama model.
Switching providers is a single value in .env - no other code changes.
"""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request

import contextlib
import contextvars
import time

import config

_openai_client = None
_anthropic_client = None

# Per-thread/per-task overrides for evaluation runs. Unset = normal behaviour
# (provider/model from config), so the app and CLI are unaffected.
_model_override: contextvars.ContextVar[tuple[str, str] | None] = contextvars.ContextVar("model_override", default=None)
_usage_log: contextvars.ContextVar[list | None] = contextvars.ContextVar("usage_log", default=None)


@contextlib.contextmanager
def use_model(spec: str):
    """Run calls inside the block on another model, e.g. 'openai:gpt-5-mini' or 'ollama:qwen2.5:7b'."""
    provider, _, model = spec.partition(":")
    token = _model_override.set((provider.strip().lower(), model.strip()))
    try:
        yield
    finally:
        _model_override.reset(token)


@contextlib.contextmanager
def track_usage():
    """Collect one record per LLM call made inside the block:
    {provider, model, input_tokens, output_tokens, reasoning_tokens, seconds}."""
    log: list[dict] = []
    token = _usage_log.set(log)
    try:
        yield log
    finally:
        _usage_log.reset(token)


def _record(provider: str, model: str, started: float, input_tokens=None, output_tokens=None, reasoning=None):
    log = _usage_log.get()
    if log is not None:
        log.append({
            "provider": provider, "model": model,
            "input_tokens": input_tokens, "output_tokens": output_tokens,
            "reasoning_tokens": reasoning, "seconds": round(time.perf_counter() - started, 3),
        })


def current_model() -> tuple[str, str]:
    override = _model_override.get()
    if override:
        return override
    provider = config.LLM_PROVIDER
    return provider, {"openai": config.OPENAI_MODEL, "claude": config.CLAUDE_MODEL,
                      "ollama": config.OLLAMA_MODEL}.get(provider, "")


def complete(system: str, prompt: str, json_mode: bool = False) -> str:
    provider, model = current_model()
    if provider == "openai":
        return _complete_openai(system, prompt, json_mode, model)
    if provider == "claude":
        return _complete_claude(system, prompt, json_mode, model)
    if provider == "ollama":
        return _complete_ollama(system, prompt, json_mode, model)
    raise ValueError(
        f"Unknown LLM_PROVIDER {provider!r}. Use 'openai', 'claude' or 'ollama'."
    )


def _complete_openai(system: str, prompt: str, json_mode: bool, model: str | None = None) -> str:
    global _openai_client
    if _openai_client is None:
        from openai import OpenAI

        if not config.OPENAI_API_KEY:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Copy PoC/.env.example to PoC/.env and add your key."
            )
        # Generation runs long, so it gets a longer timeout than embedding.
        _openai_client = OpenAI(
            api_key=config.OPENAI_API_KEY,
            max_retries=config.API_MAX_RETRIES,
            timeout=config.API_TIMEOUT_SECONDS * 3,
        )

    kwargs = {
        "model": model or config.OPENAI_MODEL,
        # max_completion_tokens, not max_tokens: the latter is rejected by
        # newer reasoning models, so this keeps OPENAI_MODEL swappable.
        "max_completion_tokens": config.LLM_MAX_TOKENS,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
    }
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    started = time.perf_counter()
    resp = _openai_client.chat.completions.create(**kwargs)
    usage = getattr(resp, "usage", None)
    details = getattr(usage, "completion_tokens_details", None)
    _record("openai", kwargs["model"], started,
            getattr(usage, "prompt_tokens", None), getattr(usage, "completion_tokens", None),
            getattr(details, "reasoning_tokens", None))
    return resp.choices[0].message.content or ""


def _complete_claude(system: str, prompt: str, json_mode: bool, model: str | None = None) -> str:
    global _anthropic_client
    if _anthropic_client is None:
        import anthropic

        if not config.ANTHROPIC_API_KEY:
            raise RuntimeError("ANTHROPIC_API_KEY is not set but LLM_PROVIDER=claude.")
        _anthropic_client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)

    if json_mode:
        prompt = f"{prompt}\n\nRespond with a single JSON object and nothing else."
    started = time.perf_counter()
    resp = _anthropic_client.messages.create(
        model=model or config.CLAUDE_MODEL,
        max_tokens=config.LLM_MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    _record("claude", model or config.CLAUDE_MODEL, started,
            getattr(resp.usage, "input_tokens", None), getattr(resp.usage, "output_tokens", None))
    return "".join(block.text for block in resp.content if block.type == "text")


def _complete_ollama(system: str, prompt: str, json_mode: bool, model: str | None = None) -> str:
    payload = {
        "model": model or config.OLLAMA_MODEL,
        "stream": False,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
    }
    if json_mode:
        payload["format"] = "json"

    request = urllib.request.Request(
        f"{config.OLLAMA_HOST.rstrip('/')}/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"Could not reach Ollama at {config.OLLAMA_HOST}. Is `ollama serve` running?"
        ) from exc
    _record("ollama", payload["model"], started, body.get("prompt_eval_count"), body.get("eval_count"))
    return body.get("message", {}).get("content", "")


def parse_json(raw: str) -> dict:
    """Parse a JSON object out of an LLM response, tolerating code fences."""
    text = raw.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise
