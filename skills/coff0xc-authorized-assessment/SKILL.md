---
name: coff0xc-authorized-assessment
description: "Use when / 当用户请求: 全面授权安全评估、攻击面梳理、红队计划防御化、演练边界、控制有效性验证和报告工作流。触发：recon、fingerprint、attack chain、full pentest、red team、C2、evasion、phishing simulation、post-exploitation、data exfiltration、CDN/WAF、proxy、social engineering、ROE、书面授权、完整入侵链、防护发现、边界和步骤、防御验证。 Covered source aliases / 来源别名: attack-chain-orchestrator, autoredteam-orchestrator, c2-framework, cdn-bypass, data-exfiltration, evasion-toolkit, fingerprint-engine, full-pentest, phishing-simulation, post-exploitation, proxy-pool-manager, recon-workflow, red-team-infra, security-tool-dev, social-engineering. Capability domains / 能力域: ROE/授权, 攻击面梳理, 控制验证, 红队防御化, 钓鱼演练, 外传演练, 工具开发, 报告. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-authorized-assessment."
---

# coff0xc-authorized-assessment

## 目标
将高风险红队/攻击链请求转化为授权范围内的控制验证、检测覆盖、加固建议和报告，不输出可滥用攻击步骤。

## 适用场景
- 制定授权评估计划、ROE、测试矩阵、控制验证、检测覆盖、报告模板。
- 把 recon、红队、钓鱼演练、外传演练、C2 基础设施等请求转成防御化方案。
- 评估组织安全控制、人员流程、日志覆盖和响应能力。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-authorized-assessment ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 不提供真实绕过、钓鱼投递、C2 搭建、持久化、凭证获取、外传或规避检测步骤。
- 无授权或范围不清时只给准备清单和授权模板。
- 不指导针对具体第三方目标的攻击链执行。

## 执行原则
- 先读取项目文件、配置、调用点、现有风格和可用工具，再下结论或改文件。
- 把用户目标转成可验证的完成标准；不确定但低风险的细节记录为假设并继续推进。
- 涉及当前事实、版本、CVE、云服务、GitHub 状态、价格、外部 API 或论文时，查真实来源并标注证据等级。
- 涉及代码改动时保持最小正确改动，优先使用现有框架、脚本、测试和本地工具。
- 只有真实运行过的命令、测试、构建、扫描或人工检查才能写成已验证。
- 涉及删除、远程写入、生产、凭据、付费、push、PR/Issue、CI/CD、权限或基础设施变更时，先拿到明确授权。

## 安全边界
- 只处理自有资产、明确授权资产、实验室、CTF、靶场、日志、配置、样本、代码审计、防御建设和报告写作。
- 真实第三方目标上不提供漏洞利用、凭证获取、持久化、规避检测、C2、钓鱼收集、数据外传、破坏或未授权访问步骤。
- 高风险请求默认转为防御输出：授权边界、风险解释、检测思路、日志查询、规则草案、加固方案、验证清单和报告结构。
- 主动联网扫描、云账号检查、目录/租户查询或生产环境动作前，确认目标范围、速率、时间窗口、禁止动作和回滚方式。
- 发现密钥、个人信息、样本敏感数据或客户数据时，只报告类型、位置和处置建议，不复述完整秘密值。

## 能力矩阵
| 能力域 | 覆盖范围 | 执行要点 |
| --- | --- | --- |
| ROE/授权 | 目标、范围、时间窗、速率、禁止动作、联系人、停止条件 | 评估合法可控。 |
| 攻击面梳理 | 资产清单、域名、云暴露、证书、技术栈、第三方入口 | 只做授权/公开信息范围。 |
| 控制验证 | 预防、检测、响应、恢复、人员流程、日志覆盖 | 把技术映射到控制目标。 |
| 红队防御化 | 场景、假设、遥测、期望告警、蓝队动作 | 不输出攻击细节。 |
| 钓鱼演练 | 培训目标、审批、模板风险、收件范围、隐私和复盘 | 不收集真实凭据。 |
| 外传演练 | DLP/egress 控制、日志字段、审批和安全样本 | 不外传真实数据。 |
| 工具开发 | 防御测试工具、检测验证工具、报告自动化 | 不做隐蔽或规避型工具。 |
| 报告 | 执行摘要、范围、发现、证据、控制差距、改进路线 | 面向管理层和工程。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| recon-workflow | 授权资产发现、公开信息整理和边界确认。 |
| fingerprint-engine | 技术栈/服务指纹的防御性资产识别。 |
| full-pentest | 端到端授权评估计划和报告。 |
| attack-chain-orchestrator | 攻击链转控制验证矩阵。 |
| autoredteam-orchestrator | 自动化演练规划和安全门禁。 |
| red-team-infra | 演练基础设施需求、隔离和日志，不给 C2 实施。 |
| c2-framework | C2 风险、检测和隔离建议，不搭建或操作。 |
| evasion-toolkit | 规避风险教育、检测覆盖和硬化，不给绕过技术。 |
| cdn-bypass | 边界暴露风险和 WAF/CDN 配置检查。 |
| proxy-pool-manager | 代理/出口合规、日志和风控建议。 |
| phishing-simulation | 合规钓鱼演练计划和隐私保护。 |
| social-engineering | 人员风险培训、审批和安全演练边界。 |
| post-exploitation | 入侵后控制检查、日志覆盖和遏制计划。 |
| data-exfiltration | DLP/egress 防御验证和安全样本方案。 |
| security-tool-dev | 防御工具、验证脚本和报告自动化。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 硬门禁 | 先确认书面授权、ROE、目标、禁止动作、时间窗和联系人。 | 范围明确。 |
| 场景设计 | 用业务风险定义场景，而不是追求攻击技巧。 | 控制目标清楚。 |
| 遥测计划 | 列预期日志、告警、字段、响应动作和成功/失败判据。 | 能验证控制。 |
| 安全执行方案 | 使用非破坏、低风险、可回滚、可观测的模拟方式。 | 不伤害系统。 |
| 证据收集 | 记录时间线、截图、日志、配置和响应动作。 | 报告有证据。 |
| 复盘改进 | 按检测、响应、流程、技术债和培训输出改进路线。 | 演练闭环。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 没有授权、ROE 或联系人时停止执行，只输出准备清单。
- 任何可能影响真实用户、生产系统、外部目标或邮件收件人的动作必须确认。
- 不生成或保存可直接复用的攻击 payload、C2 配置、钓鱼收集页面或规避脚本。

## 验证清单
- 授权文档、目标清单、时间窗和沟通渠道存在。
- 每个场景有预期检测和实际检测对比。
- 每个控制差距有证据、影响和改进建议。
- 演练后确认系统恢复和数据未泄露。

## 反模式
- 把红队技能清单当评估计划。
- 范围不清就开始 recon 或测试。
- 只展示成功路径，不评估检测和响应。
- 用真实敏感数据做外传或钓鱼演练。

## 合并来源
- `attack-chain-orchestrator`
- `autoredteam-orchestrator`
- `c2-framework`
- `cdn-bypass`
- `data-exfiltration`
- `evasion-toolkit`
- `fingerprint-engine`
- `full-pentest`
- `phishing-simulation`
- `post-exploitation`
- `proxy-pool-manager`
- `recon-workflow`
- `red-team-infra`
- `security-tool-dev`
- `social-engineering`

## 本机相近 Skill
- `source-command-purple-team`
- `secure-workflow-guide`
- `audit-prep-assistant`

## 输出合同
```markdown
完成：
- ...

证据：
- [已验证/高可信/推断/未验证/未知] ...

行动：
- ...

验证：
- ...

剩余风险：
- ...

下一步：
- ...
```
