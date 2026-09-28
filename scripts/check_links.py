#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_links.py — 悬空链接校验：扫描 .md 相对链接，目标不存在即报悬空（红线：悬空=0）。

用法：python check_links.py [--root <dir>] [--strict-url]
  --root        扫描根（默认＝本脚本所在 skill 目录）
  --strict-url  额外统计 [联网]/[本地] 计数与 URL 数（书目确证自检）
"""
import os, re, sys, argparse
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
NET = re.compile(r"\[联网\]")
LOC = re.compile(r"\[本地\]")
URL = re.compile(r"https?://[^\s)\]|]+")

def scan(root):
    bad, net, loc, urls = [], 0, 0, set()
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ("tmp", ".git", "__pycache__", "node_modules")]
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            txt = open(p, encoding="utf-8").read()
            for m in LINK.finditer(txt):
                t = m.group(1).split("#")[0].strip()
                if not t or t.startswith(("http:", "https:", "mailto:")):
                    continue
                tgt = os.path.normpath(os.path.join(dp, t))
                if not os.path.exists(tgt):
                    bad.append((os.path.relpath(p, root), t))
            net += len(NET.findall(txt)); loc += len(LOC.findall(txt))
            urls.update(URL.findall(txt))
    return bad, net, loc, urls

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--strict-url", action="store_true")
    a = ap.parse_args()
    bad, net, loc, urls = scan(a.root)
    for p, t in bad:
        print("悬空:", p, "->", t)
    print("悬空链接数 =", len(bad))
    if a.strict_url:
        print("[联网] =", net, " [本地] =", loc, " URL =", len(urls))
    sys.exit(1 if bad else 0)

main()
