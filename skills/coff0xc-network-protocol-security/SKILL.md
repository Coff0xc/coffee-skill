---
name: coff0xc-network-protocol-security
description: "Use when / 当用户请求: 全面网络协议、TLS/DNS/TCP/UDP/QUIC/HTTP、无线/RF/蓝牙、协议日志分析、通信安全和形式化协议建模工作流。触发：network protocol、TLS、DNS、HTTP/2、HTTP/3、QUIC、TCP、UDP、WiFi、Bluetooth、BLE、RF、packet、pcap、Wireshark、协议分析、安全通信、ProVerif、Mermaid protocol、抓包、握手、解析异常、加密协商、异常字段、通信流程。 Covered source aliases / 来源别名: network-protocol, wireless-security. Capability domains / 能力域: 协议设计, TLS/PKI, DNS, HTTP/QUIC, Packet 分析, 无线/BLE/RF, 形式化. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-network-protocol-security."
---

# coff0xc-network-protocol-security

## 能力定位
面向网络协议、TLS/DNS/QUIC/HTTP、无线通信、抓包和形式化建模的协议安全分析能力。它把通信证据转成流程图、风险点和验证建议。

## 能交付什么
- 协议流程、握手和状态机说明
- pcap/日志字段分析、异常字段和安全影响
- TLS/PKI/DNS/HTTP/QUIC/无线风险清单
- Mermaid/ProVerif/Tamarin 方向的建模建议

## 可以接收什么输入
- pcap、Wireshark 导出、协议日志、报文字段
- 协议规范、实现代码、握手说明、证书链
- 无线/BLE/RF 捕获摘要或设备通信流程

## 放心使用的边界
- 可做本地抓包和授权通信分析
- 不提供未授权监听、入侵、绕过或干扰第三方网络步骤
- 主动探测、无线发射、生产网络测试必须先确认范围
- 安全类能力默认只用于授权、防御、检测、加固、验证和报告；不提供未授权攻击、凭据窃取、持久化、规避检测、C2、钓鱼收集、数据外传或破坏性步骤。

## 为什么可以放心
- 把报文字段、代码和规范分开标注证据
- 优先说明状态机和信任边界
- 形式化建模只表达可验证协议性质，不夸大结论

## 典型使用方式
```text
使用 coff0xc-network-protocol-security 分析这个 pcap 里的 TLS 握手和异常字段。
使用 coff0xc-network-protocol-security 把这个协议流程画成 Mermaid 并指出安全边界。
Use coff0xc-network-protocol-security to review DNS/QUIC behavior and propose verification checks.
```


## 目标
分析通信协议和网络遥测中的安全属性、状态机、认证、加密和配置风险，默认用于授权和防御场景。

## 适用场景
- 分析协议设计、抓包、日志、TLS/DNS/HTTP/QUIC 配置、无线/BLE/RF 合规测试和通信安全。
- 把协议描述转成时序图、状态机、威胁模型或形式化验证输入。
- 诊断连接失败、证书错误、降级风险、重放风险和网络检测规则。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-network-protocol-security ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 不提供未授权无线攻击、干扰、绕过、捕获凭据或第三方网络入侵步骤。
- 不对生产网络执行主动扫描、压测或变更，除非确认授权。
- 不把加密算法名称当作安全结论，必须看配置和协议上下文。

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
| 协议设计 | 消息流、状态机、认证、密钥协商、重放、降级、错误处理 | 可画图和验证。 |
| TLS/PKI | 证书链、SAN、过期、cipher、mTLS、OCSP、pinning、HSTS | 配置有证据。 |
| DNS | 解析链、DNSSEC、DoH/DoT、缓存、split horizon、zone transfer 风险 | 日志和配置结合。 |
| HTTP/QUIC | headers、cookies、CORS、cache、HTTP/2/3、ALPN、proxy | 应用协议边界。 |
| Packet 分析 | pcap、Wireshark、flow、latency、重传、异常序列 | 网络事实可复查。 |
| 无线/BLE/RF | 频段、配对、认证、加密、设备暴露、合规测试 | 授权实验室优先。 |
| 形式化 | Mermaid sequence、ProVerif/Tamarin 思路、攻击者模型 | 安全性质明确。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| network-protocol | 有线/互联网协议、TLS/DNS/HTTP/QUIC/pcap 分析。 |
| wireless-security | WiFi/BLE/RF 合规和防御分析。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 输入确认 | 确认 pcap、日志、配置、协议文档、设备、授权和时间窗。 | 数据合法可分析。 |
| 协议建模 | 列参与方、消息、状态、密钥、信任边界和攻击者能力。 | 安全属性明确。 |
| 证据分析 | 从抓包、日志、配置、证书和源码提取事实。 | 不是凭经验猜。 |
| 风险判断 | 检查认证、加密、完整性、重放、降级、隐私和错误处理。 | 发现有上下文。 |
| 修复检测 | 给配置、协议变更、日志字段、规则和复测方法。 | 能执行和验证。 |
| 图示/报告 | 输出时序图、状态机、证据表和剩余风险。 | 便于沟通。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 无线测试、抓包、主动扫描或连接设备前确认授权和法规边界。
- 生产证书、DNS、路由、WAF/proxy 配置修改前确认。
- 形式化结论要说明攻击者模型和未建模假设。

## 验证清单
- TLS：证书链、cipher、协议版本、握手日志或测试命令。
- DNS：权威/递归路径、记录、TTL、DNSSEC 状态。
- pcap：过滤表达式、包号、时间戳和字段。
- 协议模型：安全性质、参与方和反例/无反例条件。

## 反模式
- 只看端口开放就下安全结论。
- 没有时间窗和包号的抓包分析。
- 把实验室无线方法用于真实第三方环境。
- 形式化模型漏掉关键参与方却给强结论。

## 合并来源
- `network-protocol`
- `wireless-security`

## 本机相近 Skill
- `crypto-protocol-diagram`
- `mermaid-to-proverif`

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
