# Log Analyzer `devops/log-analyzer`

prototype · P0 · atomic · safety S1 · autonomy L1

## What it does
Groups noisy log streams by error signature and counts occurrences.

## When to use / not use
- **Use when:** Triaging failing jobs, server logs, or incident bursts.
- **Do not use when:** Executing cluster rollbacks directly.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `devops/log-analyzer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add devops/log-analyzer
afe test devops/log-analyzer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/filesystem

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test devops/log-analyzer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
