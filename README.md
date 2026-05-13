# coffee-skill

`coffee-skill` is a publish-ready Codex skill pack for practical engineering, AI agents, documentation, and defensive security work.

It turns a broad, fragmented skill collection into a smaller set of high-coverage skills with stronger trigger descriptions, clear safety boundaries, validation checklists, and a fallback router for cases where automatic skill triggering misses the user's intent.

Recommended GitHub About text:

```text
Comprehensive Codex skills pack for engineering, AI agents, docs, and defensive security, with multilingual triggers, validation checklists, and a router fallback
```

## Why This Exists

AI coding agents often have two recurring problems:

1. Skills become too fragmented. The agent may have many narrow skills, but similar tasks trigger the wrong one or no skill at all.
2. Skills may describe capability in the body, while clients usually trigger from frontmatter `name` and `description`.

This repository solves those problems by:

- consolidating 87 source skills into 15 comprehensive capability skills,
- adding `coff0xc-skill-router` as a trigger-dense fallback,
- writing trigger descriptions and usage notes for Chinese, English, and common international users,
- keeping security topics defensive and authorization-scoped,
- including validation, provenance, triggering, and sanitization documentation.

## What Is Inside

This repository contains 16 skills:

- 15 comprehensive capability skills.
- 1 trigger fallback router: `coff0xc-skill-router`.

| Skill | Use it for | Security-scoped |
|---|---|---|
| `coff0xc-software-engineering` | Software engineering, language development, testing, refactoring, scripts, Git | no |
| `coff0xc-ai-agent-rag` | AI agents, RAG, prompts, LLM apps, tool calling, evals, observability | no |
| `coff0xc-api-data-platform` | REST, GraphQL, OpenAPI, databases, CLI, SDK, data contracts | no |
| `coff0xc-ui-doc-output` | UI/frontend work, PDF/document output, reports, translation | no |
| `coff0xc-secure-code-appsec` | Code audit, Web/API/GraphQL/OAuth/browser/LLM app security | yes |
| `coff0xc-cloud-devsecops` | Cloud, Docker, Kubernetes, CI/CD, supply chain, secret handling | yes |
| `coff0xc-detection-response` | SOC, SIEM, detection engineering, YARA/Sigma, IR, forensics, malware triage | yes |
| `coff0xc-vulnerability-lifecycle` | CVE research, patch analysis, vuln management, reports, remediation tracking | yes |
| `coff0xc-identity-zero-trust` | IAM, SSO, MFA, AD/Kerberos, privileges, credentials, Zero Trust | yes |
| `coff0xc-authorized-assessment` | Authorized assessment planning, ROE, control validation, red-team-to-defense mapping | yes |
| `coff0xc-binary-mobile-iot` | Reverse engineering, binary/mobile/IoT/ICS/CTF/crypto analysis | yes |
| `coff0xc-blockchain-security` | Smart contracts, DeFi, Web3, multi-chain audit routing | yes |
| `coff0xc-compliance-architecture` | Threat modeling, compliance, data security, DLP, privacy, baselines | yes |
| `coff0xc-purple-deception` | Purple team exercises, ATT&CK mapping, honeypots, deception defense | yes |
| `coff0xc-network-protocol-security` | Network protocols, TLS/DNS/QUIC/HTTP, packet analysis, wireless security | yes |
| `coff0xc-skill-router` | Fallback skill routing when a specific skill does not auto-trigger | yes |

## Why Use It

- **Broad coverage without clutter**: 87 source skills are mapped into 15 capability areas.
- **Better automatic triggering**: frontmatter descriptions include Chinese, English, common domain terms, source aliases, acronyms, and manual invocation phrases.
- **Router fallback**: `coff0xc-skill-router` catches broad requests and routes them to the right capability skill.
- **Practical workflows**: every capability skill includes when to use it, when not to use it, a capability matrix, workflow stages, hard gates, validation checks, and anti-patterns.
- **Defensive security posture**: security skills focus on authorized assets, detection, hardening, verification, reporting, and safe assessment planning.
- **Publication hygiene**: this repo includes provenance, sanitization notes, validation scripts, Apache-2.0 license, and NOTICE.

## What Each Skill Gives You

Each capability skill is written to make the agent do useful work instead of only giving generic advice:

- clear trigger terms in frontmatter,
- when-to-use and when-not-to-use boundaries,
- source-skill routing notes,
- phased workflow,
- evidence levels,
- hard gates for risky work,
- validation checklist,
- anti-patterns,
- compact output contract.

## Where You Can Use It

Use `coffee-skill` in local Codex-style skill directories or compatible clients that load `SKILL.md` folders.

Good fits:

- daily coding and refactoring,
- AI Agent / RAG system design,
- API, database, and CLI engineering,
- UI and document generation workflows,
- defensive application security reviews,
- cloud and DevSecOps reviews,
- detection engineering and incident response,
- vulnerability research and remediation planning,
- identity, Zero Trust, and AD/Kerberos defense,
- blockchain smart contract audit preparation,
- compliance, architecture, and threat modeling.

Not a fit:

- unauthorized access,
- credential theft,
- phishing collection,
- persistence or C2 operation,
- evasion guidance,
- destructive actions,
- production or remote changes without explicit authorization.

## Install

Review the skills first, then copy the folders under `skills/` into your Codex skills directory.

Typical local install target on Windows:

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

Restart or refresh Codex after copying so the client re-indexes skill metadata.

## How To Use

Ask naturally:

```text
帮我审计这个项目的 Web/API 安全问题
用 Agent/RAG 的方式设计一个本地知识库助手
检查这个 K8s 和 CI/CD 配置有没有供应链风险
帮我写一条检测这个日志行为的 Sigma/YARA 规则
```

If auto-triggering misses, invoke the skill explicitly:

```text
使用 coff0xc-skill-router 帮我选择合适 skill
使用 coff0xc-ai-agent-rag 设计一个 RAG Agent
使用 coff0xc-secure-code-appsec 审计这个项目
使用 coff0xc-cloud-devsecops 检查 K8s 和 CI/CD
使用 coff0xc-detection-response 写检测规则
```

See [docs/TRIGGERING.md](docs/TRIGGERING.md) and [docs/USAGE.md](docs/USAGE.md).

## Languages

The skill content is primarily Chinese + English. The trigger strategy also includes common English tool names and acronyms.

Quick reference files are available for multiple languages:

- [English / 中文 / 日本語 / 한국어 / Español / Français / Deutsch / Português / Italiano / Nederlands / Polski / Русский / العربية / Türkçe / हिन्दी / Bahasa Indonesia / Tiếng Việt / ไทย](docs/LANGUAGES.md)

These translations are lightweight usage references, not separate skill implementations.

## Safety Scope

Security-related skills are defensive and authorization-scoped. They are intended for:

- owned or explicitly authorized assets,
- local code and configuration review,
- logs, reports, samples, lab environments, CTFs, and training ranges,
- detection, hardening, verification, and reporting.

They do not include instructions for unauthorized exploitation, credential theft, persistence, detection evasion, C2 operation, phishing collection, data exfiltration, or destructive actions.

See [SECURITY.md](SECURITY.md) and [docs/SANITIZATION.md](docs/SANITIZATION.md).

## Repository Layout

```text
skills/                 # Installable skill folders
docs/                   # Usage, triggering, coverage, provenance, sanitization notes
scripts/                # Local validation helper
manifest.json           # Machine-readable skill inventory
LICENSE                 # Apache License 2.0
NOTICE                  # Attribution notice
README.md               # This file
```

## Validation

Run:

```powershell
python .\scripts\validate_release.py
```

The validator checks:

- every skill folder has a matching `SKILL.md` frontmatter name,
- required release docs exist,
- all manifest skills exist,
- no local user path, private key, GitHub token, or OpenAI-style key pattern is present.

## Documentation

- [Usage Guide](docs/USAGE.md)
- [Triggering Guide](docs/TRIGGERING.md)
- [Coverage Matrix](docs/COVERAGE.md)
- [Language References](docs/LANGUAGES.md)
- [Sanitization Notes](docs/SANITIZATION.md)
- [Provenance](docs/PROVENANCE.md)
- [Security Policy](SECURITY.md)

## License

This repository is licensed under the Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
