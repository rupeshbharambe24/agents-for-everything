# Structured Extractor `text/structured-extractor`

beta · P0 · atomic · safety S0 · autonomy L1

## What it does
Extracts names, ISO dates, PIN codes, emails, phones, and multilingual numbers (e.g. 'pachas hazaar' -> 50000) into typed fields.

## When to use / not use
- **Use when:** Converting free text or voice transcripts into strict JSON records or form fields.
- **Do not use when:** Prose summarization.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S0) and declared MCP server permissions.
3. Executes `text/structured-extractor` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add text/structured-extractor
afe test text/structured-extractor
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
None

## Safety
- Safety tier: `S0`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test text/structured-extractor` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
