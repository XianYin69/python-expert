# 评审清单 · security-antipattern

- [ ] BLOCK 无 eval/exec 处理外部输入；字面量解析用 ast.literal_eval
- [ ] BLOCK 无 pickle.loads/marshal 加载不可信数据（改 JSON/msgpack + 校验）
- [ ] BLOCK yaml.safe_load 或 SafeLoader
- [ ] BLOCK subprocess 用列表参数、shell=False；无字符串拼接命令
- [ ] BLOCK 外部路径 realpath 后校验仍在允许根内；解压防 ../ 穿越与 zip bomb
- [ ] SQL/模板参数化与自动转义，无字符串拼 SQL
- [ ] BLOCK 无硬编码密钥；TLS 验证未被关闭；口令用 argon2/bcrypt，令牌用 secrets
- [ ] 无裸 open() 缺 encoding（显式 utf-8）
- [ ] 无 `is` 比较值、无 `== None`、无迭代中修改容器
- [ ] 无类级可变属性被当实例状态使用
- [ ] datetime 带 tz（timezone.utc），无 naive now()
