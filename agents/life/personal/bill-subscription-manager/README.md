# Bills & Subscriptions Manager `personal/bill-subscription-manager`

prototype · P1 · atomic · safety S1 · autonomy L1

## What it does
Tracks recurring bills and subscriptions, flags due dates, and guides cancellation steps.

## When to use / not use
- **Use when:** Performing bills & subscriptions manager tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `personal/bill-subscription-manager` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add personal/bill-subscription-manager
afe test personal/bill-subscription-manager
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/email

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test personal/bill-subscription-manager` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
