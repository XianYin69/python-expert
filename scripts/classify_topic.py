#!/usr/bin/env python3
"""classify_topic.py - map a query/code to python-expert knowledge leaves."""
import sys, json, argparse, io
TOPICS = {
 "style-typing": ["pep8", "lint", "ruff", "black", "format", "typing", "mypy", "annotat", "docstring", "风格", "类型", "命名"],
 "data-structures": ["list", "dict", "set", "tuple", "deque", "heapq", "dataclass", "namedtuple", "slots", "lru", "容器", "结构", "选型"],
 "algorithms": ["algorithm", "big-o", "on2", "sort", "search", "bisect", "recursion", "dp", "graph", "复杂度", "嵌套"],
 "concurrency-async": ["thread", "multiprocessing", "asyncio", "async ", "await", "coroutine", "gil", "lock", "queue", "pool", "concurrent", "race", "并发", "异步", "死锁"],
 "errors-logging": ["exception", "except", "raise", "traceback", "logging", "logger", "structlog", "异常", "报错", "日志", "堆栈"],
 "testing": ["pytest", "fixture", "mock", "monkeypatch", "parametrize", "coverage", "hypothesis", "测试", "夹具", "覆盖率", "断言"],
 "packaging-deps": ["pyproject", "setup.py", "requirements", "venv", "pip ", "uv", "poetry", "pdm", "wheel", "sdist", "打包", "依赖", "虚拟环境"],
 "performance": ["slow", "performance", "profile", "cprofile", "timeit", "optimize", "bottleneck", "cython", "numpy", "性能", "优化", "内存"],
 "security-antipattern": ["eval", "exec", "pickle", "yaml.load", "shell=True", "subprocess", "path", "injection", "assert ", "mutable default", "bare except", "安全", "注入", "反模式"],
}
def score(text):
    t = text.lower()
    return {k: sum(t.count(w) for w in ws) for k, ws in TOPICS.items()}
def main():
    ap = argparse.ArgumentParser(description="classify python-expert topic")
    ap.add_argument("--text", default=""); ap.add_argument("--code"); ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--emit-tree", dest="tree"); a = ap.parse_args()
    if a.tree:
        io.open(a.tree, "w", encoding="utf-8").write(json.dumps(
            {"version": 1, "skill": "python-expert",
             "leaves": [{"id": k, "keywords": v,
                         "knowledge": "knowledge/%s.md" % k,
                         "checklist": "checklists/%s.md" % k} for k, v in TOPICS.items()]},
            ensure_ascii=False, indent=1))
        print("[OK] tree ->", a.tree); return
    txt = a.text + ("\n" + io.open(a.code, encoding="utf-8", errors="replace").read() if a.code else "")
    sc = sorted(score(txt).items(), key=lambda kv: -kv[1])[: a.top]
    print(json.dumps({"scores": dict(sc), "primary": sc[0][0] if sc[0][1] else None}, ensure_ascii=False))
if __name__ == "__main__":
    main()
