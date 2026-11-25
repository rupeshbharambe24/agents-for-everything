# ID Document Reader `vision/id-document-reader`

prototype · P1 · atomic · safety S4 · autonomy L2

## What it does
Extracts identity card fields for consented KYC workflows with quality checks.

## When to use / not use
- **Use when:** Performing id document reader tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S4) and declared MCP server permissions.
3. Executes `vision/id-document-reader` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add vision/id-document-reader
afe test vision/id-document-reader
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/ocr

## Safety
- Safety tier: `S4`
- Side effects: ['vision-action']
- Approval gates: ['verified_user_consent']

## Evaluation
Run `afe test vision/id-document-reader` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
