"""作品のキーワード検索(絞り込み + ヒット箇所ハイライト)を build_html.py に追加する。
CSS/HTML/JS は f-string の中に入るので、リテラルの波括弧は {{ }} で書く。
"""
s = open('build_html.py', encoding='utf-8').read()
assert 'id="q"' not in s, 'search already added'

# ---------- 1. CSS ----------
anchor = '.controls {{ margin:26px 0 0; display:flex; gap:8px; flex-wrap:wrap; align-items:center; }}\n'
css = anchor + """.qwrap {{ position:relative; display:flex; align-items:center; }}
#q {{ font:inherit; font-size:.86rem; width:min(320px,58vw); box-sizing:border-box;
  padding:5px 30px 5px 13px; border-radius:20px; border:1px solid var(--border);
  background:var(--surface-1); color:var(--text-primary); }}
#q::placeholder {{ color:var(--muted); }}
#q:focus {{ outline:2px solid var(--series-1); outline-offset:1px; }}
#qclear {{ position:absolute; right:2px; border:none; background:none; color:var(--muted);
  font-size:1rem; line-height:1; padding:4px 8px; border-radius:50%; }}
#qhit {{ font-size:.82rem; color:var(--text-secondary); font-variant-numeric:tabular-nums; }}
#qhit.none {{ color:var(--series-2); }}
mark.hit {{ background:rgba(235,104,52,.3); color:inherit; border-radius:2px; padding:0 1px; }}
"""
assert anchor in s
s = s.replace(anchor, css, 1)

# ---------- 2. HTML ----------
old = '''<div class="controls">
  <button id="fnew">NEW({NEW_N}件)のみ表示</button>'''
new = '''<div class="controls">
  <span class="qwrap">
    <input id="q" type="search" placeholder="キーワードで検索(スペース区切りでAND)"
           autocomplete="off" spellcheck="false" aria-label="作品をキーワード検索">
    <button id="qclear" type="button" title="検索をクリア" aria-label="検索をクリア">&times;</button>
  </span>
  <span id="qhit" role="status" aria-live="polite"></span>
  <span style="color:var(--muted)">|</span>
  <button id="fnew">NEW({NEW_N}件)のみ表示</button>'''
assert old in s
s = s.replace(old, new, 1)

# ---------- 3. JS ----------
old_js = '''window.__applyCardFilters = function () {{
  document.querySelectorAll('#grid .card').forEach(c => {{
    const ok = (!fn || c.dataset.new === 'true') && (!fj || c.dataset.c === 'JP')
               && c.dataset.mfilter !== 'hide';
    c.style.display = ok ? '' : 'none';
  }});
}};'''
new_js = '''const CARDS = [].slice.call(document.querySelectorAll('#grid .card'));
const qbox = document.getElementById('q'), qclear = document.getElementById('qclear'),
      qhit = document.getElementById('qhit');
let terms = [], marked = [];

// 全角英数と全角スペースだけを畳む。1文字→1文字なので、
// 正規化後の添字をそのまま元テキストの添字として使える(ハイライトに必要)。
function norm(t) {{
  return t.replace(/[\\uFF01-\\uFF5E]/g, c => String.fromCharCode(c.charCodeAt(0) - 0xFEE0))
          .replace(/\\u3000/g, ' ').toLowerCase();
}}

// カードごとの検索対象テキスト(メモ欄は除く)を一度だけ作る
CARDS.forEach(c => {{
  const b = c.querySelector('.body').cloneNode(true);
  b.querySelectorAll('.marks').forEach(n => n.remove());
  c.__s = norm(b.textContent.replace(/\\s+/g, ' '));
}});

function unmark(root) {{
  root.querySelectorAll('mark.hit').forEach(m => m.replaceWith(document.createTextNode(m.textContent)));
  root.normalize();
}}
function clearMarks() {{ marked.forEach(unmark); marked = []; }}

function markAll(root) {{
  const nodes = [], w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
  for (let n; (n = w.nextNode());) {{
    if (n.data.trim() && !n.parentNode.closest('.marks, .label, script, style')) nodes.push(n);
  }}
  let any = false;
  nodes.forEach(node => {{
    const raw = node.data, nk = norm(raw), hits = [];
    terms.forEach(t => {{
      for (let i = nk.indexOf(t); i >= 0; i = nk.indexOf(t, i + t.length)) hits.push([i, i + t.length]);
    }});
    if (!hits.length) return;
    hits.sort((a, b) => a[0] - b[0]);
    const seg = [];
    hits.forEach(h => {{
      const last = seg[seg.length - 1];
      if (last && h[0] <= last[1]) last[1] = Math.max(last[1], h[1]);
      else seg.push(h.slice());
    }});
    const frag = document.createDocumentFragment();
    let pos = 0;
    seg.forEach(h => {{
      if (h[0] > pos) frag.appendChild(document.createTextNode(raw.slice(pos, h[0])));
      const m = document.createElement('mark');
      m.className = 'hit'; m.textContent = raw.slice(h[0], h[1]);
      frag.appendChild(m); pos = h[1];
    }});
    if (pos < raw.length) frag.appendChild(document.createTextNode(raw.slice(pos)));
    node.replaceWith(frag);
    any = true;
  }});
  if (any) marked.push(root);
}}

window.__applyCardFilters = function () {{
  clearMarks();
  let hits = 0;
  CARDS.forEach(c => {{
    const ok = (!fn || c.dataset.new === 'true') && (!fj || c.dataset.c === 'JP')
               && c.dataset.mfilter !== 'hide'
               && terms.every(t => c.__s.indexOf(t) >= 0);
    c.style.display = ok ? '' : 'none';
    if (ok) hits++;
  }});
  qhit.textContent = terms.length ? hits + ' 件ヒット' : '';
  qhit.classList.toggle('none', terms.length > 0 && hits === 0);
  qclear.style.display = qbox.value ? '' : 'none';
  if (terms.length) CARDS.forEach(c => {{ if (c.style.display !== 'none') markAll(c.querySelector('.body')); }});
}};

function runSearch() {{
  const q = norm(qbox.value).trim();
  terms = q ? q.split(/\\s+/) : [];
  window.__applyCardFilters();
}}
qbox.addEventListener('input', runSearch);
qbox.addEventListener('keydown', ev => {{
  if (ev.key === 'Escape') {{ qbox.value = ''; runSearch(); }}
}});
qclear.addEventListener('click', () => {{ qbox.value = ''; qbox.focus(); runSearch(); }});
document.addEventListener('keydown', ev => {{
  if (ev.key === '/' && !ev.metaKey && !ev.ctrlKey &&
      !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {{
    ev.preventDefault(); qbox.focus(); qbox.select();
  }}
}});
qclear.style.display = 'none';'''
assert old_js in s
s = s.replace(old_js, new_js, 1)

open('build_html.py', 'w', encoding='utf-8').write(s)
print('search feature wired into build_html.py')
