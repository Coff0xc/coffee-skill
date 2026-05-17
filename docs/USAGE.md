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
2. Read the skill's `快速规则（日常任务先读这里）` block first.
3. Read the minimum necessary project context.
4. Make the smallest correct change or analysis.
5. Run the relevant project validation.
6. Report completed work, real validation, residual risk, and next step.

Do not create quality evals, golden responses, workflow traces, or long skill graphs for normal tasks. Those are repository release tools, not runtime ceremony.

Do not load `references/` by default. References are for deep review, external skill merging, router debugging, and release/eval work. For ordinary tasks, use the main skill body and the target project's own validation.

## When To Run Evals

Run the local eval commands only when you are maintaining this skill repository or the user explicitly asks for review, eval, quality testing, release, push, CI, benchmark, or proof that the skills still work.

```powershell
python .\scripts\validate_release.py
python .\scripts\run_trigger_eval.py
python .\scripts\run_quality_eval.py
```

## How To Choose Or Compose Skills

Use this pack by matching your task to the outcome you want, not by memorizing every source skill. For narrow tasks, name one skill directly or describe the task naturally. For broad work, ask the router to choose and chain only the needed skills.

| If you want... | Use this skill | Expected capability |
|---|---|---|
| 使用 coff0xc-software-engineering 修复这个 repo 的 failing tests，并说明验证结果。 | `coff0xc-software-engineering` | 代码补丁、脚本或配置修改; 失败原因和根因链路说明; 快速内循环、CI 复现和 diff 卫生 |
| 使用 coff0xc-ai-agent-rag 设计一个带引用、缓存和失败降级的企业知识库助手。 | `coff0xc-ai-agent-rag` | Agent/RAG 架构方案和数据流; 工具 schema、记忆/缓存策略、检索和引用策略 |
| 使用 coff0xc-api-data-platform 设计这个 billing REST API，包含 OpenAPI、分页和错误码。 | `coff0xc-api-data-platform` | REST/GraphQL/OpenAPI 契约; 数据库 schema、迁移和数据一致性建议 |
| 使用 coff0xc-ui-doc-output 优化这个 dashboard，并用截图检查移动端。 | `coff0xc-ui-doc-output` | 可用 UI/组件/页面改动或设计建议; 设计系统、状态门禁、可访问性和浏览器截图验收 |
| 使用 coff0xc-office-doc-tools 生成一份可编辑 PPTX，并检查预览、图表和导出文件。 | `coff0xc-office-doc-tools` | 可编辑 PPTX/DOCX/PDF/XLSX 文件; 渲染/预览 QA、公式检查和交付路径 |
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
| 使用 coff0xc-skill-router 帮我判断这个任务该用哪个 skill。 | `coff0xc-skill-router` | 推荐主 skill 和必要辅助 skill; 候选边界和下一步 |
| 你自己判断要用哪些 coff0xc skills，并把它们串成工作流完成这个功能。 | `coff0xc-skill-router` | 轻量主/辅 skill graph、阶段顺序、验证门禁、重路由条件 |

## Autonomous Composition Examples

```text
你自己判断要用哪些 coff0xc skills，并把它们串成工作流完成这个功能。
这个 vibe coding 任务可能涉及前后端、数据库、安全和文档，你来编排 skill。
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
使用 coff0xc-software-engineering 修复这个 repo 的 failing tests，并说明验证结果。
使用 coff0xc-software-engineering 复现这个 CI 失败，先读仓库规则，做最小修复，跑快速内循环和最终审计，只暂存相关文件。
使用 coff0xc-ai-agent-rag 设计一个带引用、缓存和失败降级的企业知识库助手。
使用 coff0xc-api-data-platform 设计这个 billing REST API，包含 OpenAPI、分页和错误码。
使用 coff0xc-ui-doc-output 优化这个 dashboard，并用截图检查移动端。
使用 coff0xc-ui-doc-output 重做这个 SaaS admin 页面，先做产品类型路由、设计系统检查、empty/loading/error 状态、可访问性和反 AI 味视觉验收。
使用 coff0xc-office-doc-tools 生成一份可编辑 PPTX，并检查预览、图表和导出文件。
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
你自己判断要用哪些 coff0xc skills，并把它们串成工作流完成这个功能。
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
python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses
```

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
