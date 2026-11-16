# Full Workflow

This file is the on-demand extended workflow for `coff0xc-skill-router`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Serve as the fallback entry for auto-triggering and the entry for multi-skill orchestration. When the frontend model does not automatically select a specific Coff0xc skill, or a task clearly spans multiple domains, quickly pick the primary skill and necessary support skills, then read and execute the workflow of the skill for the current stage.

## Why a Router Is Needed
- Many clients only use `name` and `description` for triggering; body content does not help the first trigger.
- Chinese requests, abbreviations, English tool names, and security-domain jargon can easily cause specific skills to miss triggers.
- Real tasks are often not completable by one skill: development can involve APIs, data, UI, security, Office delivery, or release verification.
- The router only handles routing and orchestration; it does not pack every specialist rule into one large context.

## Autonomous Orchestration Rules
1. If a more specific Coff0xc skill already fully covers the task, execute that skill directly; do not output a router plan.
2. If the task is cross-domain, build a minimal skill graph: pick one primary skill, then add support skills; do not stuff in every skill that looks related.
3. Each support skill must have a clear responsibility: add contracts, add UI, add security, add file delivery, add detection, add compliance, add verification.
4. Execute the skill the current stage needs first. After the stage completes, decide from evidence whether to continue, switch, or add a skill.
5. If the request involves security, production, credentials, remote writes, deletion, or paid actions, first apply the matching specialist skill's hard gates.
6. If the combination cannot be determined, give 2-3 candidate workflows and the smallest clarification questions; do not execute high-risk actions out of thin air.
7. Unless the user explicitly asks for evaluation/release/push/quality validation, do not generate workflow traces, golden responses, eval reports, or long self-justifying material.
8. Multi-stage complex development can use the state machine in `references/complex-workflow.md`; do not create `prd.md`/`design.md`/`implement.md` for light tasks.

## Skill Composition Loop
Use this loop only for cross-domain work or when the user explicitly asks to "chain skills yourself / orchestrate a workflow." Single-domain development, UI, Office, security, API, and similar tasks go straight into the matching specialist skill.

1. Read the task and evidence: goals, inputs, deliverables, constraints, risks, existing files.
2. Pick the primary skill: decide who owns the final result.
3. Add support skills: add only capabilities the current task genuinely needs.
4. Order the stages: write inputs, actions, outputs, and completion gates for each stage.
5. Execute the current stage: read that skill's `SKILL.md` and follow its workflow.
6. Re-route: adjust the graph when a new surface appears, e.g. expanding from dev to API/UI/AppSec/Office.
7. Close out: after all stage gates pass, summarize completed items, verified items, risks, and next steps.

## Common Composition Patterns
| Task type | Default primary skill | Common support skills | Composition intent |
| --- | --- | --- | --- |
| Vibe coding / full-stack feature | `coff0xc-software-engineering` | `coff0xc-api-data-platform`, `coff0xc-ui-doc-output`, `coff0xc-secure-code-appsec` | Fix/implement first, then add contracts, interface quality, and security regression |
| AI knowledge base / Agent app | `coff0xc-ai-agent-rag` | `coff0xc-api-data-platform`, `coff0xc-software-engineering`, `coff0xc-ui-doc-output` | Set the Agent/RAG architecture first, then land APIs, code, and UI |
| Data product / analytics dashboard | `coff0xc-api-data-platform` | `coff0xc-ui-doc-output`, `coff0xc-office-doc-tools`, `coff0xc-software-engineering` | Set the data contract first, then build the interface and deliverable files |
| Investor / executive deliverable | `coff0xc-office-doc-tools` | `coff0xc-ui-doc-output`, `coff0xc-api-data-platform`, `coff0xc-research-drawio-diagram` | Set the deliverable file first, then add narrative, data, and figures |
| Secure release review | `coff0xc-secure-code-appsec` | `coff0xc-cloud-devsecops`, `coff0xc-software-engineering`, `coff0xc-compliance-architecture` | Find risks first, then fix, verify, and organize launch evidence |
| Detection / incident workflow | `coff0xc-detection-response` | `coff0xc-vulnerability-lifecycle`, `coff0xc-cloud-devsecops`, `coff0xc-purple-deception` | Build detection/timeline first, then prioritize and validate coverage |

Read `references/router-map.md` for more combinations and the full routing table only during complex orchestration or router debugging.

## Output Format
Do not output this section for ordinary tasks; execute the matching specialist skill directly. For complex tasks, output a short orchestration first, without long theory:

```markdown
Workflow:
- Primary skill: <skill>
- Support skills: <skill>: <why needed>
- Not used for now: <skill>: <why not needed>

Stages:
1. <stage name> - using <skill>, gate: <verifiable completion criterion>
2. <stage name> - using <skill>, gate: <verifiable completion criterion>

Re-route conditions:
- If <evidence> is found, add/switch to <skill>.
```

It can be updated as execution goes, but do not treat the "initial workflow" as an unchangeable plan.

## Manual Trigger Phrasings
If auto-triggering is unstable, the user can write directly:

```text
Use coff0xc-secure-code-appsec to audit this project
Use coff0xc-ai-agent-rag to design a RAG Agent
Call coff0xc-cloud-devsecops to check K8s and CI/CD
Use coff0xc-office-doc-tools to generate an editable PPTX and check the preview
Write Sigma/YARA detections per coff0xc-detection-response
Use coff0xc-skill-router to help me pick the right skill
```

## Trigger Troubleshooting
- Skill directory names must match the frontmatter `name`.
- After installing or replacing, restart/refresh the client so the skill list is re-indexed.
- Keeping only `name` and `description` in frontmatter is most stable; trigger words must be written into the `description`.
- When identically named skills sit in multiple directories, they may compete for triggers; keep one primary version.
- Descriptions that are too short or only state abstract capabilities easily miss triggers; they should include Chinese, English, tool names, task names, and common abbreviations.

## On-Demand References

| Reference | When to read |
| --- | --- |
| `references/complex-workflow.md` | L2/L3 multi-file, multi-stage, multi-skill, architecture/API/schema/auth, multi-worker, or full vibe coding workflows. |
| `references/router-map.md` | Complex multi-domain orchestration, routing debugging, extended composition patterns, explaining why a skill was selected or excluded. |
