from decimal import Decimal

from src.billing import invoice_total, normalize_amount


def test_normalize_amount_accepts_currency_commas():
    assert normalize_amount("$1,200.50") == Decimal("1200.50")


def test_invoice_total_applies_discount_and_tax():
    rows = [
        {"quantity": "2", "unit_price": "$100.00"},
        {"quantity": "1", "unit_price": "$50.00"},
    ]

    assert invoice_total(rows, discount_rate=Decimal("0.10"), tax_rate=Decimal("0.08")) == Decimal("243.00")
