import re, json, html as H
from collections import Counter

merged = json.load(open('merged2.json', encoding='utf-8'))
meta = json.load(open('meta.json', encoding='utf-8'))

SEC = {'hardware components': 'hw',
       'software apps and online services': 'sw',
       'hand tools and fabrication machines': 'tool'}


def clean(t):
    t = re.sub(r'<[^>]+>', ' ', t)
    t = H.unescape(t)
    t = t.replace('×', ' ')
    return re.sub(r'\s+', ' ', t).strip(' -–—,')


out = {}
for e in merged:
    key = e['url'].replace('https://www.hackster.io', '')
    s = open(meta[key]['file'], encoding='utf-8', errors='ignore').read()
    i = s.find('Things used in this project')
    j = s.find('<section id="story"')
    blk = s[i:j] if (i != -1 and j > i) else ''
    parts = {'hw': [], 'sw': [], 'tool': []}
    if blk:
        chunks = re.split(r'<tr class="head">', blk)
        for ch in chunks[1:]:
            h3 = re.search(r'<h3[^>]*>(.*?)</h3>', ch, re.S)
            sec = SEC.get(clean(h3.group(1)).lower() if h3 else '', None)
            if not sec:
                continue
            rows = re.split(r'<td class="part-img">', ch)[1:]
            for r in rows:
                qty = re.search(r'quantity">\s*(\d+)', r)
                a = re.search(r'<a[^>]*href="[^"]*/products/[^"]*"[^>]*>(.*?)</a>', r, re.S)
                if a:
                    name = clean(a.group(1))
                else:
                    body = re.split(r'class="[^"]*times"', r)[0]
                    body = re.sub(r'<a\b[^>]*>.*?</a>', ' ', body, flags=re.S)
                    name = clean(body)
                name = re.sub(r'\s{2,}', ' ', name).strip()
                if name and len(name) < 120:
                    parts[sec].append({'name': name, 'qty': int(qty.group(1)) if qty else 1})
    out[key] = parts

json.dump(out, open('parts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
n_hw = sum(1 for v in out.values() if v['hw'])
print('projects with hardware list:', n_hw, '/', len(out))
print('projects with software list:', sum(1 for v in out.values() if v['sw']))
print('total hw rows:', sum(len(v['hw']) for v in out.values()))
print()
print('--- top raw hardware names ---')
for k, v in Counter(p['name'] for v in out.values() for p in v['hw']).most_common(40):
    print(f'  {v:3d}  {k}')
print()
print('--- top raw software names ---')
for k, v in Counter(p['name'] for v in out.values() for p in v['sw']).most_common(30):
    print(f'  {v:3d}  {k}')
