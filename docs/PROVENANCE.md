# Provenance

This repository is a publication candidate generated from a local skill consolidation workflow.

## Inputs

- A local Codex skill export.
- A user-provided Claude skill archive.
- Locally installed skills used as style references.

## Transformation

- Similar skills were clustered by capability area.
- High-risk dual-use material was converted to defensive, authorization-scoped guidance.
- The current release consolidates 91 source skills and workflows into 17 comprehensive capability skills.
- Earlier snapshots started from 87 source skills and 15 original capability skills; later updates added research draw.io and Office/PDF document artifact workflows.
- A research draw.io diagram skill was added as a new workflow after public-source analysis of diagrams.net/draw.io editing/export behavior.
- A trigger fallback router skill was added because client auto-triggering depends heavily on frontmatter metadata.
- External UI skill material was reduced to generalized workflow and quality gates. Personal definitions, local machine paths, absolute taste rules, and default authorization language were not copied into the runtime skill.
- The external quick-rule style was generalized across all runtime skills as `快速规则（日常任务先读这里）`; no external personal paths, authorization shortcuts, or project-specific identity rules were copied.

## Publication Caveat

Before pushing to a public repository, confirm that you have the right to publish the included text. This release candidate uses Apache License 2.0.
