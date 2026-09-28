#!/usr/bin/env python3
"""knowledge_index.py - list/search the python-expert knowledge tree."""
import os, json, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TREE = os.path.join(ROOT, "asset", "knowledge_tree.json")
def load():
    return json.loads(open(TREE, encoding="utf-8").read())
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--topic"); ap.add_argument("--query")
    ap.add_argument("--list", action="store_true"); a = ap.parse_args()
    leaves = load()["leaves"]
    if a.list or not (a.topic or a.query):
        print(json.dumps([{"id": l["id"], "title": l.get("title", ""),
                           "authority": l.get("authority", ""), "knowledge": l["knowledge"]}
                          for l in leaves], ensure_ascii=False, indent=1)); return
    sel = [l for l in leaves if a.topic in (l["id"], l.get("title"))] or leaves
    out = []
    for l in sel:
        k = os.path.join(ROOT, "asset", l["knowledge"])
        body = open(k, encoding="utf-8").read() if os.path.exists(k) else ""
        if a.query:
            lines = [x for x in body.splitlines() if a.query.lower() in x.lower()]
            out.append({"topic": l["id"], "exists": bool(body), "matches": lines[:12]})
        else:
            out.append({"topic": l["id"], "path": k, "bytes": len(body),
                        "checklist": os.path.join(ROOT, "asset", l["checklist"]),
                        "head": body.splitlines()[:6]})
    print(json.dumps(out, ensure_ascii=False, indent=1))
if __name__ == "__main__":
    main()
