# Code Reviewer `coding/code-reviewer`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Flags concrete defects like hardcoded secrets, eval/exec, SQL string interpolation, and missing error handling.

## When to use / not use
- **Use when:** Automated PR and diff review before merge.
- **Do not use when:** Writing net-new code.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `coding/code-reviewer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add coding/code-reviewer
afe test coding/code-reviewer
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
Run `afe test coding/code-reviewer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
