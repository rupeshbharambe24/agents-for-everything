# Accounts Payable Agent `finance/accounts-payable`

prototype · P1 · composite · safety S4 · autonomy L2

## What it does
Matches parsed invoices against PO/receipt totals and prepares an approval queue (no autonomous payment).

## When to use / not use
- **Use when:** Performing accounts payable agent tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S4) and declared MCP server permissions.
3. Executes `finance/accounts-payable` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add finance/accounts-payable
afe test finance/accounts-payable
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/accounting

## Safety
- Safety tier: `S4`
- Side effects: ['finance-action']
- Approval gates: ['approve_payment_batch']

## Evaluation
Run `afe test finance/accounts-payable` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
