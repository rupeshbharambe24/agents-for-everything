# 🤝 Contributing to Agents for Everything

Thank you for helping build the open library of AI agents! 🎉 Whether you fix a typo, add one eval case or build a whole industry pack, your contribution matters.

**New here?** Pick something from [Ways to contribute](#-ways-to-contribute), set up in [two minutes](#-set-up-in-two-minutes), and open a pull request. We review every PR.

---

## 🌱 Ways to contribute

| Contribution | Difficulty | How |
|---|:---:|---|
| 🐛 Report a bug or confusing doc | ⭐ | [Bug report](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?template=bug.yml) |
| 💡 Request an agent | ⭐ | [Agent request](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?template=agent-request.yml) |
| 🧪 Add eval cases to an existing agent | ⭐ | Append lines to `agents/<family>/<category>/<agent>/evals/cases.jsonl` |
| 🌍 Add non-English test cases or translations | ⭐⭐ | Same as above, with a `locale` field (e.g. `"hi-IN"`, `"es-ES"`) |
| ✍️ Improve an agent's prompt or limitations | ⭐⭐ | Edit `prompts/system.md` or the `Limitations` section of its README |
| 🧩 Build a new agent | ⭐⭐⭐ | [Add a new agent](#-add-a-new-agent) |
| 🔌 Add a live-model implementation or framework adapter | ⭐⭐⭐ | [Writing an agent](docs/guides/writing-an-agent.md) |
| 🏢 Propose a new category or industry pack | ⭐⭐⭐ | [New category RFC](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?template=new-category-rfc.yml) |

Issues labelled [`good first issue`](https://github.com/rupeshbharambe24/agents-for-everything/labels/good%20first%20issue) are a great place to start.

---

## ⚡ Set up in two minutes

You need Python 3.10+ and [uv](https://docs.astral.sh/uv/). Node.js 22.6+ is only needed for the TypeScript packages.

```bash
git clone https://github.com/<your-username>/agents-for-everything.git   # your fork
cd agents-for-everything
uv sync --all-packages        # installs the core runtime and the `afe` CLI
uv run afe validate           # should finish with no errors
```

No API keys are needed: agents run in an offline, deterministic mode for development and CI.

---

## 🧩 Add a new agent

1. **Check it doesn't exist yet.**
   ```bash
   uv run afe search "<your task>"
   ```
2. **Scaffold it from the template.**
   ```bash
   uv run afe new --tier atomic --category <category> --slug <agent-slug>
   ```
3. **Write the contract first.**
   - `agent.yaml`: unique `<category>/<slug>` ID, capabilities, tools, safety level (`S0`–`S4`), autonomy (`L0`–`L4`).
   - `schemas/input.schema.json` and `schemas/output.schema.json`: reuse [shared types](spec/types) (`afe://types/...`) where possible.
   - `prompts/system.md`: clear instructions for the model.
4. **Implement and test.**
   - `impl/python/agent.py`, using the `agents-for-everything` core runtime.
   - **At least 10 eval cases** in `evals/cases.jsonl`: normal, edge, adversarial (prompt injection) and, where relevant, non-English inputs.
5. **Check and regenerate.**
   ```bash
   uv run afe validate
   uv run afe test <category>/<agent-slug>
   uv run afe verify <category>/<agent-slug>
   python3 scripts/build_catalog.py            # CATALOG.md and registry/
   python3 scripts/build_readmes.py            # agent, team, recipe and MCP-server READMEs
   python3 scripts/build_category_readmes.py   # category READMEs
   ```

> **Don't hand-edit generated files.** `CATALOG.md`, `registry/`, category READMEs and the generated block of each agent README come from the manifests. Edit `agent.yaml` (or the Limitations section) and rerun the scripts. CI checks that generated files are up to date.

---

## ✅ Pull request checklist

- [ ] `uv run afe validate` passes
- [ ] `agent.yaml` validates; the ID is unique and kebab-case
- [ ] Input and output schemas reuse shared types where possible
- [ ] Eval cases cover normal, edge and adversarial inputs (≥ 10 for `prototype`)
- [ ] The safety level and `approval_required_for` gates are conservative
- [ ] Generated files are regenerated (see step 5)
- [ ] No API keys, secrets or vendor-locked code outside `impl/adapters/`
- [ ] Nothing on the [prohibited uses list](SECURITY.md#prohibited-uses--excluded-agents)
- [ ] Commits are signed off (`git commit -s`)

**Commit messages** follow [Conventional Commits](https://www.conventionalcommits.org/): `feat(voice): add wake-word agent`, `fix(evals): …`, `docs(readme): …`.

---

## 🛡️ Safety-sensitive agents

Agents at **S3** (external side effects) or **S4** (money, legal, health, identity, deletion) need a `SAFETY_REVIEW.md` and approval from a safety reviewer. See the [safety review guide](docs/guides/safety-review.md).

---

## 📜 License and sign-off

All contributions are licensed under **[Apache-2.0](LICENSE)**. Sign off each commit (`git commit -s`) to certify the [Developer Certificate of Origin](https://developercertificate.org/).

By participating you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

**Questions?** [Open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new). Thank you for contributing! 💖
