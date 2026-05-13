---
name: coff0xc-api-data-platform
description: "Use when / 当用户请求: 全面 API、数据库、数据平台、CLI、SDK 和接口契约工程工作流。触发：REST、GraphQL、OpenAPI、SQL、数据库、迁移、CLI、SDK、分页、认证、错误码、JSON 输出、数据模型、ETL、数据质量、后端接口、请求响应、鉴权、版本兼容、存储结构、外部客户接口。 Covered source aliases / 来源别名: api-design, database, cli-creator. Capability domains / 能力域: API 设计, 认证授权, 数据模型, 查询与分页, CLI/SDK, 数据平台, 兼容演进. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-api-data-platform."
---

# coff0xc-api-data-platform

## 目标
把接口、数据和命令行工具做成稳定契约：输入明确、输出可机器处理、错误可诊断、变更可兼容、数据可迁移。

## 适用场景
- 设计或实现 REST/GraphQL/OpenAPI、数据库 schema、迁移、数据访问层、CLI 或 SDK。
- 需要把网页/API 文档、curl、OpenAPI、SDK 或本地脚本变成可组合工具。
- 需要检查接口兼容性、分页、认证、错误模型、幂等性或数据一致性。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-api-data-platform ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- Web/API 安全漏洞审计转 `coff0xc-secure-code-appsec`。
- 生产数据库迁移、数据删除、远程写操作必须先确认。
- 不要在示例里写真实 token、cookie、账号或客户数据。

## 执行原则
- 先读取项目文件、配置、调用点、现有风格和可用工具，再下结论或改文件。
- 把用户目标转成可验证的完成标准；不确定但低风险的细节记录为假设并继续推进。
- 涉及当前事实、版本、CVE、云服务、GitHub 状态、价格、外部 API 或论文时，查真实来源并标注证据等级。
- 涉及代码改动时保持最小正确改动，优先使用现有框架、脚本、测试和本地工具。
- 只有真实运行过的命令、测试、构建、扫描或人工检查才能写成已验证。
- 涉及删除、远程写入、生产、凭据、付费、push、PR/Issue、CI/CD、权限或基础设施变更时，先拿到明确授权。

## 能力矩阵
| 能力域 | 覆盖范围 | 执行要点 |
| --- | --- | --- |
| API 设计 | REST 资源、GraphQL schema、OpenAPI、版本、错误模型 | 契约稳定且可生成客户端。 |
| 认证授权 | API key、OAuth、session、scope、tenant、RBAC | 明确鉴权边界和最小权限。 |
| 数据模型 | 实体、关系、索引、约束、事务、并发、一致性 | 迁移有验证和回滚策略。 |
| 查询与分页 | filter、sort、cursor、offset、rate limit、partial response | 大数据量下行为稳定。 |
| CLI/SDK | 命令树、配置、环境变量、JSON/NDJSON、dry-run、doctor | 适合自动化和脚本组合。 |
| 数据平台 | ETL、schema drift、数据质量、审计日志、重跑和幂等 | 数据链路可恢复。 |
| 兼容演进 | breaking change、deprecation、feature flags、migration notes | 用户可平滑升级。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| api-design | 接口资源、OpenAPI、请求/响应、错误码、版本策略。 |
| database | schema、迁移、索引、事务、SQL/NoSQL、备份恢复。 |
| cli-creator | 可组合 CLI、SDK 封装、JSON 输出、doctor/dry-run。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 契约发现 | 读取现有 routes、schema、OpenAPI、SDK、README、测试和客户端调用点。 | 知道现有接口风格。 |
| 模型设计 | 定义实体、权限、状态机、错误、分页、幂等和兼容要求。 | 契约不含模糊行为。 |
| 实现路径 | 优先复用现有 controller/service/repository/CLI 框架。 | 改动边界清晰。 |
| 数据安全 | 检查输入校验、参数化查询、敏感字段、日志脱敏和权限检查。 | 数据不泄漏、不越权。 |
| 验证 | 跑接口测试、迁移 dry-run、本地样例、CLI help/json 输出。 | 用户能复现。 |
| 文档交付 | 更新 OpenAPI/README/示例，不包含真实凭据。 | 契约可被使用。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 生产数据库迁移、数据回填、删除、远程 API 写入必须确认。
- 修改公共 API 或破坏兼容性前必须标明影响范围。
- 生成 GitHub/云端 CLI 自动化时，不默认执行远程写入。

## 验证清单
- 接口：schema/contract 测试、curl 本地样例、错误路径。
- 数据库：迁移 up/down、约束、索引 explain、事务测试。
- CLI：`--help`、无配置错误、只读命令、JSON 输出解析。
- SDK：类型检查、示例代码和异常处理。

## 反模式
- 把 API 错误统一成 500 或模糊字符串。
- 分页、排序、过滤没有稳定契约。
- 迁移没有回滚和数据验证。
- CLI 输出只适合人看，不适合机器解析。

## 合并来源
- `api-design`
- `database`
- `cli-creator`

## 本机相近 Skill
- `cli-creator`
- `gh-cli`

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
