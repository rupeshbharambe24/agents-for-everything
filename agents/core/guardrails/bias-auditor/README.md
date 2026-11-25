# Bias Auditor `guardrails/bias-auditor`

prototype · P2 · composite · safety S0 · autonomy L1

## What it does
Tests outputs for unequal treatment using counterfactual inputs (swap names, gender, region).

## When to use / not use
- **Use when:** You need single-purpose bias auditor (agent + test set → bias report).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S0`) and declared MCP permissions.
3. Runs `guardrails/bias-auditor` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add guardrails/bias-auditor
afe test guardrails/bias-auditor
```

## Composes with
evaluation/llm-judge

## Tools required
None (pure computation / LLM reasoning)

## Safety
- Safety tier: `S0`
- Side effects: `[]`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test guardrails/bias-auditor` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
