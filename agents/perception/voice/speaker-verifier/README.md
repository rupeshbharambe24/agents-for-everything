# Speaker Verifier `voice/speaker-verifier`

prototype · P2 · atomic · safety S4 · autonomy L2

## What it does
Consent-based speaker verification with anti-spoofing and synthetic-voice detection.

## When to use / not use
- **Use when:** You need single-purpose speaker verifier (audio + enrolled print → match + liveness).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `voice/speaker-verifier` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add voice/speaker-verifier
afe test voice/speaker-verifier
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/observability

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test voice/speaker-verifier` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
