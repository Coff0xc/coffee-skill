# PPTX Defense Rewrite Workflow

Use this for thesis/project defense decks, graduation presentations, academic proposal defenses, and any task shaped like: source `.docx`/paper + existing `.pptx` -> rewritten defense PPT.

Do not load this for small PPT text edits. Use the fast PPT gate in `SKILL.md` instead.

## Runtime Rule

Do not guess installed plugin paths or hardcode versioned runtime paths. Use the tools already available in the active environment:

1. Prefer the active `presentations:Presentations` skill/plugin if it is loaded and callable.
2. If a versioned Presentations path is missing or mismatched, do not stop. Use workspace dependency discovery or Office document tools to read source files and build the deck.
3. If artifact-tool/Office render is unavailable, still produce a structurally valid `.pptx` with the best available local library, then state which render/visual checks could not run.
4. Never upload thesis, defense, student, client, or internal files to external services without explicit user approval.

The fallback sequence is:

```text
active Presentations plugin/tool
-> workspace dependency loader / bundled Office tools
-> local OOXML/Python/JS library fallback
-> content-only outline if no PPTX writer is available
```

Stopping condition: only stop before building when no local readable source exists, no local writer exists, or the requested output requires an external service that is not authorized.

## Inputs

Typical inputs:

- thesis or report `.docx`,
- old defense `.pptx`,
- images, charts, experiment screenshots, model diagrams, result tables,
- school/company template requirements,
- page count or defense duration.

First establish:

- output path,
- expected duration and slide count,
- whether the existing PPT is a content source, visual template, or weak draft to replace,
- whether the final deck must preserve a school template or logo,
- whether the material contains personal/student or institutional sensitive data.

## Phase 1 - Read Sources

Entry criteria: at least one source file exists.

Actions:

1. Read the DOCX structure: title, abstract, problem, methods, system design, experiments, results, conclusion, references, appendix clues.
2. Read the old PPTX slide list: titles, useful assets, weak pages, duplicated content, missing defense logic.
3. Extract reusable assets from the old PPT only when they are relevant and legally/user-provided.
4. Do not infer core research claims from filenames. Use document content.

Exit criteria:

- a short source map exists,
- old PPT slides are classified as keep/rewrite/drop,
- missing data or assets are known.

## Phase 2 - Defense Story

Entry criteria: source structure is understood.

Build a defense claim spine:

1. Title / identity / topic.
2. Research background and problem.
3. Research objective and contribution.
4. Related work or requirement analysis, only if needed for defense.
5. Method: model, algorithm, dataset, workflow, or system architecture.
6. Implementation: modules, UI, pipeline, deployment, or key engineering choices.
7. Experiments / evaluation / results.
8. Comparison, ablation, error cases, or limitations.
9. Conclusion and future work.
10. Q&A / thank-you page.

For a 10-15 minute undergraduate defense, default to 12-16 slides. Do not create 30+ slides unless the user asks.

Exit criteria: every slide has a claim title and proof object.

## Phase 3 - Design System

Entry criteria: story spine is stable.

Actions:

1. Choose one restrained academic visual system: title hierarchy, body size, accent color, figure/table style, footer/source style.
2. Avoid generic template cards, crowded paragraphs, random gradients, decorative icons, and repeating the same two-column layout.
3. Use visual proof objects: architecture diagram, YOLO/model pipeline, dataset examples, result table, metric chart, UI/system screenshots, error case grid.
4. Keep Chinese defense decks readable from a projector: short titles, large enough text, no dense paragraphs copied from the thesis.

Exit criteria: contact-sheet plan has distinct rhythms and no three consecutive same-layout slides.

## Phase 4 - Build Editable PPTX

Entry criteria: source map, claim spine, and design system are ready.

Actions:

1. Create a new PPTX rather than overwriting the old one.
2. Keep text, tables, charts, diagrams, and images editable where practical.
3. Use the old PPT only as source/template evidence, not as a blind base.
4. Name the final file with the topic, for example `YOLOv8-illegal-item-defense-rewrite.pptx`; do not use `output.pptx` or `deck.pptx`.
5. Keep scratch files under a task-specific workspace; only final deliverables go to the user-facing output directory.

Exit criteria: the PPTX exists, is non-empty, has the target slide count, and contains editable text shapes.

## Phase 5 - Verify

Entry criteria: PPTX has been built.

Required checks:

1. Open or inspect the PPTX package: slide count, slide XML, editable text, media, charts/diagrams if present.
2. Render or preview slides/contact sheet when available.
3. Check title/body overflow, blank slides, duplicated placeholders, missing images, unreadable charts, footer/source consistency.
4. Check defense coverage: background, objective, method/system, experiments/results, conclusion, Q&A.
5. If render is unavailable, state that only structural checks were completed and list remaining visual risk.

Exit criteria: structural checks pass and visual/render checks either pass or are explicitly disclosed as unavailable.

## Failure Recovery

- If the Presentations skill path/version is missing: switch to workspace dependency/Office tools; do not retry path discovery repeatedly.
- If DOCX extraction fails: inspect OOXML text or use available document reader; preserve the failure in notes.
- If PPTX rendering fails because LibreOffice or a renderer is missing: continue with OOXML/package checks and disclose render limitation.
- If the deck looks like copied thesis paragraphs: reduce text, convert to diagrams/tables, and re-run the contact-sheet review.
- If the output is image-only: rebuild as editable objects or explicitly state why an image-only slide is unavoidable.

## Final Response Contract

Return:

- final `.pptx` path,
- what was rewritten,
- source files used,
- validation completed,
- validation not completed and why,
- remaining manual review points.

Do not mention scratch scripts, internal plans, or temporary render files unless the user asks for them.
