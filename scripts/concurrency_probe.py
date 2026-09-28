#!/usr/bin/env python3
"""concurrency_probe.py - static audit of threading/asyncio/GIL-boundary risks."""
import os, re, json, argparse
PATS = [
 ("C001", re.compile(r"\bthreading\.Thread\("), "thread created: CPU-bound? GIL blocks parallelism -> multiprocessing/asyncio"),
 ("C002", re.compile(r"\.start\(\)(?!.*\.join\()"), "start() without join()/context manager -> leak"),
 ("C003", re.compile(r"\bLock\(\)"), "lock: keep scope minimal, avoid nested acquisition"),
 ("C004", re.compile(r"\bglobal\s+\w+"), "global mutation under threads -> needs lock or queue"),
 ("C005", re.compile(r"\basyncio\.run\("), "asyncio.run: no blocking calls inside (use to_thread)"),
 ("C006", re.compile(r"\b(requests|urllib)\.|time\.sleep\(", ), "blocking I/O inside async -> use httpx/aiofiles/asyncio.sleep"),
 ("C007", re.compile(r"\bQueue\(\)|\bqueue\.Queue"), "queue ok; check put_nowait backpressure"),
 ("C008", re.compile(r"@app\.|ThreadPoolExecutor|ProcessPoolExecutor"), "pool: size to workload; processes for CPU, threads for I/O"),
 ("C009", re.compile(r"\bshelve\b|\bdbm\."), "shelve/dbm not process-safe"),
 ("C010", re.compile(r"\bthreading\.local\("), "thread-local: asyncio tasks share a thread -> use contextvars"),
 ("C011", re.compile(r"\bcollections\.defaultdict\("), "shared mutable container across threads -> guard or use queue"),
 ("C012", re.compile(r"\bos\.fork\("), "fork + threads is unsafe on Windows/with locks"),
]
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("--limit", type=int, default=100); a = ap.parse_args()
    hits = []
    for root, dirs, files in os.walk(a.path):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".venv", "tmp")]
        for fn in files:
            if not fn.endswith(".py"):
                continue
            p = os.path.join(root, fn)
            for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
                for rid, rx, msg in PATS:
                    if rx.search(line):
                        hits.append({"file": p, "line": i, "rule": rid, "msg": msg})
    print(json.dumps({"gil": "CPython GIL serializes bytecode; CPU-bound needs processes or C/numpy",
                      "free_threading": hasattr(__import__("sys"), "_is_gil_enabled"),
                      "count": len(hits), "hits": hits[: a.limit]}, ensure_ascii=False, indent=1))
if __name__ == "__main__":
    main()
