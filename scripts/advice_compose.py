#!/usr/bin/env python3
"""advice_compose.py - assemble verdicts into the standard expert-advice document."""
import os, json, argparse, time
SEC = ["结论（TL;DR）", "事实（诊断行/数据）", "判断（判定·依据·取舍·边界）",
       "清单核对（pass/fail/n-a/need-data）", "改动建议（有序·可验证·可回滚）", "未覆盖与后续实验"]
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--topic", required=True)
    ap.add_argument("--verdict", required=True, help="json from expert judgement step")
    ap.add_argument("--out", help="write md to workspace path"); a = ap.parse_args()
    v = json.loads(open(a.verdict, encoding="utf-8").read())
    L = ["# Python 专家裁决 · %s · %s" % (a.topic, time.strftime("%Y-%m-%d %H:%M")), ""]
    for s in SEC:
        key = s.split("（")[0]
        L.append("## " + s)
        body = v.get(key) or v.get(s)
        if isinstance(body, list):
            L += ["- " + (json.dumps(x, ensure_ascii=False) if isinstance(x, dict) else str(x)) for x in body]
        elif body:
            L.append(str(body))
        else:
            L.append("_（缺项：本裁决未提供 %s，不得省略交付）_" % key)
        L.append("")
    L.append("_依据可追溯性：每条判断须引用 asset/knowledge/ 条目或诊断行；数字须来自 scripts/ 实测。_")
    txt = "\n".join(L)
    print(txt)
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        open(a.out, "w", encoding="utf-8").write(txt)
if __name__ == "__main__":
    main()
