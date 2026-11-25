# Narrator `voice/text-to-speech`

beta · P0 · atomic · safety S0 · autonomy L1

## What it does
Synthesizes spoken responses, read-backs, and multilingual confirmations from text.

## When to use / not use
- **Use when:** Reading responses, confirmations, or missing-field prompts aloud.
- **Do not use when:** Text-only headless pipelines.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S0) and declared MCP server permissions.
3. Executes `voice/text-to-speech` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add voice/text-to-speech
afe test voice/text-to-speech
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/tts

## Safety
- Safety tier: `S0`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test voice/text-to-speech` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
