# Desktop Operator `computer-use/desktop-operator`

prototype · P1 · composite · safety S3 · autonomy L2

## What it does
Operates native desktop apps via screenshots, mouse, and keyboard with approval gates.

## When to use / not use
- **Use when:** Performing desktop operator tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `computer-use/desktop-operator` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add computer-use/desktop-operator
afe test computer-use/desktop-operator
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/browser

## Safety
- Safety tier: `S3`
- Side effects: ['computer-use-action']
- Approval gates: ['execute_gui_action']

## Evaluation
Run `afe test computer-use/desktop-operator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
