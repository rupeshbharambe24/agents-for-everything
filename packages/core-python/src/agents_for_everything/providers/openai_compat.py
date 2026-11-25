"""OpenAI and OpenAI-compatible HTTP provider (OpenAI, Groq, vLLM, OpenRouter, etc.)."""

from __future__ import annotations

import json
import os

from ._http import extract_json_object, post_json
from .base import BaseModelProvider, CompletionRequest, CompletionResponse, ProviderConfig


class OpenAICompatProvider(BaseModelProvider):
    """Calls Chat Completions endpoints compatible with the OpenAI API."""

    def __init__(self, config: ProviderConfig | None = None) -> None:
        cfg = config or ProviderConfig(
            name="openai",
            model=os.environ.get("AFE_MODEL", "gpt-4o-mini"),
            api_key=os.environ.get("OPENAI_API_KEY"),
            base_url=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        )
        super().__init__(cfg)

    def complete(self, request: CompletionRequest) -> CompletionResponse:
        if not self.config.api_key:
            raise RuntimeError("OPENAI_API_KEY is required for OpenAICompatProvider")
        base = (self.config.base_url or "https://api.openai.com/v1").rstrip("/")
        payload = {
            "model": self.config.model,
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
            "messages": [
                {"role": "system", "content": request.system_prompt},
                {"role": "user", "content": json.dumps(request.user_payload, ensure_ascii=False)},
            ],
        }
        if request.output_schema is not None:
            payload["response_format"] = {"type": "json_object"}
        data = post_json(
            f"{base}/chat/completions",
            payload,
            {"Authorization": f"Bearer {self.config.api_key}"},
            timeout_seconds=self.config.timeout_seconds,
        )
        text = data["choices"][0]["message"]["content"]
        usage = data.get("usage", {})
        return CompletionResponse(
            content=text,
            parsed_json=extract_json_object(text),
            model=self.config.model,
            provider=self.config.name,
            input_tokens=int(usage.get("prompt_tokens", 0)),
            output_tokens=int(usage.get("completion_tokens", 0)),
        )
