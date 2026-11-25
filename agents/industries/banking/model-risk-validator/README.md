# AI Model Risk Validator `banking/model-risk-validator`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Checks AI/ML models for documentation, performance, fairness, drift and explainability under model-risk policy.

> **Important Safety Notice:** Financial compliance assistant; high-stakes KYC, AML, lending, fraud, and dispute actions require human officer review and approval.

## When to use / not use
- **Use when:** You need single-purpose ai model risk validator (model + data → validation report).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `banking/model-risk-validator` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add banking/model-risk-validator
afe test banking/model-risk-validator
```

## Composes with
documents/document-parser, guardrails/pii-redactor

## Tools required
afe/compliance-reg

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test banking/model-risk-validator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
