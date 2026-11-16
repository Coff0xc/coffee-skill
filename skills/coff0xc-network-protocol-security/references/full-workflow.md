# Full Workflow

This file is the on-demand extended workflow for `coff0xc-network-protocol-security`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Analyze security properties, state machines, authentication, encryption, and configuration risks in communication protocols and network telemetry, for authorized and defensive scenarios by default.

## Applicable Scenarios
- Analyzing protocol design, packet captures, logs, TLS/DNS/HTTP/QUIC configuration, wireless/BLE/RF compliance testing, and communication security.
- Turning protocol descriptions into sequence diagrams, state machines, threat models, or formal-verification inputs.
- Diagnosing connection failures, certificate errors, downgrade risk, replay risk, and network detection rules.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-network-protocol-security ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not provide unauthorized wireless attacks, jamming, bypass, credential capture, or third-party network intrusion steps.
- Do not run active scanning, load testing, or changes against production networks without confirmed authorization.
- Do not treat an encryption algorithm name as a security conclusion; configuration and protocol context must be examined.

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
| Protocol design | message flows, state machines, authentication, key agreement, replay, downgrade, error handling | Can be drawn and verified. |
| TLS/PKI | certificate chains, SAN, expiry, cipher, mTLS, OCSP, pinning, HSTS | Configuration has evidence. |
| DNS | resolution chain, DNSSEC, DoH/DoT, caching, split horizon, zone transfer risk | Logs and configuration together. |
| HTTP/QUIC | headers, cookies, CORS, cache, HTTP/2/3, ALPN, proxy | Application-protocol boundaries. |
| Packet analysis | pcap, Wireshark, flow, latency, retransmission, anomalous sequences | Network facts are re-checkable. |
| Wireless/BLE/RF | bands, pairing, authentication, encryption, device exposure, compliance testing | Authorized labs first. |
| Formal methods | Mermaid sequence, ProVerif/Tamarin ideas, attacker models | Security properties are explicit. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| network-protocol | Wired/internet protocols, TLS/DNS/HTTP/QUIC/pcap analysis. |
| wireless-security | WiFi/BLE/RF compliance and defensive analysis. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Input confirmation | Confirm pcap, logs, configuration, protocol docs, devices, authorization, and time window. | Data is lawful and analyzable. |
| Protocol modeling | List participants, messages, states, keys, trust boundaries, and attacker capabilities. | Security properties are explicit. |
| Evidence analysis | Extract facts from packet captures, logs, configuration, certificates, and source code. | Not guessed from experience. |
| Risk judgment | Check authentication, encryption, integrity, replay, downgrade, privacy, and error handling. | Findings have context. |
| Fix and detection | Give configuration, protocol changes, log fields, rules, and retest methods. | Executable and verifiable. |
| Diagrams/report | Output sequence diagrams, state machines, evidence tables, and residual risk. | Easy to communicate. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Confirm authorization and legal boundaries before wireless testing, packet capture, active scanning, or connecting devices.
- Confirm first before production certificate, DNS, routing, WAF/proxy configuration changes.
- Formal conclusions must state the attacker model and unmodeled assumptions.

## Verification Checklist
- TLS: certificate chain, cipher, protocol version, handshake logs, or test commands.
- DNS: authoritative/recursive path, records, TTL, DNSSEC status.
- pcap: filter expressions, packet numbers, timestamps, and fields.
- Protocol model: security properties, participants, and counter-example/no-counter-example conditions.

## Anti-Patterns
- Reaching security conclusions from open ports alone.
- Packet-capture analysis with no time window or packet numbers.
- Applying lab wireless methods to real third-party environments.
- Formal models that omit key participants yet give strong conclusions.

## Merged Sources
- `network-protocol`
- `wireless-security`

## Nearby Skills on This Machine
- `crypto-protocol-diagram`
- `mermaid-to-proverif`

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
