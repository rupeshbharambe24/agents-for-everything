# Trip Planner `travel/trip-planner`

prototype · P1 · composite · safety S1 · autonomy L1

## What it does
Builds day-by-day travel itineraries aligned with budget, pace, transit time, and interests.

## When to use / not use
- **Use when:** Performing trip planner tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `travel/trip-planner` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add travel/trip-planner
afe test travel/trip-planner
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/web-search, afe/maps

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test travel/trip-planner` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
