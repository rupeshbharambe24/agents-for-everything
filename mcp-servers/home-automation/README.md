<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Smart Home & Matter MCP Server**

# 🧰 Smart Home & Matter MCP Server

![id: afe/home-automation](https://img.shields.io/badge/id-afe%2Fhome--automation-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Query device states and trigger Home Assistant / Matter actions with lock confirmation.

**Backed by:** home-assistant / matter MCP server

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `get_states` | Read sensor and device states. | ✅ |
| `control_device` | Adjust lights, climate, or locks with safety gates. |  |

## 🤖 Used by 3 agents

[`physical/robot-task-planner`](../../agents/action/physical/robot-task-planner/README.md), [`physical/sensor-monitor`](../../agents/action/physical/sensor-monitor/README.md), [`physical/smart-home-controller`](../../agents/action/physical/smart-home-controller/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
