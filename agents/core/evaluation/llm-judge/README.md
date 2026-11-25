# LLM Judge `evaluation/llm-judge`

beta · P0 · atomic · safety S0 · autonomy L1

## What it does
Evaluates agent outputs during CI regressions, prompt optimization, and quality gates.

## When to use / not use
- **Use when:** Automated grading of open-ended outputs against criteria.
- **Do not use when:** Exact deterministic JSON field equality checks.

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S0) and declared tool limits.
3. Executes core `evaluation/llm-judge` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add evaluation/llm-judge
afe test evaluation/llm-judge
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
Run `afe test evaluation/llm-judge` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
