"""End-to-end Voice-Powered Form Filling application."""

from __future__ import annotations

import argparse
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

RECIPE_DIR = Path(__file__).resolve().parent
REPO_ROOT = RECIPE_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "packages" / "core-python" / "src"))

from agents_for_everything import AgentRunner, RunContext  # noqa: E402


def process_voice_utterance(
    utterance: str,
    form_schema: dict[str, Any],
    prefill: dict[str, Any] | None = None,
    locale: str = "hi-IN",
    confirm_submit: bool = False,
    target_url: str = "https://forms.example.org/loan",
    provider_name: str = "auto",
) -> dict[str, Any]:
    """Process one voice utterance safely through guardrails, form filler, and browser adapter."""
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name, auto_approve=confirm_submit, locale=locale)

    inj = runner.run("guardrails/prompt-injection-detector", {"content": utterance}, context=ctx).output
    if not inj.get("is_safe", True):
        return {
            "values": prefill or {},
            "missing": [],
            "status": "blocked_injection",
            "prompt_back": "Unsafe instruction detected in audio transcript.",
            "safe_log": "[BLOCKED_INJECTION]",
        }

    redacted = runner.run("guardrails/pii-redactor", {"text": utterance}, context=ctx).output
    filled = runner.run(
        "voice/voice-form-filler",
        {
            "form": form_schema,
            "audio": {"format": "text-simulated", "transcript_hint": utterance, "locale_hint": locale},
            "locale": locale,
            "prefill": prefill or {},
            "confirm_submit": confirm_submit,
        },
        context=ctx,
    ).output

    browser_res = runner.run(
        "browser/web-form-filler",
        {"url": target_url, "fields": filled.get("values", {}), "submit": False},
        context=ctx,
    ).output

    return {
        "values": filled.get("values", {}),
        "missing": filled.get("missing", []),
        "invalid": filled.get("invalid", []),
        "status": filled.get("status"),
        "prompt_back": filled.get("prompt_back", ""),
        "safe_log": redacted.get("redacted_text", ""),
        "browser_fill": browser_res,
    }


def serve_demo(host: str = "127.0.0.1", port: int = 8765) -> None:
    form_schema = json.loads((RECIPE_DIR / "fixtures" / "loan_basic.json").read_text(encoding="utf-8"))
    ui_html = (RECIPE_DIR / "ui" / "index.html").read_text(encoding="utf-8")

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            if self.path == "/" or self.path == "/index.html":
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(ui_html.encode("utf-8"))
            elif self.path == "/api/schema":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(form_schema).encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()

        def do_POST(self) -> None:
            if self.path != "/api/fill":
                self.send_response(404)
                self.end_headers()
                return
            length = int(self.headers.get("Content-Length", "0"))
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            result = process_voice_utterance(
                utterance=str(body.get("utterance", "")),
                form_schema=form_schema,
                prefill=body.get("prefill") or {},
                locale=str(body.get("locale", "hi-IN")),
                confirm_submit=bool(body.get("confirm_submit", False)),
            )
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode("utf-8"))

        def log_message(self, format: str, *args: Any) -> None:
            return

    server = ThreadingHTTPServer((host, port), Handler)
    print(f"Voice Form Filling UI running at http://{host}:{port}")
    server.serve_forever()


def main() -> int:
    parser = argparse.ArgumentParser(description="Voice-Powered Form Filling Demo")
    parser.add_argument("--serve", action="store_true", help="Start local web UI server")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if args.serve:
        serve_demo(port=args.port)
        return 0

    schema = json.loads((RECIPE_DIR / "fixtures" / "loan_basic.json").read_text(encoding="utf-8"))
    turn1 = process_voice_utterance(
        "mera naam Priya Sharma hai, DOB 12 March 1990, PIN 411001, monthly income pachas hazaar",
        schema,
    )
    print("Turn 1:", json.dumps(turn1, indent=2, ensure_ascii=False))
    turn2 = process_voice_utterance(
        "my mobile number is 9876543210",
        schema,
        prefill=turn1["values"],
        confirm_submit=True,
    )
    print("Turn 2:", json.dumps(turn2, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
