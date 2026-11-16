# Full Workflow

This file is the on-demand extended workflow for `coff0xc-purple-deception`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Use controlled exercises to validate defensive capability and observability, and output detection gaps, response gaps, and deception-defense designs.

## Applicable Scenarios
- Designing purple-team exercises, ATT&CK technique mapping, detection-coverage assessment, and response-capability validation.
- Planning honeypots, decoy accounts, decoy files, canary tokens, deception networks, and alert processes.
- Turning red-team TTPs into defensive controls, log fields, query rules, and exercise metrics.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-purple-deception ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not provide real attack execution, evasion, defense bypass, or unauthorized exercise steps.
- Honeypots must not share networks with high-privilege production systems or collect personal information beyond their purpose.
- Do not treat a decoy hit as proof of successful intrusion; the context needs validation.

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
| ATT&CK mapping | tactics, techniques, data sources, detection, response, and prevention controls | Forms a coverage matrix. |
| Exercise plan | objectives, scope, scenarios, roles, timing, success criteria, stop conditions | Can be run safely. |
| Detection validation | log fields, SIEM/EDR queries, alerts, false positives, false negatives, latency | Assesses real capability. |
| Response validation | triage, escalation, communication, containment, recovery, review | Process can be exercised. |
| Deception defense | honeypot, decoy account, decoy file, canary, fake service | Isolation and monitoring are explicit. |
| Metrics | coverage, MTTD, MTTR, precision, recall, alert fatigue, control gap | Improvement is quantifiable. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| purple-team | Purple-team plans, ATT&CK mapping, control validation, and review. |
| honeypot | Deception defense, decoys, isolation, alerts, and operations risk. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Objectives and scope | Define business risk, technical scope, participating roles, prohibited actions, and stop conditions. | Exercise is controlled. |
| Technique mapping | Select ATT&CK techniques, expected telemetry, detection rules, and response actions. | Validation points are explicit. |
| Safe simulation | Design low-risk simulations or tabletop exercises without outputting attack details. | Can trigger controls. |
| Data collection | Record alert times, log fields, response actions, and communication records. | Evidence is re-checkable. |
| Gap analysis | Identify missing logs, missing rules, false positives, delays, and process blockers. | Improvements are specific. |
| Roadmap | Schedule detection, response, deception, and training improvements by benefit and cost. | Closed-loop governance. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Confirm authorization, notification scope, production impact, and rollback before exercises.
- Confirm isolation, log retention, privacy, and legal boundaries before honeypots go live.
- Do not run simulated attacks against real external targets.

## Verification Checklist
- Every technique has expected vs. actual detection compared.
- Every alert has fields, timestamps, rule name, and response records.
- Deception assets have isolation, access auditing, and false-touch handling.
- Review items have owners and completion criteria.

## Anti-Patterns
- Only demonstrating red-team actions without validating blue-team capability.
- No review or remediation tracking after an exercise.
- Decoys so realistic they create business and privacy risk.
- Counting only coverage without looking at alert quality and response time.

## Merged Sources
- `honeypot`
- `purple-team`

## Nearby Skills on This Machine
- `source-command-purple-team`
- `detection-engineering`

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
