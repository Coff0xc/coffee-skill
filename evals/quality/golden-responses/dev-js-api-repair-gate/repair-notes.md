# JS API Repair Notes

Need Package: CI log, package scripts, API contract, lockfile, and failing usage budget tests.
Root cause: plan normalization and numeric unit handling were missing from the usage helper.
Fast inner loop: node-based behavior check for calculateRemainingBudget and shouldThrottle.
CI: npm test would run the usage tests after the local behavior check.
Lockfile: package-lock.json is unchanged because no dependency was needed.
Security: invalid plan and negative units now fail closed.
