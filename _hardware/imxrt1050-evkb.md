---
title: IMXRT1050-EVKB (NXP i.MX RT1050 クロスオーバー MCU 評価キット)
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

```
┌────────────────────────────────────────────────────────────────────────┐
│  USB micro-B (J28: OpenSDA/LPC-Link2 デバッガ)                         │
│  USB micro-B (J9: USB OTG #1)                                          │
│  USB Type-A (J12: USB OTG #2 ホスト)                                   │
│  5V DC Jack (J2)                                                       │
│                                                                        │
│  ┌────────────────────────────────────────────────────────────────┐    │
│  │              i.MX RT1052 (Cortex-M7, 600 MHz)                   │    │
│  │  TCM 最大 512KB / OCRAM / DCP / BEE                             │    │
│  └─┬───────┬───────┬──────┬─────────┬─────────┬───────────┬───────┘    │
│    │       │       │      │         │         │           │            │
│  FlexSPI  SEMC   SDIO   USB-OTG×2  Ethernet  LCD parallel  CSI Camera  │
│    │       │       │      │         │         │           (J35)        │
│    ▼       ▼       ▼      ▼         ▼         ▼                        │
│  HyperFlash 64MB / QSPI 8MB                                            │
│  SDRAM 32MB                                                            │
│  microSD ソケット (J20)                                                │
│                                                                        │
│  Arduino R3 互換ヘッダ J22-J25(直接実装、はんだ付け不要)             │
│  FXOS8700CQ 6軸センサ(加速度+磁気)                                  │
│  3.5mm オーディオジャック / オンボードマイク / スピーカー I/F (J17)    │
│  SAI / SPDIF / オーディオコーデック WM8960                             │
│  ユーザボタン×2 / RGB LED / リセット SW3                                │
└────────────────────────────────────────────────────────────────────────┘
```

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
