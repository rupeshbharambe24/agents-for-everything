# Voice-to-Form Filler `voice/voice-form-filler`

beta · P0 · composite · safety S2 · autonomy L2

## What it does
Lets users complete structured forms hands-free or in local languages by composing STT, structured extraction, verification, TTS prompts, and an approval gate.

## When to use / not use
- **Use when:** Hands-free or multilingual voice-to-form filling with strict validation.
- **Do not use when:** Submitting payments or legal filings without user read-back.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `voice/voice-form-filler` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add voice/voice-form-filler
afe test voice/voice-form-filler
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/stt

## Safety
- Safety tier: `S2`
- Side effects: ['fills-form-fields']
- Approval gates: ['submit']

## Evaluation
Run `afe test voice/voice-form-filler` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
