---
name: coff0xc-detection-response
description: "Use when / 当用户请求: 全面 SOC、安全运营、检测工程、威胁狩猎、威胁情报、邮件安全、恶意软件分析、取证和应急响应工作流。触发：SIEM、Sigma、YARA、Sigma/YARA、IOC、日志、告警、EDR、IR、forensics、malware、phishing、timeline、detection response、incident response、incident、威胁情报、狩猎、误报、安全告警太吵、安全告警、检测响应、事故响应、检测逻辑、降误报、验证样本、alert tuning。 Covered source aliases / 来源别名: detection-engineering, email-security, forensics-analysis, incident-response, malware-analysis, osint, soc-operations, threat-hunting, threat-intelligence. Capability domains / 能力域: 检测工程, SOC 运营, 威胁狩猎, 威胁情报, 邮件安全, 取证分析, 恶意软件分析, 应急响应. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-detection-response."
---

# coff0xc-detection-response

## 能力定位
面向 SOC、检测工程、威胁狩猎、取证和应急响应的防御运营能力。它把日志、样本线索和告警问题转成可验证检测、时间线和响应建议。

## 能交付什么
- Sigma/YARA/查询规则草案和字段映射
- IOC、时间线、攻击阶段和 ATT&CK 映射
- 误报分析、测试样例和调优建议
- 应急处置、取证保全和复盘改进清单

## 可以接收什么输入
- EDR/SIEM/云日志、告警、IOC、样本摘要
- 取证笔记、邮件头、网络流量摘要、事件时间线
- 已有 Sigma/YARA/查询规则和误报反馈

## 放心使用的边界
- 只做防御检测、应急、取证和报告
- 不提供未授权攻击、持久化、规避检测或恶意样本投递步骤
- 处理真实日志时避免泄露个人信息和敏感资产细节
- 安全类能力默认只用于授权、防御、检测、加固、验证和报告；不提供未授权攻击、凭据窃取、持久化、规避检测、C2、钓鱼收集、数据外传或破坏性步骤。

## 为什么可以放心
- 检测规则必须说明数据源、字段、测试样例和误报风险
- IR 输出区分已观测事实和推断
- 优先给可执行的处置和验证步骤

## 典型使用方式
```text
使用 coff0xc-detection-response 根据这些 EDR 日志写 Sigma 和 YARA 检测规则。
使用 coff0xc-detection-response 做一次威胁狩猎假设、日志查询和告警调优。
Use coff0xc-detection-response to build an incident timeline from these forensics notes.
```


## 目标
把告警、日志、样本、IOC 和情报转成可验证的检测、处置和复盘结果；事实、推断和未知必须分开。

## 适用场景
- 编写或评审 Sigma/YARA/SIEM 查询、检测逻辑、狩猎假设和告警处置流程。
- 分析邮件头、IOC、日志、EDR 告警、内存/磁盘取证结果、恶意样本元数据。
- 制定应急响应计划、时间线、影响范围、遏制恢复和复盘改进。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-detection-response ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 不要运行未知恶意样本或提供规避检测/持久化技巧。
- OSINT 不做骚扰、钓鱼、账号接管或隐私侵犯。
- 不把情报传闻当已确认入侵事实。

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
| 检测工程 | Sigma、YARA、SIEM query、EDR logic、field mapping、FP tuning | 规则含数据源和测试样例。 |
| SOC 运营 | 告警分级、triage、升级、case notes、SLA、runbook | 处置路径清楚。 |
| 威胁狩猎 | 假设、ATT&CK 技术、遥测、查询、结果解释 | 区分命中和未命中意义。 |
| 威胁情报 | IOC、TTP、来源可靠性、时效、关联和可操作性 | 标注证据等级。 |
| 邮件安全 | headers、SPF/DKIM/DMARC、URL、附件、投递链 | 保留证据链。 |
| 取证分析 | timeline、文件、进程、网络、用户、持久化位置 | 记录来源和时间区。 |
| 恶意软件分析 | 静态元数据、字符串、行为假设、沙箱报告、家族关联 | 不执行危险样本。 |
| 应急响应 | 准备、识别、遏制、根除、恢复、监控、复盘 | 每步有负责人和验证。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| detection-engineering | 规则编写、日志字段、误报压降和测试。 |
| soc-operations | 告警 triage、case 流程和运营指标。 |
| threat-hunting | 狩猎假设、查询和 ATT&CK 映射。 |
| threat-intelligence | 情报源评估、IOC/TTP 关联和时效判断。 |
| email-security | 钓鱼邮件分析、认证记录和附件/URL 风险。 |
| forensics-analysis | 主机/磁盘/日志时间线和证据链。 |
| malware-analysis | 静态/沙箱安全分析和 YARA 方向。 |
| incident-response | IR 指挥、遏制、恢复和复盘。 |
| osint | 公开信息收集、归因假设和来源可信度。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 证据接收 | 记录数据源、时间窗、时区、主机、用户、样本哈希、日志字段。 | 证据可追溯。 |
| 事实分层 | 分开已确认事实、强关联、弱假设、未知和需要补数项。 | 不夸大结论。 |
| 分析路径 | 按 kill chain/ATT&CK/时间线/资产影响组织调查。 | 知道下一条查询查什么。 |
| 检测产物 | 生成查询/规则、字段映射、测试数据、FP 条件和部署注意。 | 能上线验证。 |
| 处置计划 | 遏制、根除、恢复、监控、沟通和复盘。 | 业务和安全都可执行。 |
| 闭环验证 | 确认告警下降、风险清除、日志覆盖和补救完成。 | 事件可关闭。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 运行样本、连接可疑基础设施、查询真实用户隐私数据前必须确认。
- 对外归因、公开披露、通知客户或执法相关输出必须保持证据等级。
- 规则部署到生产 SIEM/EDR 前需要变更审批和回滚。

## 验证清单
- 规则：正样例、负样例、字段存在性、时间窗、性能和误报样本。
- IR：每个处置动作有日志或配置证据。
- 情报：来源、发布时间、相关性、过期状态。
- 取证：hash、时间线一致性、证据保全路径。

## 反模式
- 把 IOC 命中直接等同于入侵成功。
- 规则没有数据源字段说明。
- 只给处置建议不说明如何验证完成。
- 把第三方情报原文当事实复述。

## 合并来源
- `detection-engineering`
- `email-security`
- `forensics-analysis`
- `incident-response`
- `malware-analysis`
- `osint`
- `soc-operations`
- `threat-hunting`
- `threat-intelligence`

## 本机相近 Skill
- `yara-rule-authoring`
- `sarif-parsing`
- `source-command-vuln-research`

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
