# Task Manager `productivity/task-manager`

prototype · P0 · composite · safety S2 · autonomy L1

## What it does
Composes action-item-extractor to prioritize tasks into actionable daily focus lists.

## When to use / not use
- **Use when:** Organizing messy personal or work inputs into prioritized daily tasks.
- **Do not use when:** Team-wide sprint planning in enterprise Jira.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `productivity/task-manager` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add productivity/task-manager
afe test productivity/task-manager
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/calendar

## Safety
- Safety tier: `S2`
- Side effects: ['updates-task-list']
- Approval gates: ['none']

## Evaluation
Run `afe test productivity/task-manager` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
