---
name: coff0xc-software-engineering
description: "Use when / 当用户请求: 全面软件工程、语言开发、测试、重构、脚本、Git 和工程质量工作流。触发：Python、JavaScript、TypeScript、Go、Rust、Java、C/C++、Shell、bugfix、feature、测试、重构、构建、脚本、Git、本地工程化、仓库跑不起来、报错链路、最小修复、证明好了、failing tests、repo does not run。 Covered source aliases / 来源别名: c-cpp-dev, code-simplifier, git-workflow, go-dev, java-dev, js-ts-dev, python-dev, rust-dev, shell-scripting, testing. Capability domains / 能力域: 语言实现, 缺陷修复, 特性开发, 重构简化, 测试体系, 构建质量, Git 协作. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-software-engineering."
---

# coff0xc-software-engineering

## 目标
把粗略需求落到可运行、可测试、可维护的工程改动上，同时保持仓库风格和用户已有改动不被覆盖。

## 适用场景
- 多语言代码实现、bug 修复、脚本编写、测试补齐、工程化整理和局部重构。
- 需要读取项目结构、定位调用链、修改多个文件并运行验证的任务。
- 需要在不触碰远程状态的前提下查看 Git 状态、diff、分支、提交准备或变更摘要。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-software-engineering ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 纯解释问题或一行命令查询，直接回答即可。
- 生产部署、force 操作、删除分支/文件、远程 push、CI 权限变更，必须单独授权。
- 安全审计深挖应转入 `coff0xc-secure-code-appsec` 或相关安全 skill。

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
| 语言实现 | Python、JS/TS、Go、Rust、Java、C/C++、Shell | 遵循项目已有包管理、格式化、类型和测试方式。 |
| 缺陷修复 | 复现、根因、最小补丁、回归测试 | 先定位失败路径，避免只改表象。 |
| 特性开发 | 接口、数据流、状态、错误处理、边界条件 | 先定义验收标准，再按模块实现。 |
| 重构简化 | 去重、命名、模块边界、死代码、复杂分支 | 保持行为不变，明确回归验证。 |
| 测试体系 | 单元、集成、属性测试、fixtures、mock、e2e 入口 | 用风险决定测试深度。 |
| 构建质量 | lint、typecheck、format、build、package、dependency lock | 先跑窄验证，再跑宽验证。 |
| Git 协作 | status、diff、变更摘要、提交候选说明 | 不 reset、不 checkout 覆盖用户改动。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
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

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 恢复上下文 | 读取 AGENTS/README/manifest/lockfile/配置/测试脚本，查看目录和 dirty 状态。 | 知道项目类型、现有命令和用户已有改动。 |
| 定位影响面 | 找入口、调用点、类型、数据结构、边界条件和可用测试。 | 知道该改哪些文件和不该碰哪些文件。 |
| 实现改动 | 按现有风格最小补丁，保留兼容行为，避免无关重构。 | 代码完成且没有明显并行系统。 |
| 窄验证 | 运行与变更直接相关的单测、类型检查或脚本。 | 关键路径通过或失败原因明确。 |
| 宽验证 | 必要时运行 lint、build、集成测试或 smoke check。 | 跨模块影响被覆盖。 |
| 复查交付 | 检查 diff、删除临时输出、记录风险和下一步。 | 用户能看到完成项和验证项。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 删除、重命名大量文件、迁移目录结构或更换包管理器前必须确认。
- 引入新依赖前确认项目已有依赖习惯和实际收益。
- 无法运行测试时，说明原因并给出用户可运行命令。

## 验证清单
- Python：`pytest`、`ruff check`、`mypy/pyright` 或项目脚本。
- JS/TS：`npm/pnpm/yarn test`、`lint`、`typecheck`、`build`。
- Go/Rust/Java/C++：对应 `test`、`fmt`、`lint`、`build`。
- Shell：语法检查、dry-run、路径边界检查和最小样例运行。

## 反模式
- 没读项目就按通用模板改。
- 为了小问题引入新框架或大抽象。
- 吞异常、伪造兼容层、只修测试不修逻辑。
- 覆盖用户未要求回滚的改动。

## 合并来源
- `c-cpp-dev`
- `code-simplifier`
- `git-workflow`
- `go-dev`
- `java-dev`
- `js-ts-dev`
- `python-dev`
- `rust-dev`
- `shell-scripting`
- `testing`

## 本机相近 Skill
- `dev`
- `modern-python`
- `property-based-testing`
- `planning-with-files`

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
