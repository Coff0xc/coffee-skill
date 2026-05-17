# UI Generalized Rules

Use this reference only for substantial UI work, UI skill improvement, external skill merging, or visual-quality review. It distills reusable patterns from external UI/frontend skills without copying personal definitions, project paths, default-authorization language, or fixed taste rules.

## Source Merge Policy

- Extract workflows, gates, and review checks; do not copy personas, personal names, local paths, brand-specific tokens, or private project assumptions.
- Convert absolute rules into product-aware rules. Example: avoid one-note purple or blue-purple gradients unless brand context requires them; do not globally ban a hue.
- Convert locale rules into locale-aware rules. Dates, numbers, currency, units, and time zones follow the product locale and domain, not one hardcoded format.
- Remove unsafe default authorization statements. Production, credentials, paid resources, deletion, publication, push, PR/issue actions, and CI/CD permission changes still require explicit authorization.
- Treat tool-heavy Figma, browser, screenshot, and Playwright skills as route-only references unless their license and runtime match the current repo.

## Product Defaults

| Product type | Default quality bar |
| --- | --- |
| SaaS/admin/ops | Quiet, dense, scan-first; predictable navigation; tables, filters, forms, bulk actions, and audit states matter more than decorative hero sections. |
| Analytics/dashboard | Units, time ranges, filter scope, empty/error states, chart labels, axis meaning, and anomaly explanation must be visible. |
| Editor/tool | Workspace-first; stable toolbars; icon buttons with labels/tooltips; save, undo, loading, error, and keyboard paths are first-class. |
| Consumer/landing | First viewport must reveal the product, place, person, or offer with real or traceable visual assets; avoid empty gradient-first pages. |
| Design system | Tokens, variants, state matrix, accessibility notes, examples, and regression path are the deliverable. |
| Game/interactive | Feedback, animation, state machine, rules/physics engine choice, and playability matter more than static cover art. |

## Visual System Gates

- Scan tokens, CSS variables, theme files, Tailwind config, component libraries, Storybook, icon dependencies, and existing screenshots before designing.
- If no design system exists, derive a small local token map from the most repeated colors, type sizes, spacing, radius, shadow, and icon style.
- Prefer semantic tokens and component variants over scattered raw colors, magic spacing, and one-off class piles.
- Keep palettes multi-dimensional: avoid a whole page dominated by one hue family unless it is a deliberate brand requirement.
- Use icon libraries already present in the project. Avoid emoji as production UI controls because rendering and semantics vary.
- Keep icon stroke weight, optical size, label behavior, and hit targets consistent.

## State And Interaction Gates

- Cover populated, empty, loading, error, disabled, success, hover, active, selected, focus, long-content, missing-asset, and small-screen states when relevant.
- Use skeleton or structured loading for content regions; use a spinner only for short local actions.
- Put errors near the failing control or region, with retry or recovery when possible.
- Keyboard order, focus visibility, labels, ARIA names, contrast, reduced motion, and chart non-color cues are part of structure, not final polish.
- Stable dimensions matter for boards, tables, charts, toolbar buttons, cards, tiles, media, counters, and tabs; dynamic content should not resize the whole layout unpredictably.

## Data Display Gates

- Do not invent or silently derive business-critical totals. Use backend/source-of-truth data, workbook formulas, or document the formula and assumptions.
- Format numbers with grouping, units, currencies, percentages, signs, and precision appropriate to the domain.
- Dashboard controls should make time range, filter scope, sorting, pagination, and data freshness obvious.
- Tables need column widths, wrapping/truncation strategy, keyboard access, sticky headers when useful, and horizontal overflow behavior.
- For long lists or large tables, check pagination, virtualization, incremental loading, and empty/error behavior.

## Frontend Engineering Gates

- Detect framework, routing, styling, package manager, build tool, and test scripts before editing.
- Prefer existing component/data-fetching/state patterns. Add dependencies only when they remove real complexity and fit the project.
- Watch LCP, INP, and CLS risks: reserve image/media space, lazy-load noncritical media, avoid render-blocking fonts, and keep expensive work off the hot path.
- Debounce or throttle high-frequency input, scroll, resize, search, and save flows; handle cancellation and race conditions.
- Separate data acquisition from presentation. Use hooks/composables/services only where the project already uses that pattern or duplication is real.
- Avoid repeated full-page re-renders for dense dashboards; memoization, virtualization, and stable props are tools, not decoration.

## Visual Verification Gates

- Use the cheapest evidence that answers the question: DOM snapshot for locator/state truth, screenshot for visual composition, console/network checks for runtime health.
- For UI implementation, verify at least one desktop and one mobile viewport. Dense tools usually need a tablet or constrained panel width too.
- Check blank render, broken assets, console errors, text clipping, overlap, contrast, focus order, scroll traps, button usability, and form path.
- If a Figma design exists and tools are available, map design tokens/components to code tokens/components, document deviations, and compare screenshot evidence.
- If Playwright is available, prefer role/label locators and web-first assertions; avoid sleep-based checks.
- If screenshots cannot be produced, say the code is implemented but visual verification is blocked.

## Review Output

For UI review tasks, report findings first:

| Severity | Evidence | Why it matters | Fix |
| --- | --- | --- | --- |
| P0-P3 | File/line, screenshot, DOM, console, or command | Real user or workflow impact | Minimal actionable repair |

End with verification gaps and residual risk, not a design essay.

## Quality Eval Mode

Use this only when the user asks to verify or improve this skill pack, not during normal UI delivery.

- For UI quality, use `evals/quality/cases/ui-admin-dashboard-visual-gate/`.
- A valid response should include `output/index.html`, `screenshots/desktop.png`, `screenshots/mobile.png`, `render-audit.json`, and `evaluation-notes.md`.
- Evidence should prove product fit, design-system inspection, state coverage, accessibility basics, desktop/mobile screenshot checks, console cleanliness, and remaining limitations.
- Run `python .\scripts\run_quality_eval.py` for committed golden responses.
- To score real agent outputs, place them under `evals/quality/responses/<case-id>/` and run `python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses`.
- Passing the deterministic eval proves required evidence exists; it does not replace final screenshot review or human taste judgment.
