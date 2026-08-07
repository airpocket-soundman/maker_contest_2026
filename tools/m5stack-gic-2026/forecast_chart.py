"""予測セクション(グラフ+3モデル並記)のHTML片を生成し build_html.py から読み込ませる。"""
import json, math, html as H, datetime as dt

p = json.load(open('prediction.json', encoding='utf-8'))        # Opus 5
pf = json.load(open('prediction_fable.json', encoding='utf-8'))  # Fable 5
pc = json.load(open('codex_result.json', encoding='utf-8'))      # Codex gpt-5.6-sol
JST = dt.timezone(dt.timedelta(hours=9))

W, Hh = 720, 230
PAD_L, PAD_B = 44, 26
N0, CEN, LO, HI = p['n_now'], p['central'], p['lo'], p['hi']
h_now = p['hours_left']

X_SPAN = 7 * 24 + 0.0
Y_MAX = math.ceil(max(HI, pf['hi'], pc['hi']) / 50) * 50


def X(h):
    return PAD_L + (X_SPAN - h) / X_SPAN * (W - PAD_L - 40)


def Y(v):
    return (Hh - PAD_B) - v / Y_MAX * (Hh - PAD_B - 12)


# --- 実績(直近7日の累積) ---
daily = p['daily']
dl = dt.datetime.fromisoformat(p['deadline_pst_utc'])
BASE = N0 - sum(daily.values())
run, pts = 0, []
for k in sorted(daily):
    run += daily[k]
    end = dt.datetime.fromisoformat(k + 'T23:59:59+00:00')
    hrem = (dl - end).total_seconds() / 3600
    if 0 <= hrem <= X_SPAN:
        pts.append((hrem, run + BASE))
pts.append((h_now, N0))
obs_path = 'M' + ' L'.join(f'{X(h):.1f},{Y(v):.1f}' for h, v in pts) if pts else ''

# --- Opus 予測バンドと中心線(2025年ラッシュ形状) ---
cv = p['curve']
cen_path = 'M' + ' L'.join(f'{X(c["h"]):.1f},{Y(c["central"]):.1f}' for c in cv)
hi_path = 'M' + ' L'.join(f'{X(c["h"]):.1f},{Y(c["hi"]):.1f}' for c in cv)
lo_path = 'M' + ' L'.join(f'{X(c["h"]):.1f},{Y(c["lo"]):.1f}' for c in cv)
band = ('M' + ' L'.join(f'{X(c["h"]):.1f},{Y(c["hi"]):.1f}' for c in cv) +
        ' L' + ' L'.join(f'{X(c["h"]):.1f},{Y(c["lo"]):.1f}' for c in reversed(cv)) + ' Z')

grid, yax = [], []
v = 0
while v <= Y_MAX:
    grid.append(f'<line class="grid" x1="{PAD_L}" y1="{Y(v):.1f}" x2="{W-40}" y2="{Y(v):.1f}"></line>')
    yax.append(f'<text class="axis" x="{PAD_L-8}" y="{Y(v)+4:.1f}" text-anchor="end">{v}</text>')
    v += 50
xlab = []
for d in range(7, -1, -1):
    h = d * 24
    lab = '締切' if d == 0 else f'-{d}d'
    xlab.append(f'<line class="mline" x1="{X(h):.1f}" y1="12" x2="{X(h):.1f}" y2="{Hh-PAD_B}"></line>'
                f'<text class="axis" x="{X(h):.1f}" y="{Hh-PAD_B+15}" text-anchor="middle">{lab}</text>')

svg = f'''<svg width="{W}" height="{Hh}" role="img" aria-label="最終投稿数の予測">
 {''.join(grid)}{''.join(xlab)}
 <path class="fband" d="{band}"></path>
 <path class="fhi" d="{hi_path}"></path>
 <path class="flo" d="{lo_path}"></path>
 <path class="fcen" d="{cen_path}"></path>
 <path class="aline" d="{obs_path}"></path>
 <line class="nowline" x1="{X(h_now):.1f}" y1="12" x2="{X(h_now):.1f}" y2="{Hh-PAD_B}"></line>
 <text class="axis" x="{X(h_now):.1f}" y="9" text-anchor="middle">現在 {N0}</text>
 <circle class="pdot" cx="{X(0):.1f}" cy="{Y(CEN):.1f}" r="4.5"></circle>
 <text class="pval" x="{X(0)-8:.1f}" y="{Y(CEN)-9:.1f}" text-anchor="end">Opus {CEN:.0f}</text>
 <circle class="pdot2" cx="{X(0):.1f}" cy="{Y(pf['central']):.1f}" r="4.5"></circle>
 <text class="pval2" x="{X(0)-8:.1f}" y="{Y(pf['central'])+16:.1f}" text-anchor="end">Fable {pf['central']:.0f}</text>
 <circle class="pdot3" cx="{X(0):.1f}" cy="{Y(pc['prediction']):.1f}" r="4.5"></circle>
 <text class="pval3" x="{X(0)-8:.1f}" y="{Y(pc['prediction'])-9:.1f}" text-anchor="end">Codex {pc['prediction']}</text>
 {''.join(yax)}
</svg>'''


def mrows(methods):
    return ''.join(
        f'<tr><td>{H.escape(mm["name"])}</td><td>{mm["value"]:.0f}</td>'
        f'<td class="dsc">{H.escape(mm["desc"])}</td></tr>' for mm in methods)


# Codex の手法を他モデルと同粒度に展開(自己申告+検算)
codex_methods = [
    dict(name='X-1 締切後投稿の除外', value=187,
         desc='2025年の投稿時刻リストから締切後の5件を除外し、締切時点の実質最終数を187件と再定義(全体は192件)'),
    dict(name='X-2 倍率適用(採用)', value=143 * 187 / 123,
         desc=f'2025年は締切{h_now:.0f}時間前に123件→締切時187件(1.52倍)。同じ倍率を現在143件に乗算: 143 × 187/123 ≈ 217件'),
    dict(name='X-3 レンジ設定', value=pc['prediction'],
         desc='倍率(比率推定)の統計的不確実性を反映して 200〜240件(Codex自己申告。分布の詳細は開示されていない)'),
]

as_of_o = dt.datetime.fromisoformat(p['as_of_jst'])
as_of_f = dt.datetime.fromisoformat(pf['as_of_jst'])
dl_jst = dt.datetime.fromisoformat(p['deadline_jst'])

html = f'''
<h2>最終投稿数の予測(3モデル比較)</h2>
<p class="sub">
応募締切は公式サイト記載の <strong>2026-08-07 23:59 PST</strong>(= {dl_jst:%Y-%m-%d %H:%M} JST)。8月の米西海岸は実際にはPDT(UTC-7)のため、表記どおりPSTと解釈した場合より締切が1時間早い可能性があります(全モデルともPST表記どおりを採用)。
3モデルとも同一の観測データ(2026年の日別投稿数、および前年2025年大会=最終192件の投稿時刻リスト)から独立に算出しています。観測値はいずれも <strong>143件</strong> です。
</p>
<p class="sub"><strong>経過メモ</strong>(予測値は算出時点の記録として固定):<br>・8/7 07:55 JST — 142件。前夜から新規0件、1件(StampFly)がカテゴリ取り下げ。<br>・8/7 12:16 JST — <strong>162件</strong>。駆け込み開始、約14時間で+20件(8/6 21:15〜8/7 10:49 JST公開)。締切まで残り約29時間での必要増分は Codex +55 / Opus +34 / Fable +23。現在のペースが続けば3モデルとも射程内で、ラッシュの規模が Codex(2025年再現)と Fable(前倒し割引)のどちらに近いかが決まり手になります。<br>・8/7 14:01 JST — <strong>162件</strong>。新規1件(Makerchip Decorder)、1件(Water Drop Survival)がカテゴリ取り下げで差し引きゼロ。残り約27時間、必要増分は Codex +55 / Opus +34 / Fable +23。<br>・8/7 17:18 JST — <strong>163件</strong>。一時取り下げされていたStampFly 3D Flight Recorderがカテゴリに復帰(+1)。新規投稿はなし。残り約24時間、必要増分は Codex +54 / Opus +33 / Fable +22。</p>

<table class="mtable"><thead><tr><th>モデル</th><th>予測値</th><th>レンジ</th><th>算出時刻</th><th>一言でいうと</th></tr></thead><tbody>
<tr><td><span class="dot3"></span>Codex (gpt-5.6-sol)</td><td>{pc['prediction']}</td><td>{pc['lo']}〜{pc['hi']}</td><td>{H.escape(pc['as_of_jst'])} JST</td><td class="dsc">2025年の伸び率をほぼそのまま適用(ラッシュ再現前提)</td></tr>
<tr><td><span class="dot1"></span>Opus 5</td><td>{CEN:.0f}</td><td>{LO:.0f}〜{HI:.0f}</td><td>{as_of_o:%m-%d %H:%M} JST</td><td class="dsc">ラッシュ再現とペース継続を0.6:0.4で加重平均</td></tr>
<tr><td><span class="dot2"></span>Fable 5</td><td>{pf['central']:.0f}</td><td>{pf['lo']:.0f}〜{pf['hi']:.0f}</td><td>{as_of_f:%m-%d %H:%M} JST</td><td class="dsc">投稿前倒しの証拠からラッシュを割り引き、幾何平均で折衷</td></tr>
</tbody></table>

<figure><div class="scroll">{svg}</div></figure>
<div class="legend">
  <span><i class="key" style="background:var(--series-1)"></i>実績</span>
  <span><i class="key" style="background:var(--series-2)"></i>Opus 5(中心線とレンジ帯)</span>
  <span><i class="key" style="background:var(--series-3)"></i>Fable 5</span>
  <span><i class="key" style="background:var(--series-4)"></i>Codex</span>
</div>
<p class="sub">中心線とレンジ帯はOpus 5のもので、2025年大会の最終48時間の投稿形状(時間刻み)を今年の規模にスケールして描いています。FableとCodexは締切時点の予測値をマーカーで示しています。</p>

<h3 class="mh"><span class="dot3"></span>Codex(gpt-5.6-sol)予測値: {pc['prediction']} 件(レンジ {pc['lo']}〜{pc['hi']})</h3>
<p class="sub">実行時刻 {H.escape(pc['as_of_jst'])} JST / {H.escape(pc['cli'])} / reasoning effort: {H.escape(pc['effort'])} / 消費トークン約{pc['tokens']:,}。
OpenAIのCodex CLIに同一データ(model_input.json)を渡して非対話実行した結果で、以下の手法はCodexの自己申告を検算のうえ展開したものです。</p>
<table class="mtable"><thead><tr><th>手法</th><th>値</th><th>計算方法</th></tr></thead><tbody>{mrows(codex_methods)}</tbody></table>
<p class="sub">特徴: 3モデル中で唯一「2025年の締切後投稿」をノイズとして除外した一方、2025年のラッシュがそのまま再現される前提のため上限側の予測。行動変化(前倒し)の補正はしていません。</p>

<h3 class="mh"><span class="dot1"></span>Opus 5 予測値: {CEN:.0f} 件(レンジ {LO:.0f}〜{HI:.0f})</h3>
<p class="sub">算出時刻 {as_of_o:%Y-%m-%d %H:%M} JST。6つの手法を計算し、締切ラッシュを織り込むA系({p['surge_lo']:.0f}〜{p['surge_hi']:.0f}件)に0.6、ラッシュ無しのB・C系({p['flat_lo']:.0f}〜{p['flat_hi']:.0f}件)に0.4の重みを付けた加重平均を採用。
較正には2025年実績(締切{h_now:.0f}時間前に{p['n_at_25']}件→最終{p['total25']}件、最後の48時間だけで{p['add25']}件=全体の36%)を使用しています。</p>
<table class="mtable"><thead><tr><th>手法</th><th>値</th><th>計算方法</th></tr></thead><tbody>{mrows(p['methods'])}</tbody></table>
<p class="sub">特徴: 複数手法のアンサンブルでレンジが最も広く、中庸の予測。重み0.6:0.4は「ラッシュは起きるが規模は不確か」という判断による設定値で、ここに恣意性が残ります。</p>

<h3 class="mh"><span class="dot2"></span>Fable 5 予測値: {pf['central']:.0f} 件(レンジ {pf['lo']:.0f}〜{pf['hi']:.0f})</h3>
<p class="sub">算出時刻 {as_of_f:%Y-%m-%d %H:%M} JST。Opus 5と同じ較正データを使いつつ、「今年は投稿が前倒しされている」という行動シフトを明示的に織り込みます。
根拠: 締切前16〜2日の投稿数が2025年={pf['pre25']}件に対し2026年={pf['pre26']}件。2025年型の駆け込み層の一部はすでに投稿済みとみられ、駆け込みシェアのそのまま適用は上限とみなします。</p>
<table class="mtable"><thead><tr><th>手法</th><th>値</th><th>計算方法</th></tr></thead><tbody>{mrows(pf['methods'])}</tbody></table>
<p class="sub">特徴: 行動変化を織り込んだ分3モデル中で最も低い予測。幾何平均は「真の駆け込み規模が何倍かわからない」タイプの不確かさに対する標準的な折衷ですが、2倍率の中間を取る以上の理論的裏付けはありません。</p>

<h3 class="mh">共通の前提と限界</h3>
<p class="sub">(1) 較正に使える前年大会が1回分しかなく、2025年の締切ラッシュが再現される保証はありません。
(2) 2026年は締切{h_now:.0f}時間前で143件と2025年同時点(123件)を{(143/123-1)*100:.0f}%上回っており、母数・行動とも同一ではありません。
(3) いずれも削除済み2件を含む「公開ページ数」の予測であり、実際の有効応募数(別途Googleフォーム提出が必要)とは一致しません。
(4) 2025年には締切後の追加登録が数件ありました(Codexのみ除外、Opus/Fableは含む——このため同じ「シェア保存」でも上限値が223件と217件に分かれています)。
(5) 答え合わせは締切後(2026-08-08 16:59 JST以降)の再集計で可能です。</p>
'''
open('forecast_section.html', 'w', encoding='utf-8').write(html)
print('written; Opus', round(CEN), 'Fable', round(pf['central']), 'Codex', pc['prediction'])
