# Voice-Powered Form Filling (`recipe/voice-form-filling`)

Speak naturally (including Hinglish / Indic languages) to populate structured form fields, validate formats, ask for missing fields by voice, populate web forms, and confirm with a human-in-the-loop gate before submission.

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
