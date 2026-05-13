---
name: coff0xc-cloud-devsecops
description: "Use when / 当用户请求: 全面云安全、容器/Kubernetes、Serverless、DevSecOps、供应链、CI/CD 和密钥管理工作流。触发：AWS、Azure、GCP、IAM、S3/Blob/GCS、Docker、K8s、镜像、Serverless、CI/CD、SAST、DAST、SCA、SBOM、secret scanning、IaC、Terraform、GitHub Actions、发版流水线、集群配置、镜像权限、依赖来源、配置暴露、pipeline risk。 Covered source aliases / 来源别名: cloud-security, container-security, devsecops, docker-k8s, secrets-management, serverless-security, supply-chain-security. Capability domains / 能力域: 云配置, 容器镜像, Kubernetes, Serverless, CI/CD, 供应链, 密钥管理. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-cloud-devsecops."
---

# coff0xc-cloud-devsecops

## 目标
用只读优先、证据化的方式评估云原生和交付链风险，输出可落地加固方案和验证路线。

## 适用场景
- 审查云配置、IaC、容器镜像、K8s manifests、CI/CD workflow、依赖和密钥风险。
- 设计 DevSecOps pipeline、安全基线、SBOM、依赖扫描、secret scanning 和发布门禁。
- 分析云账号权限、日志、网络暴露、存储公开、serverless 权限和运行时风险。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-cloud-devsecops ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 不要默认连接或修改生产云账号。
- 不要输出发现的完整密钥值。
- 未授权目标的云枚举、接管、绕过、持久化请求转为防御建议。

## 执行原则
- 先读取项目文件、配置、调用点、现有风格和可用工具，再下结论或改文件。
- 把用户目标转成可验证的完成标准；不确定但低风险的细节记录为假设并继续推进。
- 涉及当前事实、版本、CVE、云服务、GitHub 状态、价格、外部 API 或论文时，查真实来源并标注证据等级。
- 涉及代码改动时保持最小正确改动，优先使用现有框架、脚本、测试和本地工具。
- 只有真实运行过的命令、测试、构建、扫描或人工检查才能写成已验证。
- 涉及删除、远程写入、生产、凭据、付费、push、PR/Issue、CI/CD、权限或基础设施变更时，先拿到明确授权。

## 安全边界
- 只处理自有资产、明确授权资产、实验室、CTF、靶场、日志、配置、样本、代码审计、防御建设和报告写作。
- 真实第三方目标上不提供漏洞利用、凭证获取、持久化、规避检测、C2、钓鱼收集、数据外传、破坏或未授权访问步骤。
- 高风险请求默认转为防御输出：授权边界、风险解释、检测思路、日志查询、规则草案、加固方案、验证清单和报告结构。
- 主动联网扫描、云账号检查、目录/租户查询或生产环境动作前，确认目标范围、速率、时间窗口、禁止动作和回滚方式。
- 发现密钥、个人信息、样本敏感数据或客户数据时，只报告类型、位置和处置建议，不复述完整秘密值。

## 能力矩阵
| 能力域 | 覆盖范围 | 执行要点 |
| --- | --- | --- |
| 云配置 | IAM、storage、network、security group、KMS、logging、backup、public exposure | 按 provider 和资产类型给证据。 |
| 容器镜像 | Dockerfile、base image、root、capabilities、secrets、SBOM、CVE | 区分构建时和运行时风险。 |
| Kubernetes | RBAC、namespace、Pod Security、NetworkPolicy、service account、admission、secrets | 最小权限和隔离优先。 |
| Serverless | function IAM、trigger、env、timeout、VPC、event source、dependency | 检查权限和事件边界。 |
| CI/CD | workflow permissions、OIDC、artifact、cache、pull_request、agent actions | 防止流水线被输入劫持。 |
| 供应链 | lockfile、SCA、license、maintainer risk、typosquat、dependency confusion、SBOM | 风险分级和可替代路径。 |
| 密钥管理 | 发现、范围、轮换、撤销、KMS/HSM、访问日志、least privilege | 只报位置和处理流程。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| cloud-security | AWS/Azure/GCP/IAM/存储/网络/日志/CSPM。 |
| container-security | Docker 镜像、运行时、K8s 安全。 |
| docker-k8s | 开发/部署容器配置和本地验证。 |
| serverless-security | 函数权限、事件触发和云日志。 |
| devsecops | CI/CD 安全门禁、SAST/DAST/SCA、发布流程。 |
| supply-chain-security | 依赖、恶意包、SBOM、锁文件和包源。 |
| secrets-management | 密钥发现、轮换、存储和访问审计。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 范围确认 | 确认云 provider、账号/项目、repo、IaC、集群、pipeline 和只读边界。 | 不误碰生产。 |
| 资产清单 | 读取 Terraform/CloudFormation/K8s/Dockerfile/workflow/lockfile/env example。 | 资产和入口完整。 |
| 风险检查 | 按身份、网络、数据、运行时、供应链、日志恢复分层审查。 | 发现有证据。 |
| 优先级 | 按公网暴露、权限级别、数据敏感性、可利用性和修复成本排序。 | 先改高价值风险。 |
| 修复方案 | 给最小权限、策略片段、配置修改、pipeline gate 和轮换计划。 | 可执行且可回滚。 |
| 验证 | 本地 lint/plan、只读命令、策略模拟、扫描报告和审计日志验证。 | 证明风险降低。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 任何云端写入、策略修改、密钥撤销、资源删除、pipeline 权限变更前必须确认。
- IaC apply、kubectl apply/delete、workflow dispatch 视为远程/生产风险。
- 第三方扫描器上传源码或 SBOM 前确认隐私和许可。

## 验证清单
- IaC：validate、fmt、plan、policy check。
- Container：build、trivy/grype、docker history、运行用户检查。
- K8s：manifest lint、RBAC can-i、namespace 隔离检查。
- CI/CD：workflow permission diff、触发条件和 secret 使用路径。

## 反模式
- 把 provider 最佳实践清单原样贴给用户，不看实际配置。
- 发现 secret 后复述完整值。
- 只修镜像 CVE，不处理 root、capability、secret 和 network。
- 在未确认下直接运行云端修改命令。

## 合并来源
- `cloud-security`
- `container-security`
- `devsecops`
- `docker-k8s`
- `secrets-management`
- `serverless-security`
- `supply-chain-security`

## 本机相近 Skill
- `supply-chain-risk-auditor`
- `insecure-defaults`
- `agentic-actions-auditor`
- `devcontainer-setup`

## 输出合同
```markdown
完成：
- ...

证据：
- [已验证/高可信/推断/未验证/未知] ...

行动：
- ...

验证：
- ...

剩余风险：
- ...

下一步：
- ...
```
