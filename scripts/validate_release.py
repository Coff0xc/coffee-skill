from __future__ import annotations

import json
import re
import subprocess
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
QUICK_RULE_HEADING = "## 快速规则（日常任务先读这里）"
DEFAULT_OUTPUT_HEADING = "## 默认输出"
SKILL_ID_PATTERN = re.compile(r"<!--\s*skill-id:\s*cs-[a-z0-9]{3}-[a-f0-9]{8}\s*-->")
MAX_SKILL_DESCRIPTION_CHARS = 450
MAX_TOTAL_DESCRIPTION_CHARS = 5000
MAX_SKILL_BODY_BYTES = 6800
FULL_WORKFLOW_REFERENCE = "references/full-workflow.md"
SKILL_INVENTORY_JSON = ROOT / "docs" / "skill-inventory.json"
SKILL_INVENTORY_MD = ROOT / "docs" / "SKILL_INVENTORY.md"
FORBIDDEN_LICENSE_TERMS = [
    "AGPL",
    "GNU Affero",
]

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
    "TRADEMARK.md",
    "manifest.json",
    "docs/TRIGGERING.md",
    "docs/TRIGGER_EVAL.md",
    "docs/QUALITY_EVAL.md",
    "docs/USAGE.md",
    "docs/SKILL_INDEX.md",
    "docs/LANGUAGES.md",
    "docs/COVERAGE.md",
    "docs/SANITIZATION.md",
    "docs/SKILL_INVENTORY.md",
    "docs/skill-inventory.json",
    "docs/PROVENANCE.md",
    "docs/ENFORCEMENT.md",
    "docs/TAKEDOWN_TEMPLATE.md",
    ".github/workflows/validate.yml",
    "evals/trigger-eval.json",
    "evals/quality/eval-set.json",
    "evals/quality/quality-eval-results.json",
    "evals/quality/quality-eval-results.md",
    "evals/quality/golden-responses/ui-admin-dashboard-visual-gate/output/index.html",
    "evals/quality/golden-responses/ui-admin-dashboard-visual-gate/screenshots/desktop.png",
    "evals/quality/golden-responses/ui-admin-dashboard-visual-gate/screenshots/mobile.png",
    "evals/quality/golden-responses/dev-repo-repair-ci-gate/src/billing.py",
    "evals/quality/golden-responses/dev-repo-repair-ci-gate/repair-notes.md",
    "evals/quality/golden-responses/office-ppt-aesthetic/final/operating-review.pptx",
    "evals/quality/golden-responses/office-ppt-aesthetic/render-checks/contact-sheet.png",
    "evals/quality/golden-responses/office-excel-parse/final/billing-exceptions.xlsx",
    "evals/quality/golden-responses/office-excel-parse/render-checks/dashboard.png",
    "evals/quality/golden-responses/office-docx-format/final/vendor-risk-review.docx",
    "evals/quality/golden-responses/office-docx-format/render-checks/page-1.png",
    "evals/quality/golden-responses/office-docx-format/render-checks/page-2.png",
    "evals/quality/cases/ui-admin-dashboard-visual-gate/prompt.md",
    "evals/quality/cases/ui-admin-dashboard-visual-gate/input/bad-dashboard.html",
    "evals/quality/cases/dev-repo-repair-ci-gate/prompt.md",
    "evals/quality/cases/dev-repo-repair-ci-gate/input/AGENTS.md",
    "evals/quality/cases/dev-repo-repair-ci-gate/input/README.md",
    "evals/quality/cases/dev-repo-repair-ci-gate/input/ci.log",
    "evals/quality/cases/dev-repo-repair-ci-gate/input/requirements.lock",
    "evals/quality/cases/dev-repo-repair-ci-gate/input/src/billing.py",
    "evals/quality/cases/dev-repo-repair-ci-gate/input/test/test_billing.py",
    "evals/quality/cases/office-ppt-aesthetic/prompt.md",
    "evals/quality/cases/office-ppt-aesthetic/input/operating-review-outline.md",
    "evals/quality/cases/office-excel-parse/prompt.md",
    "evals/quality/cases/office-excel-parse/input/messy-billing-exceptions.csv",
    "evals/quality/cases/office-excel-parse/input/workbook-notes.md",
    "evals/quality/cases/office-docx-format/prompt.md",
    "evals/quality/cases/office-docx-format/input/vendor-risk-review-structure.md",
    "scripts/run_trigger_eval.py",
    "scripts/run_quality_eval.py",
    "scripts/build_quality_golden_responses.py",
    "scripts/build_skill_inventory.py",
    "scripts/install_local_skills.ps1",
    "scripts/scan_provenance.py",
    "skills/coff0xc-office-doc-tools/references/pptx-defense-rewrite.md",
    "skills/coff0xc-skill-router/references/router-map.md",
    "skills/coff0xc-skill-router/references/complex-workflow.md",
    "skills/coff0xc-ui-doc-output/references/ui-generalized-rules.md",
    "skills/coff0xc-research-drawio-diagram/scripts/build_drawio.py",
    "skills/coff0xc-research-drawio-diagram/examples/research-pipeline.json",
    "skills/coff0xc-research-drawio-diagram/examples/research-pipeline.drawio",
    "skills/coff0xc-research-drawio-diagram/references/drawio-public-notes.md",
]

REQUIRED_I18N_FILES = [
    "docs/i18n/README.en.md",
    "docs/i18n/README.zh-CN.md",
    "docs/i18n/README.ja.md",
    "docs/i18n/README.ko.md",
    "docs/i18n/README.es.md",
    "docs/i18n/README.fr.md",
    "docs/i18n/README.de.md",
    "docs/i18n/README.pt-BR.md",
    "docs/i18n/README.it.md",
    "docs/i18n/README.nl.md",
    "docs/i18n/README.pl.md",
    "docs/i18n/README.ru.md",
    "docs/i18n/README.ar.md",
    "docs/i18n/README.tr.md",
    "docs/i18n/README.hi.md",
    "docs/i18n/README.id.md",
    "docs/i18n/README.vi.md",
    "docs/i18n/README.th.md",
]


def dynamic_required_files() -> list[str]:
    files = list(REQUIRED_FILES)
    files.extend(
        path.relative_to(ROOT).as_posix()
        for path in sorted(SKILLS.glob(f"*/{FULL_WORKFLOW_REFERENCE}"))
    )
    return files


def validate_skill_inventory() -> list[str]:
    errors: list[str] = []
    try:
        from build_skill_inventory import collect_inventory, render_markdown
    except Exception as exc:  # pragma: no cover - release gate path
        return [f"skill inventory generator import failed: {exc}"]

    if not SKILL_INVENTORY_JSON.exists():
        errors.append("missing required file: docs/skill-inventory.json")
    if not SKILL_INVENTORY_MD.exists():
        errors.append("missing required file: docs/SKILL_INVENTORY.md")
    if errors:
        return errors

    expected = collect_inventory()
    try:
        actual_json = json.loads(SKILL_INVENTORY_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"docs/skill-inventory.json: invalid JSON: {exc}"]

    actual_md = SKILL_INVENTORY_MD.read_text(encoding="utf-8")
    if actual_json != expected:
        errors.append("docs/skill-inventory.json is stale or inconsistent with scripts/build_skill_inventory.py")
    if actual_md != render_markdown(expected):
        errors.append("docs/SKILL_INVENTORY.md is stale or inconsistent with scripts/build_skill_inventory.py")
    return errors


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


def iter_release_text_files() -> list[Path]:
    """Return tracked release files for leakage checks.

    Local planning notes and evidence files can contain machine-private paths.
    Release validation should protect files that are actually published.
    """
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except OSError:
        result = None

    if result is not None and result.returncode == 0:
        release_rels = {rel for rel in result.stdout.splitlines() if rel.strip()}
        release_rels.update(dynamic_required_files())
        release_rels.update(REQUIRED_I18N_FILES)
        candidates = [(ROOT / rel).resolve() for rel in sorted(release_rels) if (ROOT / rel).exists()]
    else:
        candidates = sorted(ROOT.rglob("*"))

    files: list[Path] = []
    for path in candidates:
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".py", ".ps1", ".yml", ".yaml", ""} and path.name not in {"LICENSE"}:
            continue
        files.append(path)
    return files


def main() -> None:
    errors: list[str] = []

    for rel in [*dynamic_required_files(), *REQUIRED_I18N_FILES]:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")
    errors.extend(validate_skill_inventory())

    license_path = ROOT / "LICENSE"
    if license_path.exists():
        license_text = license_path.read_text(encoding="utf-8", errors="ignore")
        if "Source-Available Noncommercial License" not in license_text:
            errors.append("LICENSE: expected source-available noncommercial license text")
        if "Any commercial use requires prior notice to Coff0xc" not in license_text:
            errors.append("LICENSE: expected commercial prior-notice requirement")
    notice_path = ROOT / "NOTICE"
    if notice_path.exists():
        notice_text = notice_path.read_text(encoding="utf-8", errors="ignore")
        if "source-available noncommercial license" not in notice_text:
            errors.append("NOTICE: expected source-available noncommercial notice")

    manifest_path = ROOT / "manifest.json"
    manifest = []
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    skill_paths = sorted(SKILLS.glob("*/SKILL.md"))
    if len(skill_paths) != len(manifest):
        errors.append(f"skill count mismatch: files={len(skill_paths)} manifest={len(manifest)}")

    manifest_by_name = {item.get("name"): item for item in manifest}
    manifest_names = set(manifest_by_name)
    total_description_chars = 0
    for path in skill_paths:
        folder = path.parent.name
        values, fm_errors = parse_frontmatter(path)
        errors.extend(fm_errors)
        text = path.read_text(encoding="utf-8")
        description = values.get("description", "")
        if values.get("name") != folder:
            errors.append(f"{path}: frontmatter name does not match folder")
        if folder not in manifest_names:
            errors.append(f"{path}: not listed in manifest")
        if not description:
            errors.append(f"{path}: missing description")
        else:
            total_description_chars += len(description)
            if len(description) > MAX_SKILL_DESCRIPTION_CHARS:
                errors.append(
                    f"{path}: description too long ({len(description)} chars > {MAX_SKILL_DESCRIPTION_CHARS})"
                )
            manifest_item = manifest_by_name.get(folder)
            if manifest_item is not None and manifest_item.get("description") != description:
                errors.append(f"{path}: frontmatter description differs from manifest")
        if QUICK_RULE_HEADING not in text:
            errors.append(f"{path}: missing quick rules section")
        elif "## 能力定位" in text and text.index(QUICK_RULE_HEADING) > text.index("## 能力定位"):
            errors.append(f"{path}: quick rules section must appear before capability positioning")
        if DEFAULT_OUTPUT_HEADING not in text:
            errors.append(f"{path}: missing default output section")
        if not SKILL_ID_PATTERN.search(text):
            errors.append(f"{path}: missing source skill-id marker")
        body_bytes = len(text.encode("utf-8"))
        if body_bytes > MAX_SKILL_BODY_BYTES:
            errors.append(f"{path}: SKILL.md too large ({body_bytes} bytes > {MAX_SKILL_BODY_BYTES})")
        if FULL_WORKFLOW_REFERENCE in text and not (path.parent / FULL_WORKFLOW_REFERENCE).exists():
            errors.append(f"{path}: references full workflow but the file is missing")

    if total_description_chars > MAX_TOTAL_DESCRIPTION_CHARS:
        errors.append(
            f"frontmatter description budget exceeded: {total_description_chars} chars > {MAX_TOTAL_DESCRIPTION_CHARS}"
        )

    for path in iter_release_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for idx, line in enumerate(text.splitlines(), 1):
            if path.name in {"README.md", "NOTICE"} or path.parts[-2:] == ("docs", "PROVENANCE.md"):
                for term in FORBIDDEN_LICENSE_TERMS:
                    if term in line:
                        errors.append(f"{path}:{idx}: stale open-source license term {term}")
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
