# performance · 性能剖析与优化

## 判据（可执行）

1. 顺序不可颠倒：**测量 → 定位热点 → 改一处 → 再测量**。未测就改 = 无效优化。
2. 工具选择：整体热点 `cProfile`/`py-spy`（采样、低开销）；微基准 `timeit`（多次、同参、预热）；
   内存 `tracemalloc`/`memray`；I/O 等待看日志时间戳而非 CPU 剖析。
3. 报告必须含：环境（Python 版本/平台/CPU 核数）、数据规模、基线值、优化后值、方差或重复次数。
4. 优先算法级改动（O(n²)→O(n log n)）再常数级优化（局部变量、`map`、推导式、避免属性查找）。
5. 常见常数优化：循环内避免全局/属性查找（局部别名）、字符串用 `join` 不用 `+=`、
   预编译 `re`、`str` 拼接走 f-string、避免重复 `open`、批量 I/O 与缓冲。
6. 解释器瓶颈：CPU-bound 热点 → numpy/Cython/`_struct`/C 扩展或 `concurrent.futures` 多进程；
   不要指望多线程加速纯 Python 计算（GIL）。
7. 缓存策略：`lru_cache` 只用于纯函数且基数可控；跨进程缓存需外部存储并声明失效策略。
8. 内存：大文件流式读（`for line in f`）而非 `read()`；生成器/`yield` 替代中间列表；
   百万级对象用 `slots`/`array`/`numpy`；注意循环引用 + `__del__` 导致回收代价。
9. I/O：批量写入、事务合并、连接复用（池）、异步或线程掩盖等待；网络设超时与重试上限。
10. 启动性能：延迟导入重依赖、避免 import 期做 I/O；CLI 冷启动预算需实测。
11. C 扩展边界：只在剖析证明必要后引入；须给出可回退的纯 Python 实现与 ABI/构建说明。

## 阈值参考（须实测复核）

- 单次调用 < 1ms 的微优化通常无意义；热点占比 < 20% 的改动不值得引入复杂度。

## 来源

docs.python.org/3/library/{timeit,cProfile,tracemalloc,profile}.html；HOWTO instrumentation；
numpy/Cython 官方性能文档；memray / py-spy 项目文档。
