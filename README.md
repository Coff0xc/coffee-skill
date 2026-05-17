# coffee-skill

中文 | [English](#english)

把 Codex / AgentSkills 兼容 AI 助手从“临场发挥”变成可复用、可验证、可恢复的工作流，同时保留普通任务的快路径。

`coffee-skill` 不是脚本工具，也不是触发词合集。它是一套可安装的 `SKILL.md` 工作流包：普通任务直接进入最相关 skill 干活，跨领域任务才让 router 选择主 skill、补必要辅助 skill、按阶段执行和验证。

本仓库是开源项目，采用 `AGPL-3.0-only`。别人可以 fork、修改、分发、商用，但必须保留许可证、版权和来源说明；发布衍生版本或把修改版作为网络服务提供时，也必须按 AGPL 提供对应源码。`Coff0xc` / `coffee-skill` 名称和项目身份不随许可证授权，不能冒充原创、官方、独家或授权版本。

`18 skills` · `中英触发` · `自治编排 router` · `131 个触发/组合评测用例` · `7 个真实产物质量评测夹具` · `CI 自动验证` · `AGPL-3.0-only`

## 两种模式

| 模式 | 什么时候用 | AI 应该怎么做 |
|---|---|---|
| 默认执行模式 | 日常修 bug、写功能、改 UI、做 PPT/Excel/DOCX、审计代码、整理报告 | 直接选最具体的 skill，读最小必要上下文，动手修改或分析，跑可用验证，简短汇报。 |
| Release / Eval 模式 | 你明确说 review、eval、质量测试、发版、推送、CI、benchmark、确认 skill 是否好用 | 跑 trigger eval、quality eval、golden fixtures、workflow trace、docs/manifest 同步和发布门禁。 |

一句话：平时不要让 skill 先证明自己，先让它把任务做完；只有要发版或验证 skill 质量时才跑重型门禁。

## 为什么之前会变慢，现在怎么避免

Skill 变慢通常不是能力太强，而是普通任务也加载了发版门禁、长路由表和审美长清单。这个仓库现在按“快路径 + 按需 reference”组织：

- 每个 skill 顶部都有 `快速规则（日常任务先读这里）`：先给 3-4 条硬门禁和当前任务的默认执行方式。
- 普通任务只读主 `SKILL.md` 顶部：目标、边界、短工作流、核心门禁。
- 深度 UI/外部 skill 合并/路由调试/quality eval 才读取 `references/`。
- `coff0xc-skill-router` 只在跨领域或不确定任务介入；单域 UI、dev、Office、安全任务直接进专业 skill。
- `trigger eval`、`quality eval`、`workflow trace`、golden responses 是 release guard，不是日常任务前置步骤。

## 和其他 skill 仓库的区别

| 维度 | 常见 skill 仓库 | coffee-skill |
|---|---|---|
| 目标 | 提供单个场景提示词或工具说明 | 覆盖工程、AI/RAG、API/数据、UI、Office、科研图、安全审计等真实工作流 |
| 编排方式 | 通常让用户自己选一个 skill | 窄任务直达具体 skill；跨域任务才由 router 选主 skill、加辅助 skill、排阶段、执行中重路由 |
| 触发方式 | 主要靠关键词堆叠 | 每个 skill 有定位、边界、交付物、输入类型、验证方式和自治编排入口 |
| 质量证明 | 通常只能证明“写了 skill” | 有 trigger eval、quality eval、golden responses 和 CI 门禁，但这些只作为 release guard |
| 产物要求 | 多数停留在文本建议 | 要求代码 diff、截图、PPTX/DOCX/XLSX、draw.io、报告、验证结果等可交付物 |
| Office 能力 | 常见是“生成文件/转换格式” | 会真实检查 PPTX OOXML、Excel 公式/表/图表、DOCX comments/redlines/styles/rels |
| 开发能力 | 常见是语言提示或泛化步骤 | 强制读仓库规则、定位根因、最小修复、跑验证、不乱改 lockfile |
| 安全边界 | 容易混合攻防动作 | 授权/防御优先，生产、凭据、删除、push、PR、云资源等高风险动作必须确认 |
| 可维护性 | 依赖人工记忆 | manifest、docs、evals、golden fixtures、CI 一起约束漂移 |

一句话：很多 skill 仓库解决“AI 知不知道该怎么说”，`coffee-skill` 更关注“AI 能不能用合适的能力把真实工作做完，并留下必要证据”。

## 自治编排：AI 自己串 skill

你不需要预先知道该用哪个 skill。简单任务直接描述目标即可；复杂跨域任务可以让 router 先给轻量任务图，然后立即执行第一阶段：

```text
你自己判断要用哪些 coff0xc skills，并把它们串成工作流完成这个功能。
这个 vibe coding 任务可能涉及前后端、数据库、安全和文档，你来编排 skill。
```

router 的职责不是永远停在“推荐一个 skill”，也不是每次都输出长计划。它只在跨域时给最小可执行编排：

```text
主 skill: coff0xc-software-engineering
辅助 skills:
- coff0xc-api-data-platform: 定 API/schema/数据契约
- coff0xc-ui-doc-output: 做 UI 状态和截图验收
- coff0xc-secure-code-appsec: 做认证/输入/权限回归
阶段: 仓库规则 -> 数据契约 -> 实现 -> UI 验收 -> 安全审计 -> 测试/build
```

如果执行中发现新证据，工作流可以调整。例如：普通 dev 任务发现需要正式 PPTX 交付，就新增 `coff0xc-office-doc-tools`；Agent 应用发现缺数据契约，就新增 `coff0xc-api-data-platform`。

## 先看这个

| 你想让 AI 做什么 | 直接怎么说 | 你应该拿到什么 |
|---|---|---|
| 日常修项目/写功能 | `这个 repo 测试挂了，帮我最小修复并验证` | 直接进入 dev skill，代码补丁、验证结果、剩余风险 |
| 不知道该用哪个工作流 | `使用 coff0xc-skill-router 判断该用哪个 skill` | 推荐主 skill、必要辅助 skill、下一步 |
| 任务跨多个领域 | `你自己判断要用哪些 coff0xc skills，并串成工作流完成` | 轻量主/辅 skill graph、阶段顺序、验证门禁、重路由条件 |
| 修项目、写功能、跑测试 | `使用 coff0xc-software-engineering 修复这个 repo` | 代码补丁、验证结果、剩余风险 |
| 设计 Agent / RAG / Prompt | `使用 coff0xc-ai-agent-rag 设计这个知识库助手` | 架构、工具、检索、引用、评测、降级方案 |
| 做 API / 数据库 / SDK | `使用 coff0xc-api-data-platform 设计这个接口` | OpenAPI/schema、错误码、分页、迁移和数据质量方案 |
| 做 UI / dashboard / 前端体验 | `使用 coff0xc-ui-doc-output 优化这个 dashboard` | UI 改动、状态覆盖、响应式/可访问性、截图验证 |
| 做正式 PPT / Excel / DOCX / PDF | `使用 coff0xc-office-doc-tools 生成可交付文件` | 可编辑文件、预览/渲染 QA、公式和格式检查 |
| 做论文/算法架构图 | `使用 coff0xc-research-drawio-diagram 画 draw.io 图` | 可编辑 `.drawio`、图结构、证据表 |
| 做授权安全分析 | `使用对应 coff0xc-* security skill` | 证据化发现、风险说明、修复/检测/加固建议 |

知道 skill 名就直接点名；不知道或任务明显跨领域，就用 `coff0xc-skill-router` 轻量编排。普通单域任务不要先绕 router。

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

最稳的格式：

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
| 自治编排 | `coff0xc-skill-router` | 不确定该用哪个 skill，或任务跨多个领域 | 主/辅 skill graph、阶段顺序、门禁、重路由条件 |

完整清单见 [docs/COVERAGE.md](docs/COVERAGE.md)。

## 质量门禁

### Office

`coff0xc-office-doc-tools` 的定位不是“生成一个文件就算完成”，而是让文件能打开、能编辑、能审阅、能验证、能继续交付。

| 文件 | 必须过的门禁 | 失败表现 |
|---|---|---|
| PPTX | 每页先有结论型标题和证明对象；先锁定设计系统；规划 contact sheet；避免模板感和连续重复版式；用 comeback scorecard 检查叙事、节奏、留白、字体、图表清晰度；渲染预览后再交付。 | 只有漂亮背景、卡片堆叠、标题空泛、图表不能证明观点、没有预览检查。 |
| Excel / CSV / XLSX | 先检查编码、分隔符、表头、单位、日期、空值、异常值和已有公式/图表；保留 raw/source/assumptions；关键派生值用公式；trace 关键输出；扫描公式错误；检查图表和 dashboard 渲染。 | 手写 split、硬编码计算结果、覆盖原始数据、图表无来源、公式错误未扫。 |
| DOCX / Word | 先读标题层级、表格、批注、修订、页眉页脚、字段和元数据；用真实 styles、numbering、table geometry；表格只放真正行列数据；尽量逐页渲染检查版式。 | 只抽文本就说读懂、假标题/假列表、表格包长段落、批注/修订锚点没检查。 |

### UI / Dev

- UI 不只看“页面能打开”，还要求产品类型路由、设计系统、状态覆盖、响应式、可访问性和截图证据。
- Dev 不只看“代码改了”，还要求读仓库规则、复现失败、定位根因、最小修复、跑可用验证、避免 lockfile 噪声。

## 本地验证

这些命令是维护本仓库、发版、推送或确认 skill 质量时用的 release guard；不是普通用户任务的默认前置步骤。

```powershell
python .\scripts\validate_release.py
python .\scripts\run_trigger_eval.py
python .\scripts\run_quality_eval.py
```

当前 trigger eval 覆盖 131 个本地 proxy cases，用来检查应该触发的 prompt 是否命中目标 skill、短 Office 交付句是否触发、博士级/顶级工程/授权红队/UI/多域危机场景是否包含预期 skill set，以及简单问题是否误触发。

quality eval 默认评分 `evals/quality/golden-responses/` 里的真实产物夹具：

- Workflow：检查 `workflow-trace.json` 的阶段、skills、输入、产物、门禁、重路由和最终验证。
- UI：HTML 静态质量、状态覆盖、反模板文本、桌面/移动 PNG、render audit、HTML hash、console cleanliness、overlap/clipping 和审美评分证据。
- Dev：执行 Python 和 Node 行为断言，同时检查 requirements/package lockfile 不被噪声改动。
- PPTX：解包 `.pptx`，检查 slide XML、可编辑 text shapes、chart parts、source notes、layout diversity 和 PNG render evidence。
- XLSX：解包 `.xlsx`，检查 workbook/sheets/tables/chart parts、bounded formulas、错误值、关键公式重算和 PNG render evidence。
- DOCX：解包 `.docx`，检查 comments、anchors、tracked changes、styles、numbering、table geometry、rels、headers/footers、fields 和页面 PNG evidence。

CI 会在 push / pull request 上自动运行 release validation、trigger eval、quality eval 和 whitespace check。普通任务只需要按对应 skill 跑当前项目自己的验证。

## 安全边界

安全相关 skills 只用于授权、防御、检测、加固、验证和报告。

适用范围：本地代码、配置、日志、样本、报告、实验室、CTF、靶场、已授权资产。

不提供：未授权访问、凭据窃取、持久化、规避检测、C2、钓鱼收集、数据外传、破坏性操作。

生产环境、凭据、付费资源、远程写入、删除、push、PR、云资源和 CI/CD 权限变更，需要用户明确授权。

## 仓库结构

```text
skills/                 # 可安装的 skill 文件夹
docs/                   # 使用、触发、覆盖、来源、清理和多语言说明
evals/                  # trigger eval、quality eval、golden responses
scripts/                # 发布校验、触发评测、质量评测脚本
.github/workflows/      # CI 验证流程
manifest.json           # 机器可读 skill 清单
LICENSE                 # GNU Affero General Public License v3.0
NOTICE                  # 归属说明
```

## 文档

- [Usage Guide](docs/USAGE.md)
- [Triggering Guide](docs/TRIGGERING.md)
- [Trigger Evaluation](docs/TRIGGER_EVAL.md)
- [Quality Evaluation](docs/QUALITY_EVAL.md)
- [Coverage Matrix](docs/COVERAGE.md)
- [Language References](docs/LANGUAGES.md)
- [Sanitization Notes](docs/SANITIZATION.md)
- [Provenance](docs/PROVENANCE.md)
- [Enforcement Guide](docs/ENFORCEMENT.md)
- [Takedown Template](docs/TAKEDOWN_TEMPLATE.md)
- [Trademark Policy](TRADEMARK.md)
- [Security Policy](SECURITY.md)

## 许可证

从当前版本起使用 GNU Affero General Public License v3.0 only，即 `AGPL-3.0-only`。见 [LICENSE](LICENSE) 和 [NOTICE](NOTICE)。

这意味着：这是 OSI 意义上的开源路线，不能靠许可证禁止商业使用；但任何复制、修改、分发、再打包、课程/agent 包分发或网络服务托管，都必须遵守 AGPL 的源码、同许可证、版权和通知义务。

严正声明：开源不等于允许偷署名、闭源套壳、删许可证、删 `NOTICE`、去除源码标识、冒充原创、冒充 Coff0xc 官方或暗示独家授权。Coff0xc 会使用 Git 历史、源码标识、相似度对比、购买记录、平台页面和交付包作为下架投诉、许可证执行、商标/冒充投诉和法律主张的证据。

本仓库的 `SKILL.md` 文件包含源码级标识。它是版权和来源取证元数据，不影响 skill 执行。扫描可疑复制品：

```powershell
python .\scripts\scan_provenance.py <suspected-folder>
```

注意：许可证变更不追溯。变更前已经发布的版本仍按当时适用的许可证授权。

---

## English

Turn Codex / AgentSkills-compatible AI assistants from ad hoc execution into reusable, verifiable, recoverable workflows while preserving a fast path for normal work.

`coffee-skill` is not a script package or a keyword list. It is an installable pack of `SKILL.md` workflows: narrow tasks go straight to the most specific skill, while cross-domain tasks use the router to choose a primary skill, add necessary support skills, execute phases, verify, and re-route.

This repository is open source under `AGPL-3.0-only`. Others may fork, modify, distribute, and use it commercially, but they must preserve the license, copyright, and origin notices. If they distribute a derivative or run a modified version as a network service, they must provide the corresponding source under the AGPL. The `Coff0xc` / `coffee-skill` names and project identity are not licensed for false originality, official endorsement, exclusivity, or impersonation.

`18 skills` · `Chinese/English triggers` · `autonomous router` · `131 trigger/composition eval cases` · `7 real-artifact quality eval fixtures` · `CI validation` · `AGPL-3.0-only`

## Two Modes

| Mode | Use when | Assistant behavior |
|---|---|---|
| Execution mode | Everyday bug fixes, features, UI edits, Office artifacts, code review, reports | Pick the most specific skill, read minimal context, execute, run relevant validation, report briefly. |
| Release / eval mode | Explicit review, eval, quality test, release, push, CI, benchmark, or skill-quality request | Run trigger evals, quality evals, golden fixtures, workflow traces, docs/manifest sync, and release gates. |

Normal work should not start by proving the skill system. It should start by doing the task.

## Why Skills Felt Slow

The slow path came from loading release gates, long route tables, and detailed design checklists during ordinary work. The pack now uses a fast-path plus on-demand references:

- Every skill starts with `快速规则（日常任务先读这里）`: 3-4 hard gates and the default way to proceed.
- Normal tasks load only the top of the main `SKILL.md`: goal, boundary, short workflow, and core gates.
- Deep UI review, external skill merging, router debugging, and quality evals load `references/` only when needed.
- `coff0xc-skill-router` is only for uncertain or cross-domain work; narrow UI, dev, Office, or security tasks go directly to the specific skill.
- Trigger evals, quality evals, workflow traces, and golden responses are release guards, not runtime ceremony.

## How This Differs

| Dimension | Typical skill repos | coffee-skill |
|---|---|---|
| Goal | Single-purpose prompts or tool notes | End-to-end workflows across engineering, AI/RAG, API/data, UI, Office, research diagrams, and authorized security |
| Orchestration | Users usually pick one skill manually | Narrow tasks go directly to one skill; cross-domain tasks use the router for primary/support skill selection, phases, gates, and re-routing |
| Routing | Mostly keyword matching | Positioning, inputs, deliverables, boundaries, verification, and an autonomous composition entry point |
| Proof | Usually proves the skill file exists | Trigger evals, quality evals, golden responses, and CI gates, used as release guards |
| Output | Often text advice | Diffs, screenshots, PPTX/DOCX/XLSX, draw.io files, reports, and verification evidence |
| Office | Often file generation or conversion | OOXML checks for PPTX slides/charts/text, XLSX formulas/tables/charts, DOCX comments/redlines/styles/rels |
| Development | Generic coding guidance | Repo rules, root-cause repair, minimal diffs, validation, and lockfile discipline |
| Safety | Mixed or implicit boundaries | Authorization-first security boundaries and confirmation gates for high-risk actions |
| Maintenance | Manual review | Manifest, docs, evals, golden fixtures, and CI keep behavior from drifting |

In short: many skill repos help an assistant know what to say. `coffee-skill` focuses on whether the assistant can organize capabilities, finish real work, and leave evidence.

## Autonomous Composition

For broad work, do not pre-select every skill. Ask the router for a lightweight workflow and then execute the first phase:

```text
Decide which coff0xc skills are needed, chain them into a workflow, and complete this task.
This vibe-coding task may include frontend, backend, data, security, and docs; orchestrate the skills yourself.
```

The router should produce a primary skill, only necessary supporting skills, phase order, gates, and re-routing conditions. For example, a SaaS feature may compose `software-engineering + api-data-platform + ui-doc-output + secure-code-appsec`.

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

If you know the skill, name it directly. If the task is clearly narrow, do not route first. If it is uncertain or cross-domain, start with `coff0xc-skill-router`.

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
| Autonomous composition | `coff0xc-skill-router` | uncertain or cross-domain tasks | primary/supporting skill graph, phase order, gates, re-routing conditions |

See [docs/COVERAGE.md](docs/COVERAGE.md) for the full list.

## Validation

These commands are release guards for this repository. They are not the default prelude for normal user work.

```powershell
python .\scripts\validate_release.py
python .\scripts\run_trigger_eval.py
python .\scripts\run_quality_eval.py
```

The trigger evaluation currently covers 131 local proxy cases, including short Office artifact prompts and extreme multi-skill composition prompts for research, top-tier development, authorized red-team planning, UI engineering, incident/crisis work, and protocol/IoT analysis.

The quality evaluation scores committed golden responses under `evals/quality/golden-responses/`. It checks real HTML/PNG UI evidence, imports and executes a repo-repair Python behavior assertion, and opens `.pptx`, `.xlsx`, and `.docx` as OOXML packages to verify slide/chart/text structures, workbook formulas/tables/charts/recalculated cells, and Word comments/redlines/styles/numbering/rels/table geometry.

It is a deterministic release gate, not a replacement for native Office rendering, full Excel calculation, human taste review, or real project CI.

## Safety Scope

Security-related skills are defensive and authorization-scoped. They are for owned or explicitly authorized assets, local code/config review, logs, reports, labs, CTFs, training ranges, detection, hardening, verification, and reporting.

They do not provide guidance for unauthorized access, credential theft, persistence, detection evasion, C2, phishing collection, data exfiltration, or destructive actions. Production, credentials, paid services, remote writes, deletion, push, PR actions, cloud resources, and CI/CD permission changes require explicit authorization.

## Repository Layout

```text
skills/                 # Installable skill folders
docs/                   # Usage, triggering, coverage, provenance, i18n, sanitization
evals/                  # Trigger evals, quality evals, golden responses
scripts/                # Release validation and eval scripts
.github/workflows/      # CI validation
manifest.json           # Machine-readable skill inventory
LICENSE                 # GNU Affero General Public License v3.0
NOTICE                  # Attribution notice
```

## Documentation

- [Usage Guide](docs/USAGE.md)
- [Triggering Guide](docs/TRIGGERING.md)
- [Trigger Evaluation](docs/TRIGGER_EVAL.md)
- [Quality Evaluation](docs/QUALITY_EVAL.md)
- [Coverage Matrix](docs/COVERAGE.md)
- [Language References](docs/LANGUAGES.md)
- [Sanitization Notes](docs/SANITIZATION.md)
- [Provenance](docs/PROVENANCE.md)
- [Enforcement Guide](docs/ENFORCEMENT.md)
- [Takedown Template](docs/TAKEDOWN_TEMPLATE.md)
- [Trademark Policy](TRADEMARK.md)
- [Security Policy](SECURITY.md)

## License

From the current version onward, this repository is licensed under GNU Affero General Public License v3.0 only, `AGPL-3.0-only`. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

This is an OSI-style open source path, so the license does not prohibit commercial use. It does require license preservation, copyright notices, source availability, same-license sharing for covered derivatives, and source availability for modified network-service deployments.

Strict notice: open source does not allow removing attribution, removing `LICENSE` / `NOTICE`, stripping source identifiers, closed-source repackaging in violation of the AGPL, false originality claims, or any implication of official Coff0xc authorization. Coff0xc may use Git history, source identifiers, similarity analysis, purchase records, platform pages, and distributed artifacts as evidence for takedown requests, license enforcement, trademark/impersonation complaints, and legal claims.

`SKILL.md` files include source-level identifiers for copyright and origin evidence. They do not affect skill execution. To scan a suspected copy:

```powershell
python .\scripts\scan_provenance.py <suspected-folder>
```

This license change is not retroactive. Versions published before the change remain under the license terms that applied to those earlier versions.
