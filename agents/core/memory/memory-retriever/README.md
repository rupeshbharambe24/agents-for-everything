# Memory Retriever `memory/memory-retriever`

prototype · P0 · atomic · safety S1 · autonomy L1

## What it does
Matches query terms against stored memory records and returns top-k ranked matches.

## When to use / not use
- **Use when:** Hydrating agent context from long-term user/project memory.
- **Do not use when:** Stateless S0 transformations.

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S1) and declared tool limits.
3. Executes core `memory/memory-retriever` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add memory/memory-retriever
afe test memory/memory-retriever
```

## Composes with
- Upstream/Downstream: orchestration/router, orchestration/verifier

## Tools required
afe/vector-store

## Safety
- Level: `S1`
- Side effects: ['none']
- Approval required for: ['none']

## Evaluation
Run `afe test memory/memory-retriever` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
