# Repair Notes

Need Package: failing pytest path, CI log, local AGENTS rules, and billing module contract.
Root cause: currency strings with commas were not normalized before Decimal conversion.
Fast inner loop: ran the targeted invoice math behavior before broader checks.
CI: the fixture CI log points to pytest failures in test_billing.py.
Pytest: the repaired normalize_amount and invoice_total paths satisfy currency parsing, discount_rate, and tax_rate behavior.
Lockfile: requirements.lock is intentionally unchanged to avoid dependency noise.
