"""Google Gemini REST API provider."""

from __future__ import annotations

import json
import os

from ._http import extract_json_object, post_json
from .base import BaseModelProvider, CompletionRequest, CompletionResponse, ProviderConfig


class GeminiProvider(BaseModelProvider):
    """Calls Gemini `generateContent` REST endpoint."""

    def __init__(self, config: ProviderConfig | None = None) -> None:
        cfg = config or ProviderConfig(
            name="gemini",
            model=os.environ.get("AFE_MODEL", "gemini-2.5-flash"),
            api_key=os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"),
            base_url=os.environ.get("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta"),
        )
        super().__init__(cfg)

    def complete(self, request: CompletionRequest) -> CompletionResponse:
        if not self.config.api_key:
            raise RuntimeError("GEMINI_API_KEY or GOOGLE_API_KEY is required for GeminiProvider")
        base = (self.config.base_url or "https://generativelanguage.googleapis.com/v1beta").rstrip("/")
        url = f"{base}/models/{self.config.model}:generateContent?key={self.config.api_key}"
        gen_cfg: dict[str, object] = {
            "temperature": request.temperature,
            "maxOutputTokens": request.max_tokens,
        }
        if request.output_schema is not None:
            gen_cfg["responseMimeType"] = "application/json"
        payload = {
            "systemInstruction": {"parts": [{"text": request.system_prompt}]},
            "contents": [
                {"role": "user", "parts": [{"text": json.dumps(request.user_payload, ensure_ascii=False)}]}
            ],
            "generationConfig": gen_cfg,
        }
        data = post_json(url, payload, {}, timeout_seconds=self.config.timeout_seconds)
        candidates = data.get("candidates", [])
        text = ""
        if candidates:
            parts = candidates[0].get("content", {}).get("parts", [])
            text = "".join(p.get("text", "") for p in parts)
        usage = data.get("usageMetadata", {})
        return CompletionResponse(
            content=text,
            parsed_json=extract_json_object(text),
            model=self.config.model,
            provider="gemini",
            input_tokens=int(usage.get("promptTokenCount", 0)),
            output_tokens=int(usage.get("candidatesTokenCount", 0)),
        )
