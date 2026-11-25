# Returns & Refunds Agent `support/returns-refunds-agent`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Checks return eligibility and prepares refunds; refunds need human approval.

## When to use / not use
- **Use when:** You need single-purpose returns & refunds agent (request → decision + prepared refund).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `support/returns-refunds-agent` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add support/returns-refunds-agent
afe test support/returns-refunds-agent
```

## Composes with
support/ticket-triager, search/rag-qa

## Tools required
afe/ticketing

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test support/returns-refunds-agent` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
