import re, json, html
from collections import Counter

authors = [l.strip() for l in open('authors_clean.txt') if l.strip()]
VAL = r'("(?:[^"\\]|\\.)*"|null)'

# The user object serialises its keys alphabetically, so each field can be pinned
# by the key that follows it. That makes the match unambiguous even though the
# page embeds many other JSON objects (project records, page chrome, ...).
NEXT = {'country_iso2': 'id', 'name': 'news_role', 'city': 'created_month_year',
        'state': 'stats', 'website': None, 'bio': 'challenge_prizes'}

info = {}
for a in authors:
    s = open('profiles/' + a + '.html', encoding='utf-8', errors='ignore').read()

    def grab(key):
        nxt = NEXT.get(key)
        pat = r'"' + key + r'":\s*' + VAL + (r'\s*,\s*"' + nxt + r'"' if nxt else r'\s*\}\s*,\s*"projects"')
        m = re.search(pat, s)
        if not m:
            return None
        v = m.group(1)
        if v == 'null':
            return None
        try:
            out = html.unescape(json.loads(v))
        except Exception:
            return None
        return out or None

    info[a] = dict(country=grab('country_iso2'), city=grab('city'), state=grab('state'),
                   name=grab('name'), website=grab('website'))

bad = [a for a, v in info.items() if not v['name']]
print('name missing:', len(bad), bad)
print('country unknown:', sum(1 for v in info.values() if not v['country']))
json.dump(info, open('authors_info.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(Counter(v['country'] for v in info.values()).most_common())
for k in ['hiroshi-miki', 'akita', 'mongonta555', 'jasisz', 'thomassimmer', 'aguacatec-team', 'esbenb']:
    print(' ', k, info[k])
