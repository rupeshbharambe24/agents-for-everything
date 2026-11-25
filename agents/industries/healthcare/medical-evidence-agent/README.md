# Medical Evidence Summarizer `healthcare/medical-evidence-agent`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Evidence summaries from guidelines and literature with citations.

> **Important Safety Notice:** Clinical workflow aid for licensed professionals only; outputs are unapproved drafts requiring clinician review and never replace medical judgement.

## When to use / not use
- **Use when:** You need single-purpose medical evidence summarizer (clinical question → summary).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `healthcare/medical-evidence-agent` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add healthcare/medical-evidence-agent
afe test healthcare/medical-evidence-agent
```

## Composes with
search/academic-search, voice/speech-to-text

## Tools required
afe/web-search

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `True`

## Evaluation
Run `afe test healthcare/medical-evidence-agent` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
