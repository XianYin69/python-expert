# algorithms · 算法与复杂度

## 判据（可执行）

1. 先量后改：任何「太慢」结论必须有 `perf_probe.py`/`cProfile` 数据支撑；
   无数据 → 判定为「存疑需实验」，禁止给出加速倍数。
2. 复杂度自检表：嵌套循环对同一集合 → O(n²)，改哈希查找/排序+双指针；
   `x in list` 在循环内 → 先转 `set`；重复排序 → 排序一次或 `heapq`。
3. 查找：有序数据用 `bisect`（O(log n)）；字符串前缀用 trie 或 `str.startswith` 批量；
   子串匹配交给 `re`（预编译）或 `in`（CPython 用 Crochemore–Perrin 线性）。
4. 图/树：优先 `networkx`（算法成熟）而非自写 BFS/DFS；小规模用 dict 邻接表即可。
5. 动态规划：先写递归 + `lru_cache` 验证正确性，再决定是否自底向上省栈/省内存。
6. 递归深度：默认上限 1000；深递归 → 改迭代或 `sys.setrecursionlimit` 前先证明必要（栈溢出不可捕获）。
7. 数值密集：向量化（numpy）替代 Python 层循环，通常 10–100×；纯 Python 热点再考虑 C 扩展。
8. 幂等与稳定：排序 key 用 `tuple` 保证确定性；`sorted` 稳定，勿依赖 `list.sort` 未定义次序。
9. 近似算法：只需 Top-K/去重统计时允许 `heapq`/`HyperLogLog` 类近似，但须在结论中声明误差界。

## 阈值

- n ≤ 10³：O(n²) 可接受；10⁴–10⁵：必须 O(n log n)；≥10⁶：向量化或外部存储/流式处理。
- 单函数 > 60 行算法实现 → 拆步骤并加单元测试边界（空/单元素/重复/已排序/逆序）。

## 来源

CLRS；docs.python.org/3/library/bisect.html、/itertools.html；numpy 官方 performance 指南；
`timeit`/`cProfile` 文档。
