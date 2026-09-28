#!/usr/bin/env python3
"""perf_probe.py - measure a callable: timeit + cProfile + tracemalloc (read-only)."""
import sys, timeit, cProfile, pstats, tracemalloc, io, json, argparse, importlib.util
def load(path, name):
    spec = importlib.util.spec_from_file_location("m", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    if not hasattr(m, name):
        raise AttributeError("no callable %s in %s" % (name, path))
    return getattr(m, name)
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--file", required=True)
    ap.add_argument("--func", required=True); ap.add_argument("--arg", default=None)
    ap.add_argument("--number", type=int, default=100); a = ap.parse_args()
    argv = [a.arg] if a.arg else []
    fn = load(a.file, a.func)
    out = {"func": a.func, "number": a.number}
    out["timeit_us"] = round(timeit.timeit(lambda: fn(*argv), number=a.number) / a.number * 1e6, 2)
    pr = cProfile.Profile(); pr.enable()
    for _ in range(a.number):
        fn(*argv)
    pr.disable(); s = io.StringIO()
    pstats.Stats(pr, stream=s).sort_stats("cumulative").print_stats(10)
    out["profile_top"] = s.getvalue()[-2000:]
    tracemalloc.start(); fn(*argv); cur, peak = tracemalloc.get_traced_memory(); tracemalloc.stop()
    out["mem_peak_kb"] = round(peak / 1024, 1)
    out["baseline"] = "single call, warm cache; compare against a variant with same args"
    out["python"] = sys.version.split()[0]
    print(json.dumps(out, ensure_ascii=False, indent=1))
if __name__ == "__main__":
    main()
