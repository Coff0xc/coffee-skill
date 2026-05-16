# coffee-skill

中文 | [English](#english)

`coffee-skill` 是一套可安装到 Codex / AgentSkills 兼容 AI 助手里的工作流 skill 包。它把常见任务拆成 18 个可触发的 SOP：开发、Agent/RAG、API/数据、UI、Office/PDF、科研 draw.io 图、防御安全，以及一个兜底路由 skill。

它不是脚本库，也不是独立应用。安装后，AI 在遇到真实任务时会加载更具体的工作方式：先看什么、怎么做、哪些动作要先确认、怎么验证、最后如何汇报。

## GitHub About

推荐仓库描述：

```text
Codex skill pack for real work: dev, Agent/RAG, API/data, Office docs, research diagrams, and defensive security, with bilingual triggers, routing, and validation.
```

推荐 topics：

```text
codex, skills, ai-agents, rag, office-docs, appsec, defensive-security, devsecops, prompt-engineering
```

## 你能用它做什么

| 任务 | 用哪个 skill | 结果 |
|---|---|---|
| 修 bug、写功能、跑测试、做全栈改造 | `coff0xc-software-engineering` | 代码改动、测试/构建结果、diff 摘要 |
| 设计 Agent、RAG、Prompt、工具调用和评测 | `coff0xc-ai-agent-rag` | 架构、工具 schema、检索/引用/评测方案 |
| 设计 API、数据库、OpenAPI、CLI/SDK | `coff0xc-api-data-platform` | 接口契约、schema、错误码、迁移和数据质量方案 |
| 优化 UI、dashboard、报告表达和翻译 | `coff0xc-ui-doc-output` | 页面/组件建议、截图验证、报告结构和交付文案 |
| 做 PPTX、DOCX、PDF、Excel/CSV 文件 | `coff0xc-office-doc-tools` | 可编辑文件、渲染/预览 QA、公式和格式检查 |
| 根据论文/代码画可编辑 draw.io 图 | `coff0xc-research-drawio-diagram` | `.drawio` 文件、图结构、证据表 |
| 做授权范围内的代码/云/检测/身份/合约/协议安全工作 | 对应安全 skill | 证据化发现、风险说明、修复/检测/加固建议 |
| 不确定该用哪个 | `coff0xc-skill-router` | 推荐 skill、理由、边界和下一步 |

完整 skill 清单见 [Coverage Matrix](docs/COVERAGE.md)。

## 快速安装

Windows / Codex Desktop：

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

安装后重启或刷新 Codex，让客户端重新索引 skill metadata。

确认安装是否生效：

```text
使用 coff0xc-skill-router 帮我判断这个任务该用哪个 skill。
```

## 推荐用法

你可以自然描述任务：

```text
这个 Python 项目的 pytest 挂了，帮我定位失败用例，做最小修复，然后跑测试和 lint。
用 Agent/RAG 的方式设计一个本地知识库助手，需要引用来源、缓存、失败降级和评测集。
检查这个 Docker、K8s 和 GitHub Actions 配置有没有供应链、SBOM、secret scanning 和 IaC 风险。
把这份 Markdown 大纲做成可编辑 PPTX，包含图表、讲述逻辑、预览验证和最终文件路径。
根据这篇论文和官方 GitHub 画一个可编辑的 draw.io 科研算法架构图。
```

也可以直接点名 skill：

```text
使用 coff0xc-software-engineering 少问确认，直接实现这个多文件开发任务。
使用 coff0xc-ai-agent-rag 设计一个带引用、缓存和失败降级的企业知识库助手。
使用 coff0xc-api-data-platform 设计这个 billing REST API，包含 OpenAPI、分页和错误码。
使用 coff0xc-office-doc-tools 生成一份高审美可编辑 PPTX，并检查预览、图表和导出文件。
使用 coff0xc-secure-code-appsec 审计这个 Web/API 项目的认证和越权风险。
```

简单规则：知道要用哪个就直接点名；不知道就先用 `coff0xc-skill-router`。

## Office 文件质量门禁

`coff0xc-office-doc-tools` 是这次重点增强的文件交付 skill。它不只要求“生成文件”，还要求交付物能被打开、编辑、审阅、验证和继续使用。

| 文件类型 | 质量门禁 |
|---|---|
| PPTX | 先写 claim spine；锁定 design system；规划 contact sheet；避免模板感、重复卡片和空洞标题；用 comeback scorecard 检查 story、rhythm、whitespace、typography、chart clarity；渲染预览后再交付。 |
| Excel / CSV / XLSX | 先 inspect workbook / data shape；识别编码、分隔符、表头、单位、日期、空值和异常值；保留 raw/source/assumptions；派生值用公式；trace 关键输出；扫描公式错误；检查图表和 dashboard 渲染。 |
| DOCX / Word | 先理解标题层级、表格、批注、修订、页眉页脚和字段；使用真实 styles、numbering、table geometry；避免假标题/假列表/表格包装长段落；尽量逐页渲染检查格式，不能只靠文本抽取判断版式。 |

## 安全边界

安全相关 skills 只用于授权、防御、检测、加固、验证和报告。它们适合本地代码、配置、日志、样本、报告、实验室、CTF、靶场和已授权资产。

不用于未授权访问、凭据窃取、持久化、规避检测、C2、钓鱼收集、数据外传或破坏性操作。生产、凭据、付费、远程写入、删除、push、PR、云资源和 CI/CD 权限变更都需要明确授权。

见 [SECURITY.md](SECURITY.md) 和 [docs/SANITIZATION.md](docs/SANITIZATION.md)。

## 验证

发布前检查：

```powershell
python .\scripts\validate_release.py
```

触发评测：

```powershell
python .\scripts\run_trigger_eval.py
```

当前评测覆盖 113 个本地 proxy cases，用来检查应该触发的 prompt 是否命中目标 skill，以及简单问题是否误触发。它不能完全复刻所有客户端的私有触发逻辑，但能抓出明显漏词、误触发和路由退化。

## 仓库结构

```text
skills/                 # 可安装的 skill 文件夹，每个目录至少有 SKILL.md
docs/                   # 使用、触发、覆盖、来源、清理和多语言说明
evals/                  # 本地触发评测数据和生成结果
scripts/                # 发布校验和触发评测脚本
manifest.json           # 机器可读 skill 清单
LICENSE                 # Apache License 2.0
NOTICE                  # 归属说明
```

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

Apache License 2.0。见 [LICENSE](LICENSE) 和 [NOTICE](NOTICE)。

---

## English

`coffee-skill` is an installable skill pack for Codex and AgentSkills-compatible AI assistants. It turns common work into 18 triggerable operating procedures: software engineering, Agent/RAG, API/data, UI, Office/PDF artifacts, research draw.io diagrams, defensive security, and a router fallback.

It is not a script library or standalone app. After installation, the assistant can load a task-specific workflow that tells it what to inspect, what to do, what to avoid, what requires confirmation, how to verify, and how to report the result.

## GitHub About

Recommended repository description:

```text
Codex skill pack for real work: dev, Agent/RAG, API/data, Office docs, research diagrams, and defensive security, with bilingual triggers, routing, and validation.
```

Recommended topics:

```text
codex, skills, ai-agents, rag, office-docs, appsec, defensive-security, devsecops, prompt-engineering
```

## What It Covers

| Task | Skill | Output |
|---|---|---|
| Bugs, features, tests, refactors, full-stack work | `coff0xc-software-engineering` | Code changes, validation results, diff summary |
| Agents, RAG, prompts, tool use, evaluation | `coff0xc-ai-agent-rag` | Architecture, tool schemas, retrieval/citation/eval plan |
| APIs, databases, OpenAPI, CLI/SDK | `coff0xc-api-data-platform` | Contracts, schema, errors, migration and data quality plan |
| UI, dashboards, reports, translation | `coff0xc-ui-doc-output` | UX/page guidance, screenshot checks, delivery copy |
| PPTX, DOCX, PDF, Excel/CSV artifacts | `coff0xc-office-doc-tools` | Editable files, render/preview QA, formula and format checks |
| Research diagrams from papers/code | `coff0xc-research-drawio-diagram` | Editable `.drawio`, graph spec, evidence table |
| Authorized defensive security work | Security skills | Evidence-backed findings, fixes, detections, hardening advice |
| Unsure which one to use | `coff0xc-skill-router` | Recommended skill, rationale, boundaries, next step |

See [Coverage Matrix](docs/COVERAGE.md) for the full list.

## Install

Windows / Codex Desktop:

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

Restart or refresh Codex so it re-indexes skill metadata.

Smoke check:

```text
Use coff0xc-skill-router to choose the right skill for this task.
```

## Usage

Natural prompts work:

```text
Fix this Python project's failing pytest cases, make the smallest correct change, then run tests and lint.
Design a local knowledge-base assistant with Agent/RAG architecture, citations, cache, fallback, and evals.
Check this Docker, Kubernetes, and GitHub Actions setup for supply-chain and secret risks.
Create an editable PPTX from this Markdown outline and verify the preview.
Create an editable draw.io research architecture diagram from this paper and official repo.
```

Explicit invocation is more reliable:

```text
Use coff0xc-software-engineering to build this feature end to end with tests.
Use coff0xc-ai-agent-rag to design a RAG assistant with citations and fallback behavior.
Use coff0xc-api-data-platform to design this REST API and database schema.
Use coff0xc-office-doc-tools to create a polished editable PPTX and verify the preview.
Use coff0xc-secure-code-appsec to review this authorized API for authz risks.
```

If you know the skill, name it. If you do not, start with `coff0xc-skill-router`.

## Office Artifact Quality Gates

`coff0xc-office-doc-tools` is the file-delivery skill. It does not stop at “a file exists”; the file should be openable, editable, reviewable, verifiable, and reusable.

| Artifact | Gate |
|---|---|
| PPTX | Claim spine, design system, contact-sheet plan, anti-template checks, comeback scorecard, and rendered preview review. |
| Excel / CSV / XLSX | Workbook/data inspect, encoding and delimiter checks, raw/source/assumptions preservation, formula-driven derived values, traced key outputs, formula error scan, chart/dashboard render checks. |
| DOCX / Word | Structural reading of headings, tables, comments, tracked changes, headers/footers, real styles/numbering/table geometry, and page-rendered layout checks instead of text extraction only. |

## Safety Scope

Security-related skills are defensive and authorization-scoped. They are intended for owned or explicitly authorized assets, local code/config review, logs, reports, lab environments, CTFs, training ranges, detection, hardening, verification, and reporting.

They do not include guidance for unauthorized access, credential theft, persistence, detection evasion, C2 operation, phishing collection, data exfiltration, or destructive actions. Production, credentials, paid services, remote writes, deletion, push, PR actions, cloud resources, and CI/CD permission changes require explicit authorization.

## Validation

```powershell
python .\scripts\validate_release.py
python .\scripts\run_trigger_eval.py
```

The trigger evaluation currently covers 113 local proxy cases. It is a release guard for routing and false positives; it does not claim to reproduce every client runtime's private selection logic.

## Repository Layout

```text
skills/                 # Installable skill folders
docs/                   # Usage, triggering, coverage, provenance, i18n, sanitization
evals/                  # Trigger eval cases and generated reports
scripts/                # Release validation and trigger scoring
manifest.json           # Machine-readable skill inventory
LICENSE                 # Apache License 2.0
NOTICE                  # Attribution notice
```

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

Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
