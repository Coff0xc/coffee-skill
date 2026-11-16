# Full Workflow

This file is the on-demand extended workflow for `coff0xc-secure-code-appsec`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Locate application security issues centered on code and evidence, and give verifiable fixes; keep high-risk requests defensive and within authorization boundaries.

## Applicable Scenarios
- Auditing code, configuration, routes, APIs, authentication/authorization, browser security, GraphQL, OAuth/OIDC, LLM/Agent security.
- Finding vulnerability root causes, confirming false positives, giving remediation recommendations, regression tests, and security reports.
- Analyzing authorized-test evidence, Burp projects, logs, SARIF, scan results, or source-leak risk.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-secure-code-appsec ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not run active scanning, brute force, exploitation, or bypass against unauthorized targets.
- Do not provide payloads, exploit chains, bypass scripts, or data-exfiltration steps that can directly attack third parties.
- Binary, mobile, IoT, cloud, or identity specialties go to the matching skill.

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
| Entry-point inventory | routes, controllers, GraphQL resolvers, webhooks, file upload, SPA routes | List user-controllable inputs. |
| Source/Sink | request parameters, headers, cookies, body, files, env, DB to command, SQL, template, file, URL, deserialize | Build reachable paths. |
| Authentication and authorization | session, JWT, OAuth, OIDC, tenant, role, object ownership, CSRF | Distinguish unauthenticated, low-privilege, and high-privilege paths. |
| Web/API vulnerabilities | injection, XSS, SSRF, XXE, path traversal, deserialization, IDOR, logic bug | Give verifiable evidence for each. |
| Browser/SPA | CSP, CORS, postMessage, Cookie, storage, DOM sink, extension manifest | Check frontend trust boundaries. |
| GraphQL | schema, resolver auth, batching, depth, introspection, IDOR, N+1 | Focus on field-level permissions. |
| LLM/Agent security | prompt injection, tool injection, data leakage, memory poisoning, agent CI/CD | Tool permissions and data boundaries first. |
| Backdoor detection | anomalous entry points, obfuscation, dynamic execution, suspicious networking, hidden accounts, anomalous scheduled tasks | Explain with code/configuration evidence. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| code-audit | Code-level source/sink, dangerous functions, taint analysis, and fixes. |
| web-pentest | Authorized web application validation, OWASP Top 10, and business logic. |
| api-discovery | Interface enumeration, route/docs/client inference, without unauthorized probing. |
| api-security-test | API authentication, authorization bypass, parameter validation, rate limiting, and error leakage. |
| graphql-pentest | GraphQL schema/resolver permissions and query complexity. |
| oauth-security | OAuth/OIDC redirect, state, PKCE, scope, token storage. |
| browser-security | DOM/CSP/CORS/Cookie/postMessage/extension security. |
| spa-pentest | Frontend routing, token exposure, source maps, frontend/backend permission mismatch. |
| llm-red-teaming | LLM/Agent defensive validation, prompt injection, and tool boundaries. |
| backdoor-detector | Webshells, anomalous dynamic execution, hidden admin endpoints, and malicious code traits. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Authorization and scope | Confirm assets, code, environment, test methods, prohibited actions, and output sensitivity. | Know what can be done. |
| Architecture/entry points | Read routes, schemas, auth middleware, controllers, clients, config, tests. | Attack surface and trust boundaries are clear. |
| Data-flow analysis | Trace validation, escaping, permissions, and exception handling from source to sink. | Candidate findings and evidence chains exist. |
| Validation priority | Order by reachability, impact, permissions, exploitation complexity, and data sensitivity. | Highest risk validated first. |
| Fix design | Give minimal fixes, test cases, compatibility impact, and logging/monitoring recommendations. | Actionable. |
| Report review | Every finding includes location, impact, evidence, reproduction conditions, fix, and validation. | Nothing exaggerated, no risk missed. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Confirm authorization and rate first for active scanning, authentication-bypass testing, file-upload testing, and external callback validation.
- Do not output real secret values, complete customer data, or payloads usable for unauthorized attacks.
- When using Semgrep/CodeQL and similar tools, record rules, versions, targets, and filtering criteria.

## Verification Checklist
- Static: file/line number, call chain, source/sink, permission paths.
- Dynamic: validate only in authorized local/test environments, recording request conditions and expected results.
- Tools: Semgrep/CodeQL/SARIF results need deduplication and false-positive analysis.
- Fixes: add regression tests, confirm the vulnerability path is blocked and normal paths remain.

## Anti-Patterns
- Listing only tool scan results without reachability and false-positive judgment.
- Treating a vulnerability title as evidence.
- Replacing fix and detection plans with an attacker view.
- Fixing only frontend validation, not the server-side boundary.

## Merged Sources
- `api-discovery`
- `api-security-test`
- `backdoor-detector`
- `browser-security`
- `code-audit`
- `graphql-pentest`
- `llm-red-teaming`
- `oauth-security`
- `spa-pentest`
- `web-pentest`

## Nearby Skills on This Machine
- `source-command-code-audit`
- `semgrep`
- `codeql`
- `variant-analysis`
- `burpsuite-project-parser`

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
