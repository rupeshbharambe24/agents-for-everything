# Order Fraud Screener `ecommerce/order-fraud-screener`

prototype · P2 · atomic · safety S4 · autonomy L2

## What it does
Scores orders for fraud risk with reasons for manual review.

## When to use / not use
- **Use when:** You need single-purpose order fraud screener (order → risk + reasons).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `ecommerce/order-fraud-screener` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add ecommerce/order-fraud-screener
afe test ecommerce/order-fraud-screener
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/http

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test ecommerce/order-fraud-screener` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
