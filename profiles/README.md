# Runtime & Deployment Profiles

These profiles configure `agents-for-everything` runtimes for local, on-premises, air-gapped, and low-bandwidth deployments — especially regulated **Banking**, **Healthcare**, **Government**, **Insurance**, and **Legal** packs.

| Profile | Target Environment | Default Provider | PII Redaction | External Network |
|---|---|---|---|---|
| [`local-onprem.yaml`](local-onprem.yaml) | Enterprise VPC / local workstation | `ollama` (`qwen2.5:14b`) | Enabled | Local endpoints only |
| [`regulated-airgapped.yaml`](regulated-airgapped.yaml) | Banks, hospitals, public sector | `ollama` (`llama3.3:70b`) or local vLLM | Strict + `data_retention: none` | Disabled (`S3`/`S4` mandatory HITL) |
| [`low-bandwidth-edge.yaml`](low-bandwidth-edge.yaml) | Rural voice, agriculture, field kits | `ollama` (`llama3.2:3b`) | Enabled | Minimal / intermittent sync |

See [Local & On-Premises Guide](../docs/guides/local-onprem.md) for environment variable configuration and CLI usage.
