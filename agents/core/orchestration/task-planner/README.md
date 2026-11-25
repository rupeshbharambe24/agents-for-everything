# Task Planner `orchestration/task-planner`

beta · P0 · atomic · safety S0 · autonomy L1

## What it does
Decomposes complex multi-step goals into an acyclic execution plan (DAG) of atomic agent calls.

## When to use / not use
- **Use when:** Planning multi-step workflows before calling execution agents.
- **Do not use when:** Single-step atomic transformations.

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S0) and declared tool limits.
3. Executes core `orchestration/task-planner` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add orchestration/task-planner
afe test orchestration/task-planner
```

## Composes with
- Upstream/Downstream: orchestration/router, orchestration/verifier

## Tools required
None (pure computation or orchestrator)

## Safety
- Level: `S0`
- Side effects: ['none']
- Approval required for: ['none']

## Evaluation
Run `afe test orchestration/task-planner` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
