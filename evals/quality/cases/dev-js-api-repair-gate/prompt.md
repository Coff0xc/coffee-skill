# Quality Eval Prompt: JS API Repair Gate

Use `coff0xc-software-engineering` to repair this small JavaScript API helper repository.

Goal: make the failing usage-budget behavior pass with the smallest correct source change.

Required behavior:
- Read `AGENTS.md`, `README.md`, `ci.log`, `package-lock.json`, source, and tests before editing.
- Create a short Need Package.
- Fix the root cause in `src/usage.js`.
- Do not add dependencies.
- Do not modify `package-lock.json` unless a dependency actually changes.
- Do not rewrite tests to match broken behavior.
- Save evidence in `repair-notes.md`: root cause, fast inner loop, CI command, validation result, lockfile decision, and remaining risk.

Expected output directory shape:

```text
responses/dev-js-api-repair-gate/
├── src/
│   └── usage.js
├── package-lock.json      # optional; if present it must be unchanged
└── repair-notes.md
```
