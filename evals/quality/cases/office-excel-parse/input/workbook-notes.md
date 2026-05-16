# Workbook Notes

The final workbook is for finance operations. Leadership wants a dashboard first, but analysts must be able to audit every number.

Known pitfalls:
- Currency values mix `$1,240.50`, `980.00`, and `12,400`.
- Dates mix ISO, US short date, slash date, and one invalid value.
- There is a duplicate invoice row.
- Blank amount and review_hours values should be explicit quality issues, not silently converted to zero.
- Negative invoice amounts should be flagged for review.
