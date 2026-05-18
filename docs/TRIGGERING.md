# Triggering Guide

## Why Skills Sometimes Do Not Auto-Trigger

Most clients select skills from frontmatter metadata, especially `name` and `description`. The body of `SKILL.md` is usually loaded only after the skill has already triggered, so trigger words and capability terms must be in `description`.

## Trigger Strategy In This Pack

- Each capability skill starts with broad Chinese/English capability terms.
- Descriptions include concrete deliverables, domain nouns, tool names, acronyms, and manual invocation cues without carrying long source-alias inventories.
- Release validation keeps frontmatter descriptions under a small metadata budget so daily skill selection stays fast.
- Each skill body starts with `快速规则（日常任务先读这里）`, then capability positioning, inputs, deliverables, boundaries, trust reasons, and examples.
- `coff0xc-skill-router` is the fallback when auto-triggering misses and the lightweight autonomous composer for cross-domain tasks.
- Narrow prompts should go directly to the most specific skill. Broad prompts should trigger a small workflow graph and then execution, not a long proof artifact.
- Main `SKILL.md` files are optimized for runtime fast paths. Heavy checklists, route maps, and eval guidance live in `references/` and should be loaded only when the active task needs them.

## Runtime Modes

| Mode | Trigger wording | Expected behavior |
|---|---|---|
| Execution mode | Normal task requests: fix, build, analyze, generate, edit, review a file, repair tests | Use one primary skill, add support skills only when needed, and execute the task. |
| Release / eval mode | `review the skill`, `run eval`, `quality test`, `release`, `push`, `CI gate`, `benchmark`, `确认是否真的好用` | Run trigger/quality/release gates and update generated eval artifacts. |

`workflow-trace.json`, golden responses, trigger evals, and quality evals belong to release/eval mode. They should not appear in normal task execution unless the user explicitly asks for them.

If a normal task feels slow, first check whether the agent unnecessarily invoked the router, loaded references, or entered release/eval mode. The expected fix is to return to the most specific skill and run only task-relevant validation.

## Composition Triggers

Use the router when the user says any of these:

```text
你自己判断要用哪些 coff0xc skills，并把它们串成工作流完成。
这个任务同时涉及前后端、数据库、UI 和安全，你来编排。
Decide which coff0xc skills are needed and chain them into a workflow.
Orchestrate a vibe-coding workflow for this repo.
```

Expected router output:

- primary skill,
- only necessary supporting skills with one-line reasons,
- phase order with gates,
- skills intentionally not used,
- re-routing conditions if new evidence appears.

The router should keep this output short. After the lightweight plan, continue with the first actionable phase instead of stopping at planning.

## Manual Invocation

Use one of these phrases when auto-triggering misses:

| Skill | Manual phrase | Capability cues |
|---|---|---|
| `coff0xc-software-engineering` | `使用 coff0xc-software-engineering ...` | 自主开发, 代码修复, 功能实现, 测试验证, CI 分诊, 快速内循环, 构建质量, Git 协作 |
| `coff0xc-ai-agent-rag` | `使用 coff0xc-ai-agent-rag ...` | Agent 架构, RAG 管线, 工具调用, 记忆系统, Prompt 工程, 评测观测 |
| `coff0xc-api-data-platform` | `使用 coff0xc-api-data-platform ...` | API 契约, 数据模型, 认证授权, CLI/SDK, 数据质量, 兼容演进 |
| `coff0xc-ui-doc-output` | `使用 coff0xc-ui-doc-output ...` | 产品 UI, 设计系统, 组件架构, 交互状态, 视觉验收, 报告输出, 翻译润色 |
| `coff0xc-office-doc-tools` | `使用 coff0xc-office-doc-tools ...` | PPT/PPTX, DOCX/Word, PDF, Excel/XLSX, CSV/表格, 渲染验证 |
| `coff0xc-research-drawio-diagram` | `使用 coff0xc-research-drawio-diagram ...` | 科研绘图, 论文方法图, 模型结构图, draw.io, 证据表, 推断标注 |
| `coff0xc-secure-code-appsec` | `使用 coff0xc-secure-code-appsec ...` | 代码审计, Source/Sink, 认证授权, Web/API 安全, GraphQL/OAuth, 后门检测 |
| `coff0xc-cloud-devsecops` | `使用 coff0xc-cloud-devsecops ...` | 云配置, 容器镜像, Kubernetes, CI/CD, 供应链, 密钥管理 |
| `coff0xc-detection-response` | `使用 coff0xc-detection-response ...` | 检测工程, 威胁狩猎, SIEM/SOC, YARA/Sigma, 应急响应, 取证分析 |
| `coff0xc-vulnerability-lifecycle` | `使用 coff0xc-vulnerability-lifecycle ...` | CVE 研究, 补丁分析, 影响评估, 优先级, 授权验证, 修复跟踪 |
| `coff0xc-identity-zero-trust` | `使用 coff0xc-identity-zero-trust ...` | 身份治理, AD/Kerberos, IAM, 凭证风险, 横向移动防御, 零信任 |
| `coff0xc-authorized-assessment` | `使用 coff0xc-authorized-assessment ...` | 授权范围, ROE, 攻击面, 控制验证, 红队防御化, 报告 |
| `coff0xc-binary-mobile-iot` | `使用 coff0xc-binary-mobile-iot ...` | 逆向分析, 移动安全, IoT 固件, ICS/OT, 密码实现, 崩溃/漏洞线索 |
| `coff0xc-blockchain-security` | `使用 coff0xc-blockchain-security ...` | 智能合约, DeFi, 资产流, 权限模型, 预言机/跨链, 多链审计 |
| `coff0xc-compliance-architecture` | `使用 coff0xc-compliance-architecture ...` | 安全架构, 威胁建模, 合规映射, 数据安全, 隐私, 成熟度 |
| `coff0xc-purple-deception` | `使用 coff0xc-purple-deception ...` | 紫队演练, ATT&CK, 检测覆盖, 响应验证, 欺骗防御, 运营改进 |
| `coff0xc-network-protocol-security` | `使用 coff0xc-network-protocol-security ...` | 协议分析, TLS/DNS/HTTP, Packet/pcap, 无线/BLE/RF, 状态机, 形式化建模 |
| `coff0xc-skill-router` | `使用 coff0xc-skill-router ...` | 自治编排, 多 skill 工作流, 任务图, 阶段门禁, 重路由 |

## Troubleshooting

1. Ensure the folder name equals the frontmatter `name`.
2. Restart or refresh the client after copying skills.
3. Remove duplicate skill names across `.codex/skills`, `.agents/skills`, or other scanned locations.
4. Keep trigger terms in frontmatter `description`, not only in the Markdown body.
5. Use `coff0xc-skill-router` when unsure which skill should handle a request or when the task should compose multiple skills; do not use it as a mandatory prelude to every task.
6. If a task is broad, mention the expected deliverable, for example `检测规则`, `OpenAPI`, `draw.io`, `PPTX`, `XLSX`, `测试验证`, `CI 复现`, `设计系统`, `状态门禁`, `浏览器截图`, or `风险清单`.
7. For autonomous composition, include wording such as `你自己判断`, `串联 skill`, `任务图`, `工作流`, `vibe coding`, or `chain the needed skills`.
