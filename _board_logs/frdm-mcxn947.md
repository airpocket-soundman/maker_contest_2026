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
| Pmod ヘッダ(J7、2×6 ピン) | Digilent Pmod モジュール接続(SPI / I²C 系、Type 2A 互換) |
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
- 初回接続時、Windows のデバイスマネージャに `MCU-LINK` 系の COM ポートが見えれば OK。

#### 書き込み手段

本ボードでは以下のいずれの方法でもファームウェア書き込みが可能。

| 方法 | 経路 | 主な用途 |
| --- | --- | --- |
| **MCU-Link(SWD/CMSIS-DAP)** | MCU-Link 側 Type-C → オンボードデバッガ → SWD | 通常のビルド〜デバッグ。MCUXpresso for VS Code の標準フロー |
| **USB シリアル(ROM ISP ブートローダ)** | MCU-Link が出す仮想 COM(LPUART 経由)、または MCU 直結 Type-C(USB-HID/MSC ISP) | デバッガなしで書き換えたい場合 / MCU-Link が壊れた時の復旧 / 量産フラッシュ |

> MCX N947 は ROM 内蔵の ISP ブートローダ(`blhost` / MCUBootUtility 等で操作可能)を持つため、SWD を使わなくても USB シリアル経由でファーム書き換えができる。詳細手順とハマり所は実機で試した時点で本セクションに追記する。

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

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2001.png' | relative_url }}" alt="VS Code の MCUXpresso 拡張 QUICKSTART PANEL。Open MCUXpresso Installer がハイライトされている">
     <figcaption>図 1: QUICKSTART PANEL から「Open MCUXpresso Installer」を選ぶ</figcaption>
   </figure>
4. Installer が起動すると、初回は **使用統計の協力可否ダイアログ**が出るので Accept / Decline どちらかを選ぶ(後から `Usage Statistics` メニューで切替可能)。続いて **Changelog**(更新履歴)が表示されるので OK で閉じる。

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2002.png' | relative_url }}" alt="MCUXpresso Installer 起動直後の Help us to improve ダイアログ。Accept / Decline ボタン">
     <figcaption>図 2: 起動直後の使用統計ダイアログ(Accept / Decline はあとから変更可能)</figcaption>
   </figure>

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2003.png' | relative_url }}" alt="MCUXpresso Installer Changelog ダイアログ。Version 26.03.160 の改善点が一覧表示されている">
     <figcaption>図 3: 続いて表示される Changelog(OK で閉じる)</figcaption>
   </figure>

5. Installer のメイン画面に到達したら、一覧(**2 画面で全項目を網羅**)から、本ボードの NPU 開発で **必要なものだけ**を選んでインストール:

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2004.png' | relative_url }}" alt="MCUXpresso Installer メイン画面の上半分。Software Kits と Components の前半が見えている">
     <figcaption>図 4: Installer 画面 1/2(Software Kits / Components 上段)</figcaption>
   </figure>

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2005.png' | relative_url }}" alt="MCUXpresso Installer メイン画面の下半分。Components のデバッグプローブと Standalone Tools が見えている">
     <figcaption>図 5: Installer 画面 2/2(デバッグプローブ系と Standalone Tools)</figcaption>
   </figure>

   | カテゴリ | 項目 | 理由 |
   | --- | --- | --- |
   | Software Kits | **MCUXpresso SDK Developer** | FRDM-MCXN947 SDK を扱うため必須 |
   | Components | **Arm GNU Toolchain** | C/C++ ビルドに必須 |
   | Components | **Standalone Toolchain Add-ons** | Arm GNU 用 NXP 拡張ヘッダ・ライブラリ |
   | Components | **LinkServer** | オンボード MCU-Link をデバッグプローブとして使う |
   | Standalone Tools | **MCUXpresso Configuration Tools** | ピンマックス / クロック / ペリフェラル設定 GUI |
   | Standalone Tools | **GUI Guider** | LCD ヘッダで HMI を作る時の LVGL ベース設計ツール。画面表示系 |
   | Standalone Tools | **FreeMASTER** | 推論結果や電流波形をリアルタイム可視化するモニタ。画面表示系 |

   - **Zephyr Developer / Zephyr SDK / Matter Developer** は本ログでは Zephyr 不採用方針のため不要。
   - **SEGGER J-Link / PEmicro** は外付けプローブを使わない限り不要。
   - **Secure Provisioning Tool** はセキュアブート / プロビジョニングを扱う段階で追加すれば良い。
6. **Install** ボタンを押すと、コンポーネントによっては **NXP アカウントでのサインインを要求**される(SDK 系を含むほぼ全部)。

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2006.png' | relative_url }}" alt="NXP Authentication のサインインダイアログ。Email Address 入力欄と CONTINUE / CREATE AN ACCOUNT ボタン">
     <figcaption>図 6: インストール中に出る NXP アカウントのサインインダイアログ</figcaption>
   </figure>

   > **注意(回避策)**: このダイアログ内の **CREATE AN ACCOUNT** ボタンからアカウントを作ろうとすると、現状(2026 年時点)バグで完了しないことがある。
   > **先に [NXP 公式サイト](https://www.nxp.com/) でブラウザからアカウントを作成**しておき、その資格情報でこのダイアログにログインすれば問題なく進める。

7. 各コンポーネントごとに **License Agreement** ダイアログが順次出るので、内容を確認のうえ **I ACCEPT** で進める(コンポーネント数だけ繰り返し出る点に注意)。

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2007.png' | relative_url }}" alt="GUI Guider v1.10.1 の License Agreement ダイアログ。I ACCEPT / DECLINE ボタン">
     <figcaption>図 7: GUI Guider の License Agreement</figcaption>
   </figure>

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2008.png' | relative_url }}" alt="FreeMASTER tool 3.2 の License Agreement ダイアログ">
     <figcaption>図 8: FreeMASTER の License Agreement(同様にコンポーネントごとに出る)</figcaption>
   </figure>

8. インストールが進むと、最後に **環境変数を更新したので VS Code を再起動するよう促す Warning** が出る。OK で閉じる。

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2009.png' | relative_url }}" alt="MCUXpresso Installer の Warning message。環境変数を更新したので VS Code を再起動するよう促されている。画面下部のログには GUI Guider / FreeMASTER のダウンロード失敗メッセージが見える">
     <figcaption>図 9: 環境変数更新の警告(画面下にエラーログが出ている場合は要確認)</figcaption>
   </figure>

   > **実機で発生したインストールエラー(2026 年時点)**: 図 9 の画面下部ログに、**GUI Guider と FreeMASTER のダウンロード URL 取得失敗**が記録されていた:
   >
   > ```
   > [error] Could not get download URL for GUI-GUIDER-SETUP-1.10.1-GA-WIN. Skipping...
   > [error] Could not get download URL for FMASTERSW: 200: OK. Skipping download...
   > [error] Error occurred while installing FreeMASTER.
   > *** Installation error ***
   > ```
   >
   > LinkServer など多くのコンポーネントは正常にインストール済み(✅ 緑チェック)だが、上記 2 つは未インストール状態。**Installer 側の一時的不具合または NXP 配信側の問題**と思われ、後日 Installer の **更新マーク(右上のクラウド/再読み込みアイコン)で再試行**するか、各ツールを **NXP 公式サイトから個別ダウンロード**して導入することで回避可能。

9. VS Code を再起動。再起動後、アクティビティバーの MCUXpresso アイコンを開くと、**IMPORTED REPOSITORIES が空**の初期状態になっている。この時点で `Import Example from Repository` を開いても Repository / Toolchain の選択肢が無く、フォーム上にエラーが出る。

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2010.png' | relative_url }}" alt="VS Code 再起動後の MCUXpresso 拡張。IMPORTED REPOSITORIES が空で、右側の Import Example from Repository フォームには Please select a repository / Please select a toolchain のエラーが出ている">
     <figcaption>図 10: VS Code 再起動直後の MCUXpresso 拡張(リポジトリ未登録の初期状態)</figcaption>
   </figure>

10. QUICKSTART PANEL → **Import Repository** を押すと、Import Repository ダイアログが開く。**REMOTE** タブを選び、Repository ドロップダウンから **MCUXpresso SDK**(`https://github.com/nxp-mcuxpresso/mcuxsdk-manifests`)を選ぶ。本ボードでは新世代 MCUXpresso SDK のリポジトリを使う(Legacy 2.x / Zephyr 系 / Matter はここでは選ばない)。
11. Repository を選ぶと Revision / Name / Location などの入力欄が現れる。
    - **Revision**: デフォルトの `main` のままで良い(タグ指定したい場合のみ変更)
    - **Name**: ローカルでの識別名。デフォルト `mcuxsdk` を流用
    - **Location**: SDK 一式を展開するローカルパス。**ドキュメントリポジトリ(本リポ)とは別の作業ディレクトリ**を指定する(例: `d:\workspace\github`)。SDK は数 GB になるため、Git 管理下のディレクトリに紛れ込ませない

    入力後 **Import** ボタンを押すとリポジトリ取得が始まる。

    <figure>
      <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2011.png' | relative_url }}" alt="Import Repository ダイアログ。Repository に MCUXpresso SDK、Revision に main、Name に mcuxsdk、Location に d:\workspace\github が入力され、Import ボタンが押せる状態">
      <figcaption>図 11: Import 直前のダイアログ(Revision / Name / Location 入力済み)</figcaption>
    </figure>

    Import が完了すると IMPORTED REPOSITORIES に該当リポジトリが現れ、Import Example のフォームでも Repository / Board / Toolchain が選べるようになる。
12. **Import Example from Repository** で Repository に取得した SDK を選び、Board に `frdmmcxn947`、Template に `hello_world` を指定して取り込む(以降の手順は[Hello World / 動作確認ログ](#a-mcuxpresso-sdk-hello_worlduart-出力)参照)。ビルド → フラッシュで実機動作を確認する。

> 進めながら詰まった点・解決策はこの後の「Hello World / 動作確認ログ」に時系列で残す。

## Hello World / 動作確認ログ

最初の動作確認に使うサンプルと、その記録テンプレート。
扱うサンプルはすべて MCUXpresso SDK 経由(理由は[開発環境セットアップ](#開発環境セットアップ)に記載)。
**実機で確認できた値・出力・つまずきは各サンプルの「実行ログ」欄に追記していく。**

### A) MCUXpresso SDK: `hello_world`(UART 出力)

LPUART 経由でシリアル出力する SDK 同梱の定番サンプル。デバッグ I/O 経路の疎通確認用。

#### 手順

1. VS Code → MCUXpresso 拡張 → **IMPORT EXAMPLE FROM REPOSITORY**
2. 各フィールドを以下のように指定する:

   | フィールド | 値 | 補足 |
   | --- | --- | --- |
   | Repository | 取り込み済みの `mcuxsdk` (Version: 26.6.0) | [開発環境セットアップ手順 11](#開発環境セットアップ) で取得済み |
   | Board | `FRDM-MCXN947` | ボード写真と一致を確認 |
   | Template | `demo_apps/hello_world_cm33_core0` | 候補は[Template 早見表](#template-の選択肢-hello-で検索した時)を参照 |
   | App type | `Repository application` | ソース配置の違いのみ。詳細は[App type 早見表](#app-type-の選択肢)を参照 |
   | Name | `frdmmcxn947_hello_world_cm33_core0` | 任意。デフォルトのままでよい |
   | Toolchain | Arm GNU Toolchain 14.2.Rel1(`Use recommended version (14.2.1)` でも可) | MCUXpresso Installer で導入済み |

   <figure>
     <img src="{{ '/images/MCUXpresso%20for%20VSCode%20Install%2012.png' | relative_url }}" alt="Import Example from Repository フォーム。Repository に mcuxsdk、Board に FRDM-MCXN947、Template に demo_apps/hello_world_cm33_core0、App type に Repository application、Toolchain に Arm GNU Toolchain 14.2.Rel1 が設定され Import ボタンが押せる状態">
     <figcaption>図 12: Import 直前の入力済みフォーム(hello_world_cm33_core0 を Repository application として取り込む)</figcaption>
   </figure>

3. **Import** を押す。プロジェクトが `mcuxsdk/examples/...` 配下に生成され、PROJECTS ビューに現れる。
4. ステータスバーまたは QUICKSTART PANEL から **Build** → **Debug**(または Flash)。
   - **Build Configuration** に注意: `debug`(RAM ロード、リセットで消える)/ `flash_debug`(Flash 書き込み、電源オフでも残る)が用意されている。最初は `debug` で十分。残したくなったら `flash_debug` に切り替える。
5. シリアルターミナル(VS Code 内蔵 Serial Monitor または TeraTerm 等)を **115200 / 8N1** で開く。

##### Template の選択肢(`hello` で検索した時)

| テンプレート | 用途 |
| --- | --- |
| **`demo_apps/hello_world_cm33_core0`** | **標準版**。Core0 + LPUART(MCU-Link 経由 COM)で `hello world.`。**最初の疎通確認はこれ** |
| `demo_apps/hello_world_qspi_xip_cm33_core0` | 外付け QSPI フラッシュから XIP 実行する版 |
| `demo_apps/hello_world_virtual_com_cm33_core0` | シリアル出力先が MCU 直結 USB の Virtual COM(USB CDC) |
| `freertos_examples/freertos_hello_cm33_core0` | FreeRTOS タスクから hello world を出す |
| `multicore_examples/hello_world_primary_core` | Core0 が Core1 を起動するデュアルコア構成 |
| `trustzone_examples/hello_world_ns_cm33_core0` | TrustZone 分離環境の Non-Secure 側で動く |

##### App type の選択肢

| App type | 中身 | こういう時 |
| --- | --- | --- |
| **Repository application** | `mcuxsdk/examples/...` 配下にプロジェクトを作り SDK ソースを参照する(コピーしない) | **疎通確認・実験段階(今ここ)** |
| **Freestanding application** | SDK の必要ファイルを指定先にコピーして自己完結型に | コンテスト提出物・配布物として独立させる時 |

> RAM 実行 / Flash 書き込みは App type ではなく **Build Configuration**(リンカスクリプト `*_ram.ld` / `*_flash.ld`)で決まる点に注意。

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

### B) MCUXpresso SDK: `led_blinky_peripheral`

GPIO で基板上のユーザー LED(RGB の 1 色)を点滅させる、デバッガ・フラッシュ経路の "千本ノック" 用サンプル。

> FRDM-MCXN947 のオンボードユーザー LED は **RGB 3 色 × 1 個**。Zephyr DTS 上のピン配置は Red=GPIO0\_P10 / Green=GPIO0\_P27 / Blue=GPIO1\_P2(いずれも ACTIVE_LOW)。SDK サンプルは通常このうち 1 色だけを点滅させる。

#### 手順

1. MCUXpresso 拡張 → **IMPORT EXAMPLE** → Repository に `mcuxsdk`、Board に `FRDM-MCXN947`、Template 検索ボックスに `led` と入力すると 3 候補が出るので **`demo_apps/led_blinky_peripheral_cm33_core0`** を選ぶ。
2. App type: `Repository application` / Toolchain: Arm GNU Toolchain で Import。
3. Build Configuration `debug` で **Build → Debug**(または Flash)。
4. ボード上のユーザー LED が約 1 Hz 程度で点滅することを確認。

##### Template の選択肢(`led` で検索した時)

| テンプレート | 用途 |
| --- | --- |
| **`demo_apps/led_blinky_peripheral_cm33_core0`** | **標準の点滅デモ**。GPIO ペリフェラル直叩きで LED を周期 ON/OFF。**最初はこれ** |
| `cmsis_driver_examples/gpio/cmsis_button_toggle_led_cm33_core0` | CMSIS-Driver(ベンダ非依存の標準 API)+ ユーザーボタン押下で LED トグル |
| `driver_examples/gpio/gpio_led_output_cm33_core0` | SDK GPIO ドライバ(`fsl_gpio.c`)の使い方リファレンス |

#### 実行ログ(実機確認後に追記)

- 点滅した LED の色 / シルク番号:
- 点滅周期(目視):
- 備考:

#### つまずき・解決メモ

- _まだなし。_

### C) NPU を使った "Hello World"(最小推論サンプル)

eIQ Neutron NPU の動作確認用最小プロジェクトとして、SDK 同梱の **`eiq_examples/tflm_label_image_cm33_core0`** を使う。
TensorFlow Lite for Microcontrollers + Neutron NPU で、組み込みモデル(MobileNet 系の量子化モデル)に対する 1 枚画像のラベル推論を行うサンプル。**外部センサ不要**で、ボードに焼くだけでシリアルに推論結果が出る。

#### 手順

1. MCUXpresso 拡張 → **IMPORT EXAMPLE** → Repository に `mcuxsdk`、Board に `FRDM-MCXN947`、Template 検索ボックスに `tflm` と入力 → **`eiq_examples/tflm_label_image_cm33_core0`** を選ぶ。
2. App type: `Repository application` / Toolchain: Arm GNU Toolchain で Import。
3. **ビルド**: Build Configuration `debug` または `flash_debug` で Build。TFLM ライブラリの初回コンパイルがあるため数分かかる。ビルドログに `Neutron` / `NPU` 系の文字列が出ているか確認(出ていなければ CPU フォールバック扱い)。
4. **書き込み + 実行**: Debug または Flash → シリアル(115200 / 8N1)で出力を確認。
5. 推論結果のラベル名と推論時間(ms)をログに残す。

##### Template の選択肢(`tflm` で検索した時)

| テンプレート | 中身 | 用途 |
| --- | --- | --- |
| **`eiq_examples/tflm_label_image_cm33_core0`** | **画像分類**、組み込みモデル + 組み込み画像で 1 枚推論。外部接続不要 | **NPU の最初の動作確認はこれ** |
| `eiq_examples/tflm_cifar10_cm33_core0` | CIFAR-10 の 10 クラス分類 | 別モデルでの比較計測 |
| `eiq_examples/tflm_kws_cm33_core0` | Keyword Spotting(キーワード検出)。バンドル PCM データで動く版あり | 音声系の足がかり |
| `eiq_examples/tflm_lib_cm33_core0` | TFLM ライブラリ自体のビルドサンプル(推論アプリではない) | 通常は不要 |
| `eiq_examples/tflm_modelrunner_cm33_core0` | 任意モデルを差し込んで動かす汎用ランナー | 自作モデル投入時の土台 |

> カメラ + 推論パイプラインを試すサンプルは別カテゴリで、Template 検索を `mpp` に変えると `eiq_examples/mpp_cm33_core0` 系が出る。NPU の最初の動作確認では使わない。

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
