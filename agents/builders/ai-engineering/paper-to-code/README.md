# Paper Implementer `ai-engineering/paper-to-code`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Implements the method from an ML paper and reproduces a key result.

## When to use / not use
- **Use when:** You need single-purpose paper implementer (paper → code + results).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `ai-engineering/paper-to-code` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add ai-engineering/paper-to-code
afe test ai-engineering/paper-to-code
```

## Composes with
evaluation/llm-judge, search/rag-qa

## Tools required
afe/python-sandbox, afe/shell-sandbox

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test ai-engineering/paper-to-code` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
