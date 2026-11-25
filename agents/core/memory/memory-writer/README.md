# Memory Writer `memory/memory-writer`

beta · P0 · atomic · safety S2 · autonomy L2

## What it does
Filters ephemeral noise and writes clean deduplicated memory records with consent.

## When to use / not use
- **Use when:** Persisting preferences or project decisions across sessions.
- **Do not use when:** Zero-retention confidential runs.

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S2) and declared tool limits.
3. Executes core `memory/memory-writer` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add memory/memory-writer
afe test memory/memory-writer
```

## Composes with
- Upstream/Downstream: orchestration/router, orchestration/verifier

## Tools required
None (pure computation or orchestrator)

## Safety
- Level: `S2`
- Side effects: ['writes-memory-store']
- Approval required for: ['none']

## Evaluation
Run `afe test memory/memory-writer` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
