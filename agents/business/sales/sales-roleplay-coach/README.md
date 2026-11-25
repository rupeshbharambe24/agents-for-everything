# Sales Roleplay Coach `sales/sales-roleplay-coach`

prototype · P2 · atomic · safety S0 · autonomy L1

## What it does
Simulates buyers for practice and scores the conversation.

## When to use / not use
- **Use when:** You need single-purpose sales roleplay coach (scenario → roleplay + feedback).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S0`) and declared MCP permissions.
3. Runs `sales/sales-roleplay-coach` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add sales/sales-roleplay-coach
afe test sales/sales-roleplay-coach
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
None (pure computation / LLM reasoning)

## Safety
- Safety tier: `S0`
- Side effects: `[]`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test sales/sales-roleplay-coach` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
