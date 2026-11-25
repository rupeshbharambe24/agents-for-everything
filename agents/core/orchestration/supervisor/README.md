# Supervisor / Orchestrator `orchestration/supervisor`

beta · P0 · composite · safety S1 · autonomy L3

## What it does
Coordinates multi-step agent execution across atomic workers declared in uses_agents.

## When to use / not use
- **Use when:** End-to-end orchestration of multi-step plans across worker agents.
- **Do not use when:** Simple single-agent calls.

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S1) and declared tool limits.
3. Executes core `orchestration/supervisor` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add orchestration/supervisor
afe test orchestration/supervisor
```

## Composes with
- Upstream/Downstream: orchestration/router, orchestration/verifier

## Tools required
None (pure computation or orchestrator)

## Safety
- Level: `S1`
- Side effects: ['none']
- Approval required for: ['none']

## Evaluation
Run `afe test orchestration/supervisor` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
