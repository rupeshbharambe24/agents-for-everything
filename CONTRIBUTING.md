# Contributing to Agents for Everything

Thank you for helping build the open, composable library of AI agents!

## Quick Workflow: Adding or Improving an Agent

1. **Check for duplicates** in `CATALOG.md` or run:
   ```bash
   afe search "<your task>"
   ```
2. **Scaffold from the official template**:
   ```bash
   afe new --tier atomic --category <category> --slug <agent-slug>
   ```
3. **Complete the contract first**:
   - Fill `agent.yaml` (unique `<category>/<slug>` ID, capabilities, tools, safety level `S0`–`S4`, autonomy `L0`–`L4`).
   - Define strict `schemas/input.schema.json` and `schemas/output.schema.json` using shared `afe://types/*` schemas where applicable.
   - Write clear instructions in `prompts/system.md`.
   - Document behavior and limitations honestly in `README.md` (following the standard template).
4. **Implement & Test**:
   - Add a clean implementation in `impl/python/agent.py` (using `agents-for-everything` core primitives).
   - Add **at least 10 eval cases** in `evals/cases.jsonl` covering normal cases, edge cases, adversarial/prompt-injection inputs, and non-English / multilingual inputs where applicable.
5. **Validate, Verify Badge & Regenerate Catalog**:
   ```bash
   afe validate
   afe test <category>/<agent-slug>
   afe verify <category>/<agent-slug>
   python3 scripts/build_catalog.py
   ```
6. **Optional — Upgrade Manifest to `afe/v2`**:
   ```bash
   afe migrate <category>/<agent-slug> --in-place
   ```

## PR Checklist

- [ ] `agent.yaml` validates against `spec/agent.schema.json`; ID is unique and kebab-case
- [ ] Input/output schemas reuse shared types in `spec/types/` where possible
- [ ] `README.md` states purpose, I/O, safety controls, and honest limitations
- [ ] `evals/cases.jsonl` includes normal, edge, and adversarial cases (>= 10 cases for `prototype`)
- [ ] Safety level (`S0`–`S4`) and `approval_required_for` gates are set conservatively
- [ ] No hardcoded API keys or vendor-locked code outside `impl/adapters/`
- [ ] Complies with the Prohibited Uses policy in [SECURITY.md](SECURITY.md)

## Licensing & Sign-Off

All contributions are licensed under **Apache-2.0**. Contributors certify their right to contribute under the Developer Certificate of Origin (`git commit -s`).
