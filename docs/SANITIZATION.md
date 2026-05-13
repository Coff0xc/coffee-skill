# Sanitization Notes

This release candidate was prepared to avoid publishing local machine details or secrets.

## Removed Or Excluded

- Intermediate extraction folders and original archives.
- Local planning/progress files from the working session.
- Generated optimization scripts that are not needed to use the skills.
- Extracted `CLAUDE_v19_draft.md`.

## Checked Patterns

The release validator checks for:

- the local Windows username marker used during preparation,
- the matching local Windows profile path marker,
- private key block markers,
- GitHub token patterns,
- OpenAI-style key patterns.

## Residual Sensitive Words

Security skills necessarily mention words such as `secret`, `token`, `password`, `credential`, and `key` in defensive contexts. These are not treated as secrets by themselves.

## Before Public Publishing

Review the repository manually for:

- license rights,
- attribution/provenance,
- company/private names,
- internal-only workflows,
- any content you do not want public.
