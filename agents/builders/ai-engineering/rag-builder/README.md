# RAG Builder `ai-engineering/rag-builder`

prototype · P1 · composite · safety S2 · autonomy L2

## What it does
Configures chunking, hybrid retrieval, and reranking parameters tuned against eval recall.

## When to use / not use
- **Use when:** Performing rag builder tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `ai-engineering/rag-builder` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add ai-engineering/rag-builder
afe test ai-engineering/rag-builder
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/vector-store, afe/python-sandbox

## Safety
- Safety tier: `S2`
- Side effects: ['ai-engineering-action']
- Approval gates: ['none']

## Evaluation
Run `afe test ai-engineering/rag-builder` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
