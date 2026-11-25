# Agents for Everything — Catalog

> Auto-generated from `agent.yaml`, `team.yaml`, `recipe.yaml`, and `server.yaml` manifests via `scripts/build_catalog.py`.

- **Agents:** 66
- **Teams:** 6
- **Recipes:** 3
- **MCP Servers:** 15
- **Direct Compatible Edges:** 20

## Agents

| ID | Name | Family / Category | Tier | Maturity | Priority | Safety | Summary |
|---|---|---|---|---|---|---|---|
| [`browser/web-form-filler`](agents/action/browser/web-form-filler/README.md) | Web Form Filler | `action/browser` | atomic | `prototype` | P0 | S2 | Populates web form fields from validated JSON and always stops before final submit for confirmation. |
| [`browser/web-navigator`](agents/action/browser/web-navigator/README.md) | Browser Operator | `action/browser` | composite | `prototype` | P0 | S3 | Completes multi-step web tasks safely using accessibility trees and screenshots with injection guards. |
| [`browser/web-scraper`](agents/action/browser/web-scraper/README.md) | Web Scraper | `action/browser` | atomic | `prototype` | P0 | S1 | Extracts structured records from public pages into JSON while respecting robots.txt and rate limits. |
| [`computer-use/shell-operator`](agents/action/computer-use/shell-operator/README.md) | Shell Operator | `action/computer-use` | atomic | `prototype` | P0 | S3 | Prepares and runs scoped terminal commands in a sandbox, requiring approval for state changes. |
| [`documents/document-parser`](agents/action/documents/document-parser/README.md) | Document Parser | `action/documents` | atomic | `prototype` | P0 | S1 | Converts rich documents and scans into clean Markdown with preserved headings and sections. |
| [`documents/file-organizer`](agents/action/documents/file-organizer/README.md) | File Organizer | `action/documents` | atomic | `prototype` | P0 | S2 | Classifies files by extension/topic and produces a dry-run move plan before touching disk. |
| [`documents/invoice-receipt-parser`](agents/action/documents/invoice-receipt-parser/README.md) | Invoice & Receipt Parser | `action/documents` | atomic | `prototype` | P0 | S1 | Extracts vendor, date, line items, GST/VAT tax, and total from invoices and verifies the math. |
| [`documents/spreadsheet-agent`](agents/action/documents/spreadsheet-agent/README.md) | Spreadsheet Agent | `action/documents` | atomic | `prototype` | P0 | S2 | Computes totals, averages, and filtered summaries across tabular spreadsheet data. |
| [`documents/table-extractor`](agents/action/documents/table-extractor/README.md) | Table Extractor | `action/documents` | atomic | `prototype` | P0 | S1 | Extracts Markdown, CSV, or raw text tables into structured row dictionaries. |
| [`integration/api-caller`](agents/action/integration/api-caller/README.md) | API Caller | `action/integration` | atomic | `prototype` | P0 | S3 | Prepares and invokes REST/GraphQL API requests from OpenAPI specs with approval for writes. |
| [`coding/bug-fixer`](agents/builders/coding/bug-fixer/README.md) | Bug Fixer | `builders/coding` | composite | `prototype` | P0 | S2 | Diagnoses bugs from stack traces, proposes a patch, adds regression tests, and verifies review. |
| [`coding/code-generator`](agents/builders/coding/code-generator/README.md) | Feature Implementer | `builders/coding` | composite | `prototype` | P0 | S2 | Implements scoped features from a spec and pairs them with unit tests. |
| [`coding/code-reviewer`](agents/builders/coding/code-reviewer/README.md) | Code Reviewer | `builders/coding` | atomic | `prototype` | P0 | S1 | Reviews code diffs for bugs, security risks, bare excepts, and maintainability issues. |
| [`coding/codebase-qa`](agents/builders/coding/codebase-qa/README.md) | Codebase Q&A | `builders/coding` | composite | `prototype` | P0 | S1 | Answers questions about a repository with exact file citations. |
| [`coding/test-writer`](agents/builders/coding/test-writer/README.md) | Test Writer | `builders/coding` | atomic | `prototype` | P0 | S2 | Generates targeted unit and edge-case tests for functions and APIs. |
| [`data/data-analyst`](agents/builders/data/data-analyst/README.md) | Data Analyst | `builders/data` | composite | `prototype` | P0 | S1 | Cleans datasets, computes descriptive statistics, and drafts plain-language insights. |
| [`data/data-cleaner`](agents/builders/data/data-cleaner/README.md) | Data Cleaner | `builders/data` | atomic | `prototype` | P0 | S2 | Trims strings, removes duplicates, and flags missing values with a deterministic change log. |
| [`data/text-to-sql`](agents/builders/data/text-to-sql/README.md) | Text-to-SQL | `builders/data` | atomic | `prototype` | P0 | S1 | Converts natural-language questions into safe read-only SELECT queries against a schema. |
| [`devops/log-analyzer`](agents/builders/devops/log-analyzer/README.md) | Log Analyzer | `builders/devops` | atomic | `prototype` | P0 | S1 | Clusters errors and warnings in application logs and highlights root causes. |
| [`communication/chat-summarizer`](agents/business/communication/chat-summarizer/README.md) | Chat Summarizer | `business/communication` | atomic | `prototype` | P0 | S1 | Summarizes Slack, Teams, WhatsApp, or Discord threads with decisions and open asks. |
| [`communication/email-drafter`](agents/business/communication/email-drafter/README.md) | Email Drafter | `business/communication` | atomic | `prototype` | P0 | S2 | Drafts context-matched email replies and saves them as drafts without sending autonomously. |
| [`communication/inbox-triager`](agents/business/communication/inbox-triager/README.md) | Inbox Triager | `business/communication` | atomic | `prototype` | P0 | S1 | Sorts, prioritizes, and labels emails; surfaces urgent threads and reply-needed items. |
| [`meetings/action-item-extractor`](agents/business/meetings/action-item-extractor/README.md) | Action Item Extractor | `business/meetings` | atomic | `prototype` | P0 | S2 | Pulls concrete tasks with owners and due dates from meeting notes, transcripts, or chats. |
| [`meetings/meeting-notetaker`](agents/business/meetings/meeting-notetaker/README.md) | Meeting Notetaker | `business/meetings` | composite | `prototype` | P0 | S1 | Transcribes meetings and produces structured summaries with decisions and risks. |
| [`meetings/meeting-scheduler`](agents/business/meetings/meeting-scheduler/README.md) | Meeting Scheduler | `business/meetings` | composite | `prototype` | P0 | S3 | Finds conflict-free meeting slots across calendars and prepares invites for approval. |
| [`support/reply-drafter`](agents/business/support/reply-drafter/README.md) | Reply Drafter | `business/support` | composite | `prototype` | P0 | S2 | Drafts KB-grounded support replies for human agents to review and send. |
| [`support/support-chatbot`](agents/business/support/support-chatbot/README.md) | Support Assistant | `business/support` | composite | `prototype` | P0 | S1 | Answers customer questions from KB docs with citations and flags handoffs when uncertain. |
| [`support/ticket-triager`](agents/business/support/ticket-triager/README.md) | Ticket Triager | `business/support` | atomic | `prototype` | P0 | S2 | Classifies, prioritizes, and routes incoming support tickets cleanly. |
| [`evaluation/llm-judge`](agents/core/evaluation/llm-judge/README.md) | LLM Judge | `core/evaluation` | atomic | `prototype` | P0 | S0 | Scores outputs against a rubric with calibrated, explained verdicts. |
| [`guardrails/content-moderator`](agents/core/guardrails/content-moderator/README.md) | Content Moderator | `core/guardrails` | atomic | `prototype` | P0 | S0 | Classifies text against configurable safety and policy categories. |
| [`guardrails/hallucination-checker`](agents/core/guardrails/hallucination-checker/README.md) | Grounding Checker | `core/guardrails` | atomic | `prototype` | P0 | S0 | Checks each claim in an answer against provided sources and flags unsupported statements. |
| [`guardrails/pii-redactor`](agents/core/guardrails/pii-redactor/README.md) | PII Redactor | `core/guardrails` | atomic | `prototype` | P0 | S0 | Detects and masks personal data (emails, phones, Aadhaar, PAN, SSN, card numbers) reversibly. |
| [`guardrails/prompt-injection-detector`](agents/core/guardrails/prompt-injection-detector/README.md) | Injection Detector | `core/guardrails` | atomic | `prototype` | P0 | S0 | Scans untrusted content (web pages, emails, files, speech transcripts) for hidden prompt-injection instructions. |
| [`memory/knowledge-ingestor`](agents/core/memory/knowledge-ingestor/README.md) | Knowledge Ingestor | `core/memory` | atomic | `prototype` | P0 | S2 | Parses, chunks, and prepares documents for hybrid keyword + vector indexing with metadata. |
| [`memory/memory-retriever`](agents/core/memory/memory-retriever/README.md) | Memory Retriever | `core/memory` | atomic | `prototype` | P0 | S1 | Recalls relevant memories for the current task, ranked and deduplicated. |
| [`memory/memory-writer`](agents/core/memory/memory-writer/README.md) | Memory Writer | `core/memory` | atomic | `prototype` | P0 | S2 | Extracts durable user preferences, facts, and decisions without creating duplicates. |
| [`orchestration/critic`](agents/core/orchestration/critic/README.md) | Critic / Reflector | `core/orchestration` | atomic | `prototype` | P0 | S0 | Reviews another agent's output against a rubric and returns specific, actionable fixes. |
| [`orchestration/human-approval-gate`](agents/core/orchestration/human-approval-gate/README.md) | Human-in-the-Loop Gate | `core/orchestration` | atomic | `prototype` | P0 | S1 | Pauses a workflow before risky steps, displays a clear summary/diff, and records approve/reject decisions. |
| [`orchestration/router`](agents/core/orchestration/router/README.md) | Intent Router | `core/orchestration` | atomic | `prototype` | P0 | S0 | Classifies a user request and selects the best matching agent or team with extracted arguments. |
| [`orchestration/supervisor`](agents/core/orchestration/supervisor/README.md) | Supervisor / Orchestrator | `core/orchestration` | composite | `prototype` | P0 | S1 | Executes a plan by delegating steps to worker agents, tracks state, and re-plans when a step fails. |
| [`orchestration/task-planner`](agents/core/orchestration/task-planner/README.md) | Task Planner | `core/orchestration` | atomic | `prototype` | P0 | S0 | Breaks a goal into ordered, dependency-aware steps with success criteria and estimated cost. |
| [`orchestration/verifier`](agents/core/orchestration/verifier/README.md) | Output Verifier | `core/orchestration` | atomic | `prototype` | P0 | S0 | Checks outputs against required fields, formats, regex rules, and cross-field constraints. |
| [`research/deep-researcher`](agents/information/research/deep-researcher/README.md) | Deep Researcher | `information/research` | composite | `prototype` | P0 | S1 | Plans research questions, searches iteratively, reads sources, fact-checks, and writes a cited report. |
| [`research/fact-checker`](agents/information/research/fact-checker/README.md) | Fact Checker | `information/research` | composite | `prototype` | P0 | S1 | Verifies discrete claims against web or retrieved sources and outputs verdicts with evidence. |
| [`research/report-writer`](agents/information/research/report-writer/README.md) | Report Writer | `information/research` | atomic | `prototype` | P0 | S0 | Turns research findings into structured Markdown reports with executive summaries and references. |
| [`research/source-reader`](agents/information/research/source-reader/README.md) | Source Reader | `information/research` | atomic | `prototype` | P0 | S1 | Reads one URL or document deeply and extracts key points, facts, and quotes. |
| [`search/answer-engine`](agents/information/search/answer-engine/README.md) | Answer Engine | `information/search` | composite | `prototype` | P0 | S1 | Searches web sources, reads content, and synthesizes a direct cited answer. |
| [`search/rag-qa`](agents/information/search/rag-qa/README.md) | Document Q&A | `information/search` | composite | `prototype` | P0 | S1 | Answers questions over private documents with citations and refuses when unsupported. |
| [`search/semantic-search`](agents/information/search/semantic-search/README.md) | Hybrid Searcher | `information/search` | atomic | `prototype` | P0 | S1 | Hybrid keyword + vector search over private document corpora with top-k ranking. |
| [`search/web-search`](agents/information/search/web-search/README.md) | Web Searcher | `information/search` | atomic | `prototype` | P0 | S1 | Runs queries on search APIs, deduplicates URLs, and ranks results with snippets. |
| [`text/classifier`](agents/information/text/classifier/README.md) | Text Classifier | `information/text` | atomic | `prototype` | P0 | S0 | Zero/few-shot classification of text into any custom label set with confidence. |
| [`text/entity-extractor`](agents/information/text/entity-extractor/README.md) | Entity Extractor | `information/text` | atomic | `prototype` | P0 | S0 | Extracts named entities (people, organizations, dates, amounts, emails) from unstructured text. |
| [`text/proofreader`](agents/information/text/proofreader/README.md) | Proofreader | `information/text` | atomic | `prototype` | P0 | S0 | Fixes whitespace, grammar, spelling, and consistency issues with tracked corrections. |
| [`text/rewriter`](agents/information/text/rewriter/README.md) | Rewriter | `information/text` | atomic | `prototype` | P0 | S0 | Adapts tone, length, reading level, or audience while preserving original facts. |
| [`text/structured-extractor`](agents/information/text/structured-extractor/README.md) | Structured Extractor | `information/text` | atomic | `prototype` | P0 | S0 | Turns unstructured text or speech transcripts into normalized JSON matching a target schema. |
| [`text/summarizer`](agents/information/text/summarizer/README.md) | Summarizer | `information/text` | atomic | `prototype` | P0 | S0 | Summarizes any length of content in a chosen style (TL;DR, bullets, executive) with key points. |
| [`text/translator`](agents/information/text/translator/README.md) | Translator | `information/text` | atomic | `prototype` | P0 | S0 | Context-aware translation preserving formatting and glossaries across 100+ languages including Indic. |
| [`productivity/task-manager`](agents/life/productivity/task-manager/README.md) | Task Manager | `life/productivity` | composite | `prototype` | P0 | S2 | Captures tasks from notes, chat, or voice, prioritizes them, and structures a daily plan. |
| [`vision/ocr`](agents/perception/vision/ocr/README.md) | Text Extractor (OCR) | `perception/vision` | atomic | `prototype` | P0 | S1 | Extracts printed and handwritten text with layout blocks from images and scans. |
| [`vision/screenshot-understander`](agents/perception/vision/screenshot-understander/README.md) | Screen Parser | `perception/vision` | atomic | `prototype` | P0 | S1 | Converts UI screenshots into a structured tree of buttons, inputs, and coordinates. |
| [`vision/visual-qa`](agents/perception/vision/visual-qa/README.md) | Visual Q&A | `perception/vision` | atomic | `prototype` | P0 | S1 | Answers targeted questions about any image or diagram. |
| [`voice/realtime-voice-assistant`](agents/perception/voice/realtime-voice-assistant/README.md) | Real-time Voice Assistant | `perception/voice` | composite | `prototype` | P0 | S1 | Full-duplex speech assistant with low latency, interruption handling, and tool dispatch. |
| [`voice/speech-to-text`](agents/perception/voice/speech-to-text/README.md) | Transcriber | `perception/voice` | atomic | `prototype` | P0 | S1 | Batch or streaming speech recognition with punctuation, language detection, and code-switching. |
| [`voice/text-to-speech`](agents/perception/voice/text-to-speech/README.md) | Narrator | `perception/voice` | atomic | `prototype` | P0 | S0 | Natural speech synthesis from text with locale, speed, and tone control. |
| [`voice/voice-command`](agents/perception/voice/voice-command/README.md) | Voice Command Interpreter | `perception/voice` | atomic | `prototype` | P0 | S1 | Maps spoken commands to structured app actions or function calls. |
| [`voice/voice-form-filler`](agents/perception/voice/voice-form-filler/README.md) | Voice-to-Form Filler | `perception/voice` | composite | `prototype` | P0 | S2 | Listens to natural speech, maps answers to typed form fields, checks gaps, and confirms before submit. |

## Teams

| ID | Name | Pattern | Maturity | Priority | Members | Summary |
|---|---|---|---|---|---|---|
| [`document-intake`](teams/document-intake/README.md) | Document Intake Team | prompt-chaining | `prototype` | P0 | 4 | Turns incoming raw documents into validated, human-approved structured records. |
| [`inbox-zero`](teams/inbox-zero/README.md) | Inbox Zero Team | prompt-chaining | `prototype` | P0 | 4 | Triages inbox emails, drafts replies, extracts action items, and waits for human approval. |
| [`meeting-to-done`](teams/meeting-to-done/README.md) | Meeting-to-Done Team | prompt-chaining | `prototype` | P0 | 3 | Converts meeting audio into structured notes, extracted action items, and prioritized tasks. |
| [`research-team`](teams/research-team/README.md) | Research Team | orchestrator-workers | `prototype` | P0 | 6 | Produces a cited, grounding-verified research report on any topic. |
| [`support-desk`](teams/support-desk/README.md) | Support Desk Team | routing | `prototype` | P0 | 4 | Triages customer tickets, retrieves KB answers, drafts replies, and gates risky escalations. |
| [`voice-concierge`](teams/voice-concierge/README.md) | Voice Concierge Team | routing | `prototype` | P0 | 4 | Voice in, intent routing and action execution, and spoken response out. |

## Recipes

| ID | Name | Maturity | Priority | Entrypoint | Summary |
|---|---|---|---|---|---|
| [`chat-with-your-docs`](recipes/chat-with-your-docs/README.md) | Chat with Your Docs | `prototype` | P0 | `app.py` | Private document Q&A assistant with PII masking, chunk ingestion, semantic retrieval, and grounding checks. |
| [`deep-research-app`](recipes/deep-research-app/README.md) | Deep Research App | `prototype` | P0 | `app.py` | Cited deep-research application running planning, web search, reading, fact-checking, and grounding verification. |
| [`voice-form-filling`](recipes/voice-form-filling/README.md) | Voice-Powered Form Filling | `prototype` | P0 | `app.py` | Speak naturally in any language to populate typed form fields, validate gaps, and confirm before submit. |

## MCP Servers

| ID | Name | Transport | Summary |
|---|---|---|---|
| [`afe/browser`](mcp-servers/browser/README.md) | Browser Automation MCP Server | `stdio` | Playwright-based browser navigation, accessibility-tree reading, and safe form filling. |
| [`afe/calendar`](mcp-servers/calendar/README.md) | Calendar Scheduling MCP Server | `stdio` | Query free/busy slots across time zones and propose meeting invites with confirmation. |
| [`afe/chat`](mcp-servers/chat/README.md) | Team Chat MCP Server | `stdio` | Read channels/threads and draft replies across Slack, Teams, Discord, or WhatsApp. |
| [`afe/documents`](mcp-servers/documents/README.md) | Documents MCP Server | `stdio` | Parse PDF, DOCX, PPTX, HTML, and spreadsheets into structured Markdown/tables. |
| [`afe/email`](mcp-servers/email/README.md) | Email Draft & Read MCP Server | `stdio` | Read inbox threads, apply labels, and create drafts without sending autonomously. |
| [`afe/filesystem`](mcp-servers/filesystem/README.md) | Scoped Filesystem MCP Server | `stdio` | Workspace-scoped file discovery, read, diff preview, and safe move/organize operations. |
| [`afe/http`](mcp-servers/http/README.md) | HTTP Fetch MCP Server | `stdio` | Fetch URLs and REST/GraphQL endpoints with robots.txt and rate-limit awareness. |
| [`afe/ocr`](mcp-servers/ocr/README.md) | OCR MCP Server | `stdio` | Printed and handwritten text extraction with layout bounding boxes. |
| [`afe/python-sandbox`](mcp-servers/python-sandbox/README.md) | Isolated Python Sandbox MCP Server | `stdio` | Sandboxed Python code execution for data analysis, cleaning, and verification. |
| [`afe/shell-sandbox`](mcp-servers/shell-sandbox/README.md) | Scoped Shell Sandbox MCP Server | `stdio` | Allowlisted terminal command execution with human confirmation for destructive actions. |
| [`afe/sql`](mcp-servers/sql/README.md) | Read-Only SQL MCP Server | `stdio` | Schema inspection and read-only SELECT execution across SQLite/Postgres/DuckDB. |
| [`afe/stt`](mcp-servers/stt/README.md) | Speech-to-Text MCP Server | `stdio` | Streaming and batch speech transcription with multilingual code-switching support. |
| [`afe/tts`](mcp-servers/tts/README.md) | Text-to-Speech MCP Server | `stdio` | Natural multilingual text-to-speech synthesis with SSML and pacing controls. |
| [`afe/vector-store`](mcp-servers/vector-store/README.md) | Hybrid Vector Store MCP Server | `stdio` | Hybrid keyword + semantic indexing and retrieval with metadata ACL filters. |
| [`afe/web-search`](mcp-servers/web-search/README.md) | Web Search MCP Server | `stdio` | Search web indexes and return ranked snippets and URLs. |
