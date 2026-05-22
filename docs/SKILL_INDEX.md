# Skill Index

`coffee-skill` 的入口索引。按“你要交付什么”选 skill，不按关键词硬背。

## 先看这个：快速选择

| 任务形态 | 先用哪个 | 不要先用 |
|---|---|---|
| 一个 repo、一个 bug、一个功能、一个 CI 失败 | `coff0xc-software-engineering` | `coff0xc-skill-router`，除非任务明显跨领域 |
| 一个 UI、前端页面、dashboard、报告表达 | `coff0xc-ui-doc-output` | Office skill，除非交付物是 PPTX/DOCX/XLSX/PDF |
| 一个正式 Office / 文件型交付物 | `coff0xc-office-doc-tools` | UI skill，除非是 web/app 界面 |
| 论文 DOCX + 旧 PPTX 重写答辩 PPT | `coff0xc-office-doc-tools` | 不要先走 router，除非还要改代码/实验/系统 |
| 一个 Agent/RAG/LLM 系统设计 | `coff0xc-ai-agent-rag` | dev skill，除非要求落地到真实仓库 |
| 一个 API、数据库、数据契约问题 | `coff0xc-api-data-platform` | router，除非还涉及 UI/安全/Office |
| 一个授权安全领域问题 | 对应安全 skill | 未授权、生产、凭据或破坏性动作 |
| 多领域混合、不确定入口 | `coff0xc-skill-router` | 手动把所有 skill 全塞进去 |

## 能力地图：产品与工程

| Skill | 什么时候用 | 应该留下什么证据 |
|---|---|---|
| `coff0xc-software-engineering` | 写功能、修 repo、复现 CI、修测试、重构、脚本、full-stack 改动。 | 改动文件、根因、窄验证、必要时加宽验证、lockfile/diff 卫生说明。 |
| `coff0xc-api-data-platform` | REST/GraphQL/OpenAPI、数据库 schema、迁移、CLI/SDK、数据模型、分页、错误码、ETL/数据质量。 | 契约/schema/错误模型、迁移或兼容说明、数据检查、示例或测试。 |
| `coff0xc-ai-agent-rag` | Agent/RAG/LLM 应用、Prompt 工作流、工具调用、记忆、检索、评测、观测、延迟和成本。 | 系统流、检索/引用策略、工具 schema、评测集、失败模式、降级和工程交接。 |
| `coff0xc-ui-doc-output` | 产品 UI、dashboard、admin、设计系统、响应式状态、可访问性、报告结构、技术翻译。 | UI 改动或审查结论、状态覆盖、桌面/移动端或浏览器证据、剩余视觉风险。 |
| `coff0xc-office-doc-tools` | PPTX、DOCX、PDF、XLSX、CSV、公式、图表、批注、修订、正式文件检查。 | 可编辑文件路径、渲染/预览证据、OOXML 或结构检查、公式/格式检查、来源假设。 |
| `coff0xc-research-drawio-diagram` | 把论文、算法、模型结构、代码路径或科研流程画成可编辑 draw.io。 | `.drawio` 文件、节点/边 spec、证据表、来源映射、推断标注。 |

## 能力地图：安全与治理

安全类 skill 只用于自有、本地、实验室、CTF、训练靶场或明确授权资产。生产、凭据、付费服务、远程写入、删除、PR/push、云资源变更和 CI/CD 权限变更都需要明确授权。

| Skill | 什么时候用 | 应该留下什么证据 |
|---|---|---|
| `coff0xc-secure-code-appsec` | 代码/Web/API/GraphQL/OAuth/CSP/CORS/Cookie/Prompt 注入/越权/SSRF/XSS/SQLi/source-sink/后门风险。 | 发现列表、文件/行号或路由、影响、证据、可利用边界、修复、测试和检测/日志建议。 |
| `coff0xc-cloud-devsecops` | 云/IaC/Kubernetes/Docker/serverless/CI/CD/供应链/密钥/SBOM/SCA 风险。 | 风险清单、最小权限和隔离建议、pipeline gate、密钥轮换、验证命令。 |
| `coff0xc-detection-response` | Sigma/YARA/SIEM、威胁狩猎、IOC、IR 时间线、EDR 告警、恶意样本/邮件/日志、误报调优。 | 检测逻辑、字段映射、ATT&CK 映射、测试样例、误报分析和调优建议。 |
| `coff0xc-vulnerability-lifecycle` | CVE、advisory、补丁、可利用性、EPSS/KEV/CVSS、资产影响、修复优先级、漏洞报告。 | 原理、补丁差异、影响范围、业务优先级、缓解措施、owner 和验证计划。 |
| `coff0xc-identity-zero-trust` | IAM、AD/Kerberos、SSO/MFA、BloodHound 路径、服务账号、PAM、session、device posture、权限蔓延。 | 身份路径、权限风险、控制缺口、收敛顺序和加固建议。 |
| `coff0xc-authorized-assessment` | 授权评估、ROE、攻击面梳理、控制验证、红队防御化演练、报告结构。 | 书面范围、允许/禁止动作、阶段、观测点、检测/控制矩阵和报告计划。 |
| `coff0xc-binary-mobile-iot` | 二进制、APK/IPA、固件、IoT/ICS/OT、kernel/mobile、Frida 点、UART/JTAG/SPI、协议解析、密码实现风险。 | 样本结构、入口点、字符串/配置/权限、通信路径、风险假设和验证路线。 |
| `coff0xc-blockchain-security` | Solidity/EVM/Solana/Cosmos/Substrate/Cairo/TON/Algorand、DeFi、AMM、oracle、bridge、token、NFT、资产流和状态机。 | 入口点、资产流、权限/不变量风险、PoC 边界、修复建议和测试覆盖。 |
| `coff0xc-compliance-architecture` | 威胁建模、安全架构、控制映射、数据分类、隐私/DLP、SOC 2/ISO/GDPR/CIS/NIST、上线评审。 | 信任边界、STRIDE/控制矩阵、证据缺口、风险决策和整改计划。 |
| `coff0xc-purple-deception` | ATT&CK 映射、紫队计划、控制验证、检测覆盖、欺骗防御、decoy/canary、SOC 改进。 | 技术映射、日志需求、覆盖矩阵、演练假设和改进 backlog。 |
| `coff0xc-network-protocol-security` | TLS/DNS/HTTP/QUIC/TCP/UDP、pcap/Wireshark、无线/BLE/RF、状态机、安全通信、形式化协议图。 | 协议流程、握手/状态分析、异常字段、安全影响和验证/建模建议。 |

## 常见组合

只有任务真的跨领域，或你不确定入口时，才用 `coff0xc-skill-router`。

| 任务 | 常见组合 |
|---|---|
| Full-stack SaaS 功能 | `software-engineering` + `api-data-platform` + `ui-doc-output` + `secure-code-appsec` |
| Agent/RAG 产品 | `ai-agent-rag` + `api-data-platform` + `software-engineering` + `ui-doc-output` |
| 从代码/数据生成高管交付物 | `office-doc-tools` + `api-data-platform` + `ui-doc-output` + `research-drawio-diagram` |
| 安全发布评审 | `secure-code-appsec` + `cloud-devsecops` + `software-engineering` + `compliance-architecture` |
| 事件响应/检测包 | `detection-response` + `vulnerability-lifecycle` + `cloud-devsecops` + `purple-deception` |
| 协议 / IoT / 二进制研究 | `network-protocol-security` + `binary-mobile-iot` + `research-drawio-diagram` + 可选 `office-doc-tools` |

## 手动触发示例

```text
使用 coff0xc-software-engineering：复现 CI 失败，做最小修复，并跑可用验证。
使用 coff0xc-ui-doc-output：重做这个 dashboard，检查状态、移动端、可访问性和截图证据。
使用 coff0xc-office-doc-tools：把这份大纲做成可编辑 PPTX，并检查渲染、图表和来源。
使用 coff0xc-ai-agent-rag：设计一个带引用、缓存、失败降级和评测集的知识库助手。
使用 coff0xc-secure-code-appsec：审计这个 API 的越权和输入验证风险。
你自己判断要用哪些 coff0xc skills，并把它们串成工作流完成这个功能。
```
