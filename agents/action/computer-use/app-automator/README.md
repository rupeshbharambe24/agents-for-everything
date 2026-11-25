# App Automator `computer-use/app-automator`

prototype · P1 · atomic · safety S3 · autonomy L2

## What it does
Automates desktop apps cleanly using OS accessibility APIs (AppleScript, UI Automation, AT-SPI).

## When to use / not use
- **Use when:** Performing app automator tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `computer-use/app-automator` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add computer-use/app-automator
afe test computer-use/app-automator
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/shell-sandbox

## Safety
- Safety tier: `S3`
- Side effects: ['computer-use-action']
- Approval gates: ['execute_app_script']

## Evaluation
Run `afe test computer-use/app-automator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
