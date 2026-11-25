# Drone Mission Planner `physical/drone-mission-planner`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Plans survey and inspection flights within airspace rules.

> **Important Safety Notice:** Physical/robotic safety assistant; confirm hazardous, irreversible, or actuator commands with a human operator and verify safety interlocks.

## When to use / not use
- **Use when:** You need single-purpose drone mission planner (area + goal → flight plan).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `physical/drone-mission-planner` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add physical/drone-mission-planner
afe test physical/drone-mission-planner
```

## Composes with
orchestration/human-approval-gate

## Tools required
afe/maps

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test physical/drone-mission-planner` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
