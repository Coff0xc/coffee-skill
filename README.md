# coffee-skill

[![CI](https://github.com/Coff0xc/coffee-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/Coff0xc/coffee-skill/actions/workflows/validate.yml)
![Skills](https://img.shields.io/badge/skills-18-2f855a)
![Trigger Eval](https://img.shields.io/badge/trigger_eval-131_cases-2563eb)
![Quality Eval](https://img.shields.io/badge/quality_eval-7_real_artifacts-7c3aed)
![License](https://img.shields.io/badge/license-source_available_noncommercial-b91c1c)
![Codex](https://img.shields.io/badge/Codex-AgentSkills-111827)

Turn Codex / AgentSkills-compatible assistants into reusable, verifiable, recoverable workflows without making ordinary tasks slow.

`coffee-skill` is an installable `SKILL.md` workflow pack. It is built for the three failure modes that hurt agentic coding work: the assistant chooses the wrong capability, produces work without evidence, or turns simple tasks into heavy process.

The design:

- **Narrow tasks go direct**: bug fixes, UI work, Office artifacts, AppSec review, and reports should use the most specific skill.
- **Cross-domain tasks compose**: the router selects a primary skill, adds only necessary support skills, sequences phases, defines gates, and re-routes when evidence changes.
- **Quality leaves evidence**: dev work shows diffs and validation, UI work shows state/screenshot/layout evidence, Office work opens OOXML packages, and security work keeps authorization boundaries explicit.
- **Fast by default**: every skill starts with quick rules; trigger evals, quality evals, golden responses, and workflow traces are release/eval gates.

This repository is publicly visible, but it is not open-source licensed. Personal learning, research, evaluation, and local noncommercial use are allowed with attribution preserved. Any commercialization, company internal production use, consulting deliverable, paid course, paid community, agent-pack bundling, hosted service, mirror, resale, or derivative publication requires prior notice to Coff0xc and written permission. Without written permission, there is no commercial authorization.

## 30-Second Setup

For personal learning, research, evaluation, and local noncommercial use:

```powershell
.\scripts\install_local_skills.ps1
```

The script moves old installed `coff0xc-*` folders into `~\.codex\skills-backup-coff0xc-*`, then copies the current repository version. Restart or refresh Codex, then try:

```text
Use coff0xc-software-engineering: this repo has failing tests; make the smallest repair and validate it.
```

If you do not know which skill to use:

```text
Decide which coff0xc skills are needed, chain them into a workflow, and complete this task.
```

## Choose An Entry Point

| Task | Use | Expected output |
|---|---|---|
| Repo repair, feature work, CI reproduction | `coff0xc-software-engineering` | diff, root cause, validation, residual risk |
| Frontend/UI/report polish, or formal PPTX/DOCX/XLSX | `coff0xc-ui-doc-output` / `coff0xc-office-doc-tools` | screenshot/browser evidence, or editable Office files with structure checks |
| Thesis defense rewrite from a thesis DOCX + old PPTX | `coff0xc-office-doc-tools` | restructured thesis content, defense narrative, editable PPTX, structure/preview checks |
| Agent/RAG, API/data contracts, research diagrams | `coff0xc-ai-agent-rag` / `coff0xc-api-data-platform` / `coff0xc-research-drawio-diagram` | architecture, schemas, evals, draw.io files, evidence tables |
| Security, compliance, incident response, identity, cloud, protocol, blockchain | matching `coff0xc-*` security skill | authorization scope, evidence, impact, remediation/detection/hardening |
| Cross-domain or unclear work | `coff0xc-skill-router` | primary skill, support skills, phase gates, re-routing conditions |

See the full [Skill Index](docs/SKILL_INDEX.md).

## Why These Skills Exist

| Common agent failure | How this pack handles it |
|---|---|
| Wrong capability or too much planning | Narrow tasks go direct; cross-domain tasks use the router; normal work does not run release gates. |
| Code changes without proof | Dev workflow reads repo rules, finds root cause, makes small diffs, validates, and avoids lockfile noise. |
| Template-looking UI | UI workflow checks product type, design system, states, responsiveness, accessibility, and screenshots/browser evidence. |
| Office files that only exist by name | Office workflow requires editable PPTX/XLSX/DOCX, render evidence, and OOXML structure checks. |
| Security work that drifts out of scope | Security workflows are authorization-first and evidence-based, with confirmation gates for risky actions. |

## Two Modes

| Mode | Use when | Assistant behavior |
|---|---|---|
| Execution mode | Everyday bug fixes, features, UI edits, Office artifacts, code review, reports | Pick the most specific skill, read minimal context, execute, run relevant validation, report briefly. |
| Release / eval mode | Explicit review, eval, quality test, release, push, CI, benchmark, or skill-quality request | Run trigger evals, quality evals, golden fixtures, workflow traces, docs/manifest sync, and release gates. |

Normal work should not start by proving the skill system. It should start by doing the task.

## Why Skills Felt Slow

The slow path came from loading release gates, long route tables, and detailed design checklists during ordinary work. The pack now uses a fast-path plus on-demand references:

- Every skill starts with `Quick Rules (read this first for everyday tasks)`: 3-4 hard gates and the default way to proceed.
- Normal tasks load only the top of the main `SKILL.md`: goal, boundary, core gates, and default output.
- Deep UI review, external skill merging, router debugging, and quality evals load `references/` only when needed.
- `coff0xc-skill-router` is only for uncertain or cross-domain work; narrow UI, dev, Office, or security tasks go directly to the specific skill.
- Multi-file, multi-stage, architecture/API/schema/auth, or multi-worker work can load `coff0xc-skill-router/references/complex-workflow.md`.
- Trigger evals, quality evals, workflow traces, and golden responses are release guards, not runtime ceremony.

## How This Differs

| Dimension | Typical skill repos | coffee-skill |
|---|---|---|
| Goal | Single-purpose prompts or tool notes | End-to-end workflows across engineering, AI/RAG, API/data, UI, Office, research diagrams, and authorized security |
| Orchestration | Users usually pick one skill manually | Narrow tasks go directly to one skill; cross-domain tasks use the router for primary/support skill selection, phases, gates, and re-routing |
| Routing | Mostly keyword matching | Positioning, inputs, deliverables, boundaries, verification, and an autonomous composition entry point |
| Proof | Usually proves the skill file exists | Trigger evals, quality evals, golden responses, and CI gates, used as release guards |
| Output | Often text advice | Diffs, screenshots, PPTX/DOCX/XLSX, draw.io files, reports, and verification evidence |
| Office | Often file generation or conversion | OOXML checks for PPTX slides/charts/text, XLSX formulas/tables/charts, DOCX comments/redlines/styles/rels |
| Development | Generic coding guidance | Repo rules, root-cause repair, minimal diffs, validation, and lockfile discipline |
| Safety | Mixed or implicit boundaries | Authorization-first security boundaries and confirmation gates for high-risk actions |
| Maintenance | Manual review | Manifest, docs, evals, golden fixtures, and CI keep behavior from drifting |

In short: many skill repos help an assistant know what to say. `coffee-skill` focuses on whether the assistant can organize capabilities, finish real work, and leave evidence.

## Autonomous Composition

For broad work, do not pre-select every skill. Ask the router for a lightweight workflow and then execute the first phase:

```text
Decide which coff0xc skills are needed, chain them into a workflow, and complete this task.
This vibe-coding task may include frontend, backend, data, security, and docs; orchestrate the skills yourself.
```

The router should produce a primary skill, only necessary supporting skills, phase order, gates, and re-routing conditions. For example, a SaaS feature may compose `software-engineering + api-data-platform + ui-doc-output + secure-code-appsec`, sequenced repo rules → data contracts → implementation → UI acceptance → security audit → tests/build.

Complex work can upgrade into a Trellis-style state machine: intake, repo evidence, blocking clarification, strategy decision, implementation loop, spec/code/architecture review, integration validation, and finish. This is only for L2/L3 tasks; simple tasks should not create `prd.md`, `design.md`, `implement.md`, or stacked review gates.

## How To Prompt

Most reliable format:

```text
Use <skill-name>:
Goal: ...
Input: ...
Deliverable: ...
Validation: ...
Limits: ...
```

If you know the skill, name it directly. If the task is clearly narrow, do not route first. If it is uncertain or cross-domain, start with `coff0xc-skill-router`.

Natural-language prompts work too:

```text
This Python project's pytest run is failing — locate the failing cases, make the minimal fix, then run tests and lint.
Turn this Markdown outline into an editable PPTX with charts, a narrative arc, preview validation, and the final file path.
Design a local knowledge-base assistant using Agent/RAG, with cited sources, caching, failure fallbacks, and an eval set.
Draw an editable draw.io research algorithm architecture diagram from this paper and the official GitHub.
```

See [Skill Index](docs/SKILL_INDEX.md) for the full capability map, recipes, and manual invocation examples; see [Coverage Matrix](docs/COVERAGE.md) for full domain coverage.

## Validation

These commands are release guards for this repository. They are not the default prelude for normal user work.

```powershell
python .\scripts\validate_release.py
python .\scripts\run_trigger_eval.py
python .\scripts\run_quality_eval.py
```

The trigger evaluation currently covers 131 local proxy cases, including short Office artifact prompts and extreme multi-skill composition prompts for research, top-tier development, authorized red-team planning, UI engineering, incident/crisis work, and protocol/IoT analysis.

The quality evaluation scores committed golden responses under `evals/quality/golden-responses/`. It checks real HTML/PNG UI evidence, imports and executes a repo-repair Python behavior assertion, and opens `.pptx`, `.xlsx`, and `.docx` as OOXML packages to verify slide/chart/text structures, workbook formulas/tables/charts/recalculated cells, and Word comments/redlines/styles/numbering/rels/table geometry.

It is a deterministic release gate, not a replacement for native Office rendering, full Excel calculation, human taste review, or real project CI.

### Office quality gates

| File | Gates | Failure mode |
|---|---|---|
| PPTX | Every slide starts with a conclusion-style title and an object to prove; lock the design system first; plan a contact sheet; avoid template feel and repeated layouts; check narrative, pacing, whitespace, fonts, and chart clarity with a comeback scorecard; deliver only after a render preview. | Pretty backgrounds only, stacked cards, vague titles, charts that prove nothing, no preview check. |
| Excel / CSV / XLSX | Check encoding, delimiters, headers, units, dates, nulls, outliers, and existing formulas/charts first; keep raw/source/assumptions; derive key values with formulas; trace key outputs; scan for formula errors; check chart and dashboard rendering. | Hand-split data, hardcoded computed results, overwritten source data, charts without sources, unscanned formula errors. |
| DOCX / Word | Read heading hierarchy, tables, comments, revisions, headers/footers, fields, and metadata first; use real styles, numbering, and table geometry; tables hold only true row/column data; render-check layout page by page where possible. | Claiming understanding from extracted text alone, fake headings/lists, tables wrapping long paragraphs, unchecked comment/revision anchors. |

### UI / Dev gates

- UI is judged not only on "the page opens" but on product-type routing, design system, state coverage, responsive behavior, accessibility, and screenshot evidence.
- Dev is judged not only on "the code changed" but on reading repo rules, reproducing the failure, finding the root cause, making the minimal fix, running available validation, and avoiding lockfile noise.

## Safety Scope

Security-related skills are defensive and authorization-scoped. They are for owned or explicitly authorized assets, local code/config review, logs, reports, labs, CTFs, training ranges, detection, hardening, verification, and reporting.

They do not provide guidance for unauthorized access, credential theft, persistence, detection evasion, C2, phishing collection, data exfiltration, or destructive actions. Production, credentials, paid services, remote writes, deletion, push, PR actions, cloud resources, and CI/CD permission changes require explicit authorization.

## Repository Layout

```text
skills/                 # Installable skill folders
docs/                   # Usage, triggering, coverage, provenance, i18n, sanitization
evals/                  # Trigger evals, quality evals, golden responses
scripts/                # Release validation and eval scripts
.github/workflows/      # CI validation
manifest.json           # Machine-readable skill inventory
LICENSE                 # Source-available noncommercial license
NOTICE                  # Attribution notice
```

## Documentation

- [Usage Guide](docs/USAGE.md)
- [Skill Index](docs/SKILL_INDEX.md)
- [Triggering Guide](docs/TRIGGERING.md)
- [Trigger Evaluation](docs/TRIGGER_EVAL.md)
- [Quality Evaluation](docs/QUALITY_EVAL.md)
- [Coverage Matrix](docs/COVERAGE.md)
- [Language References](docs/LANGUAGES.md)
- [Sanitization Notes](docs/SANITIZATION.md)
- [Provenance](docs/PROVENANCE.md)
- [Enforcement Guide](docs/ENFORCEMENT.md)
- [Takedown Template](docs/TAKEDOWN_TEMPLATE.md)
- [Trademark Policy](TRADEMARK.md)
- [Security Policy](SECURITY.md)

## License

From the current version onward, this repository uses a custom source-available noncommercial license. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

Personal learning, research, evaluation, and local noncommercial use are allowed with attribution preserved. Commercialization requires prior notice to Coff0xc and written permission. Unauthorized commercial use, company internal production use, consulting delivery, resale, paid redistribution, commercial hosting, paid course bundling, paid community use, paid agent-pack bundling, mirroring, or packaging into any product or service is not permitted.

Strict notice: unnotified commercial use, unauthorized commercial use, removal of attribution, removal of `LICENSE` / `NOTICE`, stripping source identifiers, false originality claims, or any implication of official Coff0xc authorization is not permitted. Coff0xc may use Git history, source identifiers, similarity analysis, purchase records, platform pages, and distributed artifacts as evidence for takedown requests, license enforcement, trademark/impersonation complaints, and legal claims.

`SKILL.md` files include source-level identifiers for copyright and origin evidence. They do not affect skill execution. To scan a suspected copy:

```powershell
python .\scripts\scan_provenance.py <suspected-folder>
```

This license change is not retroactive. Versions published before the change remain under the license terms that applied to those earlier versions.
