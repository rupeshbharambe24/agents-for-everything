# Unsubscribe Cleaner `communication/unsubscribe-cleaner`

prototype · P2 · atomic · safety S3 · autonomy L2

## What it does
Finds unwanted mailing lists and unsubscribes after the user approves the list.

## When to use / not use
- **Use when:** You need single-purpose unsubscribe cleaner (inbox → list → unsubscribes).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S3`) and declared MCP permissions.
3. Runs `communication/unsubscribe-cleaner` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add communication/unsubscribe-cleaner
afe test communication/unsubscribe-cleaner
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/browser, afe/email

## Safety
- Safety tier: `S3`
- Side effects: `['external-action-requires-approval']`
- Approval gates: `['approve_external_action']`
- Handles PII: `True`

## Evaluation
Run `afe test communication/unsubscribe-cleaner` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
