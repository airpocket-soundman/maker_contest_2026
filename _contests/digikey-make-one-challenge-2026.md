---
title: DigiKey Make ONE Challenge 2026
short_title: DigiKey Make ONE 2026
tagline: 自分イチのモノづくりに挑戦 - DigiKey日本初開催の電子工作コンテスト
organizer: DigiKey
official_url: https://www.digikey.jp/ja/resources/events/2026/make-one-challenge
target_audience: エンジニア、学生、メイカー(初心者から経験者まで)
submission_format: ProtoPedia上に作品ページを公開登録(2分以内のデモ動画 + myLists部品表URLの掲載が必須)

entry_period:
  start: 2026-04-06
  end: 2026-06-22
  note: 受付時刻は 4/6 13:00 〜 6/22 23:59

schedule:
  - date: 2026-04-06
    event: 応募受付開始(13:00)
  - date: 2026-06-22
    event: 応募受付締切(23:59)
  - date: 2026-07-11
    event: 決勝審査会(一次審査通過の上位10作品が対象)
  - date: 2026-09-05〜09-06
    event: Maker Faire Tokyo 2026にて展示・授賞式

judges:
  - name: イチケン
    affiliation: 電子工作系YouTuber
    role: 特別審査委員

criteria:
  - 作品の完成度
  - モノづくりに挑戦するプロセスそのもの("ONE = イチ" のキーワードに沿った挑戦の価値)
  - NXP製品(おすすめ製品)を使用している場合、一次審査で加点

regulations:
  - 作品はProtoPediaに公開登録すること
  - キャンペーン開始以降に制作された新作であること
  - 2分以内のデモ動画を作品ページに掲載すること
  - myListsで作成した部品表のURLを作品ページに掲載すること
  - DigiKey製品を最低1点使用していること
  - 優秀作品はMaker Faire Tokyo 2026で展示、受賞者インタビュー動画が公式YouTubeで配信予定

prizes:
  - name: 最優秀賞
    count: 1 作品
    description: DigiKey部品購入権、Maker Faire Tokyo 2026 展示権、授賞式招待権、DigiKey ノベルティ。特別審査員のイチケン氏によるインタビューを受け、DigiKey 日本公式 YouTube チャンネルで作品紹介予定。
  - name: 優秀賞
    count: 3 作品
    description: Maker Faire Tokyo 2026 展示権、授賞式招待権、DigiKey ノベルティ。イチケン氏によるインタビューを受け、DigiKey 日本公式 YouTube チャンネルで作品紹介予定。
  - name: 学生賞
    count: 1 作品
    description: 授賞式招待権、DigiKey ノベルティ。学生の応募作品から選出。
  - name: イチケン賞
    count: 1 作品
    description: 授賞式招待権、DigiKey ノベルティ。特別審査員のイチケン氏が選出する特別賞。
  - name: 応募者特典
    description: コンテスト応募者向けの限定 DigiKey ノベルティ。さらに ProtoPedia 「DigiKey メイカー支援キャンペーン」連動で抽選 70 名に DigiKey 部品購入費 6,000 円のキャッシュバックあり(うち 20 名は学生優先枠)。
  - name: 来場者特典
    description: Maker Faire Tokyo 2026 来場者全員に DigiKey ノベルティをプレゼント。

cosponsors:
  - NXP Semiconductors(スポンサー)
  - ProtoPedia / 一般社団法人MA(運営協力)

hardware:
  - name: DigiKey取扱製品全般
    required: true
    note: 応募作品にはDigiKey製品を最低1点以上使用する必要があります。
  - name: NXP 推奨評価ボード 4 種比較(FRDM-MCXC444 / FRDM-MCXN947 / FRDM-IMX91 / IMXRT1050-EVKB)
    slug: nxp-frdm-eval-boards
    recommended: true
    note: 一次審査で加点対象となる「おすすめ製品」。性能比較表・価格・開発環境は詳細ページ参照。
  - name: NXP MCUXpresso 開発フレームワーク(4 ボード共通)
    slug: nxp-mcuxpresso-framework
    recommended: true
    note: VS Code 拡張・MCUXpresso SDK・eIQ Toolkit・Yocto Linux BSP・互換ツールチェーンを横断的に解説。
  - name: FRDM-MCXC444 詳細(GPIO・電源・センサ)
    slug: frdm-mcxc444
    recommended: true
    note: 入門向け Cortex-M0+ 48MHz ボード(¥1,750)。GPIO・電源・搭載センサの詳細。
  - name: FRDM-MCXN947 詳細(eIQ Neutron NPU・ONNX 変換フロー)
    slug: frdm-mcxn947
    recommended: true
    note: デュアル M33 + NPU(¥4,354)。eIQ Toolkit による ONNX→TFLite→Neutron 変換手順を解説。
  - name: FRDM-IMX91 詳細(Linux/Yocto・Wi-Fi6/BLE/802.15.4)
    slug: frdm-imx91
    recommended: true
    note: Cortex-A55 1.4GHz の Linux ボード(¥13,062)。Yocto BSP 取得・UUU 書込み手順も解説。
  - name: IMXRT1050-EVKB 詳細(Cortex-M7 600MHz・XIP 実行・GUI Guider)
    slug: imxrt1050-evkb
    recommended: true
    note: クロスオーバー MCU 高性能ボード(¥18,572)。HyperFlash XIP・LCD/カメラ/オーディオ対応。
  - name: その他おすすめ部品・ボード(STM32 / Arduino / Raspberry Pi / Seeed / M5Stack / DFRobot)
    slug: digikey-recommended-parts
    recommended: true
    note: NXP 4 ボード以外の推奨製品 10 件(BLE/Wi-Fi 開発ボード、AI カメラ、環境センサ、モータドライバ等)。
---

## 連動キャンペーン

ProtoPediaが主催する「DigiKey メイカー支援キャンペーン」と連動しており、当選者にはDigiKey部品購入費 6,000円のキャッシュバックが受けられます。

- キャンペーン第一弾応募: 2026年3月2日 〜 4月13日
- キャンペーン第二弾応募: 2026年4月15日 〜 4月27日
- 部品購入対象期間: 2026年3月2日 〜 5月31日

## 補足情報

- 公式情報源: [DigiKey公式](https://www.digikey.jp/ja/resources/events/2026/make-one-challenge)、[ProtoPedia イベントページ](https://protopedia.net/event/digikey2026)、[PR TIMES プレスリリース](https://prtimes.jp/main/html/rd/p/000000155.000051273.html)、[一般社団法人MAブログ](https://we-are-ma.jp/blog/digikey-cam/)
- DigiKeyとして日本初開催の電子工作コンテスト。
- "ONE(イチ)" をキーワードに、初めての電子工作にチャレンジする方も、自分なりの一作を仕上げたい経験者も対象。

> ⚠️ 本ページの内容は公開情報をもとにまとめた参考情報です。応募前に必ず[公式サイト](https://www.digikey.jp/ja/resources/events/2026/make-one-challenge)で最新情報をご確認ください。
