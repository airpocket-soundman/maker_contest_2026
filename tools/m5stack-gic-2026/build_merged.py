import re, json, html as H
from collections import Counter

PAT = re.compile(
    r'### \d+\. (.+?)\n- \*\*URL\*\*: (\S+)\n'
    r'(?:- \*\*(?!概要)[^\n]*\n)*'          # skip any extra metadata bullets
    r'- \*\*概要\*\*: (.+?)\n- \*\*オリジナリティ\*\*: (.+?)(?=\n\n###|\n?$)', re.S)


def parse(path):
    md = open(path, encoding='utf-8').read()
    d = {}
    for m in PAT.finditer(md):
        title, url, g, o = m.groups()
        key = url.strip().replace('https://www.hackster.io', '')
        d[key] = dict(title=title.strip().replace(' ★NEW', ''), url=url.strip(),
                      gaiyo=g.strip(), orig=o.strip())
    return d


summaries = {}
for p in ['m5stack_contest_2026_entries.md', 'new_summaries.md', 'new_summaries3.md', 'new_summaries4.md', 'new_summaries5.md', 'new_summaries6.md', 'new_summaries7.md']:
    summaries.update(parse(p))
print('summaries:', len(summaries))

order = [l.strip() for l in open('order_final.txt') if l.strip()]
newest = set(l.strip() for l in open('urls_new7.txt') if l.strip())
withdrawn = set(l.strip() for l in open('withdrawn.txt') if l.strip())
missing = [u for u in order if u not in summaries]
print('missing summaries:', missing)

# images + licenses
img_by_url, lic_by_url = {}, {}
imgs_old = json.load(open('images.json'))
urls_old = [l.strip() for l in open('urls.txt') if l.strip()]
lic_old = json.load(open('licenses.json'))
for i, u in enumerate(urls_old, 1):
    img_by_url[u] = H.unescape(imgs_old.get(str(i), ''))
    lic_by_url[u] = lic_old.get(str(i), '')
for f in ['projects2.json', 'projects3.json', 'projects4.json', 'projects5.json', 'projects6.json', 'projects7.json']:
    for o in json.load(open(f, encoding='utf-8')):
        u = o['url'].replace('https://www.hackster.io', '')
        img_by_url[u] = o['img']
        lic_by_url[u] = o['license']

meta = json.load(open('meta.json', encoding='utf-8'))
traced = json.load(open('traced.json', encoding='utf-8'))
ainfo = json.load(open('authors_info.json', encoding='utf-8'))

merged = []
i = 0
for u in order:
    if u in withdrawn:
        continue
    i += 1
    e = dict(summaries[u])
    a = u.split('/')[1]
    lic = lic_by_url.get(u, '') or ''
    if '表示なし' in lic or not lic:
        lic = 'ライセンス表示なし'
    prof = ainfo[a]['country'] or ''
    tr = traced.get(a)
    e.update(n=i, img=img_by_url.get(u, ''), license=lic, is_new=u in newest,
             author=a, author_name=ainfo[a]['name'] or a,
             country=prof or (tr['country'] if tr else ''),
             country_src=('profile' if prof else ('traced' if tr else '')),
             country_via=(tr['via'] if tr and not prof else ''),
             published=meta[u]['published'])
    merged.append(e)

json.dump(merged, open('merged2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('merged:', len(merged), 'new:', sum(1 for e in merged if e['is_new']),
      'img:', sum(1 for e in merged if e['img']),
      'dated:', sum(1 for e in merged if e['published']),
      'country known:', sum(1 for e in merged if e['country']))
print(Counter(e['license'] for e in merged).most_common())
