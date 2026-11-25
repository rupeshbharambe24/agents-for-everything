# Transcriber `voice/speech-to-text`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Converts audio streams or files into clean Transcript JSON across English and Indic/global languages.

## When to use / not use
- **Use when:** Transcribing spoken audio or voice utterances into normalized text.
- **Do not use when:** Already-transcribed plain text.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `voice/speech-to-text` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add voice/speech-to-text
afe test voice/speech-to-text
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/stt

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test voice/speech-to-text` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
