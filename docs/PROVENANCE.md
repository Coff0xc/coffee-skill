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

Before pushing to a public repository, confirm that you have the right to publish the included text.

License history:
- Versions published before the license change remain under the terms that applied to those earlier versions.
- From the current license-change commit onward, this repository uses GNU Affero General Public License v3.0 only (`AGPL-3.0-only`).
- The AGPL open source license allows commercial use, but covered copying, modification, distribution, packaged derivatives, and modified network-service deployments must preserve the AGPL license, copyright notices, source availability obligations, and this NOTICE.

## Source Identification

Release `SKILL.md` files contain source-level HTML comment identifiers. These identifiers are intentionally non-rendered Markdown source metadata. They are not telemetry, do not call any network service, and do not alter model behavior. They exist to make copied source packages easier to identify.

Run:

```powershell
python .\scripts\scan_provenance.py <suspected-folder>
```

Removal of attribution, removal of `LICENSE` / `NOTICE`, removal of source identifiers, AGPL source-obligation violations, closed-source repackaging of covered derivatives, false originality claims, or any implication of official Coff0xc authorization is not permitted and may be used as evidence for takedown requests, license enforcement, trademark/impersonation complaints, and legal claims.

For practical enforcement steps, see:

- `docs/ENFORCEMENT.md`
- `docs/TAKEDOWN_TEMPLATE.md`
- `TRADEMARK.md`
