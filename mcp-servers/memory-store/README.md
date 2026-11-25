<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Long-Term Memory Store MCP Server**

# 🧰 Long-Term Memory Store MCP Server

![id: afe/memory-store](https://img.shields.io/badge/id-afe%2Fmemory--store-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Persist and query episodic memories and knowledge graph triples with consent controls.

**Backed by:** modelcontextprotocol/servers (memory)

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `read_memories` | Query stored user/session memories. | ✅ |
| `write_memory` | Store deduplicated memory record. |  |

## 🤖 Used by 6 agents

[`gaming/game-tester`](../../agents/industries/gaming/game-tester/README.md), [`memory/entity-resolver`](../../agents/core/memory/entity-resolver/README.md), [`memory/knowledge-graph-builder`](../../agents/core/memory/knowledge-graph-builder/README.md), [`memory/memory-gardener`](../../agents/core/memory/memory-gardener/README.md), [`memory/profile-builder`](../../agents/core/memory/profile-builder/README.md), [`memory/session-summarizer`](../../agents/core/memory/session-summarizer/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
