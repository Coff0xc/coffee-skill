---
name: coff0xc-software-engineering
description: "Use when / 当用户请求: dev, autonomous development, build end-to-end, full-stack feature, one-shot implementation, repo repair, monorepo repair, failing tests, CI failing tests, bugfix, code bug, refactor, scripts, local Git summary, CI failure triage, test reproduction, fast inner loop, need package, module loop, integration verification, browser smoke, diff hygiene, lockfile discipline, Python, JavaScript, TypeScript, Go, Rust, Java, C/C++, Shell, dashboard/admin/API implementation, usage ledger, platform feature, 最小修复、证明好了、仓库跑不起来、多文件开发、全栈功能、平台开发、代码 bug、修 API、少问确认、直接实现、先读仓库规则、快速内循环、复现 CI、模块化实现、最终审计、只暂存相关文件。 Covered source aliases / 来源别名: dev, c-cpp-dev, code-simplifier, git-workflow, go-dev, java-dev, js-ts-dev, python-dev, rust-dev, shell-scripting, testing. Capability domains / 能力域: 自主开发, 语言实现, 缺陷修复, 特性开发, 重构简化, 测试体系, 构建质量, Git 协作. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-software-engineering."
---

# coff0xc-software-engineering

## 能力定位
面向真实仓库的工程交付能力。适合把模糊需求变成可运行代码、可复现修复、可验证测试结果和清晰 diff 摘要。

## 能交付什么
- 代码补丁、脚本或配置修改
- 失败原因和根因链路说明
- 单元/集成/构建验证结果
- Git diff 摘要和剩余风险

## 可以接收什么输入
- 本地仓库、报错日志、测试输出、issue 描述
- 需求草稿、接口说明、UI 截图或现有模块
- package/lockfile、README、AGENTS、CI 脚本

## 放心使用的边界
- 可直接做本地、可逆、低风险的代码和测试改动
- 删除、远程 push、生产配置、凭据、付费服务和 CI/CD 权限变更必须先确认
- 不为小问题引入新框架或无必要依赖
- 默认只处理本地、可逆、可验证的低风险工作；涉及生产、凭据、付费、远程写入、删除、发布或权限变更时必须先确认。

## 为什么可以放心
- 先读项目结构和现有风格，再修改
- 先跑窄验证，再按风险跑宽验证
- 未运行的测试不会写成已通过

## 典型使用方式
```text
使用 coff0xc-software-engineering 修复这个 repo 的 failing tests，并说明验证结果。
使用 coff0xc-software-engineering 少问确认，直接实现这个多文件开发任务。
Use coff0xc-software-engineering to build this admin panel feature end to end with tests.
```


## 目标
把粗略开发需求落到可运行、可测试、可维护的本地工程改动上。默认少打断用户，先查项目、记录假设、做最小正确改动、跑可用验证，再用证据交付。

## 适用场景
- 单仓或多模块代码实现、bug 修复、failing tests、脚本编写、局部重构和测试补齐。
- 需要端到端推进的开发任务：页面、dashboard、admin panel、API、CLI、后台 job、本地工具、集成胶水代码。
- 仓库跑不起来、构建失败、依赖脚本不清楚、报错链路需要定位。
- 本地 Git 检查、diff 摘要、提交前候选说明，但不包含 push 或远程状态修改。

## 不适用场景
- 一行命令、纯解释、简单概念判断：直接回答即可。
- 纯 AI Agent/RAG/Prompt 架构设计：转入 `coff0xc-ai-agent-rag`；如果任务要求把 Agent/RAG 真正接进应用，本 skill 负责工程实现并调用该 skill 的设计约束。
- 纯 API/数据库契约设计：转入 `coff0xc-api-data-platform`；如果任务要求实现接口和迁移，本 skill 负责落地。
- 纯 UI 视觉打磨：转入 `coff0xc-ui-doc-output`；如果任务要求改前端代码，本 skill 负责实现并按 UI 验证要求检查。
- 安全审计深挖：转入 `coff0xc-secure-code-appsec` 或对应安全 skill。

## 风险分级
| 等级 | 范围 | 行为 |
| --- | --- | --- |
| L0 | 稳定概念、简单命令、无文件改动 | 直接回答或运行显然命令，标注未验证处。 |
| L1 | 单文件或局部可逆修改 | 查相关文件，最小补丁，跑窄验证。 |
| L2 | 多文件、多模块、端到端功能 | 给短计划，分模块实现，每个模块后验证和复查。 |
| L3 | 架构/API/schema/auth/AI/安全敏感逻辑/重大选型 | 查官方或源码证据，定义验证策略，再实现。 |
| L4 | 生产、凭据、付费、删除、远程写入、push/PR、CI/CD、权限、基础设施 | 停止执行相关动作，先拿明确授权。 |

升级规则：影响面扩大就升级；涉及当前事实、版本、外部 API 或安全结论至少 L3；涉及外部可见或不可逆动作就是 L4。

## 默认行为
- 能合理推断的低风险细节直接决定，并把它写成假设。
- 优先遵循仓库已有框架、包管理器、脚本、测试、命名和错误处理风格。
- 先做局部正确实现，不为未来假设引入新框架、新依赖或并行系统。
- 不回滚用户未要求回滚的改动；dirty worktree 先读清楚再协作。
- 命令、测试、构建、lint、浏览器检查只有真实运行后才能写成“已验证”。
- 同一路线连续失败两次，停止重复，换方案或说明阻塞。

## 默认快路径
普通开发任务按这个顺序走：

1. 读最小必要上下文：仓库规则、相关入口、已有改动和可用脚本。
2. 定最小影响面：哪些文件必须改、哪些文件不碰、怎么验证。
3. 直接实现：小步 patch，不做无关重构和新框架迁移。
4. 跑可用验证：先窄后宽，能跑 test/typecheck/lint/build/browser smoke 就跑。
5. 简短收口：完成项、真实验证、剩余风险、下一步。

不要为普通任务创建 quality eval、workflow trace、golden response、长篇 skill graph 或发布检查报告。只有用户明确要求 skill 质量验证、review、eval、发版、推送、CI/benchmark 门禁时，才进入重型门禁。

## 必须先确认
- 删除文件、drop table、清空缓存、迁移真实数据、force push、修改 main/master、reset hard。
- push、发布、部署、创建/关闭/评论 PR 或 Issue、发送外部消息。
- 使用生产凭据、外部账号、付费 API、云资源、CI/CD 权限或基础设施。
- 修改认证授权、支付、权限模型、生产配置，且风险无法通过本地可逆改动隔离。

## 工作循环
```text
恢复上下文 -> 需求包 -> 影响面 -> 短计划 -> 模块循环 -> 集成验证 -> 最终审计 -> 交付
```

### 1. 恢复上下文
先查真实项目，不凭记忆猜。

- 读取 `AGENTS.md`、`CLAUDE.md`、README、manifest、lockfile、框架配置、env example、测试脚本；编辑子目录前沿路径读取就近 README/AGENTS/开发说明。
- 查看 `git status --short`、当前分支和已有改动。
- 用 `rg --files`、`rg`、语言工具或项目脚本找入口、调用点、测试和构建命令。
- 如果已有 `task_plan.md`、`progress.md`、`findings.md`，先读并延续。
- 识别包管理器和工具版本：npm/pnpm/yarn/bun、poetry/uv/pip、cargo、go、maven/gradle、bazel，以及 lockfile 是否应保持原生成工具版本。

完成标准：知道项目类型、可用命令、用户已有改动、主要入口和不能碰的边界。

### 2. 需求包
不要长时间访谈。把用户需求压成一个可执行包：

| 字段 | 要写清楚什么 |
| --- | --- |
| Goal | 最终用户、系统或维护者要能做什么。 |
| Users / workflow | 主要路径、失败路径、管理员/系统路径。 |
| Inputs / outputs | 数据、文件、接口、页面、命令、事件或后台任务。 |
| UI surface | 路由、组件、状态：loading、empty、error、success、disabled。 |
| API surface | endpoint/action、request/response、validation、auth/permission。 |
| Data model | entity、关系、迁移、兼容读取、fixture。 |
| Non-goals | 本轮不做什么，避免范围膨胀。 |
| Assumptions | 低风险推断及风险等级。 |
| Acceptance | 功能路径、失败路径、测试、typecheck/lint/build、UI smoke。 |
| Risk gates | 生产、凭据、付费、远程写入、删除、公开发布、CI/CD 权限。 |

大任务把需求包写进计划或进度文件；小任务可以只在回复或内部计划中保留。

### 3. 影响面定位
写代码前确认：

- 入口、路由、命令、组件、服务、模型、schema、配置和测试。
- 调用链、数据流、状态归属、错误路径、权限边界。
- 需要新增/更新的测试，和可运行的最小验证命令。
- 是否需要同步文档、示例、类型、schema、迁移或快照。

完成标准：能说清该改哪些文件、为什么改、如何验证。

### 3.5 快速内循环
成熟大仓通常不是每次都全量 build。先找项目推荐的快速路径，再逐步加宽验证：

- 优先用项目自带 watch、targeted test、filter、workspace 命令、Storybook/component test、package-specific build。
- 测试失败先保存一次完整输出，再检索错误，不要用不同 grep 反复跑同一重测试。
- CI 失败复现要尽量匹配 CI mode、env、bundler、isolation、数据库/浏览器配置；不要用本地 shortcuts 掩盖打包或模块解析问题。
- 子模块改动使用对应包/目录命令；跨模块接口改动再跑集成或全量命令。
- 如果项目要求生成测试模板、fixture、snapshot、schema 或 docs，优先用项目脚本生成，不手写不一致结构。

### 4. 模块循环
对每个模块执行完整闭环：

```text
模块设计 -> 最小实现 -> 窄验证 -> 自审 -> 修正 -> 标记完成
```

实现要求：

- 使用现有抽象和结构化 API，不靠脆弱字符串拼接处理结构化数据。
- 不吞异常，不伪造兼容层，不用测试专用逻辑掩盖真实问题。
- 新依赖必须有明确收益，并符合项目已有依赖习惯。
- UI 改动要覆盖 loading、empty、error、success、disabled、mobile/desktop 和可访问性基础状态。
- API/后端改动要覆盖输入校验、错误码、边界条件、认证/授权、日志和敏感信息处理。
- 数据/schema 改动要考虑迁移、回滚、兼容读取和测试 fixture。
- 锁文件只在依赖真实变化时更新；再生成 lockfile 前检查原工具和版本，避免纯工具版本造成噪声。
- 临时设计笔记、日志、实验脚本放到项目允许的位置；如果没有约定，保持本地不提交，最终说明。

### 5. 验证策略
先窄后宽，按风险加码。

| 变更类型 | 最小验证 | 扩展验证 |
| --- | --- | --- |
| Python | `pytest` 相关用例、`ruff check`、类型检查 | 全量测试、包构建 |
| JS/TS | 相关 test、`lint`、`typecheck` | `build`、browser smoke、e2e |
| Go | `go test ./...` 或目标包、`gofmt` | race、集成测试 |
| Rust | `cargo test`、`cargo fmt --check` | `cargo clippy`、release build |
| Java | 目标 Maven/Gradle test | 全量 build、集成测试 |
| C/C++ | 目标构建和单测 | sanitizer、valgrind、平台构建 |
| Shell/PowerShell | 语法检查、dry-run、路径边界 | 最小样例运行 |
| UI | 本地页面打开、截图/浏览器 smoke、console 检查 | 响应式和关键流程 e2e |

无法验证时说明：缺什么环境、哪个命令没跑、风险是什么、用户下一步可运行什么。

### 5.5 CI / 回归失败分诊
当用户给 CI、测试、lint、build 或线上回归信号时：

- 先按阻塞程度排序：build/typecheck/lint > 单测 > 集成/e2e > flaky/视觉。
- 假设失败为真，先复现或用日志定位，不把 known flaky 当作免修理由。
- 区分新失败、已有失败、平台/环境失败和测试本身错误；每类用不同修复策略。
- 对同一路线连续失败两次，停止盲跑，回到调用链和最小复现。
- 修测试前先确认测试覆盖真实行为；不要只改断言迎合错误实现。

### 6. 最终同类审计
交付前复查完整 diff：

- 是否满足需求包和验收标准。
- 是否产生重复模型、重复状态、平行实现或死代码。
- 前后端/API/schema/类型是否对齐。
- 错误、空状态、边界条件、权限和敏感信息处理是否完整。
- 测试是否覆盖真实行为，而不只是 happy path。
- 临时文件、调试日志、硬编码路径、密钥和机器私有信息是否被清理。
- Git 卫生：只暂存相关文件，不用 `git add .`；不提交本地计划/日志/截图/临时输出，除非用户明确要。

## 高星仓库借鉴的工程门禁
以下是从成熟开源工程和高星 agent skill 中提炼的通用模式，已改写成本 skill 的执行要求：

| 门禁 | 执行方式 |
| --- | --- |
| 本地规则优先 | 任何代码前先读根部和目标路径附近的说明、脚本、锁文件、测试约定。 |
| 快速反馈 | 使用 target test/watch/filter，先缩小失败面，再跑更宽验证。 |
| CI 等价复现 | CI 问题要匹配 CI 环境变量、bundler、isolation、数据库、浏览器模式。 |
| 模块化合并 | 每个模块做完即窄验证和自审，避免最后才发现跨模块断裂。 |
| 依赖纪律 | 先查现有依赖；新增依赖要有明确收益；锁文件不做工具版本噪声更新。 |
| 变更卫生 | 只改请求范围；只暂存相关文件；保留用户未要求回滚的改动。 |
| 真实测试 | 测试覆盖行为和失败路径；不用 snapshot 或 happy path 假装覆盖。 |
| UI 协作 | 前端实现由本 skill 落地，但必须套用 `coff0xc-ui-doc-output` 的 UI 状态/视觉验收门禁。 |

## Release / Skill 改进自测
仅当用户要求“确认 dev skill 是否真的好用”“优化开发 skill”“不要只堆触发词”“发版前验证”“推送前跑门禁”时使用。普通 repo repair 不跑这里的质量 eval，除非它就是当前仓库的发版要求。

不要只改 frontmatter。优先用仓库内真实 repair 夹具校准：

- 参考 `evals/quality/cases/dev-repo-repair-ci-gate/`：输入包含 `AGENTS.md`、README、CI 日志、lockfile、源码和失败测试。
- 合格输出必须有修复后的 `src/billing.py` 和 `repair-notes.md`；如果输出 `requirements.lock`，必须与输入一致，除非依赖真实变化。
- `repair-notes.md` 要能证明：Need Package、fast inner loop、CI 线索、pytest 验证、root cause 和 lockfile discipline。
- 运行 `python .\scripts\run_quality_eval.py` 检查夹具完整性；有真实 agent 输出时运行 `python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses`。runner 会加载候选 `billing.py` 做行为断言，避免只靠关键词假通过。
- 质量 eval 是最小行为基准，不替代真实项目的 typecheck、lint、build、browser smoke 或 CI。

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| dev | 端到端开发、少确认推进、模块循环、集成验证和最终审计。 |
| python-dev | Python 项目、脚本、包管理、typing、ruff/pytest/uv。 |
| js-ts-dev | Node、React、TS、前端/后端 JS、npm/pnpm/yarn。 |
| go-dev | Go module、gofmt、go test、并发和接口设计。 |
| rust-dev | Cargo、borrow/lifetime、trait、clippy、测试。 |
| java-dev | Maven/Gradle、Spring、JVM 测试和类型接口。 |
| c-cpp-dev | C/C++ 构建、CMake/Make、内存安全和本地测试。 |
| shell-scripting | PowerShell/Bash 自动化、路径安全、可重复运行脚本。 |
| testing | 测试策略、覆盖缺口、回归用例和验证命令。 |
| code-simplifier | 局部简化、去重、可读性和复杂度降低。 |
| git-workflow | 本地 Git 检查、diff 解释、提交前准备。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 反模式
- 没读项目就按通用模板改。
- 小问题引入新框架、大抽象或额外服务。
- 只改测试不修逻辑，或只修表象不定位根因。
- 为了“兼容”吞异常、隐藏失败或返回假成功。
- 把未运行的命令写成已通过。
- 在用户未授权时删除、push、发布或修改远程状态。

## 输出合同
最终回复只保留高信号内容：

```markdown
完成：
- ...

验证：
- [已验证] ...
- [未验证] ...

还剩：
- ...

下一步：
- ...
```

失败时使用：

```markdown
失败命令 / 动作：
错误信息：
已排除：
可能原因：
下一步：
```

## 手动触发
- `使用 coff0xc-software-engineering 修复这个 repo 的 failing tests，并说明验证结果`
- `Use coff0xc-software-engineering to build this feature end to end with tests`
- `使用 coff0xc-software-engineering 少问确认，直接实现这个多文件开发任务`
