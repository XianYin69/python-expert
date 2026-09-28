#!/usr/bin/env python3
"""security_scan.py - flag unsafe Python constructs (eval/pickle/shell/path/encoding)."""
import os, re, json, argparse
PATS = [
 ("SEC001", re.compile(r"\beval\("), "eval() on untrusted input -> RCE", "block"),
 ("SEC002", re.compile(r"\bexec\("), "exec() dynamic code", "block"),
 ("SEC003", re.compile(r"pickle\.loads?|marshal\.loads"), "pickle = arbitrary code on load", "block"),
 ("SEC004", re.compile(r"yaml\.load\((?!.*Loader\s*=\s*(Safe|C)Safe)"), "yaml.load without SafeLoader", "block"),
 ("SEC005", re.compile(r"shell\s*=\s*True"), "shell=True -> injection", "block"),
 ("SEC006", re.compile(r"os\.system\(|subprocess\.call\(.*shell"), "os.system/shell call", "block"),
 ("SEC007", re.compile(r"tempfile\.mktemp"), "mktemp race -> use NamedTemporaryFile", "warn"),
 ("SEC008", re.compile(r"\.\./"), "'..' in path -> normalize+validate root", "warn"),
 ("SEC009", re.compile(r"open\([^)]*\)(?![^)]*encoding)"), "open() without encoding", "warn"),
 ("SEC010", re.compile(r"hashlib\.(md5|sha1)\("), "weak hash for security use", "warn"),
 ("SEC011", re.compile(r"verify\s*=\s*False|ssl\._create"), "TLS verification disabled", "block"),
 ("SEC012", re.compile(r"SECRET|PASSWORD\s*=\s*[\"']"), "hardcoded secret", "block"),
 ("ANTI001", re.compile(r"except\s*:"), "bare except swallows KeyboardInterrupt", "block"),
 ("ANTI002", re.compile(r"except\s+Exception\s*:\s*\n?\s*pass"), "except/pass hides failures", "warn"),
 ("ANTI003", re.compile(r"def \w+\([^)]*=\s*(\[\]|\{\})"), "mutable default arg", "block"),
 ("ANTI004", re.compile(r"assert\s+(os|self\.|response|len\()"), "assert for runtime validation", "warn"),
]
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("--limit", type=int, default=200); a = ap.parse_args()
    hits = []
    for root, dirs, files in os.walk(a.path):
        dirs[:] = [d for d in dirs if d not in (".git", "tmp", "__pycache__", ".venv")]
        for fn in files:
            if not fn.endswith(".py"):
                continue
            p = os.path.join(root, fn)
            src = open(p, encoding="utf-8", errors="replace").read()
            for rid, rx, msg, sev in PATS:
                for m in rx.finditer(src):
                    hits.append({"file": p, "line": src[:m.start()].count("\n") + 1,
                                 "rule": rid, "sev": sev, "msg": msg})
    hits.sort(key=lambda h: h["sev"] != "block")
    print(json.dumps({"count": len(hits), "blocking": sum(h["sev"] == "block" for h in hits),
                      "hits": hits[: a.limit]}, ensure_ascii=False, indent=1))
if __name__ == "__main__":
    main()
