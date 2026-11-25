# ADR 0003: Mandatory Safety & Autonomy Tiers (`S0`–`S4`, `L0`–`L4`)

## Status
Accepted

## Context
Reusable agents deployed across personal, enterprise, and regulated environments require uniform, enforceable safety boundaries.

## Decision
Every agent declares both a safety impact tier (`S0`–`S4`) and an autonomy tier (`L0`–`L4`) in `agent.yaml`. `SafetyPolicy` enforces declared tool scopes, `max_steps`/`timeout`/`max_cost_usd` budgets, and mandatory human-in-the-loop approval gates for `S3`/`S4` actions.
