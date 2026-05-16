# coffee-skill 中文参考

## 这是什么

`coffee-skill` 是一套面向 Codex 的技能包，覆盖软件工程、AI Agent/RAG、API/数据库、UI/报告输出、Office/PDF 文件交付、防御安全、检测响应、漏洞管理、身份安全、云与 DevSecOps、区块链安全、合规架构等工作流。

## 为什么写这个

- 原始 skill 太分散，类似任务容易触发错误 skill，甚至完全不触发。
- 很多客户端主要根据 `SKILL.md` 的 frontmatter `name` 和 `description` 选择 skill，正文内容通常要触发后才会加载。
- 安全类 skill 如果没有边界，容易从防御审查滑向未授权攻击步骤。
- 工程任务需要可验证流程，而不是只给建议。

## 好在哪里

- 将 91 个来源 skill 和工作流整合为 17 个综合能力 skill，并提供 1 个路由 skill，减少碎片化。
- 增加 `coff0xc-skill-router` 作为自动触发失败时的兜底路由。
- 每个 skill 都包含适用场景、不适用场景、能力矩阵、阶段流程、证据等级、硬门禁、验证清单和反模式。
- 安全相关内容默认用于授权、防御、检测、加固、复盘和报告。
- 发布目录包含 README、LICENSE、NOTICE、SECURITY、来源说明、脱敏说明和校验脚本。

## 怎么用

自然提问即可：

```text
帮我审计这个项目的 Web/API 安全问题
用 Agent/RAG 的方式设计一个本地知识库助手
检查这个 K8s 和 CI/CD 配置有没有供应链风险
```

如果没自动触发，手动点名：

```text
使用 coff0xc-skill-router 帮我选择合适 skill
使用 coff0xc-ai-agent-rag 设计一个 RAG Agent
使用 coff0xc-secure-code-appsec 审计这个项目
使用 coff0xc-cloud-devsecops 检查 K8s 和 CI/CD
使用 coff0xc-detection-response 写检测规则
```

## 能在哪里用

- 本地 Codex skill 目录。
- 兼容 `SKILL.md` 文件夹格式的客户端。
- 日常工程、AI 系统、Office/文档文件交付、防御安全、安全运营、漏洞管理和培训实验环境。

## 触发失败怎么办

1. 确认 skill 文件夹名和 frontmatter `name` 一致。
2. 复制后重启或刷新 Codex。
3. 删除重复 skill 名称。
4. 用 `coff0xc-skill-router` 兜底。

## 安全边界

只用于你拥有或明确授权的资产、代码、日志、样本、实验环境和培训环境。不用于未授权访问、凭据窃取、持久化、规避、C2、钓鱼收集、数据外传或破坏性动作。
