# CHANGELOG

## 0.1.1

迭代补全（Skill_Generator 修改路径）：浏览器学习横切节点 + file_ops 薄技能依赖 + 书目联网确证。

- 新增 branch/流程/浏览器学习/：不明白的语法/库/性能/工程实践强制先检索学习并给出出处再作答。
- 新增 resistance/浏览器学习约束/：先学后答、出处须确证、禁止臆造 URL、缓存不入 skill 目录。
- 新增 references/参考书目/：12 项候选书目确证结果（8 项 [联网] 带可达 URL、4 项 [本地] 未确证）。
- 新增 scripts/check_links.py：悬空链接校验 + [联网]/[本地] 计数自检（--strict-url）。
- 变更 dependence/dependence.md：追加 `file_ops | skill | local:skill_manage_system`（ff_lite.py
  search/fetch，须 :grant network；只传意图+参数、不内嵌正文）；code-guidelines / pavedpath-code
  标 skill|local，python / git 标 software|system。
- 变更 SKILL.md：标注浏览器学习为横切触发节点，红线补「出处未经确证不得标 [联网]」（仍 50 行）。
- 变更 流程.md / branch.md / resistance.md / 知识树.md：接入新节点与书目索引。
- 备注：版本号 0.1.1 按调用方指定（上一条 1.0.0 为首次生成误标，后续统一 0.1.x 序列）。
- 备注：单英文词与 ≥4 词英文书名会被切成词典页；改「中文书名+出版社」或 site:book.douban.com
  限定后可确证，境外源 fetch 报 WinError 10060 故不作确证源。

## 1.0.0

首次生成（Skill_Generator 创建路径）。

### 新增

- SKILL.md：YAML frontmatter + 一句话提示词 + 工作原则/执行路径/工具/红线（49 行）。
- agent/：四格式提示词（CLAUDE.md、agent_prompt.md、.cursorrules、instructions.md）。
- branch/流程/：十步流程节点（初始化→问题解析→领域定位→知识检索→取证探查→专家判断→
  评审清单→重构建议→输出交付→收尾）。
- asset/knowledge/：九叶领域判据（style-typing、data-structures、algorithms、concurrency-async、
  errors-logging、testing、packaging-deps、performance、security-antipattern）。
- asset/checklists/：九份评审清单，阻塞项以 BLOCK 前缀标记，由 review_checklist.py 解析。
- asset/templates/：pyproject.toml、conftest.py、protocol.py、worker_pool.py、async_gather.py。
- asset/knowledge_tree.json：机器可读索引（classify_topic.py --emit-tree 生成）。
- scripts/：13 个标准库脚本（classify_topic、knowledge_index、review_checklist、advice_compose、
  env_probe、style_probe、security_scan、test_probe、perf_probe、concurrency_probe、
  complexity_audit、packaging_probe、template_gen）。
- resistance/：评审约束、审查约束、输出约束、约束部分 + 五大机制 + 沙盒机制。
- references/知识树/：领域拓扑与出处留痕。
- dependence/dependence.md：依赖声明（全部可选，脚本零第三方依赖）。
- LICENSE：MIT。

### 约束

- 只新建 python-expert，未修改 general-programming / code-guidelines / pavedpath-code 等既有技能。
- 抓取缓存（tmp/downloads）不随包交付；链与存档落用户缓存目录。
