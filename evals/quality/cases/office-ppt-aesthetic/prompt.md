# Quality Eval Prompt: Office PPT Aesthetic Gate

Use `coff0xc-office-doc-tools` to turn the attached operating review outline into a high-taste editable PPTX plan and delivery package.

Goal: produce a reviewable output package for a leadership operating review deck.

Required output directory shape:

```text
responses/office-ppt-aesthetic/
├── deck-outline.md
├── design-system.md
├── contact-sheet-plan.md
├── comeback-scorecard.md
├── render-checks/
│   └── contact-sheet.png
└── final/
    └── operating-review.pptx
```

Constraints:
- Do not treat file existence as quality.
- Do not use generic card-grid/dashboard deck language.
- Do not invent metrics beyond the provided outline.
- `final/operating-review.pptx` must be a real OOXML PPTX package, not a renamed or empty placeholder.
- The deck must contain editable slide text, chart/proof structure, source notes, and enough layout variety for automated structure checks.

Required evidence:
- `deck-outline.md` must include a claim spine: each non-appendix slide has a claim title, proof object, and source/data note.
- `design-system.md` must lock typography, palette, chart grammar, connector/container grammar, footer/source rules, and banned motifs.
- `contact-sheet-plan.md` must show macro-layout diversity and call out weak/repeated slides.
- `comeback-scorecard.md` must score or explicitly assess story, specificity, rhythm, whitespace, chart clarity, typography, restraint, precision, and coherence.
- `render-checks/contact-sheet.png` must be a valid PNG render/contact-sheet evidence file. If native rendering is unavailable, create deterministic visual evidence from the slide plan and state the limitation in `comeback-scorecard.md`; do not use an empty renamed file.
