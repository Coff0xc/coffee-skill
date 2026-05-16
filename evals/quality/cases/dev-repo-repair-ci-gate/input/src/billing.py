from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP


def normalize_amount(value: str | int | float | Decimal) -> Decimal:
    if isinstance(value, Decimal):
        return value
    if isinstance(value, str):
        cleaned = value.replace("$", "").strip()
        return Decimal(cleaned)
    return Decimal(str(value))


def invoice_total(rows: list[dict[str, str | int | float | Decimal]], discount_rate: Decimal, tax_rate: Decimal) -> Decimal:
    subtotal = sum(
        normalize_amount(row["quantity"]) * normalize_amount(row["unit_price"])
        for row in rows
    )
    discount = normalize_amount(rows[0].get("discount", "0")) if rows else Decimal("0")
    taxable = subtotal - discount
    total = taxable + (taxable * tax_rate)
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
