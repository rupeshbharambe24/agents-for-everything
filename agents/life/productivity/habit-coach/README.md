# Habit Coach `productivity/habit-coach`

prototype · P2 · atomic · safety S1 · autonomy L1

## What it does
Helps build habits with tracking, nudges and reflection.

## When to use / not use
- **Use when:** You need single-purpose habit coach (goals → plan + check-ins).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `productivity/habit-coach` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add productivity/habit-coach
afe test productivity/habit-coach
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/calendar

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test productivity/habit-coach` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
