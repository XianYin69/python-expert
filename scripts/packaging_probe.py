#!/usr/bin/env python3
"""packaging_probe.py - audit project metadata, deps and lock/venv hygiene (read-only)."""
import os, re, json, argparse, sys
NEED = ["[project]", "name", "version", "requires-python", "dependencies"]
def read(p):
    return open(p, encoding="utf-8", errors="replace").read()
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("path", nargs="?", default="."); a = ap.parse_args()
    out = {"files": {}, "issues": []}
    pp = os.path.join(a.path, "pyproject.toml")
    if os.path.exists(pp):
        t = read(pp); out["files"]["pyproject.toml"] = len(t)
        for k in NEED:
            if k not in t:
                out["issues"].append("pyproject missing %s (PEP621)" % k)
        if "[build-system]" not in t:
            out["issues"].append("no [build-system] -> PEP517 build backend unset")
        if re.search(r"requires-python\s*=\s*[\"']>=\s*2", t):
            out["issues"].append("py2 floor declared")
        m = re.findall(r'^\s*"([\w.-]+)\s*([<>=!~]=?[^\"\']*)"?', t, re.M)
        out["declared_deps"] = [{"name": n, "spec": s} for n, s in m][:60]
        unpinned = [d for d in out["declared_deps"] if not d["spec"]]
        out["unpinned_count"] = len(unpinned)
    else:
        out["issues"].append("no pyproject.toml -> not PEP621 compliant")
    for f in ("requirements.txt", "uv.lock", "poetry.lock", "Pipfile.lock", "setup.py"):
        p = os.path.join(a.path, f)
        if os.path.exists(p):
            out["files"][f] = os.path.getsize(p)
            if f == "requirements.txt":
                lines = [l for l in read(p).splitlines() if l.strip() and not l.startswith("#")]
                out["issues"] += ["requirements.txt unpinned: %s" % l for l in lines
                                  if not re.search(r"[<>=!~]=", l)][:20]
    out["venv"] = bool(os.environ.get("VIRTUAL_ENV") or os.environ.get("CONDA_PREFIX"))
    out["python"] = sys.version.split()[0]
    print(json.dumps(out, ensure_ascii=False, indent=1))
if __name__ == "__main__":
    main()
