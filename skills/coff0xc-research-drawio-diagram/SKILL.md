---
name: coff0xc-research-drawio-diagram
description: "Use when / 当用户请求: 科研算法架构图、论文方法图、论文级模型结构图、模型结构图、实验流程图、draw.io、diagrams.net、.drawio 可编辑文件、算法 pipeline、method figure、architecture figure、paper figure、model diagram、model structure、research workflow、arXiv、official GitHub、科研绘图、论文配图、神经网络结构、Transformer/CNN/GNN/diffusion/RAG/agent 架构图。Requires public-source analysis before drawing: paper, arXiv, official repo, docs, method section, equations, ablation, benchmark, or user-provided sources. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-research-drawio-diagram."
---

# coff0xc-research-drawio-diagram

## 能力定位
面向论文、算法、模型和研究流程的可编辑 draw.io 图生成能力。重点是交付可继续编辑的 `.drawio` 源文件，并把图中元素和公开证据对应起来。

## 能交付什么
- 可编辑 `.drawio` 文件
- 图结构 JSON/spec 或模块清单
- 证据表：论文段落、公式、图号、代码路径、官方文档
- 未确认推断边和不确定项说明

## 可以接收什么输入
- 论文 PDF/arXiv/OpenReview、官方 GitHub、项目文档
- 模型结构、算法 pipeline、实验流程、训练/推理说明
- 已有草图、截图、Mermaid 或图形要求

## 放心使用的边界
- 可直接基于用户材料和公开来源整理图
- 需要联网查论文/仓库时标注来源和证据等级
- 不把推断连接伪装成论文原文事实
- 默认只处理本地、可逆、可验证的低风险工作；涉及生产、凭据、付费、远程写入、删除、发布或权限变更时必须先确认。

## 为什么可以放心
- 优先生成 draw.io 可编辑源文件，不只给 PNG/Mermaid
- 图中关键模块要能追溯到证据
- 训练路径、推理路径和指标分层标注

## 典型使用方式
```text
使用 coff0xc-research-drawio-diagram 根据论文和官方 GitHub 画一个可编辑 draw.io 方法图。
使用 coff0xc-research-drawio-diagram 把 Transformer 论文方法整理成 .drawio 模型结构图。
Use coff0xc-research-drawio-diagram to create an editable diagrams.net method figure with evidence notes.
```


## 目标
把科研算法、论文方法、模型结构或实验流程转成可编辑的 diagrams.net/draw.io `.drawio` 架构图。先基于公开来源或用户提供材料做结构分析，再画图；不要凭记忆编造模块、连接或创新点。

## 适用场景
- 用户要求画科研算法架构图、论文方法图、模型 pipeline、实验流程、系统框架或对比图。
- 用户明确要求 draw.io、diagrams.net、`.drawio`、可编辑 XML、论文配图、method figure、architecture figure。
- 需要把论文、arXiv、官方 GitHub、README、代码目录、公式、消融实验或已有草图转成结构化图。
- 需要输出可编辑源文件，而不只是 Mermaid、PNG 或文字描述。

## 不适用场景
- 纯代码依赖图、调用图、类图优先用代码图/Trailmark 类 skill。
- 只需要简单 ASCII/Mermaid 草图且不要求 draw.io 时，不必生成 `.drawio`。
- 没有来源、也不允许联网或提供材料时，只能输出“待确认草图”，不得声称是论文真实结构。

## 公开来源要求
优先使用这些证据，按可靠度排序：

1. 用户提供的论文 PDF、方法章节、图表、公式、补充材料。
2. 官方论文页、arXiv、OpenReview、ACL Anthology、IEEE/ACM/Springer 页面。
3. 官方 GitHub/项目主页、模型卡、文档、demo。
4. 高可信综述、Papers with Code、公开 benchmark 页面。
5. 其他博客/教程只能作为辅助，不得覆盖原论文。

涉及当前论文、最新模型、仓库结构、benchmark 或 API 时必须查公开来源并标注证据等级。

## draw.io 约束
- 默认输出 `.drawio`，也可输出 `.xml`。draw.io/diagrams.net 的可编辑图本质是 XML；`.drawio` 是常见文件扩展名。
- 需要可编辑交付时优先保存 `.drawio` 源文件；PNG/SVG/PDF 只作为预览或投稿导出。
- 如果导出 PNG/SVG/PDF，尽量保留 embedded diagram data，方便之后继续编辑。
- 可以先用 Mermaid/表格整理逻辑，但最终必须生成 draw.io 可编辑文件。
- 如果本地没有 draw.io Desktop，不要假称已导出 PNG/PDF；只说已生成 `.drawio`，用户可用 app.diagrams.net 或桌面版打开。

## 执行原则
- 先抽取算法事实，再画图：任务、输入、输出、模块、数据流、训练/推理差异、损失函数、评估、创新点。
- 图必须服务论文表达：读者应该能一眼看出“问题、方法主线、关键模块、信息流和贡献点”。
- 复杂图分层：总览图、模块展开图、训练流程图、推理流程图、消融/对比图不要硬塞一张。
- 术语保留论文原名；缩写首次出现写全称。
- 图中每个核心模块都要能追溯到来源段落、公式、图号、代码路径或公开文档。

## 输出产物
至少交付：

- `.drawio` 文件路径。
- 图结构说明：模块、边、分组、颜色含义。
- 证据表：每个关键模块对应来源。
- 未确认项：哪些连接或命名是推断。
- 打开/编辑说明：用 diagrams.net/draw.io 打开 `.drawio`。

可选交付：

- JSON spec：供 `scripts/build_drawio.py` 复现。
- Mermaid 草图：用于快速审阅，不替代 `.drawio`。
- PNG/SVG/PDF 预览：仅在本地工具可用并真实导出后声明。

## 工作流

| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 需求定界 | 确认图类型、目标读者、论文 venue、页面比例、输出路径和是否要多页。 | 知道画什么、不画什么。 |
| 来源分析 | 读取用户材料；必要时查公开论文、官方 repo、文档、图表和公式。 | 每个核心结构有证据。 |
| 结构抽取 | 列输入、编码器/核心算法/解码器、训练目标、推理路径、数据集、指标和创新点。 | 可转成节点和边。 |
| 图稿设计 | 选择布局：left-to-right pipeline、top-down hierarchy、swimlane、loop、multi-page。 | 信息层级清晰。 |
| 生成 draw.io | 用 `scripts/build_drawio.py` 或直接写 `.drawio` XML。 | 文件可被 draw.io 打开编辑。 |
| 自检 | 检查 XML、节点标签、连接方向、证据表、未确认项。 | 不伪造、不漏关键模块。 |
| 交付 | 给出文件路径、证据、验证和下一步。 | 用户能打开和修改。 |

## 推荐图型

| 图型 | 适用 | 布局 |
| --- | --- | --- |
| Algorithm pipeline | 输入到输出、端到端方法 | 左到右 |
| Model architecture | 神经网络/模块层级 | 分组 + 子模块 |
| Training vs inference | 训练和推理路径不同 | 双泳道 |
| Data flow | 数据处理、特征、检索、缓存 | 左到右或上到下 |
| Loss/evaluation | 多损失、多指标、多 benchmark | 辅助区块 |
| Paper contribution map | 创新点和 baseline 对比 | 中心模块 + 对比旁注 |

## JSON Spec 约定
优先用 `scripts/build_drawio.py` 生成 `.drawio`。输入 JSON 结构：

```json
{
  "title": "Model Architecture",
  "pages": [
    {
      "name": "Overview",
      "nodes": [
        {"id": "input", "label": "Input", "type": "data", "x": 40, "y": 120},
        {"id": "encoder", "label": "Encoder", "type": "module", "x": 240, "y": 120}
      ],
      "edges": [
        {"source": "input", "target": "encoder", "label": "features"}
      ]
    }
  ]
}
```

常用 `type`：`data`, `module`, `algorithm`, `model`, `loss`, `evaluation`, `output`, `claim`, `note`, `source`。

## 证据表格式

```markdown
| 图中元素 | 来源 | 证据等级 | 备注 |
| --- | --- | --- | --- |
| Encoder | Paper Section 3.1 / official repo module path | 已验证 | 原文模块名 |
| Retrieval cache | README / code path | 已验证 | 推理路径 |
| Feedback edge | 推断 | 推断 | 需要用户确认 |
```

## 验证清单
- `.drawio` 是 XML 文件，包含 `<mxfile>` 和 `<mxGraphModel>`。
- 节点 ID 唯一；边的 source/target 都存在。
- 连接方向符合论文方法，不反向。
- 训练路径、推理路径、loss、evaluation 没混在一起。
- 图中未确认内容已标注为推断。
- 没有把公开论文外的信息写成已验证事实。

## 反模式
- 只根据模型名画“常见架构”，没有来源证据。
- 把论文图复制成低分辨率图片，而不是可编辑结构图。
- 所有模块同一颜色，读者分不出 data/model/loss/eval。
- 一张图塞满所有细节，导致论文排版不可用。
- 声称已导出 PNG/PDF，但实际只生成了 `.drawio`。

## 输出合同

```markdown
完成：
- ...

证据：
- [已验证/高可信/推断/未验证/未知] ...

文件：
- ...

验证：
- ...

未确认项：
- ...

下一步：
- ...
```
