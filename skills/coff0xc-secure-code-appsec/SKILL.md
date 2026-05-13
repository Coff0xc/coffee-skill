---
name: coff0xc-secure-code-appsec
description: "Use when / 当用户请求: 全面代码安全审计、Web/API/GraphQL/OAuth/浏览器/SPA/LLM 安全、后门检测和授权应用安全验证工作流。触发：代码审计、危险函数、source/sink、污点分析、Web 安全、API 安全、GraphQL、OAuth、CSP、CORS、Cookie、Prompt 注入、越权、SSRF、XSS、SQLi、后门、Webshell、绕过登录、看到别人数据、代码入口、数据流、access control、authorization bypass。 Covered source aliases / 来源别名: api-discovery, api-security-test, backdoor-detector, browser-security, code-audit, graphql-pentest, llm-red-teaming, oauth-security, spa-pentest, web-pentest. Capability domains / 能力域: 入口梳理, Source/Sink, 认证授权, Web/API 漏洞, 浏览器/SPA, GraphQL, LLM/Agent 安全, 后门检测. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-secure-code-appsec."
---

# coff0xc-secure-code-appsec

## 目标
以代码和证据为中心定位应用安全问题，给出可验证修复；对高风险请求保持防御化和授权边界。

## 适用场景
- 审计代码、配置、路由、API、认证授权、浏览器安全、GraphQL、OAuth/OIDC、LLM/Agent 安全。
- 寻找漏洞根因、误报确认、修复建议、回归测试和安全报告。
- 分析授权测试证据、Burp 项目、日志、SARIF、扫描结果或源码泄露风险。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-secure-code-appsec ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 不要对未授权目标进行主动扫描、爆破、利用或绕过。
- 不要提供可直接攻击第三方的 payload、利用链、绕过脚本或数据外传步骤。
- 二进制、移动、IoT、云或身份专项转对应 skill。

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
| 入口梳理 | routes、controllers、GraphQL resolvers、webhooks、file upload、SPA routes | 列出用户可控输入。 |
| Source/Sink | 请求参数、headers、cookies、body、files、env、DB 到 command、SQL、template、file、URL、deserialize | 建立可达路径。 |
| 认证授权 | session、JWT、OAuth、OIDC、tenant、role、object ownership、CSRF | 区分未登录、低权、高权路径。 |
| Web/API 漏洞 | 注入、XSS、SSRF、XXE、path traversal、deserialization、IDOR、logic bug | 每项给可验证证据。 |
| 浏览器/SPA | CSP、CORS、postMessage、Cookie、storage、DOM sink、extension manifest | 检查前端信任边界。 |
| GraphQL | schema、resolver auth、batching、depth、introspection、IDOR、N+1 | 关注字段级权限。 |
| LLM/Agent 安全 | prompt injection、tool injection、data leakage、memory poisoning、agent CI/CD | 工具权限和数据边界优先。 |
| 后门检测 | 异常入口、混淆、动态执行、可疑网络、隐藏账号、异常计划任务 | 用代码/配置证据说明。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| code-audit | 代码级 source/sink、危险函数、污点分析和修复。 |
| web-pentest | 授权 Web 应用验证、OWASP Top 10 和业务逻辑。 |
| api-discovery | 接口枚举、路由/文档/客户端反推，不做未授权探测。 |
| api-security-test | API 鉴权、越权、参数校验、速率限制和错误泄露。 |
| graphql-pentest | GraphQL schema/resolver 权限和查询复杂度。 |
| oauth-security | OAuth/OIDC redirect、state、PKCE、scope、token 存储。 |
| browser-security | DOM/CSP/CORS/Cookie/postMessage/扩展安全。 |
| spa-pentest | 前端路由、token 暴露、source map、前后端权限错位。 |
| llm-red-teaming | LLM/Agent 防御验证、提示注入和工具边界。 |
| backdoor-detector | Webshell、异常动态执行、隐藏管理口和恶意代码特征。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 授权与范围 | 确认资产、代码、环境、测试方式、禁止动作和输出敏感度。 | 知道能做什么。 |
| 架构/入口 | 读取路由、schema、auth middleware、controllers、clients、config、tests。 | 攻击面和信任边界清晰。 |
| 数据流分析 | 从 source 到 sink 追踪校验、转义、权限和异常处理。 | 有候选发现和证据链。 |
| 验证优先级 | 按可达性、影响、权限、可利用复杂度和数据敏感度排序。 | 先验证高风险。 |
| 修复设计 | 给最小修复、测试用例、兼容影响和日志/监控建议。 | 能落地。 |
| 报告复查 | 每个发现包含位置、影响、证据、复现条件、修复、验证。 | 不夸大、不漏风险。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 主动扫描、认证绕过测试、文件上传测试、外部回连验证前必须确认授权和速率。
- 不输出真实秘密值、完整客户数据或可用于未授权攻击的 payload。
- 使用 Semgrep/CodeQL 等工具时记录规则、版本、目标和过滤标准。

## 验证清单
- 静态：文件/行号、调用链、source/sink、权限路径。
- 动态：仅在授权本地/测试环境中验证，记录请求条件和预期结果。
- 工具：Semgrep/CodeQL/SARIF 结果需去重和误报分析。
- 修复：加入回归测试，确认漏洞路径被阻断且正常路径保留。

## 反模式
- 只列工具扫描结果，不做可达性和误报判断。
- 把漏洞标题当证据。
- 用攻击视角替代修复和检测方案。
- 只修前端校验，不修服务端边界。

## 合并来源
- `api-discovery`
- `api-security-test`
- `backdoor-detector`
- `browser-security`
- `code-audit`
- `graphql-pentest`
- `llm-red-teaming`
- `oauth-security`
- `spa-pentest`
- `web-pentest`

## 本机相近 Skill
- `source-command-code-audit`
- `semgrep`
- `codeql`
- `variant-analysis`
- `burpsuite-project-parser`

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
