---
name: coff0xc-binary-mobile-iot
description: "Use when / 当用户请求: 全面二进制/逆向/内核/移动/IoT/ICS/CTF/密码学安全分析工作流。触发：reverse engineering、PWN、kernel、APK、IPA、Frida、firmware、UART、JTAG、SPI、SCADA、PLC、Modbus、BLE、RF、CTF、crypto review、constant-time、设备包、可执行文件、通信固件、静态分析、动态调试、接口枚举。 Covered source aliases / 来源别名: binary-exploit, crypto-security, ctf, ics-scada, iot-security, kernel-security, mobile-security, reverse-engineering. Capability domains / 能力域: 二进制/逆向, PWN/CTF, 内核安全, 移动安全, IoT 固件, 硬件接口, ICS/OT, 密码学. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-binary-mobile-iot."
---

# coff0xc-binary-mobile-iot

## 能力定位
面向二进制、移动、IoT/ICS、固件和密码实现的逆向分析能力。它把样本、固件、APK、协议和调试线索转成结构化理解、风险点和验证路线。

## 能交付什么
- 样本/固件结构和入口点分析
- 字符串、配置、权限、通信和硬件接口线索
- 内存安全、加密实现、协议解析或移动风险发现
- 复现环境、工具命令、证据和修复建议

## 可以接收什么输入
- 可执行文件、APK/IPA、固件、pcap、日志、反编译结果
- Ghidra/IDA/Frida 输出、strings、符号、崩溃栈
- 硬件接口说明、UART/JTAG/SPI 线索、ICS 协议文档

## 放心使用的边界
- 可做本地样本、授权设备和实验环境分析
- 不提供未授权利用、持久化、规避检测或真实目标攻击步骤
- 对恶意样本和客户固件避免泄露敏感字符串或密钥
- 安全类能力默认只用于授权、防御、检测、加固、验证和报告；不提供未授权攻击、凭据窃取、持久化、规避检测、C2、钓鱼收集、数据外传或破坏性步骤。

## 为什么可以放心
- 先做静态结构，再决定动态验证
- 区分证据字符串、推断行为和已复现行为
- 输出工具版本、命令和可复现路径

## 典型使用方式
```text
使用 coff0xc-binary-mobile-iot 分析这个 APK 的权限、网络通信和 Frida hook 点。
使用 coff0xc-binary-mobile-iot 检查这个固件里的接口、密钥线索和协议风险。
Use coff0xc-binary-mobile-iot to triage this executable and summarize reverse engineering findings.
```


## 目标
在授权样本、实验室、CTF 或防御审计场景下分析低层系统风险，输出证据、修复、检测和安全验证。

## 适用场景
- 分析二进制、固件、移动应用、内核模块、工业协议、硬件接口、密码学实现或 CTF 题目。
- 做授权逆向、漏洞根因分析、修复建议、检测规则、测试向量和安全报告。
- 检查 APK/IPA 权限、固件配置、协议日志、危险函数、加密误用和常数时间风险。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-binary-mobile-iot ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 真实目标不提供利用链、绕过检测、越狱/root 绕过、设备接管或破坏 ICS 操作步骤。
- 不在生产工控、医疗、交通、电力等关键系统上执行主动测试。
- 移动/IoT 真实应用分析必须确认授权和隐私边界。

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
| 二进制/逆向 | 文件格式、strings、imports、CFG、危险函数、符号、反编译 | 定位行为和风险点。 |
| PWN/CTF | 栈/堆/格式化字符串/ROP 思路、靶场验证、writeup | 仅限 CTF/实验室。 |
| 内核安全 | 驱动接口、ioctl、权限边界、内存安全、eBPF/io_uring/nftables 风险 | 防御审计和修复。 |
| 移动安全 | APK/IPA manifest、组件导出、存储、网络、WebView、证书、日志 | 不做真实绕过攻击。 |
| IoT 固件 | binwalk、文件系统、配置、默认口令风险、启动脚本、更新签名 | 证据化固件审计。 |
| 硬件接口 | UART/JTAG/SPI/SWD 识别、调试暴露、防护建议 | 不指导未授权读取。 |
| ICS/OT | 协议、PLC/HMI、网络分区、安全监控、IEC 62443/NIST 800-82 | 被动分析优先。 |
| 密码学 | 算法选择、模式、随机数、密钥管理、认证、常数时间、测试向量 | 用标准和测试验证。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| reverse-engineering | 静态/动态逆向、反汇编、行为理解。 |
| binary-exploit | CTF/实验室二进制漏洞根因和防御修复。 |
| kernel-security | 内核/驱动/eBPF/ioctl 等低层边界审计。 |
| mobile-security | Android/iOS 应用安全审查和隐私边界。 |
| iot-security | 固件、硬件接口、设备云 API 和更新机制。 |
| ics-scada | 工业协议、PLC/HMI、OT 网络和安全分区。 |
| crypto-security | 密码学实现、协议和密钥管理审查。 |
| ctf | CTF 全栈题目分析和 writeup。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 授权与样本 | 确认样本来源、目标系统、实验环境、禁止动作和保密要求。 | 可合法分析。 |
| 静态优先 | 识别格式、元数据、字符串、imports、配置、权限、符号和危险函数。 | 低风险获得证据。 |
| 行为推断 | 基于代码、配置、日志、协议和测试环境推断行为。 | 假设可验证。 |
| 实验验证 | 只在 CTF/lab/自有设备执行最小验证；关键系统被动分析。 | 不伤害真实系统。 |
| 修复检测 | 输出补丁方向、配置加固、监控字段、测试向量和回归用例。 | 可落地。 |
| 报告 | 说明样本、工具、哈希、环境、发现、证据、限制和下一步。 | 可复查。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 连接硬件接口、读取固件、动态调试、hook 或运行样本前确认授权。
- 涉及 ICS/OT 真实环境时只做被动分析，主动测试需单独书面授权。
- 不输出真实应用绕过支付、反调试、证书 pinning 或 root/jailbreak 检测的攻击脚本。

## 验证清单
- 样本 hash、工具版本、分析环境和时间记录。
- 静态发现有文件路径、函数、偏移、配置项或权限证据。
- 密码学发现用标准、测试向量或常数时间分析支撑。
- 移动/IoT 修复用 manifest/config/代码 diff 或复测结果支撑。

## 反模式
- 没有授权就给设备/APP 攻击步骤。
- 只看 strings 就下最终结论。
- 在生产 ICS 上跑主动探测。
- 密码学审查只说使用 AES/RSA，不看模式、随机数和认证。

## 合并来源
- `binary-exploit`
- `crypto-security`
- `ctf`
- `ics-scada`
- `iot-security`
- `kernel-security`
- `mobile-security`
- `reverse-engineering`

## 本机相近 Skill
- `source-command-binary-exploit`
- `source-command-iot-ics`
- `source-command-mobile-security`
- `constant-time-analysis`
- `wycheproof`

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
