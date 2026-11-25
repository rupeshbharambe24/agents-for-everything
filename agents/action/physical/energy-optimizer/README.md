# Home/Building Energy Optimizer `physical/energy-optimizer`

prototype · P2 · atomic · safety S3 · autonomy L2

## What it does
Schedules appliances and HVAC to cut cost and carbon using tariffs and weather.

> **Important Safety Notice:** Physical/robotic safety assistant; confirm hazardous, irreversible, or actuator commands with a human operator and verify safety interlocks.

## When to use / not use
- **Use when:** You need single-purpose home/building energy optimizer (devices + tariffs → schedule).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S3`) and declared MCP permissions.
3. Runs `physical/energy-optimizer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add physical/energy-optimizer
afe test physical/energy-optimizer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/http

## Safety
- Safety tier: `S3`
- Side effects: `['external-action-requires-approval']`
- Approval gates: `['approve_external_action']`
- Handles PII: `True`

## Evaluation
Run `afe test physical/energy-optimizer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
