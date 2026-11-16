# Full Workflow

This file is the on-demand extended workflow for `coff0xc-blockchain-security`. Do not load it by default; read it only for deep architecture, complex multi-stage work, quality evaluation, release, formal delivery, or when the current task needs the full gates.

## Goal
Audit contracts and protocols around asset flows, permissions, state machines, and chain specifics, proving risk first with chain-specific tools and tests.

## Applicable Scenarios
- Auditing smart contracts, DeFi protocols, on-chain asset flows, permissions, upgrades, oracles, bridges, and token integrations.
- Analyzing multi-chain projects, chain-specific risks, test coverage, formal/fuzz testing, and remediation recommendations.
- Doing audit preparation, entry-point enumeration, vulnerability validation, and reporting.

## Trigger Reinforcement
- Auto-triggering mainly depends on this file's frontmatter `description`; this skill keeps only core trigger words, tool names, common abbreviations, and manual trigger phrases to avoid overweight metadata.
- If there is no auto-trigger, write manually: `Use coff0xc-blockchain-security ...`.
- If the user only wrote a broad topic, first use `coff0xc-skill-router` to route to this skill.

## Not Applicable
- Do not guide real on-chain arbitrage, frontrunning, attacks, fund movement, or unauthorized transactions.
- Do not use real private keys, mainnet funds, or production contracts to run risky operations.
- On-chain events, contract state, prices, and vulnerability facts must be verified live.

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
| EVM/Solidity | reentrancy, access control, delegatecall, upgrades, signatures, MEV, oracle, flash loan | Foundry/Hardhat/Slither evidence. |
| Solana | PDA, account owner, signer, CPI, rent, sysvar, seeds | Account constraints and CPI boundaries. |
| Cosmos/CosmWasm | message handlers, IBC, capability, authz, bank module | State transitions and chain-halt risk. |
| Substrate | origin, weights, storage, runtime upgrade, pallet permissions | Consensus and chain-halt risk. |
| Cairo/StarkNet | felt, L1/L2 messaging, storage, account abstraction | Domain-specific boundaries. |
| TON/Algorand | messages, Jetton, rekeying, fee, field validation | Chain-model differences. |
| DeFi | AMM, lending, liquidation, oracle, governance, bridge, vault | Economic attacks and invariants. |
| Token/NFT | ERC20/721/1155, permit, fee-on-transfer, rebasing, blacklist, integration | Compatibility and asset safety. |

## Subdomain Routing
| Source skill | Handling after merge |
| --- | --- |
| blockchain-security | Overall control: identify chain, assets, entry points, tools, and test strategy. |
| chain-specific scanners | Prefer switching to installed Solana/Cosmos/Substrate/Cairo/TON/Algorand specialist skills. |
| token-integration | Token standards, compatibility, and external integration risk. |

## Workflow
| Stage | Action | Completion criterion |
| --- | --- | --- |
| Project profile | Confirm chain, language, framework, deployment status, assets, permissions, upgrades, and tests. | Audit scope is clear. |
| Entry-point enumeration | List public/external handlers, admin functions, cross-chain messages, keepers, hooks. | Entry points are complete. |
| Asset flow | Draw deposit/withdraw/swap/borrow/liquidate/bridge/governance state flows. | Key invariants are explicit. |
| Tool scanning | Run chain-matched tools and tests, keep raw output, and review manually. | Findings have evidence. |
| Manual audit | Check permissions, state, external calls, math, economic models, and chain specifics. | Deep risks covered. |
| Fix validation | Add PoC unit/invariant/fuzz tests and retest fixes. | Risk closed out. |

## Evidence Levels
- Verified: supported by local commands, tests, builds, source code, configuration, logs, official material, or reproducible data.
- High confidence: multiple reliable sources agree, but the current environment has no full reproduction.
- Inference: reasonable judgment based on verified facts, needs follow-up verification.
- Unverified: not yet confirmed, cannot be used as a final conclusion.
- Unknown: insufficient material, needs additional input or authorization.

## Hard Gates
- Mainnet transactions, private keys, fund operations, contract upgrades, and governance votes must be confirmed first and are usually not executed on the user's behalf.
- Economic-attack simulation only in forks/labs; do not guide real attacks for profit.
- External protocols, prices, and chain state must be checked against current sources.

## Verification Checklist
- Unit tests, fork tests, invariant/fuzz, static analysis, gas/weight checks.
- Every finding states preconditions, asset impact, reachable entry points, and fix tests.
- After fixes, run the originally failing cases and related regressions.

## Anti-Patterns
- Using Slither output alone as an audit report.
- Ignoring protocol economic invariants.
- Applying EVM experience directly to non-EVM chains.
- Not distinguishing owner/admin/keeper/user/attacker permissions.

## Merged Sources
- `blockchain-security`

## Nearby Skills on This Machine
- `solana-vulnerability-scanner`
- `cosmos-vulnerability-scanner`
- `substrate-vulnerability-scanner`
- `token-integration-analyzer`
- `secure-workflow-guide`

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
