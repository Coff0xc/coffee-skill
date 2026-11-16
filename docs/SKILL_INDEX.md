# Skill Index

The entry index for `coffee-skill`. Choose a skill by what you want to deliver, not by memorizing keywords.

## Start here: quick pick

| Task shape | Use first | Do not use first |
|---|---|---|
| One repo, one bug, one feature, one CI failure | `coff0xc-software-engineering` | `coff0xc-skill-router`, unless the task is clearly cross-domain |
| One UI, frontend page, dashboard, or report | `coff0xc-ui-doc-output` | The Office skill, unless the deliverable is a PPTX/DOCX/XLSX/PDF |
| One formal Office / file-type deliverable | `coff0xc-office-doc-tools` | The UI skill, unless it is a web/app interface |
| Rewrite a defense deck from a thesis DOCX + old PPTX | `coff0xc-office-doc-tools` | Do not start with the router, unless code/experiments/systems also need changes |
| One Agent/RAG/LLM system design | `coff0xc-ai-agent-rag` | The dev skill, unless it must land in a real repo |
| One API, database, or data-contract problem | `coff0xc-api-data-platform` | The router, unless UI/security/Office are also involved |
| One authorized security-domain problem | The matching security skill | Unauthorized, production, credential, or destructive actions |
| Multi-domain mix, uncertain entry point | `coff0xc-skill-router` | Manually stuffing in every skill |

## Capability map: product and engineering

| Skill | When to use | What evidence to leave |
|---|---|---|
| `coff0xc-software-engineering` | Feature work, repo repair, CI reproduction, test fixes, refactoring, scripting, full-stack changes. | Changed files, root cause, narrow validation (widened when needed), lockfile/diff hygiene notes. |
| `coff0xc-api-data-platform` | REST/GraphQL/OpenAPI, database schemas, migrations, CLI/SDK, data models, pagination, error codes, ETL/data quality. | Contracts/schemas/error models, migration or compatibility notes, data checks, examples or tests. |
| `coff0xc-ai-agent-rag` | Agent/RAG/LLM applications, prompt workflows, tool calling, memory, retrieval, evaluation, observability, latency, and cost. | System flows, retrieval/citation strategy, tool schemas, eval sets, failure modes, fallbacks, and engineering handoff. |
| `coff0xc-ui-doc-output` | Product UI, dashboards, admin, design systems, responsive states, accessibility, report structure, technical translation. | UI changes or review conclusions, state coverage, desktop/mobile or browser evidence, remaining visual risk. |
| `coff0xc-office-doc-tools` | PPTX, DOCX, PDF, XLSX, CSV, formulas, charts, comments, revisions, formal file checks. | Editable file paths, render/preview evidence, OOXML or structure checks, formula/format checks, source assumptions. |
| `coff0xc-research-drawio-diagram` | Turn papers, algorithms, model structures, code paths, or research workflows into editable draw.io diagrams. | `.drawio` files, node/edge specs, evidence tables, source mappings, inference annotations. |

## Capability map: security and governance

Security skills are only for owned, local, lab, CTF, training-range, or explicitly authorized assets. Production, credentials, paid services, remote writes, deletion, PR/push, cloud resource changes, and CI/CD permission changes all require explicit authorization.

| Skill | When to use | What evidence to leave |
|---|---|---|
| `coff0xc-secure-code-appsec` | Code/Web/API/GraphQL/OAuth/CSP/CORS/Cookie/prompt-injection/authorization-bypass/SSRF/XSS/SQLi/source-sink/backdoor risks. | Finding lists, file/line numbers or routes, impact, evidence, exploitability boundaries, fixes, tests, and detection/logging suggestions. |
| `coff0xc-cloud-devsecops` | Cloud/IaC/Kubernetes/Docker/serverless/CI/CD/supply-chain/secrets/SBOM/SCA risks. | Risk lists, least-privilege and isolation advice, pipeline gates, secrets rotation, verification commands. |
| `coff0xc-detection-response` | Sigma/YARA/SIEM, threat hunting, IOCs, IR timelines, EDR alerts, malicious samples/emails/logs, false-positive tuning. | Detection logic, field mappings, ATT&CK mappings, test samples, false-positive analysis, and tuning advice. |
| `coff0xc-vulnerability-lifecycle` | CVEs, advisories, patches, exploitability, EPSS/KEV/CVSS, asset impact, remediation priority, vulnerability reports. | Mechanism, patch diffs, affected scope, business priority, mitigations, owners, and validation plans. |
| `coff0xc-identity-zero-trust` | IAM, AD/Kerberos, SSO/MFA, BloodHound paths, service accounts, PAM, sessions, device posture, permission sprawl. | Identity paths, permission risks, control gaps, consolidation order, and hardening advice. |
| `coff0xc-authorized-assessment` | Authorized assessments, ROE, attack-surface mapping, control validation, defense-oriented red-team exercises, report structure. | Written scope, allowed/prohibited actions, phases, observation points, detection/control matrices, and report plans. |
| `coff0xc-binary-mobile-iot` | Binaries, APK/IPA, firmware, IoT/ICS/OT, kernel/mobile, Frida points, UART/JTAG/SPI, protocol parsing, crypto-implementation risks. | Sample structure, entry points, string/configuration/permission details, communication paths, risk hypotheses, and validation routes. |
| `coff0xc-blockchain-security` | Solidity/EVM/Solana/Cosmos/Substrate/Cairo/TON/Algorand, DeFi, AMM, oracles, bridges, tokens, NFTs, asset flows, and state machines. | Entry points, asset flows, permission/invariant risks, PoC boundaries, remediation advice, and test coverage. |
| `coff0xc-compliance-architecture` | Threat modeling, security architecture, control mapping, data classification, privacy/DLP, SOC 2/ISO/GDPR/CIS/NIST, launch reviews. | Trust boundaries, STRIDE/control matrices, evidence gaps, risk decisions, and remediation plans. |
| `coff0xc-purple-deception` | ATT&CK mapping, purple-team plans, control validation, detection coverage, deception defense, decoy/canary, SOC improvement. | Technique mappings, log requirements, coverage matrices, exercise hypotheses, and improvement backlogs. |
| `coff0xc-network-protocol-security` | TLS/DNS/HTTP/QUIC/TCP/UDP, pcap/Wireshark, wireless/BLE/RF, state machines, secure communication, formal protocol diagrams. | Protocol flows, handshake/state analysis, anomalous fields, security impact, and validation/modeling advice. |

## Common combinations

Use `coff0xc-skill-router` only when the task genuinely spans domains or you are unsure of the entry point.

| Task | Common combination |
|---|---|
| Full-stack SaaS feature | `software-engineering` + `api-data-platform` + `ui-doc-output` + `secure-code-appsec` |
| Agent/RAG product | `ai-agent-rag` + `api-data-platform` + `software-engineering` + `ui-doc-output` |
| Executive deliverable from code/data | `office-doc-tools` + `api-data-platform` + `ui-doc-output` + `research-drawio-diagram` |
| Secure release review | `secure-code-appsec` + `cloud-devsecops` + `software-engineering` + `compliance-architecture` |
| Incident response / detection package | `detection-response` + `vulnerability-lifecycle` + `cloud-devsecops` + `purple-deception` |
| Protocol / IoT / binary research | `network-protocol-security` + `binary-mobile-iot` + `research-drawio-diagram` + optional `office-doc-tools` |

## Manual trigger examples

```text
Use coff0xc-software-engineering: reproduce the CI failure, make the minimal fix, and run the available validation.
Use coff0xc-ui-doc-output: redo this dashboard, checking states, mobile, accessibility, and screenshot evidence.
Use coff0xc-office-doc-tools: turn this outline into an editable PPTX and check rendering, charts, and sources.
Use coff0xc-ai-agent-rag: design a knowledge-base assistant with citations, caching, failure fallbacks, and an eval set.
Use coff0xc-secure-code-appsec: audit this API for authorization-bypass and input-validation risks.
Decide which coff0xc skills are needed, chain them into a workflow, and complete this task.
```
