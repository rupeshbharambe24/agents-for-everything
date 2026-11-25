# KYC Onboarding Agent `banking/kyc-onboarding`

prototype · P1 · composite · safety S4 · autonomy L2

## What it does
Extracts and cross-checks KYC applicant records and flags mismatches for a human compliance officer.

## When to use / not use
- **Use when:** Performing kyc onboarding agent tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S4) and declared MCP server permissions.
3. Executes `banking/kyc-onboarding` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add banking/kyc-onboarding
afe test banking/kyc-onboarding
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/http

## Safety
- Safety tier: `S4`
- Side effects: ['banking-action']
- Approval gates: ['officer_kyc_signoff']

## Evaluation
Run `afe test banking/kyc-onboarding` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
