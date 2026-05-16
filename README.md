# coffee-skill

中文 | [English](#english)

`coffee-skill` 是一套给 Codex / Agent 类 AI 工具使用的技能包。它不是一个普通脚本库，也不是一个独立应用，而是一组可以安装到 AI 助手里的“工作说明书”。安装后，AI 在遇到开发、Agent/RAG、API、UI、Office/PDF 文件交付、科研绘图、防御安全等任务时，可以自动加载更具体的工作流程、边界规则和验证清单，减少胡乱发挥。

如果你还不熟悉 AI skill，可以先这样理解：

- 普通 AI 助手像一个能力很强但需要你反复交代细节的人。
- 一个 `skill` 像一份提前写好的岗位 SOP，告诉 AI：遇到什么任务该触发、先查什么、怎么做、哪些事不能做、最后怎么验证。
- 这个仓库就是把很多常见工作 SOP 整理成可安装的技能包，让 AI 不只是“回答问题”，而是更稳定地“按流程做事”。

推荐 GitHub About：

```text
Comprehensive Codex skills pack for engineering, AI agents, Office docs, research draw.io diagrams, and defensive security, with multilingual triggers and a router fallback
```

## 这个仓库有什么用

这个仓库的核心作用是：让 AI 助手在真实任务里更像一个有流程、有边界、会验证结果的工程协作者。

它主要解决几个问题：

1. **不知道该怎么让 AI 做复杂任务**
   很多人只会说“帮我改一下”或“帮我看看”，AI 可能直接给一段泛泛建议。skill 会告诉 AI：先看项目结构、再定位文件、再计划、再修改、最后验证。

2. **AI 容易漏步骤**
   比如改代码后不跑测试，做安全分析却不说明授权边界，画图只给 Mermaid 不给可编辑文件。skill 会把这些步骤写进固定流程。

3. **AI 容易选错方向**
   同一句“帮我审计这个项目”，可能是代码质量审查，也可能是 Web 安全审计，还可能是 CI/CD 风险检查。本仓库把能力拆成多个领域，并提供路由 skill 帮 AI 选对方向。

4. **AI 说“完成了”但没有证据**
   本仓库强调验证：命令没跑过就不能说已通过；事实没查过就要标注未验证；高风险动作要先确认。

5. **中文用户触发困难**
   很多 skill 只写英文关键词，中文描述时不一定触发。本仓库在 `description` 中加入中文、英文、缩写、常见口语和手动调用方式。

## 什么是 Skill

在 Codex / Claude Code / AgentSkills 这类工具里，`skill` 通常是一个文件夹，里面至少有一个 `SKILL.md`。

一个最简单的 skill 长这样：

```text
some-skill/
└── SKILL.md
```

`SKILL.md` 里通常包含两部分：

- **frontmatter**：最上面的元信息，比如 skill 名称和触发描述。AI 客户端通常先看这里决定要不要加载这个 skill。
- **正文说明**：真正的工作流程，比如适用场景、不能做什么、执行步骤、验证方式和输出格式。

所以，skill 的价值不只是“写一段提示词”。好的 skill 应该告诉 AI：

- 什么时候该用它；
- 遇到任务后先做什么；
- 哪些动作可以直接做；
- 哪些动作必须先问用户；
- 怎么判断结果是真的完成；
- 最后应该怎样汇报。

## 这个仓库适合谁

适合：

- 想让 Codex 更稳定完成本地开发任务的人；
- 经常让 AI 做代码修复、测试、重构、文档、报告、安全分析的人；
- 想把自己的工作流程沉淀成可复用 AI 能力的人；
- 中文用户，尤其是希望用自然中文描述任务也能触发正确 skill 的用户；
- 团队内部想统一 AI 工作方式、减少“每个人 prompt 不一样”的情况。

不适合：

- 只想运行一个命令行工具的人；
- 不使用 Codex / Claude Code / AgentSkills 这类支持 skill 的 AI 客户端的人；
- 想绕过授权做攻击、钓鱼、凭据窃取、隐蔽持久化或破坏性操作的人。

## 包含哪些能力

本仓库包含 18 个 skills：

- 17 个综合能力 skill；
- 1 个兜底路由 skill：`coff0xc-skill-router`。

| Skill | 可以用来做什么 | 典型场景 | 安全边界 |
|---|---|---|---|
| `coff0xc-software-engineering` | 软件开发、修 bug、全栈功能、测试、重构、脚本、Git 摘要 | “这个项目跑不起来”“少问确认，直接实现这个多文件功能”“修 failing tests” | 否 |
| `coff0xc-ai-agent-rag` | AI Agent、RAG、Prompt、LLM 应用、工具调用、评测、观测和成本 | “设计一个本地知识库助手”“评估工具调用 Agent 架构” | 否 |
| `coff0xc-api-data-platform` | REST、GraphQL、OpenAPI、数据库 schema、CLI、SDK、数据契约 | “设计 billing API”“把 curl 流程做成 CLI” | 否 |
| `coff0xc-ui-doc-output` | UI/前端体验、报告表达、翻译、交付文案 | “优化 dashboard”“把中文报告润色成英文交付版” | 否 |
| `coff0xc-office-doc-tools` | PPT/PPTX、DOCX/Word、PDF、Excel/XLSX/CSV 正式文件交付，强调 PPT 审美、Excel 数据解析、DOCX 阅读与格式门禁 | “做一份高审美可编辑 PPTX”“把 CSV 做成带公式和图表的可审计 Excel” | 否 |
| `coff0xc-research-drawio-diagram` | 论文方法图、科研架构图、模型结构图、可编辑 `.drawio` 文件 | “根据论文和官方仓库画 draw.io 方法图” | 否 |
| `coff0xc-secure-code-appsec` | 代码安全审计、Web/API/GraphQL/OAuth/浏览器/LLM 应用安全 | “审计认证越权风险”“看 source/sink 和后门迹象” | 是 |
| `coff0xc-cloud-devsecops` | 云、Docker、K8s、CI/CD、供应链、密钥管理 | “检查 GitHub Actions 和镜像供应链风险” | 是 |
| `coff0xc-detection-response` | SOC、SIEM、Sigma/YARA、威胁狩猎、应急响应、取证 | “根据日志写检测规则”“做 IR 时间线” | 是 |
| `coff0xc-vulnerability-lifecycle` | CVE、补丁分析、漏洞管理、风险优先级、修复跟踪 | “分析这个 CVE 是否影响我们” | 是 |
| `coff0xc-identity-zero-trust` | IAM、SSO、MFA、AD/Kerberos、权限、凭证、零信任 | “评估账号权限和横向移动防御” | 是 |
| `coff0xc-authorized-assessment` | 授权评估规划、ROE、控制验证、红队行为防御化 | “在授权范围内规划一次安全评估” | 是 |
| `coff0xc-binary-mobile-iot` | 逆向、二进制、移动、IoT、ICS、CTF、密码分析 | “分析 APK/固件/可执行文件的结构” | 是 |
| `coff0xc-blockchain-security` | 智能合约、DeFi、Web3、多链审计路由 | “审计合约权限、资产流、价格来源” | 是 |
| `coff0xc-compliance-architecture` | 威胁建模、合规、数据安全、隐私、基线 | “做上线前安全架构评审” | 是 |
| `coff0xc-purple-deception` | 紫队、ATT&CK 映射、蜜罐、欺骗防御、检测覆盖 | “把攻击行为映射成检测改进计划” | 是 |
| `coff0xc-network-protocol-security` | TLS/DNS/QUIC/HTTP、抓包、无线、协议安全 | “分析 pcap 里的握手和异常字段” | 是 |
| `coff0xc-skill-router` | 不确定该用哪个 skill 时做路由 | “帮我选择合适 skill”“这个任务同时涉及多个领域” | 是 |

这里的“安全边界”意思是：该 skill 涉及安全能力，默认只服务于授权、防御、检测、加固、验证和报告，不用于未授权攻击。

## 能力地图

如果你不知道从哪里开始，可以按最终想要的产物选择 skill：

| 想要的结果 | 推荐 skill | 交付物 |
|---|---|---|
| 使用 coff0xc-software-engineering 修复这个 repo 的 failing tests，并说明验证结果。 | `coff0xc-software-engineering` | 代码补丁、脚本或配置修改; 失败原因和根因链路说明 |
| 使用 coff0xc-ai-agent-rag 设计一个带引用、缓存和失败降级的企业知识库助手。 | `coff0xc-ai-agent-rag` | Agent/RAG 架构方案和数据流; 工具 schema、记忆/缓存策略、检索和引用策略 |
| 使用 coff0xc-api-data-platform 设计这个 billing REST API，包含 OpenAPI、分页和错误码。 | `coff0xc-api-data-platform` | REST/GraphQL/OpenAPI 契约; 数据库 schema、迁移和数据一致性建议 |
| 使用 coff0xc-ui-doc-output 优化这个 dashboard，并用截图检查移动端。 | `coff0xc-ui-doc-output` | 可用 UI/组件/页面改动或设计建议; 桌面/移动端截图或浏览器 smoke 结果 |
| 使用 coff0xc-office-doc-tools 生成一份可编辑 PPTX，并检查预览、图表和导出文件。 | `coff0xc-office-doc-tools` | 可编辑 PPTX/DOCX/PDF/XLSX 文件; 渲染/预览 QA、公式检查和交付路径 |
| 使用 coff0xc-research-drawio-diagram 根据论文和官方 GitHub 画一个可编辑 draw.io 方法图。 | `coff0xc-research-drawio-diagram` | 可编辑 `.drawio` 文件; 图结构 JSON/spec 或模块清单 |
| 使用 coff0xc-secure-code-appsec 审计这个 Web/API 项目的认证和越权风险。 | `coff0xc-secure-code-appsec` | 安全发现列表：位置、影响、证据、复现条件; source/sink 或权限链路说明 |
| 使用 coff0xc-cloud-devsecops 检查 Docker、K8s、CI/CD 和供应链风险。 | `coff0xc-cloud-devsecops` | 云/IaC/K8s/CI/CD 风险清单; 最小权限、网络隔离、pipeline gate 和密钥轮换建议 |
| 使用 coff0xc-detection-response 根据这些 EDR 日志写 Sigma 和 YARA 检测规则。 | `coff0xc-detection-response` | Sigma/YARA/查询规则草案和字段映射; IOC、时间线、攻击阶段和 ATT&CK 映射 |
| 使用 coff0xc-vulnerability-lifecycle 分析这个 CVE 的影响、补丁和修复优先级。 | `coff0xc-vulnerability-lifecycle` | 漏洞原理和补丁差异摘要; 受影响范围、CVSS/EPSS/KEV 和业务优先级 |
| 使用 coff0xc-identity-zero-trust 评估这个 AD 域的 Kerberos、BloodHound 路径和服务账号风险。 | `coff0xc-identity-zero-trust` | 身份/权限风险清单和路径说明; MFA/SSO/session/device posture 评估 |
| 使用 coff0xc-authorized-assessment 在书面授权范围内规划一次安全评估。 | `coff0xc-authorized-assessment` | 授权范围和 ROE 草案; 攻击面清单、测试阶段和禁止动作 |
| 使用 coff0xc-binary-mobile-iot 分析这个 APK 的权限、网络通信和 Frida hook 点。 | `coff0xc-binary-mobile-iot` | 样本/固件结构和入口点分析; 字符串、配置、权限、通信和硬件接口线索 |
| 使用 coff0xc-blockchain-security 审计这个 Solidity 合约的权限、资产流和价格来源。 | `coff0xc-blockchain-security` | 合约入口点和权限模型清单; 资产流、状态机、价格来源和外部调用风险 |
| 使用 coff0xc-compliance-architecture 做上线前安全架构评审和威胁建模。 | `coff0xc-compliance-architecture` | 架构风险评审和信任边界图; STRIDE/威胁建模、控制矩阵和差距分析 |
| 使用 coff0xc-purple-deception 把这些攻击行为映射成 ATT&CK 检测覆盖矩阵。 | `coff0xc-purple-deception` | ATT&CK 技术映射和演练假设; 检测覆盖矩阵、日志需求和响应验证点 |
| 使用 coff0xc-network-protocol-security 分析这个 pcap 里的 TLS 握手和异常字段。 | `coff0xc-network-protocol-security` | 协议流程、握手和状态机说明; pcap/日志字段分析、异常字段和安全影响 |
| 使用 coff0xc-skill-router 帮我判断这个任务该用哪个 skill。 | `coff0xc-skill-router` | 推荐 skill 和理由; 候选 skill 对比和适用边界 |

## 最常用的几个场景

### 1. 让 AI 修代码、写功能、跑验证

使用 `coff0xc-software-engineering`。

适合这样的请求：

```text
使用 coff0xc-software-engineering 修复这个 repo 的 failing tests，并说明验证结果。
使用 coff0xc-software-engineering 少问确认，直接实现这个多文件开发任务。
Use coff0xc-software-engineering to build this admin panel feature end to end with tests.
```

它会引导 AI 做这些事：

- 先读项目说明、配置、测试脚本和现有代码风格；
- 判断这是单文件修复还是多模块开发；
- 写短计划，不停在计划阶段；
- 最小正确改动；
- 能跑测试、lint、typecheck、build 就跑；
- 最后说明完成了什么、验证了什么、还有什么风险。

### 2. 设计或落地 AI Agent / RAG 系统

使用 `coff0xc-ai-agent-rag`。

适合这样的请求：

```text
使用 coff0xc-ai-agent-rag 设计一个带引用、缓存和失败降级的企业知识库助手。
Use coff0xc-ai-agent-rag to review this tool-calling agent design.
```

它会提醒 AI 不要只写 Prompt，而是考虑：

- 输入和输出；
- 工具调用；
- 检索质量；
- 记忆和缓存；
- 引用来源；
- 评测集；
- 成本、延迟和观测；
- 失败恢复和拒答策略。

### 3. 设计 API、数据库和 CLI

使用 `coff0xc-api-data-platform`。

适合这样的请求：

```text
使用 coff0xc-api-data-platform 设计这个 billing API、错误码、分页和 schema。
Use coff0xc-api-data-platform to turn this curl workflow into a stable CLI.
```

它会帮助 AI 把接口、数据结构、错误处理、分页、认证、兼容迁移和 SDK/CLI 输出一起考虑。

### 4. 优化 UI、报告和翻译

使用 `coff0xc-ui-doc-output`。

适合这样的请求：

```text
使用 coff0xc-ui-doc-output 优化这个 dashboard，并用截图检查移动端。
使用 coff0xc-ui-doc-output 把这份中文报告翻译润色成英文交付版。
```

它会提醒 AI 不只是改文字或样式，还要看：

- 页面信息密度；
- loading / empty / error / success 状态；
- 移动端和桌面端；
- 截图或浏览器验证；
- 报告结构、交付语言和术语一致性。

### 5. 生成或编辑 Office / PDF / Excel 文件

使用 `coff0xc-office-doc-tools`。

适合这样的请求：

```text
使用 coff0xc-office-doc-tools 把这份 Markdown 做成可编辑 PPTX，包含图表、讲述逻辑和预览验证。
使用 coff0xc-office-doc-tools 给这个 DOCX 加批注和修订，不覆盖原件，最后渲染检查版式。
使用 coff0xc-office-doc-tools 把这个 CSV 做成带公式、图表和校验的 Excel 工作簿。
```

它会提醒 AI 做这些事：

- 先确认最终文件格式、用途、受众和是否保留原件；
- PPTX 不能停在“能打开”：需要 claim spine、design system、contact-sheet 规划、反模板感检查、comeback scorecard 和渲染预览；
- Excel/XLSX/CSV 不能只做表面排版：需要 inspect 数据结构、保留 raw/source/assumptions、派生值用公式、trace 关键输出、扫描公式错误并检查图表渲染；
- DOCX 不能只抽文本：需要理解标题层级、表格、批注、修订和页眉页脚，检查真实 styles/numbering/table geometry，并尽量逐页渲染验证格式；
- PPT/DOCX/PDF 需要渲染或预览检查，不能只看文本；
- Excel/XLSX 需要检查公式、引用范围、错误值和图表来源；
- 最后给出最终文件路径、验证结果和未验证风险。

### 6. 根据论文画可编辑科研图

使用 `coff0xc-research-drawio-diagram`。

适合这样的请求：

```text
使用 coff0xc-research-drawio-diagram 根据这篇论文和官方 GitHub 画一个可编辑 draw.io 方法图。
帮我把这个 Transformer 论文的方法整理成 .drawio 模型结构图，要标注训练路径和推理路径。
```

这个 skill 的重点是输出可编辑 `.drawio` 文件，而不是只给一张截图或 Mermaid。它还会要求 AI 给出证据表，说明哪些连接来自论文，哪些是合理推断。

### 7. 做授权范围内的安全工作

安全相关任务会进入对应的安全 skill，例如：

```text
使用 coff0xc-secure-code-appsec 审计这个 Web/API 项目的认证和越权风险。
使用 coff0xc-cloud-devsecops 检查 Docker、K8s、CI/CD 和供应链风险。
使用 coff0xc-detection-response 根据这些日志写 Sigma/YARA 检测和验证样例。
使用 coff0xc-vulnerability-lifecycle 分析这个 CVE 的影响、补丁和修复优先级。
```

这些 skill 会强调：

- 是否有授权；
- 证据来自哪里；
- 哪些结论已验证，哪些只是推断；
- 如何修复、检测、加固和复查；
- 不提供未授权攻击、凭据窃取、持久化、规避检测或破坏性操作指导。

## 怎么安装

先审阅仓库内容，再把 `skills/` 下的文件夹复制到本地 Codex skills 目录。

Windows 示例：

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

复制后重启或刷新 Codex，让客户端重新索引 skill metadata。

如果你不确定是否安装成功，可以问：

```text
使用 coff0xc-skill-router 帮我选择合适 skill
```

如果客户端能识别并加载 `coff0xc-skill-router`，说明至少 skill 目录已经被扫描到了。

## 怎么提问更容易成功

你可以自然提问，也可以显式点名 skill。

自然提问示例：

```text
这个 Python 项目的 pytest 挂了，帮我定位失败用例，做最小修复，然后跑测试和 lint。
用 Agent/RAG 的方式设计一个本地知识库助手，需要引用来源、缓存、失败降级和评测集。
检查这个 Docker、K8s 和 GitHub Actions 配置有没有供应链、SBOM、secret scanning 和 IaC 风险。
帮我根据这篇论文和官方 GitHub 画一个可编辑的 draw.io 科研算法架构图。
```

显式调用示例：

```text
使用 coff0xc-skill-router 帮我选择合适 skill
使用 coff0xc-software-engineering 少问确认，直接实现这个多文件开发任务
使用 coff0xc-ai-agent-rag 设计一个 RAG Agent
使用 coff0xc-api-data-platform 设计这个 REST API 和数据库 schema
使用 coff0xc-ui-doc-output 优化这个 dashboard
使用 coff0xc-office-doc-tools 生成一份可编辑 PPTX 并检查预览
使用 coff0xc-research-drawio-diagram 根据论文和官方仓库生成 .drawio 架构图
使用 coff0xc-secure-code-appsec 审计这个项目
使用 coff0xc-cloud-devsecops 检查 K8s 和 CI/CD
使用 coff0xc-detection-response 写检测规则
```

一个简单原则：如果你知道要用哪个 skill，就直接点名；如果不知道，就用 `coff0xc-skill-router`。

## 什么时候应该用 Router

`coff0xc-skill-router` 是兜底入口。它适合这些情况：

- 你不知道该用哪个 skill；
- 一个任务同时涉及开发、API、UI、安全、文档等多个领域；
- 自动触发没有命中；
- 你想让 AI 先帮你拆任务。

示例：

```text
使用 coff0xc-skill-router 帮我判断这个任务应该用哪个 skill：我想把这个项目改成一个带 API、后台管理和安全审计能力的 MVP。
```

Router 不负责替代所有 skill，它更像前台分诊：先判断方向，再把任务交给最合适的专业 skill。

## 这个仓库里的文件分别是什么

```text
skills/                 # 真正可安装的 skill 文件夹
docs/                   # 用法、触发、覆盖、来源和清理说明
evals/                  # 触发率 proxy eval 数据和结果
scripts/                # 本地验证和 eval 脚本
manifest.json           # 机器可读 skill 清单
LICENSE                 # Apache License 2.0
NOTICE                  # 归属说明
README.md               # 本文档
```

如果你只想安装使用，主要看：

- `skills/`
- `README.md`
- `docs/USAGE.md`
- `docs/TRIGGERING.md`

如果你想维护或发布这个仓库，再看：

- `manifest.json`
- `scripts/validate_release.py`
- `scripts/run_trigger_eval.py`
- `evals/trigger-eval.json`
- `docs/PROVENANCE.md`
- `docs/SANITIZATION.md`

## 如何验证这个仓库是否健康

运行发布校验：

```powershell
python .\scripts\validate_release.py
```

它会检查：

- 每个 skill 文件夹都有匹配的 `SKILL.md` frontmatter name；
- 必需发布文档存在；
- manifest 中的 skills 都存在；
- 没有本地用户路径、private key、GitHub token 或 OpenAI-style key pattern。

运行触发评测：

```powershell
python .\scripts\run_trigger_eval.py
```

它会用一组本地测试问题检查：哪些 prompt 应该触发哪个 skill，哪些简单问题不应该误触发。注意，这只是本地 proxy eval，不等于完全复刻所有客户端的私有触发逻辑，但能帮助维护者发现明显漏词和误触发。

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

不用于：

- 未授权访问；
- 凭据窃取；
- 持久化；
- 规避检测；
- C2 操作；
- 钓鱼收集；
- 数据外传；
- 破坏性操作。

见 [SECURITY.md](SECURITY.md) 和 [docs/SANITIZATION.md](docs/SANITIZATION.md)。

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

`coffee-skill` is a publish-ready skill pack for Codex and AgentSkills-compatible AI coding assistants. It is not a standalone app or script library. It is a collection of installable workflow instructions that help an AI assistant choose the right process for engineering, AI Agent/RAG, API/data, UI/report output, Office/PDF file delivery, research draw.io diagrams, and defensive security tasks.

If you are new to AI skills, think of a skill as an operating procedure for the assistant:

- The skill metadata tells the client when the skill should load.
- The skill body tells the assistant what to inspect, what to do, what to avoid, how to verify the result, and how to report back.
- This repository packages those procedures into a reusable set of domain skills.

## What This Repository Does

`coffee-skill` helps AI assistants behave less like generic chatbots and more like careful task workers. It gives them:

- clearer trigger descriptions in Chinese and English,
- step-by-step workflows for common work domains,
- safety boundaries for security-related work,
- verification expectations before claiming completion,
- a router skill for cases where the user does not know which skill to choose.

## Included Skills

This repository contains 18 skills:

- 17 broad capability skills,
- 1 fallback router skill: `coff0xc-skill-router`.

| Skill | Use it for | Typical prompt | Security-scoped |
|---|---|---|---|
| `coff0xc-software-engineering` | Dev/autonomous development, full-stack or multi-file implementation, tests, refactors, scripts, Git | "Build this admin panel feature end to end with tests." | no |
| `coff0xc-ai-agent-rag` | AI agents, RAG, prompts, LLM apps, tools, evals, observability | "Design a RAG assistant with citations and fallback behavior." | no |
| `coff0xc-api-data-platform` | REST, GraphQL, OpenAPI, databases, CLI, SDK, data contracts | "Design this billing API and database schema." | no |
| `coff0xc-ui-doc-output` | UI/frontend work, report wording, translation, delivery copy | "Improve this dashboard and verify mobile layout." | no |
| `coff0xc-office-doc-tools` | PPTX, DOCX, PDF, Excel/XLSX/CSV file artifacts, with quality gates for PPT aesthetics, Excel data parsing, and DOCX reading/format fidelity | "Create a polished editable PPTX and verify the preview." | no |
| `coff0xc-research-drawio-diagram` | Research architecture diagrams and editable `.drawio` files | "Create an editable method figure from this paper and repo." | no |
| `coff0xc-secure-code-appsec` | Code audit and Web/API/GraphQL/OAuth/browser/LLM app security | "Review this authorized API for authz risks." | yes |
| `coff0xc-cloud-devsecops` | Cloud, Docker, Kubernetes, CI/CD, supply chain, secrets | "Check this GitHub Actions workflow for supply-chain risk." | yes |
| `coff0xc-detection-response` | SOC, SIEM, Sigma/YARA, threat hunting, IR, forensics | "Write detection rules from these logs." | yes |
| `coff0xc-vulnerability-lifecycle` | CVE research, patch analysis, vuln management, remediation | "Assess whether this CVE affects us." | yes |
| `coff0xc-identity-zero-trust` | IAM, SSO, MFA, AD/Kerberos, privileges, Zero Trust | "Review account permissions and lateral movement defense." | yes |
| `coff0xc-authorized-assessment` | Authorized assessment planning, ROE, control validation | "Plan an authorized security assessment." | yes |
| `coff0xc-binary-mobile-iot` | Reverse engineering, binary/mobile/IoT/ICS/CTF/crypto analysis | "Analyze this firmware or APK structure." | yes |
| `coff0xc-blockchain-security` | Smart contracts, DeFi, Web3, multi-chain audit routing | "Review contract permissions and asset flow." | yes |
| `coff0xc-compliance-architecture` | Threat modeling, compliance, data security, privacy, baselines | "Prepare a pre-launch architecture risk review." | yes |
| `coff0xc-purple-deception` | Purple team, ATT&CK mapping, honeypots, deception defense | "Map this attack behavior to detection coverage." | yes |
| `coff0xc-network-protocol-security` | TLS/DNS/QUIC/HTTP, packet analysis, wireless, protocol security | "Analyze this pcap handshake." | yes |
| `coff0xc-skill-router` | Route ambiguous tasks to the right skill | "Choose the right skill for this task." | yes |

## Install

Review the repository first, then copy the folders under `skills/` into your Codex skills directory.

Windows example:

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

Restart or refresh Codex after copying so the client re-indexes skill metadata.

## How To Use

Ask naturally:

```text
Fix this Python project's failing pytest cases, make the smallest correct change, then run tests and lint.
Design a local knowledge-base assistant with Agent/RAG architecture, citations, cache, fallback, and evals.
Check this Docker, Kubernetes, and GitHub Actions setup for supply-chain and secret risks.
Create an editable PPTX from this Markdown outline and verify the preview.
Create an editable draw.io research architecture diagram from this paper and official repo.
```

Or invoke a skill explicitly:

```text
Use coff0xc-skill-router to choose the right skill.
Use coff0xc-software-engineering to build this feature end to end with tests.
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-api-data-platform to design this REST API and database schema.
Use coff0xc-ui-doc-output to improve this dashboard.
Use coff0xc-office-doc-tools to create an editable PPTX with preview checks.
Use coff0xc-research-drawio-diagram to generate a .drawio figure from the paper and official repo.
Use coff0xc-secure-code-appsec to review this project.
```

For Office artifacts, `coff0xc-office-doc-tools` now applies stricter quality gates:

- PPTX work should include a claim spine, design system, contact-sheet plan, anti-template checks, comeback scorecard, and rendered preview review.
- Excel/XLSX/CSV work should inspect workbook/data structure, preserve raw/source/assumptions, use formulas for derived values, trace key outputs, scan formula errors, and verify chart renders.
- DOCX work should understand headings, tables, comments, tracked changes, headers/footers, real styles/numbering/table geometry, and page-rendered formatting before claiming layout quality.

## Validation

Run release validation:

```powershell
python .\scripts\validate_release.py
```

Run trigger evaluation:

```powershell
python .\scripts\run_trigger_eval.py
```

The trigger evaluation is a deterministic local proxy. It does not claim to reproduce every client's private skill-selection logic, but it is useful for catching obvious missing trigger words and false positives.

## Safety Scope

Security-related skills are defensive and authorization-scoped. They are intended for owned or explicitly authorized assets, local code and configuration review, logs, reports, lab environments, CTFs, training ranges, detection, hardening, verification, and reporting.

They do not include guidance for unauthorized exploitation, credential theft, persistence, detection evasion, C2 operation, phishing collection, data exfiltration, or destructive actions.

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
