# coffee-skill हिन्दी संदर्भ

## यह क्या है

`coffee-skill` Codex के लिए एक skill pack है। यह software engineering, AI Agent/RAG, API और data, UI और documents, defensive security, detection, incident response, और vulnerability management को कवर करता है।

## यह क्यों बनाया गया

- बहुत सारी छोटी skills automatic triggering को unreliable बना देती हैं।
- कई clients `SKILL.md` के frontmatter `name` और `description` से skill चुनते हैं।
- Security workflows में authorization और defensive-use boundaries साफ होनी चाहिए।
- Real work में generic advice से ज्यादा verifiable steps चाहिए।

## यह अच्छा क्यों है

- 87 source skills और research draw.io workflow को 16 comprehensive capability skills में consolidate करता है।
- Specific skill trigger न हो तो `coff0xc-skill-router` fallback देता है।
- हर skill में scope, exclusions, capability matrix, workflow phases, evidence levels, hard gates, validation checks, और anti-patterns हैं।
- Security content authorized defense, detection, hardening, verification, और reporting पर केंद्रित है।

## कैसे उपयोग करें

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to review Kubernetes and CI/CD risk.
```

अगर automatic trigger miss हो:

```text
Use coff0xc-skill-router to choose the right skill.
```

## कहां उपयोग करें

- Local Codex skill directories।
- `SKILL.md` folders load करने वाले compatible clients।
- Engineering, AI systems, documentation, defensive security, detection, और vulnerability management।

## Trigger fail होने पर

1. Folder name और frontmatter `name` match करें।
2. Copy के बाद Codex restart या refresh करें।
3. Duplicate skill names हटाएं।
4. `coff0xc-skill-router` को explicitly invoke करें।

## Safety boundary

इसे केवल अपने या explicitly authorized assets, code, logs, samples, labs, और training environments पर उपयोग करें। Unauthorized access, credential theft, persistence, evasion, C2, phishing collection, data exfiltration, या destructive actions के लिए उपयोग न करें।
