# Usage Guide

## Basic Flow

1. Install the `skills/` folders into your Codex skill directory.
2. Restart or refresh Codex so it re-indexes skill metadata.
3. Ask naturally in Chinese or English, or explicitly name a skill.
4. If you are unsure, invoke `coff0xc-skill-router` first.
5. For security tasks, confirm authorization before active testing or remote actions.

## How To Choose A Skill

Use this pack by matching your task to the outcome you want, not by memorizing every source skill.

| If you want... | Use this skill | Expected capability |
|---|---|---|
| 使用 coff0xc-software-engineering 修复这个 repo 的 failing tests，并说明验证结果。 | `coff0xc-software-engineering` | 代码补丁、脚本或配置修改; 失败原因和根因链路说明 |
| 使用 coff0xc-ai-agent-rag 设计一个带引用、缓存和失败降级的企业知识库助手。 | `coff0xc-ai-agent-rag` | Agent/RAG 架构方案和数据流; 工具 schema、记忆/缓存策略、检索和引用策略 |
| 使用 coff0xc-api-data-platform 设计这个 billing REST API，包含 OpenAPI、分页和错误码。 | `coff0xc-api-data-platform` | REST/GraphQL/OpenAPI 契约; 数据库 schema、迁移和数据一致性建议 |
| 使用 coff0xc-ui-doc-output 优化这个 dashboard，并用截图检查移动端。 | `coff0xc-ui-doc-output` | 可用 UI/组件/页面改动或设计建议; 桌面/移动端截图或浏览器 smoke 结果 |
| 使用 coff0xc-research-drawio-diagram 根据论文和官方 GitHub 画一个可编辑 draw.io 方法图。 | `coff0xc-research-drawio-diagram` | 可编辑 `.drawio` 文件; 图结构 JSON/spec 或模块清单 |
| 使用 coff0xc-secure-code-appsec 审计这个 Web/API 项目的认证和越权风险。 | `coff0xc-secure-code-appsec` | 安全发现列表：位置、影响、证据、复现条件; source/sink 或权限链路说明 |
| 使用 coff0xc-cloud-devsecops 检查 Docker、K8s、CI/CD 和供应链风险。 | `coff0xc-cloud-devsecops` | 云/IaC/K8s/CI/CD 风险清单; 最小权限、网络隔离、pipeline gate 和密钥轮换建议 |
| 使用 coff0xc-detection-response 根据这些 EDR 日志写 Sigma 和 YARA 检测规则。 | `coff0xc-detection-response` | Sigma/YARA/查询规则草案和字段映射; IOC、时间线、攻击阶段和 ATT&CK 映射 |
| 使用 coff0xc-vulnerability-lifecycle 分析这个 CVE 的影响、补丁和修复优先级。 | `coff0xc-vulnerability-lifecycle` | 漏洞原理和补丁差异摘要; 受影响范围、CVSS/EPSS/KEV 和业务优先级 |
| 使用 coff0xc-identity-zero-trust 评估这个 AD 域的 Kerberos、BloodHound 路径和服务账号风险。 | `coff0xc-identity-zero-trust` | 身份/权限风险清单和路径说明; MFA/SSO/session/device posture 评估 |
| 使用 coff0xc-authorized-assessment 在书面授权范围内规划一次安全评估。 | `coff0xc-authorized-assessment` | 授权范围和 ROE 草案; 攻击面清单、测试阶段和禁止动作 |
| 使用 coff0xc-binary-mobile-iot 分析这个 APK 的权限、网络通信和 Frida hook 点。 | `coff0xc-binary-mobile-iot` | 样本/固件结构和入口点分析; 字符串、配置、权限、通信和硬件接口线索 |
| 使用 coff0xc-blockchain-security 审计这个 Solidity 合约的权限、资产流和价格来源。 | `coff0xc-blockchain-security` | 合约入口点和权限模型清单; 资产流、状态机、价格来源和外部调用风险 |
| 使用 coff0xc-compliance-architecture 做上线前安全架构评审和威胁建模。 | `coff0xc-compliance-architecture` | 架构风险评审和信任边界图; STRIDE/威胁建模、控制矩阵和差距分析 |
| 使用 coff0xc-purple-deception 把这些攻击行为映射成 ATT&CK 检测覆盖矩阵。 | `coff0xc-purple-deception` | ATT&CK 技术映射和演练假设; 检测覆盖矩阵、日志需求和响应验证点 |
| 使用 coff0xc-network-protocol-security 分析这个 pcap 里的 TLS 握手和异常字段。 | `coff0xc-network-protocol-security` | 协议流程、握手和状态机说明; pcap/日志字段分析、异常字段和安全影响 |
| 使用 coff0xc-skill-router 帮我判断这个任务该用哪个 skill。 | `coff0xc-skill-router` | 推荐 skill 和理由; 候选 skill 对比和适用边界 |

## Recommended Manual Invocations

```text
使用 coff0xc-software-engineering 修复这个 repo 的 failing tests，并说明验证结果。
使用 coff0xc-ai-agent-rag 设计一个带引用、缓存和失败降级的企业知识库助手。
使用 coff0xc-api-data-platform 设计这个 billing REST API，包含 OpenAPI、分页和错误码。
使用 coff0xc-ui-doc-output 优化这个 dashboard，并用截图检查移动端。
使用 coff0xc-research-drawio-diagram 根据论文和官方 GitHub 画一个可编辑 draw.io 方法图。
使用 coff0xc-secure-code-appsec 审计这个 Web/API 项目的认证和越权风险。
使用 coff0xc-cloud-devsecops 检查 Docker、K8s、CI/CD 和供应链风险。
使用 coff0xc-detection-response 根据这些 EDR 日志写 Sigma 和 YARA 检测规则。
使用 coff0xc-vulnerability-lifecycle 分析这个 CVE 的影响、补丁和修复优先级。
使用 coff0xc-identity-zero-trust 评估这个 AD 域的 Kerberos、BloodHound 路径和服务账号风险。
使用 coff0xc-authorized-assessment 在书面授权范围内规划一次安全评估。
使用 coff0xc-binary-mobile-iot 分析这个 APK 的权限、网络通信和 Frida hook 点。
使用 coff0xc-blockchain-security 审计这个 Solidity 合约的权限、资产流和价格来源。
使用 coff0xc-compliance-architecture 做上线前安全架构评审和威胁建模。
使用 coff0xc-purple-deception 把这些攻击行为映射成 ATT&CK 检测覆盖矩阵。
使用 coff0xc-network-protocol-security 分析这个 pcap 里的 TLS 握手和异常字段。
使用 coff0xc-skill-router 帮我判断这个任务该用哪个 skill。
```

## What A Good Run Should Produce

A good Coff0xc skill run should leave the user with evidence, not just prose:

- a clear statement of the selected skill and scope,
- the concrete artifact or analysis result,
- commands, files, sources, or evidence used,
- validation results or clear reasons validation could not run,
- remaining risk and the next useful action.

## Safety And Trust

Security-scoped skills are defensive and authorization-scoped. They should transform risky requests into safe outputs: scope confirmation, evidence collection, hardening, detection, validation, and reporting. Production, credentials, paid services, deletion, push, PR actions, cloud writes, and CI/CD permission changes require explicit authorization.

## Install Notes

On Windows:

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force $dest
Copy-Item -Recurse .\skills\* $dest
```

Avoid duplicate skill names across scanned directories. Duplicates can cause inconsistent triggering.
