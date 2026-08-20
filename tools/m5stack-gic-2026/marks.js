/* ============================================================
   チェックボックス + メモ を GitHub Gist に永続化する
   - トークンとGist IDはこのブラウザの localStorage にのみ保存
   - 保存前に必ず最新を取得してマージするので、3人が同時に触っても
     お互いの入力を消さない(同じ人の同じ項目だけ後勝ち)
   ============================================================ */
(function () {
  var PEOPLE = [['higedaruma', 'ひげだるま'], ['banno', 'ばんの'], ['airpocket', 'airpocket']];
  var FILE = 'gic2026-marks.json';
  var LS_TOKEN = 'gic26_gh_token', LS_GIST = 'gic26_gist_id', LS_CACHE = 'gic26_marks_cache';
  var state = {};          // { key: { person: {c:bool, m:string} } }
  var dirty = false, saving = false, timer = null;

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var token = function () { return localStorage.getItem(LS_TOKEN) || ''; };
  var gistId = function () { return localStorage.getItem(LS_GIST) || ''; };

  function setStatus(cls, msg) {
    var d = $('#syncdot'), m = $('#syncmsg');
    if (d) d.className = 'dot ' + cls;
    if (m) m.textContent = msg;
  }

  function cell(key, pid) {
    if (!state[key]) state[key] = {};
    if (!state[key][pid]) state[key][pid] = { c: false, m: '' };
    return state[key][pid];
  }

  /* ---------- 画面へ反映 ---------- */
  function render() {
    $$('#grid .card').forEach(function (card) {
      var key = card.dataset.k;
      PEOPLE.forEach(function (p) {
        var v = (state[key] || {})[p[0]] || { c: false, m: '' };
        var cb = $('input[data-p="' + p[0] + '"]', card);
        var ta = $('textarea[data-p="' + p[0] + '"]', card);
        if (cb) { cb.checked = !!v.c; cb.parentNode.classList.toggle('on', !!v.c); }
        if (ta) { ta.value = v.m || ''; ta.classList.toggle('filled', !!(v.m || '').trim()); }
      });
      var anyMemo = PEOPLE.some(function (p) {
        return (((state[key] || {})[p[0]] || {}).m || '').trim();
      });
      var box = $('.memos', card);
      if (box && anyMemo) box.classList.add('open');
    });
    updateCounts();
    applyFilter();
  }

  function updateCounts() {
    PEOPLE.forEach(function (p) {
      var n = Object.keys(state).filter(function (k) {
        return state[k][p[0]] && state[k][p[0]].c;
      }).length;
      var b = $('#f_' + p[0]);
      if (b) b.textContent = p[1] + ' ✓' + n;
    });
  }

  /* ---------- 保存 ---------- */
  function cacheLocal() {
    try { localStorage.setItem(LS_CACHE, JSON.stringify(state)); } catch (e) {}
  }

  function scheduleSave() {
    dirty = true;
    cacheLocal();
    setStatus('busy', '未保存の変更があります…');
    clearTimeout(timer);
    timer = setTimeout(save, 1200);
  }

  function api(path, opt) {
    opt = opt || {};
    opt.headers = Object.assign({
      'Accept': 'application/vnd.github+json',
      'Authorization': 'Bearer ' + token()
    }, opt.headers || {});
    return fetch('https://api.github.com' + path, opt).then(function (r) {
      if (!r.ok) return r.text().then(function (t) { throw new Error(r.status + ' ' + t.slice(0, 120)); });
      return r.json();
    });
  }

  function mergeRemote(remote) {
    // 相手の値を土台に、自分がこのセッションで触った項目だけ上書きする
    var out = JSON.parse(JSON.stringify(remote || {}));
    Object.keys(state).forEach(function (k) {
      out[k] = out[k] || {};
      Object.keys(state[k]).forEach(function (p) {
        var mine = state[k][p];
        if (mine.touched) out[k][p] = { c: !!mine.c, m: mine.m || '' };
        else if (!out[k][p]) out[k][p] = { c: !!mine.c, m: mine.m || '' };
      });
    });
    return out;
  }

  function stripTouched(o) {
    var r = {};
    Object.keys(o).forEach(function (k) {
      var inner = {};
      Object.keys(o[k]).forEach(function (p) {
        var v = o[k][p];
        if (v && (v.c || (v.m || '').trim())) inner[p] = { c: !!v.c, m: v.m || '' };
      });
      if (Object.keys(inner).length) r[k] = inner;
    });
    return r;
  }

  function save() {
    if (!token() || !gistId()) { setStatus('ng', 'この端末に保存(Gist未設定)'); return; }
    if (saving) { clearTimeout(timer); timer = setTimeout(save, 800); return; }
    saving = true;
    setStatus('busy', '保存中…');
    api('/gists/' + gistId()).then(function (g) {
      var remote = {};
      try { remote = JSON.parse(g.files[FILE].content).items || {}; } catch (e) {}
      var merged = mergeRemote(remote);
      var body = { items: stripTouched(merged), updatedAt: new Date().toISOString() };
      var files = {};
      files[FILE] = { content: JSON.stringify(body, null, 1) };
      return api('/gists/' + gistId(), {
        method: 'PATCH', body: JSON.stringify({ files: files })
      }).then(function () { return merged; });
    }).then(function (merged) {
      Object.keys(merged).forEach(function (k) {
        state[k] = state[k] || {};
        Object.keys(merged[k]).forEach(function (p) {
          var cur = cell(k, p);
          if (!cur.touched) { cur.c = merged[k][p].c; cur.m = merged[k][p].m; }
          cur.touched = false;
        });
      });
      dirty = false; saving = false;
      cacheLocal(); render();
      setStatus('ok', '保存しました ' + new Date().toLocaleTimeString('ja-JP'));
    }).catch(function (e) {
      saving = false;
      setStatus('ng', '保存失敗: ' + e.message);
    });
  }

  /* ---------- 読み込み ---------- */
  function load() {
    try { state = JSON.parse(localStorage.getItem(LS_CACHE) || '{}'); } catch (e) { state = {}; }
    render();
    if (!token() || !gistId()) { setStatus('ng', 'Gist未設定 — この端末にのみ保存されます'); return; }
    setStatus('busy', '読み込み中…');
    api('/gists/' + gistId()).then(function (g) {
      var remote = {};
      try { remote = JSON.parse(g.files[FILE].content).items || {}; } catch (e) {}
      state = remote;
      cacheLocal(); render();
      setStatus('ok', '同期済み ' + new Date().toLocaleTimeString('ja-JP'));
    }).catch(function (e) {
      setStatus('ng', '読み込み失敗: ' + e.message + '(この端末の保存内容を表示中)');
    });
  }

  function createGist() {
    if (!token()) { alert('先にトークンを入力してください'); return; }
    setStatus('busy', 'Gistを作成中…');
    var files = {};
    files[FILE] = { content: JSON.stringify({ items: stripTouched(state), updatedAt: new Date().toISOString() }, null, 1) };
    api('/gists', {
      method: 'POST',
      body: JSON.stringify({ description: 'M5Stack GIC2026 marks', public: false, files: files })
    }).then(function (g) {
      localStorage.setItem(LS_GIST, g.id);
      $('#gistid').value = g.id;
      setStatus('ok', 'Gistを作成しました: ' + g.id + ' — このIDを他の2人にも共有してください');
    }).catch(function (e) { setStatus('ng', '作成失敗: ' + e.message); });
  }

  /* ---------- 絞り込み ---------- */
  var filters = {};
  function applyFilter() {
    var on = Object.keys(filters).filter(function (k) { return filters[k]; });
    $$('#grid .card').forEach(function (card) {
      var k = card.dataset.k;
      var ok = on.every(function (p) { return ((state[k] || {})[p] || {}).c; });
      card.dataset.mfilter = ok ? '' : 'hide';
      if (typeof window.__applyCardFilters === 'function') return;
      card.style.display = ok ? '' : 'none';
    });
    if (typeof window.__applyCardFilters === 'function') window.__applyCardFilters();
  }

  /* ---------- 起動 ---------- */
  function b64e(o) {
    return btoa(unescape(encodeURIComponent(JSON.stringify(o))))
      .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  }
  function b64d(t) {
    t = t.replace(/-/g, '+').replace(/_/g, '/');
    return JSON.parse(decodeURIComponent(escape(atob(t))));
  }
  function consumeSetupLink() {
    var m = (location.hash || '').match(/gicsetup=([A-Za-z0-9_\-]+)/);
    if (!m) return false;
    try {
      var cfg = b64d(m[1]);
      if (cfg.t) localStorage.setItem(LS_TOKEN, cfg.t);
      if (cfg.g) localStorage.setItem(LS_GIST, cfg.g);
      history.replaceState(null, '', location.pathname + location.search);
      return true;
    } catch (e) { return false; }
  }
  function shareLink() {
    if (!token() || !gistId()) { alert('先にトークンとGist IDを設定してください'); return; }
    var url = location.origin + location.pathname + '#gicsetup=' + b64e({ t: token(), g: gistId() });
    navigator.clipboard.writeText(url).then(function () {
      setStatus('ok', '招待リンクをコピーしました — 他の2人に送ってください(開くだけで設定完了)');
    }, function () { prompt('このリンクをコピーして他の2人に送ってください', url); });
  }

  function init() {
    $$('#grid .card input[type=checkbox][data-p]').forEach(function (cb) {
      cb.addEventListener('change', function () {
        var k = cb.closest('.card').dataset.k;
        var c = cell(k, cb.dataset.p);
        c.c = cb.checked; c.touched = true;
        cb.parentNode.classList.toggle('on', cb.checked);
        updateCounts(); applyFilter(); scheduleSave();
      });
    });
    $$('#grid .card textarea[data-p]').forEach(function (ta) {
      ta.addEventListener('input', function () {
        var k = ta.closest('.card').dataset.k;
        var c = cell(k, ta.dataset.p);
        c.m = ta.value; c.touched = true;
        ta.classList.toggle('filled', !!ta.value.trim());
        scheduleSave();
      });
    });
    $$('.memotog').forEach(function (b) {
      b.addEventListener('click', function () {
        var box = $('.memos', b.closest('.card'));
        box.classList.toggle('open');
        b.textContent = box.classList.contains('open') ? 'メモを隠す' : 'メモを書く';
      });
    });
    PEOPLE.forEach(function (p) {
      var b = $('#f_' + p[0]);
      if (!b) return;
      b.addEventListener('click', function () {
        filters[p[0]] = !filters[p[0]];
        b.classList.toggle('on', filters[p[0]]);
        applyFilter();
      });
    });
    var viaLink = consumeSetupLink();
    $('#tok').value = token();
    $('#gistid').value = gistId();
    if (viaLink) setStatus('busy', '招待リンクの設定を取り込みました');
    $('#savecfg').addEventListener('click', function () {
      localStorage.setItem(LS_TOKEN, $('#tok').value.trim());
      localStorage.setItem(LS_GIST, $('#gistid').value.trim());
      load();
    });
    $('#mkgist').addEventListener('click', createGist);
    $('#sharelink').addEventListener('click', shareLink);
    $('#cfgtog').addEventListener('click', function () { $('#synccfg').classList.toggle('open'); });
    $('#resync').addEventListener('click', load);
    window.addEventListener('beforeunload', function (e) {
      if (dirty) { e.preventDefault(); e.returnValue = ''; }
    });
    load();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
