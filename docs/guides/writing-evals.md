# Writing Evaluations

Every `prototype` agent requires **at least 10 eval cases** in `evals/cases.jsonl`.

## Required Coverage

- **Normal cases:** Standard representative inputs matching the core use case.
- **Boundary / edge cases:** Empty/short input, missing optional fields, conflicting units or dates.
- **Adversarial / safety cases:** Prompt injections embedded inside documents, emails, or transcripts; unauthorized actions gated by `S3`/`S4`.
- **Multilingual cases:** Especially for voice, text, and consumer-facing agents (including Indic languages & code-switching).

Run tests offline with deterministic mock mode (`afe test <id>`) or live against any provider (`afe test <id> --live --provider openai`).

## Case format

Each line of `evals/cases.jsonl` is one JSON object:

```json
{"id": "ext-51", "locale": "es-ES", "input": {"text": "Me llamo Lucía Gómez, correo lucia@example.org", "fields": ["full_name", "email"]}, "expected": {"extracted": {"full_name": "Lucía Gómez", "email": "lucia@example.org"}}, "live_only": true}
```

| Key | Meaning |
|---|---|
| `id` | Unique within the file (continue the existing numbering) |
| `input` | Must match `schemas/input.schema.json` |
| `expected` | Fields the output must contain with exactly these values |
| `locale` | Optional language tag, e.g. `hi-IN`, `es-ES` |
| `expect_non_empty` | Optional list of output fields that must not be empty |
| `expect_contains` | Optional `{field: substring}` checks (case-insensitive) |
| `expect_error` | Optional error class name the agent must raise (e.g. `ApprovalRequiredError`) |
| `live_only` | Optional. `true` skips the case in offline mode; use it for inputs only a real model can handle (new languages, free-form reasoning). CI runs offline, so every case **without** this flag must pass offline. |

Check your cases with `uv run afe test <category>/<agent>`. To run live-only cases against a model: `uv run afe test <category>/<agent> --live --provider ollama --model <model>`.
