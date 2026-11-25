# Test Writer `coding/test-writer`

prototype · P0 · atomic · safety S2 · autonomy L1

## What it does
Writes clean unit tests verifying happy paths, boundary cases, and error paths.

## When to use / not use
- **Use when:** Adding regression and unit tests for existing or newly generated code.
- **Do not use when:** Running production database migrations.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `coding/test-writer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add coding/test-writer
afe test coding/test-writer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/filesystem, afe/shell-sandbox

## Safety
- Safety tier: `S2`
- Side effects: ['writes-test-files']
- Approval gates: ['none']

## Evaluation
Run `afe test coding/test-writer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
