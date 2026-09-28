# packaging-deps · 依赖与打包

## 判据（可执行）

1. 单一元数据源：`pyproject.toml` + `[project]`（PEP621）；`setup.py` 仅在需要自定义构建时保留 shim。
2. 构建后端显式声明 `[build-system] requires/build-backend`（PEP517/518）；默认 setuptools，纯 Python 可选 hatchling/flit。
3. 版本约束：库 → 宽松下限 `>=1.2,<2`（不锁死上游）；应用 → 精确锁（`uv lock`/`poetry.lock`/`pip-tools` 编译产物）。
4. 禁止无约束依赖（`requests` 裸写）与「装到 latest 就上线」；禁止把 dev 依赖混入运行时依赖。
5. 依赖分层：`[project.optional-dependencies]` 放 extras（dev/test/docs）；避免为可选功能强拉重依赖。
6. 环境隔离：一律 venv（或 uv/poetry 管理的环境）；禁止污染系统解释器；Windows 注意 `py -3.x` 与 PATH 顺序。
7. 工具选型：新项目 `uv`（快、锁文件、workspace）；已有 poetry 项目不无因由迁移；`pip-tools` 适合最小改动。
8. 可复现：提交 lock 文件；CI 用锁安装（`uv sync --frozen` / `pip install -r requirements.lock`）。
9. 入口点：CLI 用 `[project.scripts]`，禁止让用户 `python path/to/module.py` 当接口。
10. 打包卫生：`sdist` 含测试与 LICENSE；`wheel` 不含 `tests/`、`tmp/`、缓存；`MANIFEST.in` 只补数据文件。
11. 循环依赖与隐式依赖：导入即失败必须在 CI 冒烟测试暴露；`importlib.metadata` 版本检查替代硬编码路径。
12. 许可证：新增依赖须核对 license 与传染性（MIT/Apache-2.0/BSD 兼容；GPL 需评估）；记录到 dependence/。
13. 弃用治理：`DeprecationWarning` 显式可见（`-W error::DeprecationWarning` 在 CI 跑一次）。

## 来源

packaging.python.org（PEP517/518/621/440 指引）；docs.python.org/3/installing；uv / poetry / pip-tools 文档。
