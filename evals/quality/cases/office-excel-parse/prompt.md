# Quality Eval Prompt: Office Excel Data Parse Gate

Use `coff0xc-office-doc-tools` to parse the attached messy CSV and workbook notes into an auditable Excel delivery package.

Goal: produce a workbook package that proves the agent inspected the data shape, preserved raw/source assumptions, used formulas for derived fields, and checked formula/chart quality.

Required output directory shape:

```text
responses/office-excel-parse/
├── workbook-plan.md
├── parse-audit.md
├── formula-checks.md
├── render-checks/
│   └── dashboard.png
└── final/
    └── billing-exceptions.xlsx
```

Constraints:
- Do not hand-wave CSV parsing.
- Do not hardcode derived values in prose only.
- Do not overwrite raw data.
- `final/billing-exceptions.xlsx` must be a real OOXML workbook package, not a renamed or empty placeholder.
- The workbook must contain inspectable sheets, table parts, formulas, checks, chart evidence, and bounded references for automated structure checks.

Required evidence:
- `parse-audit.md` must discuss encoding, delimiter, headers, units, date/number parsing, nulls, duplicate rows, abnormal values, and sheet/range inspection.
- `workbook-plan.md` must include Raw/Source, Assumptions, Model or Detail, Checks, and Dashboard/Summary sheets.
- `formula-checks.md` must mention bounded ranges, formula-derived values, checks/trace, formula error scan, and chart helper ranges.
- `render-checks/dashboard.png` must be a valid PNG dashboard/render evidence file. If native rendering is unavailable, create deterministic visual evidence from workbook values and state the limitation in `formula-checks.md`; do not use an empty renamed file.
