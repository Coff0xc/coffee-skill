# Enforcement Guide

This repository is publicly visible, but it is not open-source licensed and it is not free inventory for resale, mirrors, courses, agent packs, hosted services, company production workflows, or false "original" / "official" claims.

From the current license-change commit onward, `coffee-skill` is publicly visible under a custom source-available noncommercial license. Personal learning, research, evaluation, and local noncommercial use are allowed with attribution preserved. Any commercialization requires prior notice to Coff0xc and separate written commercial permission.

## Fast Decision

| Behavior | Status |
|---|---|
| Viewing the public repository | Allowed. |
| Personal learning, research, evaluation, and local noncommercial use | Allowed with attribution preserved. |
| Contacting Coff0xc to request commercial permission | Allowed. |
| Company internal production use, consulting delivery, commercial training, course, hosted, marketplace, or paid agent-pack use | Not allowed without prior notice and written permission. |
| Selling a copy, repack, course bundle, agent pack, mirror, or hosted version | Not allowed without prior notice and written permission. |
| Removing `LICENSE`, `NOTICE`, attribution, source identifiers, or license-history notices | Not allowed. |
| Claiming the work is original, exclusive, self-developed, official, or authorized | Not allowed. |
| Using `Coff0xc`, `coffee-skill`, screenshots, README wording, or skill names to imply endorsement | Not allowed. |

## Evidence Package

When reporting a suspected unauthorized seller, collect:

- marketplace URL, seller profile, product title, price, and timestamp;
- screenshots or screen recordings of the listing;
- purchased/downloaded package, if legally obtained;
- archive snapshot URL if available;
- source comparison against this repository;
- `LICENSE`, `NOTICE`, attribution, and source identifier presence/absence;
- scan result from `scripts/scan_provenance.py`;
- Git commit URL showing the original source and publication date.

## Local Scan

```powershell
python .\scripts\scan_provenance.py <suspected-folder>
```

The scan checks for source identifiers and required notices. A positive scan is not the only proof of copying; a negative scan does not prove clean-room authorship because identifiers can be removed. Use it together with textual similarity, file layout, naming, README wording, examples, eval cases, permission/notice records, and distribution records.

## Escalation Path

1. Preserve evidence before contacting the seller.
2. Send the violation notice in `docs/TAKEDOWN_TEMPLATE.md`.
3. If unresolved, file a platform IP/license/trademark complaint with the evidence package.
4. For GitHub-hosted copies, use GitHub's copyright and trademark complaint channels as appropriate.
5. For repeated or high-value commercial misuse, use counsel for a formal demand letter.

## Important Boundary

Versions published before the license change remain under the license terms that applied to those earlier versions. This enforcement guide applies to the current source-available noncommercial terms and later versions.
