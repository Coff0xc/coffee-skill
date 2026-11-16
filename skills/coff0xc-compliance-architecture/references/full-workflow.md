# Full Workflow

This file is the on-demand extended workflow for `coff0xc-compliance-architecture`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Turn architecture and compliance requirements into assets, data flows, threats, controls, evidence, and remediation plans — not generic checklists.

## Applicable Scenarios
- Doing system security architecture reviews, threat modeling, compliance gap analysis, data protection, and control matrices.
- Sorting out data classification, encryption, de-identification, DLP, access control, log auditing, and privacy risk.
- Setting security baselines, maturity paths, remediation priorities, and evidence-collection plans.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-compliance-architecture ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not answer current regulation clauses, certification requirements, or standard versions from stale memory.
- Do not treat compliance checkmarks as security conclusions; they must be tied to system evidence.
- For legal interpretation, give the technical view and evidence level; do not substitute for a lawyer's opinion.

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
| Architecture review | boundaries, trust zones, entry points, identity, data flows, third parties, failure modes | Architecture risks can be located. |
| Threat modeling | STRIDE, PASTA, attack trees, abuse cases, assets | Threats map to controls. |
| Compliance mapping | MLPS, PCI-DSS, GDPR, ISO27001, SOC2, CIS, NIST | Clauses to evidence and gaps. |
| Data security | classification and grading, encryption, de-identification, masking, retention, backup, DLP | Data lifecycle is controlled. |
| Privacy | PII, consent, purpose limitation, DSR, minimization, cross-border | Privacy risks can be explained. |
| Baselines | OS, DB, K8s, Cloud, App, Logging, Endpoint | Configuration baselines and exception management. |
| Maturity | current capability, target state, roadmap, owner, SLA, metrics | Remediation is trackable. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| security-architecture | System boundaries, threat modeling, control design, and security review. |
| compliance-audit | MLPS, PCI-DSS, GDPR, baselines, and evidence mapping. |
| data-security | Data classification, encryption, de-identification, DLP, access control. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Scope definition | Confirm system, data, regulations/standards, business goals, and review depth. | Review goals are clear. |
| Asset data flow | Draw assets, trust boundaries, identity, data flows, third parties, and storage. | Threat model has a basis. |
| Control mapping | Map threats/clauses to existing controls, evidence, and gaps. | Gaps are specific. |
| Risk ordering | Order by impact, likelihood, compliance requirements, executability, and dependencies. | Remediation has priority. |
| Remediation plan | Give owner, steps, verification, timing, exceptions, and residual risk. | Manageable and landable. |
| Evidence package | Organize screenshots, configuration, logs, tests, policies, processes, and report citations. | Auditable and re-checkable. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Current regulations, standard versions, and certification requirements must be checked against official or authoritative sources.
- Confirm permissions and de-identification before accessing production evidence, customer data, or audit systems.
- Do not write technical recommendations as legal conclusions.

## Verification Checklist
- Every compliance conclusion has evidence files, configuration, screenshots, or process records.
- Every threat has existing controls, gaps, and a verification method.
- Data-protection conclusions cover collection, transmission, storage, use, sharing, and deletion.
- Remediation items have owners, priorities, and acceptance criteria.

## Anti-Patterns
- Copying standard clauses without mapping them to the real system.
- Looking only at network boundaries, not identity and data flows.
- Treating encryption as the answer to every data-security problem.
- Marking compliance as passed with no evidence.

## Merged Sources
- `compliance-audit`
- `data-security`
- `security-architecture`

## Nearby Skills on This Machine
- `guidelines-advisor`
- `sharp-edges`
- `code-maturity-assessor`

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
