# Writing a New Agent

1. Scaffold the folder:
   ```bash
   afe new --tier atomic --category <category> --slug <agent-slug>
   ```
2. Complete `agent.yaml`, `schemas/input.schema.json`, and `schemas/output.schema.json`.
3. Write clear operational rules in `prompts/system.md`.
4. Add a reference implementation in `impl/python/agent.py` (optional if generic LLM execution suffices).
5. Add >= 10 eval cases in `evals/cases.jsonl` (normal, edge, adversarial, and multilingual where applicable).
6. Run `afe validate` and `afe test <category>/<agent-slug>`, then regenerate `CATALOG.md` via `python3 scripts/build_catalog.py`.
