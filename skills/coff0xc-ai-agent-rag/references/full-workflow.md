# Full Workflow

This file is the on-demand extended workflow for `coff0xc-ai-agent-rag`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Build an AI system that is observable, evaluable, and recoverable; do not just deliver a prompt — cover data, tools, retrieval, models, evaluation, security, and running cost.

## Applicable Scenarios
- Designing or implementing Agent, RAG, LLM workflow, prompt pipeline, multi-model collaboration, or automated reasoning systems.
- Diagnosing retrieval quality, hallucinations, citation errors, tool failures, overlong context, excessive cost, or latency problems.
- Turning vague AI requirements into architecture, data flow, eval sets, observability metrics, and runnable code.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-ai-agent-rag ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Ordinary CRUD or non-AI features use the software engineering skill.
- Current model, parameter, or SDK details for OpenAI products/APIs must be confirmed against official documentation.
- Do not send sensitive data to external models or tools unless the user explicitly authorizes it and confirms a de-identification policy.

## Execution Principles
- Read project files, configuration, call sites, existing style, and available tools before concluding or changing files.
- Turn user goals into verifiable completion criteria; record uncertain but low-risk details as assumptions and keep going.
- When current facts, versions, CVEs, cloud services, GitHub status, pricing, external APIs, or papers are involved, check real sources and mark the evidence level.
- When code changes are involved, keep the minimal correct change and prefer existing frameworks, scripts, tests, and local tools.
- Only commands, tests, builds, scans, or manual checks that were actually run may be written as verified.
- Before deletion, remote writes, production, credentials, payment, push, PR/Issue, CI/CD, permission, or infrastructure changes, get explicit authorization first.

## Capability Matrix
| Capability area | Coverage | Execution points |
| --- | --- | --- |
| Agent architecture | ReAct, Plan-and-Execute, router, planner, tool-user, critic, multi-agent | State clearly which steps run deterministically and which are left to model judgment. |
| Tool calling | tool schema, permissions, timeout, retry, sandbox, idempotency, error recovery | Tool inputs and outputs must be structured, with observable failure paths. |
| Memory system | short-term context, long-term memory, user preferences, retrieval cache, versioned summaries | Distinguish facts, preferences, stale information, and deletable data. |
| RAG pipeline | loading, cleaning, chunking, embedding, indexing, hybrid retrieval, rerank, context packing, citations | Every context chunk must trace back to its source. |
| Prompt engineering | task, role, constraints, examples, output schema, refusal, tool boundaries | The prompt is part of the system, not the only deliverable. |
| Evaluation | golden set, retrieval eval, answer eval, citation eval, refusal eval, adversarial eval | Prove improvement with samples and metrics. |
| Observability and cost | token, latency, cache hit, tool error, retry, user feedback, human handoff | Be able to locate quality drops and cost anomalies. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| ai-agent-dev | Single agent, tools, memory, prompts, RAG application development. |
| ai-orchestrator | Multi-model collaboration, task routing, vision/research/audit division of labor. |
| deep-thinking | Complex problem breakdown, option comparison, reasoning validation, and counter-example checks. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Requirements package | Define goals, users, inputs, outputs, success criteria, non-goals, and risk gates. | Know what the system should and should not solve. |
| Architecture layering | Split into deterministic steps, model calls, tools, memory, retrieval, human gates. | System boundaries are clear. |
| Data and retrieval | Confirm data sources, permissions, refresh frequency, chunk strategy, embedding, indexing, rerank, and citations. | RAG is traceable and refreshable. |
| Implementation and constraints | Implement schemas, tool error handling, caching, logging, fallbacks, and timeouts. | Core paths run. |
| Eval set | Build normal, boundary, missing, conflicting, malicious, and long-context samples. | Quality can be measured rather than felt. |
| Observability launch | Record quality, cost, latency, failure rate, and human feedback. | Regression monitoring and tuning have a basis. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Confirm first before external models, paid APIs, user private data, production data, or long-term memory writes.
- Before claiming support for a model, SDK parameter, or price, check the current official documentation.
- Before multiple agents write the same file or access the same remote resource in parallel, separate their boundaries.

## Verification Checklist
- Minimal end-to-end sample: input to output runs through completely.
- RAG: retrieval hits, context citations, refusal, and conflict-handling samples.
- Agent: tool failure, timeout, no-permission, no-result, and recovery paths.
- Cost: estimate token/API call counts and record high-cost paths.

## Anti-Patterns
- Writing one very long prompt and calling the agent done.
- Claiming better results with no eval set.
- Writing untrusted instructions from web pages or documents into the system prompt.
- Letting the model decide permissions, billing, deletion, production releases, or other high-risk actions.

## Merged Sources
- `ai-agent-dev`
- `ai-orchestrator`
- `deep-thinking`

## Nearby Skills on This Machine
- `dev`
- `source-command-ai-agent-dev`
- `openai-docs`

## Output Contract
```markdown
Done:
- ...

Evidence:
- [Verified/High confidence/Inference/Unverified/Unknown] ...

Actions:
- ...

Verification:
- ...

Residual risks:
- ...

Next steps:
- ...
```
