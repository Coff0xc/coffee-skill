from __future__ import annotations

import argparse
import filecmp
import importlib.util
import json
import re
import sys
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVAL_SET = ROOT / "evals" / "quality" / "eval-set.json"
DEFAULT_OUTPUT = ROOT / "evals" / "quality" / "quality-eval-results.json"


@dataclass
class AssertionResult:
    id: str
    passed: bool
    evidence: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def resolve_case_path(eval_root: Path, rel: str) -> Path:
    return (eval_root / rel).resolve()


def validate_fixture(case: dict[str, Any], eval_root: Path) -> list[str]:
    errors: list[str] = []
    prompt_file = resolve_case_path(eval_root, case["prompt_file"])
    if not prompt_file.exists():
        errors.append(f"missing prompt_file: {case['prompt_file']}")
    for rel in case.get("input_files", []):
        path = resolve_case_path(eval_root, rel)
        if not path.exists():
            errors.append(f"missing input_file: {rel}")
    for assertion in case.get("assertions", []):
        assertion_type = assertion.get("type")
        if assertion_type not in {
            "file_exists",
            "file_contains_all",
            "file_not_contains_regex",
            "file_unchanged_if_present",
            "python_billing_behavior",
        }:
            errors.append(f"{case['id']}: unsupported assertion type {assertion_type}")
        if assertion_type == "file_unchanged_if_present":
            reference = assertion.get("reference")
            if not reference or not resolve_case_path(eval_root, reference).exists():
                errors.append(f"{case['id']}: missing reference for assertion {assertion.get('id')}")
    return errors


def evaluate_assertion(assertion: dict[str, Any], response_dir: Path, eval_root: Path) -> AssertionResult:
    assertion_id = assertion["id"]
    assertion_type = assertion["type"]
    target = response_dir / assertion["path"]

    if assertion_type == "file_exists":
        return AssertionResult(
            id=assertion_id,
            passed=target.exists(),
            evidence=f"{target} exists" if target.exists() else f"{target} does not exist",
        )

    if assertion_type == "file_contains_all":
        if not target.exists():
            return AssertionResult(id=assertion_id, passed=False, evidence=f"{target} does not exist")
        text = read_text(target).lower()
        missing = [term for term in assertion["terms"] if term.lower() not in text]
        return AssertionResult(
            id=assertion_id,
            passed=not missing,
            evidence="all terms found" if not missing else f"missing terms: {', '.join(missing)}",
        )

    if assertion_type == "file_not_contains_regex":
        if not target.exists():
            return AssertionResult(id=assertion_id, passed=False, evidence=f"{target} does not exist")
        text = read_text(target)
        hits = [pattern for pattern in assertion["patterns"] if re.search(pattern, text, flags=re.IGNORECASE)]
        return AssertionResult(
            id=assertion_id,
            passed=not hits,
            evidence="no banned patterns found" if not hits else f"matched banned patterns: {', '.join(hits)}",
        )

    if assertion_type == "file_unchanged_if_present":
        if not target.exists():
            return AssertionResult(id=assertion_id, passed=True, evidence=f"{target} absent, no churn")
        reference = resolve_case_path(eval_root, assertion["reference"])
        passed = filecmp.cmp(target, reference, shallow=False)
        return AssertionResult(
            id=assertion_id,
            passed=passed,
            evidence="matches reference" if passed else f"{target} differs from {reference}",
        )

    if assertion_type == "python_billing_behavior":
        if not target.exists():
            return AssertionResult(id=assertion_id, passed=False, evidence=f"{target} does not exist")
        module_name = f"quality_eval_billing_{response_dir.name.replace('-', '_')}"
        try:
            spec = importlib.util.spec_from_file_location(module_name, target)
            if spec is None or spec.loader is None:
                return AssertionResult(id=assertion_id, passed=False, evidence=f"could not load {target}")
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            amount = module.normalize_amount("$1,200.50")
            total = module.invoice_total(
                [
                    {"quantity": "2", "unit_price": "$100.00"},
                    {"quantity": "1", "unit_price": "$50.00"},
                ],
                discount_rate=Decimal("0.10"),
                tax_rate=Decimal("0.08"),
            )
        except Exception as exc:  # noqa: BLE001 - report arbitrary candidate-output failures.
            return AssertionResult(id=assertion_id, passed=False, evidence=f"behavior check raised {exc!r}")
        passed = amount == Decimal("1200.50") and total == Decimal("243.00")
        return AssertionResult(
            id=assertion_id,
            passed=passed,
            evidence=f"normalize_amount={amount!s}, invoice_total={total!s}",
        )

    return AssertionResult(id=assertion_id, passed=False, evidence=f"unsupported assertion type {assertion_type}")


def evaluate_response_case(case: dict[str, Any], responses_dir: Path, eval_root: Path) -> dict[str, Any]:
    case_dir = responses_dir / case["id"]
    assertion_results = [evaluate_assertion(assertion, case_dir, eval_root) for assertion in case["assertions"]]
    passed = all(item.passed for item in assertion_results)
    return {
        "id": case["id"],
        "skill": case["skill"],
        "category": case["category"],
        "response_dir": str(case_dir),
        "passed": passed,
        "assertions": [item.__dict__ for item in assertion_results],
    }


def write_markdown_report(summary: dict[str, Any], output: Path) -> None:
    lines = [
        "# Quality Evaluation Report",
        "",
        "This report is generated from `evals/quality/eval-set.json` by `scripts/run_quality_eval.py`.",
        "",
        "Unlike trigger evals, these cases define artifact-level quality checks for actual task outputs.",
        "",
        "## Summary",
        "",
        f"- Cases: {summary['case_count']}",
        f"- Mode: {summary['mode']}",
        f"- Fixture errors: {summary['fixture_error_count']}",
    ]

    if summary["mode"] == "responses":
        lines.extend(
            [
                f"- Passed cases: {summary['passed_cases']}",
                f"- Failed cases: {summary['failed_cases']}",
                f"- Assertion pass rate: {summary['assertion_pass_rate']}",
            ]
        )

    lines.extend(["", "## Fixture Validation", ""])
    if summary["fixture_errors"]:
        for error in summary["fixture_errors"]:
            lines.append(f"- {error}")
    else:
        lines.append("No fixture errors.")

    if summary["mode"] == "responses":
        lines.extend(["", "## Response Results", ""])
        for case in summary["results"]:
            lines.append(f"### {case['id']}")
            lines.append("")
            lines.append(f"- Skill: `{case['skill']}`")
            lines.append(f"- Passed: `{case['passed']}`")
            for assertion in case["assertions"]:
                status = "PASS" if assertion["passed"] else "FAIL"
                lines.append(f"- {status} `{assertion['id']}`: {assertion['evidence']}")
            lines.append("")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run coffee-skill artifact quality eval checks.")
    parser.add_argument("--eval-set", type=Path, default=DEFAULT_EVAL_SET)
    parser.add_argument("--responses-dir", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    eval_set = load_json(args.eval_set)
    eval_root = args.eval_set.parent
    fixture_errors: list[str] = []
    for case in eval_set["cases"]:
        fixture_errors.extend(validate_fixture(case, eval_root))

    results: list[dict[str, Any]] = []
    mode = "fixture"
    if args.responses_dir:
        mode = "responses"
        results = [evaluate_response_case(case, args.responses_dir, eval_root) for case in eval_set["cases"]]

    assertion_total = sum(len(case["assertions"]) for case in results)
    assertion_passed = sum(
        1
        for case in results
        for assertion in case["assertions"]
        if assertion["passed"]
    )
    summary = {
        "schema_version": 1,
        "mode": mode,
        "case_count": len(eval_set["cases"]),
        "fixture_error_count": len(fixture_errors),
        "fixture_errors": fixture_errors,
        "passed_cases": sum(1 for case in results if case["passed"]),
        "failed_cases": sum(1 for case in results if not case["passed"]),
        "assertion_total": assertion_total,
        "assertion_passed": assertion_passed,
        "assertion_pass_rate": round(assertion_passed / assertion_total, 4) if assertion_total else None,
        "results": results,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown_report(summary, args.output.with_suffix(".md"))

    print(
        json.dumps(
            {
                "mode": summary["mode"],
                "case_count": summary["case_count"],
                "fixture_error_count": summary["fixture_error_count"],
                "passed_cases": summary["passed_cases"],
                "failed_cases": summary["failed_cases"],
                "assertion_pass_rate": summary["assertion_pass_rate"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )

    if fixture_errors or any(not case["passed"] for case in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
