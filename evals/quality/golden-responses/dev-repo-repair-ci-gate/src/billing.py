from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP


def normalize_amount(value: str | int | float | Decimal) -> Decimal:
    if isinstance(value, Decimal):
        return value
    normalized = str(value).strip().replace("$", "").replace(",", "")
    return Decimal(normalized)


def invoice_total(lines, discount_rate=Decimal("0"), tax_rate=Decimal("0")) -> Decimal:
    subtotal = Decimal("0")
    for line in lines:
        quantity = normalize_amount(line["quantity"])
        unit_price = normalize_amount(line["unit_price"])
        subtotal += quantity * unit_price
    discounted = subtotal * (Decimal("1") - Decimal(str(discount_rate)))
    taxed = discounted * (Decimal("1") + Decimal(str(tax_rate)))
    return taxed.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
