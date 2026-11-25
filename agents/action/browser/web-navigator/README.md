# Browser Operator `browser/web-navigator`

beta · P0 · composite · safety S3 · autonomy L2

## What it does
Navigates web workflows step by step, screens page content for prompt injections, and stops before side effects.

## When to use / not use
- **Use when:** Multi-page interactive web workflows requiring navigation and confirmation.
- **Do not use when:** Simple read-only HTTP fetches.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `browser/web-navigator` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add browser/web-navigator
afe test browser/web-navigator
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/browser

## Safety
- Safety tier: `S3`
- Side effects: ['browser-interaction']
- Approval gates: ['submit', 'purchase']

## Evaluation
Run `afe test browser/web-navigator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
