# `afe/web-search`

MCP server contract for web search queries, deduplication, and ranked snippet retrieval.
Backed in-process by `LocalMCPRegistry` for offline testing, and designed to bind to Brave Search, SearXNG, or Tavily MCP servers in production.
