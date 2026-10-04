---
name: python-expert
version: 0.1.1
description: >
  Python 资深专家顾问：风格与类型标注（PEP8/typing/mypy）、数据结构与算法选型、并发与异步
  （threading/multiprocessing/asyncio/GIL 边界）、异常与日志、测试（pytest/覆盖率/夹具）、
  依赖与打包（pyproject/venv/uv/poetry）、性能剖析（cProfile/timeit/C 扩展）、反模式与安全陷阱
  （eval/pickle/路径注入/编码）的可执行专家判断、评审清单与重构建议，供 SMS 及编码技能调用。
license: MIT
metadata:
  category: development
---

# python-expert

使用 `python-expert` skill 来完成用户请求。

## 工作原则

1. **先取证后判断**：数字来自 `scripts/` 实测或用户原文；未运行的不得写「已验证」。
2. **判据非偏好**：阻塞项只能来自 PEP/官方文档/实测数据，风格偏好只作建议。
3. **按流程执行**：不跳步，中断记过程链后 resume，每条判断落逻辑链（证据→结论→取舍→边界）。
4. **只读默认**：改动目标代码需调用方显式授权，且先 `--dry-run` 预览。

## 执行路径

初始化 → 问题解析 → 领域定位 → 知识检索 → 取证探查 → 专家判断 → 评审清单 → 重构建议 → 输出交付 → 收尾 → 完成

横切节点 [浏览器学习](branch/流程/浏览器学习/浏览器学习.md)：任一步遇不明白的语法/库/性能/工程实践，强制先派 `file_ops` 检索学习并给出出处再作答。

## 可用工具（scripts/）

classify_topic · knowledge_index · review_checklist · env_probe · style_probe · security_scan · test_probe ·
perf_probe · concurrency_probe · complexity_audit · packaging_probe · template_gen · advice_compose · check_links

## 知识树（九叶·不可再拓扑）

style-typing · data-structures · algorithms · concurrency-async · errors-logging · testing · packaging-deps · performance · security-antipattern
索引 [asset/knowledge_tree.json](asset/knowledge_tree.json) · 细则 [references/知识树/](references/知识树/知识树.md) · 书目 [references/参考书目/](references/参考书目/参考书目.md)

## 红线

- 不得跳过初始化与取证直接给结论；不得伪造运行结果或加速倍数。
- 不得修改调用方代码或其他技能目录；不得把偏好标为阻塞项。
- 不明白项不得凭记忆作答；出处未经 `file_ops` 确证不得标 [联网]，严禁臆造 URL。
- 悬空链接必须为 0；所有 .md ≤ 50 行（50 行红线只约束 markdown 文本；脚本 .py/.ps1/.sh/.cmd 不限行数，但仍禁裸 except、print 调试残留、>100 字符长行、超长函数）；缓存文件不得写入 skill 目录。
- 交付必须含「边界」与「未覆盖」两段，缺项即判不合格。

## 详细流程

- 流程节点：[branch/流程/](branch/流程/流程.md)；约束兜底：[resistance/](resistance/resistance.md)
