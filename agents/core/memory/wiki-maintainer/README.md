# Wiki Maintainer `memory/wiki-maintainer`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Keeps an internal wiki current: finds stale pages, drafts updates from new sources.

## When to use / not use
- **Use when:** You need single-purpose wiki maintainer (wiki + sources → edit proposals).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `memory/wiki-maintainer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add memory/wiki-maintainer
afe test memory/wiki-maintainer
```

## Composes with
memory/knowledge-ingestor, text/summarizer

## Tools required
afe/documents

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test memory/wiki-maintainer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
