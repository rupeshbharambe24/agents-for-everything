"""Provider base classes and request/response structures."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ProviderConfig:
    """Configuration for a model provider."""

    name: str
    model: str
    api_key: str | None = None
    base_url: str | None = None
    timeout_seconds: float = 30.0


@dataclass(slots=True)
class CompletionRequest:
    """Normalized model completion request."""

    system_prompt: str
    user_payload: dict[str, Any]
    output_schema: dict[str, Any] | None = None
    temperature: float = 0.1
    max_tokens: int = 2048
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class CompletionResponse:
    """Normalized model completion response."""

    content: str
    parsed_json: dict[str, Any] | None = None
    model: str = "unknown"
    provider: str = "unknown"
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0


class BaseModelProvider(ABC):
    """Abstract base class implemented by all model providers."""

    def __init__(self, config: ProviderConfig) -> None:
        self.config = config

    @abstractmethod
    def complete(self, request: CompletionRequest) -> CompletionResponse:
        """Execute a completion request and return structured/text output."""
