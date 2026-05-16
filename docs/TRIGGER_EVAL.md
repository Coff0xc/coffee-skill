# Trigger Evaluation

This repository includes a local trigger proxy evaluation for `coff0xc-skill-router` and the 17 capability skills.

## Purpose

Skill clients usually select a skill from frontmatter metadata, especially `name` and `description`. This eval checks whether the current metadata is likely to route realistic prompts to the intended skill.

It is designed to catch:

- missing trigger terms,
- ambiguous overlap between skills,
- router fallback gaps,
- false positives on simple or unrelated prompts,
- multilingual manual invocation coverage.

## Files

- `evals/trigger-eval.json`: should-trigger and should-not-trigger cases.
- `scripts/run_trigger_eval.py`: local scorer using actual `SKILL.md` frontmatter.
- `evals/trigger-eval-results.json`: generated detailed results.
- `evals/trigger-eval-results.md`: generated readable report.

## Run

```powershell
python .\scripts\run_trigger_eval.py
```

The script exits non-zero if any case fails. To inspect scores without changing files, run it and read the generated JSON/Markdown report.

## Metrics

- `positive_top1_rate`: expected skill is the top ranked skill.
- `positive_top3_rate`: expected skill appears in the top three ranked skills.
- `positive_triggered_rate`: at least one skill scored above threshold for should-trigger cases.
- `router_top1_rate`: router cases rank `coff0xc-skill-router` first.
- `router_top3_rate`: router cases include `coff0xc-skill-router` in top three.
- `negative_no_trigger_rate`: should-not-trigger cases stay below threshold.
- `negative_false_positive_rate`: should-not-trigger cases incorrectly trigger a skill.

## Limits

This is a deterministic local proxy. It does not reproduce the private trigger logic of every Codex client or model runtime. Treat failures as strong evidence of metadata gaps, and treat passes as a useful release guard rather than a guarantee.
