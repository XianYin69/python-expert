# CHANGELOG

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
