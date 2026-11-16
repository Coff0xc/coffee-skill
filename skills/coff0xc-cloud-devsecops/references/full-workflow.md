# Full Workflow

This file is the on-demand extended workflow for `coff0xc-cloud-devsecops`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Assess cloud-native and delivery-chain risk in a read-only-first, evidence-based way, and output actionable hardening plans and verification paths.

## Applicable Scenarios
- Reviewing cloud configuration, IaC, container images, K8s manifests, CI/CD workflows, dependencies, and secret risks.
- Designing DevSecOps pipelines, security baselines, SBOM, dependency scanning, secret scanning, and release gates.
- Analyzing cloud account permissions, logs, network exposure, public storage, serverless permissions, and runtime risk.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-cloud-devsecops ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not connect to or modify production cloud accounts by default.
- Do not output complete discovered secret values.
- Cloud enumeration, takeover, bypass, or persistence requests for unauthorized targets become defensive recommendations.

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
| Cloud configuration | IAM, storage, network, security group, KMS, logging, backup, public exposure | Give evidence per provider and asset type. |
| Container images | Dockerfile, base image, root, capabilities, secrets, SBOM, CVE | Distinguish build-time from runtime risk. |
| Kubernetes | RBAC, namespace, Pod Security, NetworkPolicy, service account, admission, secrets | Least privilege and isolation first. |
| Serverless | function IAM, trigger, env, timeout, VPC, event source, dependency | Check permissions and event boundaries. |
| CI/CD | workflow permissions, OIDC, artifact, cache, pull_request, agent actions | Keep pipelines from being hijacked by inputs. |
| Supply chain | lockfile, SCA, license, maintainer risk, typosquat, dependency confusion, SBOM | Risk grading and alternative paths. |
| Secrets management | discovery, scope, rotation, revocation, KMS/HSM, access logs, least privilege | Report only location and handling process. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| cloud-security | AWS/Azure/GCP/IAM/storage/network/logs/CSPM. |
| container-security | Docker images, runtime, K8s security. |
| docker-k8s | Development/deployment container configuration and local validation. |
| serverless-security | Function permissions, event triggers, and cloud logs. |
| devsecops | CI/CD security gates, SAST/DAST/SCA, release process. |
| supply-chain-security | Dependencies, malicious packages, SBOM, lockfiles, and package sources. |
| secrets-management | Secret discovery, rotation, storage, and access audit. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Scope confirmation | Confirm cloud provider, account/project, repo, IaC, cluster, pipeline, and read-only boundaries. | No accidental production contact. |
| Asset inventory | Read Terraform/CloudFormation/K8s/Dockerfile/workflow/lockfile/env example. | Assets and entry points complete. |
| Risk review | Review by identity, network, data, runtime, supply-chain, and log-recovery layers. | Findings have evidence. |
| Prioritization | Order by public exposure, permission level, data sensitivity, exploitability, and fix cost. | Highest-value risks fixed first. |
| Fix plan | Give least privilege, policy snippets, configuration changes, pipeline gates, and rotation plans. | Executable and reversible. |
| Verification | Local lint/plan, read-only commands, policy simulation, scan reports, and audit-log validation. | Proves risk is reduced. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Confirm first before any cloud write, policy change, secret revocation, resource deletion, or pipeline permission change.
- Treat IaC apply, kubectl apply/delete, and workflow dispatch as remote/production risk.
- Confirm privacy and licensing before third-party scanners upload source code or SBOMs.

## Verification Checklist
- IaC: validate, fmt, plan, policy check.
- Container: build, trivy/grype, docker history, running-user check.
- K8s: manifest lint, RBAC can-i, namespace isolation check.
- CI/CD: workflow permission diff, trigger conditions, and secret usage paths.

## Anti-Patterns
- Pasting a provider best-practice checklist to the user without looking at the actual configuration.
- Repeating a discovered secret's full value.
- Fixing only image CVEs while ignoring root, capabilities, secrets, and network.
- Running cloud-modifying commands directly without confirmation.

## Merged Sources
- `cloud-security`
- `container-security`
- `devsecops`
- `docker-k8s`
- `secrets-management`
- `serverless-security`
- `supply-chain-security`

## Nearby Skills on This Machine
- `supply-chain-risk-auditor`
- `insecure-defaults`
- `agentic-actions-auditor`
- `devcontainer-setup`

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
