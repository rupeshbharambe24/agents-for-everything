# Industry Packs (`agents/industries/`)

Vertical agent packs combining domain regulations, specialized schemas, local/on-prem open-weights profiles, and reusable horizontal agents from `core/`, `perception/`, `information/`, and `action/`.

## Available Industry Packs (12 Packs)

| Pack | Agents | S3/S4 Gated | Horizontal Agents Reused | Domain Review Focus |
|---|---|---|---|---|
| [**Agriculture**](agriculture/README.md) (`agriculture/`) | 6 | 0 | `vision/image-captioner`, `vision/ocr`, `voice/speech-to-text`, `voice/text-to-speech`, `search/rag-qa` | Designed for low-bandwidth, voice-first, Indic/regional language operation on local/edge models |
| [**Banking and financial services**](banking/README.md) (`banking/`) | 17 | 12 | `vision/id-document-reader`, `documents/document-parser`, `finance/financial-statement-analyzer`, `voice/voice-form-filler`, `voice/realtime-voice-assistant`, `security/phishing-analyzer`, `guardrails/pii-redactor` | Financial Risk & Banking Domain Review (S4 AML/KYC/Sanctions/Fraud/Credit requires compliance officer sign-off) |
| [**E-commerce and retail**](ecommerce/README.md) (`ecommerce/`) | 11 | 3 | `vision/image-captioner`, `search/semantic-search`, `text/sentiment-analyzer`, `browser/page-change-monitor` | Merchant Operations & Fraud Screening (S4 fraud flags and S3 marketplace syncs require human confirmation) |
| [**Energy and utilities**](energy/README.md) (`energy/`) | 5 | 1 | `vision/ocr`, `data/data-analyst`, `data/forecaster`, `communication/business-messaging-bot` | Grid & Utility Advisory (S3 outage communications gated behind operator approval) |
| [**Gaming and interactive entertainment**](gaming/README.md) (`gaming/`) | 4 | 0 | `memory/memory-retriever`, `memory/memory-writer`, `computer-use/desktop-operator` | Creative Continuity, Rule-Bound NPCs & Sandboxed Playtest QA |
| [**Government and civic**](government/README.md) (`government/`) | 8 | 0 | `voice/speech-to-text`, `voice/text-to-speech`, `voice/voice-form-filler`, `search/rag-qa`, `research/survey-analyst`, `search/news-monitor` | Public Sector & Citizen Accessibility (vernacular voice-first intake, citizen submits final portals) |
| [**Healthcare (clinical and provider)**](healthcare/README.md) (`healthcare/`) | 8 | 7 | `voice/speech-to-text`, `voice/speaker-diarizer`, `voice/voice-form-filler`, `text/translator`, `documents/document-parser`, `search/academic-search` | Clinician Review Only — drafts SOAP notes, intake, coding, and discharge explanations; never diagnoses or prescribes |
| [**Hospitality and food service**](hospitality/README.md) (`hospitality/`) | 4 | 1 | `voice/phone-call-agent`, `search/rag-qa`, `documents/spreadsheet-agent` | AI Disclosure on Phone/Chat Channels & S3 Booking Confirmation Gates |
| [**Insurance**](insurance/README.md) (`insurance/`) | 6 | 4 | `vision/ocr`, `documents/document-parser`, `voice/voice-form-filler`, `search/rag-qa`, `guardrails/pii-redactor` | Licensed Adjuster / Underwriter Review for S3/S4 claim, coverage, and underwriting outputs |
| [**Manufacturing and industrial**](manufacturing/README.md) (`manufacturing/`) | 6 | 0 | `vision/object-detector`, `search/rag-qa`, `voice/speech-to-text`, `voice/text-to-speech`, `voice/voice-form-filler` | EHS & Industrial Safety Review (human verification before actuator changes or maintenance lockouts) |
| [**Real estate and property**](real-estate/README.md) (`real-estate/`) | 7 | 2 | `vision/ocr`, `documents/document-parser`, `search/web-search`, `meetings/meeting-scheduler` | Fair-Housing Compliance & Property Review (S4 tenant screening applies landlord written criteria with mandatory human decision) |
| [**Science and R&D**](science/README.md) (`science/`) | 9 | 0 | `documents/document-parser`, `research/source-reader`, `voice/speech-to-text`, `coding/code-generator` | Reproducible Methods, Citation Integrity & Formal Verification Helpers |

## Regulated & Low-Bandwidth Profiles
- [`profiles/regulated-airgapped.yaml`](../../profiles/regulated-airgapped.yaml) — local `ollama` (`llama3.3:70b`) / air-gapped VPC setup for **banking, insurance, healthcare, and government**.
- [`profiles/low-bandwidth-edge.yaml`](../../profiles/low-bandwidth-edge.yaml) — edge `ollama` (`llama3.2:3b`) voice-first profile for **agriculture and civic field services**.

## Proposing Additional Industry Packs
Future planned packs (Telecom, Automotive & Mobility, Aviation, Construction, Pharma, Maritime, Mining) use the [`New Category RFC`](../../.github/ISSUE_TEMPLATE/new-category-rfc.yml) template.
