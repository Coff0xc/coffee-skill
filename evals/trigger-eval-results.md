# Trigger Evaluation Report

This report is generated from `evals/trigger-eval.json` by `scripts/run_trigger_eval.py`.

Important: this is a local proxy evaluation based on `SKILL.md` frontmatter metadata. It does not claim to reproduce the private skill-selection behavior of every Codex client.

## Summary

- Cases: 128
- Skills: 18
- Threshold: 3.0
- Positive top-1 rate: 0.9646
- Positive top-3 rate: 1.0
- Positive triggered rate: 1.0
- Router top-1 rate: 0.7895
- Router top-3 rate: 1.0
- Composition full top-N rate: 1.0
- Negative no-trigger rate: 1.0
- Negative false-positive rate: 0.0

## By Skill

| Skill | Total | Top-1 | Top-3 | Triggered |
|---|---:|---:|---:|---:|
| `coff0xc-ai-agent-rag` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-api-data-platform` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-authorized-assessment` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-binary-mobile-iot` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-blockchain-security` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-cloud-devsecops` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-compliance-architecture` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-detection-response` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-identity-zero-trust` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-network-protocol-security` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-office-doc-tools` | 8 | 1.0 | 1.0 | 1.0 |
| `coff0xc-purple-deception` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-research-drawio-diagram` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-secure-code-appsec` | 5 | 1.0 | 1.0 | 1.0 |
| `coff0xc-skill-router` | 19 | 0.7895 | 1.0 | 1.0 |
| `coff0xc-software-engineering` | 9 | 1.0 | 1.0 | 1.0 |
| `coff0xc-ui-doc-output` | 7 | 1.0 | 1.0 | 1.0 |
| `coff0xc-vulnerability-lifecycle` | 5 | 1.0 | 1.0 | 1.0 |

## Failures

No failed cases.
