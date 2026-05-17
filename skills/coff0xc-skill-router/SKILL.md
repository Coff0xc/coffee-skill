---
name: coff0xc-skill-router
description: "Coff0xc lightweight skill router and autonomous multi-skill composer. Use only when the user asks the AI to decide which coff0xc skills to use, chain skills, build a task/workflow graph, orchestrate vibe coding, handle cross-domain/multi-domain work, or recover from an uncertain/missing trigger. 中文触发：自主编排、多 skill 工作流、AI 自己判断、自动串联 skill、任务图、工作流图、跨领域、跨域、多领域、多维度、编排工作流、vibe coding、不确定用哪个、选择 skill、帮我分流、串联 skill。Do not use for narrow tasks already covered by one specific skill."
---

# coff0xc-skill-router

## 快速规则（日常任务先读这里）
> **[单域直达]** 能用一个专业 skill 做完就直接用它，不输出长 skill graph。
> **[跨域编排]** 只有任务确实跨多个领域或用户要求 AI 自己串联 skill，才给主 skill、辅助 skill、阶段和门禁。
> **[轻量执行]** 复杂任务只给 3-5 行可执行工作流，然后马上进入第一阶段。
> **[发版边界]** trigger eval、quality eval、workflow trace、golden responses 只在 review/eval/发版/CI/推送时使用。

普通任务按本节分流；只有路由调试、skill 质量验证或复杂跨域工作流才读取 router map reference。

## 能力定位
面向不确定任务和跨领域任务的轻量 autonomous skill composer。它不是把所有能力揉成一个大 skill，也不是普通任务的必经步骤；它只在任务确实需要选择、分流或跨域编排时介入。

单一任务只选一个最具体 skill；复杂任务输出主 skill、辅助 skill、执行顺序、门禁和重路由条件。

## 能交付什么
- 轻量分流结果：当前主 skill、必要辅助 skill、暂不使用的 skill
- 分阶段执行顺序：每阶段调用哪个 skill、输入、输出、完成门禁
- 候选 skill 对比、取舍理由和适用边界
- 需要澄清的最少问题
- 执行中新增、移除或切换 skill 的条件
- 后续手动触发或自然语言触发句式

## 可以接收什么输入
- 模糊任务描述、多个领域混合需求、vibe coding 需求
- 用户说不确定用哪个 skill、自动触发失败
- 仓库、截图、日志、论文、配置等混合材料
- 用户要求 AI 自己判断、自己串联 skill、按工作流完成

## 放心使用的边界
- 负责规划和编排，不替代专业 skill 的深层执行规则
- 遇到安全、生产、凭据、删除、远程写入或付费动作时沿用目标 skill 的门禁
- 无法确定时给 2-3 个候选组合并问最小澄清问题
- 安全类能力默认只用于授权、防御、检测、加固、验证和报告；不提供未授权攻击、凭据窃取、持久化、规避检测、C2、钓鱼收集、数据外传或破坏性步骤。

## 为什么可以放心
- 保持 skill 模块化，只在需要时加载对应专业流程
- 每个 skill 都必须有明确职责、输入、输出和退出门禁
- 执行中根据真实证据重路由，而不是死守初始判断
- 保留手动触发写法，用户仍可强制指定某个 skill

## 典型使用方式
```text
使用 coff0xc-skill-router 帮我判断这个任务该用哪个 skill。
使用 coff0xc-skill-router 这个需求同时涉及 API、UI 和安全，帮我分流。
你自己判断要用哪些 coff0xc skills，并把它们串成工作流完成这个功能。
这个 vibe coding 任务可能涉及前后端、数据库、安全和文档，你来编排 skill。
Use coff0xc-skill-router when a Coff0xc skill did not auto-trigger.
```


## 目标
作为自动触发兜底入口和多 skill 编排入口。当前端模型没有自动选择具体 Coff0xc skill，或任务明显跨多个领域时，快速选择主 skill 和必要支持 skill，然后读取并执行当前阶段对应 skill 的工作流。

## 为什么需要 Router
- 多个客户端只用 `name` 和 `description` 参与触发，正文内容不会帮助首次触发。
- 中文请求、缩写、英文工具名和安全领域黑话容易导致具体 skill 漏触发。
- 真实任务经常不是一个 skill 能完成：开发会牵涉 API、数据、UI、安全、Office 交付或发布验证。
- Router 只负责分流和编排，不把所有专业规则装进一个大上下文。

## 自治编排规则
1. 如果一个更具体的 Coff0xc skill 已经完全覆盖任务，直接执行该 skill；不要输出 router 计划。
2. 如果任务跨领域，构造最小 skill graph：选一个主 skill，再添加支持 skill；不要把所有看似相关的 skill 都塞进去。
3. 每个支持 skill 必须有明确职责：补契约、补 UI、补安全、补文件交付、补检测、补合规、补验证。
4. 先执行当前阶段需要的 skill。阶段完成后根据证据决定是否继续、切换或新增 skill。
5. 如果请求涉及安全、生产、凭据、远程写入、删除或付费动作，先套用对应专业 skill 的硬门禁。
6. 如果无法确定组合，给出 2-3 个候选 workflow 和最小澄清问题；不要凭空执行高风险动作。
7. 除非用户明确要求评测/发版/推送/质量验证，不要生成 workflow trace、golden response、eval 报告或长篇自证材料。

## Skill Composition Loop
只在跨域或用户明确要求“你自己串联 skill / 编排工作流”时使用本循环。普通开发、UI、Office、安全、API 等单域任务直接进入对应专业 skill。

1. 读任务和证据：目标、输入、交付物、约束、风险、已有文件。
2. 选主 skill：决定谁负责最终结果。
3. 加支持 skill：只加入当前任务真实需要的能力。
4. 排阶段：每阶段写清输入、动作、输出和完成门禁。
5. 执行当前阶段：读取对应 skill 的 `SKILL.md`，按它的工作流做。
6. 重路由：发现新表面时调整 graph，例如从 dev 扩到 API/UI/AppSec/Office。
7. 收口：所有阶段门禁通过后，总结完成项、验证项、风险和下一步。

## 常见组合模式
| 任务类型 | 默认主 skill | 常见支持 skill | 组合意图 |
| --- | --- | --- | --- |
| Vibe coding / full-stack feature | `coff0xc-software-engineering` | `coff0xc-api-data-platform`, `coff0xc-ui-doc-output`, `coff0xc-secure-code-appsec` | 先修/实现，再补契约、界面质量和安全回归 |
| AI knowledge base / Agent app | `coff0xc-ai-agent-rag` | `coff0xc-api-data-platform`, `coff0xc-software-engineering`, `coff0xc-ui-doc-output` | 先定 Agent/RAG 架构，再落 API、代码和 UI |
| Data product / analytics dashboard | `coff0xc-api-data-platform` | `coff0xc-ui-doc-output`, `coff0xc-office-doc-tools`, `coff0xc-software-engineering` | 先定数据契约，再做界面和可交付文件 |
| Investor / executive deliverable | `coff0xc-office-doc-tools` | `coff0xc-ui-doc-output`, `coff0xc-api-data-platform`, `coff0xc-research-drawio-diagram` | 先定交付文件，再补叙事、数据和图 |
| Secure release review | `coff0xc-secure-code-appsec` | `coff0xc-cloud-devsecops`, `coff0xc-software-engineering`, `coff0xc-compliance-architecture` | 先找风险，再修复、验证和整理上线证据 |
| Detection / incident workflow | `coff0xc-detection-response` | `coff0xc-vulnerability-lifecycle`, `coff0xc-cloud-devsecops`, `coff0xc-purple-deception` | 先建检测/时间线，再做优先级和覆盖验证 |

更多组合和完整路由表只在复杂编排或 router 调试时读取 `references/router-map.md`。

## 输出格式
普通任务不要输出这段，直接执行对应专业 skill。复杂任务先输出短编排，不要写长篇理论：

```markdown
工作流：
- 主 skill: <skill>
- 辅助 skills: <skill>: <为什么需要>
- 暂不使用: <skill>: <为什么不需要>

阶段：
1. <阶段名> - 使用 <skill>，门禁：<可验证完成标准>
2. <阶段名> - 使用 <skill>，门禁：<可验证完成标准>

重路由条件：
- 如果发现 <证据>，新增/切换到 <skill>。
```

执行时可以边做边更新，但不要把“初始工作流”当不可改的计划。

## 手动触发写法
如果自动触发不稳定，用户可以直接写：

```text
使用 coff0xc-secure-code-appsec 审计这个项目
用 coff0xc-ai-agent-rag 设计一个 RAG Agent
调用 coff0xc-cloud-devsecops 检查 K8s 和 CI/CD
使用 coff0xc-office-doc-tools 生成一份可编辑 PPTX 并检查预览
按 coff0xc-detection-response 写 Sigma/YARA 检测
用 coff0xc-skill-router 帮我选择合适 skill
```

## 触发排障
- skill 目录名必须和 frontmatter `name` 一致。
- 安装或替换后需要重启/刷新客户端，让 skill 列表重新索引。
- frontmatter 只保留 `name` 和 `description` 最稳；触发词必须写进 `description`。
- 同名 skill 分布在多个目录时可能抢占触发，保留一份主版本。
- 太短或只写抽象能力的 description 容易漏触发；应包含中文、英文、工具名、任务名和常见缩写。

## 按需 References

| Reference | 何时读取 |
| --- | --- |
| `references/router-map.md` | 复杂多域编排、路由调试、扩展组合模式、解释某个 skill 为什么被选或被排除。 |
