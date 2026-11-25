# Frontend Builder `coding/frontend-builder`

prototype · P1 · composite · safety S2 · autonomy L2

## What it does
Builds accessible UI components and pages from specs or design tokens.

## When to use / not use
- **Use when:** Performing frontend builder tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `coding/frontend-builder` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add coding/frontend-builder
afe test coding/frontend-builder
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/filesystem, afe/browser

## Safety
- Safety tier: `S2`
- Side effects: ['coding-action']
- Approval gates: ['none']

## Evaluation
Run `afe test coding/frontend-builder` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
