# Usage Guide

## Basic Flow

1. Install the `skills/` folders into your Codex skill directory.
2. Restart or refresh Codex so it re-indexes skill metadata.
3. Ask naturally in Chinese or English, or explicitly name a skill.
4. For narrow tasks, let the most specific skill execute directly; do not route first.
5. If you are unsure or the task spans multiple domains, invoke `coff0xc-skill-router` for a lightweight workflow and then execute the first phase.
6. For security tasks, confirm authorization before active testing or remote actions.

## Default Fast Path

For everyday work, the expected behavior is:

1. Pick the most specific skill.
2. Read the skill's `Quick Rules (read this first for everyday tasks)` block first.
3. Read the minimum necessary project context.
4. Make the smallest correct change or analysis.
5. Run the relevant project validation.
6. Report completed work, real validation, residual risk, and next step.

Do not create quality evals, golden responses, workflow traces, or long skill graphs for normal tasks. Those are repository release tools, not runtime ceremony.

Every main `SKILL.md` keeps a short `Default output` section so fast-path runs still return completed work, validation evidence, remaining risk, and next step without loading the expanded workflow.

Do not load `references/` by default. `references/full-workflow.md` is the expanded workflow for deep, multi-stage, formal-review, or release/eval work. For ordinary tasks, use the main skill body and the target project's own validation.

Complex work has one exception: L2/L3 multi-file, multi-stage, architecture/API/schema/auth, multi-skill, or multi-worker work can load `skills/coff0xc-skill-router/references/complex-workflow.md`. Thesis/report DOCX plus old PPTX defense-deck rewrites can load `skills/coff0xc-office-doc-tools/references/pptx-defense-rewrite.md`. These references are not required for small edits.

## When To Run Evals

Run the local eval commands only when you are maintaining this skill repository or the user explicitly asks for review, eval, quality testing, release, push, CI, benchmark, or proof that the skills still work.

```powershell
python .\scripts\validate_release.py
python .\scripts\run_trigger_eval.py
python .\scripts\run_quality_eval.py
```

## How To Choose Or Compose Skills

Use this pack by matching your task to the outcome you want, not by memorizing every source skill. For narrow tasks, name one skill directly or describe the task naturally. For broad work, ask the router to choose and chain only the needed skills.

For a compact card-style index, see [Skill Index](SKILL_INDEX.md).
For a full local environment map across installed Codex/agent/plugin skills, see [Installed Skill Inventory](SKILL_INVENTORY.md). That file is metadata-only and is meant for consolidation and deduping, not runtime publication.

| If you want... | Use this skill | Expected capability |
|---|---|---|
| Use coff0xc-software-engineering to fix this repo's failing tests and report the validation results. | `coff0xc-software-engineering` | Code patches, script or configuration changes; failure cause and root-cause chain; fast inner loop, CI reproduction, and diff hygiene |
| Use coff0xc-ai-agent-rag to design an enterprise knowledge-base assistant with citations, caching, and failure fallbacks. | `coff0xc-ai-agent-rag` | Agent/RAG architecture plans and data flows; tool schemas, memory/caching strategy, retrieval and citation strategy |
| Use coff0xc-api-data-platform to design this billing REST API, including OpenAPI, pagination, and error codes. | `coff0xc-api-data-platform` | REST/GraphQL/OpenAPI contracts; database schemas, migrations, and data-consistency advice |
| Use coff0xc-ui-doc-output to polish this dashboard and check mobile with screenshots. | `coff0xc-ui-doc-output` | Usable UI/component/page changes or design advice; design systems, state gates, accessibility, and browser screenshot acceptance |
| Use coff0xc-office-doc-tools to generate an editable PPTX and check its preview, charts, and exported file. | `coff0xc-office-doc-tools` | Editable PPTX/DOCX/PDF/XLSX files; render/preview QA, formula checks, and delivery paths |
| Use coff0xc-research-drawio-diagram to draw an editable draw.io method diagram from the paper and official GitHub. | `coff0xc-research-drawio-diagram` | Editable `.drawio` files; diagram-structure JSON/spec or module lists |
| Use coff0xc-secure-code-appsec to audit this Web/API project for authentication and authorization-bypass risks. | `coff0xc-secure-code-appsec` | Security finding lists: location, impact, evidence, reproduction conditions; source/sink or permission-chain explanations |
| Use coff0xc-cloud-devsecops to check Docker, K8s, CI/CD, and supply-chain risks. | `coff0xc-cloud-devsecops` | Cloud/IaC/K8s/CI/CD risk lists; least-privilege, network-isolation, pipeline-gate, and secrets-rotation advice |
| Use coff0xc-detection-response to write Sigma and YARA detection rules from these EDR logs. | `coff0xc-detection-response` | Sigma/YARA/query-rule drafts and field mappings; IOCs, timelines, attack stages, and ATT&CK mappings |
| Use coff0xc-vulnerability-lifecycle to analyze this CVE's impact, patch, and remediation priority. | `coff0xc-vulnerability-lifecycle` | Vulnerability-mechanism and patch-diff summaries; affected scope, CVSS/EPSS/KEV, and business priority |
| Use coff0xc-identity-zero-trust to assess this AD domain's Kerberos, BloodHound paths, and service-account risks. | `coff0xc-identity-zero-trust` | Identity/permission risk lists and path explanations; MFA/SSO/session/device-posture assessments |
| Use coff0xc-authorized-assessment to plan a security assessment within the written authorization. | `coff0xc-authorized-assessment` | Authorization-scope and ROE drafts; attack-surface lists, test phases, and prohibited actions |
| Use coff0xc-binary-mobile-iot to analyze this APK's permissions, network traffic, and Frida hook points. | `coff0xc-binary-mobile-iot` | Sample/firmware structure and entry-point analysis; string, configuration, permission, communication, and hardware-interface clues |
| Use coff0xc-blockchain-security to audit this Solidity contract's permissions, asset flows, and price sources. | `coff0xc-blockchain-security` | Contract entry-point and permission-model lists; asset flows, state machines, price sources, and external-call risks |
| Use coff0xc-compliance-architecture for a pre-launch security architecture review and threat modeling. | `coff0xc-compliance-architecture` | Architecture risk reviews and trust-boundary diagrams; STRIDE/threat modeling, control matrices, and gap analysis |
| Use coff0xc-purple-deception to map these attack behaviors into an ATT&CK detection-coverage matrix. | `coff0xc-purple-deception` | ATT&CK technique mappings and exercise hypotheses; detection-coverage matrices, log requirements, and response validation points |
| Use coff0xc-network-protocol-security to analyze the TLS handshake and anomalous fields in this pcap. | `coff0xc-network-protocol-security` | Protocol flows, handshake, and state-machine explanations; pcap/log field analysis, anomalous fields, and security impact |
| Use coff0xc-skill-router to help me decide which skill this task needs. | `coff0xc-skill-router` | Recommended primary skill and necessary support skills; candidate boundaries and next steps |
| Decide which coff0xc skills are needed, chain them into a workflow, and complete this task. | `coff0xc-skill-router` | Lightweight primary/support skill graph, phase order, validation gates, re-routing conditions |

## Autonomous Composition Examples

```text
Decide which coff0xc skills are needed, chain them into a workflow, and complete this task.
This vibe coding task may involve frontend, backend, database, security, and docs — orchestrate the skills yourself.
Decide which coff0xc skills are needed, chain them into a workflow, and complete this task.
```

Typical compositions:

| Task | Likely composition | Why |
|---|---|---|
| SaaS feature / admin panel | `software-engineering` + `api-data-platform` + `ui-doc-output` + `secure-code-appsec` | Code owns implementation; API/data owns contracts; UI owns states/screenshots; AppSec owns auth/input review. |
| Agent/RAG product | `ai-agent-rag` + `api-data-platform` + `software-engineering` + `ui-doc-output` | Agent owns system design; API/data owns storage and contracts; dev/UI make it usable. |
| Executive deliverable from repo/data | `office-doc-tools` + `ui-doc-output` + `api-data-platform` + `research-drawio-diagram` | Office owns files; UI owns narrative clarity; data owns evidence; draw.io owns diagrams. |
| Secure release | `secure-code-appsec` + `cloud-devsecops` + `software-engineering` + `compliance-architecture` | AppSec/cloud find risks; dev fixes; compliance turns evidence into release material. |

## Recommended Manual Invocations

```text
Use coff0xc-software-engineering to fix this repo's failing tests and report the validation results.
Use coff0xc-software-engineering to reproduce this CI failure: read the repo rules first, make the minimal fix, run the fast inner loop and the final audit, and stage only the related files.
Use coff0xc-ai-agent-rag to design an enterprise knowledge-base assistant with citations, caching, and failure fallbacks.
Use coff0xc-api-data-platform to design this billing REST API, including OpenAPI, pagination, and error codes.
Use coff0xc-ui-doc-output to polish this dashboard and check mobile with screenshots.
Use coff0xc-ui-doc-output to redo this SaaS admin page: start with product-type routing, a design-system check, empty/loading/error states, accessibility, and anti-AI-look visual acceptance.
Use coff0xc-office-doc-tools to generate an editable PPTX and check its preview, charts, and exported file.
Use coff0xc-research-drawio-diagram to draw an editable draw.io method diagram from the paper and official GitHub.
Use coff0xc-secure-code-appsec to audit this Web/API project for authentication and authorization-bypass risks.
Use coff0xc-cloud-devsecops to check Docker, K8s, CI/CD, and supply-chain risks.
Use coff0xc-detection-response to write Sigma and YARA detection rules from these EDR logs.
Use coff0xc-vulnerability-lifecycle to analyze this CVE's impact, patch, and remediation priority.
Use coff0xc-identity-zero-trust to assess this AD domain's Kerberos, BloodHound paths, and service-account risks.
Use coff0xc-authorized-assessment to plan a security assessment within the written authorization.
Use coff0xc-binary-mobile-iot to analyze this APK's permissions, network traffic, and Frida hook points.
Use coff0xc-blockchain-security to audit this Solidity contract's permissions, asset flows, and price sources.
Use coff0xc-compliance-architecture for a pre-launch security architecture review and threat modeling.
Use coff0xc-purple-deception to map these attack behaviors into an ATT&CK detection-coverage matrix.
Use coff0xc-network-protocol-security to analyze the TLS handshake and anomalous fields in this pcap.
Use coff0xc-skill-router to help me decide which skill this task needs.
Decide which coff0xc skills are needed, chain them into a workflow, and complete this task.
```

## What A Good Run Should Produce

A good Coff0xc skill run should leave the user with evidence, not just prose:

- a clear statement of the selected skill and scope,
- for cross-domain work, the primary skill, supporting skills, phase order, and re-routing conditions,
- the concrete artifact or analysis result,
- commands, files, sources, or evidence used,
- validation results or clear reasons validation could not run,
- remaining risk and the next useful action.

## Local Quality Evals

This section is for release/eval mode only. If the user asked for a normal project task, run that project's tests instead.

Use trigger evals to check routing metadata:

```powershell
python .\scripts\run_trigger_eval.py
```

Use quality evals to check whether UI/dev skills force concrete artifacts and reviewable evidence:

```powershell
python .\scripts\run_quality_eval.py
```

To score actual agent outputs, save them under `evals/quality/responses/<case-id>/` and run:

```powershell
python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses --allow-code-execution
```

## Safety And Trust

Security-scoped skills are defensive and authorization-scoped. They should transform risky requests into safe outputs: scope confirmation, evidence collection, hardening, detection, validation, and reporting. Production, credentials, paid services, deletion, push, PR actions, cloud writes, and CI/CD permission changes require explicit authorization.

## Install Notes

On Windows:

```powershell
.\scripts\install_local_skills.ps1
```

The installer backs up old installed `coff0xc-*` folders to `~\.codex\skills-backup-coff0xc-*` before copying the current repository version. Restart or refresh Codex after installing.

Avoid duplicate skill names across scanned directories. Duplicates can cause inconsistent triggering.
