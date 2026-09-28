#!/usr/bin/env python3
"""test_probe.py - pytest/coverage runner + test-quality static hints (dry-run default)."""
import os, re, json, argparse, subprocess, sys
HINTS = [
 ("TQ001", re.compile(r"@pytest\.mark\.skip\b"), "unconditional skip hides failures"),
 ("TQ002", re.compile(r"assert\s+True\b"), "tautological assertion"),
 ("TQ003", re.compile(r"pytest\.raises\(\s*Exception"), "over-broad expected exception"),
 ("TQ004", re.compile(r"\btime\.sleep\("), "sleep in tests -> fake clock/event"),
 ("TQ005", re.compile(r"mock\.patch\("), "patch where looked up, not where defined"),
 ("TQ006", re.compile(r"def test_\w+\(\s*\)"), "test takes no fixture/param"),
]
def hints(path):
    res = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".venv", "tmp")]
        for fn in files:
            if not (fn.startswith("test_") or fn.endswith("_test.py")):
                continue
            p = os.path.join(root, fn)
            for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
                for rid, rx, msg in HINTS:
                    if rx.search(line):
                        res.append({"file": p, "line": i, "rule": rid, "msg": msg})
    return res
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("--run", action="store_true", help="run pytest (default: dry-run)")
    ap.add_argument("--cov", action="store_true")
    a = ap.parse_args()
    out = {"static_hints": hints(a.path)[:100], "pytest": "not-run (dry-run; pass --run)"}
    if a.run:
        cmd = [sys.executable, "-m", "pytest", "-q", "--tb=short"]
        if a.cov:
            cmd += ["--cov", "--cov-report=term-missing"]
        try:
            r = subprocess.run(cmd + [a.path], capture_output=True, text=True, timeout=600)
            out["pytest"] = {"rc": r.returncode, "tail": (r.stdout or r.stderr)[-3000:]}
        except Exception as e:
            out["pytest"] = "unavailable: %s" % e
    print(json.dumps(out, ensure_ascii=False, indent=1))
if __name__ == "__main__":
    main()
