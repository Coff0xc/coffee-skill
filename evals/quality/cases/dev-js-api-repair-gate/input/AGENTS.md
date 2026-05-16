# Fixture Agent Rules

- Make the smallest behavior-preserving fix.
- Do not add packages for simple parsing or math.
- Keep `package-lock.json` unchanged unless `package.json` dependencies change.
- Record root cause, fast inner loop, and CI-equivalent validation in `repair-notes.md`.
