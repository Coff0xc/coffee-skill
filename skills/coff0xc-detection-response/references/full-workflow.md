# Full Workflow

This file is the on-demand extended workflow for `coff0xc-detection-response`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Turn alerts, logs, samples, IOCs, and intelligence into verifiable detection, handling, and review results; facts, inferences, and unknowns must stay separate.

## Applicable Scenarios
- Writing or reviewing Sigma/YARA/SIEM queries, detection logic, hunting hypotheses, and alert-handling processes.
- Analyzing mail headers, IOCs, logs, EDR alerts, memory/disk forensic results, and malicious-sample metadata.
- Building incident response plans, timelines, impact scope, containment/recovery, and review improvements.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-detection-response ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not run unknown malicious samples or provide detection-evasion/persistence techniques.
- OSINT must not be used for harassment, phishing, account takeover, or privacy violations.
- Do not treat intelligence rumors as confirmed intrusion facts.

## Execution Principles
- Read project files, configuration, call sites, existing style, and available tools before concluding or changing files.
- Turn user goals into verifiable completion criteria; record uncertain but low-risk details as assumptions and keep going.
- When current facts, versions, CVEs, cloud services, GitHub status, pricing, external APIs, or papers are involved, check real sources and mark the evidence level.
- When code changes are involved, keep the minimal correct change and prefer existing frameworks, scripts, tests, and local tools.
- Only commands, tests, builds, scans, or manual checks that were actually run may be written as verified.
- Before deletion, remote writes, production, credentials, payment, push, PR/Issue, CI/CD, permission, or infrastructure changes, get explicit authorization first.

## Security Boundaries
- Handle only owned assets, explicitly authorized assets, labs, CTFs, ranges, logs, configuration, samples, code audits, defensive work, and report writing.
- Do not provide exploitation, credential acquisition, persistence, detection evasion, C2, phishing collection, data exfiltration, destruction, or unauthorized-access steps against real third-party targets.
- High-risk requests default to defensive output: authorization boundaries, risk explanations, detection ideas, log queries, rule drafts, hardening plans, validation checklists, and report structure.
- Before active online scanning, cloud-account checks, directory/tenant queries, or production-environment actions, confirm target scope, rate, time window, prohibited actions, and rollback method.
- When keys, personal information, sensitive sample data, or customer data is found, report only the type, location, and handling recommendation; do not repeat the full secret value.

## Capability Matrix
| Capability area | Coverage | Execution points |
| --- | --- | --- |
| Detection engineering | Sigma, YARA, SIEM query, EDR logic, field mapping, FP tuning | Rules include data sources and test samples. |
| SOC operations | alert grading, triage, escalation, case notes, SLA, runbook | Handling paths are clear. |
| Threat hunting | hypotheses, ATT&CK techniques, telemetry, queries, result interpretation | Distinguish what hits and misses mean. |
| Threat intelligence | IOC, TTP, source reliability, timeliness, correlation, actionability | Mark the evidence level. |
| Email security | headers, SPF/DKIM/DMARC, URL, attachments, delivery chain | Preserve the evidence chain. |
| Forensic analysis | timeline, files, processes, network, users, persistence locations | Record source and time zone. |
| Malware analysis | static metadata, strings, behavior hypotheses, sandbox reports, family correlation | Do not execute dangerous samples. |
| Incident response | preparation, identification, containment, eradication, recovery, monitoring, review | Every step has an owner and verification. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| detection-engineering | Rule writing, log fields, false-positive reduction, and testing. |
| soc-operations | Alert triage, case flow, and operations metrics. |
| threat-hunting | Hunting hypotheses, queries, and ATT&CK mapping. |
| threat-intelligence | Intelligence-source assessment, IOC/TTP correlation, and timeliness judgment. |
| email-security | Phishing-mail analysis, authentication records, and attachment/URL risk. |
| forensics-analysis | Host/disk/log timelines and evidence chains. |
| malware-analysis | Static/sandbox-safe analysis and YARA direction. |
| incident-response | IR command, containment, recovery, and review. |
| osint | Public-information collection, attribution hypotheses, and source credibility. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Evidence intake | Record data sources, time window, time zone, hosts, users, sample hashes, log fields. | Evidence is traceable. |
| Fact layering | Separate confirmed facts, strong correlations, weak hypotheses, unknowns, and items needing more data. | Conclusions are not exaggerated. |
| Analysis path | Organize the investigation by kill chain/ATT&CK/timeline/asset impact. | Know what the next query should check. |
| Detection deliverables | Produce queries/rules, field mappings, test data, FP conditions, and deployment notes. | Can be validated in production. |
| Handling plan | Containment, eradication, recovery, monitoring, communication, and review. | Executable for business and security. |
| Closed-loop verification | Confirm alerts dropping, risk cleared, log coverage, and remediation complete. | Incident can be closed. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Confirm first before running samples, connecting to suspicious infrastructure, or querying real user private data.
- External attribution, public disclosure, customer notification, or law-enforcement-related output must keep its evidence level.
- Rules deployed to production SIEM/EDR need change approval and rollback.

## Verification Checklist
- Rules: positive samples, negative samples, field existence, time window, performance, and false-positive samples.
- IR: every handling action has log or configuration evidence.
- Intelligence: source, publication time, relevance, expiry status.
- Forensics: hash, timeline consistency, evidence-preservation path.

## Anti-Patterns
- Treating an IOC hit as proof of successful intrusion.
- Rules with no data-source field explanation.
- Giving handling recommendations without saying how completion is verified.
- Repeating third-party intelligence text as fact.

## Merged Sources
- `detection-engineering`
- `email-security`
- `forensics-analysis`
- `incident-response`
- `malware-analysis`
- `osint`
- `soc-operations`
- `threat-hunting`
- `threat-intelligence`

## Nearby Skills on This Machine
- `yara-rule-authoring`
- `sarif-parsing`
- `source-command-vuln-research`

## Output Contract
```markdown
Done:
- ...

Evidence:
- [Verified/High confidence/Inference/Unverified/Unknown] ...

Actions:
- ...

Verification:
- ...

Residual risks:
- ...

Next steps:
- ...
```
