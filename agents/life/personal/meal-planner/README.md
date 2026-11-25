# Meal Planner `personal/meal-planner`

prototype · P2 · composite · safety S0 · autonomy L1

## What it does
Weekly meal plans and grocery lists by diet, budget and pantry.

## When to use / not use
- **Use when:** You need single-purpose meal planner (preferences → plan + list).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S0`) and declared MCP permissions.
3. Runs `personal/meal-planner` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add personal/meal-planner
afe test personal/meal-planner
```

## Composes with
text/structured-extractor, search/web-search

## Tools required
None (pure computation / LLM reasoning)

## Safety
- Safety tier: `S0`
- Side effects: `[]`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test personal/meal-planner` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
