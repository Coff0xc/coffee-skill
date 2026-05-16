# Quality Eval Prompt: Multi-Skill Workflow Execution Gate

Use `coff0xc-skill-router` to compose and execute a recoverable multi-skill workflow for a billing anomaly that also has a security alert and customer-facing deliverables.

Goal: prove the agent did more than pick skills. It must leave a machine-readable execution trace that records phases, skills, inputs, artifacts, gates, re-routing, and final verification.

Required behavior:
- Start with `coff0xc-skill-router` and create a task-specific skill graph.
- Use support skills for software repair, API/data contract, AppSec/security regression, compliance evidence, UI review, and Office customer deliverables.
- Execute in phases and record each phase's inputs, produced artifacts, and gate status.
- Record at least one re-route when new evidence changes the skill graph.
- Save final verification commands and result.

Expected output directory shape:

```text
responses/composition-workflow-execution-gate/
├── workflow-trace.json
└── workflow-summary.md
```
