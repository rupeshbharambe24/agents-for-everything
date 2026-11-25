# Cash Flow Forecaster `finance/cash-flow-forecaster`

prototype · P2 · atomic · safety S1 · autonomy L1

## What it does
13-week cash forecast from receivables, payables and history.

> **Important Safety Notice:** Accounting/tax workflow assistant; does not provide regulated investment advice and requires human finance sign-off for ledger postings.

## When to use / not use
- **Use when:** You need single-purpose cash flow forecaster (ledgers → forecast).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `finance/cash-flow-forecaster` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add finance/cash-flow-forecaster
afe test finance/cash-flow-forecaster
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/python-sandbox, afe/shell-sandbox

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test finance/cash-flow-forecaster` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
