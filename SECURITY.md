# Security & Agent Safety Policy

## Reporting a Vulnerability

If you discover a security vulnerability, prompt-injection bypass, unsafe default permission, or leaked secret in `agents-for-everything`, please **do not** open a public issue. Email `rupeshbharambe2004@gmail.com` or use GitHub Private Vulnerability Reporting with reproduction details.

## Agent Safety Tiers (`S0`–`S4`)

Every agent manifest must declare an honest safety tier:

| Level | Scope | Required Controls |
|---|---|---|
| **S0** | Pure computation, no external access | Schema validation |
| **S1** | Reads external or private data | Read-only tool scopes; prompt-injection screening |
| **S2** | Reversible local writes or drafts | Change preview / undo capability; logged side effects |
| **S3** | External side effects (send, post, modify records, shell) | Human approval per action by default; explicit policy override |
| **S4** | High stakes (money, legal, health, identity, deletion) | Mandatory human approval, immutable audit log, domain disclaimers, no autonomous submit |

## Prohibited Uses & Excluded Agents

This repository strictly refuses and will reject pull requests containing:

- CAPTCHA solving or bot-detection evasion
- Scraping that ignores `robots.txt`, terms of service, or rate limits; mass harvesting of personal data
- Surveillance, stalking, or unauthorized profiling of individuals
- Voice or face cloning without verified consent; deceptive impersonation
- Bots that conceal they are AI when interacting directly with humans
- Autonomous financial trading, gambling, or moving money without human approval
- Credential harvesting, malware, or offensive exploitation outside authorized security test scopes
- Agents making final autonomous decisions in hiring, lending, insurance, clinical care, or legal outcomes
