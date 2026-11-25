# CRM Updater `sales/crm-updater`

prototype · P1 · atomic · safety S3 · autonomy L2

## What it does
Extracts call/meeting takeaways into structured CRM field updates gated by approval.

## When to use / not use
- **Use when:** Performing crm updater tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `sales/crm-updater` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add sales/crm-updater
afe test sales/crm-updater
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/crm

## Safety
- Safety tier: `S3`
- Side effects: ['sales-action']
- Approval gates: ['commit_crm_update']

## Evaluation
Run `afe test sales/crm-updater` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
