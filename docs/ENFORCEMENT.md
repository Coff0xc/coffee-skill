# Enforcement Guide

This repository is open source, but it is not anonymous resale inventory and it is not a source for false "original", "official", or closed-source repackaging claims.

From the current license-change commit onward, `coffee-skill` is distributed under GNU Affero General Public License v3.0 only (`AGPL-3.0-only`). The AGPL permits commercial use, but it requires preservation of license and copyright notices, source availability for covered distributions, same-license sharing for covered derivatives, and source availability for modified network-service deployments.

## Fast Decision

| Behavior | Status |
|---|---|
| Personal study, research, testing, commercial or noncommercial use | Allowed under AGPL when obligations are followed. |
| Attribution-preserving fork with license/source obligations intact | Allowed under AGPL. |
| Selling a copy, repack, course bundle, agent pack, or hosted version | Allowed only if AGPL obligations and trademark limits are followed. |
| Removing `LICENSE`, `NOTICE`, attribution, source identifiers, source-offer information, or license-history notices | Not allowed. |
| Distributing covered derivatives or modified network services without corresponding source | Not allowed. |
| Claiming the work is original, exclusive, self-developed, official, or authorized | Not allowed. |
| Using `Coff0xc`, `coffee-skill`, screenshots, README wording, or skill names to imply endorsement | Not allowed. |

## Evidence Package

When reporting a suspected unauthorized seller, collect:

- marketplace URL, seller profile, product title, price, and timestamp;
- screenshots or screen recordings of the listing;
- purchased/downloaded package, if legally obtained;
- archive snapshot URL if available;
- source comparison against this repository;
- `LICENSE`, `NOTICE`, attribution, source identifier, and source-offer presence/absence;
- scan result from `scripts/scan_provenance.py`;
- Git commit URL showing the original source and publication date.

## Local Scan

```powershell
python .\scripts\scan_provenance.py <suspected-folder>
```

The scan checks for source identifiers and required notices. A positive scan is not the only proof of copying; a negative scan does not prove clean-room authorship because identifiers can be removed. Use it together with textual similarity, file layout, naming, README wording, examples, eval cases, license/source-offer records, and distribution records.

## Escalation Path

1. Preserve evidence before contacting the seller.
2. Send the violation notice in `docs/TAKEDOWN_TEMPLATE.md`.
3. If unresolved, file a platform IP/license/trademark complaint with the evidence package.
4. For GitHub-hosted copies, use GitHub's copyright and trademark complaint channels as appropriate.
5. For repeated or high-value commercial misuse, use counsel for a formal demand letter.

## Important Boundary

Versions published before the license change remain under the license terms that applied to those earlier versions. This enforcement guide applies to the current AGPL terms and later versions.
