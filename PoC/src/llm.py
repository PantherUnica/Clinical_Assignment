"""Swappable LLM layer.

One `complete()` function over OpenAI (default), Claude or a local Ollama model.
Switching providers is a single value in .env - no other code changes.
"""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request

import config

_openai_client = None
_anthropic_client = None


def complete(system: str, prompt: str, json_mode: bool = False) -> str:
    provider = config.LLM_PROVIDER
    if provider == "openai":
        return _complete_openai(system, prompt, json_mode)
    if provider == "claude":
        return _complete_claude(system, prompt, json_mode)
    if provider == "ollama":
        return _complete_ollama(system, prompt, json_mode)
    raise ValueError(
        f"Unknown LLM_PROVIDER {provider!r}. Use 'openai', 'claude' or 'ollama'."
    )


def _complete_openai(system: str, prompt: str, json_mode: bool) -> str:
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
        "model": config.OPENAI_MODEL,
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
    resp = _openai_client.chat.completions.create(**kwargs)
    return resp.choices[0].message.content or ""


def _complete_claude(system: str, prompt: str, json_mode: bool) -> str:
    global _anthropic_client
    if _anthropic_client is None:
        import anthropic

        if not config.ANTHROPIC_API_KEY:
            raise RuntimeError("ANTHROPIC_API_KEY is not set but LLM_PROVIDER=claude.")
        _anthropic_client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)

    if json_mode:
        prompt = f"{prompt}\n\nRespond with a single JSON object and nothing else."
    resp = _anthropic_client.messages.create(
        model=config.CLAUDE_MODEL,
        max_tokens=config.LLM_MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(block.text for block in resp.content if block.type == "text")


def _complete_ollama(system: str, prompt: str, json_mode: bool) -> str:
    payload = {
        "model": config.OLLAMA_MODEL,
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
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"Could not reach Ollama at {config.OLLAMA_HOST}. Is `ollama serve` running?"
        ) from exc
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
