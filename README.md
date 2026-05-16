# coffee-skill

中文 | [English](#english)

`coffee-skill` 是一套可发布的 Codex skill pack，覆盖软件工程、AI Agent/RAG、API 与数据平台、UI/文档输出、科研 draw.io 架构图、以及防御性安全工作流。

它把分散的技能集合整理成更少但覆盖更广的能力型 skills，并强化了 frontmatter 触发描述、手动触发短语、安全边界、验证清单和兜底路由，降低“该触发却没触发”的概率。

推荐 GitHub About：

```text
Comprehensive Codex skills pack for engineering, AI agents, docs, research draw.io diagrams, and defensive security, with multilingual triggers and a router fallback
```

## 为什么做这个

AI coding agent 常见两个问题：

1. 技能太碎。类似任务可能触发错 skill，或者完全不触发。
2. 很多客户端主要根据 `SKILL.md` frontmatter 里的 `name` 和 `description` 选择 skill，正文写得再强也不一定会被读取。

这个仓库的处理方式：

- 把 87 个来源 skills 合并成 16 个综合能力 skills。
- 新增 `coff0xc-research-drawio-diagram`，专门处理科研算法架构图、论文方法图和可编辑 `.drawio` 输出。
- 加入 `coff0xc-skill-router` 作为触发兜底入口。
- 为中文、英文和多语言用户写清楚触发词、用途和失败时的手动调用方式。
- 安全类内容限定在授权、防御、检测、加固、验证和报告范围内。
- 提供发布校验、来源说明、敏感信息清理说明和触发率 proxy eval。

## 包含什么

本仓库包含 17 个 skills：

- 16 个综合能力 skills。
- 1 个兜底路由 skill：`coff0xc-skill-router`。

| Skill | 用途 | 安全边界 |
|---|---|---|
| `coff0xc-software-engineering` | dev/自主开发、全栈或多文件实现、测试、重构、脚本、Git | 否 |
| `coff0xc-ai-agent-rag` | AI Agent、RAG、Prompt、LLM 应用、工具调用、评测、观测 | 否 |
| `coff0xc-api-data-platform` | REST、GraphQL、OpenAPI、数据库、CLI、SDK、数据契约 | 否 |
| `coff0xc-ui-doc-output` | UI/前端、PDF/文档输出、报告、翻译润色 | 否 |
| `coff0xc-research-drawio-diagram` | 科研算法架构图、论文方法图、模型结构图、实验流程图、可编辑 draw.io/diagrams.net `.drawio` 文件 | 否 |
| `coff0xc-secure-code-appsec` | 代码审计、Web/API/GraphQL/OAuth/浏览器/LLM 应用安全 | 是 |
| `coff0xc-cloud-devsecops` | 云、Docker、Kubernetes、CI/CD、供应链、密钥处理 | 是 |
| `coff0xc-detection-response` | SOC、SIEM、检测工程、YARA/Sigma、应急响应、取证、恶意样本分诊 | 是 |
| `coff0xc-vulnerability-lifecycle` | CVE 研究、补丁分析、漏洞管理、报告、修复跟踪 | 是 |
| `coff0xc-identity-zero-trust` | IAM、SSO、MFA、AD/Kerberos、权限、凭证、零信任 | 是 |
| `coff0xc-authorized-assessment` | 授权评估规划、ROE、控制验证、红队到防御映射 | 是 |
| `coff0xc-binary-mobile-iot` | 逆向、二进制、移动、IoT、ICS、CTF、密码分析 | 是 |
| `coff0xc-blockchain-security` | 智能合约、DeFi、Web3、多链审计路由 | 是 |
| `coff0xc-compliance-architecture` | 威胁建模、合规、数据安全、DLP、隐私、基线 | 是 |
| `coff0xc-purple-deception` | 紫队演练、ATT&CK 映射、蜜罐、欺骗防御 | 是 |
| `coff0xc-network-protocol-security` | 网络协议、TLS/DNS/QUIC/HTTP、抓包分析、无线安全 | 是 |
| `coff0xc-skill-router` | 当具体 skill 未自动触发时，选择和路由到合适 skill | 是 |

## 为什么好用

- **覆盖广但不杂乱**：87 个来源 skills + 新增科研 draw.io 绘图工作流，被整理成 16 个能力域。
- **更容易自动触发**：frontmatter 中包含中文、英文、缩写、常见口语触发词和手动调用短语。
- **有兜底路由**：不确定该用哪个 skill 时，直接调用 `coff0xc-skill-router`。
- **能交付结果**：每个能力 skill 都包含适用/不适用边界、能力矩阵、阶段工作流、硬门槛、验证清单和反模式。
- **科研图可编辑**：`coff0xc-research-drawio-diagram` 不是只给 Mermaid 或 PNG，而是生成可在 diagrams.net/draw.io 打开的 `.drawio` 源文件。
- **安全边界清楚**：安全类技能只面向授权资产、防御、检测、加固、验证和报告。
- **发布卫生完整**：包含 Apache-2.0 license、NOTICE、provenance、sanitization notes、validator 和 trigger eval。

## draw.io 科研图 skill

`coff0xc-research-drawio-diagram` 用于把论文、算法、模型结构或实验流程转成可编辑的 `.drawio` 图。

它适合：

- 根据论文 PDF、arXiv、OpenReview、官方 GitHub 或项目文档画方法图。
- 画模型结构图、算法 pipeline、训练/推理流程、实验流程、贡献点示意图。
- 需要可编辑源文件，而不是只有截图、Mermaid 或静态 PNG。
- 需要给图中模块附证据：论文段落、公式、图号、代码路径或官方文档。

它会做：

- 先分析公开来源或用户提供材料。
- 抽取输入、输出、模块、数据流、训练目标、推理路径、指标和贡献点。
- 生成 `.drawio` 文件。
- 给出证据表和未确认推断项。

示例：

```text
使用 coff0xc-research-drawio-diagram 根据这篇论文和官方 GitHub 画一个可编辑 draw.io 方法图
帮我把这个 Transformer 论文的方法整理成 .drawio 模型结构图，要标注训练路径和推理路径
Use coff0xc-research-drawio-diagram to create an editable diagrams.net architecture figure for this algorithm pipeline.
```

## 安装

先审阅仓库内容，再把 `skills/` 下的文件夹复制到本地 Codex skills 目录。

Windows 示例：

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

复制后重启或刷新 Codex，让客户端重新索引 skill metadata。

## 怎么用

自然提问即可：

```text
帮我审计这个项目的 Web/API 安全问题
用 Agent/RAG 的方式设计一个本地知识库助手
检查这个 K8s 和 CI/CD 配置有没有供应链风险
帮我写一条检测这个日志行为的 Sigma/YARA 规则
帮我根据这篇论文画一个可编辑的 draw.io 科研算法架构图
```

如果自动触发失败，显式调用：

```text
使用 coff0xc-skill-router 帮我选择合适 skill
使用 coff0xc-software-engineering 少问确认，直接实现这个多文件开发任务
使用 coff0xc-ai-agent-rag 设计一个 RAG Agent
使用 coff0xc-secure-code-appsec 审计这个项目
使用 coff0xc-cloud-devsecops 检查 K8s 和 CI/CD
使用 coff0xc-detection-response 写检测规则
使用 coff0xc-research-drawio-diagram 根据论文和官方仓库生成 .drawio 架构图
```

更多示例见 [docs/TRIGGERING.md](docs/TRIGGERING.md) 和 [docs/USAGE.md](docs/USAGE.md)。

## 触发率评测

仓库包含一个本地 deterministic proxy eval，用来检查 skill frontmatter 对触发的覆盖情况：

```powershell
python .\scripts\run_trigger_eval.py
```

当前 eval 覆盖 17 个 skills，包括 should-trigger、should-not-trigger、router fallback、多语言调用和中文硬转述用例。详情见 [docs/TRIGGER_EVAL.md](docs/TRIGGER_EVAL.md)。

## 多语言参考

Skill 正文主要是中文 + 英文。触发策略包含常见英文工具名、缩写和中文口语表达。

多语言快速参考：

- [English / 中文 / 日本語 / 한국어 / Español / Français / Deutsch / Português / Italiano / Nederlands / Polski / Русский / العربية / Türkçe / हिन्दी / Bahasa Indonesia / Tiếng Việt / ไทย](docs/LANGUAGES.md)

这些是轻量使用说明，不是独立 skill 实现。

## 安全范围

安全相关 skills 只用于：

- 你拥有或明确授权评估的资产；
- 本地代码、配置、日志、报告、样本；
- 实验室、CTF、靶场和培训环境；
- 检测、加固、验证和报告。

不用于未授权访问、凭据窃取、持久化、规避检测、C2、钓鱼收集、数据外传或破坏性操作。

见 [SECURITY.md](SECURITY.md) 和 [docs/SANITIZATION.md](docs/SANITIZATION.md)。

## 仓库结构

```text
skills/                 # 可安装 skill 文件夹
docs/                   # 用法、触发、覆盖、来源和清理说明
evals/                  # 触发率 proxy eval 数据和结果
scripts/                # 本地验证和 eval 脚本
manifest.json           # 机器可读 skill 清单
LICENSE                 # Apache License 2.0
NOTICE                  # 归属说明
README.md               # 本文档
```

## 验证

运行：

```powershell
python .\scripts\validate_release.py
```

验证内容：

- 每个 skill 文件夹都有匹配的 `SKILL.md` frontmatter name。
- 必需发布文档存在。
- manifest 中的 skills 都存在。
- 没有本地用户路径、private key、GitHub token 或 OpenAI-style key pattern。

## 文档

- [Usage Guide](docs/USAGE.md)
- [Triggering Guide](docs/TRIGGERING.md)
- [Trigger Evaluation](docs/TRIGGER_EVAL.md)
- [Coverage Matrix](docs/COVERAGE.md)
- [Language References](docs/LANGUAGES.md)
- [Sanitization Notes](docs/SANITIZATION.md)
- [Provenance](docs/PROVENANCE.md)
- [Security Policy](SECURITY.md)

## 许可证

本仓库使用 Apache License 2.0。见 [LICENSE](LICENSE) 和 [NOTICE](NOTICE)。

---

## English

`coffee-skill` is a publish-ready Codex skill pack for software engineering, AI Agent/RAG work, API and data platforms, UI/document output, research draw.io diagrams, and defensive security workflows.

It turns a broad, fragmented skill collection into a smaller set of high-coverage skills with stronger trigger descriptions, clear safety boundaries, validation checklists, and a fallback router for cases where automatic skill triggering misses the user's intent.

Recommended GitHub About text:

```text
Comprehensive Codex skills pack for engineering, AI agents, docs, research draw.io diagrams, and defensive security, with multilingual triggers and a router fallback
```

## Why This Exists

AI coding agents often have two recurring problems:

1. Skills become too fragmented. Similar tasks may trigger the wrong skill or no skill at all.
2. Clients usually select skills from the `name` and `description` frontmatter in `SKILL.md`; capability hidden only in the body may never be loaded.

This repository addresses those problems by:

- consolidating 87 source skills into 16 comprehensive capability skills,
- adding `coff0xc-research-drawio-diagram` for research algorithm architecture diagrams and editable `.drawio` output,
- adding `coff0xc-skill-router` as a trigger-dense fallback,
- documenting Chinese, English, and multilingual usage patterns,
- keeping security topics defensive and authorization-scoped,
- including validation, provenance, triggering, and sanitization documentation.

## What Is Inside

This repository contains 17 skills:

- 16 comprehensive capability skills.
- 1 trigger fallback router: `coff0xc-skill-router`.

| Skill | Use it for | Security-scoped |
|---|---|---|
| `coff0xc-software-engineering` | Dev/autonomous development, full-stack or multi-file implementation, tests, refactors, scripts, Git | no |
| `coff0xc-ai-agent-rag` | AI agents, RAG, prompts, LLM apps, tool calling, evals, observability | no |
| `coff0xc-api-data-platform` | REST, GraphQL, OpenAPI, databases, CLI, SDK, data contracts | no |
| `coff0xc-ui-doc-output` | UI/frontend work, PDF/document output, reports, translation | no |
| `coff0xc-research-drawio-diagram` | Research algorithm architecture diagrams, paper method figures, model diagrams, experiment flows, editable draw.io/diagrams.net `.drawio` files | no |
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

- **Broad coverage without clutter**: 87 source skills plus a new research draw.io workflow are mapped into 16 capability areas.
- **Better automatic triggering**: frontmatter descriptions include Chinese, English, common domain terms, aliases, acronyms, and manual invocation phrases.
- **Router fallback**: `coff0xc-skill-router` catches broad requests and routes them to the right capability skill.
- **Practical workflows**: each capability skill includes scope, exclusions, capability matrix, staged workflow, hard gates, validation checks, and anti-patterns.
- **Editable research figures**: `coff0xc-research-drawio-diagram` generates editable `.drawio` source files instead of only Mermaid or static images.
- **Defensive security posture**: security skills focus on authorized assets, detection, hardening, verification, reporting, and safe assessment planning.
- **Publication hygiene**: this repo includes provenance, sanitization notes, validation scripts, Apache-2.0 license, and NOTICE.

## Research Draw.io Diagram Skill

Use `coff0xc-research-drawio-diagram` when you need an editable diagrams.net/draw.io architecture figure for a paper, model, algorithm, or research workflow.

Good fits:

- Turn a paper PDF, arXiv/OpenReview page, official GitHub repo, or project docs into a method figure.
- Draw model structures, algorithm pipelines, training/inference flows, experiment flows, and contribution maps.
- Deliver editable source files instead of only screenshots, Mermaid, or PNG.
- Attach evidence to diagram elements: paper sections, equations, figure numbers, code paths, or official docs.

Expected behavior:

- inspect user-provided material first,
- search public sources when needed,
- extract inputs, outputs, modules, data flow, training objectives, inference path, metrics, and contributions,
- generate a `.drawio` file,
- report evidence and uncertain inferred edges.

Examples:

```text
Use coff0xc-research-drawio-diagram to create an editable diagrams.net architecture figure for this algorithm pipeline.
Use coff0xc-research-drawio-diagram with the paper and official repo to draw a method figure with evidence notes.
使用 coff0xc-research-drawio-diagram 根据论文和官方仓库生成 .drawio 架构图。
```

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
Review this project for Web/API security issues.
Design a local knowledge-base assistant with Agent/RAG architecture.
Check this Kubernetes and CI/CD setup for supply-chain risk.
Write a Sigma/YARA detection rule for this log behavior.
Create an editable draw.io research algorithm architecture diagram from this paper.
```

If auto-triggering misses, invoke the skill explicitly:

```text
Use coff0xc-skill-router to choose the right skill.
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to check Kubernetes and CI/CD.
Use coff0xc-detection-response to write detection rules.
Use coff0xc-research-drawio-diagram to generate a .drawio architecture figure from the paper and official repo.
```

See [docs/TRIGGERING.md](docs/TRIGGERING.md) and [docs/USAGE.md](docs/USAGE.md).

## Trigger Evaluation

This repo includes a deterministic local proxy eval for skill triggering:

```powershell
python .\scripts\run_trigger_eval.py
```

The eval covers should-trigger and should-not-trigger prompts for all 17 skills, including hard paraphrases and router fallback cases. See [docs/TRIGGER_EVAL.md](docs/TRIGGER_EVAL.md).

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
evals/                  # Trigger proxy eval data and results
scripts/                # Local validation and eval helpers
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
- [Trigger Evaluation](docs/TRIGGER_EVAL.md)
- [Coverage Matrix](docs/COVERAGE.md)
- [Language References](docs/LANGUAGES.md)
- [Sanitization Notes](docs/SANITIZATION.md)
- [Provenance](docs/PROVENANCE.md)
- [Security Policy](SECURITY.md)

## License

This repository is licensed under the Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
