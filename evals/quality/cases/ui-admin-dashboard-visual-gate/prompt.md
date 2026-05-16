# Quality Eval Prompt: UI Admin Dashboard Visual Gate

Use `coff0xc-ui-doc-output` to repair the attached `bad-dashboard.html`.

Goal: turn it into a production-quality SaaS/admin dashboard screen, saved as `output/index.html`.

Constraints:
- Do not add external dependencies or remote assets.
- Do not create a marketing landing page.
- Keep the page as a working local HTML artifact.
- Remove generic AI-template styling such as neon gradients, card walls, fake people/company names, and meaningless KPI claims.
- Preserve the domain: billing operations and invoice exceptions.

Required evidence:
- Create `evaluation-notes.md`.
- Include a short `UI Need Package`.
- State the product type and why that changes density/layout.
- Describe the design system choices: tokens, spacing, radius, color, typography, and components.
- Cover populated, empty, loading, error, disabled, hover/focus, long-content, and mobile states.
- State how desktop/mobile browser validation should be performed.
- Save render evidence as `screenshots/desktop.png` and `screenshots/mobile.png`.
- Create `render-audit.json` linking the HTML hash to screenshot evidence, console cleanliness, overlap/clipped-text checks, and aesthetic scoring. If a browser is unavailable, state that limitation in `evaluation-notes.md` and still provide deterministic visual evidence instead of empty renamed files.

Expected output directory shape:

```text
responses/ui-admin-dashboard-visual-gate/
├── output/
│   └── index.html
├── screenshots/
│   ├── desktop.png
│   └── mobile.png
├── render-audit.json
└── evaluation-notes.md
```
