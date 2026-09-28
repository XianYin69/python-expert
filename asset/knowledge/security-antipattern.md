# security-antipattern · 安全与反模式

## 安全判据（阻塞级）

1. 禁止 `eval()`/`exec()` 处理外部输入；配置求值用显式解析或 `ast.literal_eval`（仍限字面量）。
2. 禁止 `pickle.loads`/`marshal` 加载不可信数据（任意代码执行）；跨进程/存储用 JSON/msgpack + 校验。
3. `yaml.load` 必须 `Loader=yaml.SafeLoader`（或直接 `yaml.safe_load`）。
4. 命令执行：`subprocess.run([...], shell=False)` 列表参数；`shell=True` 需白名单论证；禁止字符串拼接用户输入。
5. 路径注入：外部路径 `os.path.realpath` 后校验仍在允许根内（`Path.is_relative_to`）；
   归档解压防 `../` 穿越；临时文件用 `tempfile.mkdtemp/NamedTemporaryFile`，禁 `mktemp`。
6. SQL/LDAP/模板注入：参数化查询、模板自动转义；禁止字符串拼 SQL。
7. 密钥：来自环境/密钥管理，禁止硬编码与写入日志；`.env` 进 `.gitignore`。
8. TLS：默认验证证书，禁 `verify=False`；自签需显式 CA 配置。
9. 反序列化/解压限额：zip 解压前校验条目路径与总大小（zip bomb）；外部数据设大小上限。
10. 哈希与随机：口令用 `argon2`/`bcrypt`；令牌/随机用 `secrets`，禁 `random`。

## 编码反模式（判据）

11. 可变默认参数 `def f(x=[])` → `x: list | None = None` 内部再建。
12. `assert` 做校验/契约（`-O` 剥离）→ 显式 raise。
13. 循环里改正在迭代的容器 → 新列表或 `list[:]`。
14. `== None` → `is None`；`if x == []` → `if not x`（注意 0/"" 语义差异）。
15. 类级可变属性当实例状态用（共享陷阱）。
16. 裸 `open()` 不指定 `encoding` → 平台默认（Windows cp936）导致乱码；显式 `encoding="utf-8"`。
17. 可变全局单例 + 多线程；`datetime.now()` 无 tz → 用 `datetime.now(timezone.utc)`。
18. 用 `is` 比较值（小整数缓存导致「本地正常、线上错」）。
19. 宽 `except Exception` 后返回 `None` 掩盖失败 → 让错误冒泡或转领域异常。
20. 循环导入靠 `import` 藏在函数体内长期化 → 重构成依赖注入。

## 来源

OWASP Top 10 / CWE；bandit 规则族；docs.python.org/3/library/{secrets,tempfile,subprocess}.html；
Effective Python（Slatkin）条目 7/12/14/20 等。
