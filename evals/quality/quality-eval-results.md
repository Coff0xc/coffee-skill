# Quality Evaluation Report

This report is generated from `evals/quality/eval-set.json` by `scripts/run_quality_eval.py`.

Unlike trigger evals, these cases define artifact-level quality checks for actual task outputs.

## Summary

- Cases: 5
- Mode: responses
- Fixture errors: 0
- Responses dir: `evals/quality/golden-responses`
- Passed cases: 5
- Failed cases: 0
- Assertion pass rate: 1.0

## Fixture Validation

No fixture errors.

## Response Results

### ui-admin-dashboard-visual-gate

- Skill: `coff0xc-ui-doc-output`
- Passed: `True`
- PASS `ui-output-html-exists`: evals/quality/golden-responses/ui-admin-dashboard-visual-gate/output/index.html exists
- PASS `ui-uses-semantic-design-tokens`: all terms found
- PASS `ui-covers-state-and-responsive-gates`: all terms found
- PASS `ui-avoids-generic-ai-visuals`: no banned patterns found
- PASS `ui-notes-prove-quality-gates`: all terms found
- PASS `ui-desktop-screenshot-exists`: evals/quality/golden-responses/ui-admin-dashboard-visual-gate/screenshots/desktop.png exists
- PASS `ui-mobile-screenshot-exists`: evals/quality/golden-responses/ui-admin-dashboard-visual-gate/screenshots/mobile.png exists
- PASS `ui-desktop-screenshot-is-real-png`: png dimensions 1280x800, required >= 900x600
- PASS `ui-mobile-screenshot-is-real-png`: png dimensions 390x844, required >= 320x600
### dev-repo-repair-ci-gate

- Skill: `coff0xc-software-engineering`
- Passed: `True`
- PASS `dev-fixed-billing-file-exists`: evals/quality/golden-responses/dev-repo-repair-ci-gate/src/billing.py exists
- PASS `dev-fixes-currency-and-rate-paths`: all terms found
- PASS `dev-behavior-passes-fixture-tests`: normalize_amount=1200.50, invoice_total=243.00
- PASS `dev-no-unnecessary-dependency-noise`: matches reference
- PASS `dev-notes-prove-repair-loop`: all terms found
### office-ppt-aesthetic

- Skill: `coff0xc-office-doc-tools`
- Passed: `True`
- PASS `ppt-final-artifact-exists`: evals/quality/golden-responses/office-ppt-aesthetic/final/operating-review.pptx exists
- PASS `ppt-real-ooxml-package-has-editable-visual-system`: {"chart_or_diagram_objects": 3, "chart_parts": 1, "distinct_colors": 7, "layout_signatures": 6, "round_rects": 0, "slides": 6, "source_note_slides": 6, "text_shapes": 42}
- PASS `ppt-claim-spine-present`: all terms found
- PASS `ppt-design-system-lock-present`: all terms found
- PASS `ppt-contact-sheet-and-scorecard-present`: all terms found
- PASS `ppt-avoids-template-language`: no banned patterns found
- PASS `ppt-render-evidence-exists`: evals/quality/golden-responses/office-ppt-aesthetic/render-checks/contact-sheet.png exists
- PASS `ppt-render-evidence-is-real-png`: png dimensions 1280x720, required >= 900x500
### office-excel-parse

- Skill: `coff0xc-office-doc-tools`
- Passed: `True`
- PASS `excel-final-artifact-exists`: evals/quality/golden-responses/office-excel-parse/final/billing-exceptions.xlsx exists
- PASS `excel-real-workbook-has-sheets-formulas-tables-and-chart`: {"charts": 1, "formulas": 12, "recalculated_formulas": 8, "shared_strings": 0, "sheets": ["Assumptions", "Checks", "Dashboard", "Model", "Raw", "Source"], "tables": 2}
- PASS `excel-parse-audit-covers-data-shape`: all terms found
- PASS `excel-workbook-structure-auditable`: all terms found
- PASS `excel-formula-checks-present`: all terms found
- PASS `excel-no-hardcode-language`: no banned patterns found
- PASS `excel-render-evidence-exists`: evals/quality/golden-responses/office-excel-parse/render-checks/dashboard.png exists
- PASS `excel-render-evidence-is-real-png`: png dimensions 1280x720, required >= 900x500
### office-docx-format

- Skill: `coff0xc-office-doc-tools`
- Passed: `True`
- PASS `docx-final-artifact-exists`: evals/quality/golden-responses/office-docx-format/final/vendor-risk-review.docx exists
- PASS `docx-real-ooxml-has-comments-redlines-styles-rels`: {"comment_anchors": {"end": 3, "ref": 3, "start": 3}, "comments": 3, "fields": 3, "numbering_defs": 9, "rels": ["http://schemas.microsoft.com/office/2007/relationships/stylesWithEffects", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/customXml", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/fontTable", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/header", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/webSettings"], "style_count": 164, "tables": 1, "tblGrid": 2, "tcW": 20, "tracked_deletions": 1, "tracked_insertions": 1}
- PASS `docx-reading-map-covers-structure`: all terms found
- PASS `docx-style-token-map-present`: all terms found
- PASS `docx-edit-plan-preserves-review-structure`: all terms found
- PASS `docx-no-text-only-claim`: no banned patterns found
- PASS `docx-render-evidence-page-1-exists`: evals/quality/golden-responses/office-docx-format/render-checks/page-1.png exists
- PASS `docx-render-evidence-page-2-exists`: evals/quality/golden-responses/office-docx-format/render-checks/page-2.png exists
- PASS `docx-render-evidence-page-1-is-real-png`: png dimensions 850x1100, required >= 700x900
- PASS `docx-render-evidence-page-2-is-real-png`: png dimensions 850x1100, required >= 700x900
