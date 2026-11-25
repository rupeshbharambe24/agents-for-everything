# Follow-up Tracker `communication/follow-up-tracker`

prototype · P1 · atomic · safety S2 · autonomy L2

## What it does
Tracks sent email threads awaiting replies and prepares polite follow-up drafts.

## When to use / not use
- **Use when:** Performing follow-up tracker tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `communication/follow-up-tracker` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add communication/follow-up-tracker
afe test communication/follow-up-tracker
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/email

## Safety
- Safety tier: `S2`
- Side effects: ['communication-action']
- Approval gates: ['none']

## Evaluation
Run `afe test communication/follow-up-tracker` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
