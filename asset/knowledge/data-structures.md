# data-structures · 数据结构选型

## 判据（可执行）

1. 查找语义决定容器：唯一性/成员测试 → `set`；键值映射 → `dict`；有序可重复序列 → `list`；
   记录不可变+可哈希 → `tuple`/`frozenset`。禁止用 `list` 做 `in` 判重的 O(n) 扫描。
2. 队列语义：FIFO 用 `collections.deque`（两端 O(1)），禁止 `list.pop(0)`（O(n) 搬移）。
3. 计数/分组：`collections.Counter`、`defaultdict`；避免手写 `if k not in d` 三段式。
4. 排序取前 k：`heapq.nsmallest/nlargest`（O(n log k)）优于 `sorted(...)[:k]`（O(n log n)）。
5. 有序映射：插入序即 `dict`（3.7+ 语言保证）；需要按 key 排序遍历用 `sorted(d.items())` 或 `bisect` 维护索引。
6. 数据载体成本：`__slots__` 或 `@dataclass(slots=True)` 在百万级实例上省 40–60% 内存；
   大量同构小对象考虑 `array`/`numpy` 结构化数组或列式存储。
7. 缓存：`functools.lru_cache(maxsize=…)` 只用于纯函数、参数可哈希；无界缓存是内存泄漏源；
   实例方法缓存用 `functools.cached_property`。
8. 组合工具：`itertools.chain/islice/groupby/product`、`more_itertools`（第三方）替代手写嵌套循环。
9. 不可变共享：跨线程共享只读结构用 `tuple`/`frozenset`；写共享用 `queue` 或加锁，不用「约定不写」。

## 阈值

- 元素 > 10⁵ 且频繁随机访问 → 评估 `array`/`numpy`；> 10⁶ → 评估外存/分页或索引结构。
- 嵌套 dict 深度 > 3 → 换 dataclass/pydantic 模型。

## 来源

docs.python.org/3/library/collections.html 与 /howto/sort.html；CPython list/dict/set 实现复杂度表；
Reizig《Data Structures and Algorithms in Python》；python-attrs / dataclasses 文档。
