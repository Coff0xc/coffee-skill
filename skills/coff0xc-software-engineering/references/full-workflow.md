# Full Workflow

This file is the on-demand extended workflow for `coff0xc-software-engineering`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Land rough development requirements as runnable, testable, maintainable local engineering changes. By default, interrupt the user less: first check the project, record assumptions, make the minimal correct change, run available verification, then deliver with evidence.

## Applicable Scenarios
- Single-repo or multi-module code implementation, bug fixes, failing tests, script writing, local refactoring, and test backfill.
- Development tasks that need end-to-end delivery: pages, dashboards, admin panels, APIs, CLIs, background jobs, local tools, integration glue code.
- Repos that will not run, builds that fail, unclear dependency scripts, error chains that need locating.
- Local Git checks, diff summaries, and pre-commit candidate notes, without push or remote state changes.

## Not Applicable
- One-line commands, pure explanations, simple concept checks: answer directly.
- Pure AI Agent/RAG/Prompt architecture design: go to `coff0xc-ai-agent-rag`; if the task requires actually wiring Agent/RAG into the application, this skill owns engineering implementation and follows that skill's design constraints.
- Pure API/database contract design: go to `coff0xc-api-data-platform`; if the task requires implementing interfaces and migrations, this skill owns delivery.
- Pure UI visual polish: go to `coff0xc-ui-doc-output`; if the task requires changing frontend code, this skill owns implementation and checks against the UI verification requirements.
- Deep security audit: go to `coff0xc-secure-code-appsec` or the matching security skill.

## Risk Levels
| Level | Scope | Behavior |
| --- | --- | --- |
| L0 | Stable concepts, simple commands, no file changes | Answer directly or run the obvious command, marking what is unverified. |
| L1 | Single file or local reversible change | Check related files, minimal patch, run narrow verification. |
| L2 | Multi-file, multi-module, end-to-end feature | Give a short plan, implement per module, verify and re-check after each module. |
| L3 | Architecture/API/schema/auth/AI/security-sensitive logic/major decisions | Check official or source evidence, define a verification strategy, then implement. |
| L4 | Production, credentials, payment, deletion, remote writes, push/PR, CI/CD, permissions, infrastructure | Stop the relevant actions; get explicit authorization first. |

Escalation rules: escalate when the blast radius grows; anything involving current facts, versions, external APIs, or security conclusions is at least L3; anything externally visible or irreversible is L4.

## Default Behavior
- Decide low-risk details that can be reasonably inferred directly, and write them down as assumptions.
- Prefer following the repo's existing frameworks, package managers, scripts, tests, naming, and error-handling style.
- Implement the locally correct solution first; do not introduce new frameworks, new dependencies, or parallel systems for hypothetical futures.
- Do not roll back changes the user did not ask to roll back; read a dirty worktree carefully before collaborating.
- Commands, tests, builds, lint, and browser checks may only be written as "verified" after actually running them.
- If the same path fails twice in a row, stop repeating it; switch approaches or explain what is blocking.

## Default Fast Path
Ordinary development tasks follow this order:

1. Read the minimal necessary context: repo rules, related entry points, existing changes, and available scripts.
2. Set the minimal impact surface: which files must change, which files are untouched, how to verify.
3. Implement directly: small patches, no unrelated refactoring or new-framework migration.
4. Run available verification: narrow first, then wider; run test/typecheck/lint/build/browser smoke when runnable.
5. Short close-out: completed items, real verification, remaining risk, next steps.

Do not create quality evals, workflow traces, golden responses, long skill graphs, or release check reports for ordinary tasks. Enter the heavy gates only when the user explicitly asks for skill quality validation, review, eval, release, push, or CI/benchmark gates.

Complex-task escalation rules:

- L2 multi-file implementation: needs a `prd.md` or equivalent task brief, and an `implement.md` when necessary; run targeted validation after implementation.
- L3 architecture/API/schema/auth/multi-domain tasks: the router organizes primary/support skills, writes a `design.md` when necessary, then enters the implementation loop.
- Multi-worker or worktree: each worker must have independent file ownership; the main session owns merging, final build/test, and review.
- If the same implementation path or the same review gate fails 2 times in a row, stop repeating and return to strategy decisions.

## Confirm First
- Deleting files, dropping tables, clearing caches, migrating real data, force pushing, modifying main/master, hard reset.
- Push, publish, deploy, create/close/comment on PRs or Issues, send external messages.
- Using production credentials, external accounts, paid APIs, cloud resources, CI/CD permissions, or infrastructure.
- Changing authentication/authorization, payments, permission models, or production configuration when the risk cannot be isolated through local reversible changes.

## Work Loop
```text
Restore context -> Requirements package -> Impact surface -> Short plan -> Module loop -> Integration verification -> Final audit -> Delivery
```

### 1. Restore Context
Check the real project first; do not guess from memory.

- Read `AGENTS.md`, `CLAUDE.md`, README, manifest, lockfile, framework configuration, env example, test scripts; when editing a subdirectory, read the nearby README/AGENTS/dev notes along the path first.
- Check `git status --short`, current branch, and existing changes.
- Use `rg --files`, `rg`, language tooling, or project scripts to find entry points, call sites, tests, and build commands.
- If `task_plan.md`, `progress.md`, or `findings.md` already exists, read and continue them.
- Identify package managers and tool versions: npm/pnpm/yarn/bun, poetry/uv/pip, cargo, go, maven/gradle, bazel, and whether the lockfile should stay on its original generating tool version.

Completion criterion: know the project type, available commands, the user's existing changes, main entry points, and boundaries not to touch.

### 2. Requirements Package
Do not interview at length. Compress the user requirement into one executable package:

| Field | What to write clearly |
| --- | --- |
| Goal | What the end user, system, or maintainer must be able to do. |
| Users / workflow | Main path, failure path, admin/system path. |
| Inputs / outputs | Data, files, interfaces, pages, commands, events, or background tasks. |
| UI surface | Routes, components, states: loading, empty, error, success, disabled. |
| API surface | endpoint/action, request/response, validation, auth/permission. |
| Data model | entity, relations, migrations, compatible reads, fixture. |
| Non-goals | What this round does not do, to avoid scope creep. |
| Assumptions | Low-risk inferences and risk level. |
| Acceptance | Feature paths, failure paths, tests, typecheck/lint/build, UI smoke. |
| Risk gates | Production, credentials, payment, remote writes, deletion, public release, CI/CD permissions. |

For large tasks, write the requirements package into a plan or progress file; small tasks can keep it in the reply or internal plan only.

### 3. Impact Surface
Confirm before writing code:

- Entry points, routes, commands, components, services, models, schemas, configuration, and tests.
- Call chains, data flow, state ownership, error paths, permission boundaries.
- Tests to add/update, and the smallest runnable verification command.
- Whether docs, examples, types, schemas, migrations, or snapshots need syncing.

Completion criterion: can state which files to change, why, and how to verify.

### 3.5 Fast Inner Loop
Mature large repos usually do not do a full build every time. Find the project's recommended fast path first, then widen verification gradually:

- Prefer project-provided watch, targeted test, filter, workspace commands, Storybook/component test, package-specific build.
- When a test fails, save one full output first, then search the error; do not rerun the same heavy test with different greps.
- CI failure reproduction should match CI mode, env, bundler, isolation, database/browser configuration as closely as possible; do not use local shortcuts to hide packaging or module-resolution problems.
- Submodule changes use the matching package/directory commands; cross-module interface changes then run integration or full commands.
- If the project requires generating test templates, fixtures, snapshots, schemas, or docs, prefer project scripts to generate them; do not hand-write inconsistent structures.

### 4. Module Loop
Run a full closed loop for each module:

```text
Module design -> Minimal implementation -> Narrow verification -> Self-review -> Fix -> Mark complete
```

Implementation requirements:

- Use existing abstractions and structured APIs; do not handle structured data with fragile string concatenation.
- Do not swallow exceptions, fake compatibility layers, or use test-only logic to hide real problems.
- New dependencies must have clear benefit and match the project's existing dependency habits.
- UI changes must cover loading, empty, error, success, disabled, mobile/desktop, and basic accessibility states.
- API/backend changes must cover input validation, error codes, boundary conditions, authentication/authorization, logging, and sensitive-information handling.
- Data/schema changes must consider migration, rollback, compatible reads, and test fixtures.
- Lockfiles update only when dependencies genuinely change; before regenerating a lockfile, check the original tool and version to avoid noise from pure tool-version differences.
- Temporary design notes, logs, and experiment scripts go where the project allows; with no convention, keep them local and uncommitted, and explain at the end.

### 5. Verification Strategy
Narrow first, then wider, scaling with risk.

| Change type | Minimum verification | Extended verification |
| --- | --- | --- |
| Python | `pytest` related cases, `ruff check`, type checks | Full tests, package build |
| JS/TS | Related test, `lint`, `typecheck` | `build`, browser smoke, e2e |
| Go | `go test ./...` or target package, `gofmt` | race, integration tests |
| Rust | `cargo test`, `cargo fmt --check` | `cargo clippy`, release build |
| Java | Target Maven/Gradle test | Full build, integration tests |
| C/C++ | Target build and unit tests | sanitizer, valgrind, platform builds |
| Shell/PowerShell | Syntax check, dry-run, path boundaries | Minimal sample run |
| UI | Local page open, screenshot/browser smoke, console check | Responsive and key-flow e2e |

When verification is impossible, explain: what environment is missing, which command did not run, what the risk is, and what the user can run next.

### 5.5 CI / Regression Failure Triage
When the user gives CI, test, lint, build, or production regression signals:

- Order by blocking severity first: build/typecheck/lint > unit tests > integration/e2e > flaky/visual.
- Assume the failure is real; reproduce it first or locate it from logs; do not use known flakiness as an excuse not to fix it.
- Distinguish new failures, pre-existing failures, platform/environment failures, and test errors; each gets a different fix strategy.
- After two consecutive failures on the same path, stop blind reruns and return to the call chain and minimal reproduction.
- Before fixing a test, confirm the test covers real behavior; do not just change assertions to fit a wrong implementation.

### 6. Final Same-Category Audit
Re-check the complete diff before delivery:

- Whether the requirements package and acceptance criteria are met.
- Whether duplicate models, duplicate state, parallel implementations, or dead code were produced.
- Whether frontend/backend/API/schema/types align.
- Whether errors, empty states, boundary conditions, permissions, and sensitive-information handling are complete.
- Whether tests cover real behavior, not just the happy path.
- Whether temporary files, debug logs, hardcoded paths, secrets, and machine-private information were cleaned up.
- Git hygiene: stage only related files, never `git add .`; do not commit local plans/logs/screenshots/temporary output unless the user explicitly asks.

## Engineering Gates Borrowed from High-Star Repos
The following are generic patterns distilled from mature open-source engineering and high-star agent skills, rewritten as this skill's execution requirements:

| Gate | How to execute |
| --- | --- |
| Local rules first | Before any code, read the instructions, scripts, lockfiles, and test conventions at the root and near the target path. |
| Fast feedback | Use target test/watch/filter to narrow the failure surface first, then run wider verification. |
| CI-equivalent reproduction | CI issues must match CI environment variables, bundler, isolation, database, and browser mode. |
| Modular merging | Each module gets narrow verification and self-review as soon as it is done, so cross-module breaks are not found only at the end. |
| Dependency discipline | Check existing dependencies first; new dependencies need clear benefit; lockfiles get no tool-version noise updates. |
| Change hygiene | Change only the requested scope; stage only related files; keep changes the user did not ask to roll back. |
| Real tests | Tests cover behavior and failure paths; do not fake coverage with snapshots or happy paths. |
| UI collaboration | Frontend implementation is delivered by this skill, but must apply the UI state/visual acceptance gates of `coff0xc-ui-doc-output`. |

## Release / Skill Improvement Self-Test
Use only when the user asks to "confirm whether the dev skill is actually good," "improve the dev skill," "don't just pile on trigger words," "validate before release," or "run the gates before pushing." Ordinary repo repair does not run the quality eval here, unless it is the current repo's release requirement.

Do not just change frontmatter. Calibrate first with the real repair fixtures in the repo:

- See `evals/quality/cases/dev-repo-repair-ci-gate/`: inputs include `AGENTS.md`, README, CI logs, lockfile, source code, and failing tests.
- Qualifying output must include the fixed `src/billing.py` and `repair-notes.md`; if `requirements.lock` is output, it must match the input unless dependencies genuinely changed.
- `repair-notes.md` must demonstrate: requirements package, fast inner loop, CI leads, pytest verification, root cause, and lockfile discipline.
- Run `python .\scripts\run_quality_eval.py` to check fixture completeness; with real agent output, run `python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses`. The runner loads the candidate `billing.py` and runs behavioral assertions, avoiding keyword-only false passes.
- Quality eval is a minimum behavioral baseline; it does not replace real-project typecheck, lint, build, browser smoke, or CI.

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| dev | End-to-end development, low-confirmation delivery, module loop, integration verification, and final audit. |
| python-dev | Python projects, scripts, package management, typing, ruff/pytest/uv. |
| js-ts-dev | Node, React, TS, frontend/backend JS, npm/pnpm/yarn. |
| go-dev | Go modules, gofmt, go test, concurrency, and interface design. |
| rust-dev | Cargo, borrow/lifetime, traits, clippy, tests. |
| java-dev | Maven/Gradle, Spring, JVM tests, and type interfaces. |
| c-cpp-dev | C/C++ builds, CMake/Make, memory safety, and local tests. |
| shell-scripting | PowerShell/Bash automation, path safety, repeatable scripts. |
| testing | Test strategy, coverage gaps, regression cases, and verification commands. |
| code-simplifier | Local simplification, deduplication, readability, and complexity reduction. |
| git-workflow | Local Git checks, diff explanations, pre-commit preparation. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Anti-Patterns
- Changing code from a generic template without reading the project.
- Introducing a new framework, big abstraction, or extra service for a small problem.
- Changing only tests without fixing logic, or fixing appearances without locating the root cause.
- Swallowing exceptions, hiding failures, or returning fake success "for compatibility."
- Writing commands that were not run as passed.
- Deleting, pushing, publishing, or modifying remote state without user authorization.

## Output Contract
Keep only high-signal content in the final reply:

```markdown
Done:
- ...

Verification:
- [Verified] ...
- [Unverified] ...

Remaining:
- ...

Next steps:
- ...
```

On failure, use:

```markdown
Failed command / action:
Error message:
Already ruled out:
Likely causes:
Next steps:
```

## Manual Triggers
- `Use coff0xc-software-engineering to fix this repo's failing tests and explain the verification results`
- `Use coff0xc-software-engineering to build this feature end to end with tests`
- `Use coff0xc-software-engineering to implement this multi-file development task directly, with minimal confirmations`
