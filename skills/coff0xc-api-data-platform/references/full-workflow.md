# Full Workflow

This file is the on-demand extended workflow for `coff0xc-api-data-platform`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Make interfaces, data, and command-line tools into stable contracts: inputs explicit, outputs machine-processable, errors diagnosable, changes compatible, data migratable.

## Applicable Scenarios
- Designing or implementing REST/GraphQL/OpenAPI, database schemas, migrations, data-access layers, CLIs, or SDKs.
- Turning web/API docs, curl, OpenAPI, SDKs, or local scripts into composable tools.
- Checking interface compatibility, pagination, authentication, error models, idempotency, or data consistency.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-api-data-platform ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Web/API security vulnerability audits go to `coff0xc-secure-code-appsec`.
- Production database migrations, data deletion, and remote write operations must be confirmed first.
- Do not write real tokens, cookies, accounts, or customer data in examples.

## Execution Principles
- Read project files, configuration, call sites, existing style, and available tools before concluding or changing files.
- Turn user goals into verifiable completion criteria; record uncertain but low-risk details as assumptions and keep going.
- When current facts, versions, CVEs, cloud services, GitHub status, pricing, external APIs, or papers are involved, check real sources and mark the evidence level.
- When code changes are involved, keep the minimal correct change and prefer existing frameworks, scripts, tests, and local tools.
- Only commands, tests, builds, scans, or manual checks that were actually run may be written as verified.
- Before deletion, remote writes, production, credentials, payment, push, PR/Issue, CI/CD, permission, or infrastructure changes, get explicit authorization first.

## Capability Matrix
| Capability area | Coverage | Execution points |
| --- | --- | --- |
| API design | REST resources, GraphQL schema, OpenAPI, versioning, error model | Contracts are stable and can generate clients. |
| Authentication and authorization | API key, OAuth, session, scope, tenant, RBAC | State auth boundaries and least privilege clearly. |
| Data model | entities, relations, indexes, constraints, transactions, concurrency, consistency | Migrations have validation and rollback strategies. |
| Query and pagination | filter, sort, cursor, offset, rate limit, partial response | Behavior stays stable at large data volumes. |
| CLI/SDK | command tree, configuration, environment variables, JSON/NDJSON, dry-run, doctor | Suitable for automation and script composition. |
| Data platform | ETL, schema drift, data quality, audit logs, reruns, and idempotency | Data pipelines are recoverable. |
| Compatibility evolution | breaking change, deprecation, feature flags, migration notes | Users can upgrade smoothly. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| api-design | Interface resources, OpenAPI, request/response, error codes, versioning strategy. |
| database | Schema, migrations, indexes, transactions, SQL/NoSQL, backup and recovery. |
| cli-creator | Composable CLIs, SDK wrapping, JSON output, doctor/dry-run. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Contract discovery | Read existing routes, schemas, OpenAPI, SDKs, READMEs, tests, and client call sites. | Know the existing interface style. |
| Model design | Define entities, permissions, state machines, errors, pagination, idempotency, and compatibility requirements. | The contract contains no ambiguous behavior. |
| Implementation path | Prefer reusing existing controller/service/repository/CLI frameworks. | Change boundaries are clear. |
| Data security | Check input validation, parameterized queries, sensitive fields, log de-identification, and permission checks. | Data does not leak or cross authorization. |
| Verification | Run interface tests, migration dry-runs, local samples, CLI help/json output. | The user can reproduce it. |
| Documentation delivery | Update OpenAPI/README/examples with no real credentials included. | The contract can be used. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Production database migrations, data backfills, deletion, and remote API writes must be confirmed.
- Before changing a public API or breaking compatibility, state the impact scope.
- When generating GitHub/cloud CLI automation, do not execute remote writes by default.

## Verification Checklist
- Interfaces: schema/contract tests, local curl samples, error paths.
- Database: migration up/down, constraints, index explain, transaction tests.
- CLI: `--help`, no-config errors, read-only commands, JSON output parsing.
- SDK: type checks, sample code, and exception handling.

## Anti-Patterns
- Collapsing all API errors into 500 or vague strings.
- Pagination, sorting, and filtering with no stable contract.
- Migrations with no rollback or data validation.
- CLI output fit only for humans, not machine parsing.

## Merged Sources
- `api-design`
- `database`
- `cli-creator`

## Nearby Skills on This Machine
- `cli-creator`
- `gh-cli`

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
