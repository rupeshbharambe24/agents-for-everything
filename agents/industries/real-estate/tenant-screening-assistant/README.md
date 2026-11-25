# Tenant Screening Assistant `real-estate/tenant-screening-assistant`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Applies the landlord's written, fair-housing-compliant criteria and documents reasons; human decides.

## When to use / not use
- **Use when:** You need single-purpose tenant screening assistant (application + criteria → assessment).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `real-estate/tenant-screening-assistant` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add real-estate/tenant-screening-assistant
afe test real-estate/tenant-screening-assistant
```

## Composes with
documents/document-parser, vision/ocr

## Tools required
afe/documents

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test real-estate/tenant-screening-assistant` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
