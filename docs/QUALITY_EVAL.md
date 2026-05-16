# Quality Evaluation

Trigger evals answer one question: "does this prompt route to the right skill?" Quality evals answer a harder question: "does the skill force the agent to produce reviewable, high-quality work?"

This repository includes artifact-level fixtures for the two areas where routing metrics are not enough:

| Case | Skill | What it tests |
|---|---|---|
| `ui-admin-dashboard-visual-gate` | `coff0xc-ui-doc-output` | Reworking an AI-template dashboard into a SaaS/admin UI with product routing, design tokens, state coverage, accessibility evidence, anti-template cleanup, and browser validation notes. |
| `dev-repo-repair-ci-gate` | `coff0xc-software-engineering` | Repairing a failing Python repo from CI logs while reading local rules, using the fast inner loop, preserving lockfile discipline, fixing source behavior, and leaving root-cause evidence. |

## Files

- `evals/quality/eval-set.json`: cases, required artifacts, and assertions.
- `evals/quality/cases/*/prompt.md`: task prompt for each quality fixture.
- `evals/quality/cases/*/input/`: files the agent should inspect and repair.
- `scripts/run_quality_eval.py`: fixture validator and response scorer.
- `evals/quality/quality-eval-results.json`: generated machine-readable report.
- `evals/quality/quality-eval-results.md`: generated readable report.

## Validate Fixtures

```powershell
python .\scripts\run_quality_eval.py
```

Fixture mode checks that prompts, input files, references, and assertion schemas are complete. It does not grade an agent output.

## Score Agent Outputs

Run an agent on each prompt and save outputs under a response directory:

```text
evals/quality/responses/
├── ui-admin-dashboard-visual-gate/
│   ├── output/
│   │   └── index.html
│   ├── screenshots/
│   │   ├── desktop.png
│   │   └── mobile.png
│   └── evaluation-notes.md
└── dev-repo-repair-ci-gate/
    ├── src/
    │   └── billing.py
    ├── requirements.lock      # optional; if present it must match input
    └── repair-notes.md
```

Then run:

```powershell
python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses
```

The runner checks required files, required terms, banned AI-template patterns, and lockfile churn. It exits non-zero on failed assertions.

## Limits

These checks are deterministic and intentionally narrow. They do not replace human taste review, browser screenshots, visual diffing, or real CI execution. They are a release guard that makes the skill's quality gates testable instead of only aspirational.
