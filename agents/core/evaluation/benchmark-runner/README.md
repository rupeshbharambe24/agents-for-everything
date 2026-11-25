# Benchmark Runner `evaluation/benchmark-runner`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Runs public benchmarks (tool use, web tasks, coding) against agents and publishes results.

## When to use / not use
- **Use when:** You need single-purpose benchmark runner (agent → benchmark scores).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `evaluation/benchmark-runner` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add evaluation/benchmark-runner
afe test evaluation/benchmark-runner
```

## Composes with
evaluation/llm-judge

## Tools required
afe/python-sandbox

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test evaluation/benchmark-runner` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
