# Quality Eval Prompt: Office DOCX Reading And Format Gate

Use `coff0xc-office-doc-tools` to review and lightly edit the attached DOCX-structure notes.

Goal: produce a Word delivery package that proves the agent understood document structure, preserved formatting intent, and checked comments/redlines/rendering instead of only extracting text.

Required output directory shape:

```text
responses/office-docx-format/
├── reading-map.md
├── style-token-map.md
├── edit-plan.md
├── render-checks/
│   ├── page-1.png
│   └── page-2.png
└── final/
    └── vendor-risk-review.docx
```

Constraints:
- Do not overwrite the source.
- Do not claim layout quality from text extraction alone.
- Do not use fake headings, fake bullets, or tables for ordinary prose.
- The DOCX may be a placeholder in this fixture, but the notes must prove structure and format gates were followed.

Required evidence:
- `reading-map.md` must identify headings, sections, tables, comments, tracked changes, headers/footers, fields, metadata, and unresolved risks.
- `style-token-map.md` must mention real Word styles, numbering, table geometry, margins, type scale, paragraph rhythm, headers/footers, and table gate.
- `edit-plan.md` must mention preserving the original, minimal local edits, comment anchors, redline/tracked-change structural checks, and render limitations if any.
- `render-checks/page-1.png` and `render-checks/page-2.png` must exist as page render evidence. If rendering is unavailable, create placeholders and state the limitation in `edit-plan.md`.
