# Installed Skill Inventory

This is a local metadata inventory used to organize the wider skill environment around `coffee-skill`.
It does not redistribute raw external, system, or plugin skill bodies.

## Summary

- Snapshot date: `2026-05-22`
- Skill files indexed: `136`
- Unique skill names: `115`
- Duplicate names: `21`
- Runtime release policy: only `coffee-release` skills are published as Coff0xc runtime skill bodies; all other sources are metadata-only.

## Sources

| Source | Count | Policy | Meaning |
|---|---:|---|---|
| `agents-user` | 86 | `metadata-only` | User-installed agent skills. |
| `codex-system` | 5 | `metadata-only` | Codex system skills. |
| `codex-user` | 21 | `metadata-only` | User-installed Codex skills. |
| `coffee-release` | 18 | `redistributed-curated` | Curated skills in this repository. |
| `plugin-bundled` | 3 | `metadata-only` | Bundled plugin skills. |
| `plugin-runtime` | 3 | `metadata-only` | Primary runtime plugin skills. |

## Duplicate Names

| Name | Sources |
|---|---|
| `Chrome` | 2 instance(s): `plugin-bundled` |
| `UIdesign` | 2 instance(s): `agents-user`, `codex-user` |
| `coff0xc-ai-agent-rag` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-api-data-platform` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-authorized-assessment` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-binary-mobile-iot` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-blockchain-security` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-cloud-devsecops` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-compliance-architecture` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-detection-response` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-identity-zero-trust` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-network-protocol-security` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-office-doc-tools` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-purple-deception` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-research-drawio-diagram` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-secure-code-appsec` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-skill-router` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-software-engineering` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-ui-doc-output` | 2 instance(s): `codex-user`, `coffee-release` |
| `coff0xc-vulnerability-lifecycle` | 2 instance(s): `codex-user`, `coffee-release` |
| `skill-creator` | 2 instance(s): `agents-user`, `codex-system` |

## Consolidation Map

This map shows where installed skills naturally fit in the Coff0xc 18-skill model. `supporting-tooling` means the skill is useful for maintenance, creation, or installation but is not one of the runtime capability domains.

| Coff0xc target | Count |
|---|---:|
| `coff0xc-ai-agent-rag` | 5 |
| `coff0xc-api-data-platform` | 5 |
| `coff0xc-authorized-assessment` | 3 |
| `coff0xc-binary-mobile-iot` | 6 |
| `coff0xc-blockchain-security` | 12 |
| `coff0xc-cloud-devsecops` | 8 |
| `coff0xc-compliance-architecture` | 2 |
| `coff0xc-detection-response` | 4 |
| `coff0xc-identity-zero-trust` | 2 |
| `coff0xc-network-protocol-security` | 5 |
| `coff0xc-office-doc-tools` | 4 |
| `coff0xc-purple-deception` | 3 |
| `coff0xc-research-drawio-diagram` | 4 |
| `coff0xc-secure-code-appsec` | 11 |
| `coff0xc-skill-router` | 2 |
| `coff0xc-software-engineering` | 36 |
| `coff0xc-ui-doc-output` | 8 |
| `coff0xc-vulnerability-lifecycle` | 3 |
| `supporting-tooling` | 13 |

## Inventory

### agents-user

| Skill | Mapped target | Risk | Notes |
|---|---|---|---|
| `address-sanitizer` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `aflpp` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `agentic-actions-auditor` | `coff0xc-cloud-devsecops` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `algorand-vulnerability-scanner` | `coff0xc-blockchain-security` | `dual-use-high-risk` | External/system/plugin description omitted; metadata-only mapping. |
| `ask-questions-if-underspecified` | `supporting-tooling` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `atheris` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `audit-augmentation` | `supporting-tooling` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `audit-context-building` | `supporting-tooling` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `audit-prep-assistant` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `burpsuite-project-parser` | `supporting-tooling` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `cairo-vulnerability-scanner` | `coff0xc-blockchain-security` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `cargo-fuzz` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `claude-in-chrome-troubleshooting` | `coff0xc-ui-doc-output` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `code-maturity-assessor` | `coff0xc-authorized-assessment` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `codeql` | `coff0xc-secure-code-appsec` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `constant-time-analysis` | `coff0xc-cloud-devsecops` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `constant-time-testing` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `cosmos-vulnerability-scanner` | `coff0xc-blockchain-security` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `coverage-analysis` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `crypto-protocol-diagram` | `coff0xc-network-protocol-security` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `designing-workflow-skills` | `coff0xc-ai-agent-rag` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `dev` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `devcontainer-setup` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `diagramming-code` | `coff0xc-research-drawio-diagram` | `dual-use-high-risk` | External/system/plugin description omitted; metadata-only mapping. |
| `differential-review` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `dwarf-expert` | `supporting-tooling` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `entry-point-analyzer` | `coff0xc-blockchain-security` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `firebase-apk-scanner` | `coff0xc-cloud-devsecops` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `fp-check` | `supporting-tooling` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `fuzzing-dictionary` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `fuzzing-obstacles` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `genotoxic` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `gh-cli` | `coff0xc-api-data-platform` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `git-cleanup` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `graph-evolution` | `coff0xc-software-engineering` | `dual-use-high-risk` | External/system/plugin description omitted; metadata-only mapping. |
| `guidelines-advisor` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `harness-writing` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `insecure-defaults` | `coff0xc-cloud-devsecops` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `libafl` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `libfuzzer` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `mermaid-to-proverif` | `coff0xc-network-protocol-security` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `modern-python` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `mutation-testing` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `ossfuzz` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `pi-planning-with-files` | `supporting-tooling` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `planning-with-files` | `supporting-tooling` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `planning-with-files-zh` | `supporting-tooling` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `property-based-testing` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `ruzzy` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `sarif-parsing` | `coff0xc-secure-code-appsec` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `second-opinion` | `coff0xc-ai-agent-rag` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `secure-workflow-guide` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `semgrep` | `coff0xc-secure-code-appsec` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `semgrep-rule-creator` | `coff0xc-secure-code-appsec` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `semgrep-rule-variant-creator` | `coff0xc-secure-code-appsec` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `sharp-edges` | `coff0xc-api-data-platform` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `skill-creator` | `supporting-tooling` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `skill-improver` | `coff0xc-ai-agent-rag` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `solana-vulnerability-scanner` | `coff0xc-blockchain-security` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-ad-pentest` | `coff0xc-software-engineering` | `dual-use-high-risk` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-ai-agent-dev` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-binary-exploit` | `coff0xc-binary-mobile-iot` | `dual-use-high-risk` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-blockchain-security` | `coff0xc-blockchain-security` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-code-audit` | `coff0xc-secure-code-appsec` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-iot-ics` | `coff0xc-binary-mobile-iot` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-mobile-security` | `coff0xc-binary-mobile-iot` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-paper` | `coff0xc-research-drawio-diagram` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-privesc` | `coff0xc-binary-mobile-iot` | `dual-use-high-risk` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-purple-team` | `coff0xc-purple-deception` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-quick-translate` | `coff0xc-network-protocol-security` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `source-command-vuln-research` | `coff0xc-vulnerability-lifecycle` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `spec-to-code-compliance` | `coff0xc-blockchain-security` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `substrate-vulnerability-scanner` | `coff0xc-blockchain-security` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `supply-chain-risk-auditor` | `coff0xc-cloud-devsecops` | `dual-use-high-risk` | External/system/plugin description omitted; metadata-only mapping. |
| `testing-handbook-generator` | `coff0xc-software-engineering` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `token-integration-analyzer` | `coff0xc-blockchain-security` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `ton-vulnerability-scanner` | `coff0xc-blockchain-security` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `trailmark` | `coff0xc-secure-code-appsec` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `trailmark-structural` | `coff0xc-secure-code-appsec` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `trailmark-summary` | `coff0xc-detection-response` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `UIdesign` | `coff0xc-ui-doc-output` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `variant-analysis` | `coff0xc-secure-code-appsec` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |
| `vector-forge` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `wycheproof` | `coff0xc-software-engineering` | `dual-use-high-risk` | External/system/plugin description omitted; metadata-only mapping. |
| `yara-rule-authoring` | `coff0xc-detection-response` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `zeroize-audit` | `supporting-tooling` | `security-review` | External/system/plugin description omitted; metadata-only mapping. |

### codex-system

| Skill | Mapped target | Risk | Notes |
|---|---|---|---|
| `imagegen` | `coff0xc-ui-doc-output` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |
| `openai-docs` | `coff0xc-software-engineering` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |
| `plugin-creator` | `supporting-tooling` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |
| `skill-creator` | `supporting-tooling` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |
| `skill-installer` | `coff0xc-software-engineering` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |

### codex-user

| Skill | Mapped target | Risk | Notes |
|---|---|---|---|
| `cli-creator` | `coff0xc-api-data-platform` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-ai-agent-rag` | `coff0xc-ai-agent-rag` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-api-data-platform` | `coff0xc-api-data-platform` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-authorized-assessment` | `coff0xc-authorized-assessment` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-binary-mobile-iot` | `coff0xc-binary-mobile-iot` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-blockchain-security` | `coff0xc-blockchain-security` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-cloud-devsecops` | `coff0xc-cloud-devsecops` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-compliance-architecture` | `coff0xc-compliance-architecture` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-detection-response` | `coff0xc-detection-response` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-identity-zero-trust` | `coff0xc-identity-zero-trust` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-network-protocol-security` | `coff0xc-network-protocol-security` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-office-doc-tools` | `coff0xc-office-doc-tools` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-purple-deception` | `coff0xc-purple-deception` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-research-drawio-diagram` | `coff0xc-research-drawio-diagram` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-secure-code-appsec` | `coff0xc-secure-code-appsec` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-skill-router` | `coff0xc-skill-router` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-software-engineering` | `coff0xc-software-engineering` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-ui-doc-output` | `coff0xc-ui-doc-output` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `coff0xc-vulnerability-lifecycle` | `coff0xc-vulnerability-lifecycle` | `installed-coff0xc-copy` | External/system/plugin description omitted; metadata-only mapping. |
| `pdf` | `coff0xc-software-engineering` | `general` | External/system/plugin description omitted; metadata-only mapping. |
| `UIdesign` | `coff0xc-ui-doc-output` | `general` | External/system/plugin description omitted; metadata-only mapping. |

### coffee-release

| Skill | Mapped target | Risk | Notes |
|---|---|---|---|
| `coff0xc-ai-agent-rag` | `coff0xc-ai-agent-rag` | `curated-release` | Use when / 当用户请求 Agent、RAG、LLM、Prompt、embedding、向量数据库、LangChain/AutoGen、tool calling、多模型编排、记忆/缓存、评测、观测、成本、失败恢复或可落地 AI 助手。交付架构、工具 schema、检索引用、eval 和降级。手动触发：使用 coff0xc-ai-agent-rag。 |
| `coff0xc-api-data-platform` | `coff0xc-api-data-platform` | `curated-release` | Use when / 当用户请求 API、数据库、数据平台、CLI/SDK 或接口契约：REST、GraphQL、OpenAPI、SQL/Postgres、schema/migration、分页、认证/鉴权、错误码、JSON、ETL、数据质量、usage ledger、filter builder、impact analysis。手动触发：使用 coff0... |
| `coff0xc-authorized-assessment` | `coff0xc-authorized-assessment` | `curated-release` | Use only for authorized security assessment / 当用户请求已授权评估、ROE、attack surface、recon/fingerprint、red team/adversary emulation、防御化攻击链规划、control validation、CDN/WAF 边界、phishing/social-e... |
| `coff0xc-binary-mobile-iot` | `coff0xc-binary-mobile-iot` | `curated-release` | Use when / 当用户请求 reverse engineering、PWN、kernel、APK/IPA、Frida、firmware、IoT/ICS/SCADA、PLC/Modbus、UART/JTAG/SPI、BLE/RF、CTF、crypto review、constant-time、设备包或可执行文件分析。手动触发：使用 coff0xc-bi... |
| `coff0xc-blockchain-security` | `coff0xc-blockchain-security` | `curated-release` | Use when / 当用户请求 blockchain、smart contract、DeFi/Web3、多链安全：Solidity/EVM、Solana、Cosmos、Substrate、Cairo/StarkNet、TON、Algorand、AMM、oracle、bridge、token/NFT、Foundry/Hardhat/Slither、资产流和... |
| `coff0xc-cloud-devsecops` | `coff0xc-cloud-devsecops` | `curated-release` | Use when / 当用户请求 cloud、container、Kubernetes/K8s、serverless、DevSecOps、supply chain、CI/CD 或 secrets：AWS/Azure/GCP、IAM、S3/Blob/GCS、Docker、Terraform/IaC、GitHub Actions、SBOM/SCA、secret... |
| `coff0xc-compliance-architecture` | `coff0xc-compliance-architecture` | `curated-release` | Use when / 当用户请求 security architecture、threat modeling、compliance、data security/privacy/DLP、baseline：STRIDE、等保、PCI-DSS、GDPR、ISO27001、SOC2、CIS/NIST、control evidence、risk register、a... |
| `coff0xc-detection-response` | `coff0xc-detection-response` | `curated-release` | Use when / 当用户请求 SOC、安全运营、detection engineering、threat hunting/intel、incident response/IR、forensics、malware、phishing：SIEM、Sigma、YARA、IOC、logs、alerts、EDR、timeline、alert tuning、误报和检... |
| `coff0xc-identity-zero-trust` | `coff0xc-identity-zero-trust` | `curated-release` | Use when / 当用户请求 identity、IAM、zero trust、AD/Active Directory、Kerberos、SSO/MFA、BloodHound、PAM、service accounts、权限/凭证风险、identity paths、lateral movement defense、access governance 或特权... |
| `coff0xc-network-protocol-security` | `coff0xc-network-protocol-security` | `curated-release` | Use when / 当用户请求 network/protocol security：TLS、DNS、TCP/UDP、HTTP/2、HTTP/3、QUIC、WiFi、Bluetooth/BLE、RF、packet/pcap/Wireshark、抓包、握手、状态机、secure communication、ProVerif 或 Mermaid protoco... |
| `coff0xc-office-doc-tools` | `coff0xc-office-doc-tools` | `curated-release` | Use when / 当用户请求正式 Office 或文件型交付物：PPT PPTX PowerPoint slides deck、DOCX Word redline comments、PDF read create review render、Excel XLSX CSV workbook chart formula table export。要求可编辑... |
| `coff0xc-purple-deception` | `coff0xc-purple-deception` | `curated-release` | Use when / 当用户请求 purple team、ATT&CK、control validation、detection coverage、emulation plan、honeypot/deception、decoy/canary、SOC 改进、检测有效性、覆盖指标或防守能力验证。仅限授权防御演练。手动触发：使用 coff0xc-purple-d... |
| `coff0xc-research-drawio-diagram` | `coff0xc-research-drawio-diagram` | `curated-release` | Use when / 当用户请求 draw.io、diagrams.net、.drawio、科研图、论文方法图、architecture/method/model diagram、algorithm pipeline、Transformer/CNN/GNN/diffusion/RAG/agent 架构图。绘制前需要 paper/arXiv/official... |
| `coff0xc-secure-code-appsec` | `coff0xc-secure-code-appsec` | `curated-release` | Use when / 当用户请求 code/AppSec audit：source/sink、taint、Web/API/GraphQL/OAuth、CSP/CORS/Cookie、LLM prompt injection、access control/authorization bypass、SSRF/XSS/SQLi、backdoor/Webshell... |
| `coff0xc-skill-router` | `coff0xc-skill-router` | `curated-release` | Coff0xc lightweight skill router/composer. Use only when the user asks AI to decide which coff0xc skills to use, chain skills, build a task/workflow graph, orchestrate vibe coding... |
| `coff0xc-software-engineering` | `coff0xc-software-engineering` | `curated-release` | Use when / 当用户请求 dev/software engineering：build product、repo repair、failing tests/CI、bugfix、feature/refactor、full-stack/end-to-end implementation、REST API/frontend UI implementati... |
| `coff0xc-ui-doc-output` | `coff0xc-ui-doc-output` | `curated-release` | Use when / 当用户请求 UI/frontend/product surface/report/translation polish：dashboard/admin/SaaS、component/design system、responsive/mobile、accessibility/ARIA/contrast、loading/empty/err... |
| `coff0xc-vulnerability-lifecycle` | `coff0xc-vulnerability-lifecycle` | `curated-release` | Use when / 当用户请求 vulnerability lifecycle：CVE、advisory、patch diff、CVSS/EPSS/KEV、PoC 验证、bug bounty、pentest report、影响范围、修复优先级、缓解措施、security patch 或修复跟踪。授权验证优先。手动触发：使用 coff0xc-vulnera... |

### plugin-bundled

| Skill | Mapped target | Risk | Notes |
|---|---|---|---|
| `browser` | `coff0xc-software-engineering` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |
| `Chrome` | `coff0xc-ui-doc-output` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |
| `Chrome` | `coff0xc-ui-doc-output` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |

### plugin-runtime

| Skill | Mapped target | Risk | Notes |
|---|---|---|---|
| `documents` | `coff0xc-cloud-devsecops` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |
| `Presentations` | `coff0xc-office-doc-tools` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |
| `Spreadsheets` | `coff0xc-office-doc-tools` | `platform-provided` | External/system/plugin description omitted; metadata-only mapping. |

## Optimization Notes

- Keep `skills/` limited to the curated `coff0xc-*` release set unless a new domain is intentionally promoted.
- Use this inventory to decide whether a new external skill should remain a reference, become a script, or be merged into an existing Coff0xc domain.
- Do not copy external/system/plugin skill bodies into this repository without checking license, provenance, and safety boundaries.
