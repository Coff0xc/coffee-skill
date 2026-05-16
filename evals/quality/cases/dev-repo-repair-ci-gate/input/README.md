# Billing Fixture

Small Python billing helper used by the quality eval.

Fast inner loop:

```powershell
python -m pytest test/test_billing.py
```

Release gate:

```powershell
python -m pytest
```

The expected invoice formula is:

```text
subtotal = sum(quantity * unit_price)
discount = subtotal * discount_rate
tax = (subtotal - discount) * tax_rate
total = subtotal - discount + tax
```
