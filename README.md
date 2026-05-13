# coffee-skill

Comprehensive Codex skill pack for software engineering, AI agents, API/data work, UI/document output, and defensive security workflows.

This repository contains 16 skills:

- 15 comprehensive capability skills.
- 1 trigger-dense fallback router: `coff0xc-skill-router`.

The pack was built from a local consolidation of 87 source skills and is designed to reduce duplicate triggers while keeping broad capability coverage.

## Skills

| Skill | Focus | Security-scoped |
|---|---|---|
| `coff0xc-software-engineering` | 全面软件工程、语言开发、测试、重构、脚本、Git 和工程质量工作流 | no |
| `coff0xc-ai-agent-rag` | 全面 AI Agent、RAG、Prompt、LLM 应用、多模型协作、评测、观测和成本控制工作流 | no |
| `coff0xc-api-data-platform` | 全面 API、数据库、数据平台、CLI、SDK 和接口契约工程工作流 | no |
| `coff0xc-ui-doc-output` | 全面 UI 设计、前端体验、PDF/文档处理、报告交付和技术翻译工作流 | no |
| `coff0xc-secure-code-appsec` | 全面代码安全审计、Web/API/GraphQL/OAuth/浏览器/SPA/LLM 安全、后门检测和授权应用安全验证工作流 | yes |
| `coff0xc-cloud-devsecops` | 全面云安全、容器/Kubernetes、Serverless、DevSecOps、供应链、CI/CD 和密钥管理工作流 | yes |
| `coff0xc-detection-response` | 全面 SOC、安全运营、检测工程、威胁狩猎、威胁情报、邮件安全、恶意软件分析、取证和应急响应工作流 | yes |
| `coff0xc-vulnerability-lifecycle` | 全面漏洞研究、CVE/补丁分析、漏洞管理、风险优先级、报告、授权验证和修复跟踪工作流 | yes |
| `coff0xc-identity-zero-trust` | 全面身份安全、零信任、AD/Kerberos、IAM、权限、凭证风险、横向移动防御和访问控制审查工作流 | yes |
| `coff0xc-authorized-assessment` | 全面授权安全评估、攻击面梳理、红队计划防御化、演练边界、控制有效性验证和报告工作流 | yes |
| `coff0xc-binary-mobile-iot` | 全面二进制/逆向/内核/移动/IoT/ICS/CTF/密码学安全分析工作流 | yes |
| `coff0xc-blockchain-security` | 全面区块链、智能合约、DeFi、Web3、跨链、代币和多链安全审计工作流 | yes |
| `coff0xc-compliance-architecture` | 全面安全架构、威胁建模、合规审计、数据安全、DLP、隐私、安全基线和成熟度评估工作流 | yes |
| `coff0xc-purple-deception` | 全面紫队演练、ATT&CK 映射、控制验证、检测能力评估、蜜罐/欺骗防御和安全运营改进工作流 | yes |
| `coff0xc-network-protocol-security` | 全面网络协议、TLS/DNS/TCP/UDP/QUIC/HTTP、无线/RF/蓝牙、协议日志分析、通信安全和形式化协议建模工作流 | yes |
| `coff0xc-skill-router` | Auto-trigger fallback and routing helper | yes |

## Install

Review the skills first, then copy the folders under `skills/` into your Codex skills directory.

Typical local install target:

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

Restart or refresh Codex after copying so the client re-indexes skill metadata.

## Triggering

Skill auto-triggering depends mostly on each `SKILL.md` frontmatter `name` and `description`. This pack improves triggering by:

1. Using bilingual `Use when / 当用户请求` descriptions.
2. Including Chinese and English trigger words, tool names, acronyms, and source-skill aliases.
3. Including manual invocation phrases such as `使用 coff0xc-ai-agent-rag ...`.
4. Providing `coff0xc-skill-router` as a fallback when a specific skill does not auto-trigger.

See [docs/TRIGGERING.md](docs/TRIGGERING.md) for the routing table and troubleshooting.

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
docs/                   # Triggering, coverage, provenance, sanitization notes
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

## License

This repository is licensed under the Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
