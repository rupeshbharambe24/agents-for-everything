# Performance Optimizer `coding/performance-optimizer`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Profiles code and optimizes hot paths with benchmarks.

## When to use / not use
- **Use when:** You need single-purpose performance optimizer (code + benchmark → diff + results).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `coding/performance-optimizer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add coding/performance-optimizer
afe test coding/performance-optimizer
```

## Composes with
coding/code-generator, coding/code-reviewer

## Tools required
afe/shell-sandbox

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `False`

## Evaluation
Run `afe test coding/performance-optimizer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
