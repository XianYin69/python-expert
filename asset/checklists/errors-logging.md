# 评审清单 · errors-logging

- [ ] BLOCK 无裸 `except:`、无 `except Exception: pass`
- [ ] 捕获类型最小化，重抛用 `raise ... from err` 保留 __cause__
- [ ] 外部异常已翻译为领域异常，上层只认领域异常
- [ ] BLOCK 资源全部 with 管理（文件/锁/事务/临时目录）
- [ ] 库代码不调 basicConfig、不加 handler、不设 root level
- [ ] 日志用惰性格式化（`log.info("x=%s", x)`），异常用 log.exception
- [ ] 级别语义符合约定（DEBUG/INFO/WARNING/ERROR/CRITICAL）
- [ ] correlation_id 通过 contextvars + Filter 注入并可跨线程传递
- [ ] BLOCK 日志无密钥/PII（集中脱敏）
- [ ] 重试只用于幂等操作，有指数退避与次数上限
