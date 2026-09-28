# 评审清单 · style-typing

- [ ] BLOCK 格式工具已配置并在 CI 执行（ruff format/check 或 black），diff 只含语义变更
- [ ] BLOCK 公共 API 全量标注，mypy --strict（或 pyright）零错误
- [ ] 入参用宽类型（Sequence/Mapping/Iterable），返回用窄类型（list/dict）
- [ ] 无 `Optional[X]`/`List[int]` 旧式写法（≥3.10 用 `X | None`、内置泛型）
- [ ] 跨模块业务数据用 dataclass(frozen=True, slots=True) 或 Protocol，不用裸 dict
- [ ] 无长期 `Any` 逃逸（改 `object` + 收窄或 `TypeGuard`）
- [ ] 命名与 docstring 风格全库一致，公共 API 有摘要+参数+异常
- [ ] 函数 ≤40 行、参数 ≤5、嵌套 ≤4 层，超出有拆分计划
- [ ] BLOCK 无 `assert` 承担输入校验
- [ ] 循环依赖已消除或改为依赖注入
