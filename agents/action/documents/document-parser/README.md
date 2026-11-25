# Document Parser `documents/document-parser`

prototype · P0 · atomic · safety S1 · autonomy L1

## What it does
Normalizes PDF/DOCX/HTML/scan inputs into clean Markdown and structured metadata.

## When to use / not use
- **Use when:** Preparing uploaded files for Q&A, extraction, or summarization.
- **Do not use when:** Already-clean Markdown strings.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `documents/document-parser` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add documents/document-parser
afe test documents/document-parser
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
Run `afe test documents/document-parser` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
