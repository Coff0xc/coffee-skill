from __future__ import annotations

import argparse
import json
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path


STYLE_BY_TYPE = {
    "data": "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;",
    "module": "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;",
    "algorithm": "rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;",
    "model": "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;",
    "loss": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;",
    "evaluation": "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;",
    "output": "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;",
    "claim": "shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;",
    "note": "rounded=0;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;dashed=1;",
    "source": "shape=document;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;",
}

EDGE_STYLE = "endArrow=block;html=1;rounded=0;strokeWidth=2;"


def safe_id(raw: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_-]+", "_", raw.strip())
    if not value:
        raise ValueError("empty id")
    if value[0].isdigit():
        value = f"n_{value}"
    return value


def add_geometry(cell: ET.Element, x: float, y: float, width: float, height: float) -> None:
    ET.SubElement(
        cell,
        "mxGeometry",
        {
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "as": "geometry",
        },
    )


def build_page(page: dict[str, object]) -> ET.Element:
    model = ET.Element(
        "mxGraphModel",
        {
            "dx": "1200",
            "dy": "800",
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": str(page.get("pageWidth", 1400)),
            "pageHeight": str(page.get("pageHeight", 900)),
            "math": "0",
            "shadow": "0",
        },
    )
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

    seen: set[str] = set()
    for node in page.get("nodes", []):  # type: ignore[union-attr]
        if not isinstance(node, dict):
            raise ValueError("node must be an object")
        node_id = safe_id(str(node["id"]))
        if node_id in seen:
            raise ValueError(f"duplicate node id: {node_id}")
        seen.add(node_id)
        node_type = str(node.get("type", "module"))
        style = str(node.get("style", STYLE_BY_TYPE.get(node_type, STYLE_BY_TYPE["module"])))
        cell = ET.SubElement(
            root,
            "mxCell",
            {
                "id": node_id,
                "value": str(node.get("label", node_id)),
                "style": style,
                "vertex": "1",
                "parent": "1",
            },
        )
        add_geometry(
            cell,
            float(node.get("x", 40)),
            float(node.get("y", 40)),
            float(node.get("width", 160)),
            float(node.get("height", 70)),
        )

    for idx, edge in enumerate(page.get("edges", []), 1):  # type: ignore[union-attr]
        if not isinstance(edge, dict):
            raise ValueError("edge must be an object")
        source = safe_id(str(edge["source"]))
        target = safe_id(str(edge["target"]))
        if source not in seen:
            raise ValueError(f"edge source not found: {source}")
        if target not in seen:
            raise ValueError(f"edge target not found: {target}")
        cell = ET.SubElement(
            root,
            "mxCell",
            {
                "id": safe_id(str(edge.get("id", f"e_{idx}_{source}_{target}"))),
                "value": str(edge.get("label", "")),
                "style": str(edge.get("style", EDGE_STYLE)),
                "edge": "1",
                "parent": "1",
                "source": source,
                "target": target,
            },
        )
        ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    return model


def build_drawio(spec: dict[str, object]) -> ET.Element:
    now_ms = str(int(time.time() * 1000))
    mxfile = ET.Element(
        "mxfile",
        {
            "host": "app.diagrams.net",
            "modified": now_ms,
            "agent": "coffee-skill",
            "version": "24.0.0",
            "type": "device",
        },
    )
    pages = spec.get("pages") or [{"name": spec.get("title", "Overview"), "nodes": spec.get("nodes", []), "edges": spec.get("edges", [])}]
    if not isinstance(pages, list) or not pages:
        raise ValueError("spec.pages must be a non-empty list")
    for index, page in enumerate(pages, 1):
        if not isinstance(page, dict):
            raise ValueError("page must be an object")
        diagram = ET.SubElement(
            mxfile,
            "diagram",
            {
                "id": f"page_{index}",
                "name": str(page.get("name", f"Page {index}")),
            },
        )
        diagram.append(build_page(page))
    return mxfile


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate editable diagrams.net/draw.io XML from a research diagram JSON spec.")
    parser.add_argument("spec", type=Path, help="Path to JSON spec")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Output .drawio path")
    args = parser.parse_args()

    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    mxfile = build_drawio(spec)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    ET.indent(mxfile, space="  ")
    tree = ET.ElementTree(mxfile)
    tree.write(args.output, encoding="utf-8", xml_declaration=True)
    print(json.dumps({"output": str(args.output), "pages": len(mxfile.findall("diagram"))}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
