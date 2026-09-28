# concurrency-async · 并发与异步

## GIL 边界（判据）

1. GIL 串行化 CPython 字节码执行：**CPU-bound 多线程不提速**（常因争锁更慢）；
   I/O-bound 多线程有效（阻塞时释放 GIL）。
2. 选型三分法：CPU 密集 → `ProcessPoolExecutor`/`multiprocessing`（绕 GIL，代价=序列化与进程启动）；
   大量 I/O 等待 → `asyncio`（单线程事件循环，万级连接）；少量阻塞 I/O 调用 → `ThreadPoolExecutor`。
3. 3.13+ free-threading（`--disable-gil` 构建）为实验特性：不得作为生产结论前提，须实测并声明构建标志。

## asyncio 规则

4. 事件循环内禁止阻塞：`requests`/`time.sleep`/同步 DB → 改 `httpx.AsyncClient`/`asyncio.sleep`/`asyncio.to_thread`。
5. 并发上限用 `Semaphore` 或分批 `gather`，禁止无界 `gather(*huge)`（内存与下游打爆）。
6. 取消与超时：`asyncio.timeout()`/`wait_for` 包裹；`CancelledError` 不得被 `except Exception` 吞掉（BaseException 语义）。
7. 任务必须有引用：`create_task` 返回值存集合，否则可能被 GC；用 `TaskGroup`（3.11+）收敛异常。
8. 混合栈：库无异步版本 → `to_thread`，不要为「全异步」重写驱动。

## 共享状态

9. 线程共享可变对象需 `Lock`/`RLock` 或消息传递（`queue.Queue`）；优先消息传递。
10. 计数/标志用 `itertools.count`（线程安全）或加锁；`+=` 非原子。
11. 跨进程不共享内存：状态走 `multiprocessing.Queue`/`Manager`（慢）或外部存储；句柄/socket 不可跨进程传。
12. `threading.local` 在 asyncio 下不可靠（同线程多任务）→ `contextvars`。
13. 死锁预防：固定加锁顺序、`acquire(timeout=)`、不在锁内做 I/O 或回调。

## 验证

14. 并发正确性靠压力测试（多轮 + 随机延迟）与 `--runtime` 超时；不可只凭「跑一次没崩」。

## 来源

docs.python.org/3/{library/asyncio*,library/threading.html,library/multiprocessing.html,howto/instrumentation.html}；
Beazley「Understanding the GIL」/free-threading PEP703。
