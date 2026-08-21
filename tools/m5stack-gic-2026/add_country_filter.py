"""所在国での絞り込み(プルダウン)を追加する。
日本専用ボタンはプルダウンに吸収されるので置き換える。
ついでに、表示件数カウンタを検索専用から全フィルタ共通に広げ、
Markdown 側に残っていた古い固定値も実データ由来にする。
"""
s = open('build_html.py', encoding='utf-8').read()
assert 'id="fc"' not in s, 'country filter already added'

# ---------- 1. プルダウンの選択肢を組み立てる ----------
anchor = "_as = st.get('auth_src', {})\n"
opts = (anchor +
        "CC_OPTS = ''.join(\n"
        "    f'<option value=\"{'NA' if k == '(未設定)' else k}\">'\n"
        "    f'{\"未設定\" if k == \"(未設定)\" else NAME.get(k, k)}({v})</option>'\n"
        "    for k, v in by_proj)\n")
assert s.count(anchor) == 1
s = s.replace(anchor, opts)

# ---------- 2. HTML: 日本ボタン -> プルダウン ----------
old = '  <button id="fjp">日本の投稿者のみ表示</button>\n'
new = ('  <select id="fc" aria-label="所在国で絞り込み">\n'
       '    <option value="">所在国: すべて</option>\n'
       '{CC_OPTS}  </select>\n')
assert s.count(old) == 1
s = s.replace(old, new)

# ---------- 3. CSS ----------
old = "button.on {{ background:var(--series-1); color:#fff; border-color:var(--series-1); }}\n"
new = old + ("select {{ font:inherit; font-size:.86rem; padding:5px 12px; border-radius:20px;\n"
             "  cursor:pointer; border:1px solid var(--border);\n"
             "  background:var(--surface-1); color:var(--text-primary); max-width:min(260px,60vw); }}\n"
             "select.on {{ background:var(--series-1); color:#fff; border-color:var(--series-1); }}\n")
assert s.count(old) == 1
s = s.replace(old, new)

# ---------- 4. JS ----------
old = """let fn = false, fj = false;
const bn = document.getElementById('fnew'), bj = document.getElementById('fjp');
function apply() {{
  bn.classList.toggle('on', fn); bj.classList.toggle('on', fj);
  bn.textContent = fn ? 'すべて表示({TOTAL}件)' : 'NEW({NEW_N}件)のみ表示';
  bj.textContent = fj ? '所在国で絞らない' : '日本の投稿者のみ表示';
  window.__applyCardFilters();
}}"""
new = """let fn = false;
const bn = document.getElementById('fnew'), fc = document.getElementById('fc');
function apply() {{
  bn.classList.toggle('on', fn);
  fc.classList.toggle('on', !!fc.value);
  bn.textContent = fn ? 'すべて表示({TOTAL}件)' : 'NEW({NEW_N}件)のみ表示';
  window.__applyCardFilters();
}}
fc.addEventListener('change', apply);"""
assert s.count(old) == 1
s = s.replace(old, new)

old = """    const ok = (!fn || c.dataset.new === 'true') && (!fj || c.dataset.c === 'JP')
               && c.dataset.mfilter !== 'hide'
               && terms.every(t => c.__s.indexOf(t) >= 0);"""
new = """    const ok = (!fn || c.dataset.new === 'true')
               && (!fc.value || c.dataset.c === fc.value)
               && c.dataset.mfilter !== 'hide'
               && terms.every(t => c.__s.indexOf(t) >= 0);"""
assert s.count(old) == 1
s = s.replace(old, new)

# 件数表示を検索専用から全フィルタ共通に
old = """  qhit.textContent = terms.length ? hits + ' 件ヒット' : '';
  qhit.classList.toggle('none', terms.length > 0 && hits === 0);"""
new = """  qhit.textContent = hits < {TOTAL} ? '表示 ' + hits + ' / {TOTAL} 件' : '';
  qhit.classList.toggle('none', hits === 0);"""
assert s.count(old) == 1
s = s.replace(old, new)

old = "bj.onclick = () => {{ fj = !fj; apply(); }};\n"
assert s.count(old) == 1
s = s.replace(old, '')

# ---------- 5. Markdown 側の古い固定値 ----------
old = """## 投稿者の所在国(Hacksterプロフィール登録値)"""
new = """## 投稿者の所在国(プロフィール登録値 + 追跡・調査による補完)"""
assert s.count(old) == 1
s = s.replace(old, new)

old = """登録のある投稿者は87名で、所在国は{n_countries}か国。45名は国を登録しておらず「未設定」。
プロフィールページにSNSリンクは公開されていないため、SNS経由での補完はできませんでした。"""
new = """所在国が判明している投稿者は{A_PROF + A_TRAC + A_MAN}名で、{n_countries}か国。
内訳はHacksterプロフィールの登録値が{A_PROF}名、作品ページのGitHub・個人サイトを辿って
確認できたものが{A_TRAC}名、別途の調査で確認できたものが{A_MAN}名。
残る{A_NONE}名は手がかりが無いか本人と断定できず「未設定」です。"""
assert s.count(old) == 1
s = s.replace(old, new)

open('build_html.py', 'w', encoding='utf-8').write(s)
print('country filter wired')
