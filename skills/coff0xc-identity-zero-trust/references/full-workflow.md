# Full Workflow

This file is the on-demand extended workflow for `coff0xc-identity-zero-trust`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Assess permission risk from identity, device, network, application, and data access paths, and output detection, least-privilege, and zero-trust improvement plans.

## Applicable Scenarios
- Reviewing AD, Kerberos, cloud IAM, SSO/MFA, PAM, service accounts, permission delegation, and access paths.
- Doing defensive path analysis from BloodHound/directory exports/audit logs.
- Designing zero-trust controls, conditional access, credential governance, least privilege, and lateral-movement detection.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-identity-zero-trust ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not provide credential theft, hash extraction, ticket forgery, MFA bypass, real privilege escalation, or lateral-movement steps.
- Do not run modification commands on production directories, tenants, or endpoints without explicit authorization.
- Real user private and credential data must be de-identified.

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
| Identity governance | users, groups, roles, service accounts, privileged accounts, lifecycle, JML | Permissions have owners and reasons. |
| Authentication strength | MFA, SSO, conditional access, device posture, session policy | High-risk paths have strong authentication. |
| Authorization model | RBAC, ABAC, tenant boundary, delegation, admin roles | Least privilege and separation of duties. |
| AD/Kerberos | GPO, SPN, delegation, trust, ACL, tiering, adminSDHolder | Defensive path analysis. |
| Credential risk | hardcoding, shared accounts, long-lived tokens, weak storage, rotation, audit | Do not expose secret values. |
| Lateral-movement defense | remote administration, shares, RDP/WinRM/SSH, log coverage, network segmentation | Detection and blocking recommendations. |
| Zero trust | identity, device, application, data, network, continuous evaluation | Control matrix and maturity path. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| identity-security | IAM/SSO/MFA/PAM/identity governance. |
| zero-trust | Zero-trust architecture, control matrix, and maturity path. |
| ad-pentest | AD/Kerberos defensive path analysis and hardening. |
| credential-access | Credential-exposure detection, rotation, and log audit. |
| privilege-escalation | Privilege-escalation path defense, permission boundaries, and least privilege. |
| lateral-movement | Lateral-movement detection, segmentation, and remote-access control. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Scope and data | Confirm directory/tenant, data exports, logs, tool results, and authorization. | Data sources are lawful. |
| Asset modeling | List identities, roles, systems, data, admin channels, and trust relationships. | Access graph is clear. |
| Path analysis | Find high-privilege paths, weak authentication, excessive delegation, long-lived credentials, and log blind spots. | Risks have evidence. |
| Control mapping | Map MFA, PAM, segmentation, JIT/JEA, audit, detection, and response. | Know which controls are missing. |
| Fix plan | Order by permission reduction, rotation, policy, segmentation, detection, and training. | Executable in stages. |
| Verification | Permission queries, policy simulation, log hits, access failure/success path verification. | Risk reduction is provable. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Confirm business impact first for directory changes, account disabling, credential rotation, policy rollout, and permission convergence.
- Do not output real user passwords, hashes, tokens, cookies, or abusable tickets.
- Minimize references to personal identity information in BloodHound or logs.

## Verification Checklist
- Permissions: before/after role/ACL/policy diffs.
- Authentication: MFA/conditional-access hit logs.
- Detection: key event IDs, SIEM queries, and samples.
- Zero trust: control-matrix completeness and residual risk.

## Anti-Patterns
- Listing only attack paths without a business-acceptable fix order.
- Disabling all accounts or forcing rotation across the board.
- Ignoring service accounts and automation tasks.
- Assuming a control works with no log verification.

## Merged Sources
- `ad-pentest`
- `credential-access`
- `identity-security`
- `lateral-movement`
- `privilege-escalation`
- `zero-trust`

## Nearby Skills on This Machine
- `source-command-ad-pentest`
- `source-command-privesc`
- `zeroize-audit`

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
