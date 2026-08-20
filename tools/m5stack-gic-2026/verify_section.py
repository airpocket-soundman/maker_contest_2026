"""締切後の答え合わせセクション(HTML片)を生成する。"""
import json, math, html as H, datetime as dt

fr = json.load(open('final_result.json', encoding='utf-8'))
p = json.load(open('prediction.json', encoding='utf-8'))
pf = json.load(open('prediction_fable.json', encoding='utf-8'))
pc = json.load(open('codex_result.json', encoding='utf-8'))

FINAL = fr['listed_total']
NOW_N = fr['category_now']
daily = fr['daily_final']

MODELS = [
    ('Codex (gpt-5.6-sol)', pc['prediction'], pc['lo'], pc['hi'], 'dot3',
     '2025年の伸び率(1.52倍)をほぼそのまま適用'),
    ('Opus 5', round(p['central']), round(p['lo']), round(p['hi']), 'dot1',
     'ラッシュ再現とペース継続を0.6:0.4で加重平均'),
    ('Fable 5', round(pf['central']), round(pf['lo']), round(pf['hi']), 'dot2',
     '投稿前倒しの証拠からラッシュを割り引き、幾何平均で折衷'),
]
ranked = sorted(MODELS, key=lambda m: abs(m[1] - FINAL))

rows = ''
for rank, (name, pred, lo, hi, dot, how) in enumerate(ranked, 1):
    err = pred - FINAL
    pct = abs(err) / FINAL * 100
    inrange = 'レンジ内' if lo <= FINAL <= hi else 'レンジ外'
    rows += (f'<tr><td>{rank}</td><td><span class="{dot}"></span>{H.escape(name)}</td>'
             f'<td>{pred}</td><td>{lo}〜{hi}</td><td>{err:+d}</td><td>{pct:.1f}%</td>'
             f'<td class="dsc">{inrange} / {H.escape(how)}</td></tr>')

# 締切直前の日別(8/4以降)
bars = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>'
               for k, v in sorted(daily.items()) if k >= '2026-08-01')

html = f'''
<h2>答え合わせ: 締切後の確定値と予測の評価</h2>
<p class="sub">
締切(2026-08-07 23:59 PST = 08-08 16:59 JST)を過ぎたため、確定値との突き合わせを行いました。
<strong>コンテストカテゴリに掲載された応募作品は {FINAL} 件</strong>で確定しました
(うち締切後に公開日が付いているものが {fr['after_deadline']} 件、ページ削除済みで公開日を取得できないものが {fr['undated']} 件ありますが、
主催者のカテゴリに載っている以上は応募として扱い、すべて集計対象に含めています。締切時刻までに公開されたものだけを数えると {FINAL - fr['after_deadline']} 件です)。
</p>

<table class="mtable"><thead><tr><th>順位</th><th>モデル</th><th>予測</th><th>レンジ</th><th>誤差</th><th>誤差率</th><th>評価</th></tr></thead>
<tbody>{rows}</tbody></table>

<p class="sub"><strong>3モデルとも過小予測でした。</strong>最も近かったのはCodex({pc['prediction']}件、誤差{pc['prediction']-FINAL:+d})ですが、
それでも{abs(pc['prediction']-FINAL)/FINAL*100:.0f}%下振れしており、レンジ上限({pc['hi']}件)すら確定値に届いていません。
予測の分かれ目だった「2025年の駆け込みシェアをそのまま当てはめてよいか」という論点では、
<strong>そのまま当てはめたCodexが最も正解に近く、行動シフトを理由に割り引いたFable 5が最も外しました</strong>。</p>

<h3 class="mh">なぜ全モデルが外したのか</h3>
<p class="sub">敗因は共通していて、<strong>予測時点(8/6、締切48時間前)の143件という観測値を「ほぼ出そろった母数」と見なしたこと</strong>にあります。
実際には最後の2日間で <strong>+93件</strong>(8/7に50件、8/8に27件、8/6の残り分を含む)が投稿され、全体の <strong>{93/FINAL*100:.0f}%</strong> が最終48時間に集中しました。
2025年大会の同区間シェアは36%でしたから、今年の駆け込みは前年より<strong>さらに極端</strong>だったことになります。</p>
<p class="sub">Fable 5 が根拠にした「締切前16〜2日の投稿数が2025年9件 → 2026年73件」という前倒しの事実そのものは正しかったのですが、
そこから引いた「前倒しした分だけ駆け込み層が減る」という推論が誤りでした。実際には
<strong>母集団全体が前年より大きくなっていた</strong>(前倒し組も駆け込み組も増えた)ため、前倒しは駆け込みの代替ではなく上乗せだったことになります。
参加規模の拡大そのものを見落としていた点が、3モデル共通の構造的な誤りです。</p>

<h3 class="mh">締切前後の日別投稿数(確定)</h3>
<div class="tiles" style="align-items:flex-start">
<table class="mtable"><thead><tr><th>日付(UTC)</th><th>投稿数</th></tr></thead><tbody>{bars}</tbody></table>
</div>
<p class="sub">8/9以降の {fr['after_deadline']} 件は公開日が締切を過ぎていますが、カテゴリに掲載されているため集計に含めています(2025年大会でも締切後の追加登録が数件ありました)。審査期間は8/28まで続くため、今後もカテゴリの出入りが起こりえます。</p>
'''
open('verify_section.html', 'w', encoding='utf-8').write(html)
print('verify section written; FINAL =', FINAL)
for name, pred, lo, hi, _, _ in ranked:
    print(f'  {name:22s} {pred:4d}  err {pred-FINAL:+4d}')
