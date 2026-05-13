---
name: coff0xc-ai-agent-rag
description: "Use when / 当用户请求: 全面 AI Agent、RAG、Prompt、LLM 应用、多模型协作、评测、观测和成本控制工作流。触发：Agent、RAG、embedding、向量数据库、Prompt、LangChain、AutoGen、工具调用、多模型编排、代码审计协作、视觉分析、评测、缓存、记忆、失败恢复、查资料助手、调用工具、答错追踪、可落地 AI 助手、AI workflow。 Covered source aliases / 来源别名: ai-agent-dev, ai-orchestrator, deep-thinking. Capability domains / 能力域: Agent 架构, 工具调用, 记忆系统, RAG 管线, Prompt 工程, 评测, 观测与成本. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-ai-agent-rag."
---

# coff0xc-ai-agent-rag

## 目标
构建可观测、可评测、可恢复的 AI 系统；不要只交付 Prompt，要覆盖数据、工具、检索、模型、评测、安全和运行成本。

## 适用场景
- 设计或实现 Agent、RAG、LLM workflow、prompt pipeline、多模型协作或自动化推理系统。
- 诊断检索质量、幻觉、引用错误、工具失败、上下文过长、成本过高或 latency 问题。
- 把模糊 AI 需求转成架构、数据流、评测集、观测指标和可运行代码。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-ai-agent-rag ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 普通 CRUD 或非 AI 功能用软件工程 skill。
- OpenAI 产品/API 的当前模型、参数或 SDK 细节必须结合官方文档确认。
- 不要把敏感数据发给外部模型或工具，除非用户明确授权并确认脱敏策略。

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
| Agent 架构 | ReAct、Plan-and-Execute、router、planner、tool-user、critic、multi-agent | 明确哪些步骤确定性执行，哪些步骤交给模型判断。 |
| 工具调用 | tool schema、权限、timeout、retry、sandbox、幂等、错误恢复 | 工具输入输出要结构化，失败路径可观测。 |
| 记忆系统 | 短期上下文、长期记忆、用户偏好、检索缓存、版本化摘要 | 区分事实、偏好、过期信息和可删除数据。 |
| RAG 管线 | 加载、清洗、切分、embedding、索引、混合检索、rerank、context packing、引用 | 每段上下文能追溯来源。 |
| Prompt 工程 | 任务、角色、约束、样例、输出 schema、拒答、工具边界 | Prompt 是系统的一部分，不是唯一交付物。 |
| 评测 | golden set、retrieval eval、answer eval、citation eval、refusal eval、adversarial eval | 用样例和指标证明改进。 |
| 观测与成本 | token、latency、cache hit、tool error、retry、用户反馈、人工接管 | 能定位质量下降和成本异常。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| ai-agent-dev | 单 Agent、工具、记忆、Prompt、RAG 应用开发。 |
| ai-orchestrator | 多模型协作、任务路由、视觉/研究/审计分工。 |
| deep-thinking | 复杂问题拆解、方案比较、推理校验和反例检查。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 需求包 | 定义目标、用户、输入、输出、成功标准、非目标、风险门禁。 | 知道系统要解决什么和不解决什么。 |
| 架构分层 | 拆成 deterministic steps、model calls、tools、memory、retrieval、human gates。 | 系统边界清晰。 |
| 数据与检索 | 确认数据源、权限、更新频率、chunk 策略、embedding、索引、rerank 和引用。 | RAG 可追溯、可刷新。 |
| 实现与约束 | 实现 schema、工具错误处理、缓存、日志、fallback 和超时。 | 核心链路可运行。 |
| 评测集 | 构造正常、边界、缺失、冲突、恶意、长上下文样例。 | 能衡量质量而不是凭感觉。 |
| 观测上线 | 记录质量、成本、延迟、失败率和人工反馈。 | 有回归监控和调参依据。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 外部模型、付费 API、用户隐私数据、生产数据、长期记忆写入前必须确认。
- 声称支持某模型、SDK 参数或价格前必须查官方当前文档。
- 多 Agent 并行写同一文件或访问同一远程资源前必须分清边界。

## 验证清单
- 最小端到端样例：输入到输出完整跑通。
- RAG：检索命中、上下文引用、拒答和冲突处理样例。
- Agent：工具失败、超时、无权限、无结果和恢复路径。
- 成本：估算 token/API 调用次数，记录高成本路径。

## 反模式
- 只写一个很长的 Prompt 就说完成 Agent。
- 没有评测集就宣称效果更好。
- 把网页或文档里的不可信指令写进系统 Prompt。
- 让模型决定权限、计费、删除、生产发布等高风险动作。

## 合并来源
- `ai-agent-dev`
- `ai-orchestrator`
- `deep-thinking`

## 本机相近 Skill
- `dev`
- `source-command-ai-agent-dev`
- `openai-docs`

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
