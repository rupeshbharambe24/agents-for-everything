# Publishing releases and packages

This guide covers the one-time setup for publishing Agents for Everything to **PyPI** (Python) and **npm** (JavaScript), and how to cut a release.

## Packages

| Registry | Name | Folder | What it is |
|---|---|---|---|
| PyPI | `agents-for-everything` | `packages/core-python` | Core runtime: manifests, runner, safety, providers, exporters |
| PyPI | `agents-for-everything-cli` | `cli` | The `afe` command-line tool |
| npm | `@agents-for-everything/core` | `packages/core-typescript` | TypeScript runtime (not yet built for publishing) |
| npm | `@agents-for-everything/adapters` | `packages/adapters` | Framework adapters (not yet built for publishing) |

## One-time setup: PyPI (Trusted Publishing, no API tokens)

PyPI has no "reserve a name" button: a name belongs to whoever publishes it first. With Trusted Publishing, GitHub Actions publishes for you, so you never create or store an API token.

1. Create an account at <https://pypi.org/account/register/> and turn on two-factor authentication.
2. Go to <https://pypi.org/manage/account/publishing/> → **Add a new pending publisher** → **GitHub**, and fill in:

   | Field | Value |
   |---|---|
   | PyPI Project Name | `agents-for-everything` |
   | Owner | `rupeshbharambe24` |
   | Repository name | `agents-for-everything` |
   | Workflow name | `release.yml` |
   | Environment name | `pypi` |

3. Repeat step 2 with the project name `agents-for-everything-cli`.
4. On GitHub: **Settings → Environments → New environment** named `pypi`. (Optional: add yourself as a required reviewer so every publish waits for your click.)

A pending publisher does **not** reserve the name until the first upload succeeds, so cut the first release soon after.

## One-time setup: npm (claim the scope)

Scoped names like `@agents-for-everything/core` belong to the npm **organization** `agents-for-everything`. Creating the organization claims every name under it, without publishing anything.

1. Create an account at <https://www.npmjs.com/signup> and turn on two-factor authentication.
2. Go to <https://www.npmjs.com/org/create>, enter `agents-for-everything`, and pick the **free** plan (unlimited public packages).

Publish the TypeScript packages later, once they have a build step that outputs JavaScript (Node does not strip TypeScript types inside `node_modules`).

## Cutting a release

```bash
git tag -a v0.1.0 -m "v0.1.0"
git push origin v0.1.0
```

The [`release.yml`](../../.github/workflows/release.yml) workflow then:

1. exports A2A cards and Agent Skills for every agent,
2. builds both Python packages,
3. creates a GitHub Release with the exports, catalog and packages attached,
4. publishes both packages to PyPI (only after the PyPI setup above).

Use a hyphenated tag (for example `v0.2.0-rc.1`) for a pre-release. Bump `version` in `packages/core-python/pyproject.toml` and `cli/pyproject.toml` before each new tag: PyPI rejects re-uploading an existing version.

## Check a build locally

```bash
uv build packages/core-python --out-dir /tmp/afe-dist
uv build cli --out-dir /tmp/afe-dist
uvx twine check /tmp/afe-dist/*
```
