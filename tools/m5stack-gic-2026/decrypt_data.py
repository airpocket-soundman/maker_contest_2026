"""data/m5stack-gic-2026-data.enc を復号する。
使い方: python decrypt_data.py <password> <input.enc> <output.tar.gz>
"""
import sys, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

password, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
raw = open(src, 'rb').read()
salt, iv, ct = raw[:16], raw[16:28], raw[28:]
key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 250_000, dklen=32)
open(dst, 'wb').write(AESGCM(key).decrypt(iv, ct, None))
print('decrypted ->', dst)
