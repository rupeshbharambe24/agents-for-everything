# Feature Implementer `coding/code-generator`

prototype · P0 · composite · safety S2 · autonomy L1

## What it does
Composes spec implementation and test-writer verification following repo conventions.

## When to use / not use
- **Use when:** Implementing well-specified feature changes inside a repository.
- **Do not use when:** Ambiguous product requests without specs.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `coding/code-generator` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add coding/code-generator
afe test coding/code-generator
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/filesystem, afe/shell-sandbox

## Safety
- Safety tier: `S2`
- Side effects: ['writes-code']
- Approval gates: ['none']

## Evaluation
Run `afe test coding/code-generator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
