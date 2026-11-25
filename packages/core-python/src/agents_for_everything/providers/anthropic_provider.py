"""Anthropic Messages API provider."""

from __future__ import annotations

import json
import os

from ._http import extract_json_object, post_json
from .base import BaseModelProvider, CompletionRequest, CompletionResponse, ProviderConfig


class AnthropicProvider(BaseModelProvider):
    """Calls Anthropic's `/v1/messages` API."""

    def __init__(self, config: ProviderConfig | None = None) -> None:
        cfg = config or ProviderConfig(
            name="anthropic",
            model=os.environ.get("AFE_MODEL", "claude-sonnet-4-5"),
            api_key=os.environ.get("ANTHROPIC_API_KEY"),
            base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com"),
        )
        super().__init__(cfg)

    def complete(self, request: CompletionRequest) -> CompletionResponse:
        if not self.config.api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is required for AnthropicProvider")
        base = (self.config.base_url or "https://api.anthropic.com").rstrip("/")
        user_msg = json.dumps(request.user_payload, ensure_ascii=False)
        if request.output_schema is not None:
            user_msg = f"{user_msg}\n\nReturn valid JSON matching schema:\n{json.dumps(request.output_schema)}"
        payload = {
            "model": self.config.model,
            "max_tokens": request.max_tokens,
            "temperature": request.temperature,
            "system": request.system_prompt,
            "messages": [{"role": "user", "content": user_msg}],
        }
        data = post_json(
            f"{base}/v1/messages",
            payload,
            {
                "x-api-key": self.config.api_key,
                "anthropic-version": "2023-06-01",
            },
            timeout_seconds=self.config.timeout_seconds,
        )
        text = "".join(part.get("text", "") for part in data.get("content", []))
        usage = data.get("usage", {})
        return CompletionResponse(
            content=text,
            parsed_json=extract_json_object(text),
            model=self.config.model,
            provider="anthropic",
            input_tokens=int(usage.get("input_tokens", 0)),
            output_tokens=int(usage.get("output_tokens", 0)),
        )
