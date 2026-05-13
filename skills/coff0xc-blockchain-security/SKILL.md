---
name: coff0xc-blockchain-security
description: "Use when / 当用户请求: 全面区块链、智能合约、DeFi、Web3、跨链、代币和多链安全审计工作流。触发：Solidity、EVM、Solana、Cosmos、Substrate、Cairo/StarkNet、TON、Algorand、DeFi、AMM、oracle、bridge、token、NFT、智能合约审计、Foundry、Hardhat、Slither、链上资金逻辑、价格来源、资产流转、合约权限、测试覆盖。 Covered source aliases / 来源别名: blockchain-security. Capability domains / 能力域: EVM/Solidity, Solana, Cosmos/CosmWasm, Substrate, Cairo/StarkNet, TON/Algorand, DeFi, Token/NFT. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-blockchain-security."
---

# coff0xc-blockchain-security

## 目标
围绕资产流、权限、状态机和链特性审计合约与协议，优先使用链专用工具和测试证明风险。

## 适用场景
- 审计智能合约、DeFi 协议、链上资产流、权限、升级、预言机、桥、代币集成。
- 分析多链项目、链特定风险、测试覆盖、形式化/模糊测试和修复建议。
- 做审计准备、入口点枚举、漏洞验证和报告。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-blockchain-security ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 不指导真实链上套利、抢跑、攻击、资金转移或未授权交易。
- 不使用真实私钥、主网资金或生产合约执行风险操作。
- 链上最新事件、合约状态、价格和漏洞事实必须实时查证。

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
| EVM/Solidity | 重入、访问控制、delegatecall、升级、签名、MEV、oracle、flash loan | Foundry/Hardhat/Slither 证据。 |
| Solana | PDA、account owner、signer、CPI、rent、sysvar、seeds | 账户约束和 CPI 边界。 |
| Cosmos/CosmWasm | message handlers、IBC、capability、authz、bank 模块 | 状态转换和链停风险。 |
| Substrate | origin、weights、storage、runtime upgrade、pallet 权限 | 共识和链 halt 风险。 |
| Cairo/StarkNet | felt、L1/L2 messaging、storage、account abstraction | 域特定边界。 |
| TON/Algorand | 消息、Jetton、rekeying、fee、field validation | 链模型差异。 |
| DeFi | AMM、lending、liquidation、oracle、governance、bridge、vault | 经济攻击和不变量。 |
| Token/NFT | ERC20/721/1155、permit、fee-on-transfer、rebasing、blacklist、integration | 兼容性和资产安全。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| blockchain-security | 总控：识别链、资产、入口、工具和测试策略。 |
| chain-specific scanners | 优先转用已安装的 Solana/Cosmos/Substrate/Cairo/TON/Algorand 专用 skill。 |
| token-integration | 代币标准、兼容性和外部集成风险。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 项目画像 | 确认链、语言、框架、部署状态、资产、权限、升级和测试。 | 审计范围清楚。 |
| 入口枚举 | 列 public/external handlers、admin functions、cross-chain messages、keepers、hooks。 | 入口完整。 |
| 资产流 | 画 deposit/withdraw/swap/borrow/liquidate/bridge/governance 状态流。 | 关键不变量明确。 |
| 工具扫描 | 运行链适配工具和测试，保留原始输出并人工复核。 | 发现有证据。 |
| 人工审计 | 按权限、状态、外部调用、数学、经济模型、链特性检查。 | 覆盖深层风险。 |
| 验证修复 | 添加 PoC 单测/不变量/模糊测试，复测修复。 | 风险闭环。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 主网交易、私钥、资金操作、合约升级、治理投票前必须确认并通常不代执行。
- 经济攻击模拟仅在 fork/lab 中进行，不指导真实攻击获利。
- 外部协议/价格/链状态必须查当前来源。

## 验证清单
- 单元测试、fork test、invariant/fuzz、static analysis、gas/weight 检查。
- 每个发现说明前置条件、资产影响、可达入口和修复测试。
- 修复后跑原失败用例和相关回归。

## 反模式
- 只用 Slither 输出当审计报告。
- 忽略协议经济不变量。
- 把 EVM 经验直接套到非 EVM 链。
- 不区分 owner/admin/keeper/user/attacker 权限。

## 合并来源
- `blockchain-security`

## 本机相近 Skill
- `solana-vulnerability-scanner`
- `cosmos-vulnerability-scanner`
- `substrate-vulnerability-scanner`
- `token-integration-analyzer`
- `secure-workflow-guide`

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
