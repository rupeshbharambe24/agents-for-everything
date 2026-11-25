# Table Extractor `documents/table-extractor`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Converts tabular text inside documents or PDFs into clean JSON row arrays.

## When to use / not use
- **Use when:** Pulling line-item tables from PDFs, reports, or Markdown files.
- **Do not use when:** Unstructured prose paragraphs.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `documents/table-extractor` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add documents/table-extractor
afe test documents/table-extractor
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/documents, afe/ocr

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test documents/table-extractor` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
