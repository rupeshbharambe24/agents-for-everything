<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Voice-Powered Form Filling**

# 🍳 Voice-Powered Form Filling

![recipe: voice-form-filling](https://img.shields.io/badge/recipe-voice--form--filling-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square)

> Speak naturally in any language to populate typed form fields, validate gaps, and confirm before submit.

| | |
|---|---|
| **Problem** | Long loan, intake, and government forms are slow on mobile and inaccessible for hands-free or local-language users. |
| **Solution** | Composes speech-to-text, pii-redactor, structured-extractor, verifier, text-to-speech, web-form-filler, and human-approval-gate. |

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`voice/speech-to-text`](../../agents/perception/voice/speech-to-text/README.md) | Batch or streaming speech recognition with punctuation, language detection, and code-switching. | S1 |
| [`voice/text-to-speech`](../../agents/perception/voice/text-to-speech/README.md) | Natural speech synthesis from text with locale, speed, and tone control. | S0 |
| [`voice/voice-form-filler`](../../agents/perception/voice/voice-form-filler/README.md) | Listens to natural speech, maps answers to typed form fields, checks gaps, and confirms before submit. | S2 |
| [`text/structured-extractor`](../../agents/information/text/structured-extractor/README.md) | Turns unstructured text or speech transcripts into normalized JSON matching a target schema. | S0 |
| [`orchestration/verifier`](../../agents/core/orchestration/verifier/README.md) | Checks outputs against required fields, formats, regex rules, and cross-field constraints. | S0 |
| [`orchestration/human-approval-gate`](../../agents/core/orchestration/human-approval-gate/README.md) | Pauses a workflow before risky steps, displays a clear summary/diff, and records approve/reject decisions. | S1 |
| [`guardrails/pii-redactor`](../../agents/core/guardrails/pii-redactor/README.md) | Detects and masks personal data (emails, phones, Aadhaar, PAN, SSN, card numbers) reversibly. | S0 |
| [`guardrails/prompt-injection-detector`](../../agents/core/guardrails/prompt-injection-detector/README.md) | Scans untrusted content (web pages, emails, files, speech transcripts) for hidden prompt-injection instructions. | S0 |
| [`browser/web-form-filler`](../../agents/action/browser/web-form-filler/README.md) | Populates web form fields from validated JSON and always stops before final submit for confirmation. | S2 |

**MCP servers:** [`afe/stt`](../../mcp-servers/stt/README.md), [`afe/tts`](../../mcp-servers/tts/README.md), [`afe/browser`](../../mcp-servers/browser/README.md)

<!-- afe:end-generated -->

## Architecture

`speech-to-text` -> `prompt-injection-detector` + `pii-redactor` (logs) -> `voice-form-filler` (`structured-extractor` + `verifier` + `text-to-speech`) -> `browser/web-form-filler` -> `orchestration/human-approval-gate`.

## Run Demo CLI or Web UI

```bash
# Run CLI multi-turn demo
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/voice-form-filling/app.py

# Run interactive local Web UI on http://127.0.0.1:8765
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/voice-form-filling/app.py --serve

# Run recipe integration test
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/voice-form-filling/tests/test_recipe.py
```
