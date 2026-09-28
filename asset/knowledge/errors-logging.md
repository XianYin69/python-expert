# errors-logging · 异常与日志

## 异常判据

1. 禁止 `except:` 与 `except Exception: pass`（吞 `KeyboardInterrupt`/掩盖失败）；
   最小化捕获类型，捕获后要么处理、要么 `raise ... from err` 重抛。
2. 边界处翻译异常：外部错误（`requests.HTTPError`、`OSError`）→ 领域异常（`ConfigError`），
   保留 `__cause__` 链（PEP3134），上层只认领域异常。
3. 自定义异常继承 `Exception` 并带上下文字段；禁止用异常做流程控制（可预期分支用返回值/`None`/`match`）。
4. `try` 块只包可能失败的语句；`else` 放成功路径，`finally` 只放清理。
5. 资源用 `with`（文件/锁/事务/临时目录）；`__enter__/__exit__` 或 `contextlib`，禁止手写 close 链。
6. 输入校验用显式 `raise ValueError/TypeError`，不用 `assert`（`-O` 剥离）。
7. 重试策略：只重试幂等操作 + 指数退避 + 上限次数；不可重试（4xx/校验失败）直接失败。

## 日志判据

8. 库代码：`logging.getLogger(__name__)`，**绝不** `basicConfig()`/加 handler/设 root level（属应用所有）。
9. 应用入口一次性配置 `dictConfig`；默认 `NullHandler` 于库顶层，避免 "no handlers" 噪声。
10. 用惰性格式化 `log.info("n=%s", n)`，禁止 f-string 拼接（级别关闭时不应付出格式化成本）。
11. 异常日志：`log.exception()` 或 `log.error(..., exc_info=True)`，保留栈；
    结构化日志（structlog/JSON）时 `exc_info` 仍须序列化进字段。
12. 级别约定：`DEBUG` 诊断细节 / `INFO` 生命周期里程碑 / `WARNING` 可自愈降级 /
    `ERROR` 请求失败但进程存活 / `CRITICAL` 不可用。
13. 关联 ID：请求级 `contextvars` + Filter 注入 `correlation_id`，跨线程/进程显式传递。
14. 禁止记录密钥、token、身份证/密码字段；PII 需脱敏函数集中处理。

## 来源

docs.python.org/3/library/{logging,logging.config}.html、HOWTO logging；PEP3134；structlog 文档。
