# AML Alert Investigator `banking/aml-alert-investigator`

prototype · P1 · composite · safety S4 · autonomy L2

## What it does
Investigates transaction-monitoring alerts, compiles context, and drafts narrative summaries for AML analysts.

## When to use / not use
- **Use when:** Performing aml alert investigator tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S4) and declared MCP server permissions.
3. Executes `banking/aml-alert-investigator` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add banking/aml-alert-investigator
afe test banking/aml-alert-investigator
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/accounting

## Safety
- Safety tier: `S4`
- Side effects: ['banking-action']
- Approval gates: ['aml_analyst_signoff']

## Evaluation
Run `afe test banking/aml-alert-investigator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
