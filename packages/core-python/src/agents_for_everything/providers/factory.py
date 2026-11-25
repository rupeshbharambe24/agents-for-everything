"""Capability-driven provider selection."""

from __future__ import annotations

import os

from .anthropic_provider import AnthropicProvider
from .base import BaseModelProvider, ProviderConfig
from .gemini_provider import GeminiProvider
from .mock import MockProvider
from .ollama_provider import OllamaProvider
from .openai_compat import OpenAICompatProvider


def resolve_provider(
    provider_name: str | None = None,
    model: str | None = None,
) -> BaseModelProvider:
    """Resolve a provider from explicit choice, environment, or deterministic mock fallback."""
    chosen = (provider_name or os.environ.get("AFE_PROVIDER") or "auto").lower()

    if chosen == "auto":
        if os.environ.get("OPENAI_API_KEY"):
            chosen = "openai"
        elif os.environ.get("ANTHROPIC_API_KEY"):
            chosen = "anthropic"
        elif os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"):
            chosen = "gemini"
        elif os.environ.get("OLLAMA_HOST"):
            chosen = "ollama"
        else:
            chosen = "mock"

    if chosen == "mock":
        return MockProvider(ProviderConfig(name="mock", model=model or "afe-mock-v1"))
    if chosen in {"openai", "openai-compat"}:
        return OpenAICompatProvider(
            ProviderConfig(
                name="openai",
                model=model or os.environ.get("AFE_MODEL", "gpt-4o-mini"),
                api_key=os.environ.get("OPENAI_API_KEY"),
                base_url=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"),
            )
        )
    if chosen == "anthropic":
        return AnthropicProvider(
            ProviderConfig(
                name="anthropic",
                model=model or os.environ.get("AFE_MODEL", "claude-sonnet-4-5"),
                api_key=os.environ.get("ANTHROPIC_API_KEY"),
                base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com"),
            )
        )
    if chosen == "gemini":
        return GeminiProvider(
            ProviderConfig(
                name="gemini",
                model=model or os.environ.get("AFE_MODEL", "gemini-2.5-flash"),
                api_key=os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"),
                base_url=os.environ.get("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta"),
            )
        )
    if chosen == "ollama":
        return OllamaProvider(
            ProviderConfig(
                name="ollama",
                model=model or os.environ.get("AFE_MODEL", "llama3.2"),
                base_url=os.environ.get("OLLAMA_HOST", "http://localhost:11434"),
            )
        )
    raise ValueError(f"Unsupported provider: {chosen!r}")
