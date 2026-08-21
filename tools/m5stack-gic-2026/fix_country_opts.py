"""国名テーブルの取りこぼし(PT/MX)を埋め、プルダウンでは「未設定」を末尾に置く。"""
# --- stats.py の NAME に追記 ---
s = open('stats.py', encoding='utf-8').read()
old = "'SG': 'シンガポール', 'TH': 'タイ', 'DK': 'デンマーク'}"
new = "'SG': 'シンガポール', 'TH': 'タイ', 'DK': 'デンマーク',\n        'PT': 'ポルトガル', 'MX': 'メキシコ'}"
assert s.count(old) == 1, 'NAME anchor not found'
s = s.replace(old, new)
open('stats.py', 'w', encoding='utf-8').write(s)
print('stats.py NAME extended')

# --- 「未設定」をプルダウンの末尾へ ---
s = open('build_html.py', encoding='utf-8').read()
old = """CC_OPTS = ''.join(
    f'<option value="{'NA' if k == '(未設定)' else k}">'
    f'{"未設定" if k == "(未設定)" else NAME.get(k, k)}({v})</option>'
    for k, v in by_proj)
"""
new = """_cc_rows = ([r for r in by_proj if r[0] != '(未設定)']
            + [r for r in by_proj if r[0] == '(未設定)'])   # 未設定は末尾に
CC_OPTS = ''.join(
    f'<option value="{'NA' if k == '(未設定)' else k}">'
    f'{"未設定" if k == "(未設定)" else NAME.get(k, k)}({v})</option>'
    for k, v in _cc_rows)
"""
assert s.count(old) == 1, 'CC_OPTS anchor not found'
s = s.replace(old, new)
open('build_html.py', 'w', encoding='utf-8').write(s)
print('未設定 moved to the end of the dropdown')
