"""jp_manual.json(調査で判明した所在国)をパイプラインに通す。
 - build_merged.py : プロフィール/追跡より優先して country を上書きし、country_src='manual'
 - stats.py        : 著者単位の出所内訳を stats.json に出す(説明文の数字を実データ由来にするため)
 - build_html.py   : 所在国グラフに3本目のセグメント、凡例、カードの (調査) バッジ、説明文の自動化
"""
import io

# ---------- build_merged.py ----------
s = open('build_merged.py', encoding='utf-8').read()
assert 'jp_manual' not in s, 'build_merged already wired'

old = "ainfo = json.load(open('authors_info.json', encoding='utf-8'))"
new = (old + "\n"
       "# ユーザーの調査で所在国が判明した著者。プロフィール登録値・追跡より優先する。\n"
       "manual = json.load(open('jp_manual.json', encoding='utf-8'))")
assert s.count(old) == 1
s = s.replace(old, new)

old = """    prof = ainfo[a]['country'] or ''
    tr = traced.get(a)
    e.update(n=i, img=img_by_url.get(u, ''), license=lic, is_new=u in newest,
             author=a, author_name=ainfo[a]['name'] or a,
             country=prof or (tr['country'] if tr else ''),
             country_src=('profile' if prof else ('traced' if tr else '')),
             country_via=(tr['via'] if tr and not prof else ''),
             published=meta[u]['published'])"""
new = """    prof = ainfo[a]['country'] or ''
    tr = traced.get(a)
    man = manual.get(a, '')
    if man:
        cc, csrc, cvia = man, 'manual', '調査による確認(手動指定)'
    elif prof:
        cc, csrc, cvia = prof, 'profile', ''
    elif tr:
        cc, csrc, cvia = tr['country'], 'traced', tr['via']
    else:
        cc, csrc, cvia = '', '', ''
    e.update(n=i, img=img_by_url.get(u, ''), license=lic, is_new=u in newest,
             author=a, author_name=ainfo[a]['name'] or a,
             country=cc, country_src=csrc, country_via=cvia,
             published=meta[u]['published'])"""
assert s.count(old) == 1
s = s.replace(old, new)
open('build_merged.py', 'w', encoding='utf-8').write(s)
print('build_merged.py wired')

# ---------- stats.py ----------
s = open('stats.py', encoding='utf-8').read()
assert 'auth_src' not in s
old = """json.dump(dict(series=series, weekly=sorted(wk.items()),
               by_proj=by_proj.most_common(), by_auth=by_auth.most_common(),
               by_proj_src={f'{k[0]}|{k[1]}': v for k, v in by_proj_src.items()},
               names=NAME),"""
new = """json.dump(dict(series=series, weekly=sorted(wk.items()),
               by_proj=by_proj.most_common(), by_auth=by_auth.most_common(),
               by_proj_src={f'{k[0]}|{k[1]}': v for k, v in by_proj_src.items()},
               auth_src=dict(Counter(asrc.values())),
               names=NAME),"""
assert s.count(old) == 1
s = s.replace(old, new)
open('stats.py', 'w', encoding='utf-8').write(s)
print('stats.py wired')

# ---------- build_html.py ----------
s = open('build_html.py', encoding='utf-8').read()
assert "'manual'" not in s

# (a) 3本目のセグメント
old = """    prof = src.get(f'{k}|profile', 0)
    trac = src.get(f'{k}|traced', 0)"""
new = """    prof = src.get(f'{k}|profile', 0)
    trac = src.get(f'{k}|traced', 0)
    manu = src.get(f'{k}|manual', 0)"""
assert s.count(old) == 1
s = s.replace(old, new)

old = """        if trac:
            w = trac / maxv * BARW
            cbars.append(f'<rect class="bar2" x="{x}" y="{y}" width="{w:.1f}" height="{BARH}" rx="3"></rect>')
            x += w
    extra = f' <tspan class="cval2">(うち追跡 {trac})</tspan>' if trac else ''"""
new = """        if trac:
            w = trac / maxv * BARW
            cbars.append(f'<rect class="bar2" x="{x}" y="{y}" width="{w:.1f}" height="{BARH}" rx="3"></rect>')
            x += w + (GAPX if manu else 0)
        if manu:
            w = manu / maxv * BARW
            cbars.append(f'<rect class="bar3" x="{x}" y="{y}" width="{w:.1f}" height="{BARH}" rx="3"></rect>')
            x += w
    note = ([f'追跡 {trac}'] if trac else []) + ([f'調査 {manu}'] if manu else [])
    extra = f' <tspan class="cval2">(うち{" / ".join(note)})</tspan>' if note else ''"""
assert s.count(old) == 1
s = s.replace(old, new)

# (b) bar3 の色
old = ".bar2 {{ fill:var(--series-2); }}\n"
new = old + ".bar3 {{ fill:var(--series-3); }}\n"
assert s.count(old) == 1
s = s.replace(old, new)

# (c) カードのバッジ
old = """    if e.get('country_src') == 'traced':
        flag += '(追跡)'"""
new = """    if e.get('country_src') == 'traced':
        flag += '(追跡)'
    elif e.get('country_src') == 'manual':
        flag += '(調査)'"""
assert s.count(old) == 1
s = s.replace(old, new)

# (d) 説明文と凡例(数字は実データから)
old = '''<p class="sub">Hacksterプロフィールの登録国(country_iso2)を一次情報とし、未登録だった45名については作品ページに書かれたGitHub・個人サイトを辿って本人アカウントと確認できた12名を「追跡で判明」として加えています。他人のライブラリのリポジトリを参照しているだけのものは除外しました。いずれも本人が公開している所在地であり、国籍そのものではありません。残る33名は手がかりが無いか本人と断定できず「未設定」です。</p>'''
new = '''<p class="sub">Hacksterプロフィールの登録国(country_iso2)を一次情報({A_PROF}名)とし、未登録だった著者のうち作品ページのGitHub・個人サイトを辿って本人アカウントと確認できた{A_TRAC}名を「追跡で判明」、別途の調査で所在国を確認できた{A_MAN}名を「調査で判明」として加えています。他人のライブラリのリポジトリを参照しているだけのものは除外しました。いずれも本人が公開している所在地であり、国籍そのものではありません。残る{A_NONE}名は手がかりが無いか本人と断定できず「未設定」です。</p>'''
assert s.count(old) == 1
s = s.replace(old, new)

old = '''  <span><i class="key" style="background:var(--series-2)"></i>追跡で判明</span>'''
new = old + '''
  <span><i class="key" style="background:var(--series-3)"></i>調査で判明</span>'''
assert s.count(old) == 1
s = s.replace(old, new)

# (e) A_* を算出
anchor = "# ---------------- Chart C: countries (profile-declared vs traced) ----------------\n"
calc = (anchor
        + "_as = st.get('auth_src', {})\n"
        + "A_PROF, A_TRAC = _as.get('profile', 0), _as.get('traced', 0)\n"
        + "A_MAN, A_NONE = _as.get('manual', 0), _as.get('', 0)\n")
assert s.count(anchor) == 1
s = s.replace(anchor, calc)

open('build_html.py', 'w', encoding='utf-8').write(s)
print('build_html.py wired')
