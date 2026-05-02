---
title: NXP 推奨評価ボード 4 種比較 (DigiKey Make ONE Challenge 2026)
slug: nxp-frdm-eval-boards
tagline: FRDM-MCXC444 / FRDM-MCXN947 / FRDM-IMX91 / IMXRT1050-EVKB の 4 ボード比較と開発環境
manufacturer: NXP Semiconductors
category: 評価ボード(MCU / Linux / エッジAI / リアルタイム制御)
official_url: https://www.nxp.com/

features:
  - DigiKey Make ONE Challenge 2026 で「おすすめ製品」として一次審査の加点対象になる NXP 4 ボードを 1 ページで横比較
  - エントリ向け Cortex-M0+ (MCXC444) からエッジAI(MCXN947 + NPU)、組込み Linux(i.MX 91)、高性能リアルタイム(i.MX RT1050) までを網羅
  - 各ボードで利用できる開発環境(IDE / SDK / RTOS)を整理

specs:
  - label: 共通の特徴
    value: NXP MCU/MPU 評価ボード、オンボードデバッガ搭載(USB 1本で書込み・デバッグ可)
  - label: 共通の開発スイート
    value: MCUXpresso IDE / MCUXpresso for VS Code / MCUXpresso SDK / eIQ ML ツールキット
  - label: 加点対象コンテスト
    value: DigiKey Make ONE Challenge 2026 (NXP 製品使用で一次審査加点)

resources:
  - name: NXP - FRDM-MCXC444 製品ページ
    url: https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-MCXC444
  - name: NXP - FRDM-MCXN947 製品ページ
    url: https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-MCXN947
  - name: NXP - FRDM-IMX91 製品ページ
    url: https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-IMX91
  - name: NXP - MIMXRT1050-EVKB 製品ページ
    url: https://www.nxp.com/design/design-center/development-boards-and-designs/MIMXRT1050-EVKB
  - name: FRDM-MCXC444 ユーザーマニュアル UM12120 (PDF)
    url: https://docs.rs-online.com/00be/A700000012839604.pdf
  - name: FRDM-IMX91 ユーザーマニュアル UM12262 (PDF)
    url: https://www.farnell.com/datasheets/4594689.pdf
  - name: IMXRT1050-EVKB ハードウェアユーザーガイド (PDF)
    url: https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/imxrt/3368/1/IMXRT1050EVKBHUG.pdf
  - name: NXP - MCUXpresso 開発スイート
    url: https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-software-development-kit-sdk
  - name: NXP - eIQ ML ツールキット
    url: https://www.nxp.com/design/design-center/software/eiq-ml-development-environment
  - name: DigiKey - FRDM-MCXC444 取扱
    url: https://www.digikey.com/en/products/detail/nxp-usa-inc/FRDM-MCXC444/24374774
  - name: DigiKey - FRDM-MCXN947 取扱
    url: https://www.digikey.com/en/products/detail/nxp-usa-inc/FRDM-MCXN947/22036137
  - name: DigiKey - FRDM-IMX91 取扱
    url: https://www.digikey.in/en/products/detail/nxp-usa-inc/FRDM-IMX91/26236212
  - name: DigiKey - IMXRT1050-EVKB 取扱
    url: https://www.digikey.com/product-detail/en/nxp-usa-inc/IMXRT1050-EVKB/568-13886-ND/8440447
---

## 概要

DigiKey Make ONE Challenge 2026 では、スポンサーである **NXP Semiconductors** の以下 4 ボードが「おすすめ製品」に指定されており、作品で使用すると **一次審査での加点対象** になります。各ボードは想定アプリケーションとコア性能が大きく異なるため、用途に合ったものを選んでください。

| 略称 | 想定用途 | 一言で |
|---|---|---|
| **FRDM-MCXC444** | エントリ・低消費電力 IoT | Cortex-M0+ 48MHz の入門 MCU 評価ボード |
| **FRDM-MCXN947** | エッジ AI / 産業 IoT | NPU 内蔵デュアル M33、組込みAI推論向け |
| **FRDM-IMX91** | 組込み Linux / IoT ゲートウェイ | Cortex-A55 1.4GHz + Wi-Fi 6/BLE/802.15.4 |
| **IMXRT1050-EVKB** | 高性能リアルタイム制御・グラフィックス | Cortex-M7 600MHz クロスオーバー MCU |

## 性能比較表

| 項目 | FRDM-MCXC444 | FRDM-MCXN947 | FRDM-IMX91 | IMXRT1050-EVKB |
|---|---|---|---|---|
| 搭載チップ | MCXC444 | MCXN947 | i.MX 91 (アプリケーションプロセッサ) | i.MX RT1052 (クロスオーバー MCU) |
| コア | Arm Cortex-M0+ | デュアル Arm Cortex-M33 + DSP | Arm Cortex-A55 (シングル) | Arm Cortex-M7 |
| 最大動作周波数 | 48 MHz | 150 MHz | 1.4 GHz | 600 MHz |
| 内蔵 Flash | 256 KB(*) | 2 MB | (なし、外付け) | (なし、外付け QSPI/HyperFlash) |
| 内蔵 RAM | 32 KB(*) | 構成可能(フルECC RAM) | (なし、LPDDR4 1GB 外付け) | オンチップ SRAM 最大 512 KB |
| 外部メモリ | — | — | LPDDR4 1GB / eMMC 8GB / microSD | SDRAM 32MB / HyperFlash 64MB / QSPI 8MB |
| AI アクセラレータ | なし | **eIQ Neutron NPU** | (CPU で eIQ ライブラリを実行) | CMSIS-NN / TFLite Micro (CPU) |
| 搭載センサ | 3軸加速度 FXLS8974CFR3、可視光センサ | (なし、拡張ヘッダ経由) | (なし、拡張ヘッダ経由) | (なし、拡張ヘッダ経由) |
| 主な通信 I/F | USB / I²C / SPI / UART / SLCD | Hi-Speed USB / CAN 2.0 / I3C / 10/100 Ethernet | USB / Ethernet / Wi-Fi 6 / BLE 5.4 / 802.15.4 | USB OTG / Ethernet / CAN / SDIO / I²S / SPDIF |
| 拡張ヘッダ | Arduino R3 / mikroBUS / Pmod / FRDM | Arduino R3 / mikroBUS / Pmod | 40pin GPIO 拡張 + 2x5 NXP I/F | Arduino R3 (ボードに直接実装) |
| グラフィックス | SLCD セグメント駆動 | — | (HDMI 等は無し、組込み Linux 側で対応) | パラレル LCD (16/24bit) / カメラ I/F |
| 想定 OS | ベアメタル / RTOS | ベアメタル / RTOS / Zephyr | **Linux** (Yocto/Buildroot) | ベアメタル / RTOS / Linux |
| デバッガ | オンボード MCU-Link (CMSIS-DAP) | オンボード MCU-Link (CMSIS-DAP) | オンボードデバッガ + Linux シリアルコンソール | オンボード OpenSDA (DAPLink) |
| 電源 | USB Type-C | USB Type-C | USB Type-C (PD 対応) | USB micro-B / 5V DC |
| ロジックレベル | 3.3V CMOS | 3.3V / 1.8V (周辺で切替) | 3.3V CMOS | 3.3V CMOS |
| ボードサイズ感 | 小型(Freedom 標準) | 小型(Freedom 標準) | 中型(Linux ボード相当) | 中型(EVK 標準) |

(*) FRDM-MCXC444 の MCXC444 チップは Flash 256KB / RAM 32KB が公式値。DigiKey 推奨ページに「Flash 2MB/SRAM 256KB」と記載があるが、これは MCX C シリーズ全体の上限値の表現と思われる。実機の MCXC444 チップは 256KB/32KB。

## 開発環境(IDE / SDK / RTOS)対応

各ボードで利用可能な代表的な開発環境を整理します。

### FRDM-MCXC444
| 種類 | 対応環境 |
|---|---|
| 公式 IDE | **MCUXpresso IDE** / **MCUXpresso for VS Code** |
| SDK | **MCUXpresso SDK** (FRDM-MCXC444 ボードコンポーネント込み) |
| 商用 IDE | Keil MDK (Arm Compiler 6) / IAR Embedded Workbench for Arm |
| RTOS | FreeRTOS / Zephyr / NuttX / Mbed OS |
| AI | eIQ ライブラリ(CPU 推論、軽量モデル向け) |
| デバッグ | オンボード MCU-Link (CMSIS-DAP) / 外部 J-Link |

### FRDM-MCXN947
| 種類 | 対応環境 |
|---|---|
| 公式 IDE | **MCUXpresso IDE** / **MCUXpresso for VS Code** |
| SDK | **MCUXpresso SDK** + **eIQ Neutron NPU 用ライブラリ** |
| AI ツール | **eIQ Toolkit** (TensorFlow Lite / ONNX → Neutron NPU 最適化) |
| 商用 IDE | Keil MDK / IAR EWARM |
| RTOS | FreeRTOS / Zephyr (デュアルコア対応) / Azure RTOS ThreadX |
| ネットワーク | lwIP (Ethernet) / NXP MCU-Boot / Matter |
| デバッグ | オンボード MCU-Link (CMSIS-DAP) / 外部 J-Link / SEGGER OZONE |

### FRDM-IMX91
| 種類 | 対応環境 |
|---|---|
| 公式 BSP | **NXP Linux BSP** (Yocto Project ベース) |
| ディストリビューション | Yocto Project / Buildroot / Debian/Ubuntu 派生 |
| アプリ開発 | C/C++ (GCC/Clang) / Python / Node.js / Go (任意) |
| 無線スタック | hostapd/wpa_supplicant (Wi-Fi) / BlueZ (BLE) / OpenThread / Matter |
| セキュリティ | EdgeLock 2GO / EdgeLock Secure Enclave SDK |
| RTOS (補助) | Zephyr / FreeRTOS (M コア相当の利用は限定的) |
| デバッグ | UART シリアルコンソール / SSH / GDB(リモート) / oprofile |

### IMXRT1050-EVKB
| 種類 | 対応環境 |
|---|---|
| 公式 IDE | **MCUXpresso IDE** / **MCUXpresso for VS Code** |
| SDK | **MCUXpresso SDK** (IMXRT1050 ボードコンポーネント込み) |
| 商用 IDE | Keil MDK / IAR EWARM |
| RTOS | FreeRTOS / Azure RTOS ThreadX / Zephyr / NuttX / Mbed OS |
| グラフィックス | NXP GUI Guider / emWin / LVGL |
| AI | eIQ + CMSIS-NN / TensorFlow Lite for Microcontrollers |
| デバッグ | オンボード OpenSDA (DAPLink) / 外部 J-Link |

### NXP 共通の便利ツール

- **MCUXpresso Config Tools**: ピンマックス・クロックツリー・周辺機能設定を GUI で生成
- **MCUXpresso Installer**: 各種 SDK / IDE / VSCode 拡張のインストールマネージャ
- **MCU Boot Utility / NXP-MCUBootUtility**: フラッシュ書込み・セキュアブート設定

## 選び方の目安

- **コスト最優先・電池駆動・センサ取り込み中心** → FRDM-MCXC444
- **エッジ AI 推論を MCU 単体で行いたい** → FRDM-MCXN947 (eIQ Neutron NPU)
- **Linux ベースで Wi-Fi 6/BLE/Matter 対応の IoT を作る** → FRDM-IMX91
- **画像処理・モータ制御・グラフィックス UI など演算量重め** → IMXRT1050-EVKB

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。最新の価格・在庫・仕様は各製品の [NXP 公式ページ](https://www.nxp.com/) および [DigiKey](https://www.digikey.jp/) で確認してください。
