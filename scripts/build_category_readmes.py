"""Generate enriched category & industry-pack READMEs across all 54 categories (BLUEPRINT.md §14.3)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "packages" / "core-python" / "src"))

from agents_for_everything import discover_agents  # noqa: E402

sys.path.insert(0, str(ROOT / "scripts"))
from build_readmes import CATEGORY_EMOJI, REPO_URL, badge  # noqa: E402

REGULATED_INDUSTRIES = {"banking", "insurance", "healthcare", "government"}
REGULATED_CATEGORIES = REGULATED_INDUSTRIES | {"finance", "legal", "wellness"}
VOICE_INDIC_CATS = {"voice", "accessibility", "agriculture", "government", "banking", "healthcare", "education"}

PACK_NOTES: dict[str, tuple[str, str]] = {
    "banking": (
        "Financial Risk & Banking Domain Review (S4 AML/KYC/Sanctions/Fraud/Credit requires compliance officer sign-off)",
        "`vision/id-document-reader`, `documents/document-parser`, `finance/financial-statement-analyzer`, `voice/voice-form-filler`, `voice/realtime-voice-assistant`, `security/phishing-analyzer`, `guardrails/pii-redactor`",
    ),
    "insurance": (
        "Licensed Adjuster / Underwriter Review for S3/S4 claim, coverage, and underwriting outputs",
        "`vision/ocr`, `documents/document-parser`, `voice/voice-form-filler`, `search/rag-qa`, `guardrails/pii-redactor`",
    ),
    "healthcare": (
        "Clinician Review Only — drafts SOAP notes, intake, coding, and discharge explanations; never diagnoses or prescribes",
        "`voice/speech-to-text`, `voice/speaker-diarizer`, `voice/voice-form-filler`, `text/translator`, `documents/document-parser`, `search/academic-search`",
    ),
    "ecommerce": (
        "Merchant Operations & Fraud Screening (S4 fraud flags and S3 marketplace syncs require human confirmation)",
        "`vision/image-captioner`, `search/semantic-search`, `text/sentiment-analyzer`, `browser/page-change-monitor`",
    ),
    "real-estate": (
        "Fair-Housing Compliance & Property Review (S4 tenant screening applies landlord written criteria with mandatory human decision)",
        "`vision/ocr`, `documents/document-parser`, `search/web-search`, `meetings/meeting-scheduler`",
    ),
    "manufacturing": (
        "EHS & Industrial Safety Review (human verification before actuator changes or maintenance lockouts)",
        "`vision/object-detector`, `search/rag-qa`, `voice/speech-to-text`, `voice/text-to-speech`, `voice/voice-form-filler`",
    ),
    "agriculture": (
        "Designed for low-bandwidth, voice-first, Indic/regional language operation on local/edge models",
        "`vision/image-captioner`, `vision/ocr`, `voice/speech-to-text`, `voice/text-to-speech`, `search/rag-qa`",
    ),
    "energy": (
        "Grid & Utility Advisory (S3 outage communications gated behind operator approval)",
        "`vision/ocr`, `data/data-analyst`, `data/forecaster`, `communication/business-messaging-bot`",
    ),
    "government": (
        "Public Sector & Citizen Accessibility (vernacular voice-first intake, citizen submits final portals)",
        "`voice/speech-to-text`, `voice/text-to-speech`, `voice/voice-form-filler`, `search/rag-qa`, `research/survey-analyst`, `search/news-monitor`",
    ),
    "hospitality": (
        "AI Disclosure on Phone/Chat Channels & S3 Booking Confirmation Gates",
        "`voice/phone-call-agent`, `search/rag-qa`, `documents/spreadsheet-agent`",
    ),
    "science": (
        "Reproducible Methods, Citation Integrity & Formal Verification Helpers",
        "`documents/document-parser`, `research/source-reader`, `voice/speech-to-text`, `coding/code-generator`",
    ),
    "gaming": (
        "Creative Continuity, Rule-Bound NPCs & Sandboxed Playtest QA",
        "`memory/memory-retriever`, `memory/memory-writer`, `computer-use/desktop-operator`",
    ),
}


def _parse_category_meta() -> dict[tuple[str, str], str]:
    bp = (ROOT / "BLUEPRINT.md").read_text(encoding="utf-8")
    cat_re = re.compile(
        r"^#### 7\.\d+\s+(.+?)\s+—\s+`agents/([^/]+)/([^/]+)/`\s+·\s+ID prefix `([^/]+)/`",
        re.M,
    )
    out: dict[tuple[str, str], str] = {}
    for m in cat_re.finditer(bp):
        title, fam, cat, _ = m.groups()
        out[(fam, cat)] = title.strip()
    return out


def main() -> int:
    agents = discover_agents(ROOT)
    cat_titles = _parse_category_meta()

    grouped: dict[tuple[str, str], list] = {}
    for m in agents.values():
        grouped.setdefault((m.family, m.category), []).append(m)

    for (fam, cat), members in sorted(grouped.items()):
        members.sort(key=lambda x: (x.priority, x.id))
        title = cat_titles.get((fam, cat), cat.replace("-", " ").title())
        cat_dir = ROOT / "agents" / fam / cat

        emoji = CATEGORY_EMOJI.get(cat, "🤖")
        n0 = sum(1 for x in members if x.priority == "P0")
        n1 = sum(1 for x in members if x.priority == "P1")
        n2 = sum(1 for x in members if x.priority == "P2")
        crumbs = "[🏠 Agents for Everything](../../../README.md) › [📖 Catalog](../../../CATALOG.md)"
        if fam == "industries":
            crumbs += " › [🏢 Industry packs](../README.md)"
        lines = [
            "<!-- Generated by scripts/build_category_readmes.py — edit agent.yaml files, not this page. -->",
            "",
            crumbs + f" › **{title}**",
            "",
            f"# {emoji} {title}",
            "",
            " ".join([
                badge("agents", str(len(members)), "2563eb"),
                badge("P0", str(n0), "7c3aed"), badge("P1", str(n1), "8b5cf6"), badge("P2", str(n2), "a78bfa"),
                badge("family", fam, "0d9488"),
            ]),
            "",
            f"Every agent below lives in `agents/{fam}/{cat}/<slug>/` and has the ID prefix `{cat}/`.",
            "",
        ]

        if cat in REGULATED_CATEGORIES:
            lines.extend([
                "> **Regulated / High-Assurance Policy:** Supports local/on-prem open-weights deployment "
                "([`regulated-airgapped.yaml`](../../../profiles/regulated-airgapped.yaml)), PII redaction in traces, "
                "and mandatory human sign-off on `S3`/`S4` actions (`SAFETY_REVIEW.md`).",
                "",
            ])

        lines.extend([
            "## Agents in This Category",
            "",
            "| ID | Name | Tier | Priority | Maturity | Safety | Summary |",
            "|---|---|---|---|---|---|---|",
        ])
        for m in members:
            slug = m.id.split("/", 1)[1]
            lines.append(
                f"| [`{m.id}`]({slug}/README.md) | {m.name} | {m.tier} | {m.priority} | `{m.maturity}` | {m.safety_level} | {m.summary} |"
            )

        # Horizontal reuse (especially for industries & composites)
        reused = sorted({dep for m in members for dep in m.uses_agents})
        lines.extend(["", "## Horizontal Composition & Reuse"])
        if fam == "industries" and cat in PACK_NOTES:
            review_note, pack_horiz = PACK_NOTES[cat]
            lines.append(f"- **Domain Review Focus:** {review_note}.")
            lines.append(f"- **Core Horizontal Building Blocks Reused:** {pack_horiz}.")
        if reused:
            lines.append("- **Direct `uses_agents` Dependencies:** " + ", ".join(f"`{r}`" for r in reused))
        elif fam != "industries":
            lines.append("- Atomic capabilities in this category compose via standard `afe://types/*` contracts and upstream/downstream `compatibility-graph.json` edges.")

        lines.extend([
            "",
            "## Shared Prompt & Safety Conventions",
            "- Treat untrusted external text, documents, and web pages strictly as data to prevent prompt injection.",
            "- Return strict JSON matching each agent's `schemas/output.schema.json`.",
            "- Declare least-privilege MCP servers in `tools.yaml`; `S0` agents declare zero tools.",
            "",
            "## Shared Evaluation & Profiles",
            "- Shared datasets: [`evals/datasets/README.md`](../../../evals/datasets/README.md)"
            + (" (`indic_voice_queries.jsonl`, `multilingual_form_utterances.jsonl`)" if cat in VOICE_INDIC_CATS else ""),
            "- Local/on-prem profiles: [`profiles/README.md`](../../../profiles/README.md)",
            "",
            "## Quick CLI Commands",
            "```bash",
            f"afe search --category {cat}",
            f"afe add {members[0].id} --dest ./my-app/agents",
            f"afe test {members[0].id}",
            "```",
            "",
            "## 🤝 Contribute to this category",
            "",
            f"Missing an agent for a {title.lower()} task? [Request it]({REPO_URL}/issues/new?template=agent-request.yml) "
            f"or build it: `afe new --tier atomic --category {cat} --slug <your-agent>`, then follow the "
            "[contributing guide](../../../CONTRIBUTING.md). Adding eval cases to an existing agent is a great first contribution.",
            "",
        ])

        (cat_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")

    # Build Industry Packs Index at agents/industries/README.md
    ind_dir = ROOT / "agents" / "industries"
    ind_lines = [
        "<!-- Generated by scripts/build_category_readmes.py — edit agent.yaml files, not this page. -->",
        "",
        "[🏠 Agents for Everything](../../README.md) › [📖 Catalog](../../CATALOG.md) › **Industry packs**",
        "",
        "# 🏢 Industry Packs",
        "",
        "Vertical agent packs combining domain regulations, specialized schemas, local/on-prem open-weights profiles, and reusable horizontal agents from `core/`, `perception/`, `information/`, and `action/`.",
        "",
        "## Available Industry Packs (12 Packs)",
        "",
        "| Pack | Agents | S3/S4 Gated | Horizontal Agents Reused | Domain Review Focus |",
        "|---|---|---|---|---|",
    ]
    for (fam, cat), members in sorted(grouped.items()):
        if fam != "industries":
            continue
        title = cat_titles.get((fam, cat), cat.title())
        s34 = sum(1 for m in members if m.safety_level in {"S3", "S4"})
        review_note, horiz = PACK_NOTES.get(cat, ("Domain maintainer review", "Core/Voice/Docs"))
        ind_lines.append(
            f"| {CATEGORY_EMOJI.get(cat, '')} [**{title}**]({cat}/README.md) (`{cat}/`) | {len(members)} | {s34} | {horiz} | {review_note} |"
        )
    ind_lines.extend([
        "",
        "## Regulated & Low-Bandwidth Profiles",
        "- [`profiles/regulated-airgapped.yaml`](../../profiles/regulated-airgapped.yaml) — local `ollama` (`llama3.3:70b`) / air-gapped VPC setup for **banking, insurance, healthcare, and government**.",
        "- [`profiles/low-bandwidth-edge.yaml`](../../profiles/low-bandwidth-edge.yaml) — edge `ollama` (`llama3.2:3b`) voice-first profile for **agriculture and civic field services**.",
        "",
        "## Proposing Additional Industry Packs",
        "Future planned packs (Telecom, Automotive & Mobility, Aviation, Construction, Pharma, Maritime, Mining) use the [`New Category RFC`](../../.github/ISSUE_TEMPLATE/new-category-rfc.yml) template.",
        "",
    ])
    (ind_dir / "README.md").write_text("\n".join(ind_lines), encoding="utf-8")

    print(f"Generated {len(grouped)} category READMEs + agents/industries/README.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
