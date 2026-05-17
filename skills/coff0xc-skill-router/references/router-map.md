# Router Map

Use this only when a task is genuinely cross-domain, when auto-triggering failed, or when debugging skill selection. Narrow tasks should go straight to the most specific skill.

## Composition Rules

1. Pick one primary skill that owns the final deliverable.
2. Add support skills only for capabilities the current task actually needs.
3. Give each support skill one clear job: contract, UI, safety, file artifact, detection, compliance, or verification.
4. Execute the current stage before expanding the graph.
5. Re-route when evidence changes, not because a keyword looks related.
6. Do not create workflow traces, golden responses, or eval reports during normal user work.

## Common Compositions

| Task type | Primary skill | Support skills | Intent |
| --- | --- | --- | --- |
| Full-stack SaaS/admin feature | `coff0xc-software-engineering` | `coff0xc-api-data-platform`, `coff0xc-ui-doc-output`, `coff0xc-secure-code-appsec` | Implement first, then align contracts, UI quality, and auth/input risk. |
| Agent/RAG product | `coff0xc-ai-agent-rag` | `coff0xc-api-data-platform`, `coff0xc-software-engineering`, `coff0xc-ui-doc-output` | Define agent system, then land APIs, code, and usable UI. |
| Analytics/data dashboard | `coff0xc-api-data-platform` | `coff0xc-ui-doc-output`, `coff0xc-software-engineering`, `coff0xc-office-doc-tools` | Establish data contract and formulas before UI and export artifacts. |
| Executive deliverable | `coff0xc-office-doc-tools` | `coff0xc-ui-doc-output`, `coff0xc-api-data-platform`, `coff0xc-research-drawio-diagram` | File artifact owns delivery; UI/report skill owns narrative clarity; data and diagrams provide evidence. |
| Secure release | `coff0xc-secure-code-appsec` | `coff0xc-cloud-devsecops`, `coff0xc-software-engineering`, `coff0xc-compliance-architecture` | Find risks, fix scoped issues, verify, and package release evidence. |
| Detection/incident workflow | `coff0xc-detection-response` | `coff0xc-vulnerability-lifecycle`, `coff0xc-cloud-devsecops`, `coff0xc-purple-deception` | Build timeline and detection first, then prioritize and validate coverage. |
| Authorized assessment | `coff0xc-authorized-assessment` | `coff0xc-cloud-devsecops`, `coff0xc-identity-zero-trust`, `coff0xc-detection-response`, `coff0xc-compliance-architecture` | Keep ROE/scope central; map actions to controls and evidence. |
| Protocol/IoT review | `coff0xc-network-protocol-security` | `coff0xc-binary-mobile-iot`, `coff0xc-detection-response`, `coff0xc-research-drawio-diagram` | Analyze protocol evidence, firmware/mobile endpoints, detections, and diagrams. |

## Skill Map

| Skill | Use for | Do not use for |
| --- | --- | --- |
| `coff0xc-software-engineering` | Repo repair, feature work, tests, CI failures, scripts, local Git summary, build verification. | Pure UI taste review, pure Office artifact authoring, pure security audit. |
| `coff0xc-ai-agent-rag` | Agent/RAG architecture, prompt systems, retrieval, memory, tools, evals, observability, cost. | Simple prompt rewrite without system design. |
| `coff0xc-api-data-platform` | REST/GraphQL/OpenAPI, SQL/schema/migrations, data quality, CLI/SDK, JSON/error contracts. | User-visible visual polish unless it is a data-dashboard contract. |
| `coff0xc-ui-doc-output` | UI, frontend UX, dashboard polish, design systems, accessibility, screenshots, report narrative, translation. | Formal PPTX/DOCX/PDF/XLSX file creation; route those to Office. |
| `coff0xc-office-doc-tools` | PowerPoint, Word, PDF, Excel/CSV artifacts, comments, redlines, formulas, charts, render/export QA. | Web app UI or generic markdown-only copy edits. |
| `coff0xc-research-drawio-diagram` | Editable draw.io research/method/model diagrams backed by public or user-provided sources. | Plain screenshots or non-editable diagram images. |
| `coff0xc-secure-code-appsec` | Code/app security, web/API/GraphQL/OAuth/browser/LLM security, source/sink, authz, backdoors. | Unauthorized exploitation or production attack steps. |
| `coff0xc-cloud-devsecops` | Cloud, Kubernetes, containers, CI/CD, supply chain, SBOM, secrets, IaC. | Local-only code refactors without deployment or supply-chain surface. |
| `coff0xc-detection-response` | SIEM/Sigma/YARA, threat hunting, malware triage, forensics, incident timeline, alert tuning. | Pre-incident app code review unless detection logic is the deliverable. |
| `coff0xc-vulnerability-lifecycle` | CVE/advisory/patch analysis, impact, prioritization, mitigation, tracking. | Broad code implementation without a vulnerability lifecycle question. |
| `coff0xc-identity-zero-trust` | IAM, SSO, MFA, AD/Kerberos, BloodHound paths, privileged accounts, zero trust. | Generic app auth bugs in code; use AppSec first. |
| `coff0xc-authorized-assessment` | ROE, scope, attack surface, defensive red-team planning, control validation, reports. | Unscoped or unauthorized offensive requests. |
| `coff0xc-binary-mobile-iot` | Reverse engineering, APK/IPA, firmware, IoT/ICS, kernel, PWN/CTF, crypto implementation clues. | Web/API code review unless binary/mobile evidence exists. |
| `coff0xc-blockchain-security` | Smart contracts, DeFi, bridges, token flows, oracle/price logic, multi-chain audits. | Traditional web/API security without chain assets. |
| `coff0xc-compliance-architecture` | Threat modeling, security architecture, data privacy, compliance mapping, control evidence. | Line-level code patching unless it produces compliance evidence. |
| `coff0xc-purple-deception` | ATT&CK mapping, purple-team plans, control coverage, deception/honeypots, detection validation. | Initial incident triage; use detection-response first. |
| `coff0xc-network-protocol-security` | TLS/DNS/HTTP/QUIC/TCP/UDP, packet/pcap analysis, wireless/BLE/RF, protocol diagrams. | General network configuration hardening without protocol evidence. |

## Output Template

```markdown
工作流：
- 主 skill: <skill> - <one-line reason>
- 辅助 skills: <skill>: <one-line reason>
- 暂不使用: <skill>: <one-line reason>

阶段：
1. <stage> - 使用 <skill>，门禁：<verifiable gate>
2. <stage> - 使用 <skill>，门禁：<verifiable gate>

重路由：
- 如果发现 <evidence>，新增/切换到 <skill>。
```
