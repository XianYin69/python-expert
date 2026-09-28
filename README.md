# python-expert

Python 语言与生态的资深专家顾问技能：为 SMS 主流程与编码技能（general-programming /
code-guidelines / pavedpath-code 等）在编写与评审 Python 代码时提供**可执行**的专家判断、
评审清单与重构建议。

## 覆盖领域（九叶知识树）

风格与类型标注 · 数据结构选型 · 算法与复杂度 · 并发与异步（GIL 边界）· 异常与日志 ·
测试与覆盖率 · 依赖与打包 · 性能剖析与优化 · 安全与反模式

## 快速使用

```
python scripts/classify_topic.py --text "asyncio 里调用 requests 很慢" --code pkg/svc.py
python scripts/knowledge_index.py --topic concurrency-async
python scripts/review_checklist.py --topic concurrency-async --format json
python scripts/concurrency_probe.py pkg/
python scripts/advice_compose.py --topic concurrency-async --verdict tmp/verdict.json
```

## 目录

| 目录 | 内容 |
|---|---|
| SKILL.md | 入口（YAML frontmatter + 一句话提示词） |
| agent/ | 四格式提示词（CLAUDE.md / agent_prompt.md / .cursorrules / instructions.md） |
| branch/流程/ | 十步执行流程细则 |
| asset/knowledge/ | 九份领域判据 |
| asset/checklists/ | 九份评审清单（BLOCK 标记阻塞项） |
| asset/templates/ | pyproject / conftest / protocol / worker_pool / async_gather 脚手架 |
| references/知识树/ | 领域拓扑与出处 |
| resistance/ | 约束与五大机制兜底 |
| scripts/ | 只读取证与产出脚本（标准库实现） |
| dependence/ | 依赖声明（SMS 安装时同检同净化） |

## 边界

只读评审为默认；不修改调用方代码，不改动其他技能目录；结论必带依据、取舍与失效边界。

## 许可

MIT（见 LICENSE）。
