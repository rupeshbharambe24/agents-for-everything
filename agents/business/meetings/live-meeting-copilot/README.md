# Live Meeting Copilot `meetings/live-meeting-copilot`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Answers questions and fetches facts during a meeting, privately to the user.

## When to use / not use
- **Use when:** You need single-purpose live meeting copilot (live transcript → suggestions).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `meetings/live-meeting-copilot` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add meetings/live-meeting-copilot
afe test meetings/live-meeting-copilot
```

## Composes with
search/rag-qa, voice/speech-to-text

## Tools required
afe/stt, afe/vector-store

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test meetings/live-meeting-copilot` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
