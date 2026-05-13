from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

LOCAL_USER_MARKER = "12" + "299"
LOCAL_PROFILE_MARKER = r"C:\\Users\\" + LOCAL_USER_MARKER
KEY_BLOCK_PREFIX = "BEGIN "
KEY_BLOCK_SUFFIX = "PRIVATE" + " KEY"
PRIVATE_KEY_MARKER = KEY_BLOCK_PREFIX + r"(RSA|EC|DSA|OPENSSH )?" + KEY_BLOCK_SUFFIX
GITHUB_TOKEN_MARKER = "github" + r"_pat_[A-Za-z0-9_]+|" + "ghp" + r"_[A-Za-z0-9_]{20,}"
OPENAI_KEY_MARKER = "sk" + r"-[A-Za-z0-9]{20,}"

SENSITIVE_PATTERNS = [
    re.compile(LOCAL_USER_MARKER, re.IGNORECASE),
    re.compile(LOCAL_PROFILE_MARKER, re.IGNORECASE),
    re.compile(PRIVATE_KEY_MARKER, re.IGNORECASE),
    re.compile(GITHUB_TOKEN_MARKER, re.IGNORECASE),
    re.compile(OPENAI_KEY_MARKER, re.IGNORECASE),
]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "NOTICE",
    "manifest.json",
    "docs/TRIGGERING.md",
    "docs/COVERAGE.md",
    "docs/SANITIZATION.md",
    "docs/PROVENANCE.md",
]


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 4 or lines[0] != "---":
        return {}, [f"{path}: missing opening frontmatter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, [f"{path}: missing closing frontmatter"]
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            errors.append(f"{path}: invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                errors.append(f"{path}: invalid quoted value for {key}")
        values[key.strip()] = value
    return values, errors


def main() -> None:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")

    manifest_path = ROOT / "manifest.json"
    manifest = []
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    skill_paths = sorted(SKILLS.glob("*/SKILL.md"))
    if len(skill_paths) != len(manifest):
        errors.append(f"skill count mismatch: files={len(skill_paths)} manifest={len(manifest)}")

    manifest_names = {item.get("name") for item in manifest}
    for path in skill_paths:
        folder = path.parent.name
        values, fm_errors = parse_frontmatter(path)
        errors.extend(fm_errors)
        if values.get("name") != folder:
            errors.append(f"{path}: frontmatter name does not match folder")
        if folder not in manifest_names:
            errors.append(f"{path}: not listed in manifest")
        if not values.get("description"):
            errors.append(f"{path}: missing description")

    for path in sorted(ROOT.rglob("*")):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".py", ""} and path.name not in {"LICENSE"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for idx, line in enumerate(text.splitlines(), 1):
            for pattern in SENSITIVE_PATTERNS:
                if pattern.search(line):
                    errors.append(f"{path}:{idx}: sensitive pattern {pattern.pattern}")

    summary = {
        "root": str(ROOT),
        "skill_count": len(skill_paths),
        "manifest_count": len(manifest),
        "errors": errors,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
