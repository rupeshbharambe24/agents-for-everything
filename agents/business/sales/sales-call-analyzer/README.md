# Sales Call Analyzer `sales/sales-call-analyzer`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Summarizes calls, extracts objections and next steps, gives coaching tips.

## When to use / not use
- **Use when:** You need single-purpose sales call analyzer (call → analysis).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `sales/sales-call-analyzer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add sales/sales-call-analyzer
afe test sales/sales-call-analyzer
```

## Composes with
voice/speech-to-text, sales/account-researcher

## Tools required
afe/stt

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test sales/sales-call-analyzer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
