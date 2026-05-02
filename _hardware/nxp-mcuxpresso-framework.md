---
title: NXP 推奨 4 ボード 開発エコシステム (MCUXpresso + i.MX Linux BSP)
short_title: NXP 開発エコシステム
slug: nxp-mcuxpresso-framework
tagline: Cortex-M 系 3 ボードは MCUXpresso、Cortex-A 系 FRDM-IMX91 は i.MX Linux BSP (Yocto)。系統別の開発フローと共通の eIQ AI ツールキットを解説
manufacturer: NXP Semiconductors
category: 開発フレームワーク (IDE / SDK / AI Tools / Linux BSP)
official_url: https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-

features:
  - "**Cortex-M 系** (MCXC444 / MCXN947 / IMXRT1050-EVKB) は **MCUXpresso for VS Code** または Eclipse 版 IDE + MCUXpresso SDK で開発"
  - "**Cortex-A 系** (FRDM-IMX91) は **i.MX Linux BSP (Yocto Project)** + UUU 書込みツールで Linux ベース開発(MCUXpresso ではない)"
  - "**eIQ Toolkit** は両系統共通で利用可能(TensorFlow / PyTorch / ONNX → TFLite → INT8 量子化 → MCXN947 用 Neutron NPU 最適化)"
  - Cortex-M 系は Keil MDK / IAR EWARM / SEGGER J-Link / CMSIS-DAP / pyOCD / OpenOCD など汎用 Arm ツールにも対応
  - Cortex-A 系は VS Code Remote-SSH / 任意の Linux 開発ツール(GCC / Clang / Python / Go 等)が利用可
  - DigiKey Make ONE Challenge 2026 の推奨 4 NXP ボードを横断的に解説

specs:
  - label: 統合開発環境 (Eclipse)
    value: MCUXpresso IDE (Eclipse + CDT、Windows / Linux / macOS)
  - label: 統合開発環境 (VS Code)
    value: MCUXpresso for VS Code (Marketplace 拡張、NXP 公式、推奨)
  - label: 対応コア
    value: Arm Cortex-M0+ / M4 / M7 / M33 / M55 / Cortex-A55 など。MCX / LPC / Kinetis / i.MX RT / i.MX (Linux) を網羅
  - label: SDK
    value: MCUXpresso SDK (ボード単位のサンプル + HAL/ドライバ + RTOS ポート + ミドルウェア)
  - label: 設定ツール
    value: MCUXpresso Config Tools (ピンマックス・クロックツリー・周辺機能・DCD などを GUI 設定)
  - label: インストーラ
    value: MCUXpresso Installer (SDK / GNU Arm Toolchain / Zephyr SDK / デバッグソフトを一括導入)
  - label: AI モデル開発
    value: eIQ Toolkit (eIQ ModelTool / eIQ Portal / ONNX2Quant / Neutron Converter / eIQ ライブラリ)
  - label: Linux 向け
    value: NXP i.MX Linux BSP (Yocto Project ベース) + UUU 書込みツール
  - label: 商用 IDE 連携
    value: Keil MDK (Arm Compiler 6) / IAR Embedded Workbench for Arm
  - label: 対応 RTOS
    value: FreeRTOS / Zephyr / Azure RTOS ThreadX / NuttX / Mbed OS
  - label: GUI フレームワーク
    value: NXP GUI Guider / SEGGER emWin / LVGL / TouchGFX (RT 系などディスプレイ持ち向け)
  - label: デバッガ対応
    value: オンボード MCU-Link / OpenSDA / LPC-Link2 (CMSIS-DAP/DAPLink)、外部 SEGGER J-Link / OZONE / PEmicro
  - label: 必須ハードウェア
    value: FRDM 系のいずれか (MCXC444 / MCXN947 / IMX91 / IMXRT1050-EVKB)
  - label: ホスト OS
    value: Windows / Linux / macOS

resources:
  - name: NXP - MCUXpresso ソフトウェアスイート公式トップ
    url: https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-
  - name: NXP - MCUXpresso for VS Code 製品ページ
    url: https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC
  - name: VS Code Marketplace - MCUXpresso for VS Code
    url: https://marketplace.visualstudio.com/items?itemName=NXPSemiconductors.mcuxpresso
  - name: GitHub - nxp-mcuxpresso/vscode-for-mcux
    url: https://github.com/nxp-mcuxpresso/vscode-for-mcux
  - name: NXP - MCUXpresso SDK ビルダー
    url: https://mcuxpresso.nxp.com/
    note: ボード/MCU を選んで SDK を作成・ダウンロード
  - name: NXP - eIQ ML Development Environment
    url: https://www.nxp.com/design/design-center/software/eiq-ml-development-environment
  - name: NXP - eIQ Toolkit (エンドツーエンドモデル開発)
    url: https://www.nxp.com/design/design-center/software/eiq-ml-development-environment/eiq-toolkit-for-end-to-end-model-development-and-deployment:EIQ-TOOLKIT
  - name: eIQ Toolkit User Guide (EIQTUG, PDF)
    url: https://www.nxp.com/docs/en/user-guide/EIQTKUG-1.6.9.pdf
  - name: GitHub - NXP/eiq-onnx2tflite
    url: https://github.com/NXP/eiq-onnx2tflite
    note: ONNX → TFLite 変換 CLI(オープンソース)
  - name: NXP Community - eIQ Neutron NPU Lab Guides (MCX N 用)
    url: https://community.nxp.com/t5/MCX-Microcontrollers-Knowledge/eIQ-Neutron-NPU-Lab-Guides/ta-p/1799233
  - name: NXP - i.MX Linux BSP / Yocto
    url: https://www.nxp.com/design/design-center/software/embedded-software/i-mx-software/embedded-linux-for-i-mx-applications-processors:IMXLINUX
  - name: GitHub - nxp-imx-support/meta-imx-frdm
    url: https://github.com/nxp-imx-support/meta-imx-frdm
    note: FRDM-IMX91 など i.MX FRDM ボード用 Yocto レイヤー
  - name: GitHub - NXPmicro/mfgtools (UUU 書込みツール)
    url: https://github.com/NXPmicro/mfgtools/releases
  - name: NXP Community - FRDM Training Hub
    url: https://community.nxp.com/t5/FRDM-Training-Hub/ct-p/FRDM-Hub
---

## 概要

DigiKey Make ONE Challenge 2026 の推奨 NXP 4 ボードは、コアアーキテクチャの違いにより **開発フローが 2 系統に分かれます**。

| 系統 | 対象ボード | 主な開発環境 | 動作 OS |
|---|---|---|---|
| **Cortex-M 系**(MCU) | FRDM-MCXC444 / FRDM-MCXN947 / IMXRT1050-EVKB | **MCUXpresso for VS Code** + MCUXpresso SDK / eIQ Toolkit | ベアメタル / RTOS (FreeRTOS, Zephyr, ThreadX 等) |
| **Cortex-A 系**(MPU) | **FRDM-IMX91** | **i.MX Linux BSP (Yocto Project)** + UUU 書込み + 汎用 Linux 開発ツール | Linux (Yocto / Buildroot / Debian 派生) |

> **重要**: FRDM-IMX91 は **MCUXpresso では開発しません**。Cortex-A55 上で Linux を動かす Linux ベースの開発フローになります。Cortex-M 用の SDK・IDE・サンプルは適用できないので、選定時に注意してください。

両系統に共通するのは:
- **eIQ Toolkit**(AI モデル開発): どちらでも利用可。Cortex-M 系では NPU 用 / CMSIS-NN / TFLM、Cortex-A 系では eIQ ランタイム(ONNX Runtime / TFLite / OpenCV 等)
- **NXP オンライン資料・コミュニティ**: ドキュメント / FAQ / Lab Guide

ROHM Solist-AI™ が LEXIDE-Ω と専用ツール群で完結する [独自フレームワーク](/maker_contest_2026/hardware/solist-ai-dev-framework/) なのに対し、NXP は **VS Code 拡張・OSS 互換性・Yocto 連携** などオープンエコシステムに寄った設計が特徴です。

## ツール構成

<svg class="board-diagram" viewBox="0 0 860 760" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="NXP 4 ボード 開発エコシステム 系統別構成図">
  <defs>
    <marker id="arrow-nxp" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#4b5563"/>
    </marker>
  </defs>
  <!-- Host PC 大枠 -->
  <rect x="10" y="10" width="840" height="500" rx="8" fill="#f9fafb" stroke="#d1d5db" stroke-dasharray="4 4"/>
  <text class="label label-bold" x="430" y="32" text-anchor="middle" font-size="14">Host PC (Windows / Linux / macOS)</text>
  <!-- 左カラム: Cortex-M 系 -->
  <rect x="25" y="50" width="395" height="450" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
  <text class="label label-bold" x="222" y="72" text-anchor="middle" font-size="13" fill="#1e40af">Cortex-M 系 (MCU): MCUXpresso 系統</text>
  <text class="label label-small" x="222" y="88" text-anchor="middle">FRDM-MCXC444 / FRDM-MCXN947 / IMXRT1050-EVKB</text>
  <rect class="box" x="40" y="105" width="365" height="55" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text class="label label-bold" x="222" y="125" text-anchor="middle">MCUXpresso for VS Code</text>
  <text class="label label-small" x="222" y="141" text-anchor="middle">Marketplace 拡張 / NXP 公式推奨</text>
  <text class="label label-small" x="222" y="155" text-anchor="middle">代替: MCUXpresso IDE (Eclipse 版)</text>
  <rect class="box box-mem" x="40" y="170" width="365" height="50" rx="4"/>
  <text class="label label-bold" x="222" y="190" text-anchor="middle">MCUXpresso SDK + Config Tools</text>
  <text class="label label-small" x="222" y="206" text-anchor="middle">HAL / ドライバ / サンプル(数百種) / Installer</text>
  <rect class="box" x="40" y="230" width="365" height="50" rx="4" fill="#fef3c7" stroke="#d97706"/>
  <text class="label label-bold" x="222" y="250" text-anchor="middle">対応 RTOS / GUI</text>
  <text class="label label-small" x="222" y="266" text-anchor="middle">FreeRTOS / Zephyr / ThreadX / NuttX / Mbed / LVGL / GUI Guider</text>
  <rect class="box box-io" x="40" y="290" width="365" height="50" rx="4"/>
  <text class="label label-bold" x="222" y="310" text-anchor="middle">商用 / 互換ツール</text>
  <text class="label label-small" x="222" y="326" text-anchor="middle">Keil MDK / IAR / J-Link / pyOCD / OpenOCD / CMSIS-DAP</text>
  <rect class="box" x="40" y="350" width="365" height="50" rx="4" fill="#fce7f3" stroke="#9f1239"/>
  <text class="label label-bold" x="222" y="370" text-anchor="middle">デバッガ</text>
  <text class="label label-small" x="222" y="386" text-anchor="middle">オンボード MCU-Link / OpenSDA / LPC-Link2 / 外部 J-Link</text>
  <text class="label label-small" x="222" y="412" text-anchor="middle" font-style="italic">→ Flash 書込み・ステップ実行・周辺レジスタビュー</text>
  <text class="label label-small" x="222" y="438" text-anchor="middle">アプリ言語: C/C++ (一部 MicroPython)</text>
  <text class="label label-small" x="222" y="458" text-anchor="middle">配置: ベアメタル / RTOS</text>
  <text class="label label-small" x="222" y="478" text-anchor="middle">CMSIS-NN / TFLite Micro による軽量 ML 推論</text>
  <!-- 右カラム: Cortex-A 系 -->
  <rect x="440" y="50" width="395" height="450" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text class="label label-bold" x="637" y="72" text-anchor="middle" font-size="13" fill="#92400e">Cortex-A 系 (MPU): Linux BSP 系統</text>
  <text class="label label-small" x="637" y="88" text-anchor="middle">FRDM-IMX91 のみ(MCUXpresso 不適用)</text>
  <rect class="box" x="455" y="105" width="365" height="55" rx="4" fill="#fed7aa" stroke="#d97706" stroke-width="2"/>
  <text class="label label-bold" x="637" y="125" text-anchor="middle">i.MX Linux BSP (Yocto Project)</text>
  <text class="label label-small" x="637" y="141" text-anchor="middle">meta-imx-frdm レイヤー / bitbake</text>
  <text class="label label-small" x="637" y="155" text-anchor="middle">UUU (mfgtools) で SD/eMMC へ書込み</text>
  <rect class="box box-mem" x="455" y="170" width="365" height="50" rx="4"/>
  <text class="label label-bold" x="637" y="190" text-anchor="middle">ディストリ選択肢</text>
  <text class="label label-small" x="637" y="206" text-anchor="middle">Yocto / Buildroot / Debian/Ubuntu 派生</text>
  <rect class="box box-io" x="455" y="230" width="365" height="50" rx="4"/>
  <text class="label label-bold" x="637" y="250" text-anchor="middle">アプリ開発環境</text>
  <text class="label label-small" x="637" y="266" text-anchor="middle">VS Code Remote-SSH / CLion / 任意の Linux IDE</text>
  <rect class="box" x="455" y="290" width="365" height="50" rx="4" fill="#dcfce7" stroke="#059669"/>
  <text class="label label-bold" x="637" y="310" text-anchor="middle">アプリ言語</text>
  <text class="label label-small" x="637" y="326" text-anchor="middle">C / C++ / Python / Node.js / Go / Rust 等</text>
  <rect class="box" x="455" y="350" width="365" height="50" rx="4" fill="#fce7f3" stroke="#9f1239"/>
  <text class="label label-bold" x="637" y="370" text-anchor="middle">デバッグ / 接続</text>
  <text class="label label-small" x="637" y="386" text-anchor="middle">UART シリアル / SSH / リモート GDB / perf / oprofile</text>
  <text class="label label-small" x="637" y="412" text-anchor="middle" font-style="italic">→ ホスト PC でクロスコンパイル → 実機転送</text>
  <text class="label label-small" x="637" y="438" text-anchor="middle">配置: Linux ユーザ空間プロセス</text>
  <text class="label label-small" x="637" y="458" text-anchor="middle">eIQ ランタイム / ONNX Runtime / TFLite / OpenCV</text>
  <text class="label label-small" x="637" y="478" text-anchor="middle">で CPU 推論</text>
  <!-- AI 共通 (両系統にまたがる) -->
  <rect class="box box-ai" x="155" y="525" width="550" height="55" rx="6" stroke-width="2"/>
  <text class="label label-bold" x="430" y="547" text-anchor="middle">eIQ Toolkit (両系統で利用可)</text>
  <text class="label label-small" x="430" y="563" text-anchor="middle">eIQ Portal / ModelTool / ONNX2Quant / eiq-onnx2tflite (OSS) / Neutron Converter</text>
  <text class="label label-small" x="430" y="577" text-anchor="middle">→ Cortex-M ではビルドに組込み、Linux ではランタイム経由で実行</text>
  <!-- ターゲット 4 ボード -->
  <rect x="10" y="600" width="840" height="155" rx="8" fill="#f9fafb" stroke="#d1d5db" stroke-dasharray="4 4"/>
  <text class="label label-bold" x="430" y="622" text-anchor="middle" font-size="14">ターゲットボード (DigiKey Make ONE Challenge 2026 推奨)</text>
  <rect class="box box-mcu" x="25" y="635" width="195" height="105" rx="4"/>
  <text class="label label-bold" x="122" y="657" text-anchor="middle">FRDM-MCXC444</text>
  <text class="label label-small" x="122" y="673" text-anchor="middle">Cortex-M0+ 48MHz</text>
  <text class="label label-small" x="122" y="689" text-anchor="middle" fill="#1e40af" font-weight="bold">MCUXpresso 系統</text>
  <text class="label label-small" x="122" y="705" text-anchor="middle" fill="#dc2626">NPU なし</text>
  <text class="label label-small" x="122" y="725" text-anchor="middle">¥1,750</text>
  <rect class="box box-mcu" x="225" y="635" width="195" height="105" rx="4" stroke="#d97706" stroke-width="2"/>
  <text class="label label-bold" x="322" y="657" text-anchor="middle">FRDM-MCXN947</text>
  <text class="label label-small" x="322" y="673" text-anchor="middle">デュアル M33 150MHz</text>
  <text class="label label-small" x="322" y="689" text-anchor="middle" fill="#1e40af" font-weight="bold">MCUXpresso 系統</text>
  <text class="label label-small" x="322" y="705" text-anchor="middle" fill="#d97706" font-weight="bold">eIQ Neutron NPU</text>
  <text class="label label-small" x="322" y="725" text-anchor="middle">¥4,354</text>
  <rect class="box box-mcu" x="425" y="635" width="195" height="105" rx="4" stroke="#92400e" stroke-width="2"/>
  <text class="label label-bold" x="522" y="657" text-anchor="middle">FRDM-IMX91</text>
  <text class="label label-small" x="522" y="673" text-anchor="middle">Cortex-A55 1.4GHz</text>
  <text class="label label-small" x="522" y="689" text-anchor="middle" fill="#92400e" font-weight="bold">Linux BSP 系統</text>
  <text class="label label-small" x="522" y="705" text-anchor="middle">CPU 推論 (eIQ)</text>
  <text class="label label-small" x="522" y="725" text-anchor="middle">¥13,062</text>
  <rect class="box box-mcu" x="625" y="635" width="195" height="105" rx="4"/>
  <text class="label label-bold" x="722" y="657" text-anchor="middle">IMXRT1050-EVKB</text>
  <text class="label label-small" x="722" y="673" text-anchor="middle">Cortex-M7 600MHz</text>
  <text class="label label-small" x="722" y="689" text-anchor="middle" fill="#1e40af" font-weight="bold">MCUXpresso 系統</text>
  <text class="label label-small" x="722" y="705" text-anchor="middle">XIP / GUI Guider</text>
  <text class="label label-small" x="722" y="725" text-anchor="middle">¥18,572</text>
  <!-- Arrows from systems to boards -->
  <path d="M 222 500 L 122 635" stroke="#2563eb" stroke-width="1.5" fill="none" marker-end="url(#arrow-nxp)"/>
  <path d="M 222 500 L 322 635" stroke="#2563eb" stroke-width="1.5" fill="none" marker-end="url(#arrow-nxp)"/>
  <path d="M 222 500 L 722 635" stroke="#2563eb" stroke-width="1.5" fill="none" marker-end="url(#arrow-nxp)"/>
  <path d="M 637 500 L 522 635" stroke="#d97706" stroke-width="2" fill="none" marker-end="url(#arrow-nxp)"/>
</svg>

## 各ツールの役割

### MCUXpresso for VS Code (NXP 公式 推奨)
- **配布元**: [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=NXPSemiconductors.mcuxpresso) / [GitHub: nxp-mcuxpresso/vscode-for-mcux](https://github.com/nxp-mcuxpresso/vscode-for-mcux)
- VS Code 上で **プロジェクト管理 / ビルド / デバッグ / 周辺レジスタビュー / RTOS スレッド表示** が完結
- 起動時の **Quickstart Panel** から SDK インポート・サンプル選択・デバッグ実行まで導線が一本化
- 対応 MCU: MCX / LPC / Kinetis / i.MX RT 全般
- プロジェクト形態: **MCUXpresso SDK** / **Zephyr** / **Matter** いずれも開ける
- デバッガ: NXP MCU-Link / OpenSDA / LPC-Link2、外部の SEGGER J-Link / OZONE / PEmicro
- 依存自動インストール: C/C++ 拡張 / CMake Tools / 必要に応じて Toolchain も MCUXpresso Installer 経由で導入

### MCUXpresso IDE (Eclipse 版)
- 従来からある Eclipse + CDT ベースの NXP 公式 IDE
- VS Code 版に置き換わりつつあるが、依然サポート継続中
- **どちらを選ぶか**: 既存資産が Eclipse プロジェクトなら IDE、新規プロジェクトなら VS Code 版が無難

### MCUXpresso SDK
- ボード単位で **HAL / ドライバ / RTOS ポート / ミドルウェア / 周辺サンプル** を提供
- 取得方法: [SDK ビルダー](https://mcuxpresso.nxp.com/) でボード/MCU を指定して生成、または IDE 内 Quickstart からインポート
- 例: `evkbimxrt1050_*`, `frdmmcxn947_*`, `frdmmcxc444_*` のサンプルに数百種類

### MCUXpresso Config Tools
- ピンマックス・クロックツリー・周辺機能・電源モード・DCD (i.MX RT 用 SDRAM 初期化) を **GUI 設定**
- 設定結果は C ヘッダ・ソースとして自動生成

### MCUXpresso Installer
- SDK / GNU Arm Toolchain / Zephyr SDK / デバッグソフト / J-Link Software などを 1 つのインストーラで一括導入
- VS Code 版から拡張パネル経由で起動できる

### eIQ Toolkit (AI モデル開発統合環境)
NXP の MCU/MPU 全般で AI 推論を行うための **エンドツーエンドツールキット**。

| サブツール | 役割 |
|---|---|
| **eIQ Portal** | Web ベース GUI。データ取り込み・モデル選択・学習・量子化・デプロイまで GUI で一気通貫 |
| **eIQ ModelTool** | TensorFlow / Keras / PyTorch / ONNX を **TensorFlow Lite (.tflite)** に変換 |
| **ONNX2Quant** | ONNX を QDQ 量子化(per-tensor / per-channel、INT8 アクティベーション) |
| **eiq-onnx2tflite** | ONNX → TFLite 変換 CLI ([GitHub OSS](https://github.com/NXP/eiq-onnx2tflite)) |
| **Neutron Converter** | 量子化済み TFLite を **eIQ Neutron NPU 用** に再最適化(MCXN947 で 4.8 GOPS @ INT8) |
| **eIQ ライブラリ** | TFLite / ONNX Runtime / Arm NN / OpenCV / DeepView などのランタイム集 |

> NPU 活用時の具体手順は [FRDM-MCXN947 詳細ページの「ONNX モデルの変換手順」](/maker_contest_2026/hardware/frdm-mcxn947/) を参照。

### NXP i.MX Linux BSP (Yocto Project)
- **FRDM-IMX91 専用** の組込み Linux 開発環境
- 主要レイヤー: [`meta-imx-frdm`](https://github.com/nxp-imx-support/meta-imx-frdm) (Yocto)
- ビルド: `MACHINE=imx91frdm DISTRO=fsl-imx-xwayland source ... ; bitbake imx-image-multimedia`
- 書込み: **UUU (mfgtools)** で SDP モードのボードに `flash.bin` / `sdcard.img` を流し込み
- アプリ言語は任意(C/C++ / Python / Node.js / Go / Rust)。Linux 上で eIQ ランタイムも利用可能

### 互換ツールチェーン
NXP 公式以外にも以下が使えます。

- **コンパイラ**: Arm GCC (GNU Arm Embedded) / Arm Compiler 6 (Keil MDK)
- **商用 IDE**: Keil MDK / IAR Embedded Workbench for Arm
- **デバッガ**: SEGGER J-Link PLUS / OZONE / Strawberry Linux ARM-JTAG-20-10 / CMSIS-DAP / DAPLink / PEmicro
- **書込み**: pyOCD / OpenOCD (CMSIS-DAP 経由)、Linux 機なら UUU
- **CMSIS パック**: NXP 提供の SVD / CMSIS Device ヘッダを利用

## 典型的な開発フロー

### Cortex-M 系 (MCXC444 / MCXN947 / IMXRT1050-EVKB)

1. **VS Code に拡張インストール** → Quickstart Panel から SDK / サンプルをインポート
2. **Config Tools でピン・クロック設定** → ヘッダ自動生成
3. **MCUXpresso SDK のサンプル** をベースにアプリ実装
4. **MCU-Link / OpenSDA / LPC-Link2** でビルド成果物を Flash 書込み
5. **デバッグ**(ブレークポイント / 周辺レジスタビュー / RTOS スレッド)
6. **AI を使う場合**: eIQ Toolkit でモデル変換 → SDK の eIQ サンプルに統合 → 実機推論
7. **GUI を使う場合 (RT1050 等)**: NXP GUI Guider で UI 設計 → LVGL コードとして出力

### Cortex-A 系 (FRDM-IMX91)

1. **Yocto BSP 取得**: `meta-imx-frdm` クローン + `imx-frdm-setup.sh -b frdm-imx91`
2. **bitbake でイメージビルド**: `bitbake imx-image-multimedia`
3. **ボードを SDP モード**に切替 → ホストから **UUU で書込み**
4. **シリアルコンソール (115200 8N1)** で U-Boot → Linux ブートを確認
5. アプリは **VS Code Remote-SSH** や CLion でリモート開発、ML は eIQ ライブラリ経由 で CPU 推論

## 4 ボードと使うべきツールの早見表

| ボード | コア | 系統 | コンパイラ・IDE | AI 開発 |
|---|---|---|---|---|
| FRDM-MCXC444 | Cortex-M0+ | **MCUXpresso** | MCUXpresso for VS Code + SDK | CMSIS-NN / TFLM (CPU、軽量モデルのみ) |
| FRDM-MCXN947 | デュアル M33 + DSP | **MCUXpresso** | MCUXpresso for VS Code + SDK | **eIQ Toolkit + Neutron Converter** (NPU 専用) |
| **FRDM-IMX91** | Cortex-A55 | **i.MX Linux BSP** ⚠️ | NXP Linux BSP (Yocto) + UUU + 任意の Linux 開発ツール | eIQ ランタイム / ONNX Runtime / TFLite (Linux 上の CPU 推論) |
| IMXRT1050-EVKB | Cortex-M7 | **MCUXpresso** | MCUXpresso for VS Code + SDK | CMSIS-NN / TFLM / eIQ Toolkit (CPU、中型モデル可) |

> ⚠️ FRDM-IMX91 だけ系統が異なります。MCUXpresso 系統のサンプル / SDK / Config Tools は適用できません。Yocto / Linux ベースの開発が必須です。

## ライセンス・入手

- **MCUXpresso IDE / VS Code 拡張 / SDK / Config Tools / Installer**: [NXP 公式](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-) から無償ダウンロード(NXP アカウント要)
- **eIQ Toolkit / Portal / ModelTool / Neutron Converter**: 無償([eIQ ML 環境](https://www.nxp.com/design/design-center/software/eiq-ml-development-environment))
- **eiq-onnx2tflite**: BSD ライセンスの OSS ([GitHub](https://github.com/NXP/eiq-onnx2tflite))
- **i.MX Linux BSP / meta-imx-frdm**: NXP の Yocto レイヤー([GitHub](https://github.com/nxp-imx-support/meta-imx-frdm))。ライセンスはレシピごとに準拠
- **UUU (mfgtools)**: BSD ライセンスの OSS ([GitHub](https://github.com/NXPmicro/mfgtools/releases))
- **商用 IDE (Keil MDK / IAR EWARM)**: 有償(評価版あり)

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。各ツールの最新版・対応 OS・ライセンス条件は必ず[NXP 公式の MCUXpresso ページ](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-) で確認してください。
