# Web Form Filler `browser/web-form-filler`

prototype · P0 · atomic · safety S2 · autonomy L2

## What it does
Bridges extracted field dictionaries into target browser DOM forms safely.

## When to use / not use
- **Use when:** Filling web forms after structured extraction and verification.
- **Do not use when:** Submitting forms autonomously without human review.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `browser/web-form-filler` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add browser/web-form-filler
afe test browser/web-form-filler
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/browser

## Safety
- Safety tier: `S2`
- Side effects: ['fills-web-inputs']
- Approval gates: ['submit']

## Evaluation
Run `afe test browser/web-form-filler` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
