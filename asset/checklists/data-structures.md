# 评审清单 · data-structures

- [ ] BLOCK 成员测试用 set/dict，无 `x in list` 扫描
- [ ] BLOCK FIFO 用 deque，无 `list.pop(0)`
- [ ] Top-K 用 heapq.nsmallest/nlargest，未做无谓全排序
- [ ] 计数/分组用 Counter/defaultdict，无手写三段式
- [ ] 跨线程共享容器有锁或改队列消息传递
- [ ] 缓存有 maxsize 且只用于纯函数（lru_cache/cached_property）
- [ ] 大规模同构对象有 slots/array/numpy 方案
- [ ] 嵌套 dict 深度 ≤3，超出改模型
- [ ] 不可变记录用 tuple/frozen dataclass
- [ ] 容器规模阈值有实测数据（perf_probe）支撑
