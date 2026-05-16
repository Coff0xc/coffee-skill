# Quality Eval Prompt: Dev Repo Repair CI Gate

Use `coff0xc-software-engineering` to repair this small Python repository.

Goal: make the failing CI tests pass with the smallest correct code change.

Required behavior:
- Read `AGENTS.md`, `README.md`, `ci.log`, source, tests, and the lockfile before editing.
- Create a short Need Package.
- Identify and use the fast inner loop command from the README.
- Fix the root cause in `src/billing.py`.
- Do not add dependencies.
- Do not modify `requirements.lock` unless a dependency actually changes.
- Do not rewrite tests to match broken behavior.
- Save evidence in `repair-notes.md`: root cause, commands to run, validation result, and remaining risk.

Expected output directory shape:

```text
responses/dev-repo-repair-ci-gate/
├── src/
│   └── billing.py
├── requirements.lock      # optional; if present it must be unchanged
└── repair-notes.md
```
