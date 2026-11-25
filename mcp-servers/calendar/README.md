<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Calendar Scheduling MCP Server**

# 🧰 Calendar Scheduling MCP Server

![id: afe/calendar](https://img.shields.io/badge/id-afe%2Fcalendar-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Query free/busy slots across time zones and propose meeting invites with confirmation.

**Backed by:** google-calendar / caldav MCP server

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `find_free_slots` | Compute overlapping availability windows. | ✅ |
| `create_event_draft` | Prepare calendar invite awaiting approval. |  |

## 🤖 Used by 17 agents

[`community/event-organizer`](../../agents/life/community/event-organizer/README.md), [`community/volunteer-coordinator`](../../agents/life/community/volunteer-coordinator/README.md), [`education/study-planner`](../../agents/life/education/study-planner/README.md), [`healthcare/appointment-manager`](../../agents/industries/healthcare/appointment-manager/README.md), [`hr/interview-scheduler`](../../agents/business/hr/interview-scheduler/README.md), [`legal/obligation-tracker`](../../agents/business/legal/obligation-tracker/README.md), [`meetings/calendar-optimizer`](../../agents/business/meetings/calendar-optimizer/README.md), [`meetings/meeting-prep`](../../agents/business/meetings/meeting-prep/README.md), [`meetings/meeting-scheduler`](../../agents/business/meetings/meeting-scheduler/README.md), [`personal/parenting-helper`](../../agents/life/personal/parenting-helper/README.md), [`personal/pet-care-helper`](../../agents/life/personal/pet-care-helper/README.md), [`productivity/daily-briefer`](../../agents/life/productivity/daily-briefer/README.md), [`productivity/focus-guardian`](../../agents/life/productivity/focus-guardian/README.md), [`productivity/habit-coach`](../../agents/life/productivity/habit-coach/README.md), [`productivity/reminder-agent`](../../agents/life/productivity/reminder-agent/README.md), [`productivity/task-manager`](../../agents/life/productivity/task-manager/README.md), [`sales/inbound-qualifier`](../../agents/business/sales/inbound-qualifier/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
