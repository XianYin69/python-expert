# 评审清单 · concurrency-async

- [ ] BLOCK CPU-bound 用进程（ProcessPoolExecutor/multiprocessing），未指望线程提速
- [ ] BLOCK 事件循环内无阻塞调用（requests/time.sleep/同步 DB）→ 已改异步或 to_thread
- [ ] 并发有上限（Semaphore / TaskGroup / 分批 gather），无无界 gather
- [ ] create_task 返回值有引用，异常被收敛（TaskGroup/回调）
- [ ] 超时与取消路径已处理（asyncio.timeout / wait_for），CancelledError 未被吞
- [ ] 共享可变状态有锁或消息传递，加锁顺序固定
- [ ] BLOCK 锁内不做 I/O 或回调
- [ ] asyncio 场景不用 threading.local，改 contextvars
- [ ] 跨进程不传句柄/共享内存，改队列或外部存储
- [ ] 并发正确性有压力测试（多轮 + 随机延迟 + 超时）
