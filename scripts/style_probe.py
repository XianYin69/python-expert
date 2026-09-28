#!/usr/bin/env python3
"""style_probe.py - static style/typing audit without external tools (ruff/mypy if present)."""
import os, re, sys, json, argparse, subprocess
RULES = [
 ("E501", re.compile(r"^.{101,}$"), "line > 100 chars", "warn"),
 ("N802", re.compile(r"^\s*def [A-Z]\w*\("), "function name should be lowercase", "warn"),
 ("T201", re.compile(r"\bprint\("), "print() in library code -> use logging", "info"),
 ("ANN001", re.compile(r"^\s*def \w+\([^)]*\)\s*:"), "missing return/param annotations", "info"),
 ("ANN201", re.compile(r"^\s*(?:async )?def \w+\(.*\)\s*:"), "add -> ReturnType annotation", "info"),
 ("B006", re.compile(r"def \w+\([^)]*=\s*(\[\]|\{\}|set\(\))"), "mutable default argument", "error"),
 ("S101", re.compile(r"\bassert\s+\w"), "assert used for validation (stripped under -O)", "warn"),
 ("E722", re.compile(r"^\s*except\s*:"), "bare except", "error"),
 ("C4", re.compile(r"=\s*(list|dict|set)\(\s*\["), "needless comprehension wrapper", "info"),
]
def scan(path):
    hits = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in (".git", "tmp", "__pycache__", ".venv", "node_modules")]
        for fn in files:
            if not fn.endswith(".py"):
                continue
            f = os.path.join(root, fn)
            for i, line in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
                s = line.rstrip("\n")
                if s.lstrip().startswith("#"):
                    continue
                for rid, rx, msg, sev in RULES:
                    if rx.search(s):
                        hits.append({"file": f, "line": i, "rule": rid, "msg": msg, "sev": sev})
    return hits
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("path", nargs="?", default="."); ap.add_argument("--tools", action="store_true")
    a = ap.parse_args(); res = {"static": scan(a.path)[:200]}
    if a.tools:
        for tool, args in (("ruff", ["check", a.path]), ("mypy", [a.path])):
            try:
                res[tool] = subprocess.run([tool] + args, capture_output=True, text=True, timeout=120).stdout[:4000]
            except Exception as e:
                res[tool] = "unavailable: " + str(e)
    print(json.dumps(res, ensure_ascii=False, indent=1))
if __name__ == "__main__":
    main()
