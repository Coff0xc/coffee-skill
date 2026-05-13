---
name: coff0xc-skill-router
description: "Coff0xc skill router and auto-trigger fallback. Use when a user asks for any Coff0xc capability, asks which coffee/coff0xc skill to use, says they are unsure, or when a specific skill does not auto-trigger. Routes Chinese/English requests for: software engineering, Python, JavaScript, TypeScript, Go, Rust, Java, C/C++, Shell, testing, Git, Agent, RAG, LLM, Prompt, API, database, CLI, UI, PDF, document, translation, research diagram, draw.io, diagrams.net, paper figure, algorithm architecture, code audit, Web security, API security, GraphQL, OAuth, cloud, AWS, Azure, GCP, Docker, Kubernetes, CI/CD, supply chain, secret scanning, SOC, SIEM, YARA, Sigma, incident response, malware, forensics, CVE, vulnerability management, AD, Kerberos, IAM, Zero Trust, red team, authorized assessment, reverse engineering, binary, mobile, APK, firmware, IoT, ICS, blockchain, smart contract, compliance, threat modeling, purple team, honeypot, TLS, DNS, network protocol, wireless. 中文触发：代码、开发、测试、重构、脚本、Agent、智能体、RAG、向量数据库、提示词、接口、数据库、命令行、前端、界面、PDF、文档、翻译、科研绘图、论文配图、算法架构图、模型结构图、draw.io、diagrams.net、代码审计、Web安全、云安全、容器、K8s、供应链、密钥、检测、应急、取证、漏洞、CVE、AD域、身份、零信任、红队、授权评估、逆向、二进制、移动安全、固件、工控、区块链、合约审计、合规、威胁建模、紫队、蜜罐、网络协议、无线安全、不确定用哪个、选择 skill、帮我分流、同时涉及多个领域。"
---

# coff0xc-skill-router

## 目标
作为自动触发兜底入口。当前端模型没有自动选择具体 Coff0xc skill 时，先用本路由表判断主题，再读取或按对应 skill 的工作流执行。

## 为什么需要 Router
- 多个客户端只用 `name` 和 `description` 参与触发，正文内容不会帮助首次触发。
- 中文请求、缩写、英文工具名和安全领域黑话容易导致具体 skill 漏触发。
- 合并后的大 skill 数量更少，但每个主题覆盖面更广，需要一个触发词密集的兜底入口。

## 路由规则
1. 如果另一个更具体的 Coff0xc skill 已经触发，优先执行具体 skill，本 router 只用于确认覆盖和边界。
2. 如果只有本 router 触发，按下表选择最匹配的 skill；若本地文件可读，读取该 skill 的 `SKILL.md` 后执行。
3. 如果请求涉及安全、生产、凭据、远程写入、删除或付费动作，先套用目标 skill 的硬门禁。
4. 如果无法确定路由，给出 2-3 个候选 skill 和最小澄清问题；不要凭空执行高风险动作。

## 路由表
| 目标 skill | 常见别名/来源词 | 触发说明 |
| --- | --- | --- |
| coff0xc-software-engineering | c-cpp-dev, code-simplifier, git-workflow, go-dev, java-dev, js-ts-dev, ... | 全面软件工程、语言开发、测试、重构、脚本、Git 和工程质量工作流。触发：Python、JavaScript、TypeScript、Go、Rust、Java、C/C++、Shell、bugfix、feature、测试、重构、构建、脚本、Git、本地工程化。 |
| coff0xc-ai-agent-rag | ai-agent-dev, ai-orchestrator, deep-thinking | 全面 AI Agent、RAG、Prompt、LLM 应用、多模型协作、评测、观测和成本控制工作流。触发：Agent、RAG、embedding、向量数据库、Prompt、LangChain、AutoGen、工具调用、多模型编排、代码审计协作、视觉分析、评测、缓存、记忆、失败恢复。 |
| coff0xc-api-data-platform | api-design, database, cli-creator | 全面 API、数据库、数据平台、CLI、SDK 和接口契约工程工作流。触发：REST、GraphQL、OpenAPI、SQL、数据库、迁移、CLI、SDK、分页、认证、错误码、JSON 输出、数据模型、ETL、数据质量。 |
| coff0xc-ui-doc-output | UIdesign, pdf, quick-translate | 全面 UI 设计、前端体验、PDF/文档处理、报告交付和技术翻译工作流。触发：UI、前端、dashboard、组件、页面、视觉验证、PDF、Word、文档、报告、翻译、润色、截图、版式、可访问性。 |
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
按 coff0xc-detection-response 写 Sigma/YARA 检测
用 coff0xc-skill-router 帮我选择合适 skill
```

## 触发排障
- skill 目录名必须和 frontmatter `name` 一致。
- 安装或替换后需要重启/刷新客户端，让 skill 列表重新索引。
- frontmatter 只保留 `name` 和 `description` 最稳；触发词必须写进 `description`。
- 同名 skill 分布在多个目录时可能抢占触发，保留一份主版本。
- 太短或只写抽象能力的 description 容易漏触发；应包含中文、英文、工具名、任务名和常见缩写。
