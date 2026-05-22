# Complex Workflow

Use this only for L2/L3 work: multi-file features, cross-domain vibe coding, architecture/API/schema/auth changes, multi-agent implementation, or tasks where the user explicitly asks for a full workflow. Do not use it for small bug fixes, one-file edits, simple explanations, or routine UI/Office/security tasks that one specialist skill can finish.

## Operating Model

Keep two loops separate:

1. **Execution loop**: understand, implement, verify, repair.
2. **Quality loop**: review against spec, code quality, architecture, and final integration.

The workflow is a state machine, not a ceremony. Enter the smallest state that makes the task safe and productive.

| Level | Use when | Required artifacts | Review gates |
| --- | --- | --- | --- |
| L0/L1 fast path | simple command, explanation, one-file or narrow reversible fix | none or short notes in final response | targeted validation only |
| L2 task workflow | multi-file feature, repo repair, CI failure, UI/API work | `prd.md` or equivalent task brief; optional `implement.md` | spec-lite + code review + targeted tests |
| L3 complex workflow | cross-domain, architecture/API/schema/auth/security/UI/data/Office mix, multiple workers | `prd.md`, `design.md`, `implement.md` or equivalent persistent state | spec review, code review, architecture review, integration validation |
| L4 gated workflow | production, credentials, deletion, paid services, push/PR/deploy/CI permissions | explicit authorization and rollback plan | stop until authorized |

## Context Injection

Inject only current state, not the whole history:

- active phase,
- current objective,
- acceptance criteria,
- relevant files,
- last gate result,
- blockers,
- next action.

Do not inject full logs, old brainstorms, stale plans, or every jsonl entry unless debugging the workflow itself.

## Artifacts

Use artifact files only when they reduce ambiguity.

| Artifact | Required for | Contents |
| --- | --- | --- |
| `prd.md` | L2/L3 tasks | goal, non-goals, users/workflows, inputs/outputs, acceptance, risk gates |
| `design.md` | architecture/API/schema/auth/multi-domain work | chosen approach, alternatives rejected, data flow, module boundaries, risks |
| `implement.md` | multi-phase implementation or worker handoff | tasks, owners, files, validation commands, done/blocked state |

Light tasks can keep this in the final response or local plan. Do not create these files just to satisfy the workflow.

## Phase 1 - Intake

Entry criteria: user asks for a task that might need more than one step.

Actions:

1. Identify goal, inputs, outputs, constraints, risk level, and likely primary skill.
2. If the task is L0/L1, exit to fast path.
3. If L2/L3, create or update the minimum useful artifacts.
4. Ask at most 1-3 blocking questions. If assumptions are low-risk, proceed and label them.

Exit criteria: the task has an owner skill, acceptance criteria, and a risk level.

## Phase 2 - Repository And Evidence Scan

Entry criteria: task needs local files, existing product behavior, logs, screenshots, data, or docs.

Actions:

1. Read repo rules, README, manifests, lockfiles, and relevant entry points.
2. Find tests, build scripts, routes, components, schemas, and prior user changes.
3. Record only evidence that changes decisions.
4. Stop scanning once implementation impact is clear.

Exit criteria: current structure, affected files, and validation path are known.

## Phase 3 - Grill / Clarify

Entry criteria: implementation could branch in materially different ways.

Actions:

1. Ask only blocking questions that affect output, risk, or irreversible choices.
2. Prefer concrete options when possible.
3. If no answer is needed, continue with explicit assumptions.

Exit criteria: no blocking ambiguity remains.

## Phase 4 - Strategy Decision

Entry criteria: goal and evidence are sufficient to choose a route.

Actions:

1. Decide current-session implementation, subagent delegation, or separate worktree.
2. Decide default implementation flow or TDD.
3. Choose primary skill and support skills.
4. Define gates for each phase before implementation starts.

Decision rules:

- Current session: tightly coupled work, small/medium scope, or unclear codebase.
- Subagent: independent research, review, verification, or disjoint implementation.
- Worktree: large isolated branch work where merge conflicts are manageable.
- TDD: bugfixes, parser/calculation logic, regressions, API behavior, security-sensitive rules.

Exit criteria: there is a short executable plan with gates.

## Phase 5 - Architecture Guidance

Entry criteria: design risk is high, or changes touch architecture, API/schema/auth/data flow, multi-skill coordination, or multiple modules.

Actions:

1. Write design constraints into `design.md` or the active plan.
2. Name module boundaries, data flow, state ownership, and validation points.
3. Add rejected alternatives only when they prevent likely wrong turns.

Exit criteria: implementers can change code without guessing architecture.

## Phase 6 - Implementation Loop

Entry criteria: plan is sufficient and risk gates are clear.

Actions:

1. Implement the smallest coherent slice.
2. Run targeted validation immediately after each slice.
3. Update `implement.md` or progress state with done/blocked/next.
4. Do not let two workers edit the same files.
5. Preserve user changes and lockfile discipline.

Exit criteria: all required slices are implemented and targeted validation has run or been explained.

## Phase 7 - Quality Gates

Entry criteria: implementation claims are ready for review.

Run gates in order, but skip gates that do not match the task level:

1. **Spec review**: Does the result satisfy `prd.md` and non-goals?
2. **Code review**: Bugs, regressions, error paths, tests, sensitive data, diff hygiene.
3. **Architecture review**: Boundaries, data flow, contracts, auth, scalability, compatibility.
4. **Deep architecture review**: only for L3 multi-domain or high-risk architecture changes.

If a gate fails, return to the smallest implementation step that fixes it. If the same gate fails twice, stop repeating the same route and revisit strategy.

Exit criteria: matched gates pass or residual risk is explicitly documented.

## Phase 8 - Integration

Entry criteria: implementation and reviews passed.

Actions:

1. Update specs or docs if implementation intentionally changed the plan.
2. Merge local worker results in the main session if subagents/worktrees were used.
3. Run integration validation: build, test, typecheck, lint, browser smoke, Office render, or security checks as relevant.
4. Do not push, PR, deploy, delete, or modify production without explicit authorization.

Exit criteria: final validation has run or blockers are documented.

## Phase 9 - Finish

Entry criteria: validation is complete or blocked for a known reason.

Actions:

1. Summarize completed work.
2. Summarize real validation.
3. State remaining risk.
4. State the next useful action.
5. Mark workflow state done if the task tracker exists.

Exit criteria: the user can tell what changed, what was proven, and what remains.

## Gate Selection

| Change type | Minimum gates | Extra gates |
| --- | --- | --- |
| one-file bugfix | targeted test + code review | none |
| repo repair / CI | repro + targeted test + code review | full build/test if cheap |
| UI implementation | browser/screenshot/console + UI review | responsive/e2e if critical |
| API/schema/auth | contract tests + code review + architecture review | migration/backward compatibility check |
| security-sensitive fix | targeted exploit/regression check + AppSec review | detection/logging/control evidence |
| Office artifact | open/render/structure checks | native Office/human review for final delivery |
| multi-worker implementation | owner/file map + merge review + build/test | deep architecture review |

## Stop Conditions

- Same approach fails twice.
- Same review gate fails twice.
- Scope grows beyond about 2x the initial task.
- A destructive, external, production, credential, paid, push/PR, deploy, or CI-permission action appears.
- Validation cannot run and the reason is unknown.

When stopped, report the failed action, evidence, ruled-out causes, likely cause, and next step.
