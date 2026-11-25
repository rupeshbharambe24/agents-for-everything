# Data Cleaner `data/data-cleaner`

prototype · P0 · atomic · safety S2 · autonomy L1

## What it does
Standardizes messy row records prior to analysis or database loading.

## When to use / not use
- **Use when:** Preparing dirty CSV/JSON records for analytics.
- **Do not use when:** Mutating production databases in place.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `data/data-cleaner` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add data/data-cleaner
afe test data/data-cleaner
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/python-sandbox

## Safety
- Safety tier: `S2`
- Side effects: ['cleans-dataset-copy']
- Approval gates: ['none']

## Evaluation
Run `afe test data/data-cleaner` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
