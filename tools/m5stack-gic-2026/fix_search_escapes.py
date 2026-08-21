"""build_html.py の中の JS は Python の f-string リテラルなので、
JS 側で使うバックスラッシュは二重に書かないと Python に食われる。
"""
B = chr(92)  # ヒアドキュメント経由でも壊れないように、バックスラッシュは chr で作る

s = open('build_html.py', encoding='utf-8').read()
reps = [
    ("/[" + B + "uFF01-" + B + "uFF5E]/g", "/[" + B + B + "uFF01-" + B + B + "uFF5E]/g"),
    ("replace(/" + B + "u3000/g",          "replace(/" + B + B + "u3000/g"),
    ("replace(/" + B + "s+/g, ' ')",       "replace(/" + B + B + "s+/g, ' ')"),
    ("q.split(/" + B + "s+/)",             "q.split(/" + B + B + "s+/)"),
]
for old, new in reps:
    assert s.count(old) == 1, (old, s.count(old))
    s = s.replace(old, new)
open('build_html.py', 'w', encoding='utf-8').write(s)
print('escapes doubled:', len(reps))
