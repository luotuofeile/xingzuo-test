# -*- coding: utf-8 -*-
import re, io, sys
p = sys.argv[1] if len(sys.argv) > 1 else r"D:\AI_Data\timeheart\公众号运营\星座测试_托管\yunshi\month.html"
s = io.open(p, encoding="utf-8").read()
print("文件:", p, "| 大小:", len(s))

for tag in ["html", "body", "section", "div", "span"]:
    o = len(re.findall(r"<%s[ >]" % tag, s))
    c = len(re.findall(r"</%s>" % tag, s))
    print(f"{tag}: 开{o} 闭{c} " + ("OK" if o == c else "!! MISMATCH"))

ids = re.findall(r'id="([a-z]+)"', s)
print("锚点 id:", ids)
print("导航 href 数量:", s.count('<a href="#'))
print("强标签未配对:", len(re.findall(r"<strong>", s)) - len(re.findall(r"</strong>", s)))
print("残留「本周/每周」:", len(re.findall(r"本周|每周", s)))
print("残留半角逗号:", len(re.findall(r"[a-z\u4e00-\u9fff]\,", s)))