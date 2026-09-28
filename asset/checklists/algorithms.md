# 评审清单 · algorithms

- [ ] BLOCK 性能结论有 cProfile/timeit 数据（无数据即判「存疑需实验」）
- [ ] 无嵌套循环对同一集合，或已证明规模上限可接受
- [ ] BLOCK 循环内无 O(n) 容器操作（index/remove/in/insert(0)）
- [ ] 有序数据查找用 bisect
- [ ] 递归深度受控（≤1000）或已改迭代
- [ ] 数值密集段已向量化（numpy）
- [ ] 边界测试齐全：空/单元素/重复/已排序/逆序/超大
- [ ] 复杂度已写入 docstring 或注释
- [ ] 近似算法声明了误差界与适用条件
- [ ] 排序 key 确定性（tuple key），不依赖未定义次序
