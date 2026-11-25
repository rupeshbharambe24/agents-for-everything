# Critic / Reflector `orchestration/critic`

beta · P0 · atomic · safety S0 · autonomy L1

## What it does
Provides structured self-critique and revision instructions in evaluator-optimizer loops.

## When to use / not use
- **Use when:** Improving drafts of reports, emails, code, or translations before delivery.
- **Do not use when:** Hard schema validation (use orchestration/verifier instead).

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S0) and declared tool limits.
3. Executes core `orchestration/critic` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add orchestration/critic
afe test orchestration/critic
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
Run `afe test orchestration/critic` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
