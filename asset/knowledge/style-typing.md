# style-typing · 风格与类型标注

## 判据（可执行）

1. 格式交给工具，不靠人眼：`ruff format`（或 black）+ `ruff check`（E,F,W,I,N,UP,B,ANN,S,C4,RET）。
   行宽 88–100 任选其一并全库一致；争议规则以配置为准，禁止逐条手改。
2. 类型标注策略：新代码全量标注；`mypy --strict`（或 pyright basic）为门禁，
   存量代码用 `disallow_untyped_defs = true` 分模块渐进解禁。
3. 标注写法：`X | None`（PEP604，≥3.10）优于 `Optional[X]`；`list[int]` 优于 `List[int]`；
   入参用 `Sequence/Mapping/Iterable`（宽），返回用 `list/dict`（窄）——LSP 方向。
4. 结构类型优先：`Protocol`（PEP544）替代继承式 ABC，除非需要共享实现；
   `Self`（PEP673）标注链式返回；`TypeVar` 上界用 `bound=`。
5. 数据载体：不可变用 `@dataclass(frozen=True, slots=True)`；对外边界用 pydantic/msgspec 校验，
   内部层不再重复校验；禁止用 dict 传业务对象跨模块。
6. 命名：模块/函数 `snake_case`，类 `PascalCase`，常量 `UPPER`；布尔名 `is_/has_/can_` 前缀。
7. docstring：公共 API 必有一句话摘要 + 参数/返回/异常（Google 或 numpy 风格，全库一致）；
   私有实现不写空话 docstring。
8. `from __future__ import annotations` 用于延迟求值场景；不要在运行时 `eval` 注解字符串。

## 阈值与门禁

- 单函数 > 40 行或 > 4 层缩进 → 拆分；圈复杂度 > 10 → 重构。
- 参数 > 5 个 → 改 dataclass/关键字参数对象。
- 循环导入出现 → 抽公共层或依赖倒置（Protocol 注入）。

## 常见误判

- 把 `Any` 当逃生舱长期保留：应改 `object`（强制窄化）或 `TypeGuard` 收窄。
- 用 `assert` 做输入校验（`-O` 下被剥离）→ 显式 `raise ValueError`。

## 来源

PEP8 / PEP484 / PEP544 / PEP604 / PEP673；mypy.readthedocs.io；docs.python.org/3/library/typing.html；
ruff 规则表（Ruff 项目，MIT）。
