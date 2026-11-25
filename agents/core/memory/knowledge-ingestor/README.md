# Knowledge Ingestor `memory/knowledge-ingestor`

prototype · P0 · atomic · safety S2 · autonomy L2

## What it does
Splits raw documents into deterministic overlapping chunks with provenance IDs for RAG agents.

## When to use / not use
- **Use when:** Preparing manuals, PDFs, or wikis for search/rag-qa.
- **Do not use when:** Already-chunked short messages.

## How it works
1. Validates incoming JSON against `schemas/input.schema.json`.
2. Applies `SafetyPolicy` (S2) and declared tool limits.
3. Executes core `memory/knowledge-ingestor` logic (deterministic local checks plus live model synthesis when configured).
4. Validates structured output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add memory/knowledge-ingestor
afe test memory/knowledge-ingestor
```

## Composes with
- Upstream/Downstream: orchestration/router, orchestration/verifier

## Tools required
afe/vector-store, afe/documents

## Safety
- Level: `S2`
- Side effects: ['writes-vector-index']
- Approval required for: ['none']

## Evaluation
Run `afe test memory/knowledge-ingestor` to execute all 10 cases in `evals/cases.jsonl`.

## Limitations
Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
