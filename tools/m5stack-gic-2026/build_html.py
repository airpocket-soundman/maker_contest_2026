import json, html as H, datetime as dt
from collections import Counter

m = json.load(open('merged2.json', encoding='utf-8'))
st = json.load(open('stats.json', encoding='utf-8'))
NAME = st['names']
full_series = st['series']
TOTAL = len(m)
NEW_N = sum(1 for e in m if e['is_new'])
DELETED = [e for e in m if '削除済み' in e['title']]
DEL_NOTE = ' と '.join(f"#{e['n']} {e['title'].replace('(削除済み)', '')}" for e in DELETED)

# The first two entries were published in January; activity then stops until May.
# Clip the plotted window so the meaningful period is not crushed by empty months.
CLIP_FROM = '2026-05-01'
series = [r for r in full_series if r['date'] >= CLIP_FROM]
CARRY = series[0]['cum'] - series[0]['n']          # entries already published before the window
early = [r for r in full_series if r['date'] < CLIP_FROM and r['n']]
EARLY_NOTE = ('なお、これ以前に ' + '、'.join(f'{r["date"]}({r["n"]}件)' for r in early)
              + f' の計{CARRY}件があり、累積はこの{CARRY}件を起点にしています。') if early else ''

lic_cnt = Counter(e['license'] for e in m).most_common()
by_proj = st['by_proj']
by_auth = dict(st['by_auth'])
n_countries = len([k for k, _ in by_proj if k != '(未設定)'])

# ---------------- Chart A: daily bars ----------------
BW, GAP, CH = 6, 2, 190
step = BW + GAP
maxn = max(r['n'] for r in series)
W = len(series) * step
lab_y = CH + 16


def ticks(maxv, n=4):
    import math
    raw = maxv / n
    mag = 10 ** math.floor(math.log10(raw)) if raw > 0 else 1
    for mult in (1, 2, 2.5, 5, 10):
        if mag * mult >= raw:
            s = mag * mult
            break
    out, v = [], 0
    while v <= maxv + 1e-9:
        out.append(v)
        v += s
    if out[-1] < maxv:          # the top tick must cover the data, or marks overflow the plot
        out.append(out[-1] + s)
    return out


ytA = ticks(maxn)
scaleA = CH / ytA[-1]
barsA, gridA, monthlab = [], [], []
prev_month = None
for i, r in enumerate(series):
    x = i * step
    h = r['n'] * scaleA
    if r['n']:
        barsA.append(
            f'<rect class="bar" x="{x}" y="{CH-h:.1f}" width="{BW}" height="{h:.1f}" rx="3" '
            f'data-d="{r["date"]}" data-n="{r["n"]}" data-c="{r["cum"]}"></rect>')
    else:
        barsA.append(
            f'<rect class="hit" x="{x}" y="0" width="{BW}" height="{CH}" fill="transparent" '
            f'data-d="{r["date"]}" data-n="0" data-c="{r["cum"]}"></rect>')
    mo = r['date'][:7]
    if mo != prev_month:
        prev_month = mo
        monthlab.append(f'<line class="mline" x1="{x-1}" y1="0" x2="{x-1}" y2="{CH}"></line>'
                        f'<text class="axis" x="{x+2}" y="{lab_y}">{mo[5:]}月</text>')
for v in ytA:
    y = CH - v * scaleA
    gridA.append(f'<line class="grid" x1="0" y1="{y:.1f}" x2="{W}" y2="{y:.1f}"></line>')

yaxA = ''.join(f'<text class="axis" x="34" y="{CH-v*scaleA+4:.1f}" text-anchor="end">{int(v)}</text>'
               for v in ytA)

# ---------------- Chart B: cumulative area+line ----------------
CW, CH2 = W, 210
maxc = series[-1]['cum']
BASE_Y = None
ytB = ticks(maxc)
scaleB = CH2 / ytB[-1]
pts = [(i * step + BW / 2, CH2 - r['cum'] * scaleB) for i, r in enumerate(series)]
line = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
area = line + f' L{pts[-1][0]:.1f},{CH2} L{pts[0][0]:.1f},{CH2} Z'
gridB = ''.join(f'<line class="grid" x1="0" y1="{CH2-v*scaleB:.1f}" x2="{CW}" y2="{CH2-v*scaleB:.1f}"></line>'
                for v in ytB)
yaxB = ''.join(f'<text class="axis" x="34" y="{CH2-v*scaleB+4:.1f}" text-anchor="end">{int(v)}</text>'
               for v in ytB)
hitB = ''.join(
    f'<rect class="hit" x="{i*step}" y="0" width="{step}" height="{CH2}" fill="transparent" '
    f'data-d="{r["date"]}" data-n="{r["n"]}" data-c="{r["cum"]}"></rect>'
    for i, r in enumerate(series))
mlineB = ''
prev_month = None
for i, r in enumerate(series):
    mo = r['date'][:7]
    if mo != prev_month:
        prev_month = mo
        x = i * step
        mlineB += (f'<line class="mline" x1="{x-1}" y1="0" x2="{x-1}" y2="{CH2}"></line>'
                   f'<text class="axis" x="{x+2}" y="{CH2+16}">{mo[5:]}月</text>')

# ---------------- Chart C: countries (profile-declared vs traced) ----------------
src = st['by_proj_src']
rows = [(k, v) for k, v in by_proj]
maxv = max(v for _, v in rows)
RH, BARH = 22, 13
CHC = len(rows) * RH
LBL = 116
BARW = 400
GAPX = 2                     # surface gap between the two stacked segments
cbars = []
for i, (k, v) in enumerate(rows):
    y = i * RH
    prof = src.get(f'{k}|profile', 0)
    trac = src.get(f'{k}|traced', 0)
    nm = '未設定' if k == '(未設定)' else NAME.get(k, k)
    cbars.append(
        f'<text class="clab" x="{LBL-8}" y="{y+BARH-2}" text-anchor="end">{H.escape(nm)}</text>')
    x = LBL
    if k == '(未設定)':
        w = v / maxv * BARW
        cbars.append(f'<rect class="bar muted" x="{x}" y="{y}" width="{w:.1f}" height="{BARH}" rx="3"></rect>')
        x += w
    else:
        if prof:
            w = prof / maxv * BARW
            cbars.append(f'<rect class="bar" x="{x}" y="{y}" width="{w:.1f}" height="{BARH}" rx="3"></rect>')
            x += w + (GAPX if trac else 0)
        if trac:
            w = trac / maxv * BARW
            cbars.append(f'<rect class="bar2" x="{x}" y="{y}" width="{w:.1f}" height="{BARH}" rx="3"></rect>')
            x += w
    extra = f' <tspan class="cval2">(うち追跡 {trac})</tspan>' if trac else ''
    cbars.append(f'<text class="cval" x="{x+7:.1f}" y="{y+BARH-2}">{v}{extra}</text>')

# ---------------- Charts D-G: parts & technology ----------------
tech = json.load(open('tech_agg.json', encoding='utf-8'))
FORECAST = open('forecast_section.html', encoding='utf-8').read()
PRED = json.load(open('prediction.json', encoding='utf-8'))
PRED_F = json.load(open('prediction_fable.json', encoding='utf-8'))
PRED_C = json.load(open('codex_result.json', encoding='utf-8'))


def hbar(rows, label_w=190, bar_w=380, row_h=21, bar_h=12):
    """One-series horizontal bar chart. Value is direct-labelled on every row."""
    if not rows:
        return ''
    mx = max(v for _, v in rows)
    out = []
    for i, (k, v) in enumerate(rows):
        y = i * row_h
        w = v / mx * bar_w
        out.append(
            f'<text class="clab" x="{label_w-8}" y="{y+bar_h-1}" text-anchor="end">{H.escape(k)}</text>'
            f'<rect class="bar" x="{label_w}" y="{y}" width="{w:.1f}" height="{bar_h}" rx="3"></rect>'
            f'<text class="cval" x="{label_w+w+7:.1f}" y="{y+bar_h-1}">{v}</text>')
    return (f'<svg width="{label_w+bar_w+60}" height="{len(rows)*row_h+6}" role="img">'
            f'<g transform="translate(0,5)">{"".join(out)}</g></svg>')


core_rows = tech['core'][:18]
tech_rows = tech['tech'][:20]
sw_rows = [(k, v) for k, v in tech['sw'] if v >= 2][:14]
unit_rows = tech['unit'][:14]
N_PARTS = tech['n_with_parts']
core_svg = hbar(core_rows, label_w=196)
tech_svg = hbar(tech_rows, label_w=210)
sw_svg = hbar([(k[:34], v) for k, v in sw_rows], label_w=228, bar_w=300)
unit_svg = hbar(unit_rows, label_w=250, bar_w=300)

# ---------------- cards ----------------
cards = []
for e in m:
    img = e['img']
    imgtag = (f'<a href="{e["url"]}" target="_blank" rel="noopener"><img loading="lazy" src="{img}" alt=""></a>'
              if img else '<div class="noimg">画像なし(ページ削除済み)</div>')
    badge = '<span class="newb">NEW</span>' if e['is_new'] else ''
    cc = e['country']
    flag = f'{NAME.get(cc, cc)}' if cc else '所在国 未設定'
    if e.get('country_src') == 'traced':
        flag += '(追跡)'
    via = (f'<p class="via" title="{H.escape(e["country_via"])}">所在国の根拠: '
           f'{H.escape(e["country_via"])}</p>') if e.get('country_via') else ''
    pub = e['published'][:10] if e['published'] else '—'
    cards.append(f'''
<article class="card{' isnew' if e['is_new'] else ''}" data-new="{str(e['is_new']).lower()}" data-c="{cc or 'NA'}" id="p{e['n']}">
  <div class="thumb">{imgtag}{badge}</div>
  <div class="body">
    <h3><span class="num">{e['n']}</span> <a href="{e['url']}" target="_blank" rel="noopener">{H.escape(e['title'])}</a></h3>
    <p class="meta">{H.escape(e['author_name'])} ・ {H.escape(flag)} ・ {pub} ・ {H.escape(e['license'])}</p>
    {via}
    <p><span class="label">概要</span>{H.escape(e['gaiyo'])}</p>
    <p><span class="label">オリジナリティ</span>{H.escape(e['orig'])}</p>
  </div>
</article>''')

lic_html = ''.join(f'<tr><td>{H.escape(k)}</td><td>{v}</td></tr>' for k, v in lic_cnt)
ctry_html = ''.join(
    f'<tr><td>{H.escape("未設定" if k == "(未設定)" else NAME.get(k, k))}</td>'
    f'<td>{by_auth.get(k, 0)}</td><td>{v}</td></tr>' for k, v in by_proj)

first, last = series[0]['date'], series[-1]['date']
peak = max(series, key=lambda r: r['n'])

page = f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>M5Stack Global Innovation Contest 2026 エントリー作品サマリ</title>
<style>
.viz-root, body {{
  --surface-1:#fcfcfb; --plane:#f9f9f7; --text-primary:#0b0b0b; --text-secondary:#52514e;
  --muted:#898781; --grid:#e1e0d9; --baseline:#c3c2b7; --series-1:#2a78d6; --series-2:#eb6834; --series-3:#1baf7a; --series-4:#4a3aa7;
  --border:rgba(11,11,11,0.10); --newc:#0ca30c;
}}
@media (prefers-color-scheme: dark) {{
  :root:where(:not([data-theme="light"])) .viz-root, :root:where(:not([data-theme="light"])) body {{
    --surface-1:#1a1a19; --plane:#0d0d0d; --text-primary:#ffffff; --text-secondary:#c3c2b7;
    --muted:#898781; --grid:#2c2c2a; --baseline:#383835; --series-1:#3987e5; --series-2:#d95926; --series-3:#199e70; --series-4:#9085e9;
    --border:rgba(255,255,255,0.10); --newc:#0ca30c;
  }}
}}
:root[data-theme="dark"] .viz-root, :root[data-theme="dark"] body {{
  --surface-1:#1a1a19; --plane:#0d0d0d; --text-primary:#ffffff; --text-secondary:#c3c2b7;
  --muted:#898781; --grid:#2c2c2a; --baseline:#383835; --series-1:#3987e5; --series-2:#d95926; --series-3:#199e70; --series-4:#9085e9;
  --border:rgba(255,255,255,0.10); --newc:#0ca30c;
}}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--plane); color:var(--text-primary);
  font-family:system-ui,-apple-system,"Segoe UI","Hiragino Kaku Gothic ProN","Yu Gothic UI",sans-serif;
  line-height:1.7; }}
.wrap {{ max-width:1080px; margin:0 auto; padding:0 20px; }}
header {{ padding:32px 0 8px; }}
h1 {{ font-size:1.5rem; margin:0 0 10px; }}
header p {{ color:var(--text-secondary); font-size:.87rem; margin:4px 0; }}
h2 {{ font-size:1.05rem; margin:34px 0 2px; }}
.sub {{ color:var(--text-secondary); font-size:.82rem; margin:0 0 12px; }}
.tiles {{ display:flex; flex-wrap:wrap; gap:10px; margin:20px 0 4px; }}
.tile {{ background:var(--surface-1); border:1px solid var(--border); border-radius:10px;
  padding:10px 16px; min-width:120px; }}
.tile .v {{ font-size:1.6rem; font-weight:600; line-height:1.2; }}
.tile .k {{ font-size:.75rem; color:var(--text-secondary); }}
figure {{ margin:0 0 8px; background:var(--surface-1); border:1px solid var(--border);
  border-radius:12px; padding:16px 12px 10px; }}
.scroll {{ overflow-x:auto; }}
.pair {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(340px,1fr)); gap:12px; }}
.pair figure {{ margin:0; }}
svg {{ display:block; }}
.bar {{ fill:var(--series-1); }}
.bar.muted {{ fill:var(--baseline); }}
.bar2 {{ fill:var(--series-2); }}
.cval2 {{ fill:var(--muted); font-size:10px; }}
.fband {{ fill:var(--series-2); opacity:.16; }}
.fcen {{ fill:none; stroke:var(--series-2); stroke-width:2.5; }}
.fhi, .flo {{ fill:none; stroke:var(--series-2); stroke-width:1; stroke-dasharray:4 3; opacity:.7; }}
.nowline {{ stroke:var(--text-secondary); stroke-width:1; stroke-dasharray:3 3; }}
.pdot {{ fill:var(--series-2); stroke:var(--surface-1); stroke-width:2; }}
.pval {{ fill:var(--series-2); font-size:13px; font-weight:700; }}
.pdot2 {{ fill:var(--series-3); stroke:var(--surface-1); stroke-width:2; }}
.pval2 {{ fill:var(--series-3); font-size:13px; font-weight:700; }}
.pdot3 {{ fill:var(--series-4); stroke:var(--surface-1); stroke-width:2; }}
.pval3 {{ fill:var(--series-4); font-size:13px; font-weight:700; }}
.mtable {{ font-size:.8rem; margin-top:8px; }}
.mtable td.dsc {{ text-align:left; color:var(--text-secondary); font-size:.76rem; }}
.mtable td:nth-child(2) {{ font-weight:700; }}
.mh {{ font-size:.98rem; margin:26px 0 2px; }}
.dot1, .dot2, .dot3 {{ display:inline-block; width:10px; height:10px; border-radius:50%;
  margin-right:6px; vertical-align:0; }}
.dot1 {{ background:var(--series-2); }}
.dot2 {{ background:var(--series-3); }}
.dot3 {{ background:var(--series-4); }}
.legend {{ display:flex; gap:16px; font-size:.78rem; color:var(--text-secondary);
  margin:0 0 10px 4px; }}
.key {{ display:inline-block; width:11px; height:11px; border-radius:3px;
  margin-right:5px; vertical-align:-1px; }}
.via {{ font-size:.72rem; color:var(--muted); margin:0 0 8px;
  border-left:2px solid var(--series-2); padding-left:7px; }}
.grid {{ stroke:var(--grid); stroke-width:1; }}
.mline {{ stroke:var(--baseline); stroke-width:1; stroke-dasharray:2 3; }}
.axis {{ fill:var(--muted); font-size:10px; font-variant-numeric:tabular-nums; }}
.clab {{ fill:var(--text-secondary); font-size:11px; }}
.cval {{ fill:var(--text-secondary); font-size:11px; font-variant-numeric:tabular-nums; }}
.aline {{ fill:none; stroke:var(--series-1); stroke-width:2; stroke-linejoin:round; }}
.afill {{ fill:var(--series-1); opacity:.14; }}
.cross {{ stroke:var(--text-secondary); stroke-width:1; stroke-dasharray:3 3; opacity:0; }}
.dot {{ fill:var(--series-1); stroke:var(--surface-1); stroke-width:2; opacity:0; }}
#tip {{ position:fixed; pointer-events:none; opacity:0; transition:opacity .1s;
  background:var(--surface-1); border:1px solid var(--border); border-radius:8px;
  padding:6px 10px; font-size:.78rem; box-shadow:0 4px 14px rgba(0,0,0,.16); z-index:9; white-space:nowrap; }}
table {{ border-collapse:collapse; font-size:.82rem; background:var(--surface-1); }}
th, td {{ border:1px solid var(--border); padding:4px 14px; text-align:left; }}
td:not(:first-child), th:not(:first-child) {{ text-align:right; font-variant-numeric:tabular-nums; }}
details {{ margin:10px 0 0; }}
summary {{ cursor:pointer; font-size:.85rem; color:var(--text-secondary); }}
.controls {{ margin:26px 0 0; display:flex; gap:8px; flex-wrap:wrap; align-items:center; }}
button {{ font:inherit; font-size:.86rem; padding:5px 14px; border-radius:20px; cursor:pointer;
  border:1px solid var(--border); background:var(--surface-1); color:var(--text-primary); }}
button.on {{ background:var(--series-1); color:#fff; border-color:var(--series-1); }}
main {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(480px,1fr)); gap:18px;
  max-width:1080px; margin:0 auto; padding:14px 20px 60px; }}
@media (max-width:560px) {{ main {{ grid-template-columns:1fr; }} }}
.card {{ background:var(--surface-1); border:1px solid var(--border); border-radius:12px;
  overflow:hidden; display:flex; flex-direction:column; }}
.card.isnew {{ border-color:var(--newc); }}
.thumb {{ position:relative; }}
.thumb img {{ width:100%; aspect-ratio:4/3; object-fit:cover; display:block; background:#000; }}
.noimg {{ aspect-ratio:4/3; display:flex; align-items:center; justify-content:center;
  color:var(--muted); background:var(--plane); font-size:.9rem; }}
.card.iswd {{ opacity:.62; }}
.newb.wdb {{ background:var(--muted); }}
.newb {{ position:absolute; top:10px; left:10px; background:var(--newc); color:#fff;
  font-size:.72rem; font-weight:700; padding:2px 9px; border-radius:4px; letter-spacing:.05em; }}
.body {{ padding:14px 18px 18px; }}
h3 {{ font-size:1.02rem; margin:0 0 4px; line-height:1.4; }}
h3 a {{ color:var(--text-primary); text-decoration:none; }}
h3 a:hover {{ color:var(--series-1); }}
.num {{ display:inline-block; min-width:2em; text-align:center; background:var(--series-1);
  color:#fff; border-radius:6px; font-size:.82rem; padding:1px 6px; margin-right:4px;
  font-variant-numeric:tabular-nums; }}
.meta {{ font-size:.75rem; color:var(--muted); margin:0 0 8px; }}
.body p {{ font-size:.87rem; margin:8px 0; }}
.label {{ display:inline-block; font-size:.71rem; font-weight:700; color:var(--series-1);
  border:1px solid var(--series-1); border-radius:4px; padding:0 6px; margin-right:6px; vertical-align:1px; }}
</style>
</head>
<body class="viz-root">
<div class="wrap">
<header>
<h1>M5Stack Global Innovation Contest 2026 エントリー作品サマリ(全{TOTAL}作品)</h1>
<p>出典: Hackster.io M5Stackコミュニティ コンテストカテゴリ(category_id=595)全9ページ / 最終更新: <strong>2026-08-07 17:18 JST</strong>(締切まで約24時間)</p>
<p>現在のエントリー数は <strong>{TOTAL}件</strong>。締切前日の駆け込みが始まっており、8/6昼(UTC)以降の新規投稿は{NEW_N}件です(NEWバッジ)。なお1件(Water Drop Survival)は公開後にコンテストカテゴリから取り下げられたため、一覧・集計から除外しています(StampFly 3D Flight Recorderは一時取り下げ後、8/7に復帰)。番号は公開日の新しい順です。</p>

<p>※ {DEL_NOTE} は作者によりページ削除済み(HTTP 410)のため、内容・投稿日とも取得できていません。画像は各作品の公開ページのカバー画像(Hackster CDN)を参照しています。</p>

<div class="tiles">
  <div class="tile"><div class="v">{TOTAL}</div><div class="k">エントリー総数</div></div>
  <div class="tile"><div class="v">{NEW_N}</div><div class="k">前回比 増加</div></div>
  <div class="tile"><div class="v">{n_countries}</div><div class="k">投稿者の所在国数</div></div>
  <div class="tile"><div class="v">{peak['n']}</div><div class="k">日別最多({peak['date'][5:].replace('-', '/')})</div></div>
  <div class="tile"><div class="v">{PRED['central']:.0f}</div><div class="k">最終予測(Opus 5)</div></div>
  <div class="tile"><div class="v">{PRED_F['central']:.0f}</div><div class="k">最終予測(Fable 5)</div></div>
  <div class="tile"><div class="v">{PRED_C['prediction']}</div><div class="k">最終予測(Codex 5.6)</div></div>
</div>

<h2>日別 投稿数の推移</h2>
<p class="sub">{first} 〜 {last}({len(series)}日間)。投稿日は各作品ページの公開日時(UTC)、日付未取得の2件は除外しています。{EARLY_NOTE}バーにカーソルを合わせると内訳が出ます。</p>
<figure>
<div class="scroll">
<svg width="{W+50}" height="{CH+30}" role="img" aria-label="日別投稿数の推移">
  <g transform="translate(44,6)">{''.join(gridA)}{''.join(monthlab)}{''.join(barsA)}
    <line class="grid" x1="0" y1="{CH}" x2="{W}" y2="{CH}" stroke="var(--baseline)"></line></g>
  <g transform="translate(0,6)">{yaxA}</g>
</svg>
</div>
</figure>

<h2>累積 投稿数の推移</h2>
<p class="sub">同期間の積算値。7月中旬から傾きが急になり、締切直前とみられる8月頭に最も伸びています。</p>
<figure>
<div class="scroll">
<svg width="{CW+50}" height="{CH2+30}" role="img" aria-label="累積投稿数の推移">
  <g transform="translate(44,6)">{gridB}{mlineB}
    <path class="afill" d="{area}"></path><path class="aline" d="{line}"></path>
    <line class="grid" x1="0" y1="{CH2}" x2="{CW}" y2="{CH2}" stroke="var(--baseline)"></line>
    <line class="cross" id="cx" x1="0" y1="0" x2="0" y2="{CH2}"></line>
    <circle class="dot" id="cdot" r="5"></circle>{hitB}</g>
  <g transform="translate(0,6)">{yaxB}</g>
</svg>
</div>
</figure>

{FORECAST}

<h2>投稿者の所在国別 作品数</h2>
<p class="sub">Hacksterプロフィールの登録国(country_iso2)を一次情報とし、未登録だった45名については作品ページに書かれたGitHub・個人サイトを辿って本人アカウントと確認できた12名を「追跡で判明」として加えています。他人のライブラリのリポジトリを参照しているだけのものは除外しました。いずれも本人が公開している所在地であり、国籍そのものではありません。残る33名は手がかりが無いか本人と断定できず「未設定」です。</p>
<div class="legend">
  <span><i class="key" style="background:var(--series-1)"></i>プロフィール登録値</span>
  <span><i class="key" style="background:var(--series-2)"></i>追跡で判明</span>
  <span><i class="key" style="background:var(--baseline)"></i>未設定</span>
</div>
<figure>
<svg width="{LBL+BARW+160}" height="{CHC+8}" role="img" aria-label="所在国別の作品数">
  <g transform="translate(0,6)">{''.join(cbars)}</g>
</svg>
</figure>

<h2>使用されたM5Stackコアデバイス</h2>
<p class="sub">各作品ページの「Things used in this project」に登録されたハードウェアを製品系列ごとにまとめたものです({N_PARTS}/{TOTAL}件が登録済み)。1作品で複数のデバイスを使う例が多いため、合計は作品数を上回ります。</p>
<figure><div class="scroll">{core_svg}</div></figure>

<h2>作品本文に現れた技術キーワード</h2>
<p class="sub">本文テキストに対するキーワード照合で、その技術に言及した作品数を数えたものです(1作品につき1回まで)。部品欄と違い作者の申告に依存しないぶん網羅性は高い一方、文脈まで判定していないため参考値として見てください。</p>
<figure><div class="scroll">{tech_svg}</div></figure>

<h2>開発環境・サービス</h2>
<p class="sub">「Software apps and online services」欄に登録されたもののうち2件以上のものです。記入は任意のため、実際の使用率はこれより高いと考えられます。</p>
<figure><div class="scroll">{sw_svg}</div></figure>

<h2>コアデバイス以外に使われた部品</h2>
<p class="sub">ハードウェア欄のうちコアデバイス以外の登録を、センサ・アクチュエータなどのカテゴリに寄せて数えたものです。</p>
<figure><div class="scroll">{unit_svg}</div></figure>

<details><summary>国別の内訳(投稿者数 / 作品数)とライセンス内訳を表で見る</summary>
<div class="tiles" style="align-items:flex-start">
<table><thead><tr><th>所在国</th><th>投稿者</th><th>作品</th></tr></thead><tbody>{ctry_html}</tbody></table>
<table><thead><tr><th>ライセンス</th><th>作品</th></tr></thead><tbody>{lic_html}</tbody></table>
</div>
</details>

<div class="controls">
  <button id="fnew">NEW({NEW_N}件)のみ表示</button>
  <button id="fjp">日本の投稿者のみ表示</button>
</div>
</header>
</div>
<main id="grid">{''.join(cards)}</main>
<div id="tip"></div>
<script>
const tip = document.getElementById('tip');
const cx = document.getElementById('cx'), cdot = document.getElementById('cdot');
document.querySelectorAll('svg [data-d]').forEach(el => {{
  el.addEventListener('mouseenter', ev => {{
    const d = el.dataset;
    tip.innerHTML = d.d + '<br>投稿 ' + d.n + ' 件 / 累積 ' + d.c + ' 件';
    tip.style.opacity = 1;
    const svg = el.ownerSVGElement;
    if (cx && svg.contains(cx)) {{
      const x = +el.getAttribute('x') + (+el.getAttribute('width')) / 2;
      cx.setAttribute('x1', x); cx.setAttribute('x2', x); cx.style.opacity = .6;
      cdot.setAttribute('cx', x);
      cdot.setAttribute('cy', {CH2} - d.c * {scaleB});
      cdot.style.opacity = 1;
    }}
  }});
  el.addEventListener('mousemove', ev => {{
    tip.style.left = Math.min(ev.clientX + 14, innerWidth - tip.offsetWidth - 8) + 'px';
    tip.style.top = (ev.clientY + 18) + 'px';
  }});
  el.addEventListener('mouseleave', () => {{
    tip.style.opacity = 0;
    if (cx) {{ cx.style.opacity = 0; cdot.style.opacity = 0; }}
  }});
}});
let fn = false, fj = false;
const bn = document.getElementById('fnew'), bj = document.getElementById('fjp');
function apply() {{
  bn.classList.toggle('on', fn); bj.classList.toggle('on', fj);
  bn.textContent = fn ? 'すべて表示({TOTAL}件)' : 'NEW({NEW_N}件)のみ表示';
  bj.textContent = fj ? '所在国で絞らない' : '日本の投稿者のみ表示';
  document.querySelectorAll('#grid .card').forEach(c => {{
    const ok = (!fn || c.dataset.new === 'true') && (!fj || c.dataset.c === 'JP');
    c.style.display = ok ? '' : 'none';
  }});
}}
bn.onclick = () => {{ fn = !fn; apply(); }};
bj.onclick = () => {{ fj = !fj; apply(); }};
</script>
</body>
</html>'''

open('m5stack_contest_2026_entries.html', 'w', encoding='utf-8').write(page)
print('html bytes:', len(page.encode('utf-8')), 'cards:', len(cards))

# ---------------- Markdown ----------------
md = [f'''# M5Stack Global Innovation Contest 2026 エントリー作品サマリ

- 出典: Hackster.io M5Stackコミュニティのコンテストカテゴリ(category_id=595)全8ページ
- 最終更新: 2026-08-06
- **エントリー数: {TOTAL}件**(前回調査の124件から{NEW_N}件増加。★=今回の新規追加分)
- うち2件(Tab5 Smart Terminal / Pocket Gambler)は作者によりページ削除済み(HTTP 410)
- 番号は公開日の新しい順

## 投稿数の推移

- 対象期間(グラフ): {first} 〜 {last}({len(series)}日間)。全体では2026-01-01〜{last}、日付取得できたのは140件
- 日別最多: {peak['date']} の {peak['n']}件
- 週別の投稿数(週の月曜日 → 件数): ''' + ', '.join(f'{k} {v}' for k, v in st['weekly']) + '''

## 投稿者の所在国(Hacksterプロフィール登録値)

| 所在国 | 投稿者数 | 作品数 |
|---|---|---|
''' + '\n'.join(
    f'| {"未設定" if k == "(未設定)" else NAME.get(k, k)} | {by_auth.get(k, 0)} | {v} |'
    for k, v in by_proj) + f'''

登録のある投稿者は87名で、所在国は{n_countries}か国。45名は国を登録しておらず「未設定」。
プロフィールページにSNSリンクは公開されていないため、SNS経由での補完はできませんでした。

## ライセンス内訳

| ライセンス | 件数 |
|---|---|
''' + '\n'.join(f'| {k} | {v} |' for k, v in lic_cnt) + f'''

## 使用されたM5Stackコアデバイス

各作品ページの部品欄({N_PARTS}/{TOTAL}件が登録済み)より。1作品で複数使う例が多く、合計は作品数を上回ります。

| デバイス | 作品数 |
|---|---|
''' + '\n'.join(f'| {k} | {v} |' for k, v in tech['core']) + '''

## 作品本文に現れた技術キーワード

本文へのキーワード照合による、その技術に言及した作品数(1作品につき1回まで)。文脈までは判定していない参考値です。

| 技術 | 作品数 |
|---|---|
''' + '\n'.join(f'| {k} | {v} |' for k, v in tech['tech']) + '''

## 開発環境・サービス(2件以上)

| ツール / サービス | 作品数 |
|---|---|
''' + '\n'.join(f'| {k} | {v} |' for k, v in tech['sw'] if v >= 2) + '''

## コアデバイス以外に使われた部品カテゴリ

| カテゴリ | 作品数 |
|---|---|
''' + '\n'.join(f'| {k} | {v} |' for k, v in tech['unit']) + '''

---
''']
for e in m:
    star = ' ★NEW' if e['is_new'] else ''
    cc = NAME.get(e['country'], e['country']) if e['country'] else '未設定'
    md.append(f'''### {e['n']}. {e['title']}{star}
- **URL**: {e['url']}
- **投稿者 / 所在国 / 投稿日**: {e['author_name']} / {cc} / {e['published'][:10] if e['published'] else '—'}
- **ライセンス**: {e['license']}
- **概要**: {e['gaiyo']}
- **オリジナリティ**: {e['orig']}
''')
open('m5stack_contest_2026_entries.md', 'w', encoding='utf-8').write('\n'.join(md))
print('md ok')
