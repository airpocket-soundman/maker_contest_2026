---
title: FRDM-MCXN947 (NXP MCX N947 + eIQ Neutron NPU 評価ボード)
slug: frdm-mcxn947
tagline: デュアル Cortex-M33 150MHz + eIQ Neutron NPU(4.8 GOPS, INT8) を搭載した エッジAI/産業IoT 向け Freedom ボード
manufacturer: NXP Semiconductors
category: 評価ボード(エッジAI / 産業 IoT)
official_url: https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-MCXN947

features:
  - MCX N シリーズの旗艦 MCU "MCXN947" を搭載した Freedom フォームファクタ評価ボード
  - **デュアル Arm Cortex-M33** 150MHz × 2 + DSP コプロセッサ + **eIQ Neutron NPU** 内蔵
  - eIQ Neutron NPU は INT8 で 4.8 GOPS、CNN/RNN/TCN/Transformer に対応(CPU 比 最大 42 倍高速)
  - Flash 2MB (デュアルバンク)、フル ECC SRAM 最大 512KB、外付け QSPI Flash 拡張可
  - High-Speed USB Type-C / 10/100 Ethernet (QoS) / 2× FlexCAN-FD / 2× I3C / 2× SAI など豊富な I/F
  - Arduino R3 / mikroBUS (J5/J6) / Pmod (J9) / FlexIO LCD ヘッダ / SmartDMA カメラヘッダ
  - **EdgeLock Secure Subsystem**(セキュアブート・暗号アクセラ・鍵管理)を搭載
  - オンボード MCU-Link デバッガ(LPC55S69 ベース、CMSIS-DAP 準拠)
  - DigiKey Make ONE Challenge 2026 で「おすすめ製品」として一次審査の加点対象

specs:
  - label: 搭載 MCU
    value: NXP MCXN947 (デュアル Arm Cortex-M33 最大 150MHz + DSP + eIQ Neutron NPU)
  - label: 内蔵メモリ
    value: Flash 2MB(デュアルバンク、16KB キャッシュ付き) / SRAM 最大 512KB(うち 416KB はフル ECC)
  - label: 外部メモリ
    value: 外付け Quad SPI Flash (FlexSPI 経由) 拡張可
  - label: AI アクセラレータ
    value: **eIQ Neutron NPU** (4.8 GOPS @ 150MHz, INT8 のみ、CNN/RNN/TCN/Transformer 対応)
  - label: 通信ペリフェラル
    value: 10× LP Flexcomm(SPI/I²C/UART) / High-Speed USB Type-C / 10/100 Ethernet (QoS) / 2× FlexCAN-FD / 2× I3C / 2× SAI
  - label: 周辺機能
    value: SmartDMA / 16bit ADC / DAC / アナログコンパレータ / 操作アンプ / FlexPWM / 32bit タイマ
  - label: セキュリティ
    value: EdgeLock Secure Subsystem / TrustZone-M / 暗号化アクセラレータ
  - label: 拡張ヘッダ
    value: Arduino R3 互換 / mikroBUS J5・J6 / Pmod J9 / FlexIO LCD ヘッダ / SmartDMA カメラヘッダ
  - label: デバッガ
    value: オンボード MCU-Link OB (LPC55S69 ベース、CMSIS-DAP 対応) / 外部 SWD 接続可
  - label: 電源
    value: USB Type-C 5V (P5V_MCU_LINK_USB / P5V_USB_HS / P5V_HDR_IN のいずれかから給電可)
  - label: ロジックレベル
    value: 3.3V / 1.8V (周辺バンクごとに切替可)
  - label: 動作 OS
    value: ベアメタル / FreeRTOS / Zephyr / Azure RTOS ThreadX / Mbed OS など
  - label: 価格目安
    value: ¥4,354 (DigiKey JP)

resources:
  - name: NXP - FRDM-MCXN947 製品ページ
    url: https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-MCXN947
  - name: ユーザーマニュアル UM12018 (FRDM-MCXN947 Board User Manual)
    url: https://manuals.plus/m/850e3d758fe83d78fac300a4fadd334e6f7dbbebaa816473275db57080cfa8f9.pdf
    note: ピン配置・回路図・ジャンパ・電源・mikroBUS J5/J6 / Pmod J9 のピンアサインなど詳細
  - name: DigiKey JP - FRDM-MCXN947 商品ページ
    url: https://www.digikey.jp/ja/products/detail/nxp-usa-inc/FRDM-MCXN947/22036137
  - name: NXP - MCUXpresso for VS Code (拡張機能)
    url: https://marketplace.visualstudio.com/items?itemName=NXPSemiconductors.mcuxpresso
    note: VS Code から MCXN947 を完全サポート(ビルド・デバッグ・周辺レジスタ表示)
  - name: NXP - eIQ Toolkit (AI モデル変換・量子化ツール)
    url: https://www.nxp.com/design/design-center/software/eiq-ml-development-environment/eiq-toolkit-for-end-to-end-model-development-and-deployment:EIQ-TOOLKIT
  - name: eIQ Toolkit User Guide (EIQTUG, PDF)
    url: https://www.nxp.com/docs/en/user-guide/EIQTKUG-1.6.9.pdf
  - name: NXP Community - eIQ Neutron NPU Lab Guides (MCX N 用)
    url: https://community.nxp.com/t5/MCX-Microcontrollers-Knowledge/eIQ-Neutron-NPU-Lab-Guides/ta-p/1799233
    note: VS Code 版 / MCUXpresso IDE 版の Lab Guide(PDF 付属)
  - name: NXP Community - MCXN947 で独自 ML モデルを学習・展開する手順
    url: https://community.nxp.com/t5/MCX-Microcontrollers-Knowledge/MCXN947-How-to-Train-and-Deploy-Customer-ML-model-to-NPU/ta-p/1899497
  - name: GitHub - NXP/eiq-onnx2tflite (ONNX → TFLite 変換 CLI)
    url: https://github.com/NXP/eiq-onnx2tflite
  - name: NXP MCUXpresso for VS Code - 公式 GitHub
    url: https://github.com/nxp-mcuxpresso/vscode-for-mcux
  - name: Zephyr Project - FRDM-MCXN947 ボードドキュメント
    url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html
  - name: NXP Community - FRDM-MCXN Knowledge Hub
    url: https://community.nxp.com/t5/FRDM-Training-Hub/FRDM-MCXN-Knowledge-Hub/ta-p/2199187
  - name: arXiv - eIQ Neutron アーキテクチャ論文
    url: https://arxiv.org/abs/2509.14388
    note: NPU 内部構造とコンパイラ最適化の技術詳細
---

## 概要

FRDM-MCXN947 は NXP MCX N シリーズの中核ボードで、**デュアル Cortex-M33 + DSP + eIQ Neutron NPU** という構成により、産業 IoT・AI 推論・モータ制御を 1 チップでこなせる高性能 MCU を試せます。**eIQ Neutron NPU は INT8 で 4.8 GOPS** の演算能力を持ち、外部 AI アクセラレータなしでも畳み込み・MLP・小型 Transformer の推論をオンデバイスで実行できます。

DigiKey Make ONE Challenge 2026 では「おすすめ製品」(NXP 4 ボードの 1 つ) として、一次審査の加点対象になります。

## ボード ブロック図

```
┌────────────────────────────────────────────────────────────────────────┐
│  USB Type-C (CN_HS) ─ High-Speed USB                                   │
│  USB Type-C (CN_DEBUG) ─ MCU-Link OB (LPC55S69, CMSIS-DAP)             │
│                                                                        │
│       電源:  P5V_MCU_LINK_USB / P5V_USB_HS / P5V_HDR_IN                 │
│              → 内部 LDO/SMPS で 3.3V / 1.8V を生成                      │
│                                                                        │
│   ┌─────────────────────────────────────────────────────────────────┐  │
│   │              MCXN947 (デュアル Cortex-M33, 150MHz)              │  │
│   │  CPU0  ──────────────┬──────────────┐                           │  │
│   │  CPU1  ──────────────┤              │                           │  │
│   │                      ▼              ▼                           │  │
│   │   ┌──────────────────────┐  ┌────────────────┐                  │  │
│   │   │ eIQ Neutron NPU       │  │ DSP Coprocessor│                  │  │
│   │   │ 4.8 GOPS @ 150MHz     │  │ (FFT/FIR等)    │                  │  │
│   │   │ INT8、CNN/RNN/TCN/    │  └────────────────┘                  │  │
│   │   │ Transformer 対応       │                                     │  │
│   │   └──────────────────────┘                                     │  │
│   │                                                                 │  │
│   │   Flash 2MB (dual-bank, 16KB cache)                              │  │
│   │   SRAM 512KB (416KB ECC) ── SmartDMA ── FlexIO ── FlexSPI        │  │
│   │                                                                 │  │
│   │   10× LP Flexcomm (SPI/I²C/UART) | 2× FlexCAN-FD | 2× I3C | 2× SAI │
│   │   Ethernet (QoS) | USB-HS | 16bit ADC | DAC | OpAmp | Comparator │  │
│   │   EdgeLock Secure Subsystem (TrustZone-M, 暗号アクセラ)          │  │
│   └──┬──────────┬──────────┬──────────┬──────────┬───────────────┬──┘  │
│      │          │          │          │          │               │     │
│      ▼          ▼          ▼          ▼          ▼               ▼     │
│  Arduino R3  mikroBUS J5  mikroBUS J6  Pmod J9   FlexIO LCD  SmartDMA  │
│                                                              Camera    │
│                                                                        │
│   ユーザボタン×2 / RGB LED / SW1 リセット                              │
└────────────────────────────────────────────────────────────────────────┘
```

> 詳細なブロック図・回路図は [ユーザーマニュアル UM12018](https://manuals.plus/m/850e3d758fe83d78fac300a4fadd334e6f7dbbebaa816473275db57080cfa8f9.pdf) を参照。

## 主要 GPIO / ヘッダ

ボードには以下の拡張ヘッダがあり、それぞれ MCU の異なる GPIO バンクに接続されています。

| ヘッダ | 主な用途 |
|---|---|
| Arduino R3 互換ヘッダ | GPIO / SPI / I²C / UART / ADC / PWM (UNO シールド対応) |
| mikroBUS **J5** | mikroE Click ボード接続(SPI/I²C/UART/ADC/PWM/INT/RST) |
| mikroBUS **J6** | 同上(2 枚目の Click ボードを並列接続可) |
| Pmod **J9** | Digilent Pmod モジュール接続 |
| FlexIO LCD ヘッダ | パラレル LCD 直接駆動(FlexIO 機能) |
| SmartDMA カメラヘッダ | パラレル/シリアルカメラ接続(SmartDMA 経由) |

> **正確な GPIO 番号は必ず [UM12018](https://manuals.plus/m/850e3d758fe83d78fac300a4fadd334e6f7dbbebaa816473275db57080cfa8f9.pdf) §「Connectors」と Zephyr の board overlay (`frdm_mcxn947.dts`) を併用して確認してください。** デュアルコア構成のためターゲットを `cpu0` / `cpu0/ns` (Non-Secure) / `cpu1` / `cpu0/qspi` から選択する必要があります。

## 電源系統

| 項目 | 仕様 |
|---|---|
| 給電源 | USB Type-C いずれか: **P5V_MCU_LINK_USB**(MCU-Link 側 USB-C) / **P5V_USB_HS**(High-Speed USB-C) / **P5V_HDR_IN**(ヘッダ供給) |
| 内部レギュレータ | LDO / SMPS で 3.3V および 1.8V を生成 |
| MCU 動作電圧 | 1.71〜3.6V (本ボードでは 3.3V) |
| ロジックレベル | 周辺バンクで **3.3V / 1.8V を選択可** (UM12018 §Power 参照) |
| デバッガ給電 | MCU-Link OB は USB バス電源で動作。CMSIS-DAP からターゲット給電も可 |
| ヘッダ給電 | Arduino / mikroBUS / Pmod の 5V/3.3V 端子から給電も可(ジャンパ要) |

## 開発環境

| 種類 | 対応環境 |
|---|---|
| 公式 IDE (Eclipse) | **MCUXpresso IDE** (Eclipse + CDT、Windows/Linux/macOS) |
| 公式 IDE (VS Code) | **MCUXpresso for VS Code** ([Marketplace](https://marketplace.visualstudio.com/items?itemName=NXPSemiconductors.mcuxpresso))。MCXN947 に完全対応 |
| SDK | **MCUXpresso SDK** + **eIQ Neutron NPU 用ライブラリ** |
| AI ツール | **eIQ Toolkit** (TensorFlow Lite / ONNX → Neutron NPU 用に最適化) |
| 設定ツール | MCUXpresso Config Tools (ピンマックス・クロックツリー・周辺) |
| インストーラ | MCUXpresso Installer (SDK / Toolchain / Zephyr SDK / Debug ソフトを統合) |
| 商用 IDE | Keil MDK / IAR EWARM |
| RTOS | FreeRTOS / Zephyr (デュアルコア対応) / Azure RTOS ThreadX |
| ネットワーク | lwIP (Ethernet) / NXP MCU-Boot / Matter |
| デバッグ | オンボード MCU-Link (CMSIS-DAP) / 外部 J-Link / SEGGER OZONE。NXP / PEmicro / SEGGER の各種プローブ対応 |

### MCUXpresso for VS Code (補足)

NXP は VS Code 拡張版を主力に推進しており、MCXN947 の開発も Eclipse 版とほぼ同等の体験で可能です。

- **インストール**: VS Code 拡張機能 `NXPSemiconductors.mcuxpresso` を入れる(C/C++ 拡張は自動同梱)
- **対応 MCU**: MCX 全般 / LPC / Kinetis / i.MX RT
- **プロジェクト形態**: MCUXpresso SDK / Zephyr / Matter のいずれも開ける
- **デバッグ**: MCU-Link / PEmicro / SEGGER J-Link を統合認識。Cortex-M33 のデュアルコア・TrustZone・周辺レジスタビュー・RTOS スレッド表示まで対応
- **eIQ 連携**: 拡張から eIQ Toolkit のサンプルプロジェクトをインポートしてビルド・推論実行が可能

> Eclipse の操作感が苦手な人は **VS Code 版が標準的な選択肢**。Linux/macOS/Windows いずれでも同じ手順で利用可。

## eIQ Neutron NPU の活用

### NPU 仕様(おさらい)

| 項目 | 内容 |
|---|---|
| 演算性能 | **4.8 GOPS** (INT8、@ 150MHz) |
| データ型 | **INT8 のみ**(浮動小数点モデルは事前量子化必須) |
| 対応ネットワーク種 | CNN / RNN / TCN / Transformer |
| 推奨用途 | 画像分類 / 物体検出(軽量) / キーワードスポッティング / 振動・センサ異常検知 / ジェスチャ認識 |
| CPU 比 高速化 | 最大 42 倍 (NXP 公称) |

### モデル導入の全体フロー

```
[1] PyTorch / TensorFlow / Keras / ONNX で学習
        │
        ▼
[2] eIQ ModelTool (or onnx2tflite) で TensorFlow Lite (.tflite) に変換
        │
        ▼
[3] INT8 量子化 (代表データセットで Post-Training Quantization)
        │
        ▼
[4] Neutron Converter (eIQ Toolkit 内蔵) で .tflite → Neutron NPU 用 .tflite に再最適化
        │
        ▼
[5] MCUXpresso SDK / VS Code 拡張のサンプルプロジェクトに組込み
        │
        ▼
[6] FRDM-MCXN947 にフラッシュ書込みして実機推論
```

### ONNX モデルの変換手順 (おすすめ ⭐)

学習済み ONNX モデルを **そのまま Neutron NPU 上で動かす** ことが可能です。NXP は専用 CLI を OSS で公開しています。

1. **ONNX → TFLite 変換** ([NXP/eiq-onnx2tflite](https://github.com/NXP/eiq-onnx2tflite))
   ```bash
   # CLI 例(代表的なコマンド形式)
   onnx2tflite --input model.onnx --output model.tflite
   ```
   - PyTorch から `torch.onnx.export()` で書き出した `.onnx` をそのまま投入できる
   - 制約: Neutron NPU が対応するレイヤーのみ。動的形状は事前に固定が必要

2. **INT8 量子化** (eIQ Toolkit / TFLite 標準ツール)
   - 浮動小数点 `.tflite` を **代表データ 100〜数千サンプル** を与えて Post-Training Quantization
   - eIQ Toolkit の **eIQ ModelTool** で GUI 量子化が可能
   - ONNX 段階で量子化したい場合は **`ONNX2Quant`** を使用(QDQ モデル、per-tensor / per-channel、INT8 アクティベーション)

3. **Neutron Converter で NPU 用に再変換** (eIQ Toolkit 内蔵)
   - 量子化済み `.tflite` → Neutron NPU 命令にマッピングされた `.tflite` に変換
   - 変換時に対応外レイヤーが警告される。CPU フォールバック実行されるレイヤーは別表示
   - 変換後のモデルは バイト配列としてヘッダ化され、ファームのフラッシュに格納

4. **サンプルプロジェクトに統合**
   - MCUXpresso SDK の `eiq_examples/tflm_neutron_label_image` などを雛形に
   - モデルファイルを差し替え、入力前処理(リサイズ・正規化)と後処理(softmax 等)を書き換える
   - VS Code 版なら拡張の Quickstart Panel から該当サンプルをインポート可能

5. **実機推論ベンチマーク**
   - SDK 同梱のベンチサンプルで **推論時間** と **NPU 使用率** を計測
   - SWO/UART で結果出力。Solist-AI のような専用 GUI ビューアは不要(printf で十分)

> 詳細手順は [eIQ Neutron NPU Lab Guide (VS Code 版 PDF)](https://community.nxp.com/t5/MCX-Microcontrollers-Knowledge/eIQ-Neutron-NPU-Lab-Guides/ta-p/1799233) と [独自モデル展開手順 (NXP Community)](https://community.nxp.com/t5/MCX-Microcontrollers-Knowledge/MCXN947-How-to-Train-and-Deploy-Customer-ML-model-to-NPU/ta-p/1899497) を参照してください。

### 実装上の注意点

- **メモリ**: モデルとアクティベーションは SRAM 512KB(うち ECC 416KB)に収める必要あり。大きい場合は外付け QSPI Flash と組み合わせる
- **電力**: AI 推論時は全コア・NPU フル稼働で消費電流が増えるため、電池駆動アプリでは推論頻度の制御が必須
- **量子化精度**: INT8 化で精度が落ちる場合があるため、代表データセットの選定が品質を左右する
- **CMSIS-NN フォールバック**: NPU 非対応のレイヤーは CMSIS-NN(CPU)で実行されるため、モデル設計段階で NPU 親和性を意識すると最大性能が出る

### 代表的なサンプルアプリ
- `tflm_label_image` / `tflm_neutron_label_image` — MobileNet 系画像分類
- `tflm_kws` / `kws_cmsis_nn` — キーワードスポッティング(音声 ML)
- `tflm_anomaly_detection` — 振動・電流データの異常検知
- Matter / Thread サンプル(Wi-Fi 外付け時)
- モータ制御サンプル(FOC)+ AI による負荷推定の組合せ例

## 入手方法

- DigiKey JP: [FRDM-MCXN947](https://www.digikey.jp/ja/products/detail/nxp-usa-inc/FRDM-MCXN947/22036137) (¥4,354 前後)
- NXP 直販 / Mouser / Arrow Electronics などからも入手可

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。実際の開発では必ず[ユーザーマニュアル UM12018](https://manuals.plus/m/850e3d758fe83d78fac300a4fadd334e6f7dbbebaa816473275db57080cfa8f9.pdf)、[eIQ Toolkit User Guide](https://www.nxp.com/docs/en/user-guide/EIQTKUG-1.6.9.pdf) で最新の仕様(ピン対応表・電気的定格・NPU の制約・量子化精度など)を確認してください。
