"""Fable 5 としての独立予測。Opus 5 と同じ観測データ・締切を使うが、モデル構成は別。

Opus 5 との違い:
- 観測時点を再取得の 2026-08-06 08:30 UTC(17:30 JST)に更新(件数は143のまま)。
- 「2026年は投稿が前倒しされている」という行動シフトの証拠を明示的に扱う。
  2025年は締切前16日〜2日の14日間にわずか11件しか投稿がなく(そこから最後の
  48時間で69件)、2026年は同じ14日間に約90件が投稿済み。つまり2025年型の
  「直前一括投稿」層の一部が今年はすでに投稿を済ませている可能性が高く、
  2025年の駆け込みシェア36%をそのまま適用する(=223件)のは過大評価side。
- そこで駆け込み件数を「2025年再現(+69)」と「現行ペース継続(+22)」の
  幾何平均で折衷する。幾何平均は、真値の不確かさが倍率的(何倍か分からない)
  なときの標準的な折衷法。
"""
import re, json, math, datetime as dt
from collections import Counter

UTC = dt.timezone.utc
JST = dt.timezone(dt.timedelta(hours=9))

AS_OF = dt.datetime(2026, 8, 6, 8, 30, 13, tzinfo=UTC)      # 再確認時刻(143件のまま)
DL = dt.datetime(2026, 8, 8, 7, 59, tzinfo=UTC)             # 8/7 23:59 PST 表記どおり

m = json.load(open('merged2.json', encoding='utf-8'))
ts26 = sorted(dt.datetime.fromisoformat(e['published'].replace('Z', '+00:00'))
              for e in m if e['published'])
N_NOW = len(m)
h_now = (DL - AS_OF).total_seconds() / 3600

# ---- 2025年実績(較正用) ----
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
surge25 = sum(1 for h in h25 if h <= h_now)                  # 2025: 残り47.5hからの増分
pre25 = sum(1 for h in h25 if h_now < h <= h_now + 14 * 24)  # 2025: その前14日間
n_at_25 = TOTAL25 - surge25

days = Counter(t.date() for t in ts26)
pre26 = sum(v for k, v in days.items()
            if (AS_OF - dt.timedelta(days=15)).date() <= k < AS_OF.date())


def avg_last(nd):
    return sum(days.get((AS_OF - dt.timedelta(days=i)).date(), 0) for i in range(1, nd + 1)) / nd


flat_add = avg_last(3) * h_now / 24                          # 現行ペース継続の増分
share_add = N_NOW * TOTAL25 / n_at_25 - N_NOW                # シェア保存の増分
hybrid_add = math.sqrt(share_add * flat_add)                 # 幾何平均

F1 = N_NOW + share_add
F2 = N_NOW + flat_add
F3 = N_NOW + hybrid_add
CENTRAL = F3
LO, HI = F2, F1

METHODS = [
    ('F-1 シェア保存(上限側)', F1,
     f'2025年は締切{h_now:.0f}時間前時点で最終総数の{n_at_25/TOTAL25*100:.0f}%({n_at_25}/{TOTAL25}件)だった。'
     f'同じ累積シェアを仮定し 143 ÷ {n_at_25/TOTAL25:.3f} で算出'),
    ('F-2 現行ペース継続(下限側)', F2,
     f'駆け込みが起きない場合。直近3日平均 {avg_last(3):.1f}件/日 × 残り{h_now/24:.2f}日 を加算'),
    ('F-3 幾何平均ハイブリッド(採用)', F3,
     f'駆け込み増分を「2025年再現 +{share_add:.0f}件」と「ペース継続 +{flat_add:.0f}件」の'
     f'幾何平均 √({share_add:.0f}×{flat_add:.0f})≈+{hybrid_add:.0f}件 で折衷'),
]
for n, v, d in METHODS:
    print(f'{n:24s} {v:6.0f} 件   {d}')
print(f'\n行動シフトの根拠: 締切前16〜2日の投稿数は 2025年={pre25}件 に対し 2026年={pre26}件。'
      f'今年は投稿が大幅に前倒しされており、駆け込み層の一部は投稿済みとみられる。')
print(f'Fable 5 予測値: {CENTRAL:.0f} 件(レンジ {LO:.0f}〜{HI:.0f})')

json.dump({'as_of_utc': AS_OF.isoformat(), 'as_of_jst': AS_OF.astimezone(JST).isoformat(),
           'n_now': N_NOW, 'hours_left': h_now,
           'central': CENTRAL, 'lo': LO, 'hi': HI,
           'share_add': share_add, 'flat_add': flat_add, 'hybrid_add': hybrid_add,
           'pre25': pre25, 'pre26': pre26, 'surge25': surge25, 'n_at_25': n_at_25,
           'methods': [{'name': n, 'value': v, 'desc': d} for n, v, d in METHODS]},
          open('prediction_fable.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---- Codex に渡す共通データパック(同じ情報)----
json.dump({
    'task': 'M5Stack Global Innovation Contest 2026 の最終投稿数を予測せよ',
    'as_of_utc': AS_OF.isoformat(),
    'current_entries': N_NOW,
    'deadline_utc': DL.isoformat(),
    'deadline_note': '公式表記 2026-08-07 23:59 PST(8月の実際の太平洋時間はPDTで1時間早い可能性あり)',
    'daily_counts_2026': {str(k): v for k, v in sorted(days.items())},
    'undated_entries': N_NOW - len(ts26),
    'calibration_2025': {
        'total_final': TOTAL25,
        'note': '前年大会(2025)。応募期間5/19-8/22。新しい順80件の投稿時刻から算出した「締切までの残り時間(時間)」のリスト',
        'hours_before_deadline_newest80': [round(h, 2) for h in h25],
    },
}, open('model_input.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\nmodel_input.json written for Codex')
