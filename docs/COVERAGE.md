# Coverage

## Summary

- Release skills: 18
- Source skills consolidated: 91
- Comprehensive capability skills: 17
- Router/fallback skills: 1
- Trigger eval cases: 117
- Quality eval fixtures: 5 real-artifact cases with 40 assertions
- Office OOXML quality gates: PPTX package/slide/chart parsing, XLSX workbook/formula/table/chart parsing, DOCX comments/redlines/styles/numbering/rels/table geometry parsing

## Skill Capability Map

| Release skill | Core capability | Typical deliverables | Trust boundary |
|---|---|---|---|
| `coff0xc-software-engineering` | 面向真实仓库的工程交付能力。适合把模糊需求变成可运行代码、可复现修复、可验证测试结果和清晰 diff 摘要；强调先读仓库规则、需求包、快速内循环、模块循环、CI 复现、最终审计和 diff 卫生。 | 代码补丁、脚本或配置修改; 失败原因和根因链路说明; 单元/集成/构建验证结果; CI/回归分诊和剩余风险 | 本地可逆优先 |
| `coff0xc-ai-agent-rag` | 面向 AI Agent、RAG 和 LLM 应用的系统设计与落地能力。它把“写 Prompt”升级为数据、工具、检索、评测、观测和成本一起管理的工程系统。 | Agent/RAG 架构方案和数据流; 工具 schema、记忆/缓存策略、检索和引用策略; 评测集、失败用例和质量指标 | 本地可逆优先 |
| `coff0xc-api-data-platform` | 面向 API、数据库、CLI/SDK 和数据契约的工程能力。目标是让接口可使用、可演进、可测试，数据链路可迁移、可追踪、可恢复。 | REST/GraphQL/OpenAPI 契约; 数据库 schema、迁移和数据一致性建议; CLI/SDK 命令设计、JSON 输出和错误模型 | 本地可逆优先 |
| `coff0xc-ui-doc-output` | 面向 UI、前端体验、设计系统、报告表达和技术翻译交付的产物质量能力。它要求产品类型路由、设计系统遵循、组件状态覆盖、可访问性、反 AI 味视觉门禁和浏览器截图验收。 | 可用 UI/组件/页面改动或设计建议; 设计系统/tokens/variants 建议; 桌面/移动端截图或浏览器 smoke 结果; 报告结构、交付文案和翻译润色稿 | 本地可逆优先 |
| `coff0xc-office-doc-tools` | 面向 PowerPoint、Word、PDF、Excel/CSV 这类正式文件交付的 Office 文档工具能力。重点是交付可打开、可编辑、可审阅、可验证的文件。 | 可编辑 PPTX、DOCX、PDF、XLSX/CSV; 图表、批注/修订、公式检查; 渲染截图/预览 QA 和文件路径 | 本地可逆优先 |
| `coff0xc-research-drawio-diagram` | 面向论文、算法、模型和研究流程的可编辑 draw.io 图生成能力。重点是交付可继续编辑的 `.drawio` 源文件，并把图中元素和公开证据对应起来。 | 可编辑 `.drawio` 文件; 图结构 JSON/spec 或模块清单; 证据表：论文段落、公式、图号、代码路径、官方文档 | 本地可逆优先 |
| `coff0xc-secure-code-appsec` | 面向代码和应用安全的证据化审计能力。它把源码、路由、配置、扫描结果和日志转成可验证发现、修复建议和回归检查。 | 安全发现列表：位置、影响、证据、复现条件; source/sink 或权限链路说明; 修复建议、测试用例、检测/日志建议 | 授权/防御优先 |
| `coff0xc-cloud-devsecops` | 面向云原生、容器、CI/CD、供应链和密钥治理的只读优先评估能力。目标是让风险有证据、修复可落地、验证可复现。 | 云/IaC/K8s/CI/CD 风险清单; 最小权限、网络隔离、pipeline gate 和密钥轮换建议; SBOM/SCA/secret scanning 策略 | 授权/防御优先 |
| `coff0xc-detection-response` | 面向 SOC、检测工程、威胁狩猎、取证和应急响应的防御运营能力。它把日志、样本线索和告警问题转成可验证检测、时间线和响应建议。 | Sigma/YARA/查询规则草案和字段映射; IOC、时间线、攻击阶段和 ATT&CK 映射; 误报分析、测试样例和调优建议 | 授权/防御优先 |
| `coff0xc-vulnerability-lifecycle` | 面向漏洞全生命周期的研究、影响评估、优先级和修复跟踪能力。它把 CVE、补丁、PoC、资产信息和业务影响转成可执行修复计划。 | 漏洞原理和补丁差异摘要; 受影响范围、CVSS/EPSS/KEV 和业务优先级; 授权验证计划、缓解措施和修复 owner | 授权/防御优先 |
| `coff0xc-identity-zero-trust` | 面向身份、访问控制、AD/Kerberos、IAM 和零信任治理的权限风险评估能力。它帮助回答“谁能访问什么、为什么、风险在哪里、如何收敛”。 | 身份/权限风险清单和路径说明; MFA/SSO/session/device posture 评估; AD/Kerberos/IAM 横向移动和特权账号防御建议 | 授权/防御优先 |
| `coff0xc-authorized-assessment` | 面向授权安全评估和红队到防御映射的规划能力。它把评估范围、ROE、攻击面、控制验证和报告结构组织成可批准、可执行、可复盘的方案。 | 授权范围和 ROE 草案; 攻击面清单、测试阶段和禁止动作; 控制验证矩阵、检测覆盖和演练观测点 | 授权/防御优先 |
| `coff0xc-binary-mobile-iot` | 面向二进制、移动、IoT/ICS、固件和密码实现的逆向分析能力。它把样本、固件、APK、协议和调试线索转成结构化理解、风险点和验证路线。 | 样本/固件结构和入口点分析; 字符串、配置、权限、通信和硬件接口线索; 内存安全、加密实现、协议解析或移动风险发现 | 授权/防御优先 |
| `coff0xc-blockchain-security` | 面向区块链、智能合约、DeFi 和多链项目的安全审计能力。重点是资金流、权限、状态转换、预言机、跨链和测试覆盖。 | 合约入口点和权限模型清单; 资产流、状态机、价格来源和外部调用风险; 漏洞发现、影响、PoC 思路和修复建议 | 授权/防御优先 |
| `coff0xc-compliance-architecture` | 面向安全架构、威胁建模、合规映射、数据安全和成熟度评估的治理能力。它把系统设计、控制要求和审计证据整理成能落地的风险决策材料。 | 架构风险评审和信任边界图; STRIDE/威胁建模、控制矩阵和差距分析; 数据分类、隐私、DLP 和日志审计建议 | 授权/防御优先 |
| `coff0xc-purple-deception` | 面向紫队、ATT&CK 映射、检测覆盖验证和欺骗防御的安全运营改进能力。它把攻击行为语言翻译成可观测、可检测、可改进的防御能力。 | ATT&CK 技术映射和演练假设; 检测覆盖矩阵、日志需求和响应验证点; 蜜罐/诱饵/canary 设计建议 | 授权/防御优先 |
| `coff0xc-network-protocol-security` | 面向网络协议、TLS/DNS/QUIC/HTTP、无线通信、抓包和形式化建模的协议安全分析能力。它把通信证据转成流程图、风险点和验证建议。 | 协议流程、握手和状态机说明; pcap/日志字段分析、异常字段和安全影响; TLS/PKI/DNS/HTTP/QUIC/无线风险清单 | 授权/防御优先 |
| `coff0xc-skill-router` | 面向不确定任务的 skill 分诊能力。它不是替代专业 skill，而是在用户不知道该用哪个能力时先判断主题、风险和下一步入口。 | 推荐 skill 和理由; 候选 skill 对比和适用边界; 需要澄清的最少问题 | 授权/防御优先 |

## Source Skill Coverage

| Release skill | Source skills | Capability domains |
|---|---|---|
| `coff0xc-software-engineering` | `c-cpp-dev`, `code-simplifier`, `git-workflow`, `go-dev`, `java-dev`, `js-ts-dev`, `python-dev`, `rust-dev`, `shell-scripting`, `testing` | 自主开发, 代码修复, 功能实现, 测试验证, CI 分诊, 快速内循环, 构建质量, Git 协作 |
| `coff0xc-ai-agent-rag` | `ai-agent-dev`, `ai-orchestrator`, `deep-thinking` | Agent 架构, RAG 管线, 工具调用, 记忆系统, Prompt 工程, 评测观测 |
| `coff0xc-api-data-platform` | `api-design`, `database`, `cli-creator` | API 契约, 数据模型, 认证授权, CLI/SDK, 数据质量, 兼容演进 |
| `coff0xc-ui-doc-output` | `UIdesign`, `quick-translate` | 产品 UI, 设计系统, 组件架构, 交互状态, 视觉验收, 报告输出, 翻译润色 |
| `coff0xc-office-doc-tools` | `documents`, `presentations`, `spreadsheets`, `pdf` | PPT/PPTX, DOCX/Word, PDF, Excel/XLSX, CSV/表格, 渲染验证 |
| `coff0xc-research-drawio-diagram` | `new workflow` | 科研绘图, 论文方法图, 模型结构图, draw.io, 证据表, 推断标注 |
| `coff0xc-secure-code-appsec` | `api-discovery`, `api-security-test`, `backdoor-detector`, `browser-security`, `code-audit`, `graphql-pentest`, `llm-red-teaming`, `oauth-security`, `spa-pentest`, `web-pentest` | 代码审计, Source/Sink, 认证授权, Web/API 安全, GraphQL/OAuth, 后门检测 |
| `coff0xc-cloud-devsecops` | `cloud-security`, `container-security`, `devsecops`, `docker-k8s`, `secrets-management`, `serverless-security`, `supply-chain-security` | 云配置, 容器镜像, Kubernetes, CI/CD, 供应链, 密钥管理 |
| `coff0xc-detection-response` | `detection-engineering`, `email-security`, `forensics-analysis`, `incident-response`, `malware-analysis`, `osint`, `soc-operations`, `threat-hunting`, `threat-intelligence` | 检测工程, 威胁狩猎, SIEM/SOC, YARA/Sigma, 应急响应, 取证分析 |
| `coff0xc-vulnerability-lifecycle` | `bug-bounty`, `pentest-report`, `red-team-poc`, `vuln-research`, `vulnerability-management` | CVE 研究, 补丁分析, 影响评估, 优先级, 授权验证, 修复跟踪 |
| `coff0xc-identity-zero-trust` | `ad-pentest`, `credential-access`, `identity-security`, `lateral-movement`, `privilege-escalation`, `zero-trust` | 身份治理, AD/Kerberos, IAM, 凭证风险, 横向移动防御, 零信任 |
| `coff0xc-authorized-assessment` | `attack-chain-orchestrator`, `autoredteam-orchestrator`, `c2-framework`, `cdn-bypass`, `data-exfiltration`, `evasion-toolkit`, `fingerprint-engine`, `full-pentest`, `phishing-simulation`, `post-exploitation`, `proxy-pool-manager`, `recon-workflow`, `red-team-infra`, `security-tool-dev`, `social-engineering` | 授权范围, ROE, 攻击面, 控制验证, 红队防御化, 报告 |
| `coff0xc-binary-mobile-iot` | `binary-exploit`, `crypto-security`, `ctf`, `ics-scada`, `iot-security`, `kernel-security`, `mobile-security`, `reverse-engineering` | 逆向分析, 移动安全, IoT 固件, ICS/OT, 密码实现, 崩溃/漏洞线索 |
| `coff0xc-blockchain-security` | `blockchain-security` | 智能合约, DeFi, 资产流, 权限模型, 预言机/跨链, 多链审计 |
| `coff0xc-compliance-architecture` | `compliance-audit`, `data-security`, `security-architecture` | 安全架构, 威胁建模, 合规映射, 数据安全, 隐私, 成熟度 |
| `coff0xc-purple-deception` | `honeypot`, `purple-team` | 紫队演练, ATT&CK, 检测覆盖, 响应验证, 欺骗防御, 运营改进 |
| `coff0xc-network-protocol-security` | `network-protocol`, `wireless-security` | 协议分析, TLS/DNS/HTTP, Packet/pcap, 无线/BLE/RF, 状态机, 形式化建模 |
| `coff0xc-skill-router` | - | 技能分诊, 兜底触发, 候选对比, 安全门禁, 手动调用 |
