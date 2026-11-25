# Text Extractor (OCR) `vision/ocr`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Converts document images and scanned receipts into clean text and structured layout lines.

## When to use / not use
- **Use when:** Reading scanned PDFs, receipts, whiteboards, and IDs.
- **Do not use when:** Already-digital text files.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `vision/ocr` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add vision/ocr
afe test vision/ocr
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/ocr

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test vision/ocr` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
