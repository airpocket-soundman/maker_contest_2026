"""ユーザー調査で所在国=日本と判明した作品を、著者ハンドル単位の上書き表にする。
番号(n)は再クロールでずれるので、永続化のキーには著者ハンドルを使う。
"""
import json

NUMS = [1, 6, 11, 14, 15, 21, 26, 27, 29, 31, 32, 34, 36, 40, 41, 43, 45, 48, 72, 85,
        95, 96, 105, 108, 110, 113, 114, 115, 116, 120, 121, 124, 131, 135, 142, 167, 175, 227]

m = json.load(open('merged2.json', encoding='utf-8'))
by_n = {e['n']: e for e in m}
authors = sorted({by_n[n]['author'] for n in NUMS})

# その著者の作品のうち、指定に含まれていないものがないか
listed = set(NUMS)
spill = [(e['n'], e['author'], e['title'][:50]) for e in m
         if e['author'] in authors and e['n'] not in listed]

print('指定作品数:', len(NUMS), '/ 著者数:', len(authors))
print('著者単位で当てた場合の巻き込み(指定外):', len(spill))
for r in spill:
    print('  ', r)

json.dump({a: 'JP' for a in authors}, open('jp_manual.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1, sort_keys=True)
print('wrote jp_manual.json')
