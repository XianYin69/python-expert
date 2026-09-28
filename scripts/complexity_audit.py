#!/usr/bin/env python3
"""complexity_audit.py - flag likely O(n^2)+ patterns and hot spots (static, read-only)."""
import os, re, json, argparse
NESTED = re.compile(r"^(\s*)(for|while)\b")
MEMBER = re.compile(r"\b(\w+)\s+(in|not in)\s+(\w+)")
CALLS = re.compile(r"\.(index|remove|count|insert|pop)\(|\b(sorted|list|set|dict)\(")
def audit(path):
    hits = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".venv", "tmp")]
        for fn in files:
            if not fn.endswith(".py"):
                continue
            p = os.path.join(root, fn)
            stack = []
            for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
                m = NESTED.match(line)
                if m:
                    ind = len(m.group(1))
                    stack = [s for s in stack if s < ind]
                    if stack:
                        hits.append({"file": p, "line": i, "rule": "CX001",
                                     "msg": "nested loop depth %d -> check for index/dict lookup or vectorize" % (len(stack) + 1)})
                    stack.append(ind)
                mm = MEMBER.search(line)
                if mm and re.search(r"\bfor\b", line):
                    hits.append({"file": p, "line": i, "rule": "CX002",
                                 "msg": "`%s in %s` inside loop: list/set membership is O(n) vs O(1) for set/dict" % (mm.group(1), mm.group(3))})
                if CALLS.search(line) and stack:
                    hits.append({"file": p, "line": i, "rule": "CX003",
                                 "msg": "O(n) container op inside loop -> amortize or hoist"})
    return hits
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("--limit", type=int, default=120); a = ap.parse_args()
    h = audit(a.path)
    print(json.dumps({"note": "static heuristic; confirm with perf_probe.py before optimizing",
                      "count": len(h), "hits": h[: a.limit]}, ensure_ascii=False, indent=1))
if __name__ == "__main__":
    main()
