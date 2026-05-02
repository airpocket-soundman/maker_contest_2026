---
title: IMXRT1050-EVKB (NXP i.MX RT1050 クロスオーバー MCU 評価キット)
short_title: IMXRT1050-EVKB
slug: imxrt1050-evkb
tagline: Cortex-M7 600MHz クロスオーバー MCU の高性能リアルタイム評価キット
manufacturer: NXP Semiconductors
category: 評価ボード(リアルタイム制御 / 高性能 MCU)
official_url: https://www.nxp.com/design/design-center/development-boards-and-designs/MIMXRT1050-EVKB

features:
  - i.MX RT1050 クロスオーバー MCU "MIMXRT1052DVL6B" (Arm Cortex-M7 最大 600MHz) を搭載
  - 内蔵 TCM (Tightly-Coupled Memory) 最大 512KB と 32MB SDRAM / 64MB HyperFlash / 8MB QSPI Flash の大規模メモリ構成
  - LCD パラレル(16/24bit)・カメラ・SDIO・Ethernet・USB OTG・I²S・SPDIF など マルチメディア向け I/F を完備
  - **FXOS8700 6軸モーションセンサ** (加速度+磁気) をオンボード搭載
  - Arduino R3 互換ヘッダ (J22-J25) がボード上に直接実装済(初版 EVK の改良版)
  - オンボード OpenSDA / LPC-Link2 デバッガ搭載 (CMSIS-DAP / DAPLink)、外部 J-Link も使用可
  - NXP DCP (Data Co-Processor) で AES/SHA 暗号アクセラ
  - DigiKey Make ONE Challenge 2026 で「おすすめ製品」として一次審査の加点対象

specs:
  - label: 搭載 MCU
    value: NXP MIMXRT1052DVL6B (Arm Cortex-M7 最大 **600 MHz** / クロスオーバー MCU)
  - label: 内蔵メモリ
    value: TCM (Tightly-Coupled Memory) 最大 **512KB** / OCRAM
  - label: 外付けメモリ
    value: SDRAM **32MB** (IS42S16160) / HyperFlash **64MB** (512Mb、デフォルト) / QSPI Flash **8MB** (64Mb、リワーク版)
  - label: メモリ I/F
    value: FlexSPI / SEMC (SDRAM/NAND/NOR 共通コントローラ) / SDIO / eMMC
  - label: 通信ペリフェラル
    value: USB OTG ×2 / 10/100 Ethernet / 2× CAN / 8× UART / 4× I²C / 4× SPI / SDIO
  - label: マルチメディア
    value: パラレル LCD (16/24bit) / カメラ I/F (CSI、J35) / 2D グラフィックスエンジン / SAI (I²S) / SPDIF / 3.5mm オーディオジャック / オンボードマイク
  - label: AI アクセラレータ
    value: なし(CMSIS-NN / TensorFlow Lite for Microcontrollers を CPU で実行、Cortex-M7 600MHz の高速演算で軽量〜中型モデルが現実的)
  - label: 搭載センサ
    value: **FXOS8700CQ** 6軸センサ(加速度+磁気)、I²C 接続
  - label: 拡張ヘッダ
    value: Arduino R3 (J22-J25、ボードに直接実装) / カメラコネクタ J35 / LCD 用 I/F / SD カードスロット
  - label: デバッグ
    value: オンボード **OpenSDA** (旧 A/A1 リビジョン) または **LPC-Link2** (新 B/B1 リビジョン)、CMSIS-DAP/DAPLink 互換 / 外部 J-Link OK
  - label: セキュリティ
    value: DCP (Data Co-Processor、AES/SHA 暗号化) / Bus Encryption Engine (BEE) / TrustZone-M
  - label: 電源
    value: USB micro-B / 5V DC ジャック (J2)
  - label: ロジックレベル
    value: 3.3V CMOS (Arduino 5V シールドは要レベル変換)
  - label: 価格目安
    value: ¥18,572 (DigiKey JP)

resources:
  - name: NXP - MIMXRT1050-EVKB 製品ページ
    url: https://www.nxp.com/design/design-center/development-boards-and-designs/MIMXRT1050-EVKB
  - name: ハードウェアユーザーガイド (PDF, NXP コミュニティ配布)
    url: https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/imxrt/3368/1/IMXRT1050EVKBHUG.pdf
    note: ピン配置・回路図・コネクタ・搭載コンポーネントの公式仕様
  - name: ハードウェアユーザーガイド (Keil 配布ミラー、PDF)
    url: https://pack-content.cmsis.io/Keil/IMXRT1050-EVKB_BSP/1.2.0/Documents/MIMXRT1050EVKHUG.pdf
  - name: DigiKey JP - IMXRT1050-EVKB 商品ページ
    url: https://www.digikey.jp/ja/products/detail/nxp-usa-inc/IMXRT1050-EVKB/8440447
  - name: NXP - MCUXpresso for VS Code (拡張機能)
    url: https://marketplace.visualstudio.com/items?itemName=NXPSemiconductors.mcuxpresso
  - name: NXP - eIQ ML ツールキット
    url: https://www.nxp.com/design/design-center/software/eiq-ml-development-environment
  - name: Zephyr Project - MIMXRT1050-EVK ボードドキュメント
    url: https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1050_evk/doc/index.html
  - name: NuttX - i.MX RT1050 EVK サポート
    url: https://nuttx.apache.org/docs/latest/platforms/arm/imxrt/boards/imxrt1050-evk/index.html
  - name: Mbed - IMXRT1050-EVKB プラットフォーム
    url: https://os.mbed.com/platforms/MIMXRT1050-EVK/
  - name: NXP Community - IMXRT1050-EVKB 回路図スレッド
    url: https://community.nxp.com/t5/i-MX-Processors/IMXRT1050-EVKB-schematics/m-p/745205
---

## 概要

IMXRT1050-EVKB は NXP の **クロスオーバー MCU** i.MX RT1052 を搭載した評価キットで、Cortex-M7 最大 **600MHz** の演算性能と マイコン並みのリアルタイム性を両立します。LCD/カメラ I/F、Ethernet、USB OTG、SAI/SPDIF オーディオなどを揃え、HMI 機器・ロボット制御・高速画像処理・モーターコントロールなどに適合します。**EVKB** は初版 EVK の改良版で、Arduino ヘッダがボードに直接実装済みです。

DigiKey Make ONE Challenge 2026 では「おすすめ製品」(NXP 4 ボードの 1 つ) として、一次審査の加点対象になります。

## ボード ブロック図

<svg class="board-diagram" viewBox="0 0 820 620" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="IMXRT1050-EVKB ボード ブロック図">
  <defs>
    <marker id="arrow-rt" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#4b5563"/>
    </marker>
  </defs>
  <!-- 上段: USB / 電源 / デバッガ -->
  <rect class="box box-power" x="10" y="10" width="195" height="50" rx="4"/>
  <text class="label label-bold" x="107" y="32" text-anchor="middle">USB micro-B (J28)</text>
  <text class="label label-small" x="107" y="48" text-anchor="middle">OpenSDA / LPC-Link2 デバッガ</text>
  <rect class="box box-power" x="215" y="10" width="195" height="50" rx="4"/>
  <text class="label label-bold" x="312" y="32" text-anchor="middle">USB micro-B (J9)</text>
  <text class="label label-small" x="312" y="48" text-anchor="middle">USB OTG #1</text>
  <rect class="box box-power" x="420" y="10" width="195" height="50" rx="4"/>
  <text class="label label-bold" x="517" y="32" text-anchor="middle">USB Type-A (J12)</text>
  <text class="label label-small" x="517" y="48" text-anchor="middle">USB OTG #2 ホスト</text>
  <rect class="box box-power" x="625" y="10" width="185" height="50" rx="4"/>
  <text class="label label-bold" x="717" y="32" text-anchor="middle">5V DC Jack (J2)</text>
  <text class="label label-small" x="717" y="48" text-anchor="middle">外部給電</text>
  <!-- MCU -->
  <rect class="box box-mcu" x="10" y="80" width="800" height="80" rx="6"/>
  <text class="label label-bold" x="410" y="106" text-anchor="middle" font-size="15">NXP i.MX RT1052 (Cortex-M7, 600 MHz クロスオーバー MCU)</text>
  <text class="label" x="410" y="126" text-anchor="middle">TCM 最大 512KB / OCRAM / DCP (AES/SHA) / BEE / TrustZone-M</text>
  <text class="label label-small" x="410" y="144" text-anchor="middle">FlexSPI / SEMC / SDIO / USB-OTG×2 / Ethernet / SAI / SPDIF / 16bit ADC / FlexPWM</text>
  <!-- メモリ I/F 行 -->
  <rect class="box box-mem" x="10" y="180" width="260" height="60" rx="4"/>
  <text class="label label-bold" x="140" y="202" text-anchor="middle">FlexSPI</text>
  <text class="label label-small" x="140" y="218" text-anchor="middle">HyperFlash 64MB (デフォルト)</text>
  <text class="label label-small" x="140" y="232" text-anchor="middle">QSPI 8MB (リワーク版) / XIP 実行</text>
  <rect class="box box-mem" x="280" y="180" width="260" height="60" rx="4"/>
  <text class="label label-bold" x="410" y="202" text-anchor="middle">SEMC</text>
  <text class="label label-small" x="410" y="218" text-anchor="middle">SDRAM 32MB (IS42S16160)</text>
  <text class="label label-small" x="410" y="232" text-anchor="middle">大容量バッファ・LCD フレーム</text>
  <rect class="box box-mem" x="550" y="180" width="260" height="60" rx="4"/>
  <text class="label label-bold" x="680" y="202" text-anchor="middle">SDIO / microSD (J20)</text>
  <text class="label label-small" x="680" y="218" text-anchor="middle">アプリ / 大容量データ</text>
  <text class="label label-small" x="680" y="232" text-anchor="middle">eMMC 接続も可</text>
  <!-- マルチメディア / 通信 -->
  <rect class="box box-io" x="10" y="260" width="260" height="80" rx="4"/>
  <text class="label label-bold" x="140" y="282" text-anchor="middle">Ethernet / CAN</text>
  <text class="label label-small" x="140" y="298" text-anchor="middle">10/100 Ethernet PHY</text>
  <text class="label label-small" x="140" y="312" text-anchor="middle">CAN ×2 (FlexCAN)</text>
  <text class="label label-small" x="140" y="326" text-anchor="middle">産業用ネットワーク</text>
  <rect class="box box-io" x="280" y="260" width="260" height="80" rx="4"/>
  <text class="label label-bold" x="410" y="282" text-anchor="middle">LCD / カメラ I/F</text>
  <text class="label label-small" x="410" y="298" text-anchor="middle">パラレル LCD (16/24bit)</text>
  <text class="label label-small" x="410" y="312" text-anchor="middle">CSI カメラ (J35)</text>
  <text class="label label-small" x="410" y="326" text-anchor="middle">2D グラフィックスエンジン</text>
  <rect class="box box-io" x="550" y="260" width="260" height="80" rx="4"/>
  <text class="label label-bold" x="680" y="282" text-anchor="middle">オーディオ</text>
  <text class="label label-small" x="680" y="298" text-anchor="middle">SAI (I²S) / SPDIF</text>
  <text class="label label-small" x="680" y="312" text-anchor="middle">WM8960 コーデック</text>
  <text class="label label-small" x="680" y="326" text-anchor="middle">3.5mm Jack / マイク / SP J17</text>
  <!-- 拡張 -->
  <rect class="box" x="10" y="360" width="800" height="50" rx="4"/>
  <text class="label label-bold" x="410" y="382" text-anchor="middle">Arduino R3 互換ヘッダ J22 / J23 / J24 / J25 (ボードに直接実装、はんだ付け不要)</text>
  <text class="label label-small" x="410" y="398" text-anchor="middle">D0-D15 / A0-A5 / 5V/3.3V/GND ・ I²C は J24 ピン9/10 ではなく J23 ピン5/6 を使用</text>
  <!-- 搭載センサ -->
  <rect class="box box-mem" x="10" y="430" width="395" height="60" rx="4"/>
  <text class="label label-bold" x="207" y="452" text-anchor="middle">FXOS8700CQ 6軸センサ</text>
  <text class="label label-small" x="207" y="468" text-anchor="middle">加速度 + 磁気センサ</text>
  <text class="label label-small" x="207" y="482" text-anchor="middle">I²C 接続</text>
  <rect class="box" x="415" y="430" width="395" height="60" rx="4"/>
  <text class="label label-bold" x="612" y="452" text-anchor="middle">ユーザインターフェース</text>
  <text class="label label-small" x="612" y="468" text-anchor="middle">ユーザボタン ×2 / RGB LED</text>
  <text class="label label-small" x="612" y="482" text-anchor="middle">リセット SW3</text>
  <!-- セキュリティ -->
  <rect class="box" x="10" y="510" width="800" height="50" rx="4" fill="#fee2e2" stroke="#dc2626"/>
  <text class="label label-bold" x="410" y="532" text-anchor="middle">DCP (Data Co-Processor) + BEE (Bus Encryption Engine)</text>
  <text class="label label-small" x="410" y="548" text-anchor="middle">AES / SHA ハードウェアアクセラ ・ XIP 実行コードのオンザフライ復号</text>
  <!-- Arrows -->
  <path d="M 107 60 L 107 80" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-rt)"/>
  <path d="M 312 60 L 312 80" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-rt)"/>
  <path d="M 517 60 L 517 80" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-rt)"/>
  <path d="M 717 60 L 717 80" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-rt)"/>
  <path d="M 140 160 L 140 180" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 410 160 L 410 180" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 680 160 L 680 180" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 140 240 L 140 260" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 410 240 L 410 260" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 680 240 L 680 260" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 410 340 L 410 360" stroke="#2563eb" stroke-width="2" fill="none"/>
</svg>

> 詳細なブロック図・回路図は [ハードウェアユーザーガイド](https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/imxrt/3368/1/IMXRT1050EVKBHUG.pdf) を参照。

## 主要 GPIO / ヘッダ

| ヘッダ/コネクタ | 用途 |
|---|---|
| **Arduino R3 (J22-J25)** | D0-D15 / A0-A5 / 電源(5V/3.3V/GND)。J24 ピン9/10 は Arduino I²C 標準と非互換のため、I²C は **J23 ピン5/6** を使う |
| カメラコネクタ J35 | CSI パラレルカメラ(OV7725 ベース CA031C / MT9M114 ベース CA111C などを直結可) |
| LCD 用 I/F | パラレル LCD (16/24bit、RK043FN02H-CT 等) を直結 |
| microSD スロット (J20) | アプリ・大容量データ用 |
| オーディオ J17 | スピーカー出力 |
| ユーザ SW2 / SW3 | プッシュボタン (SW3 = リセット) |
| RGB LED | ステータス表示用 |

> **正確な GPIO 番号は必ず [ハードウェアユーザーガイド](https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/imxrt/3368/1/IMXRT1050EVKBHUG.pdf) §「Arduino Interface」(Table 6) と Zephyr の board overlay (`mimxrt1050_evk.dts`) を参照してください。**

## 電源系統

| 項目 | 仕様 |
|---|---|
| 主電源 | USB micro-B (J28、デバッガ) もしくは 5V DC ジャック (J2) |
| MCU 動作電圧 | 3.3V (内部 SMPS で生成、ロジックレベル 3.3V CMOS) |
| 内部レギュレータ | i.MX RT1052 内蔵 SMPS で各電源ドメイン(VDD_CORE/SOC/USB/SNVS 等)を生成。外部に DCDC コンポーネント |
| 消費電流 | 600MHz フル稼働 + 周辺有効で 数百 mA 級。低消費電力モードで mA 以下 |
| 5V 出力 | Arduino ヘッダの 5V/3.3V 端子から外部給電も可 |

## 開発環境

| 種類 | 対応環境 |
|---|---|
| 公式 IDE (Eclipse) | **MCUXpresso IDE** |
| 公式 IDE (VS Code) | **MCUXpresso for VS Code** ([Marketplace](https://marketplace.visualstudio.com/items?itemName=NXPSemiconductors.mcuxpresso))。i.MX RT 全般を完全サポート |
| SDK | **MCUXpresso SDK** (IMXRT1050 ボードコンポーネント・サンプル込み) |
| 設定ツール | MCUXpresso Config Tools |
| インストーラ | MCUXpresso Installer (SDK / Toolchain / Zephyr SDK / Debug ソフトを統合) |
| 商用 IDE | Keil MDK / IAR EWARM |
| RTOS | FreeRTOS / Azure RTOS ThreadX / Zephyr / NuttX / Mbed OS |
| GUI フレームワーク | NXP **GUI Guider** / SEGGER emWin / **LVGL** / TouchGFX |
| AI ライブラリ | **eIQ Toolkit** + CMSIS-NN / TensorFlow Lite for Microcontrollers (CPU 推論) |
| デバッグ | オンボード OpenSDA (旧) / LPC-Link2 (新)、CMSIS-DAP / DAPLink。外部 J-Link / SEGGER OZONE OK |
| 書込み Runner | LinkServer (デフォルト) / J-Link / pyOCD |

### MCUXpresso for VS Code (補足)

NXP の VS Code 拡張機能は IMXRT1050-EVKB に完全対応。Eclipse 版とほぼ同等の開発体験が得られます。

- **インストール**: VS Code 拡張 `NXPSemiconductors.mcuxpresso` を入れる(C/C++ 拡張も自動)
- **対応**: i.MX RT 全般 (RT500 / RT600 / RT1010 / RT1020 / RT1050 / RT1060 / RT1170 …)
- **デバッグ**: OpenSDA/LPC-Link2/J-Link/CMSIS-DAP のいずれも認識
- **特徴**: HyperFlash/QSPI Flash の XIP デバッグ、ペリフェラルレジスタビュー、RTOS スレッド表示、Heap/Stack 解析

## XIP 実行と起動の仕組み

i.MX RT は **MCU 並みの低レイテンシ** と **アプリケーションプロセッサ並みの大容量メモリ** を両立する「クロスオーバー」設計です。

- **コードは外付け HyperFlash / QSPI Flash から XIP (Execute-In-Place) 実行** が基本
- ブート ROM が起動時に Flash の **IVT (Image Vector Table)** を読み込み、デコード → DCD で SDRAM 初期化 → アプリ起動
- 高速性が必要なルーチンは **TCM** に配置(リンカスクリプトで `__RAMFUNC()` 修飾)
- デバッグ初期は内蔵 SRAM (OCRAM) 配置だと書込みが速くて便利

## AI / 機械学習

専用 NPU は無いものの、Cortex-M7 600MHz の演算性能 + 大容量 SDRAM/HyperFlash により、**MCU 単独で軽量〜中型のモデルを CPU 推論** で動かせます。

- **CMSIS-NN**: Arm の組込み NN 最適化ライブラリ
- **TensorFlow Lite for Microcontrollers**: 量子化済み TFLite モデルをそのまま実行
- **eIQ Toolkit**: TF / ONNX / PyTorch から TFLite 変換、量子化、ベンチマーク。MCXN947 のような Neutron NPU 専用変換は不要
- **代表サンプル**: 画像分類 (MobileNet)、KWS (キーワードスポッティング)、振動・電流からの異常検知、姿勢推定の軽量版
- 大容量 SDRAM/HyperFlash があるので、MCXN947 (内蔵 RAM 数百 KB 制約) では収まらないモデルも CPU 推論で扱える

> 高速 AI が要件なら、外付け HyperFlash 上にモデルを置き、推論時に必要な分だけ TCM/OCRAM にコピーして実行する設計パターンが定石です。

## 代表的なサンプルアプリ

- `evkbimxrt1050_demo_apps_lvgl_guider` — GUI Guider / LVGL による HMI
- `evkbimxrt1050_eiq_examples_*` — 画像分類・KWS・異常検知
- `evkbimxrt1050_lwip_*` — Ethernet TCP/IP スタック
- `evkbimxrt1050_usb_*` — USB ホスト/デバイス各種クラス
- `evkbimxrt1050_freertos_*` — FreeRTOS リファレンス
- モータ制御サンプル(FOC、3相 PMSM)
- カメラ + LCD によるリアルタイム画像処理デモ

## 入手方法

- DigiKey JP: [IMXRT1050-EVKB](https://www.digikey.jp/ja/products/detail/nxp-usa-inc/IMXRT1050-EVKB/8440447) (¥18,572 前後)
- NXP 直販 / Mouser / Arrow Electronics などからも入手可

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。実際の開発では必ず[ハードウェアユーザーガイド](https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/imxrt/3368/1/IMXRT1050EVKBHUG.pdf)、[NXP 公式ページ](https://www.nxp.com/design/design-center/development-boards-and-designs/MIMXRT1050-EVKB) と MCUXpresso SDK のサンプルで最新の仕様(ピン対応表・電気的定格・XIP 設定など)を確認してください。
