# coffee-skill English Reference

## What It Is

`coffee-skill` is a Codex skill pack for software engineering, AI Agent/RAG work, API and data design, UI and document output, defensive security, detection, incident response, and vulnerability management.

## Why It Exists

- Too many narrow skills make automatic triggering unreliable.
- Many clients select skills mainly from the `name` and `description` frontmatter in `SKILL.md`.
- Security workflows need clear authorization and defensive-use boundaries.
- Real work needs verifiable steps, not only generic advice.

## Why Use It

- It consolidates 87 source skills and adds a research draw.io workflow into 16 comprehensive capability skills.
- `coff0xc-skill-router` acts as a fallback when a specific skill does not auto-trigger.
- Each skill includes scope, exclusions, capability matrix, workflow phases, evidence levels, hard gates, validation checks, and anti-patterns.
- Security content stays focused on authorized defense, detection, hardening, verification, and reporting.

## How To Use

Ask naturally:

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to review Kubernetes and CI/CD risk.
```

If automatic triggering misses:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Where To Use

- Local Codex skill directories.
- Compatible clients that load `SKILL.md` folders.
- Engineering, AI systems, documentation, defensive security, detection, incident response, and vulnerability management.

## When Triggering Fails

1. Check that the folder name matches the frontmatter `name`.
2. Restart or refresh Codex after copying.
3. Remove duplicate skill names.
4. Explicitly invoke `coff0xc-skill-router`.

## Safety Boundary

Use only on assets, code, logs, samples, labs, and training environments that you own or are explicitly authorized to assess. Do not use it for unauthorized access, credential theft, persistence, evasion, C2, phishing collection, data exfiltration, or destructive actions.
