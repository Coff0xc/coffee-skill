# coffee-skill

中文 | [English](#english)

把 Codex / AgentSkills 兼容 AI 助手从“临场发挥”变成可复用工作流。

`coffee-skill` 是一套可安装的 `SKILL.md` 工作流包。它不提供可执行程序，而是告诉 AI 在真实任务里该什么时候触发、先查什么、怎么动手、哪些动作必须确认、怎么验证，以及最后怎么交付。

`18 skills` · `中英触发` · `router 兜底` · `113 个触发评测用例` · `Apache-2.0`

## 先看这个

| 你想让 AI 做什么 | 直接怎么说 | 你应该拿到什么 |
|---|---|---|
| 不知道该用哪个工作流 | `使用 coff0xc-skill-router 判断该用哪个 skill` | 推荐 skill、理由、边界、下一步 |
| 修项目、写功能、跑测试 | `使用 coff0xc-software-engineering 修复这个 repo` | 代码补丁、验证结果、剩余风险 |
| 设计 Agent / RAG / Prompt | `使用 coff0xc-ai-agent-rag 设计这个知识库助手` | 架构、工具、检索、引用、评测、降级方案 |
| 做 API / 数据库 / SDK | `使用 coff0xc-api-data-platform 设计这个接口` | OpenAPI/schema、错误码、分页、迁移和数据质量方案 |
| 做正式 PPT / Excel / DOCX / PDF | `使用 coff0xc-office-doc-tools 生成可交付文件` | 可编辑文件、预览/渲染 QA、公式和格式检查 |
| 做论文/算法架构图 | `使用 coff0xc-research-drawio-diagram 画 draw.io 图` | 可编辑 `.drawio`、图结构、证据表 |
| 做授权安全分析 | `使用对应 coff0xc-* security skill` | 证据化发现、风险说明、修复/检测/加固建议 |

如果只记一句：知道 skill 名就直接点名，不知道就先用 `coff0xc-skill-router`。

## 30 秒安装

在仓库根目录执行：

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

然后重启或刷新 Codex，让客户端重新索引 skill metadata。

快速验证：

```text
使用 coff0xc-skill-router 帮我判断这个任务该用哪个 skill。
```

## 怎么提问更稳

最稳的格式是：

```text
使用 <skill-name>：
目标：...
输入：...
交付：...
验证：...
限制：...
```

示例：

```text
使用 coff0xc-software-engineering：
目标：定位并修复 pytest 失败。
输入：当前 repo。
交付：最小代码补丁、失败原因、验证命令输出摘要。
验证：pytest 和 lint 能跑就跑，不能跑说明原因。
限制：不要做无关重构。
```

自然描述也可以：

```text
这个 Python 项目的 pytest 挂了，帮我定位失败用例，做最小修复，然后跑测试和 lint。
把这份 Markdown 大纲做成可编辑 PPTX，包含图表、讲述逻辑、预览验证和最终文件路径。
用 Agent/RAG 的方式设计一个本地知识库助手，需要引用来源、缓存、失败降级和评测集。
根据这篇论文和官方 GitHub 画一个可编辑的 draw.io 科研算法架构图。
```

## 能力地图

| 领域 | 推荐 skill | 适合任务 | 交付结果 |
|---|---|---|---|
| 软件工程 | `coff0xc-software-engineering` | bugfix、feature、refactor、full-stack、repo repair | diff、测试/构建结果、风险说明 |
| AI 系统 | `coff0xc-ai-agent-rag` | Agent、RAG、Prompt、工具调用、评测、观测、成本 | 架构、流程、工具 schema、评测闭环 |
| API / 数据 | `coff0xc-api-data-platform` | REST、GraphQL、OpenAPI、SQL、迁移、CLI/SDK | 契约、schema、错误模型、数据质量检查 |
| UI / 输出 | `coff0xc-ui-doc-output` | 前端、dashboard、报告表达、技术翻译 | UI/文案改进、截图验证、报告结构 |
| Office 文件 | `coff0xc-office-doc-tools` | PPTX、DOCX、PDF、XLSX、CSV、图表、批注、修订 | 可编辑文件、渲染 QA、公式/格式检查 |
| 科研图 | `coff0xc-research-drawio-diagram` | 论文方法图、模型结构图、算法 pipeline | `.drawio` 源文件、节点/边说明、证据表 |
| 授权安全 | 安全类 `coff0xc-*` skills | AppSec、云安全、检测响应、身份、合约、协议、漏洞生命周期 | 证据、影响、修复、检测、加固建议 |
| 路由兜底 | `coff0xc-skill-router` | 不确定该用哪个 skill，或任务跨多个领域 | 推荐 skill、选择理由、边界和下一步 |

完整清单见 [docs/COVERAGE.md](docs/COVERAGE.md)。

## Office 质量门禁

`coff0xc-office-doc-tools` 的定位不是“生成一个文件就算完成”，而是让文件能打开、能编辑、能审阅、能验证、能继续交付。

| 文件 | 必须过的门禁 | 失败表现 |
|---|---|---|
| PPTX | 每页先有结论型标题和证明对象；先锁定设计系统；规划 contact sheet；避免模板感和连续重复版式；用 comeback scorecard 检查叙事、节奏、留白、字体、图表清晰度；渲染预览后再交付。 | 只有漂亮背景、卡片堆叠、标题空泛、图表不能证明观点、没有预览检查。 |
| Excel / CSV / XLSX | 先检查编码、分隔符、表头、单位、日期、空值、异常值和已有公式/图表；保留 raw/source/assumptions；关键派生值用公式；trace 关键输出；扫描公式错误；检查图表和 dashboard 渲染。 | 手写 split、硬编码计算结果、覆盖原始数据、图表无来源、公式错误未扫。 |
| DOCX / Word | 先读标题层级、表格、批注、修订、页眉页脚、字段和元数据；用真实 styles、numbering、table geometry；表格只放真正行列数据；尽量逐页渲染检查版式。 | 只抽文本就说读懂、假标题/假列表、表格包长段落、批注/修订锚点没检查。 |

这三类门禁来自对官方 Office 类 skills 的重点对照：PPT 看审美和叙事，Excel 看数据解析和可审计计算，DOCX 看阅读理解、结构保真和版式验证。

## 安全边界

安全相关 skills 只用于授权、防御、检测、加固、验证和报告。

适用范围：本地代码、配置、日志、样本、报告、实验室、CTF、靶场、已授权资产。

不提供：未授权访问、凭据窃取、持久化、规避检测、C2、钓鱼收集、数据外传、破坏性操作。

生产环境、凭据、付费资源、远程写入、删除、push、PR、云资源和 CI/CD 权限变更，需要用户明确授权。

## 本地验证

发布结构校验：

```powershell
python .\scripts\validate_release.py
```

触发评测：

```powershell
python .\scripts\run_trigger_eval.py
```

当前触发评测包含 113 个本地 proxy cases，用来检查应该触发的 prompt 是否命中目标 skill，以及简单问题是否误触发。它是发布护栏，不等同于所有客户端的私有路由逻辑。

## 仓库结构

```text
skills/                 # 可安装的 skill 文件夹
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

Turn Codex / AgentSkills-compatible AI assistants from ad hoc execution into reusable workflows.

`coffee-skill` is an installable pack of `SKILL.md` workflows. It is not a standalone app. Each skill tells the assistant when to trigger, what to inspect first, how to proceed, what needs confirmation, how to verify, and how to report the result.

`18 skills` · `Chinese/English triggers` · `router fallback` · `113 trigger eval cases` · `Apache-2.0`

## Quick Start

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

## How To Prompt

Most reliable format:

```text
Use <skill-name>:
Goal: ...
Input: ...
Deliverable: ...
Validation: ...
Limits: ...
```

If you know the skill, name it directly. If you do not, start with `coff0xc-skill-router`.

## Capability Map

| Domain | Skill | Best for | Output |
|---|---|---|---|
| Software engineering | `coff0xc-software-engineering` | bugfixes, features, refactors, full-stack work, repo repair | diff, test/build results, risk notes |
| AI systems | `coff0xc-ai-agent-rag` | Agent, RAG, prompts, tools, evals, observability, cost | architecture, flow, tool schemas, eval loop |
| API / data | `coff0xc-api-data-platform` | REST, GraphQL, OpenAPI, SQL, migrations, CLI/SDK | contracts, schemas, errors, data checks |
| UI / output | `coff0xc-ui-doc-output` | frontend, dashboards, reports, translation | UX/content improvements, screenshot checks, report structure |
| Office artifacts | `coff0xc-office-doc-tools` | PPTX, DOCX, PDF, XLSX, CSV, charts, comments, redlines | editable files, render QA, formula/format checks |
| Research diagrams | `coff0xc-research-drawio-diagram` | paper method figures, model diagrams, algorithm pipelines | editable `.drawio`, node/edge spec, evidence table |
| Authorized security | security `coff0xc-*` skills | AppSec, cloud, detection, identity, contracts, protocols, vulnerability lifecycle | evidence, impact, fixes, detections, hardening |
| Routing fallback | `coff0xc-skill-router` | uncertain or cross-domain tasks | recommended skill, rationale, boundaries, next step |

See [docs/COVERAGE.md](docs/COVERAGE.md) for the full list.

## Office Quality Gates

`coff0xc-office-doc-tools` is built for formal file delivery, not just file generation.

| Artifact | Required gate |
|---|---|
| PPTX | Claim spine, design system, contact-sheet plan, anti-template checks, comeback scorecard, and rendered preview review. |
| Excel / CSV / XLSX | Workbook/data inspect, encoding and delimiter checks, raw/source/assumptions preservation, formula-driven derived values, traced key outputs, formula error scan, chart/dashboard render checks. |
| DOCX / Word | Structural reading of headings, tables, comments, tracked changes, headers/footers, real styles/numbering/table geometry, and page-rendered layout checks instead of text extraction only. |

## Safety Scope

Security-related skills are defensive and authorization-scoped. They are for owned or explicitly authorized assets, local code/config review, logs, reports, labs, CTFs, training ranges, detection, hardening, verification, and reporting.

They do not provide guidance for unauthorized access, credential theft, persistence, detection evasion, C2, phishing collection, data exfiltration, or destructive actions. Production, credentials, paid services, remote writes, deletion, push, PR actions, cloud resources, and CI/CD permission changes require explicit authorization.

## Validation

```powershell
python .\scripts\validate_release.py
python .\scripts\run_trigger_eval.py
```

The trigger evaluation currently covers 113 local proxy cases. It is a release guard for routing and false positives, not a clone of every client runtime's private selection logic.

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
