# Triggering Guide

## Why Skills Sometimes Do Not Auto-Trigger

Most clients select skills from frontmatter metadata, especially `name` and `description`. The body of `SKILL.md` is usually loaded only after the skill has already triggered, so trigger words must be in `description`.

## Trigger Strategy In This Pack

- Each capability skill starts its description with `Use when / 当用户请求`.
- Descriptions include Chinese, English, tool names, acronyms, and source aliases.
- Each capability skill contains a manual invocation phrase.
- `coff0xc-skill-router` is a broad fallback that routes ambiguous requests.

## Manual Invocation

Use one of these phrases when auto-triggering misses:

| Skill | Manual phrase | Source aliases |
|---|---|---|
| `coff0xc-software-engineering` | `使用 coff0xc-software-engineering ...` | `dev`, `c-cpp-dev`, `code-simplifier`, `git-workflow`, `go-dev`, `java-dev`, `js-ts-dev`, `python-dev`, `rust-dev`, `shell-scripting`, `testing` |
| `coff0xc-ai-agent-rag` | `使用 coff0xc-ai-agent-rag ...` | `ai-agent-dev`, `ai-orchestrator`, `deep-thinking` |
| `coff0xc-api-data-platform` | `使用 coff0xc-api-data-platform ...` | `api-design`, `database`, `cli-creator` |
| `coff0xc-ui-doc-output` | `使用 coff0xc-ui-doc-output ...` | `UIdesign`, `pdf`, `quick-translate` |
| `coff0xc-research-drawio-diagram` | `使用 coff0xc-research-drawio-diagram ...` | `draw.io`, `diagrams.net`, `.drawio`, `paper figure`, `research diagram` |
| `coff0xc-secure-code-appsec` | `使用 coff0xc-secure-code-appsec ...` | `api-discovery`, `api-security-test`, `backdoor-detector`, `browser-security`, `code-audit`, `graphql-pentest`, `llm-red-teaming`, `oauth-security`, `spa-pentest`, `web-pentest` |
| `coff0xc-cloud-devsecops` | `使用 coff0xc-cloud-devsecops ...` | `cloud-security`, `container-security`, `devsecops`, `docker-k8s`, `secrets-management`, `serverless-security`, `supply-chain-security` |
| `coff0xc-detection-response` | `使用 coff0xc-detection-response ...` | `detection-engineering`, `email-security`, `forensics-analysis`, `incident-response`, `malware-analysis`, `osint`, `soc-operations`, `threat-hunting`, `threat-intelligence` |
| `coff0xc-vulnerability-lifecycle` | `使用 coff0xc-vulnerability-lifecycle ...` | `bug-bounty`, `pentest-report`, `red-team-poc`, `vuln-research`, `vulnerability-management` |
| `coff0xc-identity-zero-trust` | `使用 coff0xc-identity-zero-trust ...` | `ad-pentest`, `credential-access`, `identity-security`, `lateral-movement`, `privilege-escalation`, `zero-trust` |
| `coff0xc-authorized-assessment` | `使用 coff0xc-authorized-assessment ...` | `attack-chain-orchestrator`, `autoredteam-orchestrator`, `c2-framework`, `cdn-bypass`, `data-exfiltration`, `evasion-toolkit`, `fingerprint-engine`, `full-pentest`, `phishing-simulation`, `post-exploitation`, `proxy-pool-manager`, `recon-workflow`, `red-team-infra`, `security-tool-dev`, `social-engineering` |
| `coff0xc-binary-mobile-iot` | `使用 coff0xc-binary-mobile-iot ...` | `binary-exploit`, `crypto-security`, `ctf`, `ics-scada`, `iot-security`, `kernel-security`, `mobile-security`, `reverse-engineering` |
| `coff0xc-blockchain-security` | `使用 coff0xc-blockchain-security ...` | `blockchain-security` |
| `coff0xc-compliance-architecture` | `使用 coff0xc-compliance-architecture ...` | `compliance-audit`, `data-security`, `security-architecture` |
| `coff0xc-purple-deception` | `使用 coff0xc-purple-deception ...` | `honeypot`, `purple-team` |
| `coff0xc-network-protocol-security` | `使用 coff0xc-network-protocol-security ...` | `network-protocol`, `wireless-security` |
| `coff0xc-skill-router` | `使用 coff0xc-skill-router ...` | `router` |

## Troubleshooting

1. Ensure the folder name equals the frontmatter `name`.
2. Restart or refresh the client after copying skills.
3. Remove duplicate skill names across `.codex/skills`, `.agents/skills`, or other scanned locations.
4. Keep trigger terms in frontmatter `description`, not only in the Markdown body.
5. Use `coff0xc-skill-router` when unsure which skill should handle a request.
