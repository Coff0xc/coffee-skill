# Usage Guide

## Basic Flow

1. Install the `skills/` folders into your Codex skill directory.
2. Restart or refresh Codex so it re-indexes skill metadata.
3. Ask naturally in Chinese or English.
4. If no specific skill triggers, invoke `coff0xc-skill-router`.
5. For security tasks, confirm authorization scope before active testing or remote actions.

## Why Use This Pack

Use `coffee-skill` when you want the agent to follow a repeatable workflow instead of improvising from scratch. The skills are organized around work domains, not tiny one-off commands, so the agent can route broad requests such as "audit this project", "design this RAG system", or "fix this CI/CD risk" to a fuller checklist.

The pack is useful when a task needs:

- project inspection before edits,
- evidence levels instead of unsupported claims,
- validation commands before saying work is complete,
- security boundaries for authorized defensive work,
- manual fallback when automatic skill triggering fails.

## Recommended Manual Invocations

```text
使用 coff0xc-skill-router 帮我选择合适 skill
使用 coff0xc-software-engineering 修复这个项目的测试失败
使用 coff0xc-ai-agent-rag 设计一个 RAG Agent
使用 coff0xc-api-data-platform 设计这个 REST API 和数据库 schema
使用 coff0xc-ui-doc-output 优化这个 dashboard
使用 coff0xc-secure-code-appsec 审计这个 Web/API 项目
使用 coff0xc-cloud-devsecops 检查 Docker、K8s、CI/CD 和供应链风险
使用 coff0xc-detection-response 写检测规则和应急响应流程
```

## Example Use Cases

### Software Engineering

Use `coff0xc-software-engineering` for multi-file coding tasks, tests, refactors, scripts, and local Git summaries.

Expected behavior:

- inspect the project first,
- follow existing style,
- make minimal correct changes,
- run available validation,
- report what passed and what remains risky.

Good prompts:

```text
使用 coff0xc-software-engineering 修复这个 repo 的 failing tests，并说明验证结果
Use coff0xc-software-engineering to refactor this module without changing behavior.
```

### AI Agent And RAG

Use `coff0xc-ai-agent-rag` when the task involves agents, tool calling, retrieval, memory, prompts, evaluations, cost, latency, or observability.

Expected behavior:

- define inputs and outputs,
- separate deterministic steps from model judgment,
- design retrieval and citation behavior,
- add evaluation examples,
- plan failure recovery.

Good prompts:

```text
使用 coff0xc-ai-agent-rag 设计一个带引用、缓存和失败降级的企业知识库助手
Use coff0xc-ai-agent-rag to review this tool-calling agent design.
```

### API And Data Platform

Use `coff0xc-api-data-platform` for REST, GraphQL, OpenAPI, database schema, migrations, CLI, SDK, and data contract work.

Good prompts:

```text
使用 coff0xc-api-data-platform 设计这个 billing API、错误码、分页和 schema
Use coff0xc-api-data-platform to turn this curl workflow into a stable CLI.
```

### UI, Docs, Reports

Use `coff0xc-ui-doc-output` for frontend UI, dashboards, PDF/Word/report output, translation, and polish work.

Good prompts:

```text
使用 coff0xc-ui-doc-output 优化这个 dashboard，并用截图检查移动端
Use coff0xc-ui-doc-output to create a clean PDF-ready report from these findings.
```

### Defensive Security

Use the security-scoped skills for authorized review, detection, hardening, and reporting.

Expected behavior:

- confirm scope and authorization,
- collect evidence,
- distinguish verified facts from assumptions,
- avoid weaponized guidance,
- produce detection, hardening, verification, and remediation steps.

Good prompts:

```text
使用 coff0xc-secure-code-appsec 审计这个 Web/API 项目的认证和越权风险
使用 coff0xc-detection-response 根据这些日志写 Sigma/YARA 检测和验证样例
使用 coff0xc-vulnerability-lifecycle 分析这个 CVE 的影响、补丁和修复优先级
```

## Where It Fits

`coffee-skill` is a good fit for local engineering work, security review preparation, education, labs, internal documentation, and defensive operations. It is not a replacement for permission, production change control, legal review, or a dedicated security program.

## When Auto-Triggering Misses

Use the router:

```text
使用 coff0xc-skill-router 帮我选择合适 skill
```

The router exists because many skill clients select skills mainly from frontmatter `name` and `description`, not the body of `SKILL.md`.

## Install Notes

On Windows:

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

Avoid duplicate skill names across scanned directories. Duplicates can cause inconsistent triggering.
