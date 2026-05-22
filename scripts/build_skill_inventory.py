from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SKILLS = ROOT / "skills"
SNAPSHOT_DATE = date.today().isoformat()


@dataclass(frozen=True)
class Source:
    id: str
    root: Path
    mode: str
    publish_policy: str
    exclude_dirs: tuple[str, ...] = ()


def home() -> Path:
    return Path(os.environ.get("USERPROFILE") or Path.home())


def sources() -> list[Source]:
    base = home()
    return [
        Source("coffee-release", SKILLS, "direct", "redistributed-curated"),
        Source("codex-user", base / ".codex" / "skills", "direct", "metadata-only", (".system",)),
        Source("codex-system", base / ".codex" / "skills" / ".system", "direct", "metadata-only"),
        Source("agents-user", base / ".agents" / "skills", "direct", "metadata-only"),
        Source(
            "plugin-bundled",
            base / ".codex" / "plugins" / "cache" / "openai-bundled",
            "recursive",
            "metadata-only",
        ),
        Source(
            "plugin-runtime",
            base / ".codex" / "plugins" / "cache" / "openai-primary-runtime",
            "recursive",
            "metadata-only",
        ),
    ]


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or lines[0] != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}

    data: dict[str, str] = {}
    i = 1
    while i < end:
        line = lines[i]
        if not line.strip() or ":" not in line:
            i += 1
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        value = raw.strip()
        if value in {">", "|", ">-", "|-"}:
            block: list[str] = []
            i += 1
            while i < end and (lines[i].startswith(" ") or lines[i].startswith("\t") or not lines[i].strip()):
                block.append(lines[i].strip())
                i += 1
            data[key] = " ".join(part for part in block if part)
            continue
        data[key] = unquote(value)
        i += 1
    return data


def skill_files_for(source: Source) -> list[Path]:
    if not source.root.exists():
        return []
    if source.mode == "direct":
        files: list[Path] = []
        for child in sorted(source.root.iterdir(), key=lambda item: item.name.lower()):
            if child.name in source.exclude_dirs or not child.is_dir():
                continue
            skill = child / "SKILL.md"
            if skill.exists():
                files.append(skill)
        return files
    return sorted(source.root.rglob("SKILL.md"), key=lambda item: item.as_posix().lower())


def classify(name: str, description: str, source_id: str) -> tuple[str, str]:
    text = f"{name} {description}".lower()
    if name.startswith("coff0xc-"):
        risk = "curated-release" if source_id == "coffee-release" else "installed-coff0xc-copy"
        return name, risk

    rules: list[tuple[str, tuple[str, ...]]] = [
        ("coff0xc-software-engineering", ("dev", "development", "python", "javascript", "typescript", "rust", "go", "java", "testing", "test", "git", "repo", "bugfix", "fuzz", "fuzzer", "fuzzing", "sanitizer", "coverage-guided")),
        ("coff0xc-secure-code-appsec", ("appsec", "codeql", "semgrep", "taint", "xss", "ssrf", "sqli", "webshell", "code audit")),
        ("coff0xc-blockchain-security", ("solana", "cosmos", "substrate", "cairo", "ton", "algorand", "blockchain", "smart contract", "defi", "token")),
        ("coff0xc-cloud-devsecops", ("cloud", "container", "kubernetes", "docker", "serverless", "github actions", "supply chain", "secret")),
        ("coff0xc-identity-zero-trust", ("identity", "iam", "active directory", "kerberos", "bloodhound", "zero trust", "mfa", "sso")),
        ("coff0xc-detection-response", ("detection", "incident", "forensic", "malware", "yara", "sigma", "soc", "threat hunting")),
        ("coff0xc-vulnerability-lifecycle", ("cve", "vulnerability lifecycle", "advisory", "patch diff", "cvss", "epss", "kev")),
        ("coff0xc-network-protocol-security", ("network", "protocol", "tls", "dns", "http/2", "http/3", "quic", "pcap", "wireshark", "proverif")),
        ("coff0xc-binary-mobile-iot", ("binary", "pwn", "reverse", "apk", "ipa", "frida", "firmware", "iot", "ics", "scada", "kernel")),
        ("coff0xc-compliance-architecture", ("compliance", "architecture", "threat model", "soc2", "iso27001", "gdpr", "nist", "risk register")),
        ("coff0xc-purple-deception", ("purple", "deception", "honeypot", "canary", "att&ck", "control validation")),
        ("coff0xc-authorized-assessment", ("authorized", "assessment", "roe", "attack surface", "red team", "adversary emulation")),
        ("coff0xc-research-drawio-diagram", ("drawio", "diagram", "mermaid", "paper", "research", "workflow graph")),
        ("coff0xc-office-doc-tools", ("ppt", "pptx", "docx", "word", "excel", "xlsx", "spreadsheet", "pdf", "presentation", "documents")),
        ("coff0xc-ui-doc-output", ("ui", "frontend", "dashboard", "visual", "responsive", "browser", "chrome", "accessibility", "design system")),
        ("coff0xc-ai-agent-rag", ("agent", "rag", "llm", "prompt", "embedding", "langchain", "autogen", "openai")),
        ("coff0xc-api-data-platform", ("api", "database", "schema", "graphql", "openapi", "cli", "sdk", "data platform")),
    ]
    mapped = "supporting-tooling"
    for target, terms in rules:
        if any(has_term(text, term) for term in terms):
            mapped = target
            break

    high_risk_terms = ("pentest", "exploit", "privesc", "red team", "attack", "pwn")
    security_terms = ("security", "audit", "vulnerability", "fuzz", "sast", "taint", "forensic")
    if any(term in text for term in high_risk_terms):
        risk = "dual-use-high-risk"
    elif any(term in text for term in security_terms):
        risk = "security-review"
    elif source_id.startswith("plugin") or source_id == "codex-system":
        risk = "platform-provided"
    else:
        risk = "general"
    return mapped, risk


def has_term(text: str, term: str) -> bool:
    if any("\u4e00" <= char <= "\u9fff" for char in term):
        return term in text
    if len(term) <= 3 and term.isascii():
        return re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text) is not None
    return term in text


def compact(text: str, limit: int = 180) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def collect_inventory() -> dict:
    items: list[dict[str, str]] = []
    source_counts: Counter[str] = Counter()
    by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    for source in sources():
        for path in skill_files_for(source):
            fm = parse_frontmatter(path)
            name = fm.get("name") or path.parent.name
            raw_description = compact(fm.get("description", ""))
            mapped, risk = classify(name, raw_description, source.id)
            description = raw_description if source.id == "coffee-release" else ""
            rel = path.relative_to(source.root).as_posix()
            item = {
                "name": name,
                "source": source.id,
                "relative_skill_path": rel,
                "description": description,
                "description_policy": "included-release" if description else "omitted-metadata-only",
                "mapped_coff0xc_skill": mapped,
                "risk_profile": risk,
                "publish_policy": source.publish_policy,
            }
            items.append(item)
            by_name[name].append(item)
            source_counts[source.id] += 1

    names = Counter(item["name"] for item in items)
    duplicates = {}
    for name in sorted(names):
        group = sorted(by_name[name], key=lambda item: (item["source"], item["relative_skill_path"]))
        if len(group) <= 1:
            continue
        duplicates[name] = {
            "instances": len(group),
            "entries": [
                {
                    "source": item["source"],
                    "relative_skill_path": item["relative_skill_path"],
                    "mapped_coff0xc_skill": item["mapped_coff0xc_skill"],
                }
                for item in group
            ],
        }
    map_counts = Counter(item["mapped_coff0xc_skill"] for item in items)

    return {
        "schema_version": 1,
        "snapshot_date": SNAPSHOT_DATE,
        "generated_by": "scripts/build_skill_inventory.py",
        "policy": (
            "Only coffee-release skills are redistributed as runtime skill bodies. "
            "Other installed/system/plugin skills are metadata-only inventory entries."
        ),
        "counts": {
            "skill_files": len(items),
            "unique_skill_names": len(names),
            "sources": dict(sorted(source_counts.items())),
            "mapped_coff0xc_skills": dict(sorted(map_counts.items())),
            "duplicate_names": len(duplicates),
        },
        "duplicates": duplicates,
        "skills": sorted(items, key=lambda item: (item["source"], item["name"].lower(), item["relative_skill_path"])),
    }


def render_markdown(inventory: dict) -> str:
    counts = inventory["counts"]
    lines = [
        "# Installed Skill Inventory",
        "",
        "This is a local metadata inventory used to organize the wider skill environment around `coffee-skill`.",
        "It does not redistribute raw external, system, or plugin skill bodies.",
        "",
        "## Summary",
        "",
        f"- Snapshot date: `{inventory['snapshot_date']}`",
        f"- Skill files indexed: `{counts['skill_files']}`",
        f"- Unique skill names: `{counts['unique_skill_names']}`",
        f"- Duplicate names: `{counts['duplicate_names']}`",
        "- Runtime release policy: only `coffee-release` skills are published as Coff0xc runtime skill bodies; all other sources are metadata-only.",
        "",
        "## Sources",
        "",
        "| Source | Count | Policy | Meaning |",
        "|---|---:|---|---|",
    ]
    source_meanings = {
        "coffee-release": "Curated skills in this repository.",
        "codex-user": "User-installed Codex skills.",
        "codex-system": "Codex system skills.",
        "agents-user": "User-installed agent skills.",
        "plugin-bundled": "Bundled plugin skills.",
        "plugin-runtime": "Primary runtime plugin skills.",
    }
    policy_by_source = {source.id: source.publish_policy for source in sources()}
    source_order = ["coffee-release", "codex-user", "codex-system", "agents-user", "plugin-bundled", "plugin-runtime"]
    for source in [s for s in source_order if s in counts["sources"]]:
        lines.append(
            f"| `{source}` | {counts['sources'][source]} | `{policy_by_source.get(source, 'metadata-only')}` | {source_meanings.get(source, '')} |"
        )
    for source, count in sorted(counts["sources"].items()):
        if source in source_order:
            continue
        lines.append(
            f"| `{source}` | {count} | `{policy_by_source.get(source, 'metadata-only')}` | {source_meanings.get(source, '')} |"
        )

    lines.extend(["", "## Duplicate Names", ""])
    if inventory["duplicates"]:
        lines.extend(["| Name | Instances | Entries |", "|---|---:|---|"])
        for name, meta in inventory["duplicates"].items():
            entries = "; ".join(
                f"`{md_escape(entry['source'])}`:`{md_escape(entry['relative_skill_path'])}` -> `{md_escape(entry['mapped_coff0xc_skill'])}`"
                for entry in meta["entries"]
            )
            lines.append(f"| `{md_escape(name)}` | {meta['instances']} | {entries} |")
    else:
        lines.append("No duplicate skill names were found.")

    lines.extend(
        [
            "",
            "## Consolidation Map",
            "",
            "This map shows where installed skills naturally fit in the Coff0xc 18-skill model. `supporting-tooling` means the skill is useful for maintenance, creation, or installation but is not one of the runtime capability domains.",
            "",
            "| Coff0xc target | Count |",
            "|---|---:|",
        ]
    )
    for target, count in sorted(counts["mapped_coff0xc_skills"].items()):
        lines.append(f"| `{target}` | {count} |")

    by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    for item in inventory["skills"]:
        by_source[item["source"]].append(item)

    lines.extend(["", "## Inventory", ""])
    for source in sorted(by_source):
        lines.extend([f"### {source}", "", "| Skill | Mapped target | Risk | Notes |", "|---|---|---|---|"])
        for item in by_source[source]:
            note = item["description"] or "External/system/plugin description omitted; metadata-only mapping."
            lines.append(
                "| `{}` | `{}` | `{}` | {} |".format(
                    md_escape(item["name"]),
                    md_escape(item["mapped_coff0xc_skill"]),
                    md_escape(item["risk_profile"]),
                    md_escape(note),
                )
            )
        lines.append("")

    lines.extend(
        [
            "## Optimization Notes",
            "",
            "- Keep `skills/` limited to the curated `coff0xc-*` release set unless a new domain is intentionally promoted.",
            "- Use this inventory to decide whether a new external skill should remain a reference, become a script, or be merged into an existing Coff0xc domain.",
            "- Do not copy external/system/plugin skill bodies into this repository without checking license, provenance, and safety boundaries.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the local skill inventory snapshot.")
    parser.add_argument("--json", default=str(DOCS / "skill-inventory.json"))
    parser.add_argument("--markdown", default=str(DOCS / "SKILL_INVENTORY.md"))
    args = parser.parse_args()

    inventory = collect_inventory()
    json_path = Path(args.json)
    md_path = Path(args.markdown)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(inventory), encoding="utf-8")
    print(
        json.dumps(
            {
                "markdown": md_path.as_posix(),
                "json": json_path.as_posix(),
                "skill_files": inventory["counts"]["skill_files"],
                "unique_skill_names": inventory["counts"]["unique_skill_names"],
                "duplicate_names": inventory["counts"]["duplicate_names"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
