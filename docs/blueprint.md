# Agents for Everything — Master Blueprint

> **The open, reusable, composable library of AI agents: one agent for every real-world task. Pick the ones you need, combine them like building blocks, ship your product.**

| | |
|---|---|
| **Repository** | `agents-for-everything` |
| **Packages** | `agents-for-everything` (PyPI) · `@agents-for-everything/core` (npm) |
| **CLI** | `agents-for-everything`, with the short alias `afe` |
| **Spec prefix** | `afe` (used only in schema IDs, e.g. `afe/v1`; not a public brand) |
| **Document** | Master blueprint: research, full agent catalog, spec standard, repo structure, roadmap |
| **Version** | 0.1 (draft) |
| **Date** | 25 November 2026 |
| **License (proposed)** | Apache-2.0 |

---

## Table of contents

1. [Vision and scope](#1-vision-and-scope)
2. [Research: the agent landscape (Nov 2026)](#2-research-the-agent-landscape-nov-2026)
3. [Design principles](#3-design-principles)
4. [Agent anatomy and the spec standard](#4-agent-anatomy-and-the-spec-standard)
5. [Repository structure](#5-repository-structure)
6. [Catalog overview](#6-catalog-overview)
7. [The full agent catalog](#7-the-full-agent-catalog)
8. [Teams: ready-made multi-agent compositions](#8-teams-ready-made-multi-agent-compositions)
9. [Recipes: end-to-end product blueprints](#9-recipes-end-to-end-product-blueprints)
10. [Reference spec: a fully worked agent](#10-reference-spec-a-fully-worked-agent)
11. [Build roadmap](#11-build-roadmap)
12. [Governance, contribution and safety policy](#12-governance-contribution-and-safety-policy)
13. [Staying current with the agent ecosystem](#13-staying-current-with-the-agent-ecosystem)
14. [Appendix: glossary, templates, sources](#14-appendix)

---

## 1. Vision and scope

### 1.1 Mission

Build the largest open repository of **production-grade, single-purpose AI agents** that anyone can pick up and reuse. Every agent does one job well, has a typed input and output, declares the tools it needs, states its safety level, and ships with tests. Agents combine into **teams** (multi-agent workflows) and teams combine into **recipes** (whole products).

Example: someone building a voice-driven loan application form takes `voice/speech-to-text` + `text/structured-extractor` + `browser/web-form-filler` + `orchestration/human-approval-gate`, or simply takes the ready-made `voice/voice-form-filler`, which composes them already.

### 1.2 What counts as an "agent" in this repo

An agent is a **packaged unit of autonomous work**:

```
Agent = Instructions (prompt)
      + Model requirements (capabilities, not a vendor)
      + Tool contracts (MCP servers it needs)
      + Typed I/O (JSON Schema in, JSON Schema out)
      + Control loop (pattern: ReAct, plan-execute, etc.)
      + Guardrails (safety level, approvals, limits)
      + Evals (test cases + metrics)
      + Docs (README, examples)
```

If something has no decision-making loop and just wraps an API, it is a **tool** (it lives in `mcp-servers/`), not an agent.

### 1.3 Scope

| In scope | Out of scope |
|---|---|
| Single-task ("atomic") agents for every common human and business task | A new agent framework competing with LangGraph, CrewAI, etc. |
| Composite agents and teams built from atomic agents | A link list ("awesome-list") of other people's projects |
| Framework-agnostic specs plus reference implementations | Lock-in to one model vendor |
| Shared tools as MCP servers | Hosting or running agents as a paid service |
| Evals, safety metadata, docs for every agent | Agents for harmful uses (see §12.4) |

### 1.4 How this differs from what already exists

| Existing type | Examples | Gap we fill |
|---|---|---|
| Awesome-lists | `kyrolabs/awesome-agents`, `e2b` agent list | Links, not reusable components |
| Prompt and persona collections | `agency-agents` (~230 role prompts for coding tools) | Mostly prompts, no typed I/O, no tests, few runnable tools |
| Skill catalogs | Agent Skills collections for Claude/Codex | Tied to coding assistants; no composition contracts |
| Framework examples | LangGraph, CrewAI, ADK cookbooks | Tied to one framework; examples, not maintained products |
| Tutorial repos | "500 AI agent projects" style lists | One-off demos, not composable |

**Our differentiators:** one standard spec for every agent; typed contracts so agents snap together; runnable in several frameworks through adapters; every agent has evals and a safety level; exportable as an MCP server, an A2A agent, an Agent Skill and a coding-assistant subagent.

---

## 2. Research: the agent landscape (Nov 2026)

### 2.1 What makes something an agent

Every agent, from a simple classifier loop to a computer-using assistant, has five parts:

| Part | Question it answers | Examples |
|---|---|---|
| **Perceive** | What is the input? | Text, voice, image, video, screen, files, events, sensors |
| **Reason / plan** | What should I do next? | LLM reasoning, planning, routing, reflection |
| **Act** | How do I change the world? | Tool/API calls, clicks, typing, file writes, messages |
| **Remember** | What do I know? | Context window, session state, long-term memory, knowledge base |
| **Learn / verify** | Did it work? | Self-checks, evaluators, human feedback, tests |

### 2.2 Ways to classify agents

These axes are recorded in every agent's metadata so the catalog can be filtered on them.

| Axis | Values |
|---|---|
| **Scope (tier)** | Atomic (one task) → Composite (orchestrates atomic agents) → Team (multi-agent workflow) → Recipe (product) |
| **Autonomy** | L0 suggest only · L1 human executes · L2 acts with per-action approval · L3 acts within policy, escalates exceptions · L4 fully autonomous in a sandbox |
| **Modality** | Text · Voice · Vision · Video · GUI/screen · API · Physical (IoT/robotics) |
| **Runtime** | Interactive (chat/voice) · Background/ambient · Scheduled (cron) · Event-driven (webhooks) · Streaming/real-time |
| **Environment** | Digital-API · Browser · Desktop/OS · Mobile · Physical world |
| **Classic AI type** | Simple reflex · Model-based · Goal-based · Utility-based · Learning (Russell & Norvig) |
| **Audience** | Consumer · Professional · Enterprise · Developer · Industry-specific |

### 2.3 Architecture patterns

Every agent declares one primary pattern. These are the patterns in common use today:

| Pattern | How it works | Best for |
|---|---|---|
| **Augmented LLM** | Single call with tools and retrieval | Simple atomic tasks |
| **Prompt chaining** | Fixed sequence of steps, each checked | Predictable pipelines (extract → validate → format) |
| **Routing** | Classify input, send to a specialist | Support desks, intent handling |
| **Parallelization** | Split work or vote across several runs | Speed, robustness, guardrails |
| **Orchestrator–workers** | Lead agent plans and delegates subtasks | Research, coding, complex projects |
| **Evaluator–optimizer** | Generate, critique, revise in a loop | Writing, translation, code |
| **ReAct** | Think → act → observe loop | Tool use with unknown number of steps |
| **Plan-and-execute** | Plan upfront, execute, re-plan on failure | Long tasks, cost control |
| **Reflection / self-critique** | Agent reviews and corrects its own output | Quality-sensitive outputs |
| **Hierarchical / supervisor** | Managers supervise worker agents | Large teams |
| **Handoff / swarm** | Agents transfer control to each other | Conversational multi-skill systems |
| **Debate / consensus** | Several agents argue, a judge decides | High-stakes judgments |
| **Blackboard** | Agents share a common workspace | Open-ended collaborative problems |
| **Human-in-the-loop** | Pauses for approval at defined points | Anything with side effects |

### 2.4 Interoperability standards to build on

The protocol stack has largely settled. We adopt open standards instead of inventing our own:

| Layer | Standard | Use in this repo |
|---|---|---|
| Agent ↔ tools/data | **MCP (Model Context Protocol)**, now under the Linux Foundation's Agentic AI Foundation | All shared tools are MCP servers; every agent can also be exposed *as* an MCP server |
| Agent ↔ agent | **A2A (Agent2Agent)** with Agent Cards; ACP as an alternative | Every agent publishes an Agent Card; teams can span processes and vendors |
| Packaged know-how | **Agent Skills** (`SKILL.md` folders) | Every agent exports as a Skill for Claude, Codex and other assistants |
| Repo instructions | **AGENTS.md** | Instructions for coding agents that contribute to this repo |
| Agent ↔ UI | **AG-UI**, A2UI | Streaming events to front-ends in recipes |
| Browser ↔ agent | **WebMCP** (emerging) | Browser agents prefer site-declared tools over DOM scraping when present |
| Observability | **OpenTelemetry GenAI semantic conventions** | Standard traces for every run |
| Schemas | **JSON Schema 2020-12** | All inputs/outputs |

*Versions and adoption figures change quickly. Recheck each standard's official repo before pinning (see §13).*

### 2.5 Frameworks to support through adapters

The core spec is framework-neutral. Reference implementations target the most used SDKs:

| Priority | Framework | Language |
|---|---|---|
| 1 | Claude Agent SDK | Python, TypeScript |
| 1 | OpenAI Agents SDK | Python, TypeScript |
| 1 | LangGraph | Python, TypeScript |
| 2 | Google ADK | Python, Java, Go |
| 2 | Microsoft Agent Framework (successor of AutoGen + Semantic Kernel) | Python, .NET |
| 2 | CrewAI | Python |
| 3 | Pydantic AI, LlamaIndex, Mastra, smolagents, Agno, DSPy | Various |

A plain, dependency-light Python and TypeScript runtime (`packages/core-*`) is always provided so an agent works without any framework.

### 2.6 The universal task map: what people actually do

The research question was: *what are all the tasks people do?* Almost every real task is a combination of **eight verbs**. The catalog was built by crossing these verbs with every domain of work and life.

| Verb family | Primitive actions | Example agents |
|---|---|---|
| **Perceive** | Listen, see, read, watch, sense | speech-to-text, ocr, screenshot-understander, sensor-monitor |
| **Understand** | Classify, extract, summarize, translate, compare | classifier, structured-extractor, summarizer, translator |
| **Find** | Search, retrieve, browse, monitor | web-search, rag-qa, page-change-monitor, news-monitor |
| **Think** | Plan, reason, analyze, decide, critique | task-planner, data-analyst, critic, decision-analyst |
| **Create** | Write, draw, code, compose, design | blog-writer, image-generator, code-generator, music-composer |
| **Act** | Click, type, fill, call API, move files, send, schedule | web-form-filler, desktop-operator, file-organizer, meeting-scheduler |
| **Coordinate** | Route, delegate, hand off, remember, track | router, supervisor, memory-writer, project-manager |
| **Guard** | Verify, redact, approve, moderate, audit | verifier, pii-redactor, human-approval-gate, audit-logger |

Your starting list (browsing, voice, searching, researching, accessing files, changing things, running tasks) maps onto these: browsing = Find + Act; voice = Perceive + Create; searching/researching = Find + Think; accessing and changing files = Act; running tasks = Coordinate + Act.

### 2.7 Where agents are being used (demand signals)

Coding and software delivery, customer support, research and analysis, document processing (invoices, contracts, KYC), sales prospecting, IT and security operations, meeting and email productivity, voice agents for call centres, browser and computer-use automation, and vertical agents in finance, healthcare, legal and government. The catalog gives these areas the most depth.

---

## 3. Design principles

1. **One agent, one job.** If the description needs "and", consider splitting it. Composite agents exist to combine.
2. **Contracts first.** Every agent has a JSON Schema for input and output. Agents compose only through contracts.
3. **Framework-agnostic spec, many implementations.** The `agent.yaml` is the source of truth; code is an implementation of it.
4. **Model-agnostic.** Agents declare required *capabilities* (tool use, vision, audio, long context), never a single vendor.
5. **Tools are MCP servers.** No agent embeds private API glue that others can't reuse.
6. **Safe by default.** Every agent has a safety level; side effects need approval unless explicitly configured otherwise.
7. **Tested or it doesn't ship.** No agent reaches `beta` without an eval suite and a passing CI run.
8. **Copy-in or install.** Users can install a package *or* copy a single agent's folder into their project (`afe add voice/speech-to-text`).
9. **Local-first option.** Where possible, each agent lists an open-weights/local configuration so it can run offline or on-prem (important for banks, government and healthcare).
10. **Multilingual by design.** Text and voice agents are tested on non-English inputs, including Indic languages.
11. **Observable.** Every run emits OpenTelemetry traces.
12. **Documentation is the product.** A good README is worth more than clever code.

---

## 4. Agent anatomy and the spec standard

### 4.1 Folder for a single agent

```
agents/<family>/<category>/<agent-slug>/
├── agent.yaml                 # Manifest: the single source of truth (spec below)
├── README.md                  # Human docs: purpose, usage, examples, limits
├── prompts/
│   ├── system.md              # System prompt / instructions
│   └── fragments/             # Reusable prompt parts (few-shot examples, rubrics)
├── schemas/
│   ├── input.schema.json      # JSON Schema for input
│   └── output.schema.json     # JSON Schema for output
├── tools.yaml                 # MCP servers + tool permissions this agent needs
├── impl/
│   ├── python/                # Reference implementation (core runtime)
│   │   ├── agent.py
│   │   └── pyproject.toml
│   ├── typescript/
│   │   ├── agent.ts
│   │   └── package.json
│   └── adapters/              # Optional framework-specific wiring
│       ├── langgraph.py
│       ├── openai_agents.py
│       └── claude_agent_sdk.py
├── evals/
│   ├── cases.jsonl            # Test inputs + expected outputs/rubrics
│   ├── rubric.md              # How outputs are judged
│   └── eval.yaml              # Metrics and pass thresholds
├── examples/
│   ├── basic.md
│   └── sample-inputs/
└── CHANGELOG.md
```

Generated at release (not hand-written): `agent-card.json` (A2A), `SKILL.md` export, MCP server wrapper, coding-assistant subagent file.

### 4.2 The manifest: `agent.yaml`

```yaml
apiVersion: afe/v1
kind: Agent
metadata:
  id: voice/voice-form-filler          # <category>/<slug>, globally unique, never reused
  name: Voice-to-Form Filler
  version: 0.1.0                       # semver
  family: perception
  category: voice
  tier: composite                      # atomic | composite
  maturity: spec                       # spec | prototype | beta | stable | deprecated
  priority: P0                         # P0 (MVP) | P1 | P2
  tags: [voice, forms, extraction, accessibility]
  maintainers: ["@github-handle"]
  license: Apache-2.0
spec:
  summary: Fill any form's fields from natural speech, then validate and confirm.
  purpose: >
    Lets users complete forms hands-free or in their own language. Maps spoken
    answers to typed fields, asks follow-up questions for missing or invalid
    fields, and never submits without confirmation.
  pattern: plan-and-execute            # see §2.3
  autonomy: L2                         # see §2.2
  io:
    input: schemas/input.schema.json   # audio stream/file + form schema + locale
    output: schemas/output.schema.json # filled field values + confidence + gaps
  model:
    capabilities: [tool_use, structured_output]
    optional_capabilities: [native_audio]
    min_context_tokens: 16000
    tested_with: [frontier-large, frontier-small, open-weights-8b]
  tools:                               # MCP servers from /mcp-servers
    required: [afe/stt]
    optional: [afe/tts, afe/browser]
  uses_agents:                         # composition: other agents it calls
    - voice/speech-to-text
    - text/structured-extractor
    - orchestration/verifier
  memory: session                      # none | session | long-term
  safety:
    level: S2                          # see §4.3
    side_effects: [fills-form-fields]
    approval_required_for: [submit]
    handles_pii: true
    data_retention: none
  limits:
    max_steps: 25
    timeout_seconds: 180
    max_cost_usd: 0.10
  evals:
    suite: evals/eval.yaml
    targets: {field_accuracy: 0.95, missing_field_recall: 0.98}
  exports: [python, typescript, mcp-server, a2a-card, agent-skill, subagent]
  locales: [en, hi, ta, te, bn, mr, es, fr, ar]
```

### 4.3 Safety levels

| Level | Meaning | Default control |
|---|---|---|
| **S0** | Pure computation on given input, no external access | None |
| **S1** | Reads external or private data (web, files, inbox) | Read-only scopes; prompt-injection screening on inputs |
| **S2** | Reversible writes (drafts, local files, form fields not yet submitted) | Undo/rollback available; changes logged |
| **S3** | External side effects (send, post, update records, run commands) | Human approval per action by default; policy can relax it |
| **S4** | High stakes: money, legal, health, security, identity, irreversible deletion | Mandatory human approval, full audit log, domain disclaimers, no autonomous mode |

### 4.4 Maturity levels

| Badge | Level | Requirements |
|---|---|---|
| 💡 | `spec` | Valid `agent.yaml`, README, schemas |
| 🧪 | `prototype` | Runs end-to-end in the core runtime; ≥ 10 eval cases |
| 🔶 | `beta` | ≥ 50 eval cases passing targets; 2+ implementations or adapters; security review for S3+ |
| ✅ | `stable` | Used in ≥ 1 recipe; 3 months without breaking change; multilingual tests where relevant |
| 🗄 | `deprecated` | Superseded; kept with alias for 2 minor releases |

### 4.5 Naming conventions

- **Slugs:** kebab-case, role-style nouns: `<object>-<role>` (`inbox-triager`, `contract-analyzer`) or a capability (`speech-to-text`).
- **IDs:** `<category>/<slug>`; category slugs are globally unique, so IDs stay short (`voice/speech-to-text`, not `perception/voice/speech-to-text`).
- **IDs never change.** Renames get an alias entry in `registry/aliases.yaml`.
- **Teams:** `teams/<team-slug>`; **recipes:** `recipes/<recipe-slug>`; **tools:** `mcp-servers/<tool-slug>`.

### 4.6 Composition contract

Agents compose when the output schema of one satisfies the input schema of another. The registry checks this automatically and publishes a **compatibility graph** ("what can I plug into `speech-to-text`?"). Shared types live in `spec/types/` (e.g. `Transcript`, `Document`, `Citation`, `Task`, `Contact`, `Money`, `Address`, `FormSchema`) so agents written by different people still fit together.

---

## 5. Repository structure

### 5.1 Top-level layout

```
agents-for-everything/
├── README.md                    # Pitch, quick start, catalog link
├── CATALOG.md                   # AUTO-GENERATED table of all agents from agent.yaml files
├── AGENTS.md                    # Instructions for AI coding agents contributing to the repo
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md                  # Vulnerability reporting + agent safety policy
├── LICENSE                      # Apache-2.0
├── CODEOWNERS                   # Category maintainers
│
├── spec/                        # THE STANDARD
│   ├── agent.schema.json        # JSON Schema for agent.yaml
│   ├── team.schema.json
│   ├── recipe.schema.json
│   ├── tools.schema.json
│   ├── types/                   # Shared I/O types: Transcript, Document, Citation, Task...
│   └── SPEC.md                  # Human-readable standard (versioned: afe/v1)
│
├── agents/                      # THE CATALOG (~570 agents)
│   ├── core/                    # family
│   │   ├── orchestration/       # category
│   │   │   ├── router/          # agent
│   │   │   ├── task-planner/
│   │   │   └── ...
│   │   ├── memory/
│   │   ├── guardrails/
│   │   └── evaluation/
│   ├── perception/              # voice, audio, vision, video, accessibility
│   ├── information/             # text, search, research
│   ├── action/                  # browser, computer-use, documents, integration, physical
│   ├── builders/                # coding, devops, data, ai-engineering, security, it-support
│   ├── business/                # communication, meetings, content, marketing, sales, support,
│   │                            # finance, legal, hr, operations, supply-chain, strategy
│   ├── life/                    # productivity, personal, travel, wellness, education,
│   │                            # creative, community
│   └── industries/              # banking, insurance, healthcare, ecommerce, real-estate,
│                                # manufacturing, agriculture, energy, government,
│                                # hospitality, science, gaming
│
├── teams/                       # Multi-agent compositions (team.yaml + graph + evals)
│   ├── research-team/
│   └── ...
│
├── recipes/                     # End-to-end product blueprints with runnable demo apps
│   ├── voice-form-filling/
│   └── ...
│
├── mcp-servers/                 # Shared tools, each an MCP server
│   ├── stt/  tts/  browser/  filesystem/  web-search/  ocr/  email/  calendar/
│   ├── vector-store/  sql/  shell-sandbox/  http/  documents/  ...
│
├── packages/                    # Runtime libraries
│   ├── core-python/             # `agents-for-everything` on PyPI: Agent base, runner, schema validation, tracing
│   ├── core-typescript/         # `@agents-for-everything/core` on npm
│   └── adapters/                # langgraph, openai-agents, claude-agent-sdk, google-adk,
│                                # ms-agent-framework, crewai, mastra
│
├── cli/                         # `agents-for-everything` CLI (alias `afe`): search, add, run, test, new, export, validate
│
├── templates/                   # Scaffolds used by `afe new`
│   ├── agent-atomic/
│   ├── agent-composite/
│   ├── team/
│   └── recipe/
│
├── evals/                       # Shared eval harness, datasets, judges, leaderboard
│   ├── harness/
│   ├── datasets/                # Shared multilingual/test corpora (license-clean)
│   └── reports/                 # AUTO-GENERATED
│
├── registry/                    # AUTO-GENERATED machine-readable catalog
│   ├── catalog.json
│   ├── compatibility-graph.json
│   └── aliases.yaml             # renamed/deprecated IDs
│
├── radar/                       # Ecosystem tracking: monthly notes on new patterns/standards
│
├── docs/                        # Documentation site source (Docusaurus or MkDocs)
│   ├── getting-started/
│   ├── concepts/
│   ├── guides/                  # writing an agent, writing evals, safety review
│   ├── blueprint.md             # this document
│   └── adr/                     # Architecture Decision Records
│
├── scripts/                     # validate manifests, build catalog, check links
│
└── .github/
    ├── workflows/               # validate.yml, evals.yml, catalog.yml, release.yml, radar.yml
    ├── ISSUE_TEMPLATE/          # agent-request.yml, bug.yml, new-category-rfc.yml
    └── PULL_REQUEST_TEMPLATE.md
```

### 5.2 Why this shape scales to 500+ agents

| Decision | Reason |
|---|---|
| Three levels: `family/category/agent` | 8 families, 54 categories, 4–22 agents each: no folder gets too big to browse |
| Short IDs (`category/slug`) | Easy to type in the CLI and in `uses_agents`; folders can move between families without breaking IDs |
| Generated `CATALOG.md` and `registry/` | Nobody edits a 600-row table by hand; one source of truth (`agent.yaml`) |
| `mcp-servers/` separate from `agents/` | Tools are reused by many agents; versioned independently |
| Agents are **not** each a published package | 500 packages are unmaintainable. Users install `agents-for-everything` (core) and pull agents with `afe add`, copying the folder in, shadcn/ui-style |
| CODEOWNERS per category | Distributed maintenance: each category has 2+ maintainers |
| Path-filtered CI | A PR touching `agents/business/legal/` only runs that category's evals |
| Monorepo tooling | `uv` workspace (Python) + `pnpm` workspace (TypeScript); Turborepo or Nx for caching if build times grow |

### 5.3 The command-line tool

The package installs the `agents-for-everything` command and the short alias `afe`, which the examples use.

```bash
afe search "fill form from voice"          # semantic search over the catalog
afe info voice/voice-form-filler            # manifest, deps, safety level, maturity
afe add voice/voice-form-filler             # copy agent + its sub-agents into ./agents
afe run text/summarizer --input doc.pdf     # run locally with the core runtime
afe test voice/speech-to-text               # run its eval suite
afe new --tier atomic --category finance    # scaffold a new agent from template
afe export voice/speech-to-text --as skill  # also: mcp-server | a2a | subagent | langgraph
afe validate                                # lint all manifests, schemas, composition graph
afe graph voice/voice-form-filler           # show composition tree
```

### 5.4 CI pipelines

| Workflow | Trigger | Does |
|---|---|---|
| `validate.yml` | Every PR | Schema-validate manifests, check IDs unique, check `uses_agents` exist and contracts fit, lint prompts and links |
| `evals.yml` | PR touching an agent | Run that agent's evals with a cheap model; full suite nightly |
| `safety.yml` | PR touching S3/S4 agents | Require a safety-reviewer approval; run red-team suite |
| `catalog.yml` | Merge to main | Regenerate `CATALOG.md`, `registry/`, docs site |
| `release.yml` | Tag | Publish core packages, generate exports (Skills, Agent Cards, MCP wrappers) |
| `radar.yml` | Weekly | Run the `ecosystem-radar` team (see §13) and open issues for new findings |

---

## 6. Catalog overview

| Measure | Count |
|---|---|
| Agents | **571** |
| Families | 8 |
| Categories | 54 |
| Teams (multi-agent compositions) | 22 |
| Recipes (end-to-end products) | 12 |
| Atomic / composite agents | 343 / 228 |
| P0 (MVP) / P1 / P2 | 66 / 170 / 335 |
| Safety S0 / S1 / S2 / S3 / S4 | 140 / 244 / 107 / 46 / 34 |

### 6.1 By family

| # | Family | Folder | Categories | Agents | P0 | P1 | P2 |
|---|---|---|---|---|---|---|---|
| 1 | Core | `agents/core/` | 4 | 46 | 14 | 16 | 16 |
| 2 | Perception and Interaction | `agents/perception/` | 5 | 59 | 8 | 24 | 27 |
| 3 | Information | `agents/information/` | 3 | 47 | 15 | 16 | 16 |
| 4 | Action | `agents/action/` | 5 | 53 | 10 | 19 | 24 |
| 5 | Builders | `agents/builders/` | 6 | 76 | 9 | 28 | 39 |
| 6 | Business Functions | `agents/business/` | 12 | 134 | 9 | 47 | 78 |
| 7 | Life and Learning | `agents/life/` | 7 | 65 | 1 | 11 | 53 |
| 8 | Industries | `agents/industries/` | 12 | 91 | 0 | 9 | 82 |

### 6.2 By category

| § | Category | Folder | ID prefix | Agents | P0 | P1 | P2 |
|---|---|---|---|---|---|---|---|
| [7.1](#71-orchestration-and-meta-agents--agentscoreorchestration--id-prefix-orchestration) | Orchestration and meta-agents | `agents/core/orchestration/` | `orchestration/` | 18 | 6 | 8 | 4 |
| [7.2](#72-memory-and-knowledge--agentscorememory--id-prefix-memory) | Memory and knowledge | `agents/core/memory/` | `memory/` | 10 | 3 | 2 | 5 |
| [7.3](#73-guardrails-trust-and-safety--agentscoreguardrails--id-prefix-guardrails) | Guardrails, trust and safety | `agents/core/guardrails/` | `guardrails/` | 12 | 4 | 4 | 4 |
| [7.4](#74-evaluation-and-quality--agentscoreevaluation--id-prefix-evaluation) | Evaluation and quality | `agents/core/evaluation/` | `evaluation/` | 6 | 1 | 2 | 3 |
| [7.5](#75-voice-and-speech--agentsperceptionvoice--id-prefix-voice) | Voice and speech | `agents/perception/voice/` | `voice/` | 17 | 5 | 6 | 6 |
| [7.6](#76-audio-and-music--agentsperceptionaudio--id-prefix-audio) | Audio and music | `agents/perception/audio/` | `audio/` | 8 | 0 | 2 | 6 |
| [7.7](#77-vision-and-images--agentsperceptionvision--id-prefix-vision) | Vision and images | `agents/perception/vision/` | `vision/` | 17 | 3 | 8 | 6 |
| [7.8](#78-video--agentsperceptionvideo--id-prefix-video) | Video | `agents/perception/video/` | `video/` | 9 | 0 | 3 | 6 |
| [7.9](#79-accessibility--agentsperceptionaccessibility--id-prefix-accessibility) | Accessibility | `agents/perception/accessibility/` | `accessibility/` | 8 | 0 | 5 | 3 |
| [7.10](#710-language-and-text--agentsinformationtext--id-prefix-text) | Language and text | `agents/information/text/` | `text/` | 17 | 7 | 4 | 6 |
| [7.11](#711-search-and-retrieval--agentsinformationsearch--id-prefix-search) | Search and retrieval | `agents/information/search/` | `search/` | 15 | 4 | 6 | 5 |
| [7.12](#712-research-and-analysis--agentsinformationresearch--id-prefix-research) | Research and analysis | `agents/information/research/` | `research/` | 15 | 4 | 6 | 5 |
| [7.13](#713-browser-and-web-automation--agentsactionbrowser--id-prefix-browser) | Browser and web automation | `agents/action/browser/` | `browser/` | 12 | 3 | 3 | 6 |
| [7.14](#714-computer-use-and-desktop--agentsactioncomputer-use--id-prefix-computer-use) | Computer use and desktop | `agents/action/computer-use/` | `computer-use/` | 9 | 1 | 2 | 6 |
| [7.15](#715-files-and-documents--agentsactiondocuments--id-prefix-documents) | Files and documents | `agents/action/documents/` | `documents/` | 18 | 5 | 9 | 4 |
| [7.16](#716-workflow-and-integration--agentsactionintegration--id-prefix-integration) | Workflow and integration | `agents/action/integration/` | `integration/` | 8 | 1 | 4 | 3 |
| [7.17](#717-physical-world-iot-and-robotics--agentsactionphysical--id-prefix-physical) | Physical world, IoT and robotics | `agents/action/physical/` | `physical/` | 6 | 0 | 1 | 5 |
| [7.18](#718-software-engineering--agentsbuilderscoding--id-prefix-coding) | Software engineering | `agents/builders/coding/` | `coding/` | 22 | 5 | 10 | 7 |
| [7.19](#719-devops-cloud-and-sre--agentsbuildersdevops--id-prefix-devops) | DevOps, cloud and SRE | `agents/builders/devops/` | `devops/` | 13 | 1 | 5 | 7 |
| [7.20](#720-data-and-analytics--agentsbuildersdata--id-prefix-data) | Data and analytics | `agents/builders/data/` | `data/` | 15 | 3 | 6 | 6 |
| [7.21](#721-ai-and-ml-engineering--agentsbuildersai-engineering--id-prefix-ai-engineering) | AI and ML engineering | `agents/builders/ai-engineering/` | `ai-engineering/` | 8 | 0 | 2 | 6 |
| [7.22](#722-cybersecurity--agentsbuilderssecurity--id-prefix-security) | Cybersecurity | `agents/builders/security/` | `security/` | 12 | 0 | 4 | 8 |
| [7.23](#723-it-support-and-administration--agentsbuildersit-support--id-prefix-it-support) | IT support and administration | `agents/builders/it-support/` | `it-support/` | 6 | 0 | 1 | 5 |
| [7.24](#724-email-and-messaging--agentsbusinesscommunication--id-prefix-communication) | Email and messaging | `agents/business/communication/` | `communication/` | 10 | 3 | 3 | 4 |
| [7.25](#725-meetings-and-calendar--agentsbusinessmeetings--id-prefix-meetings) | Meetings and calendar | `agents/business/meetings/` | `meetings/` | 8 | 3 | 2 | 3 |
| [7.26](#726-writing-and-content-creation--agentsbusinesscontent--id-prefix-content) | Writing and content creation | `agents/business/content/` | `content/` | 15 | 0 | 7 | 8 |
| [7.27](#727-marketing-and-growth--agentsbusinessmarketing--id-prefix-marketing) | Marketing and growth | `agents/business/marketing/` | `marketing/` | 14 | 0 | 6 | 8 |
| [7.28](#728-sales-and-crm--agentsbusinesssales--id-prefix-sales) | Sales and CRM | `agents/business/sales/` | `sales/` | 13 | 0 | 8 | 5 |
| [7.29](#729-customer-support-and-success--agentsbusinesssupport--id-prefix-support) | Customer support and success | `agents/business/support/` | `support/` | 11 | 3 | 4 | 4 |
| [7.30](#730-finance-and-accounting--agentsbusinessfinance--id-prefix-finance) | Finance and accounting | `agents/business/finance/` | `finance/` | 14 | 0 | 5 | 9 |
| [7.31](#731-legal-and-compliance--agentsbusinesslegal--id-prefix-legal) | Legal and compliance | `agents/business/legal/` | `legal/` | 13 | 0 | 4 | 9 |
| [7.32](#732-hr-and-recruiting--agentsbusinesshr--id-prefix-hr) | HR and recruiting | `agents/business/hr/` | `hr/` | 12 | 0 | 4 | 8 |
| [7.33](#733-operations-and-project-management--agentsbusinessoperations--id-prefix-operations) | Operations and project management | `agents/business/operations/` | `operations/` | 10 | 0 | 4 | 6 |
| [7.34](#734-procurement-supply-chain-and-logistics--agentsbusinesssupply-chain--id-prefix-supply-chain) | Procurement, supply chain and logistics | `agents/business/supply-chain/` | `supply-chain/` | 8 | 0 | 0 | 8 |
| [7.35](#735-strategy-and-leadership--agentsbusinessstrategy--id-prefix-strategy) | Strategy and leadership | `agents/business/strategy/` | `strategy/` | 6 | 0 | 0 | 6 |
| [7.36](#736-personal-productivity--agentslifeproductivity--id-prefix-productivity) | Personal productivity | `agents/life/productivity/` | `productivity/` | 10 | 1 | 4 | 5 |
| [7.37](#737-personal-life-home-and-money--agentslifepersonal--id-prefix-personal) | Personal life, home and money | `agents/life/personal/` | `personal/` | 14 | 0 | 3 | 11 |
| [7.38](#738-travel--agentslifetravel--id-prefix-travel) | Travel | `agents/life/travel/` | `travel/` | 6 | 0 | 1 | 5 |
| [7.39](#739-health-and-wellness-consumer--agentslifewellness--id-prefix-wellness) | Health and wellness (consumer) | `agents/life/wellness/` | `wellness/` | 8 | 0 | 0 | 8 |
| [7.40](#740-education-and-learning--agentslifeeducation--id-prefix-education) | Education and learning | `agents/life/education/` | `education/` | 12 | 0 | 3 | 9 |
| [7.41](#741-creative-and-media--agentslifecreative--id-prefix-creative) | Creative and media | `agents/life/creative/` | `creative/` | 10 | 0 | 0 | 10 |
| [7.42](#742-community-and-social--agentslifecommunity--id-prefix-community) | Community and social | `agents/life/community/` | `community/` | 5 | 0 | 0 | 5 |
| [7.43](#743-banking-and-financial-services--agentsindustriesbanking--id-prefix-banking) | Banking and financial services | `agents/industries/banking/` | `banking/` | 17 | 0 | 6 | 11 |
| [7.44](#744-insurance--agentsindustriesinsurance--id-prefix-insurance) | Insurance | `agents/industries/insurance/` | `insurance/` | 6 | 0 | 0 | 6 |
| [7.45](#745-healthcare-clinical-and-provider--agentsindustrieshealthcare--id-prefix-healthcare) | Healthcare (clinical and provider) | `agents/industries/healthcare/` | `healthcare/` | 8 | 0 | 0 | 8 |
| [7.46](#746-e-commerce-and-retail--agentsindustriesecommerce--id-prefix-ecommerce) | E-commerce and retail | `agents/industries/ecommerce/` | `ecommerce/` | 11 | 0 | 2 | 9 |
| [7.47](#747-real-estate-and-property--agentsindustriesreal-estate--id-prefix-real-estate) | Real estate and property | `agents/industries/real-estate/` | `real-estate/` | 7 | 0 | 0 | 7 |
| [7.48](#748-manufacturing-and-industrial--agentsindustriesmanufacturing--id-prefix-manufacturing) | Manufacturing and industrial | `agents/industries/manufacturing/` | `manufacturing/` | 6 | 0 | 0 | 6 |
| [7.49](#749-agriculture--agentsindustriesagriculture--id-prefix-agriculture) | Agriculture | `agents/industries/agriculture/` | `agriculture/` | 6 | 0 | 0 | 6 |
| [7.50](#750-energy-and-utilities--agentsindustriesenergy--id-prefix-energy) | Energy and utilities | `agents/industries/energy/` | `energy/` | 5 | 0 | 0 | 5 |
| [7.51](#751-government-and-civic--agentsindustriesgovernment--id-prefix-government) | Government and civic | `agents/industries/government/` | `government/` | 8 | 0 | 0 | 8 |
| [7.52](#752-hospitality-and-food-service--agentsindustrieshospitality--id-prefix-hospitality) | Hospitality and food service | `agents/industries/hospitality/` | `hospitality/` | 4 | 0 | 0 | 4 |
| [7.53](#753-science-and-rd--agentsindustriesscience--id-prefix-science) | Science and R&D | `agents/industries/science/` | `science/` | 9 | 0 | 1 | 8 |
| [7.54](#754-gaming-and-interactive-entertainment--agentsindustriesgaming--id-prefix-gaming) | Gaming and interactive entertainment | `agents/industries/gaming/` | `gaming/` | 4 | 0 | 0 | 4 |

---


## 7. The full agent catalog

**How to read the tables**

- **ID** = the agent slug. The full ID is `<category>/<slug>` (category shown in each heading).
- **Input → Output** = the agent's contract in short form.
- **Tools** = MCP servers or capabilities needed.
- **T** (tier): **A** = atomic, **C** = composite (calls other agents).
- **S** (safety level): S0–S4 as defined in §4.3.
- **P** (priority): **P0** = build first (MVP), **P1** = next, **P2** = later.

---

### FAMILY 1 — CORE (`agents/core/`)

The infrastructure agents that every other agent and team depends on: orchestration, memory, safety, evaluation.

#### 7.1 Orchestration and meta-agents — `agents/core/orchestration/` · ID prefix `orchestration/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `router` | Intent Router | Classifies a request and picks the best agent or team from the catalog, with extracted arguments | request → agent ID + args + confidence | registry index, embeddings | A | S0 | P0 |
| `task-planner` | Task Planner | Breaks a goal into ordered, dependency-aware steps with success criteria and estimated cost | goal + context → plan (DAG) | — | A | S0 | P0 |
| `supervisor` | Supervisor / Orchestrator | Executes a plan by delegating steps to worker agents, tracks state, re-plans when a step fails | plan → results + run log | A2A, registry | C | S1 | P0 |
| `critic` | Critic / Reflector | Reviews another agent's output against a rubric and returns specific, actionable fixes | output + rubric → critique + score | — | A | S0 | P0 |
| `verifier` | Output Verifier | Checks outputs against schema, business rules, tests or ground truth; returns pass/fail with reasons | output + checks → verdict | schema validator, code sandbox | A | S0 | P0 |
| `human-approval-gate` | Human-in-the-Loop Gate | Pauses a workflow before risky steps, shows a clear summary/diff, records approve/reject/edit | proposed action → decision + audit entry | notification channel | A | S1 | P0 |
| `clarifier` | Clarifier | Detects ambiguous or under-specified requests and asks the fewest questions needed | request → questions or refined request | — | A | S0 | P1 |
| `tool-selector` | Tool Selector | Picks the minimal set of tools/MCP servers for a task from a large registry (tool retrieval) | task → tool list | tool registry, embeddings | A | S0 | P1 |
| `context-manager` | Context Compressor | Summarizes and prunes long histories and tool outputs to stay within token budgets without losing key facts | history → compact context | — | A | S0 | P1 |
| `budget-guard` | Cost & Rate Guard | Tracks tokens, money, time and API quotas; downgrades models or stops runs at limits | run telemetry → allow/throttle/stop | telemetry | A | S0 | P1 |
| `error-recovery` | Retry & Recovery | Diagnoses failures (timeouts, tool errors, bad output), retries with alternatives, escalates when stuck | error + context → recovery action | — | A | S1 | P1 |
| `handoff-coordinator` | Handoff Coordinator | Transfers a conversation or task between agents with a structured context packet | context → handoff packet | A2A | A | S0 | P1 |
| `scheduler` | Job Scheduler | Runs agents on cron schedules or event triggers; manages queues and retries | schedule/event → job runs | queue, cron | A | S2 | P1 |
| `agent-builder` | Agent Factory | Generates a new agent scaffold (manifest, prompt, schemas, eval cases) from a plain-language description | description → agent folder | repo templates | C | S2 | P1 |
| `model-selector` | Model Selector | Chooses the right model per subtask by cost, latency, quality and data-residency rules | subtask + policy → model choice | model registry | A | S0 | P2 |
| `prompt-optimizer` | Prompt Optimizer | Improves an agent's prompt automatically using eval results (DSPy-style optimization) | prompt + evals → better prompt | eval harness | C | S0 | P2 |
| `debate-moderator` | Debate / Consensus | Runs several agents with different viewpoints and synthesizes a judged answer | question → consensus + dissent | — | C | S0 | P2 |
| `progress-reporter` | Progress Reporter | Turns long-running job state into short human-readable status updates | run state → status message | notification channel | A | S1 | P2 |

#### 7.2 Memory and knowledge — `agents/core/memory/` · ID prefix `memory/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `memory-writer` | Memory Writer | Decides what is worth remembering from an interaction (facts, preferences, decisions) and stores it without duplicates | interaction → memory records | memory store | A | S2 | P0 |
| `memory-retriever` | Memory Retriever | Recalls the memories relevant to the current task, ranked and deduplicated | query/context → memories | memory store | A | S1 | P0 |
| `knowledge-ingestor` | Knowledge Ingestor | Parses, chunks, embeds and indexes documents into a hybrid (keyword + vector) store with metadata and permissions | documents → index entries | vector-store, documents | A | S2 | P0 |
| `session-summarizer` | Session Summarizer | Writes end-of-session summaries so the next session resumes with continuity | transcript → summary + open items | memory store | A | S2 | P1 |
| `knowledge-graph-builder` | Knowledge Graph Builder | Extracts entities and relationships from text into a graph | documents → nodes + edges | graph DB | A | S2 | P1 |
| `entity-resolver` | Entity Resolver | Merges duplicate people, companies or products across sources | records → resolved entities | — | A | S1 | P2 |
| `memory-gardener` | Memory Gardener | Consolidates, expires and resolves contradictions in long-term memory | memory store → cleaned store | memory store | A | S2 | P2 |
| `profile-builder` | Preference Profiler | Builds a user preference profile with visible, editable, consent-based controls | interactions → profile | memory store | A | S2 | P2 |
| `ontology-designer` | Ontology Designer | Proposes taxonomies, tag sets and schemas for a domain or corpus | corpus/domain → taxonomy | — | A | S0 | P2 |
| `wiki-maintainer` | Wiki Maintainer | Keeps an internal wiki current: finds stale pages, drafts updates from new sources | wiki + sources → edit proposals | wiki API | C | S2 | P2 |

#### 7.3 Guardrails, trust and safety — `agents/core/guardrails/` · ID prefix `guardrails/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `prompt-injection-detector` | Injection Detector | Scans incoming content (web pages, emails, files, tool output) for hidden instructions aimed at agents | content → risk score + spans | classifier | A | S0 | P0 |
| `pii-redactor` | PII Redactor | Detects and masks personal data (names, phones, emails, Aadhaar, PAN, SSN, card numbers) before LLM calls or logging, reversibly if needed | text/doc → redacted + map | NER, regex packs | A | S0 | P0 |
| `content-moderator` | Content Moderator | Classifies text and images against a configurable harm policy | content → labels + action | moderation model | A | S0 | P0 |
| `hallucination-checker` | Grounding Checker | Checks each claim in an answer against the provided sources; flags unsupported statements | answer + sources → claim verdicts | — | A | S0 | P0 |
| `policy-enforcer` | Action Policy Enforcer | Evaluates a proposed tool call against allow/deny rules (OPA-style) before it runs | action + policy → allow/deny/approve | policy engine | A | S0 | P1 |
| `secrets-guard` | Secrets Guard | Stops API keys, tokens and passwords leaking into prompts, outputs or logs | text → findings + masked text | secret patterns | A | S0 | P1 |
| `audit-logger` | Audit Logger | Records an append-only, tamper-evident trace of decisions and tool calls | events → audit records | OpenTelemetry, log store | A | S2 | P1 |
| `red-teamer` | Red Teamer | Probes another agent for jailbreaks, data leakage and unsafe actions; reports weaknesses | agent endpoint → findings report | attack library | C | S1 | P1 |
| `bias-auditor` | Bias Auditor | Tests outputs for unequal treatment using counterfactual inputs (swap names, gender, region) | agent + test set → bias report | eval harness | C | S0 | P2 |
| `decision-explainer` | Decision Explainer | Produces plain-language reasons for an agent's decision, for regulated contexts | trace → explanation | — | A | S0 | P2 |
| `data-residency-guard` | Data Residency Guard | Routes data only to models and regions allowed by policy (e.g. data must stay in-country) | request + policy → route | model registry | A | S0 | P2 |
| `age-safety-filter` | Age-Appropriate Filter | Applies child-safe content rules for apps used by minors | content → allow/rewrite/block | moderation model | A | S0 | P2 |

#### 7.4 Evaluation and quality — `agents/core/evaluation/` · ID prefix `evaluation/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `llm-judge` | LLM Judge | Scores outputs against a rubric with calibrated, explained judgments | output + rubric → score + reason | — | A | S0 | P0 |
| `test-case-generator` | Test Case Generator | Creates eval datasets for an agent, including edge and adversarial cases | agent spec → cases.jsonl | — | A | S0 | P1 |
| `regression-runner` | Regression Runner | Runs eval suites on every change and compares with the baseline | agent + suite → report | eval harness | C | S1 | P1 |
| `trace-analyzer` | Trace Analyzer | Mines production traces to find and cluster failure patterns; explains why an agent failed | traces → failure clusters | trace store | A | S1 | P2 |
| `benchmark-runner` | Benchmark Runner | Runs public benchmarks (tool use, web tasks, coding) against agents and publishes results | agent → benchmark scores | benchmark suites | C | S1 | P2 |
| `feedback-collector` | Feedback Collector | Turns user thumbs-down and corrections into new eval cases | feedback → eval cases | — | A | S1 | P2 |

---

### FAMILY 2 — PERCEPTION AND INTERACTION (`agents/perception/`)

Agents that hear, see, watch and speak, plus accessibility.

#### 7.5 Voice and speech — `agents/perception/voice/` · ID prefix `voice/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `speech-to-text` | Transcriber | Batch or streaming speech recognition with timestamps, punctuation, language detection and code-switching (e.g. Hinglish) | audio → transcript JSON | stt | A | S1 | P0 |
| `text-to-speech` | Narrator | Natural speech from text with voice, speed, emotion and SSML control in many languages | text → audio | tts | A | S0 | P0 |
| `voice-form-filler` | Voice-to-Form Filler | Listens to the user and fills the right form fields (name, date, amount, address), validates them, asks for anything missing, confirms before submit | audio + form schema → filled fields | stt, tts, browser (opt) | C | S2 | P0 |
| `voice-command` | Voice Command Interpreter | Maps spoken commands to app actions or function calls | audio/transcript + action list → function call | stt | A | S1 | P0 |
| `realtime-voice-assistant` | Real-time Voice Assistant | Full-duplex speech-to-speech assistant with low latency, interruption (barge-in) and tool use | live audio ↔ live audio + actions | realtime audio model, tools | C | S1 | P0 |
| `voice-search` | Voice Search | Turns spoken questions into good search queries and answers by voice or text | audio → answer + sources | stt, web-search, tts | C | S1 | P1 |
| `dictation-editor` | Smart Dictation | Dictation with voice editing ("delete the last sentence", "make that a list") and formatting | audio → formatted text | stt | A | S0 | P1 |
| `speaker-diarizer` | Speaker Diarizer | Works out who spoke when and labels speakers | audio → speaker segments | diarization model | A | S1 | P1 |
| `voice-note-summarizer` | Voice Note Processor | Turns voice memos into clean notes, tasks and reminders | audio → note + tasks | stt | C | S1 | P1 |
| `phone-call-agent` | Phone Call Agent | Inbound/outbound phone agent (SIP/telephony) for bookings, reminders and surveys; always discloses it is an AI | call ↔ call + outcome | telephony, stt, tts | C | S3 | P1 |
| `live-interpreter` | Live Interpreter | Real-time two-way speech translation between people who don't share a language | audio ↔ translated audio | stt, translator, tts | C | S1 | P1 |
| `ivr-designer` | Conversational IVR | Designs and runs natural-language phone menus to replace "press 1" trees | call flows → IVR config + runtime | telephony | C | S2 | P2 |
| `pronunciation-coach` | Pronunciation Coach | Scores pronunciation and fluency and gives targeted feedback | audio + target text → scores + tips | stt, phoneme model | A | S0 | P2 |
| `emotion-detector` | Voice Emotion Detector | Detects tone, stress and emotion in speech (e.g. for support quality) | audio → emotion labels over time | audio classifier | A | S1 | P2 |
| `speaker-verifier` | Speaker Verifier | Consent-based speaker verification with anti-spoofing and synthetic-voice detection | audio + enrolled print → match + liveness | voice biometrics | A | S4 | P2 |
| `wake-word-intent` | On-device Wake Word & Intent | Small on-device keyword spotting and intent detection for low-power devices | audio → wake event + intent | edge model | A | S0 | P2 |
| `consented-voice-cloner` | Consented Voice Builder | Creates a custom voice only after verified consent from the speaker, and watermarks output | consent + samples → voice model | tts | A | S4 | P2 |

#### 7.6 Audio and music — `agents/perception/audio/` · ID prefix `audio/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `audio-cleaner` | Audio Cleaner | Removes noise, normalizes loudness, reduces echo | audio → clean audio | audio DSP | A | S0 | P1 |
| `podcast-producer` | Podcast Producer | From raw recording: clean audio, cut silences and filler, chapters, show notes, transcript | recording → episode package | stt, audio DSP | C | S1 | P1 |
| `audio-classifier` | Sound Event Classifier | Detects sounds such as alarms, glass breaking, coughing, machinery faults | audio → events + timestamps | audio classifier | A | S1 | P2 |
| `music-tagger` | Music Tagger | Tags genre, mood, tempo and key for music libraries | audio → tags | music model | A | S0 | P2 |
| `music-composer` | Music Composer | Generates music or jingles from a brief, with licence-safe output | brief → audio + stems | music generation | A | S0 | P2 |
| `audio-search` | Audio Moment Search | Finds moments in hours of audio by meaning ("where did they discuss pricing?") | audio library + query → timestamps | stt, vector-store | C | S1 | P2 |
| `sound-effect-generator` | SFX Generator | Generates sound effects from descriptions | description → audio | audio generation | A | S0 | P2 |
| `audiobook-producer` | Audiobook Producer | Turns a manuscript into a multi-voice audiobook with chapter files | manuscript → audio chapters | tts | C | S0 | P2 |

#### 7.7 Vision and images — `agents/perception/vision/` · ID prefix `vision/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `ocr` | Text Extractor (OCR) | Extracts printed and handwritten text with layout from images and scans, in many scripts | image/scan → text + layout | ocr, vision model | A | S1 | P0 |
| `visual-qa` | Visual Q&A | Answers questions about an image | image + question → answer | vision model | A | S1 | P0 |
| `screenshot-understander` | Screen Parser | Converts UI screenshots into a structured list of elements (buttons, fields, text) with coordinates for computer-use agents | screenshot → UI element tree | vision model | A | S1 | P0 |
| `image-captioner` | Image Captioner | Writes captions and descriptions at the requested detail level | image → caption | vision model | A | S0 | P1 |
| `object-detector` | Object Detector & Counter | Finds and counts objects with bounding boxes | image + classes → detections | detection model | A | S1 | P1 |
| `chart-reader` | Chart Reader | Extracts the underlying data from charts and graphs into tables | chart image → table | vision model | A | S0 | P1 |
| `ui-to-code` | Design to Code | Turns a mockup or screenshot into HTML/React components | image → code | vision model, code sandbox | C | S0 | P1 |
| `image-generator` | Image Generator | Text-to-image with style, aspect ratio and brand constraints | prompt → images | image generation | A | S0 | P1 |
| `image-editor` | Image Editor | Edits images by instruction: background removal, inpainting, resize, retouch | image + instruction → image | image editing | A | S0 | P1 |
| `id-document-reader` | ID Document Reader | Extracts fields from ID cards, passports and licences for consented KYC, with quality and tamper checks | ID image → fields + checks | ocr, vision model | A | S4 | P1 |
| `face-plate-anonymizer` | Face & Plate Anonymizer | Blurs faces, licence plates and screens in images/video for privacy | image/video → anonymized | detection model | A | S0 | P1 |
| `diagram-to-code` | Diagram Digitizer | Converts whiteboard sketches and flowcharts into Mermaid, draw.io or structured data | image → diagram code | vision model | A | S0 | P2 |
| `image-restorer` | Image Restorer | Upscales, denoises and restores old or low-quality photos | image → image | restoration model | A | S0 | P2 |
| `visual-inspector` | Visual Defect Inspector | Compares items against a reference to find defects (generic; see manufacturing for line use) | image + reference → defects | vision model | A | S1 | P2 |
| `image-similarity` | Similar Image Finder | Reverse image search and near-duplicate detection in a library | image + library → matches | embeddings | A | S1 | P2 |
| `scene-safety-monitor` | Scene Safety Monitor | Detects hazards in camera feeds (fire, smoke, missing PPE, falls) with privacy settings | video frames → alerts | detection model | C | S1 | P2 |
| `synthetic-media-detector` | AI-Image Detector | Estimates whether an image was AI-generated or manipulated, with evidence | image → likelihood + signals | forensic models | A | S0 | P2 |

#### 7.8 Video — `agents/perception/video/` · ID prefix `video/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `video-summarizer` | Video Summarizer | Summarizes videos with chapters, key frames and timestamps | video → summary + chapters | stt, vision model | C | S1 | P1 |
| `video-captioner` | Subtitle Generator | Generates and translates subtitles (SRT/VTT) with correct timing | video → subtitle files | stt, translator | C | S1 | P1 |
| `clip-generator` | Short Clip Generator | Finds the best moments in long videos and cuts vertical clips with captions for social media | video → clips | stt, video editing | C | S1 | P1 |
| `video-search` | Video Moment Search | Finds moments in a video library by spoken or visual content | library + query → timestamps | stt, vision, vector-store | C | S1 | P2 |
| `video-editor` | Transcript-based Editor | Edits video by editing the transcript or by instruction (cut, reorder, add b-roll) | video + instructions → video | ffmpeg, stt | C | S2 | P2 |
| `video-generator` | Video Generator | Text- or image-to-video generation | prompt/image → video | video generation | A | S0 | P2 |
| `dubbing-agent` | Dubbing Agent | Translates and re-voices video, optionally with lip-sync | video + target language → dubbed video | stt, translator, tts | C | S1 | P2 |
| `lecture-to-notes` | Lecture to Notes | Turns lectures into structured notes, slides index and a quiz | video → notes + quiz | stt, vision | C | S1 | P2 |
| `live-stream-monitor` | Live Stream Monitor | Watches live streams for events, highlights or policy violations | stream → events | stt, vision | C | S1 | P2 |

#### 7.9 Accessibility — `agents/perception/accessibility/` · ID prefix `accessibility/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `alt-text-writer` | Alt-Text Writer | Writes context-aware alt text for images on web pages and in documents | image + context → alt text | vision model | A | S0 | P1 |
| `accessibility-auditor` | Accessibility Auditor | Audits web pages and documents against WCAG and proposes fixes | URL/doc → issues + fixes | browser | C | S1 | P1 |
| `screen-narrator` | Screen Narrator | Describes what is on screen for blind and low-vision users and navigates by voice | screen → speech + actions | screenshot-understander, tts | C | S2 | P1 |
| `live-captioner` | Live Captioner | Real-time captions for meetings, classes and events | live audio → captions | stt | C | S1 | P1 |
| `easy-read-simplifier` | Easy-Read Simplifier | Rewrites content in plain language for cognitive accessibility and low literacy | text → easy-read text | — | A | S0 | P1 |
| `document-remediator` | Document Remediator | Makes PDFs and documents accessible (tags, reading order, headings, contrast) | document → accessible document | documents | A | S2 | P2 |
| `voice-control-navigator` | Voice Control Navigator | Hands-free control of apps and the OS by voice | voice → UI actions | stt, desktop-operator | C | S3 | P2 |
| `sign-language-interpreter` | Sign Language Interpreter | Research-grade sign language to text and text to sign avatar | video ↔ text | specialised models | C | S1 | P2 |

---

### FAMILY 3 — INFORMATION (`agents/information/`)

Agents that understand language, find information and research.

#### 7.10 Language and text — `agents/information/text/` · ID prefix `text/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `summarizer` | Summarizer | Summarizes any length of content in a chosen style (TL;DR, bullets, executive) with source references | text/doc → summary | — | A | S0 | P0 |
| `translator` | Translator | Context-aware translation that keeps formatting and follows a glossary; 100+ languages including Indic | text + target lang → translation | — | A | S0 | P0 |
| `rewriter` | Rewriter | Changes tone, length, reading level or audience while keeping meaning | text + style → text | — | A | S0 | P0 |
| `proofreader` | Proofreader | Fixes grammar, spelling, clarity and consistency against a style guide | text → corrections + clean text | — | A | S0 | P0 |
| `classifier` | Text Classifier | Zero/few-shot classification into any custom label set with confidence | text + labels → label(s) | — | A | S0 | P0 |
| `structured-extractor` | Structured Extractor | Turns free text into JSON that validates against any given schema (the workhorse for forms, records, CRM) | text + JSON schema → JSON | — | A | S0 | P0 |
| `entity-extractor` | Entity Extractor | Named entities (people, orgs, places, dates, amounts) with linking to IDs | text → entities | — | A | S0 | P0 |
| `sentiment-analyzer` | Sentiment Analyzer | Sentiment, emotion and aspect-based opinions | text → sentiment by aspect | — | A | S0 | P1 |
| `topic-tagger` | Keyword & Topic Tagger | Extracts keywords, topics and tags | text → tags | — | A | S0 | P1 |
| `explainer` | Concept Explainer | Explains a concept at a chosen level with analogies and examples | topic + level → explanation | — | A | S0 | P1 |
| `text-comparer` | Semantic Diff | Explains what changed in meaning between two versions | text A + text B → changes | — | A | S0 | P1 |
| `question-generator` | Q&A Generator | Generates FAQs and question-answer pairs from content | content → Q&A list | — | A | S0 | P2 |
| `title-generator` | Title & Headline Generator | Generates titles, headlines and subject lines | content → options | — | A | S0 | P2 |
| `glossary-builder` | Glossary Builder | Builds term lists and definitions from a corpus | corpus → glossary | — | A | S0 | P2 |
| `transliterator` | Transliterator | Converts between scripts (e.g. Devanagari ↔ Latin) without translating | text → text in target script | — | A | S0 | P2 |
| `style-guide-enforcer` | Brand Voice Enforcer | Checks and fixes text against brand voice and terminology rules | text + guide → fixes | — | A | S0 | P2 |
| `argument-mapper` | Argument Mapper | Maps claims, premises, evidence and logical fallacies in a text | text → argument map | — | A | S0 | P2 |

#### 7.11 Search and retrieval — `agents/information/search/` · ID prefix `search/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `web-search` | Web Searcher | Runs queries on search APIs, deduplicates and ranks results with snippets | query → results | web-search | A | S1 | P0 |
| `answer-engine` | Answer Engine | Search, read and synthesize a direct answer with inline citations | question → cited answer | web-search, http | C | S1 | P0 |
| `rag-qa` | Document Q&A | Answers questions over a private knowledge base with citations and "I don't know" when unsupported | question + index → cited answer | vector-store | C | S1 | P0 |
| `semantic-search` | Hybrid Searcher | Keyword + vector search over private corpora with filters | query → ranked chunks | vector-store | A | S1 | P0 |
| `query-rewriter` | Query Rewriter | Expands, decomposes and translates queries to improve recall | query → better queries | — | A | S0 | P1 |
| `reranker` | Reranker | Reorders results by true relevance to the question | query + results → reranked | rerank model | A | S0 | P1 |
| `enterprise-search` | Enterprise Search | Federated search across Drive, email, chat, wiki and tickets, respecting each user's permissions | query + identity → results | connectors | C | S1 | P1 |
| `news-monitor` | News Monitor | Tracks topics and entities in the news and alerts on meaningful changes | watchlist → alerts + digest | news APIs | C | S1 | P1 |
| `academic-search` | Academic Searcher | Finds papers with metadata, abstracts and citation counts (arXiv, PubMed, Semantic Scholar, OpenAlex) | query → papers | scholarly APIs | A | S1 | P1 |
| `source-credibility` | Source Credibility Scorer | Rates sources for reliability, bias and freshness | URLs → scores + reasons | web-search | A | S1 | P1 |
| `patent-search` | Patent Searcher | Prior-art search across patent databases | invention description → patents | patent APIs | A | S1 | P2 |
| `local-search` | Local Places Finder | Finds places with hours, ratings and directions | need + location → places | maps API | A | S1 | P2 |
| `company-lookup` | Company Lookup | Public firmographic data about companies (size, sector, filings, news) | company name → profile | registries, web-search | A | S1 | P2 |
| `dataset-finder` | Dataset Finder | Finds public datasets with licence and quality notes | need → datasets | dataset portals | A | S1 | P2 |
| `multimodal-search` | Multimodal Searcher | Searches a media library by text, image or audio | query (any modality) → items | embeddings | C | S1 | P2 |

#### 7.12 Research and analysis — `agents/information/research/` · ID prefix `research/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `deep-researcher` | Deep Researcher | Plans research questions, searches iteratively, reads dozens of sources and writes a cited report | topic + depth → report | web-search, http, documents | C | S1 | P0 |
| `source-reader` | Source Reader | Reads one URL, PDF or paper deeply and extracts key points, data and quotes with locations | source → structured notes | http, documents | A | S1 | P0 |
| `fact-checker` | Fact Checker | Verifies claims against reliable sources and gives a verdict with evidence | claims → verdicts + evidence | web-search | C | S1 | P0 |
| `report-writer` | Report Writer | Turns findings into a structured report (executive summary, sections, charts, references) | findings → report (MD/DOCX/PDF) | documents | A | S0 | P0 |
| `literature-reviewer` | Literature Reviewer | Systematic review: search, screen, extract, synthesize, PRISMA-style log | research question → review | academic-search | C | S1 | P1 |
| `competitive-analyst` | Competitive Analyst | Builds competitor profiles and feature/pricing comparison matrices | company + market → analysis | web-search | C | S1 | P1 |
| `market-researcher` | Market Researcher | Market size, segments, trends and players with sources and assumptions shown | market → report | web-search | C | S1 | P1 |
| `comparison-analyst` | Comparison Analyst | Structured "X vs Y vs Z" against weighted criteria | options + criteria → matrix + pick | web-search | A | S1 | P1 |
| `survey-analyst` | Survey Analyst | Codes open-ended survey answers into themes with counts and quotes | responses → themes report | — | C | S1 | P1 |
| `interview-synthesizer` | User Research Synthesizer | Turns user interviews into insights, quotes, journeys and personas | transcripts → insights | — | C | S1 | P1 |
| `trend-spotter` | Trend Spotter | Detects emerging trends across news, social media, papers and patents | domain → trend report | web-search, academic-search | C | S1 | P2 |
| `due-diligence` | Due Diligence Analyst | Background checks on companies and vendors from public sources (filings, litigation, news) | entity → risk report | web-search, company-lookup | C | S1 | P2 |
| `policy-analyst` | Policy Analyst | Analyzes a regulation or policy proposal: who it affects and how | policy text → impact analysis | web-search | C | S1 | P2 |
| `hypothesis-generator` | Hypothesis Generator | Proposes testable hypotheses from data or literature | context → hypotheses | — | A | S0 | P2 |
| `citation-manager` | Citation Manager | Formats references, finds DOIs and checks every citation exists | references → verified bibliography | scholarly APIs | A | S1 | P2 |

---
### FAMILY 4 — ACTION (`agents/action/`)

Agents that do things: operate browsers and computers, handle files, call APIs, control devices.

#### 7.13 Browser and web automation — `agents/action/browser/` · ID prefix `browser/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `web-navigator` | Browser Operator | Completes multi-step tasks on websites using the accessibility tree, DOM and screenshots; prefers site-declared tools (WebMCP) when present | goal + start URL → result + trace | browser | C | S3 | P0 |
| `web-form-filler` | Web Form Filler | Fills web forms from structured data, validates each field, stops before submit for approval | data + URL → filled form + review | browser | A | S2 | P0 |
| `web-scraper` | Web Scraper | Extracts structured data from pages into a schema, handles pagination, respects robots.txt and terms | URL + schema → records | browser, http | A | S1 | P0 |
| `site-crawler` | Site Crawler | Crawls a site to build a sitemap, content inventory or knowledge base | root URL → page inventory | http | A | S1 | P1 |
| `page-change-monitor` | Page Change Monitor | Watches pages for changes (price, stock, content, status) and alerts with a diff | URLs + rules → alerts | http, browser | C | S1 | P1 |
| `web-tester` | Web App Tester | Explores a web app, writes and runs end-to-end tests (Playwright) and files bug reports with screenshots | app URL + flows → tests + bugs | browser | C | S2 | P1 |
| `booking-agent` | Booking Assistant | Finds availability and prepares bookings (tables, appointments, tickets); the user confirms | request → options + prepared booking | browser | C | S3 | P2 |
| `checkout-assistant` | Checkout Assistant | Compares carts, applies valid coupons, prepares checkout and stops before payment | cart → optimized cart | browser | C | S3 | P2 |
| `tab-organizer` | Tab & Reading Organizer | Summarizes and groups open tabs, saves them to a reading list | tabs → groups + summaries | browser | A | S1 | P2 |
| `web-to-api` | Website-to-Tool Converter | Learns a website's workflows and exposes them as callable tools / MCP endpoints | site + workflows → tool definitions | browser | C | S2 | P2 |
| `web-archiver` | Web Archiver | Saves pages as PDF/WARC with metadata for records and evidence | URLs → archives | browser | A | S2 | P2 |
| `secure-login-helper` | Secure Login Helper | Handles sign-in flows by delegating credentials to the user's password manager; never sees or stores secrets | site → authenticated session | browser, password manager | A | S4 | P2 |

#### 7.14 Computer use and desktop — `agents/action/computer-use/` · ID prefix `computer-use/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `shell-operator` | Shell Operator | Runs terminal commands in a sandbox, explains them and asks before anything destructive | goal → commands + output | shell-sandbox | A | S3 | P0 |
| `desktop-operator` | Desktop Operator | Operates desktop apps through screenshots, mouse and keyboard to finish tasks | goal → completed task + trace | computer-use, screenshot-understander | C | S3 | P1 |
| `app-automator` | App Automator | Automates apps through accessibility and scripting APIs (AppleScript, UI Automation, AT-SPI) for reliability | goal → actions | OS automation | A | S3 | P1 |
| `mobile-operator` | Mobile Operator | Drives Android/iOS apps on devices or emulators for tasks and testing | goal → actions + result | device bridge | C | S3 | P2 |
| `rpa-bridge` | Legacy App Bridge | Automates legacy apps with no API (green screens, old desktop software), replacing brittle RPA scripts | workflow → executed steps | computer-use | C | S3 | P2 |
| `macro-recorder` | Teach-by-Showing Recorder | Watches the user do a task once and turns it into a reusable, parameterized workflow | recording → workflow | screen recorder | C | S2 | P2 |
| `settings-configurator` | Settings Configurator | Changes OS and app settings safely with a before/after record and rollback | desired setting → change + rollback | OS automation | A | S3 | P2 |
| `clipboard-assistant` | Clipboard Transformer | Transforms whatever is copied (reformat, translate, extract, clean) | clipboard → new clipboard | clipboard | A | S2 | P2 |
| `notification-triager` | Notification Triager | Filters and batches OS/app notifications into a digest, surfacing only urgent ones | notifications → digest + alerts | OS notifications | A | S1 | P2 |

#### 7.15 Files and documents — `agents/action/documents/` · ID prefix `documents/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `document-parser` | Document Parser | Converts PDF, DOCX, PPTX, HTML and scans into clean Markdown/JSON, keeping headings, tables and reading order | file → structured content | documents, ocr | A | S1 | P0 |
| `table-extractor` | Table Extractor | Pulls tables out of PDFs and images into CSV/XLSX, including multi-page tables | file → tables | documents, ocr | A | S1 | P0 |
| `spreadsheet-agent` | Spreadsheet Agent | Reads and edits spreadsheets by instruction: formulas, pivots, cleaning, charts | sheet + instruction → updated sheet | spreadsheet | A | S2 | P0 |
| `invoice-receipt-parser` | Invoice & Receipt Parser | Extracts vendor, dates, line items, taxes (incl. GST/VAT) and totals; checks the arithmetic | invoice/receipt → structured record | documents, ocr | A | S1 | P0 |
| `file-organizer` | File Organizer | Sorts files into folders by content and rules, renames consistently, shows a plan before moving | folder + rules → move plan → executed | filesystem | A | S2 | P0 |
| `file-finder` | File Finder | Finds files by natural description ("the contract I edited last week about the Pune office") | description → files | filesystem, vector-store | A | S1 | P1 |
| `format-converter` | Format Converter | Converts between formats (DOCX ↔ PDF ↔ MD, XLSX ↔ CSV, image formats) | file + target → file | documents | A | S2 | P1 |
| `doc-generator` | Document Generator | Creates documents and reports from templates and data (DOCX, PDF, letters, certificates) | template + data → document | documents | A | S2 | P1 |
| `slide-deck-builder` | Slide Deck Builder | Turns an outline, document or data into a presentation with a consistent design | content → deck (PPTX/PDF) | documents | C | S2 | P1 |
| `doc-classifier` | Document Classifier | Identifies document type (invoice, contract, ID, payslip, bank statement) and routes it | file → type + confidence | documents | A | S1 | P1 |
| `doc-comparer` | Document Comparer | Redline comparison of two versions with a plain-language summary of changes | doc A + doc B → redline + summary | documents | A | S1 | P1 |
| `pdf-form-filler` | PDF Form Filler | Fills fillable and flat PDF forms from data | PDF + data → filled PDF | documents | A | S2 | P1 |
| `doc-redactor` | Document Redactor | Permanently redacts sensitive data in PDFs and images (true removal, not black boxes over text) | doc + rules → redacted doc | documents, pii-redactor | A | S2 | P1 |
| `long-doc-navigator` | Long Document Navigator | Q&A and navigation in very long documents (manuals, annual reports, regulations) | doc + question → answer + page refs | documents, vector-store | C | S1 | P1 |
| `duplicate-finder` | Duplicate Finder | Finds duplicate and near-duplicate files and photos and proposes cleanup | folder → duplicate groups | filesystem | A | S1 | P2 |
| `metadata-tagger` | Metadata Tagger | Auto-tags files with topics, people, dates and projects | files → tags | filesystem | A | S2 | P2 |
| `archive-backup` | Archive & Backup Agent | Backs up, versions and applies retention rules to files | policy → backup runs + report | storage | A | S2 | P2 |
| `e-signature-prep` | E-Signature Preparer | Prepares documents for signing (fields, signer order) and stops before sending | doc + signers → ready envelope | e-sign API | A | S3 | P2 |

#### 7.16 Workflow and integration — `agents/action/integration/` · ID prefix `integration/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `api-caller` | API Caller | Calls REST/GraphQL APIs from an OpenAPI spec based on a plain-language intent | intent + spec → API response | http | A | S3 | P0 |
| `workflow-builder` | Workflow Builder | Turns a description into an automation workflow (n8n, Zapier-style, or Agents for Everything YAML) | description → workflow definition | — | C | S2 | P1 |
| `webhook-handler` | Event Handler | Receives webhooks/events, classifies them and triggers the right agent | event → triggered run | queue | A | S2 | P1 |
| `notification-dispatcher` | Notification Dispatcher | Sends alerts by email, chat, SMS or push using routing and quiet-hours rules | message + rules → deliveries | email, chat, sms | A | S3 | P1 |
| `mcp-server-generator` | MCP Server Generator | Wraps any API, CLI or database into an MCP server with tests | API spec/CLI → MCP server code | code sandbox | C | S2 | P1 |
| `data-sync` | Data Sync Agent | Keeps records in sync between apps (CRM ↔ sheet ↔ database) and resolves conflicts | source + target → sync report | connectors | A | S3 | P2 |
| `field-mapper` | Field Mapper | Maps fields between two systems' schemas with transformation rules | schema A + schema B → mapping | — | A | S0 | P2 |
| `email-to-action` | Email-to-Action | Parses inbound emails into structured actions, tickets or records | email → action record | email | A | S1 | P2 |

#### 7.17 Physical world, IoT and robotics — `agents/action/physical/` · ID prefix `physical/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `smart-home-controller` | Smart Home Controller | Controls lights, climate, locks and appliances by voice or text (Home Assistant, Matter) with confirmation for locks/security | command → device actions | home automation | C | S3 | P1 |
| `sensor-monitor` | Sensor Monitor | Watches IoT telemetry, detects anomalies and alerts | telemetry → anomalies + alerts | time-series DB | A | S1 | P2 |
| `energy-optimizer` | Home/Building Energy Optimizer | Schedules appliances and HVAC to cut cost and carbon using tariffs and weather | devices + tariffs → schedule | home automation, weather | A | S3 | P2 |
| `robot-task-planner` | Robot Task Planner | Turns instructions into safe robot action plans (ROS 2) with workspace constraints | instruction + map → action plan | ROS bridge | C | S4 | P2 |
| `drone-mission-planner` | Drone Mission Planner | Plans survey and inspection flights within airspace rules | area + goal → flight plan | maps, airspace data | C | S4 | P2 |
| `vehicle-diagnostics` | Vehicle Diagnostics | Explains OBD-II fault codes, likely causes and urgency | codes + vehicle → explanation | OBD reader | A | S0 | P2 |

---

### FAMILY 5 — BUILDERS (`agents/builders/`)

Agents for building and running technology: software, infrastructure, data, AI, security, IT.

#### 7.18 Software engineering — `agents/builders/coding/` · ID prefix `coding/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `code-generator` | Feature Implementer | Implements a feature from a spec inside an existing repo, following its conventions | spec + repo → diff | repo, shell-sandbox | C | S2 | P0 |
| `code-reviewer` | Code Reviewer | Reviews diffs for bugs, security, performance and style; posts inline comments | diff → review comments | repo | A | S1 | P0 |
| `bug-fixer` | Bug Fixer | Reproduces a reported bug, finds the root cause, patches it and adds a regression test | issue + repo → fix PR | repo, shell-sandbox | C | S2 | P0 |
| `test-writer` | Test Writer | Writes unit and integration tests to cover untested behaviour | code → tests | repo, shell-sandbox | A | S2 | P0 |
| `codebase-qa` | Codebase Q&A | Answers questions about a codebase ("where is auth handled?", "how does billing work?") | question + repo → answer + file refs | repo, code search | C | S1 | P0 |
| `refactorer` | Refactorer | Performs behaviour-preserving refactors, verified by tests | code + goal → diff | repo, shell-sandbox | A | S2 | P1 |
| `doc-writer` | Code Documentation Writer | Writes docstrings, READMEs and API reference | code → docs | repo | A | S2 | P1 |
| `pr-describer` | PR & Commit Writer | Writes PR descriptions, commit messages and changelog entries | diff → text | repo | A | S0 | P1 |
| `issue-triager` | Issue Triager | Labels, deduplicates and prioritizes issues; asks reporters for missing repro info | issue → labels + priority + reply | issue tracker | A | S3 | P1 |
| `dependency-updater` | Dependency Updater | Upgrades dependencies and fixes breaking changes, with release-note summaries | repo → upgrade PR | repo, shell-sandbox | C | S2 | P1 |
| `ci-fixer` | CI Fixer | Diagnoses failing CI runs and proposes or applies fixes | failed run → diagnosis + fix | CI API, repo | C | S2 | P1 |
| `frontend-builder` | Frontend Builder | Builds UI components and pages from designs or specs, with accessibility | design/spec → components | repo, browser | C | S2 | P1 |
| `app-builder` | App Prototyper | Builds a working full-stack prototype from a prompt | idea → running app | shell-sandbox | C | S2 | P1 |
| `code-explainer` | Code Explainer | Explains code to newcomers or non-programmers, line by line or at architecture level | code + level → explanation | — | A | S0 | P1 |
| `scaffolder` | Project Scaffolder | Creates new project boilerplate (structure, configs, CI, linting) from a description | description → project | shell-sandbox | A | S2 | P1 |
| `migration-agent` | Migration Agent | Framework and language migrations (JS → TS, Java 8 → 21, React class → hooks) | repo + target → migration PRs | repo, shell-sandbox | C | S2 | P2 |
| `legacy-modernizer` | Legacy Modernizer | Documents and modernizes legacy code (COBOL, VB6, PL/SQL) | legacy code → docs + new code | repo | C | S2 | P2 |
| `performance-optimizer` | Performance Optimizer | Profiles code and optimizes hot paths with benchmarks | code + benchmark → diff + results | shell-sandbox | C | S2 | P2 |
| `api-client-generator` | SDK Generator | Generates typed client SDKs from OpenAPI/GraphQL specs | spec → SDK | — | A | S0 | P2 |
| `db-schema-designer` | Database Schema Designer | Designs schemas and migrations from requirements | requirements → schema + migrations | — | A | S0 | P2 |
| `i18n-agent` | Internationalization Agent | Extracts strings, manages translation files, flags layout issues | repo → i18n changes | repo, translator | A | S2 | P2 |
| `snippet-helper` | Regex/SQL/Shell Helper | Writes and explains regexes, SQL queries and shell one-liners with tests | need → snippet + explanation | — | A | S0 | P2 |

#### 7.19 DevOps, cloud and SRE — `agents/builders/devops/` · ID prefix `devops/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `log-analyzer` | Log Analyzer | Clusters and explains errors in logs, links them to recent changes | logs → issues + explanation | log store | A | S1 | P0 |
| `incident-responder` | Incident Responder | Correlates alerts, logs, metrics and deploys; suggests root cause and mitigation; runs approved runbooks | incident → hypothesis + actions | observability, runbooks | C | S3 | P1 |
| `alert-triager` | Alert Triager | Deduplicates and prioritizes alerts to cut noise | alerts → grouped, ranked alerts | observability | A | S1 | P1 |
| `iac-generator` | Infrastructure-as-Code Writer | Writes Terraform, Pulumi or Kubernetes manifests from requirements, with policy checks | requirements → IaC | shell-sandbox | A | S2 | P1 |
| `cloud-cost-optimizer` | Cloud Cost Optimizer | Finds idle and oversized resources and proposes savings | billing + usage → savings plan | cloud APIs | C | S1 | P1 |
| `postmortem-writer` | Postmortem Writer | Writes a blameless postmortem from the incident timeline and chat | timeline → postmortem | chat, observability | A | S1 | P1 |
| `k8s-operator` | Kubernetes Assistant | Diagnoses cluster problems and runs safe kubectl operations with approval | issue → diagnosis + commands | kubernetes | C | S3 | P2 |
| `deploy-agent` | Release Agent | Runs releases with canary checks and automatic rollback | release → deploy report | CI/CD | C | S4 | P2 |
| `runbook-executor` | Runbook Executor | Executes written runbooks step by step with checks and approvals | runbook + context → executed steps | shell-sandbox | C | S3 | P2 |
| `config-drift-detector` | Config Drift Detector | Finds differences between declared and actual infrastructure | IaC + live state → drift report | cloud APIs | A | S1 | P2 |
| `db-admin` | Database Assistant | Query tuning, index advice, backup and health checks | DB + issue → recommendations | sql | A | S2 | P2 |
| `uptime-monitor` | Uptime Monitor | Synthetic checks and status-page updates | endpoints → status + alerts | http | A | S2 | P2 |
| `containerizer` | Containerizer | Writes Dockerfiles and compose files for an app, minimal and secure | repo → container config | shell-sandbox | A | S2 | P2 |

#### 7.20 Data and analytics — `agents/builders/data/` · ID prefix `data/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `text-to-sql` | Text-to-SQL | Turns questions into safe, read-only SQL using the schema and a semantic layer; explains the query | question + schema → SQL + result | sql | A | S1 | P0 |
| `data-analyst` | Data Analyst | Loads data, explores it, runs statistics, makes charts and writes insights (code interpreter) | data + question → analysis report | python-sandbox | C | S1 | P0 |
| `data-cleaner` | Data Cleaner | Fixes types, missing values, duplicates, outliers and inconsistent formats, with a change log | dataset → clean dataset + log | python-sandbox | A | S2 | P0 |
| `chart-maker` | Chart Maker | Picks the right chart for the data and question and renders it with a caption | data + question → chart | python-sandbox | A | S0 | P1 |
| `metric-explainer` | Metric Explainer | Answers "why did this number change?" by drilling into dimensions | metric + period → drivers | sql | C | S1 | P1 |
| `anomaly-detector` | Anomaly Detector | Detects and explains anomalies in metrics and time series | series → anomalies | python-sandbox | A | S1 | P1 |
| `forecaster` | Forecaster | Time-series forecasts with uncertainty ranges and assumptions | history → forecast | python-sandbox | A | S1 | P1 |
| `schema-mapper` | Schema Mapper | Maps source columns to a target schema with transformations | source + target schema → mapping | — | A | S0 | P1 |
| `data-labeler` | Data Labeler | Labels data with an LLM and routes low-confidence items to humans | items + guidelines → labels | review queue | A | S1 | P1 |
| `dashboard-builder` | Dashboard Builder | Builds dashboards from KPI definitions (Metabase, Superset, Streamlit, HTML) | KPIs + data → dashboard | BI tools | C | S2 | P2 |
| `etl-builder` | Pipeline Builder | Designs and writes data pipelines (dbt, Airflow, Dagster) | sources + target → pipeline code | repo | C | S2 | P2 |
| `data-quality-monitor` | Data Quality Monitor | Tests freshness, volume, schema and distribution drift | tables → quality report | sql | A | S1 | P2 |
| `synthetic-data-generator` | Synthetic Data Generator | Creates privacy-safe synthetic datasets that keep statistical properties | schema/sample → synthetic data | python-sandbox | A | S0 | P2 |
| `ab-test-analyst` | Experiment Analyst | Analyzes A/B tests: significance, effect size, guardrail metrics | experiment data → readout | python-sandbox | A | S1 | P2 |
| `data-catalog-documenter` | Data Catalog Documenter | Documents tables and columns, infers lineage and owners | warehouse → catalog entries | sql | A | S1 | P2 |

#### 7.21 AI and ML engineering — `agents/builders/ai-engineering/` · ID prefix `ai-engineering/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `prompt-engineer` | Prompt Engineer | Writes, tests and improves prompts for a task with an eval set | task + examples → prompt + scores | eval harness | A | S0 | P1 |
| `rag-builder` | RAG Builder | Builds a retrieval pipeline for a corpus and tunes chunking, embedding and retrieval against evals | corpus + questions → tuned pipeline | vector-store, eval harness | C | S2 | P1 |
| `automl-trainer` | AutoML Trainer | Trains and tunes baseline models on tabular data and reports results honestly | dataset + target → model + report | python-sandbox | C | S2 | P2 |
| `feature-engineer` | Feature Engineer | Proposes and tests features for a predictive model | dataset → features + lift | python-sandbox | A | S1 | P2 |
| `model-evaluator` | Model Evaluator | Metrics, error analysis and fairness slices for ML models | model + test set → evaluation | python-sandbox | A | S1 | P2 |
| `finetune-data-curator` | Fine-tune Data Curator | Builds and cleans fine-tuning datasets: dedupe, quality filters, format | raw examples → dataset | python-sandbox | A | S1 | P2 |
| `model-monitor` | Model Monitor | Tracks drift and performance of production models and alerts | predictions + outcomes → drift report | metrics store | A | S1 | P2 |
| `paper-to-code` | Paper Implementer | Implements the method from an ML paper and reproduces a key result | paper → code + results | python-sandbox | C | S2 | P2 |

#### 7.22 Cybersecurity — `agents/builders/security/` · ID prefix `security/`

All security agents are defensive or for authorized testing only.

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `vuln-triager` | Vulnerability Triager | Prioritizes scanner findings by reachability, exploitability and business impact | findings → ranked list + fixes | scanners, repo | A | S1 | P1 |
| `secure-code-reviewer` | Secure Code Reviewer | Finds and explains security flaws in code and proposes fixes | code/diff → findings | repo | A | S1 | P1 |
| `secret-scanner` | Secret Scanner | Finds leaked keys in repos and history and guides rotation | repo → findings + steps | repo | A | S1 | P1 |
| `phishing-analyzer` | Phishing Analyzer | Analyzes suspicious emails, links and attachments (in a sandbox) and gives a verdict | email → verdict + indicators | sandbox, threat intel | A | S1 | P1 |
| `threat-intel-summarizer` | Threat Intel Briefer | Turns threat feeds into briefings mapped to MITRE ATT&CK and your assets | feeds → briefing | threat intel | C | S1 | P2 |
| `siem-analyst` | SOC Analyst | Investigates alerts, queries the SIEM, builds a timeline and recommends response | alert → investigation | SIEM | C | S1 | P2 |
| `access-reviewer` | Access Reviewer | Reviews permissions for least privilege and flags unusual access | access lists → findings | IAM APIs | A | S1 | P2 |
| `security-compliance-auditor` | Security Compliance Auditor | Maps controls and evidence to ISO 27001, SOC 2, PCI DSS and local regulator frameworks | evidence → gap report | — | C | S1 | P2 |
| `pentest-assistant` | Pentest Assistant | For authorized engagements only: scope-checked recon, test planning and report writing | scope + findings → plan/report | scope validator | C | S3 | P2 |
| `sbom-auditor` | SBOM & Licence Auditor | Builds software bills of materials and flags licence and supply-chain risk | repo → SBOM + risks | repo | A | S1 | P2 |
| `security-awareness-trainer` | Security Awareness Trainer | Creates training content and quizzes tailored to current threats | org profile → training modules | — | A | S0 | P2 |
| `security-incident-reporter` | Security Incident Reporter | Writes incident reports in the format regulators require (e.g. CERT-In style timelines) | incident data → report | — | A | S1 | P2 |

#### 7.23 IT support and administration — `agents/builders/it-support/` · ID prefix `it-support/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `helpdesk-agent` | IT Helpdesk Agent | First-line IT support: troubleshoots with the user, uses the KB, creates tickets when stuck | issue → resolution or ticket | KB, ticketing | C | S2 | P1 |
| `access-request-handler` | Access Request Handler | Processes access requests with the right approvers and provisions after approval | request → approval flow + grant | IAM, ticketing | C | S3 | P2 |
| `device-setup-guide` | Device Setup Guide | Step-by-step device provisioning and onboarding checklists | device + role → checklist | MDM | A | S1 | P2 |
| `license-manager` | Software Licence Manager | Tracks licence usage and suggests seats to reclaim | usage → report | SaaS admin APIs | A | S1 | P2 |
| `account-recovery-guide` | Account Recovery Guide | Guides users through official self-service recovery flows; never handles passwords | issue → guided steps | KB | A | S1 | P2 |
| `asset-inventory` | IT Asset Inventory | Keeps hardware/software inventory current and flags end-of-life items | sources → inventory | MDM, CMDB | A | S1 | P2 |

---
### FAMILY 6 — BUSINESS FUNCTIONS (`agents/business/`)

Agents for the jobs every organization does: communicate, meet, write, market, sell, support, account, comply, hire, operate.

#### 7.24 Email and messaging — `agents/business/communication/` · ID prefix `communication/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `inbox-triager` | Inbox Triager | Sorts, prioritizes and labels email; surfaces what is urgent and what needs a reply | inbox → labelled, ranked list | email | A | S1 | P0 |
| `email-drafter` | Email Drafter | Drafts replies and new emails in the user's voice; saves as drafts, never sends without approval | thread + intent → draft | email | A | S2 | P0 |
| `chat-summarizer` | Chat Summarizer | Summarizes Slack, Teams, WhatsApp or Discord threads and channels with decisions and asks | messages → summary | chat | A | S1 | P0 |
| `follow-up-tracker` | Follow-up Tracker | Tracks threads waiting for a reply and drafts polite nudges | sent mail → reminders + drafts | email | A | S2 | P1 |
| `newsletter-digest` | Newsletter Digest | Merges many newsletters into one short daily or weekly digest | newsletters → digest | email | C | S1 | P1 |
| `business-messaging-bot` | WhatsApp/SMS Business Agent | Customer conversations on WhatsApp, SMS and RCS with templates, opt-in and handoff | messages ↔ replies + actions | messaging APIs | C | S3 | P1 |
| `unsubscribe-cleaner` | Unsubscribe Cleaner | Finds unwanted mailing lists and unsubscribes after the user approves the list | inbox → list → unsubscribes | email, browser | A | S3 | P2 |
| `announcement-writer` | Announcement Writer | Writes internal announcements in the right tone for the audience | facts + audience → announcement | — | A | S0 | P2 |
| `tone-checker` | Tone Checker | Flags messages that may read as rude, unclear or risky before sending | draft → issues + rewrite | — | A | S0 | P2 |
| `contact-manager` | Contact Manager | Deduplicates contacts and enriches them from email signatures | contacts + mail → clean contacts | contacts, email | A | S2 | P2 |

#### 7.25 Meetings and calendar — `agents/business/meetings/` · ID prefix `meetings/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `meeting-scheduler` | Meeting Scheduler | Finds times across calendars and time zones, proposes slots and sends invites after approval | request → invite | calendar, email | C | S3 | P0 |
| `meeting-notetaker` | Meeting Notetaker | Transcribes meetings and writes summaries with decisions, risks and action items | recording/live audio → notes | stt, speaker-diarizer | C | S1 | P0 |
| `action-item-extractor` | Action Item Extractor | Pulls tasks with owners and due dates from notes, transcripts or chats and files them in task tools | text → tasks | task manager APIs | A | S2 | P0 |
| `meeting-prep` | Meeting Prep Brief | Briefs on attendees, past threads, open issues and a suggested agenda | meeting → brief | calendar, email, search | C | S1 | P1 |
| `meeting-follow-up` | Meeting Follow-up | Drafts the recap email and tracks commitments until done | notes → recap draft + tracking | email | A | S2 | P1 |
| `agenda-builder` | Agenda Builder | Builds a time-boxed agenda from goals and pre-reads | goals → agenda | — | A | S0 | P2 |
| `calendar-optimizer` | Calendar Optimizer | Protects focus time, groups meetings and flags conflicts and overload | calendar → proposed changes | calendar | A | S2 | P2 |
| `live-meeting-copilot` | Live Meeting Copilot | Answers questions and fetches facts during a meeting, privately to the user | live transcript → suggestions | stt, rag-qa | C | S1 | P2 |

#### 7.26 Writing and content creation — `agents/business/content/` · ID prefix `content/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `blog-writer` | Blog Writer | Researches, outlines and drafts articles with sources, then polishes for readability and SEO | topic + brief → article | web-search | C | S1 | P1 |
| `copywriter` | Copywriter | Writes ad, landing-page and product copy in several variants | brief → copy variants | — | A | S0 | P1 |
| `social-post-writer` | Social Post Writer | Writes platform-specific posts and threads (LinkedIn, X, Instagram) | content/topic → posts | — | A | S0 | P1 |
| `content-repurposer` | Content Repurposer | Turns one piece into many (video → blog, blog → thread, talk → newsletter) | content → set of formats | stt | C | S0 | P1 |
| `technical-writer` | Technical Writer | Writes user guides, tutorials and how-tos from product knowledge | product info → docs | — | A | S0 | P1 |
| `editor` | Editor | Structural and line editing with tracked suggestions and reasons | draft → suggestions | — | A | S0 | P1 |
| `seo-optimizer` | On-page SEO Optimizer | Improves a page's headings, keywords, metadata and internal links | page + keywords → changes | web-search | A | S0 | P1 |
| `script-writer` | Script Writer | Video, podcast and presentation scripts with timing cues | brief → script | — | A | S0 | P2 |
| `newsletter-writer` | Newsletter Writer | Writes recurring newsletters from curated links and updates | inputs → newsletter | — | A | S0 | P2 |
| `press-release-writer` | Press Release Writer | Writes press releases in standard format with quotes and boilerplate | facts → release | — | A | S0 | P2 |
| `grant-writer` | Grant Writer | Drafts grant and funding proposals against the funder's criteria | project + call → proposal | documents | C | S0 | P2 |
| `speech-writer` | Speech Writer | Writes speeches for a speaker, occasion and duration | brief → speech | — | A | S0 | P2 |
| `storyteller` | Storyteller | Fiction, children's stories and narratives with consistent characters | prompt → story | — | A | S0 | P2 |
| `localizer` | Localizer | Adapts content culturally for a market (idioms, examples, units, references), beyond translation | content + market → localized | translator | A | S0 | P2 |
| `style-matcher` | Personal Style Matcher | Learns an author's writing style from their own samples and drafts in it | samples + brief → draft | — | A | S0 | P2 |

#### 7.27 Marketing and growth — `agents/business/marketing/` · ID prefix `marketing/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `campaign-planner` | Campaign Planner | Turns goals into a channel plan, budget split, messaging and calendar | goals + budget → plan | — | C | S0 | P1 |
| `ad-creative-generator` | Ad Creative Generator | Ad copy and image variants sized to each platform's specs | brief → creatives | image-generator | C | S0 | P1 |
| `seo-auditor` | SEO Auditor | Site-wide technical SEO audit with prioritized fixes | site → audit report | site-crawler | C | S1 | P1 |
| `keyword-researcher` | Keyword Researcher | Finds keywords with intent, volume and difficulty and clusters them | topic → keyword clusters | SEO APIs | A | S1 | P1 |
| `brand-monitor` | Brand Monitor | Tracks brand mentions and sentiment across web and social and flags crises early | brand → alerts + report | news, social APIs | C | S1 | P1 |
| `review-responder` | Review Responder | Drafts replies to customer reviews in brand voice, escalating serious complaints | review → reply draft | review platforms | A | S2 | P1 |
| `social-media-manager` | Social Media Manager | Plans, schedules and posts content and drafts replies, with approval before posting | content plan → scheduled posts | social APIs | C | S3 | P2 |
| `email-marketing-agent` | Email Marketing Agent | Builds segments and sequences and tests subject lines | goals + list → campaigns | ESP API | C | S3 | P2 |
| `landing-page-builder` | Landing Page Builder | Builds landing pages with copy, layout and analytics | brief → page | frontend-builder | C | S2 | P2 |
| `audience-segmenter` | Audience Segmenter | Clusters customers into actionable segments with descriptions | customer data → segments | python-sandbox | A | S1 | P2 |
| `marketing-reporter` | Marketing Reporter | Weekly performance narrative across analytics and ad platforms | platform data → report | analytics APIs | C | S1 | P2 |
| `competitor-ad-tracker` | Competitor Ad Tracker | Tracks competitors' ads and messaging changes in public ad libraries | competitors → changes digest | ad libraries | A | S1 | P2 |
| `influencer-scout` | Influencer Scout | Finds relevant creators and checks audience fit and brand safety | brief → shortlist | social APIs | A | S1 | P2 |
| `geo-optimizer` | AI-Search (GEO) Optimizer | Optimizes content so AI answer engines find and cite it | content + topics → recommendations | answer-engine | A | S1 | P2 |

#### 7.28 Sales and CRM — `agents/business/sales/` · ID prefix `sales/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `lead-finder` | Lead Finder | Finds companies matching an ideal customer profile from public sources | ICP → company list | web-search, company-lookup | C | S1 | P1 |
| `lead-enricher` | Lead Enricher | Adds firmographics, tech stack and recent news to leads | lead → enriched lead | company-lookup | A | S1 | P1 |
| `lead-scorer` | Lead Scorer | Scores leads by fit and intent with reasons | leads → scores | CRM | A | S1 | P1 |
| `account-researcher` | Account Researcher | Pre-call brief: company priorities, people, news, likely needs | account → brief | web-search, CRM | C | S1 | P1 |
| `outreach-personalizer` | Outreach Personalizer | Writes personalized outreach emails and sequences from research; drafts only | lead + research → sequence | — | A | S2 | P1 |
| `crm-updater` | CRM Updater | Logs calls, emails and meetings into the right CRM fields automatically | activity → CRM updates | CRM | A | S3 | P1 |
| `proposal-generator` | Proposal Generator | Builds proposals and statements of work from templates and discovery notes | notes + template → proposal | documents | C | S2 | P1 |
| `rfp-responder` | RFP & Questionnaire Responder | Answers RFPs and security questionnaires from an approved answer library, flagging new questions | RFP → draft answers | rag-qa | C | S2 | P1 |
| `sales-call-analyzer` | Sales Call Analyzer | Summarizes calls, extracts objections and next steps, gives coaching tips | call → analysis | stt | C | S1 | P2 |
| `quote-builder` | Quote Builder | Builds quotes using price books and discount rules | requirements → quote | CRM | A | S2 | P2 |
| `pipeline-forecaster` | Pipeline Forecaster | Forecasts revenue from pipeline with risk flags per deal | pipeline → forecast | CRM | A | S1 | P2 |
| `inbound-qualifier` | Inbound Lead Qualifier | Chats with inbound leads, qualifies them and books meetings | conversation → qualified lead + booking | calendar, CRM | C | S3 | P2 |
| `sales-roleplay-coach` | Sales Roleplay Coach | Simulates buyers for practice and scores the conversation | scenario → roleplay + feedback | — | A | S0 | P2 |

#### 7.29 Customer support and success — `agents/business/support/` · ID prefix `support/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `support-chatbot` | Support Assistant | Answers customer questions from the KB and policies with citations; hands off to humans cleanly | question → answer or handoff | rag-qa | C | S1 | P0 |
| `ticket-triager` | Ticket Triager | Classifies, prioritizes and routes tickets; detects duplicates | ticket → category + priority + queue | ticketing | A | S2 | P0 |
| `reply-drafter` | Reply Drafter | Drafts grounded replies for human agents to send | ticket + KB → draft | rag-qa | A | S2 | P0 |
| `kb-writer` | Knowledge Base Writer | Turns resolved tickets into KB articles and finds gaps in the KB | tickets → articles + gaps | KB | C | S2 | P1 |
| `escalation-detector` | Escalation Detector | Detects anger, churn risk, legal threats or safety issues and escalates | conversation → flags | — | A | S1 | P1 |
| `order-status-agent` | Order Status Agent | Looks up orders, shipping and refunds through APIs and explains status | customer + order → status | order APIs | A | S1 | P1 |
| `voice-of-customer` | Voice of Customer Analyst | Finds themes across tickets, reviews, calls and surveys and quantifies them | feedback sources → report | — | C | S1 | P1 |
| `returns-refunds-agent` | Returns & Refunds Agent | Checks return eligibility and prepares refunds; refunds need human approval | request → decision + prepared refund | order APIs | C | S4 | P2 |
| `support-qa-auditor` | Support QA Auditor | Scores support conversations against a quality rubric | conversations → scores + coaching | — | A | S1 | P2 |
| `customer-onboarding-guide` | Customer Onboarding Guide | Guides new customers through setup with in-app tips and check-ins | account → onboarding flow | product APIs | C | S2 | P2 |
| `churn-risk-predictor` | Churn Risk Predictor | Predicts accounts at risk and suggests save actions | usage + support data → risk list | analytics | A | S1 | P2 |

#### 7.30 Finance and accounting — `agents/business/finance/` · ID prefix `finance/`

Finance agents give information and prepare work for humans. They do not give investment advice and do not move money on their own.

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `transaction-categorizer` | Transaction Categorizer | Categorizes transactions to the chart of accounts with confidence | transactions → categories | accounting API | A | S1 | P1 |
| `accounts-payable` | Accounts Payable Agent | Invoice intake, validation, PO/receipt matching and an approval queue | invoices → matched, queued bills | invoice-receipt-parser, ERP | C | S4 | P1 |
| `bank-reconciler` | Bank Reconciler | Matches bank lines to ledger entries and explains exceptions | bank + ledger → matches + exceptions | accounting API | A | S2 | P1 |
| `expense-auditor` | Expense Auditor | Flags policy breaches, duplicates and suspicious claims | expense claims → flags | expense API | A | S1 | P1 |
| `financial-statement-analyzer` | Financial Statement Analyzer | Ratios, trends and red flags from financial statements and annual reports | statements → analysis | documents | C | S1 | P1 |
| `accounts-receivable` | Collections Assistant | Drafts polite payment reminders and tracks promises to pay | ageing report → reminders | email | C | S3 | P2 |
| `budget-variance-analyst` | Budget Variance Analyst | Explains budget versus actual differences | budget + actuals → commentary | spreadsheet | A | S1 | P2 |
| `cash-flow-forecaster` | Cash Flow Forecaster | 13-week cash forecast from receivables, payables and history | ledgers → forecast | python-sandbox | A | S1 | P2 |
| `financial-report-writer` | Financial Report Writer | Writes management commentary and board finance narratives | numbers → narrative | — | A | S0 | P2 |
| `tax-doc-organizer` | Tax Document Organizer | Collects and organizes tax documents and builds a checklist (no tax advice) | documents → organized pack | documents | A | S1 | P2 |
| `payroll-checker` | Payroll Checker | Checks payroll runs for anomalies before approval | payroll run → anomalies | payroll API | A | S1 | P2 |
| `audit-assistant` | Audit Assistant | Sampling, evidence requests and workpaper drafts | ledger + scope → workpapers | — | C | S1 | P2 |
| `spend-analyzer` | Spend Analyzer | Classifies spend by category and supplier and finds savings | AP data → spend cube + ideas | — | A | S1 | P2 |
| `earnings-call-analyzer` | Earnings Call Analyzer | Summarizes earnings calls and filings and compares guidance with prior quarters | transcript + filings → analysis | — | C | S1 | P2 |

#### 7.31 Legal and compliance — `agents/business/legal/` · ID prefix `legal/`

Legal agents support lawyers and compliance staff. They do not replace legal advice.

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `contract-analyzer` | Contract Analyzer | Extracts key clauses and flags risks against a playbook of standard positions | contract + playbook → risk report | documents | C | S1 | P1 |
| `nda-reviewer` | NDA Reviewer | Fast NDA triage: accept, redline or escalate | NDA → verdict + redlines | documents | A | S1 | P1 |
| `compliance-monitor` | Regulatory Change Monitor | Tracks new laws and regulator notices and maps them to internal obligations | jurisdictions + topics → alerts + mapping | news-monitor | C | S1 | P1 |
| `terms-simplifier` | Terms Simplifier | Explains terms of service and privacy policies in plain language and highlights risky clauses | policy text → summary + flags | — | A | S0 | P1 |
| `contract-drafter` | Contract Drafter | Drafts contracts from approved templates and term sheets | terms + template → draft | documents | A | S2 | P2 |
| `redline-negotiator` | Redline Negotiator | Proposes counter-redlines with reasons based on the playbook | redlined contract → response | documents | C | S2 | P2 |
| `legal-researcher` | Legal Researcher | Finds statutes and case law with verified citations | question + jurisdiction → memo | legal databases | C | S1 | P2 |
| `case-summarizer` | Judgment Summarizer | Summarizes judgments into facts, issues, holdings and reasoning | judgment → summary | — | A | S0 | P2 |
| `policy-writer` | Policy Writer | Drafts internal policies from regulations and company context | regulation + context → policy | — | A | S0 | P2 |
| `obligation-tracker` | Obligation Tracker | Extracts deadlines and obligations from contracts into a calendar | contracts → obligations | calendar | A | S2 | P2 |
| `trademark-checker` | Trademark Checker | Searches trademark databases for conflicts | mark + classes → conflicts | trademark DBs | A | S1 | P2 |
| `ediscovery-reviewer` | E-discovery Reviewer | Tags documents for relevance and privilege for human review | documents + criteria → tags | documents | C | S1 | P2 |
| `privacy-impact-assessor` | Privacy Impact Assessor | Drafts DPIAs for new systems under GDPR / DPDP Act | system description → DPIA draft | — | A | S0 | P2 |

#### 7.32 HR and recruiting — `agents/business/hr/` · ID prefix `hr/`

Hiring decisions stay with humans. Screening agents use structured rubrics and are bias-tested.

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `jd-writer` | Job Description Writer | Writes clear, inclusive job descriptions | role info → JD | — | A | S0 | P1 |
| `resume-screener` | Resume Screener | Scores CVs against a structured rubric with evidence for each score, for human decision | CVs + rubric → scored shortlist | documents | A | S4 | P1 |
| `hr-policy-qa` | HR Policy Assistant | Answers employee questions on leave, benefits and policies with citations | question → answer | rag-qa | C | S1 | P1 |
| `onboarding-buddy` | Onboarding Buddy | Guides new hires through checklists, people to meet and FAQs | new hire → plan + answers | HRIS, rag-qa | C | S1 | P1 |
| `candidate-sourcer` | Candidate Sourcer | Finds candidates from public professional sources and drafts outreach | role → shortlist + drafts | web-search | C | S1 | P2 |
| `interview-kit-builder` | Interview Kit Builder | Structured interview questions and scorecards for a role | role → kit | — | A | S0 | P2 |
| `interview-scheduler` | Interview Scheduler | Coordinates interview panels and candidate availability | candidates + panel → schedule | calendar | C | S3 | P2 |
| `offer-letter-generator` | Offer Letter Generator | Generates offer letters from approved templates | offer data → letter | documents | A | S2 | P2 |
| `performance-review-helper` | Performance Review Helper | Synthesizes feedback and goals into a balanced review draft | feedback + goals → draft | — | A | S1 | P2 |
| `learning-path-designer` | Learning Path Designer | Builds role-based learning paths from skills gaps | role + skills → path | LMS | A | S0 | P2 |
| `employee-survey-analyst` | Employee Survey Analyst | Themes and drivers from engagement surveys | responses → insights | — | A | S1 | P2 |
| `exit-interview-analyst` | Exit Interview Analyst | Finds attrition themes from exit interviews | interviews → themes | — | A | S1 | P2 |

#### 7.33 Operations and project management — `agents/business/operations/` · ID prefix `operations/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `project-manager` | Project Manager | Builds plans, tracks status across tools, flags risks and slipping dates | project → plan + status + risks | Jira/Linear/Asana | C | S2 | P1 |
| `status-reporter` | Status Reporter | Compiles weekly status from trackers, repos and chat | sources → status report | tracker, repo, chat | C | S1 | P1 |
| `sop-writer` | SOP Writer | Documents processes from screen recordings, notes or interviews | recording/notes → SOP | stt, vision | A | S1 | P1 |
| `requirements-analyst` | Requirements Analyst | Turns stakeholder input into PRDs, user stories and acceptance criteria | notes → PRD + stories | — | C | S0 | P1 |
| `process-miner` | Process Miner | Finds bottlenecks and rework from event logs | event log → process map + issues | python-sandbox | C | S1 | P2 |
| `okr-tracker` | OKR Tracker | Tracks objectives and key results and prompts owners for updates | OKRs → progress report | — | A | S2 | P2 |
| `vendor-manager` | Vendor Manager | Tracks vendor contracts, renewals and SLAs | contracts → renewal calendar + alerts | documents | C | S2 | P2 |
| `risk-register-keeper` | Risk Register Keeper | Maintains a risk register and reminds owners about mitigations | inputs → register updates | — | A | S2 | P2 |
| `decision-logger` | Decision Logger | Records decisions with context and rationale from meetings and chats | conversations → decision log | — | A | S2 | P2 |
| `product-feedback-prioritizer` | Product Feedback Prioritizer | Clusters feedback and scores ideas (RICE) to draft a roadmap | feedback → prioritized backlog | — | C | S1 | P2 |

#### 7.34 Procurement, supply chain and logistics — `agents/business/supply-chain/` · ID prefix `supply-chain/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `shipment-tracker` | Shipment Tracker | Multi-carrier tracking with exception alerts and customer updates | shipments → status + exceptions | carrier APIs | A | S1 | P2 |
| `demand-forecaster` | Demand Forecaster | Forecasts demand by SKU and location with seasonality and events | sales history → forecast | python-sandbox | A | S1 | P2 |
| `inventory-optimizer` | Inventory Optimizer | Sets reorder points and safety stock | demand + lead times → policy | python-sandbox | A | S1 | P2 |
| `route-optimizer` | Route Optimizer | Plans delivery routes with time windows and capacity | stops + fleet → routes | routing solver | A | S1 | P2 |
| `supplier-sourcer` | Supplier Sourcer | Finds and compares suppliers by capability, certification and price | requirement → shortlist | web-search | C | S1 | P2 |
| `purchase-order-agent` | Purchase Order Agent | Creates POs from approved requisitions and matches confirmations | requisition → PO draft | ERP | C | S4 | P2 |
| `customs-doc-preparer` | Customs Document Preparer | Suggests HS codes and prepares commercial invoices and packing lists | shipment data → documents | documents | A | S2 | P2 |
| `supplier-risk-monitor` | Supplier Risk Monitor | Watches news, financial and geopolitical risk for key suppliers | supplier list → alerts | news-monitor | C | S1 | P2 |

#### 7.35 Strategy and leadership — `agents/business/strategy/` · ID prefix `strategy/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `strategy-analyst` | Strategy Analyst | SWOT, Porter's five forces and scenario analysis with evidence | company + question → analysis | web-search | C | S1 | P2 |
| `decision-analyst` | Decision Analyst | Structured decisions: options, weighted criteria, pre-mortem, recommendation | decision → analysis | — | A | S0 | P2 |
| `business-plan-writer` | Business Plan Writer | Drafts business plans with market, model and financial sections | idea + data → plan | market-researcher | C | S0 | P2 |
| `pitch-deck-builder` | Pitch Deck Builder | Builds investor decks with story, market and metrics | company info → deck | slide-deck-builder | C | S0 | P2 |
| `board-pack-preparer` | Board Pack Preparer | Assembles board packs from department inputs with an executive summary | inputs → board pack | documents | C | S1 | P2 |
| `investor-update-writer` | Investor Update Writer | Monthly investor updates from metrics and highlights | metrics + notes → update | — | A | S0 | P2 |

---

### FAMILY 7 — LIFE AND LEARNING (`agents/life/`)

Agents for individuals: personal productivity, home, money, travel, health, learning, creativity, community.

#### 7.36 Personal productivity — `agents/life/productivity/` · ID prefix `productivity/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `task-manager` | Task Manager | Captures tasks from chat, email and voice; prioritizes them and plans the day | inputs → task list + plan | task APIs | C | S2 | P0 |
| `daily-briefer` | Daily Briefer | Morning brief: calendar, priority tasks, important mail, weather and news | sources → brief | calendar, email, weather | C | S1 | P1 |
| `note-organizer` | Second Brain Organizer | Files, links and tags notes automatically (Obsidian, Notion, Markdown) | notes → organized vault | notes API | C | S2 | P1 |
| `reminder-agent` | Reminder Agent | Natural-language reminders, including time-, place- and context-based | request → reminders | calendar/reminders | A | S2 | P1 |
| `personal-knowledge-qa` | Personal Knowledge Q&A | Answers "what did I decide about X?" across your own notes, mail and files | question → answer + sources | vector-store | C | S1 | P1 |
| `reading-list-curator` | Reading List Curator | Saves, summarizes and prioritizes articles to read | links → curated list | http | A | S1 | P2 |
| `habit-coach` | Habit Coach | Helps build habits with tracking, nudges and reflection | goals → plan + check-ins | reminders | A | S1 | P2 |
| `journal-companion` | Journal Companion | Private, local-first reflective prompts and mood trends | entries → reflections | local storage | A | S1 | P2 |
| `focus-guardian` | Focus Guardian | Blocks distractions and batches notifications during focus time | schedule → focus sessions | OS notifications | A | S2 | P2 |
| `weekly-review` | Weekly Review Coach | Guides a weekly review of tasks, goals and calendar | tasks + calendar → review + plan | task APIs | A | S1 | P2 |

#### 7.37 Personal life, home and money — `agents/life/personal/` · ID prefix `personal/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `personal-finance-tracker` | Personal Finance Tracker | Budgets and spending insights from statements; no investment advice | statements → budget + insights | documents | C | S1 | P1 |
| `bill-subscription-manager` | Bills & Subscriptions Manager | Tracks bills and subscriptions, reminds before due dates and guides cancellations | statements + mail → tracker | email | A | S1 | P1 |
| `shopping-assistant` | Shopping Assistant | Researches and compares products and tracks prices; stops before purchase | need → comparison + pick | web-search, browser | C | S1 | P1 |
| `price-tracker` | Price Tracker | Watches prices and alerts on drops | products + target → alerts | page-change-monitor | A | S1 | P2 |
| `meal-planner` | Meal Planner | Weekly meal plans and grocery lists by diet, budget and pantry | preferences → plan + list | — | C | S0 | P2 |
| `cooking-assistant` | Hands-free Cooking Assistant | Step-by-step cooking by voice, with timers and substitutions | recipe → guided steps | tts, stt | A | S0 | P2 |
| `home-inventory` | Home Inventory | Catalogues belongings from photos for insurance and moving | photos → inventory | vision | A | S1 | P2 |
| `home-maintenance` | Home Maintenance Planner | Maintenance schedules and help finding service providers | home profile → schedule | local-search | A | S1 | P2 |
| `event-planner` | Event Planner | Plans parties and weddings: checklist, budget, vendors, timeline | event brief → plan | web-search | C | S1 | P2 |
| `gift-advisor` | Gift Advisor | Gift ideas by person, occasion and budget | person + budget → ideas | web-search | A | S1 | P2 |
| `personal-doc-vault` | Personal Document Vault | Organizes personal documents (IDs, warranties, policies) with encryption and expiry reminders | documents → vault + reminders | encrypted storage | A | S2 | P2 |
| `digital-declutterer` | Digital Declutterer | Cleans up photos, files and inbox with a reviewable plan | accounts → cleanup plan | filesystem, email | C | S2 | P2 |
| `parenting-helper` | Family Organizer | Family schedules, school messages, activity ideas | inputs → family calendar + tasks | calendar | A | S2 | P2 |
| `pet-care-helper` | Pet Care Helper | Vaccination and care reminders, general pet information | pet profile → schedule | reminders | A | S1 | P2 |

#### 7.38 Travel — `agents/life/travel/` · ID prefix `travel/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `trip-planner` | Trip Planner | Day-by-day itineraries by budget, pace and interests | trip brief → itinerary | web-search, maps | C | S1 | P1 |
| `flight-hotel-searcher` | Flight & Hotel Searcher | Compares options on price, timing and flexibility; stops before booking | trip → options | travel APIs | C | S1 | P2 |
| `travel-doc-checker` | Travel Document Checker | Visa, passport validity and entry rules from official sources | trip + nationality → requirements | web-search | A | S1 | P2 |
| `local-guide` | On-trip Local Guide | Nearby recommendations, translation and directions on the go | location + interest → suggestions | local-search, translator | C | S1 | P2 |
| `flight-tracker` | Flight Tracker | Delay and gate alerts with rebooking options | booking → alerts | flight APIs | A | S1 | P2 |
| `trip-expense-reporter` | Trip Expense Reporter | Turns travel receipts into an expense report | receipts → report | invoice-receipt-parser | C | S2 | P2 |

#### 7.39 Health and wellness (consumer) — `agents/life/wellness/` · ID prefix `wellness/`

Health agents give general information, not diagnosis. Every one routes emergencies to real help.

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `symptom-navigator` | Symptom Navigator | Asks structured questions and suggests the right level of care (self-care, doctor, emergency) | symptoms → care-level guidance | medical KB | C | S4 | P2 |
| `lab-report-explainer` | Lab Report Explainer | Explains lab results in plain language and suggests questions for the doctor | report → explanation | documents | A | S4 | P2 |
| `medication-reminder` | Medication Reminder | Dose schedules, refill alerts and interaction information from authoritative databases | prescriptions → schedule | drug DB | A | S4 | P2 |
| `health-record-organizer` | Health Record Organizer | Collects reports into a timeline and summary to share with doctors | documents → timeline | documents | C | S2 | P2 |
| `fitness-coach` | Fitness Coach | Workout plans that adapt to progress and equipment | goals + level → plan | — | A | S1 | P2 |
| `nutrition-coach` | Nutrition Coach | Food logging from photos and nutrition guidance | meals → log + insights | vision | C | S1 | P2 |
| `sleep-coach` | Sleep Coach | Sleep habit guidance from wearable data | sleep data → tips | wearable APIs | A | S1 | P2 |
| `wellbeing-companion` | Wellbeing Companion | Supportive check-ins and evidence-based exercises (e.g. CBT-style); not therapy; crisis lines always available | conversation → support + resources | crisis resource directory | C | S4 | P2 |

#### 7.40 Education and learning — `agents/life/education/` · ID prefix `education/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `tutor` | Socratic Tutor | Teaches by questioning, adapts to the learner's level, does not just give answers | topic + learner → session | — | C | S1 | P1 |
| `quiz-generator` | Quiz Generator | Builds quizzes with answer keys and explanations from any material | content → quiz | — | A | S0 | P1 |
| `flashcard-maker` | Flashcard Maker | Creates spaced-repetition flashcards (Anki format) | content → cards | — | A | S0 | P1 |
| `lesson-planner` | Lesson Planner | Lesson plans aligned to curriculum outcomes | topic + grade → lesson plan | — | A | S0 | P2 |
| `grader` | Feedback Grader | Rubric-based feedback on essays, answers and code | submission + rubric → feedback | — | A | S1 | P2 |
| `course-builder` | Course Builder | Builds a course: modules, lessons, assessments, resources | goal → course | — | C | S0 | P2 |
| `language-partner` | Language Partner | Conversation practice by voice or text with gentle corrections | learner + language → practice | stt, tts | C | S1 | P2 |
| `study-planner` | Study Planner | Exam-oriented study schedule with spaced revision | syllabus + date → plan | calendar | A | S1 | P2 |
| `exam-prep-coach` | Exam Prep Coach | Practice questions, weak-area tracking and mock tests | exam + learner → practice plan | — | C | S1 | P2 |
| `math-solver` | Math Solver | Step-by-step solutions checked with a computer algebra system | problem → steps + answer | CAS | A | S0 | P2 |
| `research-mentor` | Research Mentor | Guides students through choosing a question, method and writing | student project → guidance | academic-search | C | S1 | P2 |
| `kids-learning-companion` | Kids Learning Companion | Age-appropriate learning games and stories with parental controls | child profile → activities | age-safety-filter | C | S1 | P2 |

#### 7.41 Creative and media — `agents/life/creative/` · ID prefix `creative/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `photo-organizer` | Photo Organizer & Enhancer | Sorts, culls blurry/duplicate shots and auto-enhances photos | photo library → albums + edits | vision | C | S2 | P2 |
| `brand-kit-designer` | Brand Kit Designer | Logo concepts, colour palettes and type pairings with usage rules | brand brief → kit | image-generator | C | S0 | P2 |
| `thumbnail-designer` | Thumbnail Designer | Eye-catching thumbnails and cover images | video/topic → thumbnails | image-generator | A | S0 | P2 |
| `storyboard-artist` | Storyboard Artist | Turns scripts into storyboard frames with shot notes | script → storyboard | image-generator | C | S0 | P2 |
| `comic-creator` | Comic Creator | Comic strips with consistent characters | story → panels | image-generator | C | S0 | P2 |
| `game-designer` | Game Design Assistant | Mechanics, levels, economy and narrative design documents | concept → GDD | — | C | S0 | P2 |
| `3d-asset-generator` | 3D Asset Generator | Generates 3D models from text or images (glTF) | prompt/image → 3D model | 3D generation | A | S0 | P2 |
| `interior-visualizer` | Interior Design Visualizer | Restyles room photos and suggests furniture layouts | room photo + style → renders | image-editor | A | S0 | P2 |
| `wardrobe-stylist` | Wardrobe Stylist | Outfit suggestions from photos of your own wardrobe | wardrobe + occasion → outfits | vision | A | S1 | P2 |
| `meme-generator` | Meme Generator | Meme and reaction images from a topic | topic → images | image-generator | A | S0 | P2 |

#### 7.42 Community and social — `agents/life/community/` · ID prefix `community/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `community-moderator` | Community Moderator | Applies community rules in Discord, forums and groups; escalates edge cases | messages → actions | chat APIs, content-moderator | C | S3 | P2 |
| `community-qa-bot` | Community Q&A Bot | Answers recurring questions from docs and past threads | question → answer | rag-qa | C | S1 | P2 |
| `misinformation-flagger` | Misinformation Flagger | Flags likely false claims with context and sources | posts → flags + context | fact-checker | A | S1 | P2 |
| `event-organizer` | Meetup Organizer | RSVPs, reminders, venue logistics and follow-ups for community events | event → logistics | calendar, email | A | S3 | P2 |
| `volunteer-coordinator` | Volunteer Coordinator | Matches volunteers to shifts and sends reminders | volunteers + shifts → schedule | calendar | A | S3 | P2 |

---
### FAMILY 8 — INDUSTRIES (`agents/industries/`)

Vertical agents that need domain rules, data formats and regulation. Each industry folder also ships a `README.md` listing which horizontal agents it reuses.

#### 7.43 Banking and financial services — `agents/industries/banking/` · ID prefix `banking/`

Built for regulated environments: on-prem/local model options, audit logs, explainability and human sign-off by default.

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `kyc-onboarding` | KYC Onboarding Agent | Collects documents, extracts and cross-checks data, verifies through approved registry APIs, flags mismatches for a human officer | applicant docs → KYC file + flags | id-document-reader, registry APIs | C | S4 | P1 |
| `aml-alert-investigator` | AML Alert Investigator | Investigates transaction-monitoring alerts, gathers context and drafts the suspicious transaction narrative for analysts | alert + history → investigation + draft | core banking data | C | S4 | P1 |
| `sanctions-screener` | Sanctions & PEP Screener | Fuzzy and transliteration-aware name screening with explained hits and false-positive reduction | names → hits + explanations | sanctions lists | A | S4 | P1 |
| `fraud-signal-explainer` | Fraud Signal Explainer | Explains risk-model scores on transactions and flags mule-account and scam patterns for review | transaction + score → explanation + action | risk engine | C | S4 | P1 |
| `bank-statement-analyzer` | Bank Statement Analyzer | Parses statements to income, expenses, EMIs, bounces and cash-flow features | statements → analysis | documents | A | S1 | P1 |
| `regulatory-circular-tracker` | Regulatory Circular Tracker | Tracks central bank and regulator circulars and master directions, summarizes them and maps them to affected processes and deadlines | regulator feeds → summaries + impact map | news-monitor, documents | C | S1 | P1 |
| `loan-application-assistant` | Loan Application Assistant | Guides applicants in their language, checks completeness and explains products and charges | applicant ↔ guidance + complete file | voice-form-filler | C | S3 | P2 |
| `credit-memo-drafter` | Credit Appraisal Drafter | Analyzes financials and bureau data into a credit appraisal note for the credit officer | financials + bureau → memo draft | financial-statement-analyzer | C | S4 | P2 |
| `cashflow-lending-analyst` | Cash-flow Lending Analyst | Assesses small-business credit from consented GST, bank and accounting data (e.g. via Account Aggregator) | consented data → assessment | data APIs | C | S4 | P2 |
| `dispute-chargeback-handler` | Dispute & Chargeback Handler | Collects evidence and drafts responses for card and payment disputes | dispute → evidence pack + response | payments data | C | S4 | P2 |
| `grievance-redressal` | Grievance Redressal Agent | Classifies complaints, tracks turnaround times, drafts responses and prepares escalation files | complaint → category + response + tracking | ticketing | C | S3 | P2 |
| `banking-voice-assistant` | Vernacular Banking Assistant | Voice-first help for balances, FAQs and services in local languages, authenticated through the bank's own systems | voice ↔ voice + actions | realtime-voice-assistant | C | S4 | P2 |
| `financial-literacy-guide` | Financial Literacy Guide | Explains banking, digital payments, insurance and government schemes simply, in local languages | question → explanation | rag-qa, tts | C | S1 | P2 |
| `scam-message-checker` | Scam Message Checker | Consumers forward a suspicious SMS, call script or payment request and get a risk verdict with what to do | message → verdict + advice | phishing-analyzer | A | S1 | P2 |
| `collections-assistant` | Fair Collections Assistant | Compliant, respectful repayment reminders within regulator fair-practice rules | accounts → reminders | messaging | C | S3 | P2 |
| `regulatory-return-preparer` | Regulatory Return Preparer | Prepares and validates regulatory returns against taxonomy and validation rules (e.g. XBRL) | source data → return + validation report | spreadsheet | C | S4 | P2 |
| `model-risk-validator` | AI Model Risk Validator | Checks AI/ML models for documentation, performance, fairness, drift and explainability under model-risk policy | model + data → validation report | model-evaluator, bias-auditor | C | S1 | P2 |

#### 7.44 Insurance — `agents/industries/insurance/` · ID prefix `insurance/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `claims-intake` | Claims Intake (FNOL) | Takes first notice of loss by chat or voice with photos and documents into a complete claim file | report → claim file | vision, voice-form-filler | C | S3 | P2 |
| `claims-adjuster-assistant` | Claims Adjuster Assistant | Damage assessment, coverage check against the policy and fraud indicators for the adjuster | claim + policy → assessment | vision, documents | C | S4 | P2 |
| `underwriting-assistant` | Underwriting Assistant | Summarizes submissions and risk factors for underwriters | submission → risk summary | documents | C | S4 | P2 |
| `policy-explainer` | Policy Explainer | Plain-language Q&A about what a policy does and does not cover | policy + question → answer | rag-qa | A | S1 | P2 |
| `policy-comparer` | Policy Comparer | Side-by-side comparison of coverage, exclusions and price | policies → comparison | documents | A | S1 | P2 |
| `renewal-agent` | Renewal Agent | Renewal reminders and coverage-change summaries | policies → reminders | messaging | A | S3 | P2 |

#### 7.45 Healthcare (clinical and provider) — `agents/industries/healthcare/` · ID prefix `healthcare/`

Clinical agents assist licensed professionals; outputs are drafts for clinician review.

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `medical-scribe` | Ambient Medical Scribe | Turns a consented doctor–patient conversation into a structured clinical note (SOAP) for the clinician to approve | audio → note draft | stt, speaker-diarizer | C | S4 | P2 |
| `patient-intake` | Patient Intake Agent | Pre-visit questionnaires by voice or chat in the patient's language | patient ↔ intake record | voice-form-filler | C | S4 | P2 |
| `clinical-coder` | Clinical Coding Assistant | Suggests ICD/CPT codes with evidence from the note | note → code suggestions | coding sets | A | S4 | P2 |
| `prior-authorization` | Prior Authorization Agent | Assembles clinical evidence and fills payer forms for review | case → auth packet | documents | C | S4 | P2 |
| `discharge-simplifier` | Discharge Instructions Simplifier | Rewrites discharge instructions in plain language and the patient's language | instructions → simplified + translated | translator | A | S4 | P2 |
| `appointment-manager` | Appointment Manager | Scheduling, reminders and waitlist backfill to reduce no-shows | schedule + patients → bookings | calendar, messaging | C | S3 | P2 |
| `clinical-trial-matcher` | Clinical Trial Matcher | Matches patient profiles to trial eligibility criteria | profile → trial matches | trial registries | C | S4 | P2 |
| `medical-evidence-agent` | Medical Evidence Summarizer | Evidence summaries from guidelines and literature with citations | clinical question → summary | academic-search | C | S1 | P2 |

#### 7.46 E-commerce and retail — `agents/industries/ecommerce/` · ID prefix `ecommerce/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `product-listing-writer` | Product Listing Writer | Titles, bullet points, descriptions and attributes tuned per marketplace | product data → listings | — | A | S0 | P1 |
| `catalog-enricher` | Catalog Enricher | Fills missing attributes from images and specs and normalizes the taxonomy | catalog → enriched catalog | vision | A | S2 | P1 |
| `shopping-concierge` | Shopping Concierge | Conversational product discovery on a store's own catalog | shopper ↔ recommendations | semantic-search | C | S1 | P2 |
| `review-analyzer` | Review Analyzer | Product review insights: what customers love, hate and request | reviews → insights | sentiment-analyzer | A | S1 | P2 |
| `pricing-monitor` | Pricing Monitor | Tracks competitor prices and suggests repricing within rules | SKUs + competitors → suggestions | page-change-monitor | C | S1 | P2 |
| `recommendation-agent` | Recommendation Agent | Personalized product recommendations with explanations | user + catalog → recommendations | embeddings | A | S1 | P2 |
| `size-fit-advisor` | Size & Fit Advisor | Size recommendations from measurements, brand charts and reviews | shopper + product → size | — | A | S1 | P2 |
| `cart-recovery` | Cart Recovery Agent | Personalized, consented abandoned-cart messages | abandoned cart → message | messaging | A | S3 | P2 |
| `marketplace-sync` | Marketplace Sync | Keeps listings, stock and prices in sync across marketplaces and the web store | catalog → sync report | marketplace APIs | C | S3 | P2 |
| `visual-product-search` | Visual Product Search | Find similar products from a photo | photo → products | image-similarity | A | S1 | P2 |
| `order-fraud-screener` | Order Fraud Screener | Scores orders for fraud risk with reasons for manual review | order → risk + reasons | risk signals | A | S4 | P2 |

#### 7.47 Real estate and property — `agents/industries/real-estate/` · ID prefix `real-estate/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `listing-writer` | Property Listing Writer | Listing descriptions from photos and property details | details + photos → listing | vision | A | S0 | P2 |
| `property-valuator` | Property Valuation Estimator | Comparable-sales based value ranges with assumptions shown | property → value range | property data | C | S1 | P2 |
| `lease-abstractor` | Lease Abstractor | Extracts rent, term, escalations, options and obligations from leases | lease → abstract | documents | A | S1 | P2 |
| `property-search-assistant` | Property Search Assistant | Finds and shortlists properties by needs and commute | needs → shortlist | listings APIs, maps | C | S1 | P2 |
| `maintenance-request-agent` | Maintenance Request Agent | Triage of tenant requests with photos and dispatch to vendors | request → work order | ticketing | C | S3 | P2 |
| `tenant-screening-assistant` | Tenant Screening Assistant | Applies the landlord's written, fair-housing-compliant criteria and documents reasons; human decides | application + criteria → assessment | documents | C | S4 | P2 |
| `property-doc-checker` | Property Document Checker | Checklist review of title and approval documents for missing items | documents → checklist | documents | A | S1 | P2 |

#### 7.48 Manufacturing and industrial — `agents/industries/manufacturing/` · ID prefix `manufacturing/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `quality-inspector` | Line Quality Inspector | Visual defect detection on production lines with defect logging and root-cause notes | camera frames → defects + log | vision | C | S2 | P2 |
| `predictive-maintenance` | Predictive Maintenance Agent | Predicts equipment failure from sensor data and schedules maintenance | sensor data → risk + work order | sensor-monitor | C | S2 | P2 |
| `maintenance-copilot` | Technician Copilot | Hands-free voice Q&A over manuals and maintenance history for technicians | question → steps | rag-qa, stt, tts | C | S1 | P2 |
| `work-instruction-writer` | Work Instruction Writer | Step-by-step work instructions from videos, CAD notes and experts | inputs → instructions | vision, stt | A | S1 | P2 |
| `production-scheduler` | Production Scheduler | Schedules jobs across machines given orders and constraints | orders + capacity → schedule | solver | A | S2 | P2 |
| `ehs-incident-agent` | Safety Incident Agent | Captures safety incidents and near misses and drafts investigation reports | report → incident file | voice-form-filler | C | S2 | P2 |

#### 7.49 Agriculture — `agents/industries/agriculture/` · ID prefix `agriculture/`

Designed for low-bandwidth, voice-first, local-language use.

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `crop-doctor` | Crop Doctor | Identifies likely pests and diseases from photos and gives advisory in the farmer's language | photo → diagnosis + advice | vision, tts | C | S1 | P2 |
| `farm-weather-advisor` | Farm Weather Advisor | Turns forecasts into farm actions (sow, spray, irrigate, harvest) | location + crop → advice | weather API | A | S1 | P2 |
| `market-price-advisor` | Market Price Informer | Local market and commodity prices and trends | crop + location → prices | market data APIs | A | S1 | P2 |
| `soil-report-explainer` | Soil Report Explainer | Explains soil test cards and fertilizer recommendations | soil card → explanation | ocr | A | S1 | P2 |
| `farm-record-keeper` | Farm Record Keeper | Voice logging of inputs, costs and yields | voice notes → records | stt | A | S2 | P2 |
| `agri-scheme-finder` | Agri Scheme Finder | Finds subsidy and insurance schemes a farmer is eligible for and the documents needed | farmer profile → schemes | rag-qa | A | S1 | P2 |

#### 7.50 Energy and utilities — `agents/industries/energy/` · ID prefix `energy/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `utility-bill-analyzer` | Utility Bill Analyzer | Explains bills, spots errors and tariff savings | bills → analysis | ocr | A | S1 | P2 |
| `solar-sizing-advisor` | Solar Sizing Advisor | Estimates rooftop solar size, cost and payback | location + usage → estimate | weather, maps | A | S1 | P2 |
| `load-forecaster` | Grid Load Forecaster | Short-term load forecasting for utilities | history + weather → forecast | python-sandbox | A | S1 | P2 |
| `outage-communicator` | Outage Communicator | Customer outage notices and ETAs from grid data | outage data → messages | messaging | A | S3 | P2 |
| `energy-auditor` | Building Energy Auditor | Finds efficiency improvements from bills and building data | building data → measures | — | C | S1 | P2 |

#### 7.51 Government and civic — `agents/industries/government/` · ID prefix `government/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `citizen-services-assistant` | Citizen Services Assistant | Explains services, eligibility and required documents, by voice in local languages | question → guidance | rag-qa, stt, tts | C | S1 | P2 |
| `scheme-eligibility-checker` | Scheme Eligibility Checker | Checks which government schemes a person qualifies for | profile → eligible schemes | rule engine | A | S1 | P2 |
| `gov-form-assistant` | Government Form Assistant | Helps fill government forms step by step; the citizen submits | person ↔ filled form | voice-form-filler | C | S2 | P2 |
| `grievance-filer` | Public Grievance Filer | Drafts and tracks public grievances on official portals | issue → grievance draft | browser | A | S2 | P2 |
| `rti-drafter` | RTI / FOI Request Drafter | Drafts right-to-information requests | question → request | — | A | S0 | P2 |
| `public-consultation-analyzer` | Public Consultation Analyzer | Summarizes and themes public comments on draft policies | comments → themes + summary | survey-analyst | C | S1 | P2 |
| `legislation-tracker` | Legislation Tracker | Tracks bills and gazette notifications by topic | topics → updates | news-monitor | A | S1 | P2 |
| `tender-analyzer` | Tender Analyzer | Extracts eligibility, scope, deadlines and documents from tender documents | tender → checklist | documents | C | S1 | P2 |

#### 7.52 Hospitality and food service — `agents/industries/hospitality/` · ID prefix `hospitality/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `reservation-agent` | Reservation Agent | Takes table and room bookings by phone, chat or WhatsApp | request → booking | phone-call-agent | C | S3 | P2 |
| `hotel-concierge` | Guest Concierge | Answers guest requests and gives local recommendations | request → answer/action | rag-qa, local-search | C | S2 | P2 |
| `menu-engineer` | Menu Engineer | Menu costing, pricing and appealing descriptions | recipes + costs → menu | spreadsheet | A | S0 | P2 |
| `housekeeping-optimizer` | Housekeeping Optimizer | Plans housekeeping by check-outs and priorities | occupancy → schedule | PMS | A | S2 | P2 |

#### 7.53 Science and R&D — `agents/industries/science/` · ID prefix `science/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `paper-reader` | Paper Reader | Extracts methods, results, limitations and data from a paper | paper → structured summary | documents | A | S0 | P1 |
| `experiment-designer` | Experiment Designer | Designs experiments: variables, controls, sample size, analysis plan | hypothesis → design | python-sandbox | A | S0 | P2 |
| `lab-protocol-writer` | Lab Protocol Writer | Writes clear, reproducible protocols | method notes → protocol | — | A | S0 | P2 |
| `lab-notebook` | Voice Lab Notebook | Hands-free logging of experiments | voice → notebook entries | stt | A | S2 | P2 |
| `simulation-setup` | Simulation Setup Agent | Configures simulation runs (CFD, FEA, molecular) from specifications | spec → config | simulation tools | C | S2 | P2 |
| `results-to-manuscript` | Manuscript Drafter | Drafts paper sections from results and notes, with references | results → draft | citation-manager | C | S0 | P2 |
| `proof-assistant` | Formal Proof Assistant | Helps write and check formal proofs (Lean) | statement → proof | Lean | C | S0 | P2 |
| `materials-literature-miner` | Literature Data Miner | Extracts properties and measurements from many papers into a dataset | papers → dataset | documents | C | S1 | P2 |
| `peer-review-assistant` | Peer Review Assistant | Checks manuscripts against reporting checklists and drafts reviewer notes | manuscript → notes | — | A | S0 | P2 |

#### 7.54 Gaming and interactive entertainment — `agents/industries/gaming/` · ID prefix `gaming/`

| ID | Name | What it does (purpose) | Input → Output | Tools | T | S | P |
|---|---|---|---|---|---|---|---|
| `npc-agent` | NPC Agent | Dynamic non-player character dialogue with memory, personality and game-rule constraints | game state + player → dialogue/actions | memory | C | S0 | P2 |
| `game-tester` | Game Playtester | Plays builds to find bugs, softlocks and balance problems | build → bug reports | computer-use | C | S1 | P2 |
| `level-generator` | Level Generator | Procedural level and quest generation within design rules | rules → levels | — | A | S0 | P2 |
| `game-master` | Tabletop Game Master | Runs tabletop RPG sessions with rules and story continuity | players ↔ narration | memory | C | S0 | P2 |

#### 7.55 Future industry packs (open for contribution)

Telecom (network-ops assistant, plan advisor) · Automotive and mobility (fleet manager, EV charging planner) · Aviation (maintenance records, crew scheduling) · Construction (bid estimator, site-progress monitor from photos) · Pharma (pharmacovigilance case intake, regulatory submission assembler) · Media and publishing (fact-check desk, archive tagger) · Non-profit (donor relations, impact reporter) · Sports (performance analyst, fixture scheduler) · Maritime and ports (port-call coordinator) · Mining (geology report summarizer). Proposals use the `new-category-rfc` issue template.

---

## 8. Teams: ready-made multi-agent compositions

A **team** is a reusable multi-agent workflow defined in `teams/<slug>/team.yaml`: which agents, in what graph, with what hand-offs and approval points. Teams are the step between single agents and whole products.

```yaml
# teams/research-team/team.yaml (shape)
apiVersion: afe/v1
kind: Team
metadata: {id: research-team, version: 0.1.0, maturity: spec}
spec:
  pattern: orchestrator-workers
  entry: orchestration/task-planner
  members:
    - orchestration/task-planner
    - search/web-search
    - research/source-reader
    - research/fact-checker
    - research/report-writer
    - guardrails/hallucination-checker
  graph:                       # edges: from → to (with optional condition)
    - [task-planner, web-search]
    - [web-search, source-reader]
    - [source-reader, fact-checker]
    - [fact-checker, report-writer]
    - [report-writer, hallucination-checker]
    - [hallucination-checker, report-writer, {when: "unsupported_claims > 0"}]
  approvals: []
  io: {input: schemas/input.schema.json, output: schemas/output.schema.json}
```

| Team ID | Purpose | Member agents (flow) | Pattern | P |
|---|---|---|---|---|
| `research-team` | Cited research report on any topic | task-planner → web-search → source-reader → fact-checker → report-writer → hallucination-checker | Orchestrator–workers | P0 |
| `document-intake` | Turn any incoming document into validated, structured data | doc-classifier → document-parser → structured-extractor → verifier → human-approval-gate | Prompt chaining | P0 |
| `voice-concierge` | Talk to any app: voice in, actions and voice out | speech-to-text → router → (any agent) → text-to-speech | Routing | P0 |
| `inbox-zero` | Clear the inbox daily | inbox-triager → email-drafter → follow-up-tracker → action-item-extractor → human-approval-gate | Prompt chaining | P0 |
| `meeting-to-done` | From meeting to tracked tasks and recap | meeting-notetaker → action-item-extractor → meeting-follow-up → task-manager | Prompt chaining | P0 |
| `support-desk` | Tiered customer support | ticket-triager → support-chatbot ⇄ escalation-detector → reply-drafter → kb-writer | Routing + handoff | P0 |
| `software-squad` | Ship a feature from ticket to PR | requirements-analyst → code-generator → test-writer → code-reviewer → pr-describer | Evaluator–optimizer | P1 |
| `bug-squash` | Issue to merged fix | issue-triager → bug-fixer → test-writer → code-reviewer | Orchestrator–workers | P1 |
| `data-insights` | Answer a business question from data | clarifier → text-to-sql → data-analyst → chart-maker → report-writer | Plan-and-execute | P1 |
| `content-studio` | Topic to published multi-channel content | keyword-researcher → blog-writer → editor → seo-optimizer → content-repurposer → social-post-writer | Prompt chaining | P1 |
| `sdr-team` | Prospecting pipeline | lead-finder → lead-enricher → lead-scorer → account-researcher → outreach-personalizer → crm-updater | Prompt chaining | P1 |
| `incident-war-room` | Respond to production incidents | alert-triager → log-analyzer → incident-responder → human-approval-gate → postmortem-writer | Orchestrator–workers | P1 |
| `accounts-payable-team` | Invoice to approved payment run | invoice-receipt-parser → accounts-payable → expense-auditor → human-approval-gate | Prompt chaining | P1 |
| `contract-desk` | Contract intake and review | doc-classifier → contract-analyzer → redline-negotiator → obligation-tracker | Prompt chaining | P1 |
| `kyc-pipeline` | Customer onboarding with checks | id-document-reader → kyc-onboarding → sanctions-screener → human-approval-gate → audit-logger | Prompt chaining | P1 |
| `chief-of-staff` | Personal executive assistant | daily-briefer + inbox-triager + meeting-prep + task-manager + memory-retriever, coordinated by supervisor | Hierarchical | P1 |
| `web-qa-team` | Autonomous QA for a web app | web-navigator → web-tester → accessibility-auditor → issue-triager | Orchestrator–workers | P1 |
| `agent-factory` | Build new agents for this repo | agent-builder → test-case-generator → regression-runner → red-teamer → llm-judge | Evaluator–optimizer | P1 |
| `hiring-pipeline` | Role to shortlist with fair process | jd-writer → candidate-sourcer → resume-screener → bias-auditor → interview-kit-builder | Prompt chaining | P2 |
| `learning-coach` | Personalized learning programme | course-builder → tutor → quiz-generator → flashcard-maker → study-planner | Hierarchical | P2 |
| `regulatory-watch` | Regulation to impact assessment | regulatory-circular-tracker → compliance-monitor → policy-analyst → report-writer | Prompt chaining | P2 |
| `ecosystem-radar` | Keep this repo current (see §13) | news-monitor + academic-search + web-search → trend-spotter → report-writer → issue creation | Scheduled orchestrator | P1 |

---

## 9. Recipes: end-to-end product blueprints

A **recipe** is a complete, runnable product built from agents and teams: `recipes/<slug>/` contains `recipe.yaml`, an architecture doc, a minimal demo app (UI + backend), deployment notes and evals for the whole flow.

### 9.1 Recipe: Voice-powered form filling (your example)

**Problem:** Users must fill long forms (loan applications, patient intake, government forms, field surveys). Typing is slow, hard on mobile, and impossible for low-literacy users or people more comfortable in their own language.

**Solution:** The user speaks naturally; the system fills the right fields, asks only for what is missing, reads back a summary and lets the user correct by voice before submitting.

```mermaid
flowchart LR
    U((User speaks)) --> STT[voice/speech-to-text]
    STT --> PII[guardrails/pii-redactor<br/>logs only]
    STT --> EXT[text/structured-extractor<br/>+ form schema]
    EXT --> VER[orchestration/verifier<br/>types, formats, rules]
    VER -- missing / invalid --> ASK[voice/text-to-speech<br/>asks follow-up]
    ASK --> U
    VER -- complete --> FILL{Where is the form?}
    FILL -- web page --> WEB[browser/web-form-filler]
    FILL -- PDF --> PDF[documents/pdf-form-filler]
    FILL -- own app/API --> API[integration/api-caller]
    WEB & PDF & API --> GATE[orchestration/human-approval-gate<br/>read-back + confirm]
    GATE --> DONE((Submitted by user))
```

| Step | Agent | Notes |
|---|---|---|
| 1. Load form | (recipe code) | Form described as a `FormSchema`: fields, types, required, validation, help text, allowed values |
| 2. Listen | `voice/speech-to-text` | Streaming; handles code-switching ("my DOB is 12 March nineteen ninety") |
| 3. Map speech to fields | `text/structured-extractor` | Extracts many fields from one utterance; normalizes dates, amounts, phone numbers, addresses |
| 4. Validate | `orchestration/verifier` | Checks formats (PIN code, IFSC, email), cross-field rules (age vs DOB) |
| 5. Ask for gaps | `voice/text-to-speech` | Asks one short question per missing field, in the user's language |
| 6. Fill target | `browser/web-form-filler` / `documents/pdf-form-filler` / `integration/api-caller` | Same filled JSON, three output adapters |
| 7. Confirm | `orchestration/human-approval-gate` | Reads back the summary; user corrects by voice ("change the city to Nagpur") |
| 8. Protect | `guardrails/pii-redactor`, `guardrails/audit-logger` | Personal data masked in logs; audit trail for regulated use |

**Reuse:** the same recipe powers `banking/loan-application-assistant`, `healthcare/patient-intake`, `government/gov-form-assistant`, `insurance/claims-intake` and `manufacturing/ehs-incident-agent`, each just supplying a different `FormSchema` and locale.

### 9.2 More recipes

| Recipe | What it is | Built from | P |
|---|---|---|---|
| `chat-with-your-docs` | Internal assistant that answers from company documents with citations and permissions | knowledge-ingestor, semantic-search, reranker, rag-qa, hallucination-checker, pii-redactor | P0 |
| `deep-research-app` | Perplexity/Deep-Research-style app producing cited reports | research-team, answer-engine, report-writer | P0 |
| `invoice-automation` | Email inbox → invoices extracted → ERP-ready entries → approval | email-to-action, invoice-receipt-parser, accounts-payable-team | P1 |
| `ai-receptionist` | Phone and WhatsApp receptionist that books, answers FAQs and hands off | phone-call-agent, business-messaging-bot, rag-qa, meeting-scheduler | P1 |
| `personal-chief-of-staff` | Daily brief, inbox, calendar, tasks, memory | chief-of-staff team, memory agents | P1 |
| `ai-qa-engineer` | Point at a staging URL, get tests and bug reports | web-qa-team | P1 |
| `content-engine` | One recording → blog, newsletter, social posts, clips | podcast-producer, content-studio, clip-generator | P1 |
| `vernacular-banking-helpline` | Voice helpline in local languages for banking FAQs, scams and grievances | realtime-voice-assistant, banking-voice-assistant, scam-message-checker, grievance-redressal | P2 |
| `regulatory-intelligence` | Daily regulator updates mapped to internal policies and owners | regulatory-watch team | P2 |
| `farmer-advisory` | Photo + voice crop advisory over low bandwidth | crop-doctor, farm-weather-advisor, market-price-advisor, text-to-speech | P2 |
| `accessible-web` | Browser companion that narrates pages and fills forms by voice | screen-narrator, voice-form-filler, accessibility-auditor | P2 |

---

## 10. Reference spec: a fully worked agent

Every agent's README follows this outline. Shown here for `voice/voice-form-filler`; its manifest is in §4.2.

### 10.1 README outline (template for all agents)

```markdown
# Voice-to-Form Filler  `voice/voice-form-filler`
💡 spec · P0 · composite · safety S2 · autonomy L2

## What it does            one paragraph
## When to use / not use   bullet lists
## How it works            numbered steps + diagram
## Input                   table + link to input.schema.json
## Output                  table + link to output.schema.json
## Quick start             afe add … / Python / TypeScript snippets
## Configuration           options with defaults
## Composes with           upstream and downstream agents
## Tools required          MCP servers + permissions
## Safety                  side effects, approvals, data handling
## Evaluation              metrics, current scores, how to run
## Limitations             known failure modes
## Changelog               link
```

### 10.2 Input contract

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "afe://voice/voice-form-filler/input",
  "type": "object",
  "required": ["form", "audio"],
  "properties": {
    "form":   { "$ref": "afe://types/FormSchema" },
    "audio":  { "$ref": "afe://types/AudioSource", "description": "stream or file" },
    "locale": { "type": "string", "default": "en-IN" },
    "prefill": { "type": "object", "description": "known values, e.g. from profile" },
    "mode":   { "enum": ["conversational", "single-pass"], "default": "conversational" },
    "target": { "enum": ["json", "web", "pdf", "api"], "default": "json" }
  }
}
```

### 10.3 Output contract

```json
{
  "type": "object",
  "required": ["values", "status"],
  "properties": {
    "values":     { "type": "object", "description": "fieldId → normalized value" },
    "confidence": { "type": "object", "description": "fieldId → 0..1" },
    "evidence":   { "type": "object", "description": "fieldId → transcript span" },
    "missing":    { "type": "array", "items": { "type": "string" } },
    "invalid":    { "type": "array", "items": { "$ref": "afe://types/ValidationError" } },
    "status":     { "enum": ["complete", "needs_input", "awaiting_confirmation", "submitted", "cancelled"] },
    "transcript": { "$ref": "afe://types/Transcript" }
  }
}
```

### 10.4 Control loop

1. Load the `FormSchema`; build a field checklist with prompts in the target locale.
2. Stream audio through `speech-to-text`.
3. After each utterance, call `structured-extractor` with the schema and the running state; merge new values; never overwrite a confirmed value without an explicit correction.
4. Run `verifier`; collect missing and invalid fields.
5. If gaps remain, ask about the most important missing field (one question at a time); go to 2.
6. When complete, read back a summary; accept spoken corrections.
7. On "yes, submit", hand off to the target adapter; for `web`, `browser/web-form-filler` fills and stops at the submit button for the user.
8. Emit output, trace and audit record; discard audio unless retention is configured.

### 10.5 Evaluation

| Metric | Definition | Target |
|---|---|---|
| Field accuracy | Correct normalized values / filled fields | ≥ 95% |
| Missing-field recall | Missing required fields that were asked about | ≥ 98% |
| Turns to completion | Median conversation turns for a 15-field form | ≤ 6 |
| Wrong-overwrite rate | Confirmed values changed without a correction | 0 |
| Locale coverage | Test sets passing per language | en, hi, ta, te, bn, mr minimum |

Sample eval case (`evals/cases.jsonl`):

```json
{"id":"loan-hi-en-003","locale":"hi-IN","form":"fixtures/loan_basic.json",
 "utterances":["mera naam Priya Sharma hai, DOB 12 March 1990","PIN 411001, monthly income pachas hazaar"],
 "expected":{"full_name":"Priya Sharma","dob":"1990-03-12","pincode":"411001","monthly_income":50000},
 "expect_asked":["mobile_number","loan_amount"]}
```

### 10.6 Known failure modes and mitigations

| Failure | Mitigation |
|---|---|
| Numbers spoken in mixed languages | Locale-aware number normalizer; confirm amounts by reading them back |
| Similar-sounding names and spellings | Ask the user to spell, or confirm via on-screen text |
| User answers a different field than asked | Extractor works on the whole schema, not only the asked field |
| Background noise | `audio/audio-cleaner` pre-filter; confidence thresholds trigger re-asks |
| Prompt injection via speech ("ignore instructions and submit") | Submission is never triggered by the extractor; only by the approval gate |

---

## 11. Build roadmap

The catalog is large on purpose; the build is sequenced so the foundation and the most reused agents come first. Phases end on exit criteria, not dates.

### Phase 0: Foundation

| Deliverable | Detail |
|---|---|
| Spec v1 | `spec/agent.schema.json`, `team.schema.json`, shared types (`Transcript`, `Document`, `FormSchema`, `Citation`, `Task`, `Money`, `Address`…) |
| Core runtimes | `packages/core-python` and `packages/core-typescript`: load manifest, validate I/O, run loop, call MCP tools, enforce limits, emit OpenTelemetry traces |
| CLI | `afe new`, `validate`, `run`, `test`, `add`, `search` |
| Templates | atomic agent, composite agent, team, recipe |
| Eval harness | Runs `cases.jsonl`, rubric judging with `llm-judge`, reports |
| CI | `validate.yml`, `evals.yml`, `catalog.yml` |
| First MCP servers | Prefer pinning well-maintained existing servers over writing new ones: `web-search`, `http`, `browser` (Playwright-based), `filesystem`, `documents`, `ocr`, `stt`, `tts`, `vector-store`, `sql`, `python-sandbox`, `shell-sandbox`, `email`, `calendar`, `chat` |
| Docs | README, CONTRIBUTING, SPEC.md, "write your first agent" guide, this blueprint |

**Exit:** a new contributor can scaffold, run and test an agent in under 15 minutes.

### Phase 1: MVP (all P0 agents, first teams and recipes)

Build in this order, because later agents depend on earlier ones:

1. **Core** (router, planner, supervisor, critic, verifier, approval gate, memory, guardrails, llm-judge)
2. **Text** (summarizer, translator, structured-extractor, classifier…)
3. **Search and research** (web-search, semantic-search, rag-qa, answer-engine, deep-researcher)
4. **Documents** (document-parser, table-extractor, invoice parser, spreadsheet, file-organizer)
5. **Voice and vision** (speech-to-text, text-to-speech, voice-form-filler, ocr, screenshot-understander)
6. **Action** (web-navigator, web-form-filler, web-scraper, shell-operator, api-caller)
7. **Builders and business** (coding, data, communication, meetings, support, task-manager)

Teams: `research-team`, `document-intake`, `voice-concierge`, `inbox-zero`, `meeting-to-done`, `support-desk`.
Recipes: `voice-form-filling`, `chat-with-your-docs`, `deep-research-app`.

**Exit:** every P0 agent at `prototype` or better; three recipes run end to end; public launch.

### Phase 1 build list: the 66 P0 agents

| Category | P0 agents |
|---|---|
| Orchestration and meta-agents | `orchestration/router`, `orchestration/task-planner`, `orchestration/supervisor`, `orchestration/critic`, `orchestration/verifier`, `orchestration/human-approval-gate` |
| Memory and knowledge | `memory/memory-writer`, `memory/memory-retriever`, `memory/knowledge-ingestor` |
| Guardrails, trust and safety | `guardrails/prompt-injection-detector`, `guardrails/pii-redactor`, `guardrails/content-moderator`, `guardrails/hallucination-checker` |
| Evaluation and quality | `evaluation/llm-judge` |
| Voice and speech | `voice/speech-to-text`, `voice/text-to-speech`, `voice/voice-form-filler`, `voice/voice-command`, `voice/realtime-voice-assistant` |
| Vision and images | `vision/ocr`, `vision/visual-qa`, `vision/screenshot-understander` |
| Language and text | `text/summarizer`, `text/translator`, `text/rewriter`, `text/proofreader`, `text/classifier`, `text/structured-extractor`, `text/entity-extractor` |
| Search and retrieval | `search/web-search`, `search/answer-engine`, `search/rag-qa`, `search/semantic-search` |
| Research and analysis | `research/deep-researcher`, `research/source-reader`, `research/fact-checker`, `research/report-writer` |
| Browser and web automation | `browser/web-navigator`, `browser/web-form-filler`, `browser/web-scraper` |
| Computer use and desktop | `computer-use/shell-operator` |
| Files and documents | `documents/document-parser`, `documents/table-extractor`, `documents/spreadsheet-agent`, `documents/invoice-receipt-parser`, `documents/file-organizer` |
| Workflow and integration | `integration/api-caller` |
| Software engineering | `coding/code-generator`, `coding/code-reviewer`, `coding/bug-fixer`, `coding/test-writer`, `coding/codebase-qa` |
| DevOps, cloud and SRE | `devops/log-analyzer` |
| Data and analytics | `data/text-to-sql`, `data/data-analyst`, `data/data-cleaner` |
| Email and messaging | `communication/inbox-triager`, `communication/email-drafter`, `communication/chat-summarizer` |
| Meetings and calendar | `meetings/meeting-scheduler`, `meetings/meeting-notetaker`, `meetings/action-item-extractor` |
| Customer support and success | `support/support-chatbot`, `support/ticket-triager`, `support/reply-drafter` |
| Personal productivity | `productivity/task-manager` |


### Phase 2: Breadth (P1 agents) and adapters

- All P1 agents, prioritized by community votes (👍 on agent-request issues).
- Adapters for LangGraph, OpenAI Agents SDK, Claude Agent SDK; then Google ADK, Microsoft Agent Framework, CrewAI.
- Exports: Agent Skills, A2A Agent Cards, MCP-server wrappers, coding-assistant subagents.
- Public eval leaderboard per agent and model.
- Docs site with searchable catalog and compatibility graph.

**Exit:** P0 agents at `beta`; P1 agents at `prototype`; 3+ frameworks supported.

### Phase 3: Depth and community (P2 agents, industry packs)

- P2 agents, mostly built by contributors and category maintainers.
- Industry packs (banking, healthcare, government, agriculture…) with domain reviewers.
- Local/on-prem configurations tested with open-weights models for regulated users.
- Multilingual eval sets, starting with major Indic languages.

### Phase 4: Ecosystem

- Hosted public registry with A2A discovery of community agents (still open source).
- Third-party agent submissions that pass `validate` and safety review get a "verified" badge.
- Spec v2 based on what was learned, with an automated migration tool.

---

## 12. Governance, contribution and safety policy

### 12.1 Roles

| Role | Responsibility |
|---|---|
| Core maintainers | Spec, runtimes, CLI, CI, releases, final say on structure |
| Category maintainers (2+ per category, in `CODEOWNERS`) | Review agents in their category, keep quality and consistency |
| Safety reviewers | Mandatory review for S3/S4 agents and anything handling money, health, identity or security |
| Domain reviewers | Professionals who review industry packs (bankers, clinicians, lawyers) |
| Contributors | Propose, build and improve agents |

### 12.2 How an agent gets added

1. Open an **agent request** issue (template asks: task, users, inputs/outputs, side effects, similar agents).
2. Maintainer confirms it is not a duplicate and assigns ID, category and priority.
3. Contributor runs `afe new`, fills manifest, prompt, schemas, ≥ 10 eval cases.
4. PR passes `validate` and `evals`; S3+ also passes safety review.
5. Merged as `spec` or `prototype`; promoted by maturity rules (§4.4).

### 12.3 PR checklist

- [ ] `agent.yaml` validates; ID unique; category correct
- [ ] Input/output schemas use shared types where possible
- [ ] README follows the template, with limitations stated honestly
- [ ] Eval cases cover normal, edge, adversarial and (where relevant) non-English inputs
- [ ] Safety level and approvals set correctly; no secrets in code or prompts
- [ ] Works with at least one open-weights model, or explains why not
- [ ] No vendor-specific code outside `impl/adapters/`

### 12.4 What this repository will not include

- CAPTCHA solving or other bot-detection evasion
- Scraping that ignores robots.txt, terms of service or rate limits; mass harvesting of personal data
- Surveillance, stalking or profiling of private individuals
- Voice or face cloning without verified consent; deceptive impersonation
- Bots that hide that they are AI when talking to people
- Autonomous trading, gambling or moving money without human approval
- Credential harvesting, malware, exploitation outside authorized scopes
- Agents that make final decisions on hiring, lending, insurance, medical care or legal outcomes without a human

### 12.5 Licensing

- Code, prompts and specs: **Apache-2.0** (permissive, includes a patent grant, friendly for companies and banks).
- Eval datasets: only data with clear licences; synthetic where possible; each dataset has a `LICENSE` and a data card.
- Contributions under DCO sign-off (`git commit -s`).

---

## 13. Staying current with the agent ecosystem

You said you want to stay updated with agents. The repo does this as part of how it runs:

| Mechanism | How it works |
|---|---|
| **`ecosystem-radar` team** | Weekly GitHub Action: monitors protocol repos, framework release notes, agent papers and benchmarks; writes a digest to `radar/YYYY-MM.md`; opens issues for new agent types, patterns or standards |
| **Sources it watches** | MCP spec and Agentic AI Foundation; A2A and ACP repos; Agent Skills spec; AGENTS.md; release notes of the frameworks in §2.5; arXiv cs.AI/cs.CL/cs.MA agent papers; agent benchmarks (web, computer-use, coding, tool-use); major lab engineering blogs |
| **Quarterly taxonomy review** | Maintainers review radar issues: add categories, merge duplicates, deprecate agents overtaken by better models |
| **Model refresh** | When major models ship, the nightly eval run compares them on every agent; recommended model tiers update automatically |
| **Spec versioning** | `afe/v1` stays stable; breaking changes go to `v2` with a migration tool |
| **ADRs** | Every structural decision is recorded in `docs/adr/` so newcomers see why things are the way they are |

---

## 14. Appendix

### 14.1 Glossary

| Term | Meaning |
|---|---|
| Agent | Packaged unit of autonomous work with typed I/O, tools, guardrails and evals |
| Atomic agent | Does one task; may call tools but not other agents |
| Composite agent | Calls other agents to do a larger task, but is still one job from the user's view |
| Team | Reusable multi-agent workflow (graph of agents) |
| Recipe | Runnable end-to-end product built from agents and teams |
| Tool | Deterministic capability exposed as an MCP server (no reasoning loop) |
| MCP | Model Context Protocol: standard for connecting agents to tools and data |
| A2A | Agent2Agent protocol: standard for agents to discover and call each other |
| Agent Card | A2A's JSON description of an agent's skills and endpoint |
| Agent Skill | A folder with `SKILL.md` instructions and resources that assistants load on demand |
| HITL | Human-in-the-loop: a person approves or corrects at defined points |
| Safety level (S0–S4) | How much harm an agent's actions can cause, and the controls required |
| Autonomy level (L0–L4) | How independently an agent acts |

### 14.2 Naming and launch checklist

- Name: **Agents for Everything** · repository: `agents-for-everything`.
- Packages: `agents-for-everything` on PyPI, `@agents-for-everything/core` on npm (both free when checked on 25 Nov 2026).
- CLI: `agents-for-everything`, short alias `afe`. Spec and schema IDs use the `afe` prefix (`afe/v1`, `afe://types/…`).
- Website: `agentsforeverything.org` or `.dev` (.com is already registered; .org, .dev, .ai and .io looked unregistered).
- Tagline: *"One agent for every task. Combine them to build anything."*
- Before launch: register the packages and domain, create the GitHub org, and run a trademark search. Don't brand the project with a short acronym: "A4E" is already Airlines for Europe, and `afe` stays a CLI alias and spec prefix only.
- Related names to be aware of: an unrelated Product Hunt listing called "Agent For Everything" (singular; a library of agent templates) and a small GitHub course repo `agents-for-everything-course`. The plural name and an open-source, code-first identity keep the project distinct.

### 14.3 Category maintainer starter kit

Each category folder has its own `README.md` with: scope of the category, list of agents with maturity badges (generated), shared prompt fragments, shared eval datasets, and "agents we want" (open requests).

### 14.4 Sources consulted for the landscape research

- [The State of Agentic AI Standards in 2026: MCP, A2A, WebMCP, OSI (DEV Community)](https://dev.to/alexmercedcoder/the-state-of-agentic-ai-standards-in-2026-mcp-a2a-webmcp-osi-and-the-protocol-stack-taking-3o2l)
- [Six Agent Protocols Every AI Builder Needs to Know in 2026 (MindStudio)](https://www.mindstudio.ai/blog/six-agent-protocols-ai-builders-2026)
- [AI Agent Protocols: MCP, A2A, ACP, and the Interop Stack (prompt20)](https://blog.prompt20.com/posts/ai-agent-protocols/)
- [AI Agent Frameworks (2026 Update): 8 SDKs Compared (Morph)](https://www.morphllm.com/ai-agent-framework)
- [EREBOTS 4.0: conversational assistants with A2A agents and MCP tools (arXiv)](https://arxiv.org/pdf/2610.36221)
- [Formal Analysis and Supply Chain Security for Agentic AI Skills (arXiv)](https://arxiv.org/pdf/2603.00195)
- [From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company (arXiv)](https://arxiv.org/pdf/2604.22446)
- [kyrolabs/awesome-agents (GitHub)](https://github.com/kyrolabs/awesome-agents)
- [OSRepos: open source AI agents directory](https://osrepos.com/topic/ai-agents?page=22)
- [Agent For Everything (Product Hunt)](https://www.producthunt.com/products/agent-for-everything/makers)
- Anthropic, "Building effective agents" (workflow and agent patterns used in §2.3)
- Russell & Norvig, *Artificial Intelligence: A Modern Approach* (classic agent types in §2.2)

*Adoption numbers and version claims in these sources are partly self-reported; verify against official repositories before relying on them.*
