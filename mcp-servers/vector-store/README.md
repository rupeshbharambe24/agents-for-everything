<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🧰 MCP servers](../../CATALOG.md#mcp-servers) › **Hybrid Vector Store MCP Server**

# 🧰 Hybrid Vector Store MCP Server

![id: afe/vector-store](https://img.shields.io/badge/id-afe%2Fvector--store-0f172a?style=flat-square) ![transport: stdio](https://img.shields.io/badge/transport-stdio-0d9488?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Hybrid keyword + semantic indexing and retrieval with metadata ACL filters.

**Backed by:** qdrant / chroma / pgvector MCP server

## 🔧 Tools

| Tool | Description | Read-only |
|---|---|:---:|
| `ingest` | Index chunked documents with metadata. |  |
| `query` | Retrieve ranked chunks matching query and filters. | ✅ |

## 🤖 Used by 31 agents

[`agriculture/agri-scheme-finder`](../../agents/industries/agriculture/agri-scheme-finder/README.md), [`ai-engineering/rag-builder`](../../agents/builders/ai-engineering/rag-builder/README.md), [`audio/audio-search`](../../agents/perception/audio/audio-search/README.md), [`banking/financial-literacy-guide`](../../agents/industries/banking/financial-literacy-guide/README.md), [`community/community-qa-bot`](../../agents/life/community/community-qa-bot/README.md), [`documents/archive-backup`](../../agents/action/documents/archive-backup/README.md), [`documents/file-finder`](../../agents/action/documents/file-finder/README.md), [`documents/long-doc-navigator`](../../agents/action/documents/long-doc-navigator/README.md), [`ecommerce/recommendation-agent`](../../agents/industries/ecommerce/recommendation-agent/README.md), [`government/citizen-services-assistant`](../../agents/industries/government/citizen-services-assistant/README.md), [`hospitality/hotel-concierge`](../../agents/industries/hospitality/hotel-concierge/README.md), [`hr/hr-policy-qa`](../../agents/business/hr/hr-policy-qa/README.md), [`hr/onboarding-buddy`](../../agents/business/hr/onboarding-buddy/README.md), [`insurance/policy-explainer`](../../agents/industries/insurance/policy-explainer/README.md), [`it-support/helpdesk-agent`](../../agents/builders/it-support/helpdesk-agent/README.md), [`manufacturing/maintenance-copilot`](../../agents/industries/manufacturing/maintenance-copilot/README.md), [`meetings/live-meeting-copilot`](../../agents/business/meetings/live-meeting-copilot/README.md), [`memory/knowledge-ingestor`](../../agents/core/memory/knowledge-ingestor/README.md), [`memory/memory-retriever`](../../agents/core/memory/memory-retriever/README.md), [`personal/personal-doc-vault`](../../agents/life/personal/personal-doc-vault/README.md), [`productivity/journal-companion`](../../agents/life/productivity/journal-companion/README.md), [`productivity/personal-knowledge-qa`](../../agents/life/productivity/personal-knowledge-qa/README.md), [`search/enterprise-search`](../../agents/information/search/enterprise-search/README.md), [`search/multimodal-search`](../../agents/information/search/multimodal-search/README.md), [`search/rag-qa`](../../agents/information/search/rag-qa/README.md), [`search/semantic-search`](../../agents/information/search/semantic-search/README.md), [`support/kb-writer`](../../agents/business/support/kb-writer/README.md), [`support/reply-drafter`](../../agents/business/support/reply-drafter/README.md), [`support/support-chatbot`](../../agents/business/support/support-chatbot/README.md), [`video/video-search`](../../agents/perception/video/video-search/README.md), [`vision/image-similarity`](../../agents/perception/vision/image-similarity/README.md)

Contract: [`server.yaml`](server.yaml)

<!-- afe:end-generated -->
