<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Scoped Filesystem MCP Server**

# 🧰 Scoped Filesystem MCP Server

![id: afe/filesystem](https://img.shields.io/badge/id-afe%2Ffilesystem-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Workspace-scoped file discovery, read, diff preview, and safe move/organize operations.

**Backed by:** modelcontextprotocol/servers (filesystem)

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `list_dir` | List files inside allowed workspace roots. | ✅ |
| `read_file` | Read file contents safely. | ✅ |
| `apply_plan` | Move or rename files according to an approved plan. |  |

## 🤖 Used by 25 agents

[`coding/bug-fixer`](../../agents/builders/coding/bug-fixer/README.md), [`coding/ci-fixer`](../../agents/builders/coding/ci-fixer/README.md), [`coding/code-generator`](../../agents/builders/coding/code-generator/README.md), [`coding/code-reviewer`](../../agents/builders/coding/code-reviewer/README.md), [`coding/codebase-qa`](../../agents/builders/coding/codebase-qa/README.md), [`coding/dependency-updater`](../../agents/builders/coding/dependency-updater/README.md), [`coding/doc-writer`](../../agents/builders/coding/doc-writer/README.md), [`coding/frontend-builder`](../../agents/builders/coding/frontend-builder/README.md), [`coding/refactorer`](../../agents/builders/coding/refactorer/README.md), [`coding/test-writer`](../../agents/builders/coding/test-writer/README.md), [`devops/log-analyzer`](../../agents/builders/devops/log-analyzer/README.md), [`documents/duplicate-finder`](../../agents/action/documents/duplicate-finder/README.md), [`documents/file-finder`](../../agents/action/documents/file-finder/README.md), [`documents/file-organizer`](../../agents/action/documents/file-organizer/README.md), [`documents/metadata-tagger`](../../agents/action/documents/metadata-tagger/README.md), [`operations/status-reporter`](../../agents/business/operations/status-reporter/README.md), [`orchestration/agent-builder`](../../agents/core/orchestration/agent-builder/README.md), [`personal/digital-declutterer`](../../agents/life/personal/digital-declutterer/README.md), [`personal/home-inventory`](../../agents/life/personal/home-inventory/README.md), [`personal/personal-doc-vault`](../../agents/life/personal/personal-doc-vault/README.md), [`personal/price-tracker`](../../agents/life/personal/price-tracker/README.md), [`productivity/journal-companion`](../../agents/life/productivity/journal-companion/README.md), [`security/secret-scanner`](../../agents/builders/security/secret-scanner/README.md), [`security/secure-code-reviewer`](../../agents/builders/security/secure-code-reviewer/README.md), [`security/vuln-triager`](../../agents/builders/security/vuln-triager/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
