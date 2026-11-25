# Action Item Extractor `meetings/action-item-extractor`

prototype · P0 · atomic · safety S2 · autonomy L1

## What it does
Transforms unstructured notes into schema-valid Task arrays.

## When to use / not use
- **Use when:** Turning meeting notes or chats into trackable tasks.
- **Do not use when:** Summarizing high-level discussions without tasks.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `meetings/action-item-extractor` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add meetings/action-item-extractor
afe test meetings/action-item-extractor
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/documents

## Safety
- Safety tier: `S2`
- Side effects: ['creates-task-drafts']
- Approval gates: ['none']

## Evaluation
Run `afe test meetings/action-item-extractor` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
