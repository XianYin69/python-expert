#!/usr/bin/env python3
"""template_gen.py - print/copy a scaffold from asset/templates/ (never overwrites silently)."""
import os, shutil, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TDIR = os.path.join(ROOT, "asset", "templates")
def resolve(kind):
    names = os.listdir(TDIR)
    for n in names:
        if n == kind or os.path.splitext(n)[0] == kind:
            return os.path.join(TDIR, n)
    return None
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", help="stem or filename: pyproject|conftest|protocol|worker_pool|async_gather")
    ap.add_argument("--out", help="workspace path to copy into (default: print)")
    ap.add_argument("--force", action="store_true", help="allow overwrite of --out")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list or not a.kind:
        print("\n".join(sorted(os.listdir(TDIR)))); return
    src = resolve(a.kind)
    if not src:
        raise SystemExit("no template %r" % a.kind)
    if a.out:
        if os.path.exists(a.out) and not a.force:
            raise SystemExit("[dry-run] refuse to overwrite %s (use --force)" % a.out)
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        shutil.copyfile(src, a.out); print("[OK] %s -> %s" % (a.kind, a.out)); return
    print(open(src, encoding="utf-8").read())
if __name__ == "__main__":
    main()
