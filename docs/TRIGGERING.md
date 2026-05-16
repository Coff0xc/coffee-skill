# Triggering Guide

## Why Skills Sometimes Do Not Auto-Trigger

Most clients select skills from frontmatter metadata, especially `name` and `description`. The body of `SKILL.md` is usually loaded only after the skill has already triggered, so trigger words and capability terms must be in `description`.

## Trigger Strategy In This Pack

- Each capability skill starts with broad Chinese/English capability terms.
- Descriptions include concrete deliverables, domain nouns, tool names, acronyms, and source aliases.
- Each skill body includes capability positioning, inputs, deliverables, boundaries, trust reasons, and examples.
- `coff0xc-skill-router` is the fallback when the user is unsure or auto-triggering misses.

## Manual Invocation

Use one of these phrases when auto-triggering misses:

| Skill | Manual phrase | Capability cues |
|---|---|---|
| `coff0xc-software-engineering` | `使用 coff0xc-software-engineering ...` | 自主开发, 代码修复, 功能实现, 测试验证, 构建质量, Git 协作 |
| `coff0xc-ai-agent-rag` | `使用 coff0xc-ai-agent-rag ...` | Agent 架构, RAG 管线, 工具调用, 记忆系统, Prompt 工程, 评测观测 |
| `coff0xc-api-data-platform` | `使用 coff0xc-api-data-platform ...` | API 契约, 数据模型, 认证授权, CLI/SDK, 数据质量, 兼容演进 |
| `coff0xc-ui-doc-output` | `使用 coff0xc-ui-doc-output ...` | 产品 UI, 交互状态, 视觉验证, 报告输出, 翻译润色 |
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
| `coff0xc-skill-router` | `使用 coff0xc-skill-router ...` | 技能分诊, 兜底触发, 候选对比, 安全门禁, 手动调用 |

## Troubleshooting

1. Ensure the folder name equals the frontmatter `name`.
2. Restart or refresh the client after copying skills.
3. Remove duplicate skill names across `.codex/skills`, `.agents/skills`, or other scanned locations.
4. Keep trigger terms in frontmatter `description`, not only in the Markdown body.
5. Use `coff0xc-skill-router` when unsure which skill should handle a request.
6. If a task is broad, mention the expected deliverable, for example `检测规则`, `OpenAPI`, `draw.io`, `PPTX`, `XLSX`, `测试验证`, or `风险清单`.
