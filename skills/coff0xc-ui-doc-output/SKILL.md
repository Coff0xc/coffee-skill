---
name: coff0xc-ui-doc-output
description: "Use when / 当用户请求: 全面 UI 设计、前端体验、设计系统、视觉审美门禁、报告表达和技术翻译工作流。触发：UI、前端、frontend、web/app UI、dashboard、admin panel、SaaS screen、component、component variants、dense data table、filter builder、design system、semantic tokens、responsive、mobile-first、accessibility、ARIA、contrast、empty/loading/error states、hover/focus/keyboard、browser smoke、console cleanliness、screenshot、anti-AI aesthetic、视觉验证、页面很乱、信息密度、按钮状态、窄屏表现、产品可用性、反 AI 味、设计系统、状态门禁、可访问性、报告、technical report、executive delivery、executive report、section hierarchy、terminology consistency、报告叙事、高管交付、翻译、润色、交付文案、术语一致、报告层级、交付语言。正式 Office/PDF 文件交付如 PPT/PPTX、DOCX/Word、PDF、Excel/XLSX/CSV 优先使用 coff0xc-office-doc-tools。 Covered source aliases / 来源别名: UIdesign, quick-translate. Capability domains / 能力域: 产品 UI, 设计系统, 组件架构, 交互状态, 视觉验收, 报告输出, 翻译润色. If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-ui-doc-output."
---

# coff0xc-ui-doc-output

## 能力定位
面向 UI、前端体验、报告表达和技术翻译交付的产物质量能力。它不只润色文字，还要求界面、交互状态和报告叙事真实可用、可读、可验证。

正式 Office/PDF 文件产物，例如 PPTX、DOCX、PDF、Excel/XLSX/CSV 的创建、编辑、批注、公式和渲染验证，优先使用 `coff0xc-office-doc-tools`。

## 能交付什么
- 可用 UI/组件/页面改动或设计建议
- 桌面/移动端截图或浏览器 smoke 结果
- 报告结构、交付文案和版式建议
- 翻译润色稿、术语一致性和交付说明

## 可以接收什么输入
- 前端仓库、页面截图、设计稿、组件代码
- Markdown、报告草稿、翻译文本、截图、页面文案
- 用户反馈、移动端问题、可访问性或版式问题

## 放心使用的边界
- 可直接处理本地 UI 和文档产物
- 正式 PPTX/DOCX/PDF/XLSX/CSV 文件交付转入 `coff0xc-office-doc-tools`
- 下载外部资产、上传文档、发布网站、付费服务必须先确认
- 含个人信息或客户数据的内容要先确认脱敏要求
- 默认只处理本地、可逆、可验证的低风险工作；涉及生产、凭据、付费、远程写入、删除、发布或权限变更时必须先确认。

## 为什么可以放心
- 版式相关任务必须渲染或截图验证
- UI 覆盖 loading/empty/error/success 等状态
- 翻译不改变事实、数字、命令和路径

## 典型使用方式
```text
使用 coff0xc-ui-doc-output 优化这个 dashboard，并用截图检查移动端。
使用 coff0xc-ui-doc-output 把这份中文报告翻译润色成英文交付版。
Use coff0xc-ui-doc-output to polish the report narrative and UI copy for these findings.
```


## 目标
交付真实可用的界面和可读可验证的报告/翻译产物；视觉、交互、版式建议和语言质量都要检查。

## 适用场景
- 实现、改版、打磨 UI、dashboard、工具界面、表单、组件和交互状态。
- 改进报告结构、交付文案、翻译和技术表达。
- 需要截图、浏览器、渲染、版式或移动端响应式验证。

## 触发强化
- 自动触发主要依赖本文件 frontmatter 的 `description`；本 skill 已把中文、英文、工具名、来源别名和常见缩写写入 `description`。
- 如果没有自动触发，手动写：`使用 coff0xc-ui-doc-output ...`。
- 如果用户只写了宽泛主题，可先用 `coff0xc-skill-router` 路由到本 skill。

## 不适用场景
- 不要把应用需求做成营销 landing，除非用户明确要求。
- 不要只靠文本检查 PDF 或 UI；版式相关必须渲染或截图验证。
- 不确定术语时标注并保持原文关键术语。

## 执行原则
- 先读取项目文件、配置、调用点、现有风格和可用工具，再下结论或改文件。
- 把用户目标转成可验证的完成标准；不确定但低风险的细节记录为假设并继续推进。
- 涉及当前事实、版本、CVE、云服务、GitHub 状态、价格、外部 API 或论文时，查真实来源并标注证据等级。
- 涉及代码改动时保持最小正确改动，优先使用现有框架、脚本、测试和本地工具。
- 只有真实运行过的命令、测试、构建、扫描或人工检查才能写成已验证。
- 涉及删除、远程写入、生产、凭据、付费、push、PR/Issue、CI/CD、权限或基础设施变更时，先拿到明确授权。

## 设计质量门禁
本 skill 借鉴高星 UI/agent skill 和成熟前端仓库的共同做法：先把产品任务、设计系统、组件状态、可访问性和浏览器验收绑定在一起。目标不是“更好看一点”，而是交付像真实产品团队会合并的界面。

### UI Need Package
做任何实质 UI 设计、实现或重做前，先压缩成一个可执行包。小任务可在心里完成，大任务要写进计划或回复：

| 字段 | 必须回答的问题 |
| --- | --- |
| 用户和任务 | 谁在用，第一屏要支持什么主要工作。 |
| 产品类型 | SaaS/admin、analytics/dashboard、editor/tool、consumer/landing、e-commerce、design system、game/interactive、report/translation。 |
| 信息优先级 | 主要对象、主动作、次动作、导航、空/错/加载状态。 |
| 设计系统 | 现有 tokens、组件、图标、字体、颜色、spacing、radius、shadow、motion。 |
| 数据和状态 | populated、empty、loading、error、disabled、success、long-content、missing-asset。 |
| 验收标准 | 要跑哪些静态检查、截图/浏览器视口、交互 smoke 和剩余风险说明。 |

### 产品类型路由
不要把所有界面都做成同一种 landing 或卡片墙。先选产品类型，再定默认密度和视觉语言：

| 类型 | 默认方向 | 常见误区 |
| --- | --- | --- |
| SaaS / CRM / admin / ops | 安静、密集、可扫描，表格/筛选/表单/批量操作优先。 | 做成营销 hero、过度插画、信息太松。 |
| Analytics / dashboard | 单位、时间范围、过滤器、异常状态和图表可读性优先。 | 指标卡堆叠、图表无轴/无单位、颜色只为装饰。 |
| Editor / tool | 工作区优先，稳定 toolbar、快捷操作、空/错/保存状态明确。 | 先做品牌介绍页，或让工具藏在第二屏。 |
| Consumer / landing | 第一视口必须立刻表达产品/品牌/对象，使用真实或可溯源视觉资产。 | 纯渐变背景、虚假 stock 图、价值主张空话。 |
| E-commerce / product | 产品可检查、价格/变体/库存/购买路径清楚。 | 图片暗、裁切过度、CTA 和规格被装饰淹没。 |
| Design system / component library | tokens、variants、states、accessibility notes、examples 和 regression path。 | 只有静态样式，没有组件契约。 |
| Game / interactive | 反馈、动效、状态机、规则/物理引擎和可玩性优先。 | 只做漂亮封面，没有真实交互。 |
| Report / translation | 信息层级、证据、术语一致、交付语气。 | 只润色句子，不保留证据和不确定性。 |

### 设计系统与组件门禁
- 先查现有设计系统：`tailwind.config.*`、CSS variables、theme/tokens、component library、Storybook、icons、screenshots、README/AGENTS/DESIGN 文档。
- 优先使用 semantic tokens 和现有 variants；不要在组件里随手写 raw color、magic spacing、一次性 class pile，除非项目本来就是这种风格。
- 引入图标、动画、状态管理或 UI 库前先查依赖文件；没有依赖就不要假装能 import。
- 组件优先组合而不是巨型配置对象；数据获取和展示分离；可复用状态抽到 hook，但不要为单一页面过度抽象。
- 组件必须有明确状态契约：输入、输出、交互、错误、disabled、focus、响应式和长内容行为。
- 对 shadcn/Radix/MUI/Ant/自研组件，只继承其可访问性和结构，不要保留默认模板味；radius、颜色、shadow、density 要匹配当前产品。

### 状态与可访问性门禁
用户可见 UI 不能只做 happy path。相关场景至少检查：

- populated：真实内容长度、真实数字、真实对象名，不用 Lorem ipsum、John Doe、Acme、99.99% 这类假质感占位。
- empty：告诉用户下一步能做什么，不留空白区域。
- loading：内容型区域优先 skeleton 或结构化占位，不用一个孤立 spinner 顶替整页。
- error：错误在发生位置附近说明，可重试；不要只 `alert()` 或吞错。
- disabled / unavailable：说明原因或让状态可理解。
- hover / active / selected / focus：鼠标和键盘路径都能看出当前元素。
- small-screen / long-content：320px、768px、1024px、1440px 或项目常用断点内不溢出、不遮挡。
- accessibility：语义标签、label、alt、aria-name、focus order、对比度、触摸目标、reduced-motion、图表不能只靠颜色。

### 反 AI 味视觉门禁
以下是常见 AI 生成痕迹，发现就优先改：

- 紫蓝霓虹、过度 glow、任意渐变文字、纯黑背景、单一色相统治全页。
- 三列等宽 feature cards、卡片套卡片、每个区块都是圆角白卡、无意义 bento。
- 过大 hero 字、居中大标题加两按钮的模板式首屏，尤其对工具/admin/dashboard。
- 所有内容都均匀、对称、等高、等距，没有主次和扫描路径。
- 用图标替代真实产品/数据/状态；图片暗、糊、裁切到无法检查对象。
- 表单没有 label/helper/error；按钮文字溢出；表格列宽不随内容设计。
- 动效用 `top/left/width/height` 或频繁 React state 驱动连续动画；应优先 transform/opacity，并尊重 reduced-motion。
- 页面要靠可见说明文字解释怎么用，说明交互本身没做好。

### 浏览器验收门禁
- UI 代码改动后，能启动本地服务就启动；能静态打开就给本地 HTML 路径。
- 至少检查一个桌面和一个移动视口；复杂工具再加窄屏/平板宽度。
- 看 console、网络资源、空白渲染、重叠、裁切、文本溢出、按钮可点性、表单基本路径、焦点状态。
- Canvas/WebGL/Three.js 必须检查非空像素、场景 framing、移动/交互是否可见。
- 如果浏览器或截图不可用，最终必须写明“代码已改但未做视觉验收”，不能说 UI 已验证。

### 质量 Eval 自测
当用户要求“确认 skill 是否真的好用”“优化 UI skill”“不要只堆触发词”时，不要只改描述。优先用仓库内质量夹具校准：

- 参考 `evals/quality/cases/ui-admin-dashboard-visual-gate/`：输入是典型 AI 味 dashboard，合格输出必须有 `output/index.html`、`screenshots/desktop.png`、`screenshots/mobile.png` 和 `evaluation-notes.md`。
- `evaluation-notes.md` 要能证明：UI Need Package、产品类型路由、设计系统、状态覆盖、可访问性、浏览器验收和剩余限制。
- 运行 `python .\scripts\run_quality_eval.py` 检查夹具完整性；有真实 agent 输出时运行 `python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses` 评分。
- 质量 eval 通过不等于审美一定满分；它只证明产物没有跳过关键门禁。需要最终截图和人工 taste review 时要明说。

## 能力矩阵
| 能力域 | 覆盖范围 | 执行要点 |
| --- | --- | --- |
| 产品 UI | SaaS、CRM、admin、dashboard、工具、编辑器、游戏/互动体验 | 第一屏就是可用体验。 |
| 设计系统 | 组件、间距、密度、状态、图标、颜色、响应式、可访问性 | 跟随已有设计语言。 |
| 交互状态 | loading、empty、error、success、disabled、focus、hover、keyboard | 关键流程完整。 |
| 视觉验证 | 浏览器、截图、移动/桌面、文本溢出、布局重排、资产加载 | 不凭想象说好看。 |
| 报告输出 | 安全报告、技术报告、交付说明、变更摘要 | 结构清晰、证据可追溯。 |
| 翻译润色 | 中英互译、术语一致、技术语气、保留代码/命令/路径 | 不改动事实和数字。 |

## 子域路由
| 来源 skill | 并入后的处理方式 |
| --- | --- |
| UIdesign | UI/前端体验、视觉打磨、响应式和浏览器验证。 |
| quick-translate | 技术翻译、报告翻译、术语统一和简洁润色。 |
| coff0xc-office-doc-tools | PPTX/DOCX/PDF/XLSX/CSV 等正式文件交付、批注、公式和渲染验证。 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 上下文采集 | 看现有路由、组件、样式系统、截图、资源和目标用户。 | 知道要匹配的产品语气。 |
| 体验建模 | 列核心流程、信息层级、状态、输入输出和边界案例。 | 界面不是装饰图。 |
| 实现/编辑 | 复用组件和图标，稳定尺寸，避免嵌套卡片和文本溢出。 | 功能可用。 |
| 视觉验证 | 启动本地服务或打开文件，做桌面/移动截图和交互 smoke。 | 发现并修复重叠/空白/溢出。 |
| 报告检查 | 报告结构、链接、图像、术语和敏感信息检查；正式文件渲染转入 `coff0xc-office-doc-tools`。 | 交付物可读。 |
| 交付说明 | 说明输出路径、验证方式和剩余风险。 | 用户能直接使用。 |

## 证据等级
- 已验证：本地命令、测试、构建、源码、配置、日志、官方资料或可复现数据支持。
- 高可信：多个可靠来源一致，但当前环境没有完整复现。
- 推断：基于已验证事实的合理判断，需要后续验证。
- 未验证：尚未确认，不能作为最终结论。
- 未知：资料不足，需要补充输入或授权。

## 硬门禁
- 需要下载外部资产、使用付费服务、发布网站或上传文档前确认。
- 处理包含个人信息或客户数据的文档时，先确认脱敏要求。
- 自动替换全文术语或批量改 PDF 前，保留原件并说明策略。

## 验证清单
- UI：浏览器打开、截图、移动/桌面、关键按钮和表单流程。
- Office/PDF：如需交付 PPTX/DOCX/PDF/XLSX 文件，使用 `coff0xc-office-doc-tools` 的文件级验证清单。
- 翻译：术语表、数字/单位/引用/代码不变、语气一致。
- 报告：证据链接、文件路径、行号和风险等级一致。

## 反模式
- 用大段文字解释怎么用界面，而不是做出可用控件。
- 所有界面都做成同一种卡片/渐变风格。
- 把正式 Office/PDF 文件产物留在本 skill 内粗略处理，而不使用 `coff0xc-office-doc-tools` 的文件级验证。
- 翻译时改变事实、弱化不确定性或丢失技术术语。

## 合并来源
- `UIdesign`
- `quick-translate`

## 本机相近 Skill
- `UIdesign`
- `source-command-quick-translate`
- `coff0xc-office-doc-tools`

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
