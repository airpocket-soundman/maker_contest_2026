"""最終投稿数の予測(確定版)。手法と前提をすべて明記。"""
import re, json, math, datetime as dt
from collections import Counter

UTC = dt.timezone.utc
JST = dt.timezone(dt.timedelta(hours=9))

AS_OF = dt.datetime(2026, 8, 6, 7, 48, 49, tzinfo=UTC)
DL = dt.datetime(2026, 8, 8, 7, 59, tzinfo=UTC)          # 8/7 23:59 PST 表記どおり
DL_PDT = dt.datetime(2026, 8, 8, 6, 59, tzinfo=UTC)      # 実際の8月はPDTなので1時間前

m = json.load(open('merged2.json', encoding='utf-8'))
ts26 = sorted(dt.datetime.fromisoformat(e['published'].replace('Z', '+00:00'))
              for e in m if e['published'])
ts26.sort()
N_UNDATED = len(m) - len(ts26)
N_NOW = len(ts26) + N_UNDATED
h_now = (DL - AS_OF).total_seconds() / 3600

# ---- 2025年の実績カーブ ----
DL25 = dt.datetime(2025, 8, 23, 6, 59, tzinfo=UTC)
TOTAL25 = 192
h25 = []
for d, n in (('p2025', 60), ('p2025b', 20)):
    for i in range(1, n + 1):
        s = open(f'{d}/{i:02d}.html', encoding='utf-8', errors='ignore').read()
        mm = re.search(r'content="([0-9T:\-Z]+)" itemprop="datePublished"', s)
        if mm:
            t = dt.datetime.fromisoformat(mm.group(1).replace('Z', '+00:00'))
            h25.append((DL25 - t).total_seconds() / 3600)
h25.sort()
late25 = [h for h in h25 if h <= h_now]
n_at_25 = TOTAL25 - len(late25)
mult25 = TOTAL25 / n_at_25
add25 = len(late25)

# ---- 各手法 ----
days = Counter(t.date() for t in ts26)


def avg_last(nd):
    return sum(days.get((AS_OF - dt.timedelta(days=i)).date(), 0) for i in range(1, nd + 1)) / nd


def loglin(pts):
    n = len(pts)
    mx = sum(d for d, _ in pts) / n
    my = sum(math.log(c + .5) for _, c in pts) / n
    b = (sum((d - mx) * (math.log(c + .5) - my) for d, c in pts) /
         sum((d - mx) ** 2 for d, _ in pts))
    return math.exp(my - b * mx), -b


last_full = (AS_OF - dt.timedelta(days=1)).date()
fitpts, d0 = [], dt.date(2026, 5, 11)
while d0 <= last_full:
    mid = dt.datetime.combine(d0, dt.time(12), tzinfo=UTC)
    fitpts.append(((DL - mid).total_seconds() / 86400, days.get(d0, 0)))
    d0 += dt.timedelta(days=1)

A14, k14 = loglin([p for p in fitpts if p[0] <= 16])
A28, k28 = loglin([p for p in fitpts if p[0] <= 30])
rest14 = A14 / k14 * (1 - math.exp(-k14 * h_now / 24))
rest28 = A28 / k28 * (1 - math.exp(-k28 * h_now / 24))

METHODS = [
    ('A-1 2025年比例', N_NOW * mult25,
     f'2025年大会は締切{h_now:.0f}時間前に{n_at_25}件→最終{TOTAL25}件({mult25:.2f}倍)。同じ倍率を今年の{N_NOW}件に適用'),
    ('A-2 2025年加算', N_NOW + add25,
     f'2025年は最後の{h_now:.0f}時間で{add25}件が投稿された。同じ件数が上乗せされると仮定'),
    ('B-1 指数(直近14日)', N_NOW + rest14,
     f'日次投稿数を r(d)=A·exp(-k·d)(d=締切までの残り日数)とし直近14日で回帰。k={k14:.3f}/日(倍加{math.log(2)/k14:.1f}日)'),
    ('B-2 指数(直近28日)', N_NOW + rest28,
     f'同じ指数モデルを直近28日で回帰。k={k28:.3f}/日(倍加{math.log(2)/k28:.1f}日)'),
    ('C-1 直近3日平均', N_NOW + avg_last(3) * h_now / 24,
     f'加速なし。直近3日平均 {avg_last(3):.1f}件/日が締切まで続くと仮定'),
    ('C-2 直近7日平均', N_NOW + avg_last(7) * h_now / 24,
     f'加速なし。直近7日平均 {avg_last(7):.1f}件/日が締切まで続くと仮定'),
]
for n, v, d in METHODS:
    print(f'{n:20s} {v:6.0f} 件   {d}')

surge = [v for n, v, _ in METHODS if n.startswith('A')]
flat = [v for n, v, _ in METHODS if not n.startswith('A')]
CENTRAL = sum(surge) / len(surge) * .6 + sum(flat) / len(flat) * .4
LO, HI = min(flat), max(surge)
print(f'\n本命(締切ラッシュ込み) {min(surge):.0f}〜{max(surge):.0f} / '
      f'ラッシュ無し {min(flat):.0f}〜{max(flat):.0f}')
print(f'採用: 中心 {CENTRAL:.0f} 件、レンジ {LO:.0f}〜{HI:.0f} 件')

# ---- 予測曲線: 2025年の最終48時間の形状を今年にスケールして当てはめる ----
curve = []
step = 1.0
h = h_now
while h >= 0:
    consumed = sum(1 for x in late25 if x >= h)          # 2025でこの時点までに増えた分
    curve.append({'h': round(h, 2),
                  'central': N_NOW + consumed * (CENTRAL - N_NOW) / add25,
                  'hi': N_NOW + consumed * (HI - N_NOW) / add25,
                  'lo': N_NOW + (h_now - h) / 24 * avg_last(7)})
    h -= step

SURGE_LO, SURGE_HI = min(surge), max(surge)
FLAT_LO, FLAT_HI = min(flat), max(flat)
json.dump({'surge_lo': SURGE_LO, 'surge_hi': SURGE_HI, 'flat_lo': FLAT_LO, 'flat_hi': FLAT_HI,
           'as_of_utc': AS_OF.isoformat(), 'as_of_jst': AS_OF.astimezone(JST).isoformat(),
           'deadline_pst_utc': DL.isoformat(), 'deadline_pdt_utc': DL_PDT.isoformat(),
           'deadline_jst': DL.astimezone(JST).isoformat(),
           'n_now': N_NOW, 'hours_left': h_now,
           'mult25': mult25, 'add25': add25, 'n_at_25': n_at_25, 'total25': TOTAL25,
           'methods': [{'name': n, 'value': v, 'desc': d} for n, v, d in METHODS],
           'central': CENTRAL, 'lo': LO, 'hi': HI, 'curve': curve,
           'daily': {str(k): v for k, v in sorted(days.items())}},
          open('prediction.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\nprediction.json written, curve points:', len(curve))
