---
name: coff0xc-skill-router
description: "Coff0xc autonomous skill router and lightweight multi-skill composer. Use only when the user asks the AI to decide which coffee/coff0xc skills to use, chain skills together, build a task/workflow graph, orchestrate a vibe-coding workflow, handle cross-domain or multi-domain work, or recover from a missing/uncertain skill trigger. It chooses one primary skill, adds only necessary support skills, sequences phases, defines gates, and re-routes as evidence changes. 中文触发：自主编排、多 skill 工作流、AI 自己判断、自动串联 skill、任务图、工作流图、跨领域、跨域、多领域、多维度、编排工作流、vibe coding、不确定用哪个、选择 skill、帮我分流、同时涉及多个领域、串联 skill、工作流编排。 Do not use this router for narrow tasks that already match one specific skill; route directly to that skill."
---

# coff0xc-skill-router

## 能力定位
面向不确定任务和跨领域任务的轻量 autonomous skill composer。它不是把所有能力揉成一个大 skill，也不是普通任务的必经步骤；它只在任务确实需要选择、分流或跨域编排时介入。

单一任务只选一个最具体 skill；复杂任务输出主 skill、辅助 skill、执行顺序、门禁和重路由条件。

## 执行模式优先级
默认是执行模式，不是证明模式。

- 普通任务：不要先输出完整 skill graph；直接选择最具体的主 skill 并开始执行。
- 复杂跨域任务：只给 3-5 行轻量工作流，然后马上进入第一阶段。
- 只有用户明确要求 review、eval、质量测试、发版、推送、CI、benchmark、确认 skill 是否好用时，才启用 release/eval 模式。
- `workflow-trace.json`、golden responses、trigger eval、quality eval 是发版门禁，不是普通任务默认动作。
- Router 是快速分流器，不是强制规划层；能用一个专业 skill 做完，就不要绕进多 skill 编排。

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
作为自动触发兜底入口和多 skill 编排入口。当前端模型没有自动选择具体 Coff0xc skill，或任务明显跨多个领域时，用本路由表快速选择主 skill 和必要支持 skill，然后读取并执行当前阶段对应 skill 的工作流。

## 为什么需要 Router
- 多个客户端只用 `name` 和 `description` 参与触发，正文内容不会帮助首次触发。
- 中文请求、缩写、英文工具名和安全领域黑话容易导致具体 skill 漏触发。
- 真实任务经常不是一个 skill 能完成：开发会牵涉 API、数据、UI、安全、Office 交付或发布验证。
- 合并后的大 skill 数量更少，但每个主题覆盖面更广，需要一个触发词密集的兜底和编排入口。

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

## 路由表
| 目标 skill | 常见别名/来源词 | 触发说明 |
| --- | --- | --- |
| coff0xc-software-engineering | c-cpp-dev, code-simplifier, git-workflow, go-dev, java-dev, js-ts-dev, ... | 全面软件工程、语言开发、测试、重构、脚本、Git 和工程质量工作流。触发：Python、JavaScript、TypeScript、Go、Rust、Java、C/C++、Shell、bugfix、feature、测试、重构、构建、脚本、Git、本地工程化、CI 失败、快速内循环、模块循环、最终审计。 |
| coff0xc-ai-agent-rag | ai-agent-dev, ai-orchestrator, deep-thinking | 全面 AI Agent、RAG、Prompt、LLM 应用、多模型协作、评测、观测和成本控制工作流。触发：Agent、RAG、embedding、向量数据库、Prompt、LangChain、AutoGen、工具调用、多模型编排、代码审计协作、视觉分析、评测、缓存、记忆、失败恢复。 |
| coff0xc-api-data-platform | api-design, database, cli-creator | 全面 API、数据库、数据平台、CLI、SDK 和接口契约工程工作流。触发：REST、GraphQL、OpenAPI、SQL、数据库、迁移、CLI、SDK、分页、认证、错误码、JSON 输出、数据模型、ETL、数据质量。 |
| coff0xc-ui-doc-output | UIdesign, quick-translate | 全面 UI 设计、前端体验、设计系统、报告叙事和技术翻译工作流。触发：UI、前端、dashboard、组件、页面、设计系统、状态门禁、响应式、移动端、浏览器截图、可访问性、反 AI 味、报告、翻译、润色。正式 PPTX/DOCX/PDF/XLSX 文件交付转入 `coff0xc-office-doc-tools`。 |
| coff0xc-office-doc-tools | documents, presentations, spreadsheets, pdf | 全面 Office/PDF 文件型交付工作流。触发：PowerPoint、PPT、PPTX、slides、deck、Word、DOCX、PDF、Excel、XLSX、CSV、spreadsheet、workbook、chart、formula、redline、comments、render、export、演示文稿、幻灯片、文档、表格、工作簿、公式、批注、修订、导出、可编辑文件。 |
| coff0xc-secure-code-appsec | api-discovery, api-security-test, backdoor-detector, browser-security, code-audit, graphql-pentest, ... | 全面代码安全审计、Web/API/GraphQL/OAuth/浏览器/SPA/LLM 安全、后门检测和授权应用安全验证工作流。触发：代码审计、危险函数、source/sink、污点分析、Web 安全、API 安全、GraphQL、OAuth、CSP、CORS、Cookie、Prompt 注入、越权、SSRF、XSS、SQLi、后门、Webshell。 |
| coff0xc-cloud-devsecops | cloud-security, container-security, devsecops, docker-k8s, secrets-management, serverless-security, ... | 全面云安全、容器/Kubernetes、Serverless、DevSecOps、供应链、CI/CD 和密钥管理工作流。触发：AWS、Azure、GCP、IAM、S3/Blob/GCS、Docker、K8s、镜像、Serverless、CI/CD、SAST、DAST、SCA、SBOM、secret scanning、IaC、Terraform、GitHub Actions。 |
| coff0xc-detection-response | detection-engineering, email-security, forensics-analysis, incident-response, malware-analysis, osint, ... | 全面 SOC、安全运营、检测工程、威胁狩猎、威胁情报、邮件安全、恶意软件分析、取证和应急响应工作流。触发：SIEM、Sigma、YARA、IOC、日志、告警、EDR、IR、forensics、malware、phishing、timeline、威胁情报、狩猎、误报。 |
| coff0xc-vulnerability-lifecycle | bug-bounty, pentest-report, red-team-poc, vuln-research, vulnerability-management | 全面漏洞研究、CVE/补丁分析、漏洞管理、风险优先级、报告、授权验证和修复跟踪工作流。触发：CVE、漏洞原理、补丁对比、advisory、CVSS、EPSS、KEV、PoC 验证、漏洞报告、bug bounty、pentest report、修复跟踪。 |
| coff0xc-identity-zero-trust | ad-pentest, credential-access, identity-security, lateral-movement, privilege-escalation, zero-trust | 全面身份安全、零信任、AD/Kerberos、IAM、权限、凭证风险、横向移动防御和访问控制审查工作流。触发：IAM、SSO、MFA、AD、Active Directory、Kerberos、BloodHound、权限、凭证、服务账号、提权、横向移动、Zero Trust、PAM。 |
| coff0xc-authorized-assessment | attack-chain-orchestrator, autoredteam-orchestrator, c2-framework, cdn-bypass, data-exfiltration, evasion-toolkit, ... | 全面授权安全评估、攻击面梳理、红队计划防御化、演练边界、控制有效性验证和报告工作流。触发：recon、fingerprint、attack chain、full pentest、red team、C2、evasion、phishing simulation、post-exploitation、data exfiltration、CDN/WAF、proxy、social engineering、ROE。 |
| coff0xc-binary-mobile-iot | binary-exploit, crypto-security, ctf, ics-scada, iot-security, kernel-security, ... | 全面二进制/逆向/内核/移动/IoT/ICS/CTF/密码学安全分析工作流。触发：reverse engineering、PWN、kernel、APK、IPA、Frida、firmware、UART、JTAG、SPI、SCADA、PLC、Modbus、BLE、RF、CTF、crypto review、constant-time。 |
| coff0xc-blockchain-security | blockchain-security | 全面区块链、智能合约、DeFi、Web3、跨链、代币和多链安全审计工作流。触发：Solidity、EVM、Solana、Cosmos、Substrate、Cairo/StarkNet、TON、Algorand、DeFi、AMM、oracle、bridge、token、NFT、智能合约审计、Foundry、Hardhat、Slither。 |
| coff0xc-compliance-architecture | compliance-audit, data-security, security-architecture | 全面安全架构、威胁建模、合规审计、数据安全、DLP、隐私、安全基线和成熟度评估工作流。触发：安全架构、STRIDE、威胁建模、等保、PCI-DSS、GDPR、ISO27001、SOC2、CIS、NIST、数据分类、脱敏、DLP、隐私、基线、控制矩阵。 |
| coff0xc-purple-deception | honeypot, purple-team | 全面紫队演练、ATT&CK 映射、控制验证、检测能力评估、蜜罐/欺骗防御和安全运营改进工作流。触发：purple team、ATT&CK、红蓝对抗、control validation、detection coverage、emulation plan、honeypot、deception、decoy、canary、检测有效性。 |
| coff0xc-network-protocol-security | network-protocol, wireless-security | 全面网络协议、TLS/DNS/TCP/UDP/QUIC/HTTP、无线/RF/蓝牙、协议日志分析、通信安全和形式化协议建模工作流。触发：network protocol、TLS、DNS、HTTP/2、HTTP/3、QUIC、TCP、UDP、WiFi、Bluetooth、BLE、RF、packet、pcap、Wireshark、协议分析、安全通信、ProVerif、Mermaid protocol。 |

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
