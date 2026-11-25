# Route Optimizer `supply-chain/route-optimizer`

prototype · P2 · atomic · safety S1 · autonomy L1

## What it does
Plans delivery routes with time windows and capacity.

## When to use / not use
- **Use when:** You need single-purpose route optimizer (stops + fleet → routes).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `supply-chain/route-optimizer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add supply-chain/route-optimizer
afe test supply-chain/route-optimizer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/logistics, afe/python-sandbox

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test supply-chain/route-optimizer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
