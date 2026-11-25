# Fraud Signal Explainer `banking/fraud-signal-explainer`

prototype · P1 · composite · safety S4 · autonomy L2

## What it does
Explains transaction risk signals and flags mule/scam indicators for human fraud analysts.

## When to use / not use
- **Use when:** Performing fraud signal explainer tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S4) and declared MCP server permissions.
3. Executes `banking/fraud-signal-explainer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add banking/fraud-signal-explainer
afe test banking/fraud-signal-explainer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/policy-engine

## Safety
- Safety tier: `S4`
- Side effects: ['banking-action']
- Approval gates: ['fraud_analyst_review']

## Evaluation
Run `afe test banking/fraud-signal-explainer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
