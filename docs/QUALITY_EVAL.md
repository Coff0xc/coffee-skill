# Quality Evaluation

Trigger evals answer one question: "does this prompt route to the right skill?" Quality evals answer a harder question: "does the skill force the agent to produce reviewable, high-quality work?"

This repository includes artifact-level fixtures for areas where routing metrics are not enough. The default quality command now scores checked-in golden responses, including real `.pptx`, `.xlsx`, and `.docx` OOXML packages. Use `--fixture-only` only when you want schema/path validation without scoring artifacts.

| Case | Skill | What it tests |
|---|---|---|
| `ui-admin-dashboard-visual-gate` | `coff0xc-ui-doc-output` | Reworking an AI-template dashboard into a SaaS/admin UI with product routing, design tokens, state coverage, accessibility evidence, anti-template cleanup, real PNG evidence, HTML-to-render audit, console cleanliness, overlap/clipping checks, and aesthetic scoring evidence. |
| `dev-repo-repair-ci-gate` | `coff0xc-software-engineering` | Repairing a failing Python repo from CI logs while reading local rules, using the fast inner loop, preserving lockfile discipline, fixing source behavior, and leaving root-cause evidence. |
| `dev-js-api-repair-gate` | `coff0xc-software-engineering` | Repairing a failing JavaScript API helper with Node behavior assertions, invalid-input hardening, CI evidence, and package-lock noise detection. |
| `composition-workflow-execution-gate` | `coff0xc-skill-router` | Proving autonomous multi-skill composition executed as stages with skills, inputs, artifacts, gates, rerouting, and final verification, not only top-N skill selection. |
| `office-ppt-aesthetic` | `coff0xc-office-doc-tools` | Producing a real PPTX package with claim spine, design-system lock, contact-sheet plan, comeback scorecard, editable slide objects, chart parts, source notes, layout diversity, and render evidence. |
| `office-excel-parse` | `coff0xc-office-doc-tools` | Parsing messy CSV/workbook notes into a real XLSX package with raw/source preservation, assumptions, formulas, tables, chart parts, bounded references, recalculated key formulas, and render evidence. |
| `office-docx-format` | `coff0xc-office-doc-tools` | Reviewing/editing DOCX structure with real OOXML comments, comment anchors, tracked changes, styles, numbering, table geometry, headers/footers, fields, rels, and page render evidence. |

## Files

- `evals/quality/eval-set.json`: cases, required artifacts, and assertions.
- `evals/quality/cases/*/prompt.md`: task prompt for each quality fixture.
- `evals/quality/cases/*/input/`: files the agent should inspect and repair.
- `evals/quality/golden-responses/*/`: committed scoring fixtures used by the default release gate.
- `scripts/run_quality_eval.py`: fixture validator and response scorer.
- `scripts/build_quality_golden_responses.py`: deterministic helper for rebuilding the committed golden artifacts.
- `evals/quality/quality-eval-results.json`: generated machine-readable report.
- `evals/quality/quality-eval-results.md`: generated readable report.

## Run The Release Gate

```powershell
python .\scripts\run_quality_eval.py
```

Default mode scores `evals/quality/golden-responses/` and exits non-zero on any failed assertion. It opens the Office files as OOXML zip packages and checks:

- PPTX package parts, slide count, editable text shapes, chart/diagram objects, chart XML parts, source notes, layout signatures, color diversity, and non-placeholder PNG render evidence.
- XLSX workbook parts, required sheet names, tables, chart XML parts, bounded formula text, formula-error literals, selected workbook cells, and deterministic recalculation for supported formulas such as `SUM`, `SUMIFS`, `COUNTA`, and `COUNTIFS`.
- DOCX package parts, comments XML, comment anchors, tracked insert/delete tags, Word styles, numbering definitions, table geometry (`tblGrid`/`tcW`), headers/footers, fields, relationships, content types, and non-placeholder page PNG evidence.
- UI HTML structure, design tokens, responsive/focus CSS, semantic tags, ARIA, state terms, long-token text-fit risks, valid PNG screenshots, render-audit HTML hash, console errors/warnings, overlap/clipping counts, and aesthetic score dimensions.
- Python and Node behavior checks for repo-repair fixtures, plus requirements/package lockfile churn detection.
- Multi-skill workflow trace structure, required skills, stage terms, phase inputs/artifacts/gates, reroutes, and final verification commands/results.

To validate only prompt/input/assertion schema without scoring artifacts:

```powershell
python .\scripts\run_quality_eval.py --fixture-only
```

## Score Fresh Agent Outputs

Run an agent on each prompt and save outputs under a response directory:

```text
evals/quality/responses/
├── ui-admin-dashboard-visual-gate/
│   ├── output/
│   │   └── index.html
│   ├── screenshots/
│   │   ├── desktop.png
│   │   └── mobile.png
│   ├── render-audit.json
│   └── evaluation-notes.md
├── dev-repo-repair-ci-gate/
│   ├── src/
│   │   └── billing.py
│   ├── requirements.lock      # optional; if present it must match input
│   └── repair-notes.md
├── dev-js-api-repair-gate/
│   ├── src/
│   │   └── usage.js
│   ├── package-lock.json      # optional; if present it must match input
│   └── repair-notes.md
├── composition-workflow-execution-gate/
│   ├── workflow-trace.json
│   └── workflow-summary.md
├── office-ppt-aesthetic/
│   ├── deck-outline.md
│   ├── design-system.md
│   ├── contact-sheet-plan.md
│   ├── comeback-scorecard.md
│   ├── render-checks/
│   │   └── contact-sheet.png
│   └── final/
│       └── operating-review.pptx
├── office-excel-parse/
│   ├── workbook-plan.md
│   ├── parse-audit.md
│   ├── formula-checks.md
│   ├── render-checks/
│   │   └── dashboard.png
│   └── final/
│       └── billing-exceptions.xlsx
└── office-docx-format/
    ├── reading-map.md
    ├── style-token-map.md
    ├── edit-plan.md
    ├── render-checks/
    │   ├── page-1.png
    │   └── page-2.png
    └── final/
        └── vendor-risk-review.docx
```

Then run:

```powershell
python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses
```

The runner checks required files, required terms, banned AI-template patterns, render-audit evidence, workflow traces, lockfile churn, Office QA evidence, and behavior-specific Python/Node assertions. It exits non-zero on failed assertions.

## Rebuild Golden Fixtures

After changing assertion semantics or fixture expectations, rebuild the deterministic golden responses and rerun the gate:

```powershell
python .\scripts\build_quality_golden_responses.py
python .\scripts\run_quality_eval.py
```

## Limits

These checks are deterministic and intentionally narrow. They do not replace human taste review, live browser automation, native Office render inspection, Excel's full calculation engine, Word layout review, visual diffing, or real project CI execution. They are a release guard that makes the skill's quality gates testable instead of only aspirational.
