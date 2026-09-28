# 评审清单 · testing

- [ ] BLOCK 新增/改动代码有对应测试
- [ ] 测试命名表达单一行为（test_行为_when_条件_then_结果）
- [ ] 边界覆盖：空/单元素/重复/Unicode/超时/权限失败
- [ ] BLOCK 时间、随机、网络均可注入，无真实网络与 time.sleep
- [ ] mock patch 在「使用处」而非定义处
- [ ] 覆盖率有下限（≥80% 起步）且关键路径要求分支覆盖
- [ ] 测试相互隔离（tmp_path，无顺序依赖、无全局状态）
- [ ] CI 与本地同命令同配置（pytest -q --tb=short --cov --cov-branch）
- [ ] 慢测试分层（-m "not slow"）并有 --durations 记录
- [ ] BLOCK 修 bug 先有能复现该 bug 的失败测试
- [ ] 无被 skip 掩盖的失败用例
