# Full Workflow

This file is the on-demand extended workflow for `coff0xc-office-doc-tools`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Deliver formal Office/PDF files that can be opened, edited, and checked. By default, treat "the user can take it straight into a presentation, review, archive, or further editing" as the completion standard.

## Applicable Scenarios
- Creating or improving PowerPoint/PPTX, slides, decks, and presentations.
- Creating, editing, commenting on, revising, and formatting DOCX/Word documents.
- Reading, generating, reviewing, splitting, merging, or checking PDFs.
- Creating, cleaning, analyzing, and formatting Excel/XLSX/CSV workbooks, charts, and formula models.
- Cross-file flows: PDF extraction into Excel, Excel charts into PPT, DOCX reports exported to PDF, PPT summaries sourced from Word/Excel.

## Division of Labor with Neighboring Skills
| Scenario | Prefer |
| --- | --- |
| Frontend pages, components, dashboards, browser UI | `coff0xc-ui-doc-output` |
| Formal PPTX/DOCX/PDF/XLSX file creation, editing, render validation | `coff0xc-office-doc-tools` |
| Paper algorithm figures, model structure figures, `.drawio` source files | `coff0xc-research-drawio-diagram` |
| Code generation or repo feature development | `coff0xc-software-engineering` |

If a task covers both UI and Office files, judge by the final deliverable first: a web page/app goes to UI; a PPT/DOCX/PDF/XLSX goes to this skill.

## Execution Principles
- First confirm output format, purpose, audience, file sources, whether the original must be kept, and whether sensitive information is included.
- Use structured tools where possible instead of fragile string concatenation; tables, formulas, paragraphs, slide objects, and OOXML should be handled structurally wherever possible.
- New files need a clear information architecture; editing existing files should stay as local as possible and not rearrange the whole document without reason.
- Verify after each major round of changes; fix verification failures first, and do not hide flaws in the final reply.
- Deliver only the files the user asked for in the end; preview images, temporary scripts, extracted text, and QA intermediate artifacts are not main deliverables unless the user asks for them.

## PPT Aesthetics Gate
Applies to PPT/PPTX tasks that create, redo, improve, or benchmark against a reference deck. The goal is not "it opens" but a deck with editing value, credible aesthetics, and a clear narrative.

- Write the claim spine first: every non-appendix slide must have one conclusion-style title, one main proof object, and necessary source or data notes. If a title still works after swapping in another company name, tighten it further.
- Lock the design system first: page size, background, font hierarchy, color usage, chart grammar, diagram/connector grammar, footer/source, title/kicker rules, allowed layout families, and banned motifs.
- Plan with a contact sheet: a 10-slide deck needs at least 5 macro layouts; no 3 consecutive slides with the same structure; no default card grids, decorative frames, templated dashboards, or marketing filler.
- Charts and diagrams must prove the title: prefer direct labels, use heavy legends sparingly; lines, arrows, connectors, containers, and labels must still express the same relationship after rendering.
- Brands and assets must have a source: do not hand-draw or imitate logos, mascots, product UIs, or customer marks; when something cannot be verified, express brand feel with typography, color, product language, and known data.
- Rendered QA is mandatory: render the full slide set or a contact sheet and check thumbnail rhythm, full-size text overflow, chart readability, image sharpness, source footers, and KPI/legend/connector completeness.
- Judge deliverability with a comeback scorecard: story, specificity, rhythm, whitespace, chart clarity, typography, restraint, precision, and coherence must have no obvious weak spot. When weak slides are found, rebuild the weakest 2-4 slides first instead of only fine-tuning.
- If only "functionally usable but aesthetically below standard" can be achieved, the final reply must state the remaining weaknesses explicitly; having a file output is not the same as a high-quality deck.

## Defense PPT Rewrite Gate
Applies to "paper DOCX/report + old PPTX -> rewritten defense PPT" tasks. By default this is not a light edit of the old deck but a rebuild of the defense narrative from the paper content, output as a new PPTX.

- First read the paper structure and the old PPT page structure; the old PPT is only a content/material/template reference — do not start generating from filenames or old PPT titles alone.
- Default output is a 12-16 slide undergraduate/project defense deck, unless the user gives duration, a school template, or a slide-count requirement.
- Must cover: research background, objectives/contributions, method or system architecture, key implementation, experiments/results, conclusions/outlook, Q&A.
- Every slide must have a conclusion-style title and a proof object: system architecture diagram, YOLO/model pipeline, dataset samples, result tables/figures, UI screenshots, false-positive/false-negative cases, and similar.
- Reusable images/screenshots/tables from the old PPT keep their source; school emblems/logos/third-party material with uncertain sources must not be imitated.
- On generation failure, continue down the fallback order: Presentations plugin -> workspace dependencies/Office tools -> local OOXML/Python/JS; stop only when no local read/write capability is available at all.
- Before delivery, at least run a PPTX package/OOXML structural check; when rendering is possible, run a contact-sheet/preview check; when it is not, state the remaining visual risk explicitly.

## Excel Data Parsing Gate
Applies to CSV/TSV/XLSX import, cleaning, analysis, modeling, dashboard, chart, and formula workbook work. The goal is auditable, computable, and further-editable — not a pretty table screenshot.

- Before reading, judge the data shape: source files, encoding/delimiters, headers, units, date/number formats, nulls, duplicate rows, outliers, and whether formulas/tables/charts/filters/conditional formatting already exist.
- For importing an existing workbook, do a compact inspect first: list sheets, used ranges, key tables, formula regions, styles, and charts; do not blindly re-lay out or overwrite formatting across the whole table.
- Prefer structured parsing for CSV/TSV; when cleaning is needed, keep auditable intermediate logic and avoid hand-written fragile splits. Multi-source data keeps a source/assumptions or raw/detail sheet.
- An analysis workbook's default structure: Executive Summary or Dashboard first, Source/Assumptions second, Model/Detail/Checks after; a simple tracker can be simplified but still needs clear titles, headers, and input areas.
- Derived results use formulas first: do not hardcode key calculations; formulas must not hide magic numbers — reference input/assumption cells; avoid whole-column references and use bounded ranges; cross-sheet formulas require creating the target sheet first.
- Audit suspicious key outputs by tracing or equivalent: check dependency chains, formula ranges, units, percentages, dates, and aggregation definitions. When model completeness depends on linked calculations, add a Checks area or Checks sheet.
- Charts must have an explicit data source: organize chart-ready data with helper ranges, linking to source data with formulas where needed; charts must not cover data, and axis units/formats/labels must be readable.
- Must verify: inspect values/formulas of key ranges, scan for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`, render key sheets/ranges, and check blank charts, truncated titles/numbers, column widths, frozen panes, filters, tables, and conditional formatting.
- If the user is only asking about table contents, do not change the file on your own; first read the values/formulas/table structure and answer.

## DOCX Reading and Formatting Gate
Applies to DOCX/Word reading, review, rewriting, commenting, revision, formatting, and generation. The goal is understanding document structure and keeping readable formatting, not just extracting text.

- Read a DOCX in layers first: sections/heading hierarchy, page count, paragraph types, tables/images/footnotes/headers/footers, comments, revisions, table of contents, cross-references, fields, and metadata clues.
- Layout conclusions cannot rest on text extraction or XML alone: render pages and check them one by one before delivery whenever possible; if rendering is unavailable, only claim structural/text checks were completed — do not claim the layout passed.
- Before creating or heavily revising a DOCX, pick a document archetype/preset first: memo, report, SOP, proposal, form, manual, brief, and similar; settle pages, margins, fonts, heading hierarchy, paragraph rhythm, lists, tables, callouts, headers/footers, and color tokens.
- Use real Word structure: headings use styles, lists use real numbering, tables use explicit column widths/cell padding/repeated headers; do not use fake headings, hand-typed bullets, manual numbering, or tables wrapping ordinary long paragraphs.
- Tables must pass a table gate: only genuinely tabular row/column data uses a table; sentence/paragraph content should become paragraphs, bullets, steps, callouts, or definition lists. Check table column widths, wrapping, vertical/horizontal alignment, margins, captions, pagination, and repeated headers.
- Editing an existing DOCX keeps the original by default with minimal, localized edits. Comments must anchor to specific locations; confirm before revising/accepting revisions/deleting comments/cleaning metadata/removing watermarks.
- Comments and revisions need double verification: rendering may show tracked changes but often does not show comments; structural checks of comments.xml, anchors, rels, content-types, or equivalent evidence are needed.
- After each meaningful batch of edits, re-render or re-check structure, focusing on clipping, overlap, missing glyphs, broken tables, spacing drift, header/footer misalignment, page numbers, and table-of-contents anomalies.
- At the end, distinguish: content structure understood, scope changed, pages/structure verified, and layout risks not verified.

## Quality Eval Self-Test
When the user asks to "confirm whether the Office skill is actually good," "improve the PPT/Excel/DOCX quality gates," or "don't just pile on trigger words," calibrate with the in-repo artifact-level fixtures:

- `evals/quality/cases/office-ppt-aesthetic/`: check claim spine, design-system lock, contact-sheet plan, comeback scorecard, render evidence, and the final PPTX.
- `evals/quality/cases/office-excel-parse/`: check encoding/delimiter/header/unit/date/null/duplicate/outlier audits of messy CSV/workbook notes, Raw/Source/Assumptions/Model/Checks/Dashboard structure, formula/trace/error scan/helper range, and dashboard render evidence.
- `evals/quality/cases/office-docx-format/`: check reading map, style/token map, minimal edit plan, comment/redline anchors, real styles/numbering/table geometry, and page render evidence.
- Run `python .\scripts\run_quality_eval.py` to score the real artifacts in `evals/quality/golden-responses/` by default: PPTX is unpacked and checked for slide XML/text shapes/chart parts/layout signatures, XLSX is checked for sheets/tables/charts/formulas with key formulas recomputed where supported, DOCX is checked for comments, anchors, tracked changes, styles, numbering, table geometry, rels, headers/footers, and fields.
- To check only prompt/input/assertion schemas, run `python .\scripts\run_quality_eval.py --fixture-only`; with real agent output, run `python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses`.
- Passing quality eval does not mean the Office files have passed human acceptance; PPT aesthetics, the full Excel formula engine, and page-by-page DOCX layout still need rendering by the matching tool or manual review.

## Capability Matrix
| File type | Typical capability | Verification focus |
| --- | --- | --- |
| PPT/PPTX | New decks, restructured stories, template changes, charts/tables/images, compressed storylines | Slide count, editable objects, preview images, no text overflow, clear charts/images |
| DOCX/Word | Reports, proposals, SOPs, comments, revisions, table of contents, tables, headers/footers | Original preserved, structure intact, comment/revision anchors, rendered pages, tables not clipped |
| PDF | Reading, review, generation, split/merge, layout checks, citation checks | Page count, page rendering, text-extraction cross-check, tables/images/page numbers, non-editable limits |
| Excel/XLSX/CSV | Data cleaning, formulas, summaries, charts, dashboards, templates, validation | Formula error scan, key-range inspect, chart sources, column width/freeze/format |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Task scoping | Pin down final format, input files, output directory, audience, sensitivity, and whether the original is kept. | Know which file to deliver; do not wrongly change the original. |
| File reading | Read file structure, page/slide/sheet counts, key text, tables, images, and metadata clues. | Do not guess content from filenames. |
| Content design | First settle the table of contents, page/slide/worksheet structure, data fields, and visual density. | Deliverable has a clear reading path. |
| Build/edit | Create or modify files with the right tool; preserve styles and editability. | File opens, content complete. |
| Verify and fix | Run render, preview, formula, structure, or export checks by file type. | Found issues are fixed or listed explicitly. |
| Final delivery | Give the final file path, verification results, residual risk, and next steps. | User can use it directly. |

## File-Type Gates
### PPT/PPTX
- For a new deck, write the narrative line first: theme, audience, conclusion per slide, evidence objects.
- Default output is an editable PPTX; do not turn whole slides into non-editable large images unless the user explicitly wants image-style output.
- When data charts are present, state the data source; do not invent numbers to look good.
- Final check: file exists, slide count is correct, preview/export is not blank, titles and body text do not overlap, images are clear, chart labels are readable.

### DOCX/Word
- When editing existing documents, keep the original and output a new file.
- Prefer local replacement for small changes; explain the reason when a rewrite is needed.
- Structured elements such as comments, revisions, table of contents, page numbers, tables, and cross-references need structural checks.
- Final check: file exists, page/section counts match expectations, rendering or preview shows no clipping/overlap, tables do not touch the edges, comments/revisions are kept or cleaned as required.

### PDF
- PDF reading can start with text extraction, but layout conclusions must be based on rendering or page images.
- PDF generation must be checked for page numbers, margins, fonts, tables, images, links, and citations.
- If rendering is impossible, state the reason and limit conclusions to "text/structure check"; do not claim the layout passed.
- Final check: file exists, page count is correct, pages render, key pages have no black blocks/garbled text/misalignment/clipping.

### Excel/XLSX/CSV
- Derived data uses formulas or auditable conversion steps first; do not hardcode key calculations as dead values.
- For CSV/TSV, confirm delimiters, encoding, headers, date/number formats, and nulls first.
- Charts and dashboards need explicit data-source ranges; when adding rows/columns, sync formulas, conditional formatting, and chart ranges.
- Final check: key-range values/formulas, error-value scan, chart/table preview, column width and frozen panes, output file exists.

## Verification Checklist
- File level: final file exists, is non-empty, has the correct extension, and can be opened or imported by the target tool.
- Content level: titles, sections, page/slide/sheet counts, key data, and user requirements are covered item by item.
- Visual level: render/screenshot/preview checks show no obvious clipping, overlap, garbled text, blank pages, or broken charts.
- Data level: formulas, reference ranges, error values, units, dates, percentages, and aggregation definitions are consistent.
- Security level: sensitive information, personal metadata, hidden comments, revision history, watermarks, and external links are handled as the user requires.

## Anti-Patterns
- Outputting only a paragraph of text and leaving the user to paste it into Office.
- Asserting the layout is fine from PDF/DOCX text extraction alone.
- Making a PPT out of non-editable screenshots without saying so.
- Hardcoding results in Excel that should be computed by formulas.
- Overwriting originals, deleting comments, accepting revisions, or cleaning metadata without confirmation.
- Inventing sources, numbers, citations, or legal/financial conclusions to make the layout look good.

## Merged Sources
- `documents`
- `presentations`
- `spreadsheets`
- `pdf`

## Nearby Skills on This Machine
- `documents:documents`
- `presentations:Presentations`
- `spreadsheets:Spreadsheets`
- `pdf`
- `coff0xc-ui-doc-output`

## Output Contract
```markdown
Done:
- ...

Deliverable files:
- [filename](absolute path)

Verification:
- [Verified/Could not verify] ...

Residual risks:
- ...

Next steps:
- ...
```
