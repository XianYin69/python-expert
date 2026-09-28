#!/usr/bin/env python3
"""review_checklist.py - emit the per-topic review checklist for expert review."""
import os, json, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def items(path):
    out = []
    for line in open(path, encoding="utf-8"):
        s = line.strip()
        if s.startswith("- [ ]"):
            out.append(s[5:].strip())
    return out
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--topic", required=True)
    ap.add_argument("--format", choices=["md", "json"], default="md"); a = ap.parse_args()
    p = os.path.join(ROOT, "asset", "checklists", a.topic + ".md")
    if not os.path.exists(p):
        print(json.dumps({"error": "no checklist for topic", "topic": a.topic,
                          "available": [f[:-3] for f in os.listdir(os.path.join(ROOT, "asset", "checklists"))]}))
        raise SystemExit(1)
    it = items(p)
    if a.format == "json":
        print(json.dumps({"topic": a.topic, "count": len(it),
                          "items": [{"id": "C%02d" % (i + 1), "text": t,
                                     "status": "todo", "blocking": t.startswith("BLOCK")} for i, t in enumerate(it)]},
                         ensure_ascii=False, indent=1)); return
    print("## 评审清单 · %s（%d 项）\n" % (a.topic, len(it)))
    for i, t in enumerate(it, 1):
        print("- [ ] C%02d %s" % (i, t))
    print("\n标注：pass / fail / n-a / need-data；fail 必须回链到事实表行号。")
if __name__ == "__main__":
    main()
