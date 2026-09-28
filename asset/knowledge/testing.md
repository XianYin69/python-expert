# testing · 测试与覆盖率

## 判据（可执行）

1. 框架默认 pytest：函数级测试、`assert` 原生断言、`fixture` 管理依赖、`parametrize` 覆盖边界。
2. 测试金字塔：单元（快、无 I/O）占多数；集成（真实 DB/FS）用 `tmp_path`/容器；端到端少量关键路径。
3. 一个测试一个行为：命名 `test_<行为>_when_<条件>_then_<结果>`；出现多个不相关断言 → 拆分。
4. 边界必测：空集合、单元素、重复、已排序/逆序、超大值、Unicode、编码错误、超时、权限失败。
5. 时间/随机/网络必须可注入：`monkeypatch`/`freezegun`/`random.seed`/假传输对象；禁止依赖真实网络与睡眠。
6. mock 原则：patch **使用处**而非定义处（`module.func` 的导入位置）；能不 mock 就不 mock，优先真实最小实现。
7. 异步测试：`pytest-asyncio`（`asyncio_mode=auto`）或 anyio 插件；事件循环内不混线程断言。
8. 覆盖率是下限不是目标：行覆盖 ≥80% 起步，关键路径要求分支覆盖（`--cov --cov-branch`）；
   100% 行覆盖 + 弱断言 = 无效测试，须用变异测试（`mutmut`/`cosmic-ray`）抽查。
9. 属性测试：纯函数/协议用 `hypothesis` 生成输入，比手写 3 个样例更能暴露边界。
10. 回归纪律：修 bug 先加一条能复现该 bug 的失败测试，再改实现（红-绿）。
11. 隔离：测试不得互相依赖执行顺序、不得写全局状态或共享目录（用 `tmp_path`/`tmp_path_factory`）。
12. CI 一致性：`pytest -q --tb=short --cov` 与本地同配置；随机顺序插件（`pytest-randomly`）暴露隐藏依赖。
13. 慢测试治理：`-m "not slow"` 分层，`--durations=10` 找最慢项，禁止无期限 `sleep`。

## 门禁

- 新代码无测试 → 评审判 fail（阻塞）；测试失败被 skip 掩盖 → 判 fail。

## 来源

docs.pytest.org（fixture/parametrize/monkeypatch）；coverage.py 文档；hypothesis.readthedocs.io；
`test_probe.py` 静态提示规则。
