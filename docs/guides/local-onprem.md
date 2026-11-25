# Local & On-Premises Deployment Guide

Regulated industries (**Banking**, **Insurance**, **Healthcare**, **Government**, and **Legal**) as well as privacy-conscious personal workflows can run `agents-for-everything` **100% locally** using open-weights models with zero external cloud calls.

## 1. Option A: Ollama (Workstation or Air-Gapped Server)

```bash
export AFE_PROVIDER=ollama
export OLLAMA_HOST=http://127.0.0.1:11434
export AFE_MODEL=qwen2.5:14b

PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli run banking/kyc-onboarding \
  --provider ollama \
  --input '{"input":"Verify KYC record REF-104"}'
```

## 2. Option B: Self-Hosted vLLM / llama.cpp (OpenAI-Compatible)

```bash
export AFE_PROVIDER=openai
export OPENAI_BASE_URL=http://127.0.0.1:8000/v1
export OPENAI_API_KEY=local-token
export AFE_MODEL=meta-llama/Llama-3.3-70B-Instruct
```

## 3. Mandatory Regulated Controls (`S3` / `S4`)

- Every `S4` agent requires an explicit `approval_handler` or `--auto-approve` in sandboxed verification tests; unapproved high-stakes actions raise `ApprovalRequiredError`.
- Trace spans automatically mask email, phone, 12-digit IDs, PAN, and API keys via `redact_pii` (`mask_pii=True`).
- Reference configurations live in [`profiles/`](../../profiles/README.md).
