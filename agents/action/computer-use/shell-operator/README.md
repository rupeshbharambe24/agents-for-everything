# Shell Operator `computer-use/shell-operator`

prototype · P0 · atomic · safety S3 · autonomy L2

## What it does
Translates operational intents into safe terminal commands with explainability and approval gating.

## When to use / not use
- **Use when:** Running safe build, test, or inspection commands.
- **Do not use when:** Unreviewed destructive `rm -rf` or privilege escalation.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `computer-use/shell-operator` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add computer-use/shell-operator
afe test computer-use/shell-operator
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/shell-sandbox

## Safety
- Safety tier: `S3`
- Side effects: ['runs-shell-command']
- Approval gates: ['execute_command', 'execute_destructive']

## Evaluation
Run `afe test computer-use/shell-operator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
