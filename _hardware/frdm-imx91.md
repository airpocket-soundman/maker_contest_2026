---
title: FRDM-IMX91 (NXP i.MX 91 アプリケーションプロセッサ評価ボード)
slug: frdm-imx91
tagline: Cortex-A55 1.4GHz + Wi-Fi6/BLE/802.15.4 を搭載した 組込み Linux 向け FRDM ボード
manufacturer: NXP Semiconductors
category: 評価ボード(組込み Linux / 産業 IoT)
official_url: https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-IMX91

features:
  - i.MX 91 アプリケーションプロセッサ (Cortex-A55、最大 1.4GHz) を搭載
  - LPDDR4 + eMMC 5.1 を実装、microSD スロットも装備
  - **Murata Type-2EL** モジュール(Wi-Fi 6 + Bluetooth 5.2 + IEEE 802.15.4)を搭載
  - デュアル RGMII Ethernet (TSN 対応) を装備、産業ネットワーク用途に対応
  - 40 ピン (2×20) 拡張 I/O ヘッダ + 2×5 NXP I/F (CAN, ADC×2, I²C/I³C)
  - **EdgeLock Secure Enclave** 内蔵でセキュアブート/暗号処理/タンパ検出
  - JTAG (20 ピン) + microUSB UART デバッグ I/F、SDP/UUU 経由で SD/eMMC へ書込み可能
  - DigiKey Make ONE Challenge 2026 で「おすすめ製品」として一次審査の加点対象

specs:
  - label: 搭載プロセッサ
    value: NXP i.MX 91 (Arm Cortex-A55、最大 1.4GHz、シングルコア)
  - label: メモリ (FRDM-IMX91)
    value: LPDDR4 1GB / eMMC 5.1 8GB / microSD スロット
  - label: メモリ (FRDM-IMX91S 上位版)
    value: LPDDR4 2GB / eMMC 5.1 16GB / microSD スロット (Zephyr docs ベース)
  - label: 無線
    value: Murata Type-2EL モジュール (Wi-Fi 6 + BLE 5.2 + IEEE 802.15.4 = Thread/Zigbee/Matter)
  - label: 有線通信
    value: デュアル RGMII Ethernet (10/100/1000、TSN 対応) / 2× USB 2.0 Type-C
  - label: 拡張 I/O
    value: 40 ピン (2×20) GPIO 拡張ヘッダ + 2×5 NXP I/F (CAN×1, ADC×2, I²C/I³C 拡張) + M.2/NGFF Key E スロット
  - label: ストレージ
    value: eMMC 5.1 / microSD / USB ストレージ
  - label: セキュリティ
    value: **EdgeLock Secure Enclave** (セキュアブート、暗号処理、タンパ検出) / TrustZone-A
  - label: 電源
    value: USB Type-C (PD 対応)
  - label: 動作 OS
    value: Linux (NXP BSP, Yocto Project ベース) / Zephyr (実験的、Cortex-A 対応)
  - label: ロジックレベル
    value: 3.3V CMOS
  - label: デバッグ
    value: 20 ピン JTAG / microUSB UART コンソール / Serial Download Protocol (UUU)
  - label: 価格目安
    value: ¥13,062 (DigiKey JP)

resources:
  - name: NXP - FRDM-IMX91 製品ページ
    url: https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-IMX91
  - name: NXP - Getting Started with FRDM-IMX91S
    url: https://www.nxp.com/document/guide/getting-started-with-frdm-imx91s:GS-FRDM-IMX91S
    note: 初回起動・SD カード書込み手順の公式ガイド
  - name: ユーザーマニュアル UM12262 (PDF)
    url: https://www.farnell.com/datasheets/4594689.pdf
    note: ピン配置・回路図・周辺仕様
  - name: i.MX FRDM Software User Guide UG10195 (PDF、FRDM-IMX93 用ですが手順は共通)
    url: https://www.mouser.com/pdfDocs/FRDM-IMX93_SW_UM.pdf
  - name: GitHub - nxp-imx-support/meta-imx-frdm (Yocto layer)
    url: https://github.com/nxp-imx-support/meta-imx-frdm
    note: 公式 Yocto BSP レイヤー(FRDM 系ボード共通)
  - name: U-Boot - imx91_frdm ボードドキュメント
    url: https://docs.u-boot.org/en/latest/board/nxp/imx91_11x11_frdm.html
  - name: i.MX FRDM Yocto Software Release Notes RN00265 (PDF)
    url: https://www.nxp.com/docs/en/release-note/RN00265.pdf
  - name: GitHub - NXPmicro/mfgtools (UUU 書込みツール)
    url: https://github.com/NXPmicro/mfgtools/releases
  - name: DigiKey JP - FRDM-IMX91 商品ページ
    url: https://www.digikey.jp/ja/products/detail/nxp-usa-inc/FRDM-IMX91/26236212
  - name: NXP Community - FRDM-IMX91 Series Training
    url: https://community.nxp.com/t5/FRDM-Training-Hub/FRDM-IMX91-Series-Training/ta-p/2056009
  - name: Zephyr Project - FRDM-IMX91 ボードドキュメント
    url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_imx91/doc/index.html
  - name: LinuxGizmos - FRDM-IMX91 紹介記事
    url: https://linuxgizmos.com/nxps-frdm-i-mx-91-board-provides-low-power-solution-for-linux-based-iot-systems/
---

## 概要

FRDM-IMX91 は NXP の組込み Linux 向けエントリ機 i.MX 91 を搭載した低消費電力・低コストの FRDM ボードです。**Cortex-A55** シングルコアながら 1.4GHz 動作、**Wi-Fi 6 / BLE 5.2 / 802.15.4** のトライラジオ、**EdgeLock Secure Enclave** のセキュリティブロック、デュアル Gigabit Ethernet (TSN) までオンボードで揃い、IoT ゲートウェイ・産業端末・スマート家電のリファレンスとして使えます。

DigiKey Make ONE Challenge 2026 では「おすすめ製品」(NXP 4 ボードの 1 つ) として、一次審査の加点対象になります。

> 本ボードは **Linux ベースで動作する Cortex-A 系** であり、他の MCX/RT 系ボード(ベアメタル/RTOS 中心)とは開発フローが大きく異なります。Linux/Yocto/Buildroot に慣れているか、これから学ぶ前提で選択してください。

## ボード ブロック図

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  USB Type-C (J5)  ←── SDP/UUU 書込み兼 USB ホスト/デバイス         │
│  USB Type-C (J6)  ──→ 電源 (PD 対応)                                 │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │                  i.MX 91 (Cortex-A55, 1.4GHz)                 │    │
│  │  EdgeLock Secure Enclave / TrustZone-A                        │    │
│  │  GPU: 2D グラフィックス基本機能 / VPU: 簡易デコード           │    │
│  └──┬──────────────┬───────────────┬─────────────┬───────────────┘    │
│     │              │               │             │                    │
│  LPDDR4 1GB       eMMC 8GB      microSD       USB / Eth / 拡張        │
│  (外付け)         (オンボード)   (スロット)                           │
│                                                                      │
│  Murata Type-2EL モジュール (Wi-Fi 6 + BLE 5.2 + 802.15.4)            │
│  デュアル RGMII Ethernet (10/100/1000, TSN 対応)                     │
│  M.2 / NGFF Key E スロット (Wi-Fi/BT 拡張用)                         │
│  40 ピン GPIO 拡張ヘッダ                                              │
│  2×5 NXP I/F (CAN ×1 / ADC ×2 / I²C / I³C)                            │
│  20 ピン JTAG + microUSB UART デバッグコンソール                      │
└──────────────────────────────────────────────────────────────────────┘
```

> 詳細なブロック図・回路図は [ユーザーマニュアル UM12262](https://www.farnell.com/datasheets/4594689.pdf) を参照。

## 拡張 I/O

| ヘッダ/コネクタ | 用途 |
|---|---|
| 40 ピン GPIO 拡張 (2×20) | GPIO / SPI / I²C / UART / PWM / GPCLK 等(Linux user space からは `/sys/class/gpio` または `libgpiod` 経由で制御) |
| 2×5 NXP I/F | CAN ×1 / ADC ×2 / I²C / I³C 拡張(産業用センサ・モータ駆動向け) |
| M.2 / NGFF Key E | 追加 Wi-Fi/BT モジュール、または Coral Edge TPU など |
| USB Type-C ×2 | J5: SDP 書込み兼ホスト/デバイス兼用 / J6: 電源 (PD 対応) |
| RGMII Ethernet ×2 | 産業向け TSN 用途、デュアルポート (10/100/1000) |
| JTAG (20pin) | フル機能デバッグ |
| microUSB UART | シリアルコンソール(115200 8N1 が標準) |

> Raspberry Pi 互換ピッチではないため、シールド選定時は要注意。Linux 側の Device Tree (`imx91-frdm.dts`) で各 I/O のピンマックスが定義されています。

## 電源系統

| 項目 | 仕様 |
|---|---|
| 主電源 | USB Type-C J6 (PD 対応、5V〜) |
| ロジックレベル | 3.3V CMOS |
| 内部電源 | PMIC 経由で各電源ドメインを生成(Cortex-A、DDR、PHY、各種 1.8V/3.3V) |
| 消費電力傾向 | アクティブ時で数 W 級。Linux ブート時は 1A 級の瞬時電流要 |
| バッテリ駆動 | 簡易バックアップ用 RTC 電源 (CR1220) コネクタあり |

## 開発環境

| 種類 | 対応環境 |
|---|---|
| 標準 BSP | **NXP i.MX Linux BSP** (Yocto Project ベース、`meta-imx-frdm` レイヤー) |
| ディストリ選択 | NXP Yocto / Buildroot / Debian/Ubuntu 派生 (TQ-Group, PHYTEC など) |
| アプリ言語 | C/C++ (GCC/Clang) / Python / Node.js / Go / Rust など任意 |
| 無線スタック | hostapd・wpa_supplicant (Wi-Fi) / BlueZ (BLE) / OpenThread / Matter |
| 機械学習 | **eIQ ライブラリ + ONNX Runtime / TensorFlow Lite / OpenCV (CPU 推論)** |
| セキュリティ | EdgeLock 2GO / EdgeLock Secure Enclave SDK / OPTEE-OS |
| 補助 RTOS | Cortex-A 上で限定的に Zephyr / FreeRTOS の利用は可能(主用途は Linux) |
| デバッグ | UART シリアルコンソール / SSH / リモート GDB / oprofile / perf |
| 書込みツール | **UUU (mfgtools)** / SD カード dd / OpenOCD + JTAG / J-Link |
| エディタ | 任意。Linux ホストでの clangd + VS Code リモート開発が定石 |

> NXP 公式の **MCUXpresso for VS Code** 拡張は MCX / LPC / RT 系の Cortex-M 用で、本ボード(Cortex-A55 + Linux)は対象外です。Linux 開発は通常の VS Code + Remote-SSH や CLion などを使います。

## 開発フロー(初回起動から書込みまで)

```
[1] ホスト PC で Yocto BSP を取得・ビルド
    git clone https://github.com/nxp-imx-support/meta-imx-frdm
    MACHINE=imx91frdm DISTRO=fsl-imx-xwayland \
      source sources/meta-imx-frdm/tools/imx-frdm-setup.sh -b frdm-imx91
    bitbake imx-image-multimedia
        │
        ▼
[2] ビルド成果物 (sdcard.img / flash.bin / Image / dtb / rootfs)
        │
        ▼
[3] FRDM-IMX91 を SDP (Serial Download Protocol) モードに切替
    (起動モードスイッチで設定)
        │
        ▼
[4] ホストから UUU で SD/eMMC に書込み
    uuu -b sd_all flash.bin sdcard.img
        │
        ▼
[5] ボード再起動 → U-Boot → Linux ブート
    シリアルコンソール (115200 8N1) でログ確認
```

> UUU は [NXPmicro/mfgtools リリース](https://github.com/NXPmicro/mfgtools/releases) から最新版(1.5.125 以上)を取得してください。詳細手順は [Getting Started with FRDM-IMX91S](https://www.nxp.com/document/guide/getting-started-with-frdm-imx91s:GS-FRDM-IMX91S) と [UG10195](https://www.mouser.com/pdfDocs/FRDM-IMX93_SW_UM.pdf) を参照。

## AI / 機械学習

i.MX 91 には専用 NPU は搭載されていないため、ML 推論は **Cortex-A55 CPU 上で実行** します。Linux ベースなので利用できる選択肢は豊富です。

- **eIQ ライブラリ** (NXP 公式): TensorFlow Lite / ONNX Runtime / OpenCV / Arm NN / DeepView の各ランタイムを Yocto レシピで提供
- **PyTorch / TensorFlow フル版**: Cortex-A55 + Linux なので CPython 経由で標準モデルもそのまま動く(速度はそれなり)
- **モデルフォーマット**: TFLite / ONNX / Caffe / PyTorch saved model など
- **NPU が必要なら**: 上位機種 [FRDM-IMX93](https://www.nxp.com/) (NPU 搭載) もしくは i.MX 8M Plus を検討

> エッジ側で本格的な NN 推論が必要なら、MCX 系の[FRDM-MCXN947](/maker_contest_2026/hardware/frdm-mcxn947/) の eIQ Neutron NPU の方が消費電力あたりの性能は優れます(用途次第で使い分け)。

## 入手方法

- DigiKey JP: [FRDM-IMX91](https://www.digikey.jp/ja/products/detail/nxp-usa-inc/FRDM-IMX91/26236212) (¥13,062 前後)
- NXP 直販 / Mouser / Arrow Electronics などからも入手可

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。FRDM-IMX91 と FRDM-IMX91S では搭載メモリ容量が異なる可能性があります。実際の購入・開発前に必ず[ユーザーマニュアル UM12262](https://www.farnell.com/datasheets/4594689.pdf) と [NXP 公式ページ](https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-IMX91) で最新の仕様を確認してください。
