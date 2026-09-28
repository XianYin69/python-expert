#!/usr/bin/env python3
"""env_probe.py - read-only probe of Python env, deps and project layout."""
import sys, os, json, shutil, argparse, subprocess
TOOLS = ["ruff", "mypy", "black", "pytest", "pyright", "uv", "poetry", "pip-compile"]
def pip_list():
    try:
        out = subprocess.run([sys.executable, "-m", "pip", "list", "--format=json"],
                             capture_output=True, text=True, timeout=60).stdout
        return [(p["name"], p["version"]) for p in json.loads(out or "[]")]
    except Exception as e:
        return [("error", str(e))]
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--path", default="."); a = ap.parse_args()
    info = {"python": sys.version.split()[0], "executable": sys.executable,
            "platform": sys.platform, "gil": sys._framework if hasattr(sys, "_framework") else None,
            "free_threading": bool(getattr(sys, "_is_gil_enabled", lambda: True)() is False)
            if hasattr(sys, "_is_gil_enabled") else False,
            "tools": {t: bool(shutil.which(t)) for t in TOOLS}}
    for f in ("pyproject.toml", "requirements.txt", "setup.py", "uv.lock", "poetry.lock"):
        p = os.path.join(a.path, f)
        if os.path.exists(p):
            info.setdefault("project_files", {})[f] = os.path.getsize(p)
    info["packages"] = pip_list()[:200]
    print(json.dumps(info, ensure_ascii=False, indent=1))
if __name__ == "__main__":
    main()
