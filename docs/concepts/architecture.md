# Core Architecture

`agents-for-everything` organizes agentic capabilities into four composable tiers:

1. **Atomic Agents (`tier: atomic`)**: Execute one task with JSON Schema input/output and optional MCP tool calls.
2. **Composite Agents (`tier: composite`)**: Orchestrate 2+ atomic agents into a single user-facing contract (`uses_agents`).
3. **Teams (`teams/*.yaml`)**: Reusable multi-agent directed workflows with conditional routing and approval gates.
4. **Recipes (`recipes/*`)**: End-to-end runnable products combining agents, teams, MCP servers, and UI/CLI entrypoints.

All specifications are defined in [`spec/SPEC.md`](../../spec/SPEC.md).
