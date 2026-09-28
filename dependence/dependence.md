# dependence（依赖声明）

本技能包依赖的技能包/软件/仓库地址：每行一条 `名称 | 类型 | 来源`，类型为 skill|software|repo。

```
python | software | >=3.11（官方解释器；3.13 free-threading 为实验特性）
ruff | software | pip（格式+lint，可选但强烈推荐）
mypy | software | pip（strict 类型门禁，可选）
pytest | software | pip（测试执行，可选）
pytest-cov | software | pip（覆盖率，可选）
coverage.py | software | pip（分支覆盖，可选）
pyright | software | npm/pip（类型检查替代方案，可选）
uv | software | pip（依赖与锁管理，可选）
poetry | software | pip（依赖管理替代方案，可选）
pip-tools | software | pip（最小改动的锁方案，可选）
numpy | software | pip（向量化优化，可选）
Cython | software | pip（热点 C 扩展，可选）
memray | software | pip（内存剖析，可选）
py-spy | software | pip（采样剖析，可选）
hypothesis | software | pip（属性测试，可选）
structlog | software | pip（结构化日志，可选）
bandit | software | pip（安全扫描，可选）
general-programming | skill | 调用方（SMS 编码技能）
code-guidelines | skill | 调用方（SMS 编码技能）
pavedpath-code | skill | 调用方（SMS 编码技能）
skill_manage_system | skill | 调度方（SMS 主流程）
```

## 说明

- 无 software 依赖时本技能仍可工作：`scripts/` 只用标准库，工具缺失自动降级为静态评审。
- 本技能**不**写入或修改上述调用方技能目录，仅被它们调用。
