---
name: coff0xc-office-doc-tools
description: "Use when / 当用户请求: 正式 Office 和文件型交付物能力，覆盖 PowerPoint/PPT/PPTX/slides/deck、Word/DOCX/document/redline/comment、PDF/read/create/review/render、Excel/XLSX/CSV/spreadsheet/workbook/chart/formula。适合创建、编辑、检查、转换、批注、渲染验证和导出可交付文件。可交付：可编辑 PPTX、DOCX、PDF、XLSX/CSV、图表、批注/修订、公式检查、渲染截图/预览 QA、文件路径和验证说明。触发：ppt、pptx、powerpoint、slides、deck、docx、word、redline、track changes、comments、pdf、excel、xlsx、csv、spreadsheet、workbook、chart、formula、table、render、export、office、文档、演示文稿、幻灯片、表格、工作簿、公式、批注、修订、版式、导出、可编辑文件。If this skill does not auto-trigger, user can manually invoke: 使用 coff0xc-office-doc-tools."
---

# coff0xc-office-doc-tools

## 能力定位
面向 PowerPoint、Word、PDF、Excel/CSV 这类正式文件交付的 Office 文档工具能力。它解决的不是“写一段内容”，而是把内容做成别人能打开、能编辑、能审阅、能打印、能继续使用的文件。

这个 skill 适合用户说“帮我做一份 PPT / 改一个 DOCX / 检查 PDF / 处理 Excel / 生成可交付文件”的场景。它会把产物质量放在第一位：文件要存在、内容要对、格式要稳、公式要算、版式要看过，不能只凭文本猜测就说完成。

## 能交付什么
- 可编辑 `.pptx` 演示文稿：页面结构、图表、表格、图片、讲述逻辑、导出检查和预览 QA。
- 可编辑 `.docx` 文档：报告、方案、SOP、合同草稿、批注、修订、表格、目录、页眉页脚、元数据清理建议。
- `.pdf` 阅读、审阅、生成或检查：页面渲染、文字提取、版式问题、页码、表格、图片和引用检查。
- `.xlsx` / `.csv` / `.tsv` 工作簿：数据清洗、公式、透视/汇总、图表、仪表盘、条件格式、校验列和导出文件。
- 交付说明：最终文件路径、验证方式、未验证原因、剩余风险和建议的人工复核点。

## 可以接收什么输入
- 现有 PPTX、DOCX、PDF、XLSX、CSV、TSV、Markdown、图片、截图、网页导出的表格。
- 用户给的文字大纲、会议纪要、报告草稿、审计发现、实验数据、财务/运营数据、品牌要求或模板文件。
- 批注要求、改写要求、格式要求、目标受众、页数限制、打印/展示/归档用途。
- 多个来源文件，例如“把 PDF 数据整理到 Excel，再做一页 PPT 摘要”。

## 放心使用的边界
- 可直接处理本地、可逆、可检查的文件创建、编辑、转换、分析和格式整理。
- 不上传用户文档到外部服务，不调用付费生成/转换服务，不发布或发送文件，除非用户明确确认。
- 含个人信息、客户数据、合同、财务、医疗、身份信息或内部资料时，先确认脱敏、保留范围和输出目录。
- 不伪造来源、签名、印章、审计结论、法律意见、财务真实性或官方认证。
- 修改现有文件时默认保留原件，输出新文件；批量覆盖、删除、接受所有修订、清空批注或移除水印前必须确认。
- 默认只处理本地、可逆、可验证的低风险工作；涉及生产、凭据、付费、远程写入、删除、发布或权限变更时必须先确认。

## 为什么可以放心
- 文件型交付必须有“文件存在 + 内容检查 + 视觉/结构验证”的证据链。
- PPT/DOCX/PDF 不能只靠文本抽取判断质量；版式任务要渲染或预览检查。
- Excel/XLSX 不能只看表面格式；关键公式、引用范围、错误值和图表来源要检查。
- 现有文件编辑采用最小改动原则，保留结构、样式和原始文件，避免不可追踪覆盖。
- 最终回复区分“已验证”“未能验证”和“需要人工复核”，不把未运行的检查说成通过。

## 典型使用方式
```text
使用 coff0xc-office-doc-tools 把这份 Markdown 做成可编辑 PPTX，包含图表、讲述逻辑和预览验证。
使用 coff0xc-office-doc-tools 给这个 DOCX 加批注和修订，不覆盖原件，最后渲染检查版式。
Use coff0xc-office-doc-tools to turn this CSV into a formatted Excel workbook with formulas, charts, and a formula error scan.
Use coff0xc-office-doc-tools to review this PDF report for layout, missing pages, broken tables, and export-ready issues.
```

## 目标
交付正式、可打开、可编辑、可检查的 Office/PDF 文件。默认把“用户能直接拿去汇报、审阅、归档或继续编辑”作为完成标准。

## 适用场景
- 创建或优化 PowerPoint/PPTX、slides、deck、演示文稿。
- 创建、编辑、批注、修订、格式化 DOCX/Word 文档。
- 阅读、生成、审阅、拆分、合并或检查 PDF。
- 创建、清洗、分析、格式化 Excel/XLSX/CSV 工作簿、图表和公式模型。
- 跨文件流：PDF 提取到 Excel、Excel 图表进 PPT、DOCX 报告导出 PDF、PPT 摘要来自 Word/Excel。

## 和相邻 skill 的分工
| 场景 | 优先使用 |
| --- | --- |
| 前端页面、组件、dashboard、浏览器 UI | `coff0xc-ui-doc-output` |
| 正式 PPTX/DOCX/PDF/XLSX 文件创建、编辑、渲染验证 | `coff0xc-office-doc-tools` |
| 论文算法图、模型结构图、`.drawio` 源文件 | `coff0xc-research-drawio-diagram` |
| 代码生成或仓库功能开发 | `coff0xc-software-engineering` |

如果一个任务同时包含 UI 和 Office 文件，先判断最终交付物：最终是网页/应用就走 UI；最终是 PPT/DOCX/PDF/XLSX 就走本 skill。

## 执行原则
- 先确认输出格式、用途、受众、文件来源、是否要保留原件、是否包含敏感信息。
- 能使用结构化工具就不用脆弱字符串拼接；表格、公式、段落、幻灯片对象和 OOXML 都应尽量结构化处理。
- 新建文件要有清晰信息架构；编辑现有文件要尽量局部修改，不无故重排全文。
- 每轮重大改动后做对应验证；验证失败先修，不把瑕疵隐藏在最终回复里。
- 最终只交付用户要的文件；预览图、临时脚本、提取文本、QA 中间产物除非用户要求，不作为主交付物。

## PPT 审美门禁
适用于新建、重做、优化或对标参考 deck 的 PPT/PPTX 任务。目标不是“能打开”，而是交付有编辑价值、审美可信、叙事清楚的演示文稿。

- 先写 claim spine：每个非附录页必须有一句结论型标题、一个主证明对象、必要来源或数据说明。标题如果换个公司名还能用，就继续收紧。
- 先锁 design system：页面尺寸、背景、字体层级、色彩用途、图表语法、图示/连接线语法、页脚/来源、标题/kicker 规则、允许的版式族和禁用 motif。
- 做 contact-sheet 规划：10 页 deck 至少 5 种宏观版式；不能连续 3 页同构；不要默认卡片网格、装饰框、模板化 dashboard 或营销空话。
- 图表和图示要证明标题：优先直接标签，少用沉重 legend；线、箭头、连接器、容器和标签必须在渲染后仍表达同一个关系。
- 品牌和素材必须有来源：不要手画或仿造 logo、吉祥物、产品 UI、客户标志；无法验证就用排版、颜色、产品语言和已知数据表达品牌感。
- 必须做 rendered QA：渲染整套 slide 或 contact sheet，检查缩略图节奏、全尺寸文字溢出、图表可读性、图片清晰度、来源页脚、KPI/legend/连接线完整性。
- 用 comeback scorecard 判断是否能交付：story、specificity、rhythm、whitespace、chart clarity、typography、restraint、precision、coherence 都不能有明显短板。发现弱页时，优先重构最弱的 2-4 页，而不是只做微调。
- 如果只能做到“功能可用但审美未达标”，最终必须明确说清剩余弱点，不能把有文件输出等同于高质量 deck。

## Excel 数据解析门禁
适用于 CSV/TSV/XLSX 导入、清洗、分析、建模、dashboard、图表和公式工作簿。目标是可审计、可计算、可继续编辑，而不是漂亮表格截图。

- 读取前先判断数据形态：来源文件、编码/分隔符、表头、单位、日期/数字格式、空值、重复行、异常值、是否已有公式/表格/图表/筛选/条件格式。
- 导入现有 workbook 先做 compact inspect：列出 sheet、used range、关键表格、公式区域、样式和图表；不要盲目全表重排或覆盖格式。
- CSV/TSV 优先用结构化解析；需要清洗时保留可审计中间逻辑，避免手写脆弱 split。多来源数据要保留 source/assumptions 或 raw/detail sheet。
- 分析型 workbook 默认结构：Executive Summary 或 Dashboard 在前，Source/Assumptions 其次，Model/Detail/Checks 在后；简单 tracker 可简化，但仍要有清晰标题、表头和输入区。
- 派生结果优先用公式：不要硬编码关键计算；公式不要藏魔法数字，引用输入/假设单元格；避免整列引用，使用有边界的范围；跨 sheet 公式要先创建目标 sheet。
- 可疑关键输出要 trace 或等价审计：检查依赖链、公式范围、单位、百分比、日期和汇总口径。模型完整性依赖 linked calculation 时，加 Checks 区或 Checks sheet。
- 图表必须有明确数据源：用 helper range 组织 chart-ready 数据，必要时用公式链接源数据；图表不能盖住数据，轴单位/格式/标签必须可读。
- 必须验证：inspect 关键 ranges 的 values/formulas，扫描 `#REF!`、`#DIV/0!`、`#VALUE!`、`#NAME?`、`#N/A`，渲染关键 sheet/range，检查空白图表、截断标题/数字、列宽、冻结窗格、筛选、表格和条件格式。
- 如果用户只是问表格内容问题，不要擅自改文件；先读值/公式/表结构并回答。

## DOCX 阅读与格式门禁
适用于 DOCX/Word 的阅读、审阅、改写、批注、修订、格式化和生成。目标是理解文档结构并保持可读格式，不是只抽文本。

- 阅读 DOCX 先分层理解：章节/标题层级、页数、段落类型、表格/图片/脚注/页眉页脚、批注、修订、目录、交叉引用、字段和元数据线索。
- 版式结论不能只靠文本抽取或 XML：交付前必须尽量渲染页面并逐页检查；如果渲染不可用，只能声明完成了结构/文本检查，不能声称版式通过。
- 新建或大改 DOCX 先选文档 archetype/preset：memo、report、SOP、proposal、form、manual、brief 等；确定页面、边距、字体、标题层级、段落节奏、列表、表格、callout、页眉页脚和颜色 token。
- 使用真实 Word 结构：标题用 styles，列表用真实 numbering，表格用明确列宽/单元格 padding/重复表头；不要用假标题、手打项目符号、手动编号或表格包装普通长段落。
- 表格必须通过 table gate：只有真实行列数据才用表；句子型/段落型内容应改成段落、bullet、step、callout 或定义列表。表格要检查列宽、换行、垂直/水平对齐、边距、caption、分页和重复表头。
- 编辑现有 DOCX 默认保留原件并最小局部修改。批注要锚定在具体位置；修订/接受修订/删除批注/清理元数据/去水印前必须确认。
- 评论和修订要双重验证：渲染可能显示 tracked changes，但常常不显示 comments；需要结构检查 comments.xml、anchors、rels、content-types 或等价证据。
- 每个有意义的编辑批次后重新渲染或结构复查，重点看 clipping、overlap、missing glyphs、broken tables、spacing drift、header/footer 错位、页码和目录异常。
- 最终必须区分：已读懂的内容结构、已修改的范围、已验证的页面/结构、未能验证的版式风险。

## 质量 Eval 自测
当用户要求“确认 Office skill 是否真的好用”“优化 PPT/Excel/DOCX 质量门禁”“不要只堆触发词”时，用仓库内 artifact-level 夹具校准：

- `evals/quality/cases/office-ppt-aesthetic/`：检查 claim spine、design-system lock、contact-sheet plan、comeback scorecard、render evidence 和最终 PPTX。
- `evals/quality/cases/office-excel-parse/`：检查 messy CSV/workbook notes 的编码/分隔符/表头/单位/日期/空值/重复/异常审计、Raw/Source/Assumptions/Model/Checks/Dashboard 结构、公式/trace/error scan/helper range 和 dashboard render evidence。
- `evals/quality/cases/office-docx-format/`：检查 reading map、style/token map、minimal edit plan、comment/redline anchors、真实 styles/numbering/table geometry 和 page render evidence。
- 运行 `python .\scripts\run_quality_eval.py` 默认评分 `evals/quality/golden-responses/` 的真实产物：PPTX 会解包检查 slide XML/text shapes/chart parts/layout signatures，XLSX 会检查 sheets/tables/charts/formulas 并重算支持范围内的关键公式，DOCX 会检查 comments、anchors、tracked changes、styles、numbering、table geometry、rels、headers/footers 和 fields。
- 只想检查 prompt/input/assertion schema 时运行 `python .\scripts\run_quality_eval.py --fixture-only`；有真实 agent 输出时运行 `python .\scripts\run_quality_eval.py --responses-dir .\evals\quality\responses`。
- 质量 eval 通过不等于 Office 文件已经人工验收；PPT 审美、Excel 完整公式引擎和 DOCX 逐页版式仍需要对应工具渲染或人工复核。

## 能力矩阵
| 文件类型 | 典型能力 | 验证重点 |
| --- | --- | --- |
| PPT/PPTX | 新建 deck、重做结构、改模板、加图表/表格/图片、压缩故事线 | 幻灯片数量、可编辑对象、预览图、文字不溢出、图表/图片清晰 |
| DOCX/Word | 报告、方案、SOP、批注、修订、目录、表格、页眉页脚 | 原件保留、结构未破坏、批注/修订锚点、渲染页面、表格不截断 |
| PDF | 阅读、审阅、生成、拆分/合并、版式检查、引用检查 | 页数、页面渲染、文字提取对照、表格/图片/页码、不可编辑限制 |
| Excel/XLSX/CSV | 数据清洗、公式、汇总、图表、dashboard、模板、校验 | 公式错误扫描、关键范围 inspect、图表来源、列宽/冻结/格式 |

## 工作流
| 阶段 | 动作 | 完成标准 |
| --- | --- | --- |
| 任务定界 | 明确最终格式、输入文件、输出目录、受众、敏感性和是否保留原件。 | 知道要交付哪个文件，不误改原件。 |
| 文件读取 | 读取文件结构、页/slide/sheet 数量、关键文本、表格、图片和元数据线索。 | 不靠文件名猜内容。 |
| 内容设计 | 先确定目录、页面/幻灯片/工作表结构、数据字段和视觉密度。 | 产物有清晰阅读路径。 |
| 构建/编辑 | 使用合适工具创建或修改文件；保留样式和可编辑性。 | 文件可打开，内容完整。 |
| 验证修复 | 按文件类型做渲染、预览、公式、结构或导出检查。 | 发现的问题已修或明确列出。 |
| 最终交付 | 给最终文件路径、验证结果、剩余风险和下一步。 | 用户能直接使用。 |

## 文件类型门禁
### PPT/PPTX
- 新建 deck 先写讲述线：主题、受众、每页结论、证据对象。
- 默认输出可编辑 PPTX，不把整页做成不可编辑大图，除非用户明确要图片型输出。
- 有数据图表时说明数据来源，避免为了好看编造数字。
- 最终检查：文件存在、slide 数量正确、预览/导出不空白、标题和正文不重叠、图片清晰、图表标签可读。

### DOCX/Word
- 编辑现有文档时保留原件，输出新文件。
- 小改动优先局部替换；需要重写时说明原因。
- 批注、修订、目录、页码、表格、交叉引用等结构化元素要做结构检查。
- 最终检查：文件存在、页数/章节符合预期、渲染或预览没有截断/重叠、表格不贴边、批注/修订保留或清理符合要求。

### PDF
- PDF 阅读可以先抽文本，但版式结论必须看渲染或页面图。
- PDF 生成要检查页码、边距、字体、表格、图片、链接和引用。
- 如果无法渲染，必须说明原因，并把结论限定为“文本/结构检查”，不能声称版式已通过。
- 最终检查：文件存在、页数正确、页面能渲染、关键页无黑块/乱码/错位/截断。

### Excel/XLSX/CSV
- 派生数据优先用公式或可审计的转换步骤，不把关键计算硬编码成死值。
- 对 CSV/TSV 先确认分隔符、编码、表头、日期/数字格式和空值。
- 图表和 dashboard 要有明确数据源范围；新增行列时同步公式、条件格式和图表范围。
- 最终检查：关键范围 values/formulas、错误值扫描、图表/表格预览、列宽和冻结窗格、输出文件存在。

## 验证清单
- 文件级：最终文件存在、非空、扩展名正确、能被目标工具打开或导入。
- 内容级：标题、章节、页/slide/sheet 数、关键数据和用户要求逐项覆盖。
- 视觉级：渲染/截图/预览检查，无明显截断、重叠、乱码、空白页、坏图表。
- 数据级：公式、引用范围、错误值、单位、日期、百分比、汇总口径一致。
- 安全级：敏感信息、个人元数据、隐藏批注、修订记录、水印、外部链接按用户要求处理。

## 反模式
- 只输出一段文字，让用户自己复制进 Office。
- 只看 PDF/DOCX 文本抽取，就断言版式没问题。
- 把 PPT 做成一张张不可编辑截图，却没有说明。
- Excel 里把应当公式计算的结果硬编码。
- 覆盖原件、删除批注、接受修订或清理元数据前没有确认。
- 为了排版好看编造来源、数字、引用或法律/财务结论。

## 合并来源
- `documents`
- `presentations`
- `spreadsheets`
- `pdf`

## 本机相近 Skill
- `documents:documents`
- `presentations:Presentations`
- `spreadsheets:Spreadsheets`
- `pdf`
- `coff0xc-ui-doc-output`

## 输出合同
```markdown
完成：
- ...

交付文件：
- [文件名](绝对路径)

验证：
- [已验证/未能验证] ...

剩余风险：
- ...

下一步：
- ...
```
