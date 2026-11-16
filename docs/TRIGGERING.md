# Triggering Guide

## Why Skills Sometimes Do Not Auto-Trigger

Most clients select skills from frontmatter metadata, especially `name` and `description`. The body of `SKILL.md` is usually loaded only after the skill has already triggered, so trigger words and capability terms must be in `description`.

## Trigger Strategy In This Pack

- Each capability skill starts with broad English capability terms.
- Descriptions include concrete deliverables, domain nouns, tool names, acronyms, and manual invocation cues without carrying long source-alias inventories.
- Release validation keeps frontmatter descriptions under a small metadata budget so daily skill selection stays fast.
- Each skill body starts with `Quick Rules (read this first for everyday tasks)`, then capability positioning, inputs, deliverables, boundaries, trust reasons, examples, and a short default output contract.
- `coff0xc-skill-router` is the fallback when auto-triggering misses and the lightweight autonomous composer for cross-domain tasks.
- Narrow prompts should go directly to the most specific skill. Broad prompts should trigger a small workflow graph and then execution, not a long proof artifact.
- Main `SKILL.md` files are optimized for runtime fast paths and kept under a release-enforced body-size budget. Full workflows live in `references/full-workflow.md`; route maps, special cases, and eval guidance live in `references/` and should be loaded only when the active task needs them.
- Local cross-directory consolidation is documented in [Installed Skill Inventory](SKILL_INVENTORY.md). Use it to reason about installed Codex/agent/plugin skills, duplicates, and promotion candidates; do not treat it as runtime skill content.

## Runtime Modes

| Mode | Trigger wording | Expected behavior |
|---|---|---|
| Execution mode | Normal task requests: fix, build, analyze, generate, edit, review a file, repair tests | Use one primary skill, add support skills only when needed, and execute the task. |
| Release / eval mode | `review the skill`, `run eval`, `quality test`, `release`, `push`, `CI gate`, `benchmark`, `confirm the skills really work` | Run trigger/quality/release gates and update generated eval artifacts. |

`workflow-trace.json`, golden responses, trigger evals, and quality evals belong to release/eval mode. They should not appear in normal task execution unless the user explicitly asks for them.

If a normal task feels slow, first check whether the agent unnecessarily invoked the router, loaded `references/full-workflow.md`, or entered release/eval mode. The expected fix is to return to the most specific skill and run only task-relevant validation.

## Composition Triggers

Use the router when the user says any of these:

```text
Decide which coff0xc skills are needed and chain them into a workflow.
This task spans frontend, backend, database, UI, and security — orchestrate it yourself.
Decide which coff0xc skills are needed and chain them into a workflow.
Orchestrate a vibe-coding workflow for this repo.
```

Expected router output:

- primary skill,
- only necessary supporting skills with one-line reasons,
- phase order with gates,
- skills intentionally not used,
- re-routing conditions if new evidence appears.

The router should keep this output short. After the lightweight plan, continue with the first actionable phase instead of stopping at planning.

## Manual Invocation

Use one of these phrases when auto-triggering misses:

| Skill | Manual phrase | Capability cues |
|---|---|---|
| `coff0xc-software-engineering` | `Use coff0xc-software-engineering ...` | Autonomous development, Code repair, Feature implementation, Test validation, CI triage, Fast inner loop, Build quality, Git collaboration |
| `coff0xc-ai-agent-rag` | `Use coff0xc-ai-agent-rag ...` | Agent architecture, RAG pipelines, Tool calling, Memory systems, Prompt engineering, Evaluation and observability |
| `coff0xc-api-data-platform` | `Use coff0xc-api-data-platform ...` | API contracts, Data models, Authentication and authorization, CLI/SDK, Data quality, Compatibility and evolution |
| `coff0xc-ui-doc-output` | `Use coff0xc-ui-doc-output ...` | Product UI, Design systems, Component architecture, Interaction states, Visual acceptance, Report output, Translation and polish |
| `coff0xc-office-doc-tools` | `Use coff0xc-office-doc-tools ...` | PPT/PPTX, DOCX/Word, PDF, Excel/XLSX, CSV/tables, Render validation |
| `coff0xc-research-drawio-diagram` | `Use coff0xc-research-drawio-diagram ...` | Research diagramming, Paper method diagrams, Model architecture diagrams, draw.io, Evidence tables, Inference annotations |
| `coff0xc-secure-code-appsec` | `Use coff0xc-secure-code-appsec ...` | Code auditing, Source/Sink, Authentication and authorization, Web/API security, GraphQL/OAuth, Backdoor detection |
| `coff0xc-cloud-devsecops` | `Use coff0xc-cloud-devsecops ...` | Cloud configuration, Container images, Kubernetes, CI/CD, Supply chain, Secrets management |
| `coff0xc-detection-response` | `Use coff0xc-detection-response ...` | Detection engineering, Threat hunting, SIEM/SOC, YARA/Sigma, Incident response, Forensic analysis |
| `coff0xc-vulnerability-lifecycle` | `Use coff0xc-vulnerability-lifecycle ...` | CVE research, Patch analysis, Impact assessment, Prioritization, Authorized validation, Remediation tracking |
| `coff0xc-identity-zero-trust` | `Use coff0xc-identity-zero-trust ...` | Identity governance, AD/Kerberos, IAM, Credential risk, Lateral-movement defense, Zero trust |
| `coff0xc-authorized-assessment` | `Use coff0xc-authorized-assessment ...` | Authorization scope, ROE, Attack surface, Control validation, Defense-oriented red teaming, Reporting |
| `coff0xc-binary-mobile-iot` | `Use coff0xc-binary-mobile-iot ...` | Reverse engineering, Mobile security, IoT firmware, ICS/OT, Cryptographic implementations, Crash/vulnerability leads |
| `coff0xc-blockchain-security` | `Use coff0xc-blockchain-security ...` | Smart contracts, DeFi, Asset flows, Permission models, Oracles/cross-chain, Multi-chain auditing |
| `coff0xc-compliance-architecture` | `Use coff0xc-compliance-architecture ...` | Security architecture, Threat modeling, Compliance mapping, Data security, Privacy, Maturity |
| `coff0xc-purple-deception` | `Use coff0xc-purple-deception ...` | Purple-team exercises, ATT&CK, Detection coverage, Response validation, Deception defense, Operations improvement |
| `coff0xc-network-protocol-security` | `Use coff0xc-network-protocol-security ...` | Protocol analysis, TLS/DNS/HTTP, Packet/pcap, Wireless/BLE/RF, State machines, Formal modeling |
| `coff0xc-skill-router` | `Use coff0xc-skill-router ...` | Autonomous orchestration, Multi-skill workflows, Task graphs, Phase gates, Re-routing |

## Troubleshooting

1. Ensure the folder name equals the frontmatter `name`.
2. Restart or refresh the client after copying skills.
3. Remove duplicate skill names across `.codex/skills`, `.agents/skills`, or other scanned locations.
4. Keep trigger terms in frontmatter `description`, not only in the Markdown body.
5. Use `coff0xc-skill-router` when unsure which skill should handle a request or when the task should compose multiple skills; do not use it as a mandatory prelude to every task.
6. If a task is broad, mention the expected deliverable, for example `detection rules`, `OpenAPI`, `draw.io`, `PPTX`, `XLSX`, `test validation`, `CI reproduction`, `design systems`, `state gates`, `browser screenshots`, or `risk lists`.
7. For autonomous composition, include wording such as `decide for yourself`, `chain skills`, `task graph`, `workflow`, `vibe coding`, or `chain the needed skills`.
