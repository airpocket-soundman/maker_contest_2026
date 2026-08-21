import json, datetime as dt
from collections import Counter

m = json.load(open('merged2.json', encoding='utf-8'))
m = [e for e in m if not e.get('withdrawn')]

# ---- daily / cumulative (UTC date of datePublished) ----
dates = [e['published'][:10] for e in m if e['published']]
c = Counter(dates)
start = dt.date.fromisoformat(min(dates))
end = dt.date.fromisoformat(max(dates))
series, cum = [], 0
d = start
while d <= end:
    k = d.isoformat()
    n = c.get(k, 0)
    cum += n
    series.append(dict(date=k, n=n, cum=cum))
    d += dt.timedelta(days=1)

print('period:', start, '->', end, f'({len(series)} days)')
print('dated projects:', len(dates), '/ undated:', len(m) - len(dates))
print('peak day:', max(series, key=lambda r: r['n']))
top = sorted(series, key=lambda r: -r['n'])[:8]
print('top days:', [(r['date'], r['n']) for r in top])

# weekly buckets
wk = Counter()
for k, v in c.items():
    dd = dt.date.fromisoformat(k)
    wk[(dd - dt.timedelta(days=dd.weekday())).isoformat()] += v
print('weekly:', sorted(wk.items()))

# ---- countries ----
NAME = {'JP': '日本', 'CN': '中国', 'US': 'アメリカ', 'BE': 'ベルギー', 'FR': 'フランス',
        'DE': 'ドイツ', 'AU': 'オーストラリア', 'IN': 'インド', 'CA': 'カナダ',
        'FI': 'フィンランド', 'NL': 'オランダ', 'KH': 'カンボジア', 'KI': 'キリバス',
        'AR': 'アルゼンチン', 'TW': '台湾', 'HR': 'クロアチア', 'CZ': 'チェコ',
        'BH': 'バーレーン', 'BR': 'ブラジル', 'RO': 'ルーマニア', 'GB': 'イギリス',
        'ES': 'スペイン', 'IT': 'イタリア', 'KR': '韓国', 'PL': 'ポーランド',
        'CH': 'スイス', 'SE': 'スウェーデン', 'AT': 'オーストリア', 'SG': 'シンガポール', 'TH': 'タイ', 'DK': 'デンマーク'}

by_proj = Counter(e['country'] or '(未設定)' for e in m)
authors, asrc = {}, {}
for e in m:
    authors[e['author']] = e['country'] or '(未設定)'
    asrc[e['author']] = e.get('country_src', '')
by_auth = Counter(authors.values())
by_proj_src = Counter((e['country'] or '(未設定)', e.get('country_src', '')) for e in m)
print()
print('country source (authors):', Counter(asrc.values()).most_common())
print('country source (projects):', Counter(e.get('country_src','') for e in m).most_common())

print()
print('--- projects by country ---')
for k, v in by_proj.most_common():
    print(f'  {NAME.get(k, k)} ({k}): {v}')
print('--- authors by country ---')
for k, v in by_auth.most_common():
    print(f'  {NAME.get(k, k)} ({k}): {v}')
print('distinct countries (declared):', len([k for k in by_auth if k != '(未設定)']))

json.dump(dict(series=series, weekly=sorted(wk.items()),
               by_proj=by_proj.most_common(), by_auth=by_auth.most_common(),
               by_proj_src={f'{k[0]}|{k[1]}': v for k, v in by_proj_src.items()},
               auth_src=dict(Counter(asrc.values())),
               names=NAME),
          open('stats.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
