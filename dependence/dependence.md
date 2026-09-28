# dependence（依赖声明）

本技能包依赖的技能包/软件/仓库地址：每行一条 `名称 | 类型 | 来源`，类型为 skill|software|repo。

```
python | software | system（>=3.11 官方解释器；3.13 free-threading 为实验特性）
git | software | system（版本控制，收尾节点提交用）
ruff | software | pip（格式+lint，可选）
mypy | software | pip（strict 类型门禁，可选）
pytest | software | pip（测试执行，可选）
pytest-cov | software | pip（分支覆盖，可选）
pyright | software | npm/pip（类型检查替代，可选）
uv | software | pip（依赖与锁管理，可选）
poetry | software | pip（依赖管理替代，可选）
pip-tools | software | pip（最小改动锁方案，可选）
numpy | software | pip（向量化优化，可选）
Cython | software | pip（热点 C 扩展，可选）
memray | software | pip（内存剖析，可选）
py-spy | software | pip（采样剖析，可选）
hypothesis | software | pip（属性测试，可选）
structlog | software | pip（结构化日志，可选）
bandit | software | pip（安全扫描，可选）
file_ops | skill | local:skill_manage_system（联网搜索/抓取，见下）
general-programming | skill | local（调用方·SMS 编码技能）
code-guidelines | skill | local（调用方·SMS 编码技能）
pavedpath-code | skill | local（调用方·SMS 编码技能）
skill_manage_system | skill | local（调度方·SMS 主流程）
```

## 薄技能声明

- **file_ops 承担本技能全部联网动作**：`ff_lite.py search "<词>" [n]` / `fetch <url>`，
  须调用方已 `:grant network`（未授权即降级为 `[本地]`）。本技能不自行发网络请求、不装浏览器依赖。
- **用途映射**：file_ops 供 [浏览器学习](../branch/流程/浏览器学习/浏览器学习.md)（横切·强制先学后答）、
  [知识检索](../branch/流程/知识检索/知识检索.md)（＝经验查询）、
  [参考书目](../references/参考书目/参考书目.md) 与 [知识树](../references/知识树/知识树.md)
  来源确证（＝知识库构建）三处使用。
- **调用约定**：只向 file_ops 传**意图 + 参数**，不内嵌正文、不代写其执行逻辑、不改其目录。
- 无 software 依赖时本技能仍可工作：`scripts/` 只用标准库，工具缺失自动降级为静态评审。
- 本技能**不**写入或修改上述调用方/被调方技能目录，仅被调用或按意图调用。
