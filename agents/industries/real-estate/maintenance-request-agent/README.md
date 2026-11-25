# Maintenance Request Agent `real-estate/maintenance-request-agent`

prototype · P2 · composite · safety S3 · autonomy L2

## What it does
Triage of tenant requests with photos and dispatch to vendors.

## When to use / not use
- **Use when:** You need single-purpose maintenance request agent (request → work order).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S3`) and declared MCP permissions.
3. Runs `real-estate/maintenance-request-agent` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add real-estate/maintenance-request-agent
afe test real-estate/maintenance-request-agent
```

## Composes with
documents/document-parser, vision/ocr

## Tools required
afe/ticketing

## Safety
- Safety tier: `S3`
- Side effects: `['external-action-requires-approval']`
- Approval gates: `['approve_external_action']`
- Handles PII: `True`

## Evaluation
Run `afe test real-estate/maintenance-request-agent` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
