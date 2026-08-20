"""M5Stack Core 風の独自ファビコンを作り、両ページの <head> に data URI で埋め込む。
実在のロゴは使わず、筐体(黒い角丸)+画面(オレンジ)+3ボタンのシルエットで表現する。
"""
from urllib.parse import quote

SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>"
    "<rect width='64' height='64' rx='13' fill='#111318'/>"
    "<rect x='7.5' y='7.5' width='49' height='34' rx='4.5' fill='#1e2128'/>"
    "<rect x='10' y='10' width='44' height='29' rx='3' fill='#ff6a00'/>"
    "<path d='M20 33V17l6 9 6-9v16' fill='none' stroke='#111318'"
    " stroke-width='3.4' stroke-linejoin='round' stroke-linecap='round'/>"
    "<path d='M44 17h-7v7h4a3.5 3.5 0 1 1-3.6 4.6'"
    " fill='none' stroke='#111318' stroke-width='3.4'"
    " stroke-linejoin='round' stroke-linecap='round'/>"
    "<circle cx='18' cy='52.5' r='4.3' fill='#c9ccd2'/>"
    "<circle cx='32' cy='52.5' r='4.3' fill='#c9ccd2'/>"
    "<circle cx='46' cy='52.5' r='4.3' fill='#c9ccd2'/>"
    "</svg>"
)
open('favicon.svg', 'w', encoding='utf-8').write(SVG)
DATA = 'data:image/svg+xml,' + quote(SVG, safe="/:='.-_~")
LINK = ('<link rel="icon" type="image/svg+xml" href="' + DATA + '">\n'
        '<link rel="apple-touch-icon" href="' + DATA + '">')

n = 0
for path, needle in [('build_html.py', '<title>M5Stack Global Innovation Contest 2026 エントリー作品サマリ</title>'),
                     ('encrypt_page.py', '<title>M5Stack Global Innovation Contest 2026</title>')]:
    s = open(path, encoding='utf-8').read()
    if 'rel="icon"' in s:
        # 既存を差し替え
        import re
        s = re.sub(r'<link rel="icon".*?>\n<link rel="apple-touch-icon".*?>', LINK, s, flags=re.S)
    else:
        assert needle in s, path
        s = s.replace(needle, needle + '\n' + LINK)
    open(path, 'w', encoding='utf-8').write(s)
    n += 1
print('favicon embedded into', n, 'templates; data URI len =', len(DATA))
