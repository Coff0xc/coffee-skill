from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TERMS = [
    re.compile(r"<!--\s*skill-id:\s*cs-[a-z0-9]{3}-[a-f0-9]{8}\s*-->"),
    "Required Notice: Copyright 2026 Coff0xc",
    "source-available noncommercial",
    "prior notice to Coff0xc",
]


def scan(root: Path) -> dict[str, object]:
    hits: list[dict[str, object]] = []
    checked = 0
    for path in sorted(root.rglob("*")):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".txt", ".json", ".yaml", ".yml", ""} and path.name not in {"LICENSE", "NOTICE"}:
            continue
        checked += 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        for term in TERMS:
            if isinstance(term, str):
                match = term if term in text else None
                line_no = next((idx for idx, line in enumerate(text.splitlines(), 1) if term in line), None)
            else:
                found = term.search(text)
                match = found.group(0) if found else None
                line_no = next((idx for idx, line in enumerate(text.splitlines(), 1) if term.search(line)), None)
            if match:
                hits.append(
                    {
                        "file": str(path),
                        "match": match,
                        "line": line_no,
                    }
                )
    return {
        "root": str(root),
        "checked_files": checked,
        "hit_count": len(hits),
        "hits": hits,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan a folder for Coff0xc coffee-skill source identifiers and required notices.")
    parser.add_argument("path", nargs="?", default=".", help="Folder or file tree to scan")
    args = parser.parse_args()
    report = scan(Path(args.path).resolve())
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["hit_count"] == 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
