## Summary

Describe the agent, team, recipe, or runtime change in this PR.

## Checklist

- [ ] `python3 scripts/validate_repo.py` passes cleanly
- [ ] `PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli test --all` passes
- [ ] `agent.yaml` validates against `spec/agent.schema.json` and ID is unique
- [ ] Eval cases (`evals/cases.jsonl`) include normal, edge, and adversarial tests
- [ ] Safety level (`S0`–`S4`) and `approval_required_for` gates are accurate
- [ ] No API keys, secrets, or prohibited uses (`SECURITY.md`)
- [ ] Signed off under Apache-2.0 / DCO (`git commit -s`)
