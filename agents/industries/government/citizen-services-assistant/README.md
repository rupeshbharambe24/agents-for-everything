# Citizen Services Assistant `government/citizen-services-assistant`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Explains services, eligibility and required documents, by voice in local languages.

## When to use / not use
- **Use when:** You need single-purpose citizen services assistant (question → guidance).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `government/citizen-services-assistant` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add government/citizen-services-assistant
afe test government/citizen-services-assistant
```

## Composes with
search/rag-qa, voice/speech-to-text, voice/text-to-speech

## Tools required
afe/stt, afe/tts, afe/vector-store

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test government/citizen-services-assistant` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
