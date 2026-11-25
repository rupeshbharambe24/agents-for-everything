# Scam Message Checker `banking/scam-message-checker`

prototype · P2 · atomic · safety S1 · autonomy L1

## What it does
Consumers forward a suspicious SMS, call script or payment request and get a risk verdict with what to do.

> **Important Safety Notice:** Financial compliance assistant; high-stakes KYC, AML, lending, fraud, and dispute actions require human officer review and approval.

## When to use / not use
- **Use when:** You need single-purpose scam message checker (message → verdict + advice).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `banking/scam-message-checker` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add banking/scam-message-checker
afe test banking/scam-message-checker
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/compliance-reg

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test banking/scam-message-checker` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
