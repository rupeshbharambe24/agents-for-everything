# `afe/v2` Specification — Agents for Everything

`afe/v2` extends [`afe/v1`](../SPEC.md) with first-class ecosystem discovery, verification provenance, deployment profile bindings, and lifecycle deprecation metadata while keeping full backward compatibility with `afe/v1` tools, schemas, and runtimes.

## What Is New in `afe/v2`

| Field | Location | Purpose |
|---|---|---|
| `spec.a2a` | `agent.yaml` | Declares A2A protocol transports (`http+json`, `stdio`, `in-process`), `streaming`, and `state_transition_history`. |
| `spec.verification` | `agent.yaml` | Records verification badge status (`verified` / `community` / `unverified`), `safety_reviewed`, and `on_prem_ready`. |
| `spec.deployments` | `agent.yaml` | Lists validated local/on-prem or edge profiles (e.g. `profiles/regulated-airgapped.yaml`). |
| `spec.deprecation` | `agent.yaml` | Marks deprecated agents with `replaced_by` matching [`registry/aliases.yaml`](../../registry/aliases.yaml). |

## Migrating from `afe/v1` to `afe/v2`

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli migrate voice/voice-form-filler --out ./migrated
```

Both `afe/v1` and `afe/v2` manifests pass `afe validate` and `afe verify`. See [ADR 0005](../../docs/adr/0005-spec-v2-evolution.md) for rationale.
