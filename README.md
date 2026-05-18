# coffee-skill

中文 | [English](#english)

[![CI](https://github.com/Coff0xc/coffee-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/Coff0xc/coffee-skill/actions/workflows/validate.yml)
![Skills](https://img.shields.io/badge/skills-18-2f855a)
![Trigger Eval](https://img.shields.io/badge/trigger_eval-131_cases-2563eb)
![Quality Eval](https://img.shields.io/badge/quality_eval-7_real_artifacts-7c3aed)
![License](https://img.shields.io/badge/license-source_available_noncommercial-b91c1c)
![Codex](https://img.shields.io/badge/Codex-AgentSkills-111827)

`coffee-skill` 是给 Codex / AgentSkills 兼容客户端安装的工作流 skill pack。它解决的是 AI vibe coding 的三个高频问题：AI 不知道该用什么能力、做出来的东西没质量证据、普通任务被过重流程拖慢。

核心设计很简单：

- **窄任务直达**：修 bug、改 UI、做 PPT、审计代码这类单域任务直接进入最具体 skill。
- **复杂任务编排**：跨前后端、数据、UI、安全、Office 的任务才让 `coff0xc-skill-router` 选主 skill、补辅助 skill、排阶段和重路由。
- **质量有证据**：dev 看测试和 diff；UI 看状态、截图和布局证据；Office 解包 PPTX/XLSX/DOCX 查结构；安全结论要有授权边界和证据。
- **日常快路径**：每个 skill 顶部都有 `快速规则（日常任务先读这里）`；trigger eval、quality eval、golden responses 和 workflow trace 只用于 release/eval。

本仓库公开可见，但不是开源授权。个人学习、研究、评估和本地非商业使用可以保留署名后使用；任何商业化、公司内部生产使用、咨询交付、付费课程、付费社群、agent 包、托管服务、镜像、转售或衍生发布，都必须先通知 Coff0xc 并获得书面许可。没有书面许可，就没有商业授权。

## 30 秒上手

个人学习、研究、评估和本地非商业使用，在仓库根目录执行：

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

重启或刷新 Codex，然后试：

```text
使用 coff0xc-software-engineering：这个 repo 测试挂了，帮我最小修复并验证。
```

不知道该用哪个 skill 时：

```text
你自己判断要用哪些 coff0xc skills，并把它们串成工作流完成这个功能。
```

## 选哪个入口

| 你要做什么 | 直接用 | 你应该拿到什么 |
|---|---|---|
| 修 repo、写功能、复现 CI、最小修复 | `coff0xc-software-engineering` | 代码 diff、根因、验证结果、剩余风险 |
| 做前端/UI/报告表达，或正式 PPTX/DOCX/XLSX | `coff0xc-ui-doc-output` / `coff0xc-office-doc-tools` | 截图/浏览器证据，或可编辑 Office 文件和结构检查 |
| 做 Agent/RAG、API、数据契约、科研图 | `coff0xc-ai-agent-rag` / `coff0xc-api-data-platform` / `coff0xc-research-drawio-diagram` | 架构、schema、评测、draw.io、证据表 |
| 安全、合规、应急、身份、云、协议、区块链 | 对应安全类 `coff0xc-*` skill | 授权边界、证据、影响、修复/检测/加固建议 |
| 任务跨多个领域或不知道怎么分流 | `coff0xc-skill-router` | 主 skill、辅助 skill、阶段门禁、重路由条件 |

完整卡片索引见 [Skill Index](docs/SKILL_INDEX.md)。

## 为什么这些 skills 存在

| AI 常见失败 | 本仓库怎么压住 |
|---|---|
| 一上来就长篇计划，或者选错能力 | 窄任务直达专业 skill；跨域才启用 router；普通任务不跑 release gate。 |
| 代码改了但不知道好没好 | dev skill 强制读仓库规则、定位根因、最小改动、跑可用验证、不乱改 lockfile。 |
| UI 只是“能看”，一股模板味 | UI skill 强制产品类型、设计系统、状态覆盖、响应式、可访问性和截图/浏览器证据。 |
| PPT/Excel/DOCX 只生成文件名 | Office skill 要求 PPTX/XLSX/DOCX 可编辑、可渲染、可解包检查结构和公式/批注/样式。 |
| 安全任务越界或只给吓人的话 | 安全类 skill 默认授权/防御优先，高风险动作先确认，发现必须带证据和修复路径。 |

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

完整入口选择、能力卡片、常见组合和手动触发示例见 [Skill Index](docs/SKILL_INDEX.md)。

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
LICENSE                 # Source-available noncommercial license
NOTICE                  # 归属说明
```

## 文档

- [Usage Guide](docs/USAGE.md)
- [Skill Index](docs/SKILL_INDEX.md)
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

从当前版本起使用自定义 source-available noncommercial 授权。见 [LICENSE](LICENSE) 和 [NOTICE](NOTICE)。

这意味着：个人学习、研究、评估和本地非商业使用可以使用；商业化必须先通知 Coff0xc 并获得书面许可。禁止无通知/无授权的商业使用、公司内部生产使用、咨询交付、转售、付费再分发、商业托管、内训、课程打包、付费社群、agent 包打包、镜像发布或包装成任何产品/服务。

严正声明：未经书面许可的商业化不被授权；去除署名、删除 `LICENSE` / `NOTICE`、删除源码标识、冒充原创、冒充 Coff0xc 官方或暗示独家授权，均不被许可。Coff0xc 会使用 Git 历史、源码标识、相似度对比、购买记录、平台页面和交付包作为下架投诉、许可证执行、商标/冒充投诉和法律主张的证据。

本仓库的 `SKILL.md` 文件包含源码级标识。它是版权和来源取证元数据，不影响 skill 执行。扫描可疑复制品：

```powershell
python .\scripts\scan_provenance.py <suspected-folder>
```

注意：许可证变更不追溯。变更前已经发布的版本仍按当时适用的许可证授权。

---

## English

Turn Codex / AgentSkills-compatible assistants into reusable, verifiable, recoverable workflows without making ordinary tasks slow.

`coffee-skill` is an installable `SKILL.md` workflow pack. It is built for the three failure modes that hurt agentic coding work: the assistant chooses the wrong capability, produces work without evidence, or turns simple tasks into heavy process.

The design:

- **Narrow tasks go direct**: bug fixes, UI work, Office artifacts, AppSec review, and reports should use the most specific skill.
- **Cross-domain tasks compose**: the router selects a primary skill, adds only necessary support skills, sequences phases, defines gates, and re-routes when evidence changes.
- **Quality leaves evidence**: dev work shows diffs and validation, UI work shows state/screenshot/layout evidence, Office work opens OOXML packages, and security work keeps authorization boundaries explicit.
- **Fast by default**: every skill starts with quick rules; trigger evals, quality evals, golden responses, and workflow traces are release/eval gates.

This repository is publicly visible, but it is not open-source licensed. Personal learning, research, evaluation, and local noncommercial use are allowed with attribution preserved. Any commercialization, company internal production use, consulting deliverable, paid course, paid community, agent-pack bundling, hosted service, mirror, resale, or derivative publication requires prior notice to Coff0xc and written permission. Without written permission, there is no commercial authorization.

## 30-Second Setup

For personal learning, research, evaluation, and local noncommercial use:

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

Restart or refresh Codex, then try:

```text
Use coff0xc-software-engineering: this repo has failing tests; make the smallest repair and validate it.
```

If you do not know which skill to use:

```text
Decide which coff0xc skills are needed, chain them into a workflow, and complete this task.
```

## Choose An Entry Point

| Task | Use | Expected output |
|---|---|---|
| Repo repair, feature work, CI reproduction | `coff0xc-software-engineering` | diff, root cause, validation, residual risk |
| Frontend/UI/report polish, or formal PPTX/DOCX/XLSX | `coff0xc-ui-doc-output` / `coff0xc-office-doc-tools` | screenshot/browser evidence, or editable Office files with structure checks |
| Agent/RAG, API/data contracts, research diagrams | `coff0xc-ai-agent-rag` / `coff0xc-api-data-platform` / `coff0xc-research-drawio-diagram` | architecture, schemas, evals, draw.io files, evidence tables |
| Security, compliance, incident response, identity, cloud, protocol, blockchain | matching `coff0xc-*` security skill | authorization scope, evidence, impact, remediation/detection/hardening |
| Cross-domain or unclear work | `coff0xc-skill-router` | primary skill, support skills, phase gates, re-routing conditions |

See the full [Skill Index](docs/SKILL_INDEX.md).

## Why These Skills Exist

| Common agent failure | How this pack handles it |
|---|---|
| Wrong capability or too much planning | Narrow tasks go direct; cross-domain tasks use the router; normal work does not run release gates. |
| Code changes without proof | Dev workflow reads repo rules, finds root cause, makes small diffs, validates, and avoids lockfile noise. |
| Template-looking UI | UI workflow checks product type, design system, states, responsiveness, accessibility, and screenshots/browser evidence. |
| Office files that only exist by name | Office workflow requires editable PPTX/XLSX/DOCX, render evidence, and OOXML structure checks. |
| Security work that drifts out of scope | Security workflows are authorization-first and evidence-based, with confirmation gates for risky actions. |

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

See [Skill Index](docs/SKILL_INDEX.md) for the full capability map, recipes, and manual invocation examples; see [Coverage Matrix](docs/COVERAGE.md) for full domain coverage.

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
LICENSE                 # Source-available noncommercial license
NOTICE                  # Attribution notice
```

## Documentation

- [Usage Guide](docs/USAGE.md)
- [Skill Index](docs/SKILL_INDEX.md)
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

From the current version onward, this repository uses a custom source-available noncommercial license. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

Personal learning, research, evaluation, and local noncommercial use are allowed with attribution preserved. Commercialization requires prior notice to Coff0xc and written permission. Unauthorized commercial use, company internal production use, consulting delivery, resale, paid redistribution, commercial hosting, paid course bundling, paid community use, paid agent-pack bundling, mirroring, or packaging into any product or service is not permitted.

Strict notice: unnotified commercial use, unauthorized commercial use, removal of attribution, removal of `LICENSE` / `NOTICE`, stripping source identifiers, false originality claims, or any implication of official Coff0xc authorization is not permitted. Coff0xc may use Git history, source identifiers, similarity analysis, purchase records, platform pages, and distributed artifacts as evidence for takedown requests, license enforcement, trademark/impersonation complaints, and legal claims.

`SKILL.md` files include source-level identifiers for copyright and origin evidence. They do not affect skill execution. To scan a suspected copy:

```powershell
python .\scripts\scan_provenance.py <suspected-folder>
```

This license change is not retroactive. Versions published before the change remain under the license terms that applied to those earlier versions.
