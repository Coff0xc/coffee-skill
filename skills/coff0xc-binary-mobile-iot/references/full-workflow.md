# Full Workflow

This file is the on-demand extended workflow for `coff0xc-binary-mobile-iot`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Analyze low-level system risk for authorized samples, labs, CTFs, or defensive-audit scenarios, and output evidence, fixes, detections, and security validation.

## Applicable Scenarios
- Analyzing binaries, firmware, mobile apps, kernel modules, industrial protocols, hardware interfaces, crypto implementations, or CTF challenges.
- Doing authorized reversing, vulnerability root-cause analysis, remediation recommendations, detection rules, test vectors, and security reports.
- Checking APK/IPA permissions, firmware configuration, protocol logs, dangerous functions, crypto misuse, and constant-time risk.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-binary-mobile-iot ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not provide exploit chains, detection bypass, jailbreak/root bypass, device takeover, or destructive ICS operation steps for real targets.
- Do not run active tests on production industrial-control, medical, transport, power, or other critical systems.
- Real mobile/IoT application analysis must confirm authorization and privacy boundaries.

## Execution Principles
- Read project files, configuration, call sites, existing style, and available tools before concluding or changing files.
- Turn user goals into verifiable completion criteria; record uncertain but low-risk details as assumptions and keep going.
- When current facts, versions, CVEs, cloud services, GitHub status, pricing, external APIs, or papers are involved, check real sources and mark the evidence level.
- When code changes are involved, keep the minimal correct change and prefer existing frameworks, scripts, tests, and local tools.
- Only commands, tests, builds, scans, or manual checks that were actually run may be written as verified.
- Before deletion, remote writes, production, credentials, payment, push, PR/Issue, CI/CD, permission, or infrastructure changes, get explicit authorization first.

## Security Boundaries
- Handle only owned assets, explicitly authorized assets, labs, CTFs, ranges, logs, configuration, samples, code audits, defensive work, and report writing.
- Do not provide exploitation, credential acquisition, persistence, detection evasion, C2, phishing collection, data exfiltration, destruction, or unauthorized-access steps against real third-party targets.
- High-risk requests default to defensive output: authorization boundaries, risk explanations, detection ideas, log queries, rule drafts, hardening plans, validation checklists, and report structure.
- Before active online scanning, cloud-account checks, directory/tenant queries, or production-environment actions, confirm target scope, rate, time window, prohibited actions, and rollback method.
- When keys, personal information, sensitive sample data, or customer data is found, report only the type, location, and handling recommendation; do not repeat the full secret value.

## Capability Matrix
| Capability area | Coverage | Execution points |
| --- | --- | --- |
| Binary/reversing | file formats, strings, imports, CFG, dangerous functions, symbols, decompilation | Locate behavior and risk points. |
| PWN/CTF | stack/heap/format-string/ROP ideas, range validation, writeups | CTF/lab only. |
| Kernel security | driver interfaces, ioctl, permission boundaries, memory safety, eBPF/io_uring/nftables risk | Defensive audit and fixes. |
| Mobile security | APK/IPA manifest, exported components, storage, networking, WebView, certificates, logs | No real bypass attacks. |
| IoT firmware | binwalk, filesystems, configuration, default-password risk, boot scripts, update signatures | Evidence-based firmware audit. |
| Hardware interfaces | UART/JTAG/SPI/SWD identification, debug exposure, protection recommendations | Do not guide unauthorized reads. |
| ICS/OT | protocols, PLC/HMI, network segmentation, security monitoring, IEC 62443/NIST 800-82 | Passive analysis first. |
| Cryptography | algorithm choice, modes, randomness, key management, authentication, constant time, test vectors | Validate with standards and tests. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| reverse-engineering | Static/dynamic reversing, disassembly, behavior understanding. |
| binary-exploit | CTF/lab binary vulnerability root causes and defensive fixes. |
| kernel-security | Kernel/driver/eBPF/ioctl and other low-level boundary audits. |
| mobile-security | Android/iOS application security review and privacy boundaries. |
| iot-security | Firmware, hardware interfaces, device cloud APIs, and update mechanisms. |
| ics-scada | Industrial protocols, PLC/HMI, OT networks, and security segmentation. |
| crypto-security | Crypto implementation, protocol, and key-management review. |
| ctf | Full-stack CTF challenge analysis and writeups. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Authorization and sample | Confirm sample source, target system, lab environment, prohibited actions, and confidentiality requirements. | Can be analyzed lawfully. |
| Static first | Identify format, metadata, strings, imports, configuration, permissions, symbols, and dangerous functions. | Evidence obtained at low risk. |
| Behavior inference | Infer behavior from code, configuration, logs, protocols, and test environments. | Hypotheses are verifiable. |
| Lab validation | Run minimal validation only in CTF/lab/owned devices; passive analysis for critical systems. | No harm to real systems. |
| Fix and detection | Output patch direction, configuration hardening, monitoring fields, test vectors, and regression cases. | Actionable. |
| Report | State sample, tools, hashes, environment, findings, evidence, limits, and next steps. | Reviewable. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Confirm authorization before connecting hardware interfaces, reading firmware, dynamic debugging, hooking, or running samples.
- For real ICS/OT environments, passive analysis only; active testing needs separate written authorization.
- Do not output attack scripts for bypassing payment, anti-debugging, certificate pinning, or root/jailbreak detection in real apps.

## Verification Checklist
- Sample hash, tool versions, analysis environment, and time recorded.
- Static findings have file path, function, offset, configuration item, or permission evidence.
- Crypto findings are backed by standards, test vectors, or constant-time analysis.
- Mobile/IoT fixes are backed by manifest/config/code diffs or retest results.

## Anti-Patterns
- Giving device/app attack steps without authorization.
- Reaching a final conclusion from strings alone.
- Running active probing on production ICS.
- Reviewing crypto by only saying AES/RSA is used, without looking at modes, randomness, and authentication.

## Merged Sources
- `binary-exploit`
- `crypto-security`
- `ctf`
- `ics-scada`
- `iot-security`
- `kernel-security`
- `mobile-security`
- `reverse-engineering`

## Nearby Skills on This Machine
- `source-command-binary-exploit`
- `source-command-iot-ics`
- `source-command-mobile-security`
- `constant-time-analysis`
- `wycheproof`

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
