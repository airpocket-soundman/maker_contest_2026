import re, json, html as H
from collections import Counter, defaultdict

merged = json.load(open('merged2.json', encoding='utf-8'))
merged = [e for e in merged if not e.get('withdrawn')]
meta = json.load(open('meta.json', encoding='utf-8'))
parts = json.load(open('parts.json', encoding='utf-8'))

# ---------- 1. canonical M5Stack core devices (ordered: first match wins) ----------
CORE = [
    ('Cardputer ADV', r'cardputer[\s\-]*adv'),
    ('Cardputer', r'cardputer'),
    ('Tab5', r'\btab5\b'),
    ('Core2 for AWS', r'core2\s*for\s*aws'),
    ('Core2', r'\bcore2\b'),
    ('CoreS3 / CoreS3 SE', r'cores3'),
    ('Core (Basic/Gray/Fire)', r'\b(basic core|core\s*(basic|gray|grey|fire)|esp32 basic core)\b'),
    ('CoreInk', r'coreink|core\s*ink'),
    ('PaperS3 / M5Paper', r'papers3|m5\s*paper|paper\s*s3'),
    ('PaperColor', r'papercolor'),
    ('StickC PLUS / PLUS2', r'stickc\s*plus|m5stickc'),
    ('StickS3', r'sticks3'),
    ('AtomS3R', r'atoms3r|atom\s*s3r'),
    ('AtomS3 / AtomS3 Lite / AtomS3U', r'atoms3'),
    ('Atom Lite / Matrix / Echo', r'atom\s*(lite|matrix|echo)'),
    ('Atom VoiceS3R', r'voices3r|atom\s*voice'),
    ('StampFly', r'stampfly|stamp\s*fly'),
    ('StampS3 / M5Stamp', r'stamps3|m5\s*stamp|stamp\s*pico|stampplc|stamplc'),
    ('Dial', r'\bdial\b'),
    ('DinMeter', r'dinmeter|din\s*meter'),
    ('StopWatch', r'stop\s*watch'),
    ('Capsule', r'capsule'),
    ('NanoC6 / Unit C6L', r'nanoc6|nano\s*c6|c6l'),
    ('VAMeter', r'vameter|va\s*meter'),
    ('UnitV2 / UnitV', r'unitv'),
    ('BugC2 / RoverC', r'bugc|roverc'),
    ('MorseCode Matrix', r'morse\s*code'),
]

# ---------- 2. units / modules / other hardware buckets ----------
UNIT = [
    ('StackChan (ロボットキット)', r'stack\s*chan|stackchan'),
    ('Grove / 各種ケーブル', r'grove|hy2\.0|cable'),
    ('サーボモーター', r'servo|sg9[02]|sts3\d|feetech|mg996|robstride'),
    ('LED (NeoPixel/WS2812/SK6812)', r'neopixel|ws281|sk6812|led strip|led ring|rgb led|hex\b'),
    ('3Dプリント部品 / 筐体', r'3d[\s\-]*print|enclosure|筐体|case\b|bracket|mount\b'),
    ('バッテリー / 電源', r'batter|lipo|18650|power (base|module|bank)|tailbat|solar'),
    ('ToF / 距離センサ', r'\btof\b|vl53|ultrasonic|sr04|lidar|rplidar'),
    ('IMU / 姿勢センサ', r'\bimu\b|bmi270|mpu-?6050|bmm|gyro|accelerom'),
    ('環境センサ (温湿度/気圧/CO2)', r'\benv\b|bmp\d|bme\d|sht\d|dht\d|scd4|co2|温湿度'),
    ('GPS / GNSS', r'\bgps\b|gnss|bds|at6558|atgm336'),
    ('LoRa / サブGHz', r'lora|sx126|1262|sub-?ghz|meshtastic'),
    ('NFC / RFID', r'\bnfc\b|rfid|ntag|pn532|mfrc'),
    ('オーディオ (DAC/AMP/スピーカー/マイク)', r'audio module|es8388|es8311|pcm5102|speaker|microphone|\bmic\b|i2s|synth unit|unit synth|midi'),
    ('ディスプレイ増設', r'\blcd\b|oled|display|gc9a01|st77\d|glass2|e-?ink|e-?paper'),
    ('ロードセル / 重量', r'load cell|weight|scale|hx711|lp47'),
    ('モータードライバ / DCモーター', r'motor (base|driver|module)|tmc2|drv8|dc motor|stepper|hbridge|h-bridge'),
    ('カメラ', r'camera|cam\b|ov2640|timer\s*cam'),
    ('ジョイスティック / 入力デバイス', r'joystick|joyc|encoder|button|key\s*unit|dual\s*key|angle unit|8angle'),
    ('リレー / 電力計測', r'relay|ina2\d\d|pzem|current sensor'),
    ('LLMモジュール / AI', r'llm module|ax630|module llm|unit asr|asr\b|v-?training'),
]

# ---------- 3. technology keywords, counted per project over the story text ----------
TECH = [
    ('Wi-Fi', r'\bwi-?fi\b|wlan'),
    ('BLE / Bluetooth', r'\bble\b|bluetooth'),
    ('BLE HID (キーボード/マウス)', r'ble\s*hid|hid\s*keyboard|bluetooth keyboard|ble keyboard|hid\s*mouse'),
    ('ESP-NOW', r'esp-?now'),
    ('LoRa / Meshtastic', r'\blora\b|meshtastic|meshcore'),
    ('MQTT', r'\bmqtt\b'),
    ('HTTP / REST API 連携', r'(rest|web|json|http)\s*api|api\s*(call|endpoint|request|key)|api\s*(を|で|から)'),
    ('WebSocket', r'websocket'),
    ('UDP / TCP ソケット', r'\budp\b|\btcp\b'),
    ('Webサーバ / WebUI 内蔵', r'web ?ui|web server|webserver|captive portal|softap|access point'),
    ('LVGL', r'\blvgl\b'),
    ('M5Unified / M5GFX', r'm5unified|m5gfx|lovyangfx'),
    ('生成AI / LLM 連携', r'\bllm\b|\bgpt\b|openai|claude|gemini|deepseek|xiaozhi|生成ai|chatgpt'),
    ('MCP (Model Context Protocol)', r'\bmcp\b|model context protocol'),
    ('音声認識 / TTS', r'speech|voice recognition|\bstt\b|\btts\b|whisper|asr\b|音声認識'),
    ('画像認識 / CV', r'opencv|image recognition|computer vision|object detect|yolo|画像認識'),
    ('3Dプリント', r'3d[\s\-]*print|stl file|fdm|bambu|prusa'),
    ('自作PCB / KiCad', r'kicad|custom pcb|自作基板|pcb design|easyeda'),
    ('電子ペーパー', r'e-?ink|e-?paper|epaper|電子ペーパー'),
    ('ディープスリープ / 省電力', r'deep ?sleep|light ?sleep|low power|省電力|battery life'),
    ('Home Assistant / ESPHome', r'home assistant|esphome'),
    ('MicroPython / UIFlow', r'micropython|uiflow'),
    ('Arduino / PlatformIO', r'arduino|platformio'),
    ('ESP-IDF', r'esp-?idf'),
    ('FreeRTOS / マルチタスク', r'freertos|xtaskcreate|dual core|マルチタスク'),
    ('SDカード活用', r'\bsd ?card\b|microsd|littlefs|spiffs'),
    ('OTA アップデート', r'\bota\b'),
    ('暗号 / セキュリティ', r'aes-?256|encrypt|totp|atecc|secure element|pbkdf2|署名|signing'),
    ('アマチュア無線', r'\bham\b|aprs|\bft8\b|amateur radio|qmx|アマチュア無線'),
    ('ゲーム / エミュレータ', r'\bgame\b|emulator|\bdoom\b|game ?boy|ゲーム'),
    ('ロボット / 自律走行', r'\brobot|autonomous|\bslam\b|quadruped|rover\b'),
]


def norm(t):
    return re.sub(r'\s+', ' ', t.lower())


def bucket(name, table):
    n = norm(name)
    for label, rx in table:
        if re.search(rx, n):
            return label
    return None


core_by_proj, unit_by_proj, sw_by_proj, tech_by_proj = {}, {}, {}, {}
raw_hw_unmatched = Counter()

for e in merged:
    key = e['url'].replace('https://www.hackster.io', '')
    p = parts.get(key, {'hw': [], 'sw': [], 'tool': []})
    hw_names = [re.split(r'<td', x['name'])[0].strip() for x in p['hw']]
    sw_names = [re.split(r'<td', x['name'])[0].strip() for x in p['sw']]

    cores, units = set(), set()
    for nm in hw_names:
        c = bucket(nm, CORE)
        if c:
            cores.add(c)
        else:
            u = bucket(nm, UNIT)
            if u:
                units.add(u)
            elif nm:
                raw_hw_unmatched[nm] += 1
    # units can also appear alongside a core name; scan again for unit buckets
    for nm in hw_names:
        u = bucket(nm, UNIT)
        if u and not bucket(nm, CORE):
            units.add(u)

    core_by_proj[key] = sorted(cores)
    unit_by_proj[key] = sorted(units)
    sw_by_proj[key] = sorted({re.split(r'\s*[(.]', n)[0].strip()[:48] for n in sw_names if n})

    # tech keywords from the story
    s = open(meta[key]['file'], encoding='utf-8', errors='ignore').read()
    i = s.find('<section id="story"')
    t = s[i:i + 200000] if i != -1 else s
    t = re.sub(r'<[^>]+>', ' ', t)
    t = norm(H.unescape(t))
    tech_by_proj[key] = sorted({lab for lab, rx in TECH if re.search(rx, t)})

agg = dict(
    core=Counter(c for v in core_by_proj.values() for c in v).most_common(),
    unit=Counter(u for v in unit_by_proj.values() for u in v).most_common(),
    sw=Counter(s for v in sw_by_proj.values() for s in v).most_common(),
    tech=Counter(t for v in tech_by_proj.values() for t in v).most_common(),
    per_project=dict(core=core_by_proj, unit=unit_by_proj, sw=sw_by_proj, tech=tech_by_proj),
    n_with_parts=sum(1 for v in parts.values() if v['hw']),
    total=len(merged),
)
json.dump(agg, open('tech_agg.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

for title, key in [('M5Stackコアデバイス', 'core'), ('部品カテゴリ', 'unit'),
                   ('開発環境・サービス', 'sw'), ('技術キーワード', 'tech')]:
    print(f'--- {title} ---')
    for k, v in agg[key][:26]:
        print(f'  {v:3d}  {k}')
    print()
print('--- 未分類のハードウェア名(上位) ---')
for k, v in raw_hw_unmatched.most_common(15):
    print(f'  {v:3d}  {k}')
