# 评审清单 · packaging-deps

- [ ] BLOCK pyproject.toml 为唯一元数据源（PEP621），[build-system] 显式声明
- [ ] 依赖有版本约束，运行时依赖与 dev 依赖分离（extras）
- [ ] BLOCK lock 文件入库，CI 用锁安装（uv sync --frozen / pip install -r）
- [ ] requirements.txt 无未固定版本行
- [ ] CLI 通过 [project.scripts] 暴露，不要求 python path/to/module.py
- [ ] wheel 不含 tests/tmp/缓存；sdist 含 LICENSE 与测试
- [ ] 新依赖许可证已核对并记入 dependence/
- [ ] 环境隔离（venv/uv/poetry），未污染系统解释器
- [ ] 版本下限与 requires-python 一致，无 py2 残留
- [ ] CI 跑一次 -W error::DeprecationWarning 暴露弃用
