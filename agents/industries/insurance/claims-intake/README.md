# Claims Intake (FNOL) `insurance/claims-intake`

prototype · P2 · composite · safety S3 · autonomy L2

## What it does
Takes first notice of loss by chat or voice with photos and documents into a complete claim file.

> **Important Safety Notice:** Insurance workflow assistant; claims, coverage, and underwriting outputs require licensed adjuster/underwriter verification.

## When to use / not use
- **Use when:** You need single-purpose claims intake (fnol) (report → claim file).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S3`) and declared MCP permissions.
3. Runs `insurance/claims-intake` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add insurance/claims-intake
afe test insurance/claims-intake
```

## Composes with
voice/voice-form-filler, documents/document-parser

## Tools required
afe/documents

## Safety
- Safety tier: `S3`
- Side effects: `['external-action-requires-approval']`
- Approval gates: `['approve_external_action']`
- Handles PII: `True`

## Evaluation
Run `afe test insurance/claims-intake` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
