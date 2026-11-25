# Live Interpreter `voice/live-interpreter`

prototype · P1 · composite · safety S1 · autonomy L1

## What it does
Two-way real-time speech translation across languages.

## When to use / not use
- **Use when:** Performing live interpreter tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `voice/live-interpreter` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add voice/live-interpreter
afe test voice/live-interpreter
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/stt, afe/tts

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test voice/live-interpreter` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
