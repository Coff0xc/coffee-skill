from __future__ import annotations

import argparse
import filecmp
import importlib.util
import json
import re
import struct
import sys
import zipfile
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVAL_SET = ROOT / "evals" / "quality" / "eval-set.json"
DEFAULT_RESPONSES = ROOT / "evals" / "quality" / "golden-responses"
DEFAULT_OUTPUT = ROOT / "evals" / "quality" / "quality-eval-results.json"

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
}

SUPPORTED_ASSERTIONS = {
    "file_exists",
    "file_contains_all",
    "file_not_contains_regex",
    "file_unchanged_if_present",
    "python_billing_behavior",
    "png_dimensions",
    "pptx_ooxml_structure",
    "xlsx_workbook_structure",
    "docx_ooxml_structure",
}


@dataclass
class AssertionResult:
    id: str
    passed: bool
    evidence: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def rel_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.name


def resolve_case_path(eval_root: Path, rel: str) -> Path:
    return (eval_root / rel).resolve()


def q(prefix: str, name: str) -> str:
    return f"{{{NS[prefix]}}}{name}"


def parse_xml(data: bytes) -> ET.Element:
    return ET.fromstring(data)


def parse_zip_xml(package: zipfile.ZipFile, name: str) -> ET.Element:
    return parse_xml(package.read(name))


def xml_text(root: ET.Element, tag_names: set[str] | None = None) -> str:
    values: list[str] = []
    for elem in root.iter():
        if tag_names is None or elem.tag in tag_names:
            if elem.text:
                values.append(elem.text)
    return " ".join(values)


def missing_terms(text: str, terms: list[str]) -> list[str]:
    folded = text.lower()
    return [term for term in terms if term.lower() not in folded]


def natural_part_number(path: str, pattern: str) -> int:
    match = re.search(pattern, path)
    return int(match.group(1)) if match else 0


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
        if assertion_type not in SUPPORTED_ASSERTIONS:
            errors.append(f"{case['id']}: unsupported assertion type {assertion_type}")
        if assertion_type == "file_unchanged_if_present":
            reference = assertion.get("reference")
            if not reference or not resolve_case_path(eval_root, reference).exists():
                errors.append(f"{case['id']}: missing reference for assertion {assertion.get('id')}")
    return errors


def png_dimensions(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", header[16:24])


def evaluate_png_dimensions(assertion: dict[str, Any], target: Path) -> AssertionResult:
    if not target.exists():
        return AssertionResult(assertion["id"], False, f"{rel_path(target)} does not exist")
    dims = png_dimensions(target)
    if dims is None:
        return AssertionResult(assertion["id"], False, f"{rel_path(target)} is not a PNG")
    min_width = int(assertion.get("min_width", 1))
    min_height = int(assertion.get("min_height", 1))
    passed = dims[0] >= min_width and dims[1] >= min_height
    return AssertionResult(
        assertion["id"],
        passed,
        f"png dimensions {dims[0]}x{dims[1]}, required >= {min_width}x{min_height}",
    )


def open_ooxml_zip(path: Path) -> tuple[zipfile.ZipFile | None, str | None]:
    if not path.exists():
        return None, f"{rel_path(path)} does not exist"
    if not zipfile.is_zipfile(path):
        return None, f"{rel_path(path)} is not a valid OOXML zip package"
    return zipfile.ZipFile(path), None


def slide_shape_metrics(root: ET.Element) -> dict[str, Any]:
    text_shapes = 0
    all_text = xml_text(root, {q("a", "t")})
    for shape in root.findall(".//p:sp", NS):
        if shape.findall(".//a:t", NS):
            text_shapes += 1

    positions: list[tuple[int, int, int, int]] = []
    for xfrm in root.findall(".//a:xfrm", NS):
        off = xfrm.find("a:off", NS)
        ext = xfrm.find("a:ext", NS)
        if off is None or ext is None:
            continue
        try:
            positions.append(
                (
                    int(off.attrib.get("x", "0")) // 500000,
                    int(off.attrib.get("y", "0")) // 500000,
                    int(ext.attrib.get("cx", "0")) // 500000,
                    int(ext.attrib.get("cy", "0")) // 500000,
                )
            )
        except ValueError:
            continue

    geoms = [
        elem.attrib.get("prst", "")
        for elem in root.findall(".//a:prstGeom", NS)
        if elem.attrib.get("prst")
    ]
    srgb_colors = [
        elem.attrib.get("val", "")
        for elem in root.findall(".//a:srgbClr", NS)
        if elem.attrib.get("val")
    ]
    signature = (
        len(root.findall(".//p:sp", NS)),
        text_shapes,
        len(root.findall(".//p:pic", NS)),
        len(root.findall(".//p:graphicFrame", NS)),
        tuple(sorted(positions[:6])),
    )
    return {
        "text": all_text,
        "shape_count": len(root.findall(".//p:sp", NS)),
        "text_shape_count": text_shapes,
        "picture_count": len(root.findall(".//p:pic", NS)),
        "graphic_frame_count": len(root.findall(".//p:graphicFrame", NS)),
        "chart_count": len(root.findall(".//c:chart", NS)),
        "round_rect_count": sum(1 for item in geoms if item == "roundRect"),
        "srgb_colors": srgb_colors,
        "signature": signature,
    }


def evaluate_pptx_ooxml(assertion: dict[str, Any], target: Path) -> AssertionResult:
    package, error = open_ooxml_zip(target)
    if error:
        return AssertionResult(assertion["id"], False, error)

    failures: list[str] = []
    metrics: dict[str, Any] = {}
    assert package is not None
    with package:
        names = set(package.namelist())
        required_entries = assertion.get(
            "required_entries",
            ["[Content_Types].xml", "ppt/presentation.xml", "ppt/_rels/presentation.xml.rels"],
        )
        missing_entries = [name for name in required_entries if name not in names]
        if missing_entries:
            failures.append(f"missing entries: {', '.join(missing_entries)}")

        slide_names = sorted(
            [name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)],
            key=lambda item: natural_part_number(item, r"slide(\d+)\.xml"),
        )
        min_slides = int(assertion.get("min_slides", 1))
        if len(slide_names) < min_slides:
            failures.append(f"slide count {len(slide_names)} < {min_slides}")

        slide_metrics = [slide_shape_metrics(parse_zip_xml(package, name)) for name in slide_names]
        global_text = " ".join(item["text"] for item in slide_metrics)
        missing = missing_terms(global_text, assertion.get("required_text_terms", []))
        if missing:
            failures.append(f"missing text terms: {', '.join(missing)}")

        source_slide_count = sum(1 for item in slide_metrics if "source:" in item["text"].lower())
        min_source_slides = int(assertion.get("min_source_slides", 0))
        if source_slide_count < min_source_slides:
            failures.append(f"source-note slides {source_slide_count} < {min_source_slides}")

        image_only = [
            str(idx + 1)
            for idx, item in enumerate(slide_metrics)
            if item["picture_count"] > 0 and item["text_shape_count"] == 0 and item["graphic_frame_count"] == 0
        ]
        if assertion.get("no_image_only_slides", True) and image_only:
            failures.append(f"image-only slides: {', '.join(image_only)}")

        distinct_layouts = len({item["signature"] for item in slide_metrics})
        min_layouts = int(assertion.get("min_distinct_layout_signatures", 1))
        if distinct_layouts < min_layouts:
            failures.append(f"layout signatures {distinct_layouts} < {min_layouts}")

        text_shapes = sum(item["text_shape_count"] for item in slide_metrics)
        charts = sum(item["chart_count"] for item in slide_metrics)
        graphics = sum(item["graphic_frame_count"] for item in slide_metrics)
        min_text_shapes = int(assertion.get("min_text_shapes", 0))
        if text_shapes < min_text_shapes:
            failures.append(f"editable text shapes {text_shapes} < {min_text_shapes}")

        min_chart_or_diagram = int(assertion.get("min_chart_or_diagram_objects", 0))
        chart_or_diagram = charts + graphics
        if chart_or_diagram < min_chart_or_diagram:
            failures.append(f"chart/diagram objects {chart_or_diagram} < {min_chart_or_diagram}")

        round_rects = sum(item["round_rect_count"] for item in slide_metrics)
        max_round_rects = assertion.get("max_round_rects")
        if max_round_rects is not None and round_rects > int(max_round_rects):
            failures.append(f"roundRect count {round_rects} > {max_round_rects}")

        color_count = len({color.upper() for item in slide_metrics for color in item["srgb_colors"]})
        min_colors = int(assertion.get("min_distinct_srgb_colors", 0))
        if color_count < min_colors:
            failures.append(f"distinct srgb colors {color_count} < {min_colors}")

        chart_parts = [name for name in names if re.fullmatch(r"ppt/charts/chart\d+\.xml", name)]
        min_chart_parts = int(assertion.get("min_chart_parts", 0))
        if len(chart_parts) < min_chart_parts:
            failures.append(f"chart parts {len(chart_parts)} < {min_chart_parts}")

        metrics = {
            "slides": len(slide_names),
            "layout_signatures": distinct_layouts,
            "text_shapes": text_shapes,
            "chart_or_diagram_objects": chart_or_diagram,
            "chart_parts": len(chart_parts),
            "source_note_slides": source_slide_count,
            "distinct_colors": color_count,
            "round_rects": round_rects,
        }

    return AssertionResult(
        assertion["id"],
        not failures,
        json.dumps(metrics, ensure_ascii=False, sort_keys=True) if not failures else "; ".join(failures),
    )


def column_index(col: str) -> int:
    value = 0
    for char in col.upper():
        value = value * 26 + (ord(char) - ord("A") + 1)
    return value


def column_name(index: int) -> str:
    chars: list[str] = []
    while index:
        index, remainder = divmod(index - 1, 26)
        chars.append(chr(ord("A") + remainder))
    return "".join(reversed(chars))


def split_cell_ref(ref: str) -> tuple[int, int]:
    match = re.fullmatch(r"\$?([A-Z]+)\$?(\d+)", ref.upper())
    if not match:
        raise ValueError(f"invalid cell reference {ref}")
    return column_index(match.group(1)), int(match.group(2))


def cells_in_range(start: str, end: str) -> list[str]:
    start_col, start_row = split_cell_ref(start)
    end_col, end_row = split_cell_ref(end)
    refs: list[str] = []
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            refs.append(f"{column_name(col)}{row}")
    return refs


def decode_xlsx_value(cell_type: str | None, raw_value: str | None, shared_strings: list[str]) -> Any:
    if raw_value is None:
        return None
    if cell_type == "s":
        try:
            return shared_strings[int(raw_value)]
        except (IndexError, ValueError):
            return raw_value
    if cell_type == "b":
        return raw_value == "1"
    try:
        decimal = Decimal(raw_value)
    except InvalidOperation:
        return raw_value
    if decimal == decimal.to_integral_value():
        return int(decimal)
    return float(decimal)


def decode_inline_string(cell: ET.Element) -> str:
    values = [
        elem.text
        for elem in cell.findall(".//x:is//x:t", NS)
        if elem.text
    ]
    return "".join(values)


def load_xlsx_cells(package: zipfile.ZipFile) -> tuple[dict[str, dict[str, dict[str, Any]]], dict[str, Any]]:
    workbook = parse_zip_xml(package, "xl/workbook.xml")
    rels = parse_zip_xml(package, "xl/_rels/workbook.xml.rels")
    rel_targets = {
        rel.attrib["Id"]: rel.attrib["Target"].lstrip("/")
        for rel in rels.findall("rel:Relationship", NS)
        if "Id" in rel.attrib and "Target" in rel.attrib
    }

    shared_strings: list[str] = []
    if "xl/sharedStrings.xml" in package.namelist():
        shared_root = parse_zip_xml(package, "xl/sharedStrings.xml")
        for item in shared_root.findall("x:si", NS):
            shared_strings.append(xml_text(item, {q("x", "t")}))

    sheets: dict[str, dict[str, dict[str, Any]]] = {}
    sheet_targets: dict[str, str] = {}
    for sheet in workbook.findall("x:sheets/x:sheet", NS):
        name = sheet.attrib["name"]
        rel_id = sheet.attrib.get(q("r", "id"))
        target = rel_targets.get(rel_id or "", "")
        if target and not target.startswith("xl/"):
            target = f"xl/{target}"
        sheet_targets[name] = target
        if not target:
            continue
        root = parse_zip_xml(package, target)
        cells: dict[str, dict[str, Any]] = {}
        for cell in root.findall(".//x:c", NS):
            ref = cell.attrib.get("r")
            if not ref:
                continue
            cell_type = cell.attrib.get("t")
            formula_elem = cell.find("x:f", NS)
            value_elem = cell.find("x:v", NS)
            formula = formula_elem.text if formula_elem is not None else None
            raw_value = value_elem.text if value_elem is not None else None
            value = decode_inline_string(cell) if cell_type == "inlineStr" else decode_xlsx_value(cell_type, raw_value, shared_strings)
            cells[ref.upper()] = {
                "value": value,
                "formula": formula,
                "raw_value": raw_value,
            }
        sheets[name] = cells

    metadata = {
        "sheet_targets": sheet_targets,
        "shared_string_count": len(shared_strings),
    }
    return sheets, metadata


def coerce_decimal(value: Any) -> Decimal:
    if value is None or value == "":
        return Decimal("0")
    if isinstance(value, Decimal):
        return value
    if isinstance(value, int | float):
        return Decimal(str(value))
    normalized = str(value).strip().replace("$", "").replace(",", "")
    if normalized.endswith("%"):
        return Decimal(normalized[:-1]) / Decimal("100")
    return Decimal(normalized)


def split_formula_args(text: str) -> list[str]:
    args: list[str] = []
    current: list[str] = []
    depth = 0
    in_quote = False
    idx = 0
    while idx < len(text):
        char = text[idx]
        if char == '"':
            in_quote = not in_quote
        elif not in_quote and char == "(":
            depth += 1
        elif not in_quote and char == ")":
            depth -= 1
        elif not in_quote and depth == 0 and char == ",":
            args.append("".join(current).strip())
            current = []
            idx += 1
            continue
        current.append(char)
        idx += 1
    if current:
        args.append("".join(current).strip())
    return args


def strip_formula_string(value: str) -> str:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    return value


def split_sheet_ref(ref: str, current_sheet: str) -> tuple[str, str, str | None]:
    ref = ref.strip()
    sheet_name = current_sheet
    cell_range = ref
    if "!" in ref:
        sheet_name, cell_range = ref.split("!", 1)
        sheet_name = sheet_name.strip("'")
    cell_range = cell_range.replace("$", "").upper()
    if ":" in cell_range:
        start, end = cell_range.split(":", 1)
        return sheet_name, start, end
    return sheet_name, cell_range, None


def get_xlsx_range_values(
    sheets: dict[str, dict[str, dict[str, Any]]],
    ref: str,
    current_sheet: str,
) -> list[Any]:
    sheet_name, start, end = split_sheet_ref(ref, current_sheet)
    if sheet_name not in sheets:
        raise ValueError(f"unknown sheet {sheet_name}")
    refs = cells_in_range(start, end) if end else [start]
    return [sheets[sheet_name].get(cell_ref, {}).get("value") for cell_ref in refs]


def find_top_level_operator(expr: str, operators: set[str]) -> int | None:
    depth = 0
    in_quote = False
    for idx in range(len(expr) - 1, -1, -1):
        char = expr[idx]
        if char == '"':
            in_quote = not in_quote
        elif in_quote:
            continue
        elif char == ")":
            depth += 1
        elif char == "(":
            depth -= 1
        elif depth == 0 and char in operators and idx > 0:
            return idx
    return None


def evaluate_xlsx_formula(
    formula: str,
    sheets: dict[str, dict[str, dict[str, Any]]],
    current_sheet: str,
) -> Decimal:
    expr = formula.strip()
    if expr.startswith("="):
        expr = expr[1:]

    operator_index = find_top_level_operator(expr, {"+", "-"})
    if operator_index is not None:
        left = evaluate_xlsx_formula(expr[:operator_index], sheets, current_sheet)
        right = evaluate_xlsx_formula(expr[operator_index + 1 :], sheets, current_sheet)
        return left + right if expr[operator_index] == "+" else left - right

    number_match = re.fullmatch(r"-?\d+(?:\.\d+)?", expr)
    if number_match:
        return Decimal(expr)

    function_match = re.fullmatch(r"([A-Z]+)\((.*)\)", expr, flags=re.IGNORECASE)
    if not function_match:
        values = get_xlsx_range_values(sheets, expr, current_sheet)
        return coerce_decimal(values[0])

    function_name = function_match.group(1).upper()
    args = split_formula_args(function_match.group(2))
    if function_name == "SUM":
        total = Decimal("0")
        for arg in args:
            for value in get_xlsx_range_values(sheets, arg, current_sheet):
                total += coerce_decimal(value)
        return total
    if function_name == "COUNTA":
        return Decimal(
            sum(
                1
                for arg in args
                for value in get_xlsx_range_values(sheets, arg, current_sheet)
                if value not in (None, "")
            )
        )
    if function_name == "COUNTIF":
        values = get_xlsx_range_values(sheets, args[0], current_sheet)
        criterion = strip_formula_string(args[1])
        return Decimal(sum(1 for value in values if str(value) == criterion))
    if function_name == "COUNTIFS":
        ranges = [get_xlsx_range_values(sheets, args[idx], current_sheet) for idx in range(0, len(args), 2)]
        criteria = [strip_formula_string(args[idx]) for idx in range(1, len(args), 2)]
        count = 0
        for row_values in zip(*ranges, strict=False):
            if all(str(value) == criterion for value, criterion in zip(row_values, criteria, strict=True)):
                count += 1
        return Decimal(count)
    if function_name == "SUMIFS":
        sum_values = get_xlsx_range_values(sheets, args[0], current_sheet)
        criteria_ranges = [
            get_xlsx_range_values(sheets, args[idx], current_sheet)
            for idx in range(1, len(args), 2)
        ]
        criteria = [strip_formula_string(args[idx]) for idx in range(2, len(args), 2)]
        total = Decimal("0")
        for row_idx, value in enumerate(sum_values):
            if all(
                row_idx < len(range_values) and str(range_values[row_idx]) == criterion
                for range_values, criterion in zip(criteria_ranges, criteria, strict=True)
            ):
                total += coerce_decimal(value)
        return total

    raise ValueError(f"unsupported formula function {function_name}")


def compare_expected(actual: Any, expected: Any, tolerance: Decimal = Decimal("0.0001")) -> bool:
    try:
        return abs(coerce_decimal(actual) - coerce_decimal(expected)) <= tolerance
    except (InvalidOperation, ValueError):
        return str(actual) == str(expected)


def evaluate_xlsx_ooxml(assertion: dict[str, Any], target: Path) -> AssertionResult:
    package, error = open_ooxml_zip(target)
    if error:
        return AssertionResult(assertion["id"], False, error)

    failures: list[str] = []
    metrics: dict[str, Any] = {}
    assert package is not None
    with package:
        names = set(package.namelist())
        required_entries = assertion.get(
            "required_entries",
            ["[Content_Types].xml", "xl/workbook.xml", "xl/styles.xml"],
        )
        missing_entries = [name for name in required_entries if name not in names]
        if missing_entries:
            failures.append(f"missing entries: {', '.join(missing_entries)}")

        sheets, metadata = load_xlsx_cells(package)
        required_sheets = assertion.get("required_sheets", [])
        sheet_names_folded = {name.lower(): name for name in sheets}
        missing_sheets = [name for name in required_sheets if name.lower() not in sheet_names_folded]
        if missing_sheets:
            failures.append(f"missing sheets: {', '.join(missing_sheets)}")

        formulas: list[tuple[str, str, str]] = []
        values: list[Any] = []
        for sheet_name, cells in sheets.items():
            for cell_ref, cell in cells.items():
                values.append(cell.get("value"))
                if cell.get("formula"):
                    formulas.append((sheet_name, cell_ref, str(cell["formula"])))

        min_formula_count = int(assertion.get("min_formula_count", 0))
        if len(formulas) < min_formula_count:
            failures.append(f"formula count {len(formulas)} < {min_formula_count}")

        formula_text = "\n".join(formula for _, _, formula in formulas)
        missing = missing_terms(formula_text, assertion.get("required_formula_terms", []))
        if missing:
            failures.append(f"missing formula terms: {', '.join(missing)}")

        banned_formula_regex = assertion.get("banned_formula_regex", [])
        banned_hits = [
            pattern
            for pattern in banned_formula_regex
            if re.search(pattern, formula_text, flags=re.IGNORECASE)
        ]
        if banned_hits:
            failures.append(f"banned formula patterns: {', '.join(banned_hits)}")

        error_literals = {
            "#REF!",
            "#DIV/0!",
            "#VALUE!",
            "#NAME?",
            "#N/A",
        }
        hits = [str(value) for value in values if str(value).upper() in error_literals]
        if assertion.get("forbid_error_literals", True) and hits:
            failures.append(f"error literals found: {', '.join(hits)}")

        for item in assertion.get("expected_cells", []):
            sheet_name = item["sheet"]
            cell_ref = item["cell"].upper()
            expected = item["value"]
            cell = sheets.get(sheet_name, {}).get(cell_ref, {})
            formula = cell.get("formula")
            actual = cell.get("value")
            if formula and actual is None:
                try:
                    actual = evaluate_xlsx_formula(str(formula), sheets, sheet_name)
                except Exception as exc:  # noqa: BLE001 - candidate formulas are arbitrary.
                    failures.append(f"{sheet_name}!{cell_ref} expected-cell recalc failed: {exc}")
                    continue
            if not compare_expected(actual, expected):
                failures.append(f"{sheet_name}!{cell_ref} expected {expected!r}, got {actual!r}")

        recalculated = 0
        for item in assertion.get("expected_formula_results", []):
            sheet_name = item["sheet"]
            cell_ref = item["cell"].upper()
            expected = item["value"]
            cell = sheets.get(sheet_name, {}).get(cell_ref, {})
            formula = cell.get("formula")
            if not formula:
                failures.append(f"{sheet_name}!{cell_ref} has no formula")
                continue
            cached_value = cell.get("value")
            if cached_value is not None and not compare_expected(cached_value, expected):
                failures.append(f"{sheet_name}!{cell_ref} cached expected {expected!r}, got {cached_value!r}")
            try:
                actual = evaluate_xlsx_formula(str(formula), sheets, sheet_name)
            except Exception as exc:  # noqa: BLE001 - candidate formulas are arbitrary.
                failures.append(f"{sheet_name}!{cell_ref} formula recalc failed: {exc}")
                continue
            recalculated += 1
            if not compare_expected(actual, expected):
                failures.append(f"{sheet_name}!{cell_ref} recalculated expected {expected!r}, got {actual!s}")

        chart_parts = [name for name in names if re.fullmatch(r"xl/charts/chart\d+\.xml", name)]
        min_chart_parts = int(assertion.get("min_chart_parts", 0))
        if len(chart_parts) < min_chart_parts:
            failures.append(f"chart parts {len(chart_parts)} < {min_chart_parts}")

        table_parts = [name for name in names if re.fullmatch(r"xl/tables/table\d+\.xml", name)]
        min_table_parts = int(assertion.get("min_table_parts", 0))
        if len(table_parts) < min_table_parts:
            failures.append(f"table parts {len(table_parts)} < {min_table_parts}")

        metrics = {
            "sheets": sorted(sheets.keys()),
            "formulas": len(formulas),
            "recalculated_formulas": recalculated,
            "charts": len(chart_parts),
            "tables": len(table_parts),
            "shared_strings": metadata["shared_string_count"],
        }

    return AssertionResult(
        assertion["id"],
        not failures,
        json.dumps(metrics, ensure_ascii=False, sort_keys=True) if not failures else "; ".join(failures),
    )


def document_relationship_types(package: zipfile.ZipFile) -> set[str]:
    if "word/_rels/document.xml.rels" not in package.namelist():
        return set()
    root = parse_zip_xml(package, "word/_rels/document.xml.rels")
    return {
        rel.attrib.get("Type", "")
        for rel in root.findall("rel:Relationship", NS)
        if rel.attrib.get("Type")
    }


def content_type_parts(package: zipfile.ZipFile) -> set[str]:
    if "[Content_Types].xml" not in package.namelist():
        return set()
    root = parse_zip_xml(package, "[Content_Types].xml")
    return {
        elem.attrib.get("PartName", "").lstrip("/")
        for elem in root.findall("ct:Override", NS)
        if elem.attrib.get("PartName")
    }


def evaluate_docx_ooxml(assertion: dict[str, Any], target: Path) -> AssertionResult:
    package, error = open_ooxml_zip(target)
    if error:
        return AssertionResult(assertion["id"], False, error)

    failures: list[str] = []
    metrics: dict[str, Any] = {}
    assert package is not None
    with package:
        names = set(package.namelist())
        required_entries = assertion.get(
            "required_entries",
            ["[Content_Types].xml", "word/document.xml", "word/styles.xml", "word/numbering.xml"],
        )
        missing_entries = [name for name in required_entries if name not in names]
        if missing_entries:
            failures.append(f"missing entries: {', '.join(missing_entries)}")

        if "word/document.xml" not in names:
            return AssertionResult(assertion["id"], False, "; ".join(failures))

        document = parse_zip_xml(package, "word/document.xml")
        document_text = xml_text(document, {q("w", "t"), q("w", "delText"), q("w", "instrText")})

        comments_root = parse_zip_xml(package, "word/comments.xml") if "word/comments.xml" in names else None
        comments_text = xml_text(comments_root, {q("w", "t"), q("w", "delText"), q("w", "instrText")}) if comments_root is not None else ""
        comment_count = len(comments_root.findall("w:comment", NS)) if comments_root is not None else 0
        min_comments = int(assertion.get("min_comments", 0))
        if comment_count < min_comments:
            failures.append(f"comments {comment_count} < {min_comments}")

        comment_starts = len(document.findall(".//w:commentRangeStart", NS))
        comment_ends = len(document.findall(".//w:commentRangeEnd", NS))
        comment_refs = len(document.findall(".//w:commentReference", NS))
        if assertion.get("require_comment_anchors", False):
            if not (comment_starts >= min_comments and comment_ends >= min_comments and comment_refs >= min_comments):
                failures.append(
                    f"comment anchors start/end/ref={comment_starts}/{comment_ends}/{comment_refs}, expected >= {min_comments}"
                )

        insertions = len(document.findall(".//w:ins", NS))
        deletions = len(document.findall(".//w:del", NS))
        min_tracked = int(assertion.get("min_tracked_change_tags", 0))
        if insertions + deletions < min_tracked:
            failures.append(f"tracked change tags {insertions + deletions} < {min_tracked}")

        style_ids: set[str] = set()
        if "word/styles.xml" in names:
            styles = parse_zip_xml(package, "word/styles.xml")
            style_ids = {
                style.attrib.get(q("w", "styleId"), "")
                for style in styles.findall("w:style", NS)
                if style.attrib.get(q("w", "styleId"))
            }
        required_styles = set(assertion.get("required_style_ids", []))
        missing_styles = sorted(required_styles - style_ids)
        if missing_styles:
            failures.append(f"missing style ids: {', '.join(missing_styles)}")

        numbering_count = 0
        if "word/numbering.xml" in names:
            numbering = parse_zip_xml(package, "word/numbering.xml")
            numbering_count = len(numbering.findall("w:num", NS))
        if assertion.get("require_numbering", False) and numbering_count == 0:
            failures.append("numbering.xml has no w:num definitions")

        table_count = len(document.findall(".//w:tbl", NS))
        min_tables = int(assertion.get("min_tables", 0))
        if table_count < min_tables:
            failures.append(f"tables {table_count} < {min_tables}")

        tbl_grid_count = len(document.findall(".//w:tblGrid", NS))
        tcw_count = len(document.findall(".//w:tcW", NS))
        if assertion.get("require_table_geometry", False) and (tbl_grid_count == 0 or tcw_count == 0):
            failures.append(f"table geometry missing tblGrid={tbl_grid_count}, tcW={tcw_count}")

        rel_types = document_relationship_types(package)
        if assertion.get("require_comments_rel", False) and not any(rel.endswith("/comments") for rel in rel_types):
            failures.append("document rels missing comments relationship")
        if assertion.get("require_header_footer_rels", False):
            if not any(rel.endswith("/header") for rel in rel_types):
                failures.append("document rels missing header relationship")
            if not any(rel.endswith("/footer") for rel in rel_types):
                failures.append("document rels missing footer relationship")

        content_parts = content_type_parts(package)
        required_content_parts = set(assertion.get("required_content_type_parts", []))
        missing_content_parts = sorted(required_content_parts - content_parts)
        if missing_content_parts:
            failures.append(f"missing content-type parts: {', '.join(missing_content_parts)}")

        field_count = len(document.findall(".//w:fldChar", NS)) + len(document.findall(".//w:instrText", NS))
        for name in names:
            if re.fullmatch(r"word/(header|footer)\d+\.xml", name):
                part = parse_zip_xml(package, name)
                field_count += len(part.findall(".//w:fldChar", NS)) + len(part.findall(".//w:instrText", NS))
        min_fields = int(assertion.get("min_fields", 0))
        if field_count < min_fields:
            failures.append(f"fields {field_count} < {min_fields}")

        missing = missing_terms(document_text + " " + comments_text, assertion.get("required_text_terms", []))
        if missing:
            failures.append(f"missing document text terms: {', '.join(missing)}")

        metrics = {
            "comments": comment_count,
            "comment_anchors": {"start": comment_starts, "end": comment_ends, "ref": comment_refs},
            "tracked_insertions": insertions,
            "tracked_deletions": deletions,
            "style_count": len(style_ids),
            "numbering_defs": numbering_count,
            "tables": table_count,
            "tblGrid": tbl_grid_count,
            "tcW": tcw_count,
            "fields": field_count,
            "rels": sorted(rel_types),
        }

    return AssertionResult(
        assertion["id"],
        not failures,
        json.dumps(metrics, ensure_ascii=False, sort_keys=True) if not failures else "; ".join(failures),
    )


def evaluate_assertion(assertion: dict[str, Any], response_dir: Path, eval_root: Path) -> AssertionResult:
    assertion_id = assertion["id"]
    assertion_type = assertion["type"]
    target = response_dir / assertion["path"]

    if assertion_type == "file_exists":
        return AssertionResult(
            id=assertion_id,
            passed=target.exists(),
            evidence=f"{rel_path(target)} exists" if target.exists() else f"{rel_path(target)} does not exist",
        )

    if assertion_type == "file_contains_all":
        if not target.exists():
            return AssertionResult(id=assertion_id, passed=False, evidence=f"{rel_path(target)} does not exist")
        text = read_text(target).lower()
        missing = [term for term in assertion["terms"] if term.lower() not in text]
        return AssertionResult(
            id=assertion_id,
            passed=not missing,
            evidence="all terms found" if not missing else f"missing terms: {', '.join(missing)}",
        )

    if assertion_type == "file_not_contains_regex":
        if not target.exists():
            return AssertionResult(id=assertion_id, passed=False, evidence=f"{rel_path(target)} does not exist")
        text = read_text(target)
        hits = [pattern for pattern in assertion["patterns"] if re.search(pattern, text, flags=re.IGNORECASE)]
        return AssertionResult(
            id=assertion_id,
            passed=not hits,
            evidence="no banned patterns found" if not hits else f"matched banned patterns: {', '.join(hits)}",
        )

    if assertion_type == "file_unchanged_if_present":
        if not target.exists():
            return AssertionResult(id=assertion_id, passed=True, evidence=f"{rel_path(target)} absent, no churn")
        reference = resolve_case_path(eval_root, assertion["reference"])
        passed = filecmp.cmp(target, reference, shallow=False)
        return AssertionResult(
            id=assertion_id,
            passed=passed,
            evidence="matches reference" if passed else f"{rel_path(target)} differs from {rel_path(reference)}",
        )

    if assertion_type == "python_billing_behavior":
        if not target.exists():
            return AssertionResult(id=assertion_id, passed=False, evidence=f"{rel_path(target)} does not exist")
        module_name = f"quality_eval_billing_{response_dir.name.replace('-', '_')}"
        try:
            spec = importlib.util.spec_from_file_location(module_name, target)
            if spec is None or spec.loader is None:
                return AssertionResult(id=assertion_id, passed=False, evidence=f"could not load {rel_path(target)}")
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            old_dont_write_bytecode = sys.dont_write_bytecode
            sys.dont_write_bytecode = True
            try:
                spec.loader.exec_module(module)
            finally:
                sys.dont_write_bytecode = old_dont_write_bytecode
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

    if assertion_type == "png_dimensions":
        return evaluate_png_dimensions(assertion, target)

    if assertion_type == "pptx_ooxml_structure":
        return evaluate_pptx_ooxml(assertion, target)

    if assertion_type == "xlsx_workbook_structure":
        return evaluate_xlsx_ooxml(assertion, target)

    if assertion_type == "docx_ooxml_structure":
        return evaluate_docx_ooxml(assertion, target)

    return AssertionResult(id=assertion_id, passed=False, evidence=f"unsupported assertion type {assertion_type}")


def evaluate_response_case(case: dict[str, Any], responses_dir: Path, eval_root: Path) -> dict[str, Any]:
    case_dir = responses_dir / case["id"]
    assertion_results = [evaluate_assertion(assertion, case_dir, eval_root) for assertion in case["assertions"]]
    passed = all(item.passed for item in assertion_results)
    return {
        "id": case["id"],
        "skill": case["skill"],
        "category": case["category"],
        "response_dir": rel_path(case_dir),
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
                f"- Responses dir: `{summary['responses_dir']}`",
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

    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run coffee-skill artifact quality eval checks.")
    parser.add_argument("--eval-set", type=Path, default=DEFAULT_EVAL_SET)
    parser.add_argument("--responses-dir", type=Path, default=DEFAULT_RESPONSES)
    parser.add_argument("--fixture-only", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    eval_set = load_json(args.eval_set)
    eval_root = args.eval_set.parent
    fixture_errors: list[str] = []
    for case in eval_set["cases"]:
        fixture_errors.extend(validate_fixture(case, eval_root))

    results: list[dict[str, Any]] = []
    mode = "fixture"
    responses_dir = ""
    if not args.fixture_only:
        mode = "responses"
        responses_dir = rel_path(args.responses_dir)
        if not args.responses_dir.exists():
            fixture_errors.append(f"missing responses_dir: {responses_dir}")
        else:
            results = [evaluate_response_case(case, args.responses_dir, eval_root) for case in eval_set["cases"]]

    assertion_total = sum(len(case["assertions"]) for case in results)
    assertion_passed = sum(
        1
        for case in results
        for assertion in case["assertions"]
        if assertion["passed"]
    )
    summary = {
        "schema_version": 2,
        "mode": mode,
        "responses_dir": responses_dir,
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
                "responses_dir": summary["responses_dir"],
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
