# Full Workflow

This file is the on-demand extended workflow for `coff0xc-authorized-assessment`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Turn high-risk red-team/attack-chain requests into control validation, detection coverage, hardening recommendations, and reports within the authorized scope — without outputting abusable attack steps.

## Applicable Scenarios
- Building authorized assessment plans, ROE, test matrices, control validation, detection coverage, and report templates.
- Turning recon, red-team, phishing-exercise, exfiltration-exercise, and C2-infrastructure requests into defensive plans.
- Assessing organizational security controls, people processes, log coverage, and response capability.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-authorized-assessment ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not provide real bypass, phishing delivery, C2 setup, persistence, credential acquisition, exfiltration, or detection-evasion steps.
- Without authorization or with unclear scope, give only a preparation checklist and authorization template.
- Do not guide attack-chain execution against a specific third-party target.

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
| ROE/authorization | targets, scope, time window, rate, prohibited actions, contacts, stop conditions | Assessment stays lawful and controlled. |
| Attack-surface inventory | asset inventory, domains, cloud exposure, certificates, tech stack, third-party entry points | Authorized/public-information scope only. |
| Control validation | prevention, detection, response, recovery, people processes, log coverage | Map technology to control objectives. |
| Defensive red-teaming | scenarios, hypotheses, telemetry, expected alerts, blue-team actions | Do not output attack details. |
| Phishing exercises | training goals, approvals, template risk, recipient scope, privacy, and review | Do not collect real credentials. |
| Exfiltration exercises | DLP/egress controls, log fields, approvals, and safe samples | Do not exfiltrate real data. |
| Tool development | defensive test tools, detection validation tools, report automation | Do not build covert or evasive tools. |
| Reporting | executive summary, scope, findings, evidence, control gaps, improvement path | For management and engineering. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| recon-workflow | Authorized asset discovery, public-information organization, and boundary confirmation. |
| fingerprint-engine | Defensive asset identification from tech-stack/service fingerprints. |
| full-pentest | End-to-end authorized assessment planning and reporting. |
| attack-chain-orchestrator | Attack chains turned into control-validation matrices. |
| autoredteam-orchestrator | Automated exercise planning and safety gates. |
| red-team-infra | Exercise infrastructure requirements, isolation, and logging, without C2 implementation. |
| c2-framework | C2 risk, detection, and isolation recommendations, without building or operating it. |
| evasion-toolkit | Evasion-risk education, detection coverage, and hardening, without bypass techniques. |
| cdn-bypass | Boundary exposure risk and WAF/CDN configuration checks. |
| proxy-pool-manager | Proxy/exit compliance, logging, and risk-control recommendations. |
| phishing-simulation | Compliant phishing-exercise plans and privacy protection. |
| social-engineering | People-risk training, approvals, and safe exercise boundaries. |
| post-exploitation | Post-intrusion control checks, log coverage, and containment plans. |
| data-exfiltration | DLP/egress defensive validation and safe sample plans. |
| security-tool-dev | Defensive tools, validation scripts, and report automation. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Hard gates | First confirm written authorization, ROE, targets, prohibited actions, time window, and contacts. | Scope is clear. |
| Scenario design | Define scenarios from business risk, not from pursuit of attack technique. | Control objectives are clear. |
| Telemetry plan | List expected logs, alerts, fields, response actions, and success/failure criteria. | Controls can be validated. |
| Safe execution plan | Use non-destructive, low-risk, reversible, observable simulation methods. | No harm to systems. |
| Evidence collection | Record timelines, screenshots, logs, configuration, and response actions. | Reports have evidence. |
| Review and improvement | Output an improvement path by detection, response, process, tech debt, and training. | Exercise closes the loop. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Stop execution when there is no authorization, ROE, or contact; output only a preparation checklist.
- Any action that could affect real users, production systems, external targets, or mail recipients must be confirmed.
- Do not generate or store directly reusable attack payloads, C2 configurations, phishing collection pages, or evasion scripts.

## Verification Checklist
- Authorization documents, target inventory, time window, and communication channels exist.
- Each scenario has expected vs. actual detection compared.
- Each control gap has evidence, impact, and improvement recommendations.
- After the exercise, confirm the system is restored and no data leaked.

## Anti-Patterns
- Treating a red-team skill list as an assessment plan.
- Starting recon or testing with unclear scope.
- Showing only the success path without assessing detection and response.
- Using real sensitive data for exfiltration or phishing exercises.

## Merged Sources
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

## Nearby Skills on This Machine
- `source-command-purple-team`
- `secure-workflow-guide`
- `audit-prep-assistant`

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
