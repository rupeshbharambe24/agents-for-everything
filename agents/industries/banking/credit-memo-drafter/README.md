# Credit Appraisal Drafter `banking/credit-memo-drafter`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Analyzes financials and bureau data into a credit appraisal note for the credit officer.

> **Important Safety Notice:** Financial compliance assistant; high-stakes KYC, AML, lending, fraud, and dispute actions require human officer review and approval.

## When to use / not use
- **Use when:** You need single-purpose credit appraisal drafter (financials + bureau → memo draft).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `banking/credit-memo-drafter` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add banking/credit-memo-drafter
afe test banking/credit-memo-drafter
```

## Composes with
finance/financial-statement-analyzer, documents/document-parser

## Tools required
afe/git

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test banking/credit-memo-drafter` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
