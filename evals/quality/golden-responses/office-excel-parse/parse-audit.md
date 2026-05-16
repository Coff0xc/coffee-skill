# Parse Audit

Encoding: UTF-8 fixture read.
Delimiter: comma CSV with quoted currency values.
Headers: invoice_id, region, invoice_date, amount, exception_type, review_hours, status.
Units: amount is USD and review_hours is hours.
Date parsing: ISO, US slash, and yyyy/mm/dd formats normalized; "not available" becomes a null date.
Number parsing: dollar signs and comma thousands separators normalized.
Null handling: blank amount and blank review_hours are preserved and flagged.
Duplicate rows: invoice INV-1003 appears twice.
Abnormal values: negative amount -45.00 is flagged.
Sheet/range inspection: Raw A1:G8 feeds Model A1:K8 and Dashboard A1:D10.
