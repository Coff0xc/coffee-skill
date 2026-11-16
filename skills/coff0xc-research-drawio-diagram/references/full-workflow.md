# Full Workflow

This file is the on-demand extended workflow for `coff0xc-research-drawio-diagram`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Turn research algorithms, paper methods, model structures, or experiment flows into editable diagrams.net/draw.io `.drawio` architecture diagrams. Analyze structure from public sources or user-provided material before drawing; do not invent modules, connections, or innovations from memory.

## Applicable Scenarios
- The user asks to draw a research algorithm architecture figure, paper method figure, model pipeline, experiment flow, system framework, or comparison figure.
- The user explicitly asks for draw.io, diagrams.net, `.drawio`, editable XML, paper figures, method figures, or architecture figures.
- Papers, arXiv, official GitHub repos, READMEs, code directories, formulas, ablation experiments, or existing sketches need to be turned into structured figures.
- An editable source file is required, not just Mermaid, PNG, or a text description.

## Not Applicable
- Pure code dependency graphs, call graphs, and class diagrams go to code-graph/Trailmark-type skills first.
- When only a simple ASCII/Mermaid sketch is needed and draw.io is not required, generating `.drawio` is unnecessary.
- With no sources and no permission to go online or provide material, only output a "draft pending confirmation" and never claim it is the paper's real structure.

## Public Source Requirements
Prefer this evidence, ordered by reliability:

1. Paper PDFs, method sections, figures, formulas, and supplementary material provided by the user.
2. Official paper pages, arXiv, OpenReview, ACL Anthology, IEEE/ACM/Springer pages.
3. Official GitHub repos/project homepages, model cards, documentation, demos.
4. High-trust reviews, Papers with Code, public benchmark pages.
5. Other blogs/tutorials are supporting material only and must not override the original paper.

When current papers, latest models, repo structures, benchmarks, or APIs are involved, check public sources and mark the evidence level.

## draw.io Constraints
- Default output is `.drawio`; `.xml` is also possible. An editable draw.io/diagrams.net figure is fundamentally XML; `.drawio` is the common file extension.
- When an editable deliverable is needed, save the `.drawio` source file first; PNG/SVG/PDF are only previews or submission exports.
- When exporting PNG/SVG/PDF, keep embedded diagram data where possible so the figure can keep being edited later.
- Mermaid/tables can organize the logic first, but the final deliverable must be an editable draw.io file.
- If draw.io Desktop is not installed locally, do not claim a PNG/PDF was exported; only say the `.drawio` was generated, which the user can open with app.diagrams.net or the desktop app.

## Execution Principles
- Extract algorithm facts before drawing: task, inputs, outputs, modules, data flow, training/inference differences, loss functions, evaluation, innovations.
- The figure must serve the paper's expression: readers should see at a glance the "problem, main method thread, key modules, information flow, and contribution points."
- Layer complex figures: overview, module expansion, training flow, inference flow, and ablation/comparison figures should not be forced into one figure.
- Keep the paper's original term names; write abbreviations in full on first use.
- Every core module in the figure must trace back to a source passage, formula, figure number, code path, or public document.

## Deliverables
Deliver at minimum:

- `.drawio` file path.
- Figure-structure notes: modules, edges, groupings, color meanings.
- Evidence table: a source for each key module.
- Unconfirmed items: which connections or names are inferred.
- Open/edit instructions: open the `.drawio` with diagrams.net/draw.io.

Optional deliverables:

- JSON spec: for reproduction with `scripts/build_drawio.py`.
- Mermaid sketch: for quick review, not a replacement for `.drawio`.
- PNG/SVG/PDF preview: only claimed after a real local export when the tool is available.

## Workflow

| Stage | Action | Completion criterion |
| --- | --- | --- |
| Requirements scoping | Confirm figure type, target readers, paper venue, page ratio, output path, and whether multiple pages are needed. | Know what to draw and what not to draw. |
| Source analysis | Read user material; when needed, check public papers, official repos, docs, figures, and formulas. | Every core structure has evidence. |
| Structure extraction | List inputs, encoders/core algorithms/decoders, training objectives, inference paths, datasets, metrics, and innovations. | Convertible into nodes and edges. |
| Figure design | Choose a layout: left-to-right pipeline, top-down hierarchy, swimlane, loop, multi-page. | Information hierarchy is clear. |
| Generate draw.io | Use `scripts/build_drawio.py` or write `.drawio` XML directly. | File opens and edits in draw.io. |
| Self-check | Check XML, node labels, edge directions, evidence table, and unconfirmed items. | Nothing fabricated, no key module missing. |
| Delivery | Give file path, evidence, verification, and next steps. | User can open and modify it. |

## Recommended Figure Types

| Figure type | Use for | Layout |
| --- | --- | --- |
| Algorithm pipeline | Input to output, end-to-end method | Left to right |
| Model architecture | Neural network/module hierarchy | Groups + submodules |
| Training vs inference | Training and inference paths differ | Dual swimlanes |
| Data flow | Data processing, features, retrieval, caching | Left to right or top to bottom |
| Loss/evaluation | Multiple losses, metrics, benchmarks | Supporting blocks |
| Paper contribution map | Innovations and baseline comparison | Central module + comparison side notes |

## JSON Spec Convention
Prefer generating `.drawio` with `scripts/build_drawio.py`. Input JSON structure:

```json
{
  "title": "Model Architecture",
  "pages": [
    {
      "name": "Overview",
      "nodes": [
        {"id": "input", "label": "Input", "type": "data", "x": 40, "y": 120},
        {"id": "encoder", "label": "Encoder", "type": "module", "x": 240, "y": 120}
      ],
      "edges": [
        {"source": "input", "target": "encoder", "label": "features"}
      ]
    }
  ]
}
```

Common `type` values: `data`, `module`, `algorithm`, `model`, `loss`, `evaluation`, `output`, `claim`, `note`, `source`.

## Evidence Table Format

```markdown
| Figure element | Source | Evidence level | Notes |
| --- | --- | --- | --- |
| Encoder | Paper Section 3.1 / official repo module path | Verified | Original module name |
| Retrieval cache | README / code path | Verified | Inference path |
| Feedback edge | Inference | Inference | Needs user confirmation |
```

## Verification Checklist
- The `.drawio` is an XML file containing `<mxfile>` and `<mxGraphModel>`.
- Node IDs are unique; every edge's source/target exists.
- Edge directions follow the paper's method, not reversed.
- Training paths, inference paths, loss, and evaluation are not mixed together.
- Unconfirmed content in the figure is marked as inference.
- No information from outside the public paper is written as verified fact.

## Anti-Patterns
- Drawing a "common architecture" from the model name alone, with no source evidence.
- Copying a paper figure as a low-resolution image instead of an editable structure figure.
- All modules in one color, so readers cannot tell data/model/loss/eval apart.
- Cramming every detail into one figure so it is unusable in paper layout.
- Claiming a PNG/PDF was exported when only a `.drawio` was generated.

## Output Contract

```markdown
Done:
- ...

Evidence:
- [Verified/High confidence/Inference/Unverified/Unknown] ...

Files:
- ...

Verification:
- ...

Unconfirmed items:
- ...

Next steps:
- ...
```
