# Memory Gardener `memory/memory-gardener`

prototype · P2 · atomic · safety S2 · autonomy L2

## What it does
Consolidates, expires and resolves contradictions in long-term memory.

## When to use / not use
- **Use when:** You need single-purpose memory gardener (memory store → cleaned store).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `memory/memory-gardener` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add memory/memory-gardener
afe test memory/memory-gardener
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/memory-store

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test memory/memory-gardener` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
