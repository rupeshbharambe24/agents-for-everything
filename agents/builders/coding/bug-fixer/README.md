# Bug Fixer `coding/bug-fixer`

beta · P0 · composite · safety S2 · autonomy L1

## What it does
Coordinates root-cause diagnosis, test creation, and diff review into a verified patch.

## When to use / not use
- **Use when:** Fixing reproducible bugs with stack traces or failing assertions.
- **Do not use when:** Greenfield architecture rewrites.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `coding/bug-fixer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add coding/bug-fixer
afe test coding/bug-fixer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/filesystem, afe/shell-sandbox

## Safety
- Safety tier: `S2`
- Side effects: ['patches-code']
- Approval gates: ['none']

## Evaluation
Run `afe test coding/bug-fixer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
