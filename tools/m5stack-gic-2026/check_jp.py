"""ユーザー調査で「所在国=日本」と判明した番号の、現状を突き合わせる。"""
import json

NUMS = [1, 6, 11, 14, 15, 21, 26, 27, 29, 31, 32, 34, 36, 40, 41, 43, 45, 48, 72, 85,
        95, 96, 105, 108, 110, 113, 114, 115, 116, 120, 121, 124, 131, 135, 142, 167, 175, 227]

m = json.load(open('merged2.json', encoding='utf-8'))
by_n = {e['n']: e for e in m}

buckets = {'already_JP': [], 'unset': [], 'conflict': []}
for n in NUMS:
    e = by_n.get(n)
    if e is None:
        buckets.setdefault('missing', []).append(n)
        continue
    c = e['country']
    row = (n, e['author'], e['author_name'], c or '(未設定)', e['country_src'], e['title'][:44])
    if c == 'JP':
        buckets['already_JP'].append(row)
    elif not c:
        buckets['unset'].append(row)
    else:
        buckets['conflict'].append(row)

for k in ('already_JP', 'unset', 'conflict', 'missing'):
    v = buckets.get(k, [])
    print(f'== {k}: {len(v)} ==')
    for r in v:
        print('  ', r)

print()
print('現在のJP総数:', sum(1 for e in m if e['country'] == 'JP'))
print('現在の未設定 :', sum(1 for e in m if not e['country']))
