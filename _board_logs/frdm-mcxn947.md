---
title: FRDM-MCXN947 開発ログ
short_title: FRDM-MCXN947
order: 10
board: FRDM-MCXN947
category: 高性能・AI対応
tagline: FRDM-MCXN947 を使った開発作業の記録
---

## ボード概要

FRDM-MCXN947 は、NXP の MCX N シリーズ(MCX N947)を搭載した FRDM(Freedom)プラットフォームの評価ボード。
デュアル Cortex-M33 + eIQ Neutron NPU の構成により、汎用組み込み用途から AI 推論までを 1 枚でカバーできる位置付け。

### 搭載 MCU(MCX N947)主要スペック

| 項目 | 内容 |
| --- | --- |
| CPU | Arm Cortex-M33F(CPU0)+ Cortex-M33(CPU1)、最大 150 MHz |
| AI アクセラレータ | eIQ Neutron NPU(8-bit、最大 4.8 GOPS) |
| Flash | 2 MB(デュアルバンク、16 KB キャッシュ) |
| SRAM | 最大 512 KB(うち 416 KB は ECC 付き) |
| セキュリティ | EdgeLock Secure Subsystem(暗号化アクセラレータ / TRNG) |

### 主要周辺機能

- 通信: 10x LP Flexcomm(SPI / I2C / UART)、2x FlexCAN-FD、2x I3C、2x SAI
- USB: High-Speed(EHCI モード、Host / Device)
- Ethernet: QoS 対応
- アナログ: LPADC、LPDAC、HPDAC
- DMA: SmartDMA、EDMA
- 外部ストレージ I/F: FlexSPI(Quad SPI フラッシュ対応)
- タイマ / その他: IRTC、複数 PWM モジュール、TSI V6(タッチセンス入力)

### ボード上のコネクタ・I/F

| コネクタ / 部品 | 用途 |
| --- | --- |
| Arduino UNO R3 互換ヘッダ | Arduino シールド接続 |
| mikroBUS ヘッダ ×2 | mikroe Click Boards 接続 |
| FlexIO / LCD ヘッダ | NXP LCD 8080 パラレルインターフェース |
| SmartDMA / Camera ヘッダ | ArduCam 20 ピン DVP カメラモジュール |
| USB Type-C(MCU-Link 側) | オンボードデバッガ接続 + ボード給電 |
| USB Type-C(ユーザー側) | MCU 直結の High-Speed USB(Host / Device) |
| オンボード TSI タッチパッド | 静電容量タッチ入力 |
| ユーザー LED / プッシュスイッチ | GPIO 経由の入出力 |
| オンボード MCU-Link デバッガ | CMSIS-DAP / SWD によるデバッグ・書き込み |

> 仕様の根拠は末尾の[Zephyr 対応ボードドキュメント](#参考リンク)および MCX N シリーズ Fact Sheet に基づく。
> 加速度センサや個別のシルク番号(J/SW 番号)など、現物または公式回路図で確認を要する項目は別途追記する。

## 開発環境セットアップ

FRDM-MCXN947 で利用できる開発環境は主に **MCUXpresso for VS Code** と **Zephyr / `west`** の 2 系統がある。
ただし **Zephyr は eIQ Neutron NPU に現状対応していない** ため、本ボードを選定した最大の動機(NPU 推論)を活かせない。
本ログでは Zephyr のセットアップは割愛し、Windows 11 + **MCUXpresso for VS Code** に絞って記録する。

### 共通: ハードウェア準備

- USB Type-C ケーブル(データ通信対応のもの) ×1 — まずは **MCU-Link 側** の Type-C ポートに接続する。
- 初回接続時、Windows のデバイスマネージャに `MCU-LINK` 系の COM ポートが見えれば OK。見えない場合は MCU-Link ファームウェア更新を行う(後述)。

### MCUXpresso for VS Code

#### 必要なもの

| 区分 | ツール | 入手元 |
| --- | --- | --- |
| エディタ | Visual Studio Code | Microsoft 公式 |
| 拡張 | MCUXpresso for VS Code(出版者: NXP Semiconductors) | VS Code Marketplace |
| インストーラ | MCUXpresso Installer | NXP 公式([製品ページ](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC)経由 / 拡張からも自動取得可) |
| SDK | MCUXpresso SDK for FRDM-MCXN947 | 拡張内の SDK Manager(Repository or Standalone) |

#### セットアップ手順(Windows 11)

1. **VS Code をインストール**(未導入の場合)。
2. VS Code の Extensions ビューで `MCUXpresso` を検索し、_MCUXpresso for VS Code_ をインストール。
3. アクティビティバーに追加された MCUXpresso アイコンを開き、**QUICKSTART PANEL → Open MCUXpresso Installer**。Installer 未導入なら自動でダウンロードが始まる。
4. Installer を起動し、最低限以下を選択してインストール:
   - **Software Kits**: 開発で使う SDK(後で SDK Manager 経由でも追加可能)
   - **Toolchains**: GNU Arm Embedded Toolchain
   - **Build Tools**: CMake / Ninja
   - **Debug Probes**: LinkServer(MCU-Link/CMSIS-DAP 対応)、MCU-Link host tooling
5. VS Code を再起動 → MCUXpresso 拡張の **SDK Repository** から `FRDM-MCXN947` 用 SDK を取得。
6. 拡張の **Import Example** から `evkmcxn947` 系のサンプル(後述の `hello_world` 等)を取り込み、ビルド → フラッシュ。

> 進めながら詰まった点・解決策はこの後の「Hello World / 動作確認ログ」に時系列で残す。

### MCU-Link ファームウェア更新(必要時)

古い FRDM ボードや、JLink モードに切り替えたい場合は MCU-Link ファームウェアの更新を行う。

- 手順は MCUXpresso Installer 同梱の **MCU-Link host tools** を使う(`MCU-LINK` ボリュームに `firmware.bin` を配置するブートローダ手順)。
- 実際に更新が必要だったかどうか・実施手順の詳細は次節のログに記録する。

## Hello World / 動作確認ログ

最初の動作確認に使うサンプルと、その記録テンプレート。
扱うサンプルはすべて MCUXpresso SDK 経由(理由は[開発環境セットアップ](#開発環境セットアップ)に記載)。
**実機で確認できた値・出力・つまずきは各サンプルの「実行ログ」欄に追記していく。**

### A) MCUXpresso SDK: `hello_world`(UART 出力)

LPUART 経由でシリアル出力する SDK 同梱の定番サンプル。デバッグ I/O 経路の疎通確認用。

#### 手順

1. VS Code → MCUXpresso 拡張 → **IMPORT EXAMPLE FROM REPOSITORY**
2. ボード `frdmmcxn947` を選び、テンプレートに `hello_world` を入力して取り込む(Cortex-M33 CPU0 用)
3. ステータスバーまたは QUICKSTART PANEL から **Build** → **Debug**(または Flash)
4. シリアルターミナル(VS Code 内蔵 Serial Monitor または TeraTerm 等)を **115200 / 8N1** で開く

#### シリアル出力サンプル(期待値)

```
hello world.
```

#### 実行ログ(実機確認後に追記)

- 使用 SDK バージョン:
- 使用 MCU-Link FW バージョン:
- COM ポート番号:
- 実際の出力:
- 所要時間(取り込み〜出力確認まで):

#### つまずき・解決メモ

- _まだなし。発生したらここに「症状 → 原因 → 対処」を追記する。_

#### 完了チェックリスト

- [ ] サンプルが取り込めた
- [ ] ビルドがエラーなく完了した
- [ ] フラッシュ書き込みが成功した
- [ ] シリアルターミナルに `hello world.` が表示された

### B) MCUXpresso SDK: `led_blinky`

GPIO で基板上のユーザー LED を点滅させる、デバッガ・フラッシュ経路の "千本ノック" 用サンプル。

#### 手順

1. MCUXpresso 拡張から `frdmmcxn947` の `led_blinky`(または `gpio_led_output` 系)を取り込む
2. Build → Flash
3. ボード上のオンボード LED が約 1 Hz 程度で点滅することを確認

#### 実行ログ(実機確認後に追記)

- 点滅した LED の色 / シルク番号:
- 点滅周期(目視):
- 備考:

#### つまずき・解決メモ

- _まだなし。_

#### 完了チェックリスト

- [ ] LED が周期的に点滅した
- [ ] リセットスイッチ押下で再スタートする

### C) NPU を使った "Hello World"(最小推論サンプル)

eIQ Neutron NPU の動作確認用最小プロジェクトとして、SDK 同梱の **`tflm_label_image`(`tflm_label_image_cm33_core0`)** を使う。
TensorFlow Lite for Microcontrollers + Neutron NPU で、組み込みモデル(MobileNet 系の量子化モデル)に対する 1 枚画像のラベル推論を行うサンプル。

#### 手順

1. MCUXpresso 拡張 → **IMPORT EXAMPLE** → ボード `frdmmcxn947` → テンプレート `label_image` で検索 → `eiq_examples/tflm_label_image_cm33_core0` を取り込む
2. プロジェクト設定で **NPU(Neutron)バックエンド有効** になっていることを確認(無効の場合は CPU フォールバック実行になる)
3. Build → Flash → シリアル(115200 / 8N1)で出力を確認
4. 推論結果のラベル名と推論時間(ms)をログに残す

#### シリアル出力サンプル(イメージ)

```
Label image example using a TensorFlow Lite Micro model.
Detection ...
Top1: <ラベル名>  (<確度>)
Inference time: <NN> ms
```

> _ラベル文字列・桁・フォーマットは SDK / モデルバージョンにより変動。実機で出た文字列に置き換える。_

#### 実行ログ(実機確認後に追記)

- 使用モデル(同梱 / 自前):
- NPU 有効 / 無効:
- 推論時間 NPU 使用時:
- 推論時間 CPU フォールバック時(比較用):
- 出力ラベル(代表例):

#### つまずき・解決メモ

- _まだなし。NPU 有効化の Kconfig / マクロ名や、Neutron 用 OP サポートで詰まった点を残す想定。_

#### 完了チェックリスト

- [ ] サンプルが取り込めた(NPU 対応版)
- [ ] ビルド・書き込みが成功した
- [ ] シリアルに推論結果と推論時間が出力された
- [ ] NPU vs CPU の推論時間差を把握した

## AI / NPU 実験ログ

「Hello World / 動作確認ログ」C) で `tflm_label_image` を動かした後の **応用実験** をここに集約する。
本ボードを採用した最大の理由が NPU(eIQ Neutron)である以上、コンテスト提出時の説得材料となる定量データを残せる構造にしておく。

### 共通: 推論性能スコア枠(全実験で再利用するフォーマット)

各実験では、以下のスコア表を埋めることを完了条件とする。

| 指標 | 内容 | 値 |
| --- | --- | --- |
| 復現性 | ビルド〜推論実行までを **手順だけ** で他人が再現できるか(○/△/×) |  |
| 性能 | 1 推論あたりの所要時間 [ms] / スループット [inf/s] |  |
| 電流 | 推論時の平均電流 [mA] / アイドル時との差分 [mA] |  |
| メモリ | Flash 使用 [KB] / RAM 使用 [KB] |  |
| 考察 | コンテストで主張する強み / 残課題(2〜3 行) |  |

> 電流計測には MCU-Link 側 USB と MCU 直結 USB のどちらから給電しているかも併記する(電流経路で値が変わるため)。

### 実験 1: 自前モデルを NPU で動かす(モデル差し替え)

`tflm_label_image` のモデルを差し替えて、自分で訓練した量子化モデルを Neutron NPU で実行する。

#### 想定フロー

1. **学習**: TensorFlow / Keras などで対象モデルを訓練 → 量子化(int8)
2. **変換**: eIQ Toolkit の Model Tool / Neutron Converter で `.tflite` を NPU 向けにコンバート
3. **組み込み**: 変換済みモデルを SDK プロジェクト内のモデル配列(C 配列)に置換
4. **ビルド & 実行**: シリアル出力で推論結果と推論時間を確認
5. **NPU フォールバック確認**: ログに "running on NPU" 系のメッセージ / NPU 非対応 OP がないかを確認

#### 必要なもの

- eIQ Toolkit(モデル変換)
- 対象モデル(例: 自作の小型 CNN / KWS モデル)
- ラベル / 入力前処理コードの差し替え

#### 実行ログ(実機確認後に追記)

- 使用モデル概要(タスク / 入力サイズ / パラメータ数):
- 量子化方式(動的 / 完全 int8 / 混合):
- NPU 実行可否:
- NPU 非対応で CPU フォールバックされた OP:
- スコア表(上記フォーマットを複製して記入):

#### つまずき・解決メモ

- _まだなし。NPU 未サポート OP に当たった時の対処を残す想定。_

### 実験 2: 推論性能計測(NPU vs CPU)

同一モデルを Neutron NPU で実行した場合と、CPU(Cortex-M33 + CMSIS-NN)で実行した場合の性能差を定量化する。

#### 想定フロー

1. **基準モデル決定**: `tflm_label_image` 同梱モデルなど、双方で動く量子化モデルを 1 つ選ぶ
2. **NPU 版ビルド**: NPU バックエンドを有効化 → 推論時間 / Flash / RAM を記録
3. **CPU 版ビルド**: NPU を無効化(または CMSIS-NN のみ) → 同じ指標を記録
4. **電流計測**: USB 電流計や INA219 等で平均電流を測る
5. **比較表にまとめる**

#### 比較表(実機確認後に追記)

| 構成 | 推論時間 [ms] | スループット [inf/s] | 平均電流 [mA] | Flash [KB] | RAM [KB] |
| --- | --- | --- | --- | --- | --- |
| NPU 有効 |  |  |  |  |  |
| CPU(CMSIS-NN) |  |  |  |  |  |
| 比率(NPU / CPU) |  |  |  |  |  |

#### 実行ログ(実機確認後に追記)

- 使用モデル / 入力サイズ:
- 計測条件(動作周波数 / 電源経路 / 室温など):
- スコア表:
- 主張ポイント(コンテスト用):

#### つまずき・解決メモ

- _まだなし。NPU 無効化のビルドオプションがバージョンで揺れる想定で、判明次第ここに固定する。_

### 実験 3: センサ入力(音声 / IMU)推論

カメラ系は SmartDMA / DVP 経由で別系統になるため、ここでは **オーディオ(マイク)/ IMU(加速度・ジャイロ)** の時系列センサを入力にした推論実験を扱う。

#### 候補タスク

- **キーワードスポッティング(KWS)**: マイク → MFCC / log-Mel → 小型 CNN/RNN → ラベル
- **ジェスチャ / 動作認識**: IMU(I2C/SPI 接続) → ウィンドウ切り出し → 1D-CNN / DS-CNN → ラベル

#### ハードウェア接続案

| センサ | 接続先 | 備考 |
| --- | --- | --- |
| MEMS マイク(I2S) | SAI(2 系統あり) | I2S Click Board / Arduino シールド経由 |
| IMU(I2C/SPI) | LP Flexcomm 経由 | mikroBUS の Click Board が手早い |

#### 想定フロー

1. ハードウェア接続 → センサからの生データ取得を確認(シリアル / ロガー)
2. PC 側でデータセットを収集 → 前処理(特徴量) → モデル学習 → 量子化
3. eIQ Toolkit で NPU 向け変換 → SDK プロジェクトに組み込み
4. オンボードでリアルタイム推論 → 結果をシリアル / LED に出力
5. スコア表を埋める(特に「電流」の観点はバッテリ駆動を意識して重点)

#### 実行ログ(実機確認後に追記)

- 選んだタスク:
- 使用センサ品番:
- 前処理(サンプリングレート / フレーム長 / ホップ長 / 特徴量):
- モデル概要:
- スコア表:
- デモ動画 / 写真へのリンク:

#### つまずき・解決メモ

- _まだなし。SAI / I2C 周りのピン配・クロックドメイン、リアルタイム処理時の DMA 詰まりなどを想定して残す。_

## 参考リンク

- [製品購入ページ(DigiKey JP)](https://www.digikey.jp/ja/products/detail/nxp-usa-inc/FRDM-MCXN947/22036137)
- [クイックスタートガイド(日本語PDF)](https://www.nxp.com/docs/ja/quick-reference-guide/FRDM-MCXN947-QSG.pdf)
- [MCX N シリーズ Fact Sheet(PDF)](https://www.mouser.com/datasheet/2/302/MCXNFS-3103194.pdf)
- [FRDM-MCXN ナレッジハブ(NXPコミュニティ)](https://community.nxp.com/t5/FRDM-Training-Hub/FRDM-MCXN-Knowledge-Hub/ta-p/2199187)
- [Zephyr 対応ボードドキュメント](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html)
