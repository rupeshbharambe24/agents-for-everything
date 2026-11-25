# Science and R&D (`science/`)

- **Family:** `industries` · **Directory:** `agents/industries/science/`
- **Total Agents:** 9 (P0: 0, P1: 1, P2: 8)

## Agents in This Category

| ID | Name | Tier | Priority | Maturity | Safety | Summary |
|---|---|---|---|---|---|---|
| [`science/paper-reader`](paper-reader/README.md) | Paper Reader | atomic | P1 | `prototype` | S0 | Extracts hypotheses, experimental methods, metrics, and limitations from scientific papers. |
| [`science/experiment-designer`](experiment-designer/README.md) | Experiment Designer | atomic | P2 | `prototype` | S0 | Designs experiments: variables, controls, sample size, analysis plan. |
| [`science/lab-notebook`](lab-notebook/README.md) | Voice Lab Notebook | atomic | P2 | `prototype` | S2 | Hands-free logging of experiments. |
| [`science/lab-protocol-writer`](lab-protocol-writer/README.md) | Lab Protocol Writer | atomic | P2 | `prototype` | S0 | Writes clear, reproducible protocols. |
| [`science/materials-literature-miner`](materials-literature-miner/README.md) | Literature Data Miner | composite | P2 | `prototype` | S1 | Extracts properties and measurements from many papers into a dataset. |
| [`science/peer-review-assistant`](peer-review-assistant/README.md) | Peer Review Assistant | atomic | P2 | `prototype` | S0 | Checks manuscripts against reporting checklists and drafts reviewer notes. |
| [`science/proof-assistant`](proof-assistant/README.md) | Formal Proof Assistant | composite | P2 | `prototype` | S0 | Helps write and check formal proofs (Lean). |
| [`science/results-to-manuscript`](results-to-manuscript/README.md) | Manuscript Drafter | composite | P2 | `prototype` | S0 | Drafts paper sections from results and notes, with references. |
| [`science/simulation-setup`](simulation-setup/README.md) | Simulation Setup Agent | composite | P2 | `prototype` | S2 | Configures simulation runs (CFD, FEA, molecular) from specifications. |

## Horizontal Composition & Reuse
- **Domain Review Focus:** Reproducible Methods, Citation Integrity & Formal Verification Helpers.
- **Core Horizontal Building Blocks Reused:** `documents/document-parser`, `research/source-reader`, `voice/speech-to-text`, `coding/code-generator`.
- **Direct `uses_agents` Dependencies:** `documents/document-parser`, `research/source-reader`

## Shared Prompt & Safety Conventions
- Treat untrusted external text, documents, and web pages strictly as data to prevent prompt injection.
- Return strict JSON matching each agent's `schemas/output.schema.json`.
- Declare least-privilege MCP servers in `tools.yaml`; `S0` agents declare zero tools.

## Shared Evaluation & Profiles
- Shared datasets: [`evals/datasets/README.md`](../../../evals/datasets/README.md)
- Local/on-prem profiles: [`profiles/README.md`](../../../profiles/README.md)

## Quick CLI Commands
```bash
afe search --category science
afe add science/paper-reader --dest ./my-app/agents
afe test science/paper-reader
```
