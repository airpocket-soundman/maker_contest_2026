"""m5stack_contest_2026_entries.html をパスワードで AES-GCM 暗号化し、
ブラウザ上で復号する自己完結の index.html を生成する(staticrypt方式)。
使い方: python encrypt_page.py <password> <input.html> <output.html>
"""
import sys, os, base64, hashlib, json
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

password, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
data = open(src, 'rb').read()
salt = os.urandom(16)
iv = os.urandom(12)
key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 250_000, dklen=32)
ct = AESGCM(key).encrypt(iv, data, None)
payload = base64.b64encode(salt + iv + ct).decode()

wrapper = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>M5Stack Global Innovation Contest 2026</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'%3E%3Crect%20width='64'%20height='64'%20rx='13'%20fill='%23111318'/%3E%3Crect%20x='7.5'%20y='7.5'%20width='49'%20height='34'%20rx='4.5'%20fill='%231e2128'/%3E%3Crect%20x='10'%20y='10'%20width='44'%20height='29'%20rx='3'%20fill='%23ff6a00'/%3E%3Cpath%20d='M20%2033V17l6%209%206-9v16'%20fill='none'%20stroke='%23111318'%20stroke-width='3.4'%20stroke-linejoin='round'%20stroke-linecap='round'/%3E%3Cpath%20d='M44%2017h-7v7h4a3.5%203.5%200%201%201-3.6%204.6'%20fill='none'%20stroke='%23111318'%20stroke-width='3.4'%20stroke-linejoin='round'%20stroke-linecap='round'/%3E%3Ccircle%20cx='18'%20cy='52.5'%20r='4.3'%20fill='%23c9ccd2'/%3E%3Ccircle%20cx='32'%20cy='52.5'%20r='4.3'%20fill='%23c9ccd2'/%3E%3Ccircle%20cx='46'%20cy='52.5'%20r='4.3'%20fill='%23c9ccd2'/%3E%3C/svg%3E">
<link rel="apple-touch-icon" href="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'%3E%3Crect%20width='64'%20height='64'%20rx='13'%20fill='%23111318'/%3E%3Crect%20x='7.5'%20y='7.5'%20width='49'%20height='34'%20rx='4.5'%20fill='%231e2128'/%3E%3Crect%20x='10'%20y='10'%20width='44'%20height='29'%20rx='3'%20fill='%23ff6a00'/%3E%3Cpath%20d='M20%2033V17l6%209%206-9v16'%20fill='none'%20stroke='%23111318'%20stroke-width='3.4'%20stroke-linejoin='round'%20stroke-linecap='round'/%3E%3Cpath%20d='M44%2017h-7v7h4a3.5%203.5%200%201%201-3.6%204.6'%20fill='none'%20stroke='%23111318'%20stroke-width='3.4'%20stroke-linejoin='round'%20stroke-linecap='round'/%3E%3Ccircle%20cx='18'%20cy='52.5'%20r='4.3'%20fill='%23c9ccd2'/%3E%3Ccircle%20cx='32'%20cy='52.5'%20r='4.3'%20fill='%23c9ccd2'/%3E%3Ccircle%20cx='46'%20cy='52.5'%20r='4.3'%20fill='%23c9ccd2'/%3E%3C/svg%3E">
<style>
body { margin:0; font-family:system-ui,-apple-system,"Segoe UI","Hiragino Kaku Gothic ProN","Yu Gothic UI",sans-serif;
  background:#f9f9f7; color:#1c2733; display:flex; min-height:100vh; align-items:center; justify-content:center; }
@media (prefers-color-scheme: dark) { body { background:#0d0d0d; color:#e8ecf0; } .box { background:#1e242b !important; border-color:rgba(255,255,255,.1) !important; } input { background:#14181d !important; color:#e8ecf0 !important; border-color:rgba(255,255,255,.2) !important; } }
.box { background:#fff; border:1px solid rgba(11,11,11,.1); border-radius:14px; padding:34px 38px; max-width:380px; text-align:center; }
h1 { font-size:1.05rem; margin:0 0 6px; }
p { font-size:.82rem; color:#888; margin:4px 0 18px; }
input { font:inherit; width:100%; box-sizing:border-box; padding:9px 12px; border:1px solid #ccc; border-radius:8px; }
button { font:inherit; margin-top:12px; width:100%; padding:9px 0; border:none; border-radius:8px;
  background:#2a78d6; color:#fff; cursor:pointer; }
#err { color:#d03b3b; font-size:.8rem; min-height:1.2em; margin-top:10px; }
</style>
</head>
<body>
<form class="box" id="f">
  <h1>M5Stack Global Innovation Contest 2026<br>エントリー作品サマリ</h1>
  <p>このページは閲覧用パスワードで保護されています</p>
  <input type="password" id="pw" placeholder="パスワード" autofocus autocomplete="current-password">
  <button type="submit">表示する</button>
  <div id="err"></div>
</form>
<script>
const PAYLOAD = "__PAYLOAD__";
async function decrypt(pw) {
  const raw = Uint8Array.from(atob(PAYLOAD), c => c.charCodeAt(0));
  const salt = raw.slice(0, 16), iv = raw.slice(16, 28), ct = raw.slice(28);
  const km = await crypto.subtle.importKey("raw", new TextEncoder().encode(pw), "PBKDF2", false, ["deriveKey"]);
  const key = await crypto.subtle.deriveKey(
    {name: "PBKDF2", salt, iterations: 250000, hash: "SHA-256"},
    km, {name: "AES-GCM", length: 256}, false, ["decrypt"]);
  const pt = await crypto.subtle.decrypt({name: "AES-GCM", iv}, key, ct);
  return new TextDecoder().decode(pt);
}
document.getElementById("f").addEventListener("submit", async ev => {
  ev.preventDefault();
  const pw = document.getElementById("pw").value;
  document.getElementById("err").textContent = "";
  try {
    const html = await decrypt(pw);
    sessionStorage.setItem("gic_ok", "1");
    document.open(); document.write(html); document.close();
  } catch (e) {
    document.getElementById("err").textContent = "パスワードが違います";
  }
});
</script>
</body>
</html>'''

open(dst, 'w', encoding='utf-8').write(wrapper.replace('__PAYLOAD__', payload))
print('encrypted:', src, '->', dst, f'({len(payload)//1024} KB payload)')
