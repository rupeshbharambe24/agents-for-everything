# API Caller `integration/api-caller`

beta · P0 · atomic · safety S3 · autonomy L2

## What it does
Translates structured parameters into validated HTTP requests and gates mutating methods.

## When to use / not use
- **Use when:** Integrating external APIs cleanly through declared contracts.
- **Do not use when:** Unauthenticated scraping.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `integration/api-caller` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add integration/api-caller
afe test integration/api-caller
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/http

## Safety
- Safety tier: `S3`
- Side effects: ['external-api-call']
- Approval gates: ['write_request']

## Evaluation
Run `afe test integration/api-caller` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
