# Codebase Q&A `coding/codebase-qa`

beta · P0 · composite · safety S1 · autonomy L1

## What it does
Searches source files via semantic search and returns grounded answers citing file paths.

## When to use / not use
- **Use when:** Onboarding onto unfamiliar codebases or locating symbols.
- **Do not use when:** Editing code directly.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `coding/codebase-qa` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add coding/codebase-qa
afe test coding/codebase-qa
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/filesystem

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test coding/codebase-qa` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
