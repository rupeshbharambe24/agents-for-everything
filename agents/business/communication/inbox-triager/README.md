# Inbox Triager `communication/inbox-triager`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Triage incoming email batches by urgency and actionability without sending replies.

## When to use / not use
- **Use when:** Morning inbox triage and priority ranking.
- **Do not use when:** Deleting or sending emails autonomously.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `communication/inbox-triager` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add communication/inbox-triager
afe test communication/inbox-triager
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
Run `afe test communication/inbox-triager` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
