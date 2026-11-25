# Technician Copilot `manufacturing/maintenance-copilot`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Hands-free voice Q&A over manuals and maintenance history for technicians.

## When to use / not use
- **Use when:** You need single-purpose technician copilot (question → steps).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `manufacturing/maintenance-copilot` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add manufacturing/maintenance-copilot
afe test manufacturing/maintenance-copilot
```

## Composes with
search/rag-qa, voice/speech-to-text, voice/text-to-speech

## Tools required
afe/stt, afe/tts, afe/vector-store

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test manufacturing/maintenance-copilot` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
