---
title: Solist-AI™ 開発フレームワーク (LEXIDE-Ω / Solist-AI Sim ほか)
slug: solist-ai-dev-framework
tagline: ML63Q2557 / DT-EBML63Q2557 用の統合開発環境・AIモデル生成ツール・デバッガ群
manufacturer: ローム株式会社 / LAPIS Technology
category: 開発フレームワーク (IDE / SDK / AI Tools)
official_url: https://www.rohm.com/lapis-tech/product/micon/solistai-software

features:
  - Eclipse + CDT ベースの統合開発環境 LEXIDE-Ω が ROHM Cortex-M(ML63Q2557 含む)を公式サポート
  - AIモデル自動生成ツール Solist-AI™、PC上のAI動作検証シミュレータ Solist-AI™ Sim、リアルタイム波形ビューア Solist-AI™ Scope を提供
  - CMSIS-DAP 準拠の専用デバッグアダプタ LxEASE™ と 絶縁版 LxEASE™ Isolator を用意
  - オンチップエミュレータ EASE1000 V2 でオンボードデバッグ・Flash 書込みが可能
  - Cortex-M0+ コアなので Keil MDK / Arm GCC / OpenOCD など 汎用 Arm ツールチェーンも併用できる
  - DT-EBML63Q2557 ボード購入者には IO ドライバソース・サンプル(AISignalInference / AIVibrationInference)・Windows ホストアプリが配布

specs:
  - label: 統合開発環境 (IDE)
    value: LEXIDE-Ω (Eclipse + CDT ベース。LAPIS 8/16bit RISC + ROHM Cortex-M を1つでカバー)
  - label: 対応コア
    value: Arm Cortex-M0+ (ML63Q2557 / ML63Q2537 等の Solist-AI™ MCU 全般)
  - label: AIモデル生成
    value: Solist-AI™ (Solist-AI MCU 向けに最適化された AI モデルを自動生成)
  - label: AI動作検証
    value: Solist-AI™ Sim (PC上で推論/学習動作を検証する シミュレータ)
  - label: AI動作可視化
    value: Solist-AI™ Scope (MCU内部の AI 動作をリアルタイム波形で可視化)
  - label: デバッグアダプタ
    value: LxEASE™ (CMSIS-DAP 準拠、Cortex-M 用) / LxEASE™ Isolator (絶縁版)
  - label: オンチップエミュレータ
    value: EASE1000 V2 (オンボードデバッグ・フラッシュ書込み対応)
  - label: 互換ツール
    value: 標準 Arm エコシステム (Keil MDK / Arm GCC / SEGGER J-Link / CMSIS-DAP / DAPLink) も利用可
  - label: 配布形態
    value: ROHM/LAPIS Tech 公式サイトからダウンロード(プロジェクト管理ツール・ビルド・デバッグ・Flash プログラマを含む)
  - label: ボード付属ソフト (DT-EBML63Q2557)
    value: IOドライバソース / AISignalInference / AIVibrationInference / AISignalInferenceHost (Windows)
  - label: 必須ハードウェア
    value: ML63Q2557 搭載ボード (例 DT-EBML63Q2557) + デバッグアダプタ(LxEASE™ もしくは CMSIS-DAP/DAPLink、SEGGER J-Link 等)
  - label: ホストOS
    value: Windows (LEXIDE-Ω および AISignalInferenceHost は Windows 向け)

resources:
  - name: LAPIS Technology - Solist-AI™ Development Support System
    url: https://www.rohm.com/lapis-tech/product/micon/solistai-software
    note: LEXIDE-Ω / Solist-AI Sim / Solist-AI Scope / LxEASE 全体の入口
  - name: LAPIS Technology - MCU Development Support System (汎用)
    url: https://www.rohm.com/lapis-tech/product/micon/software
    note: LEXIDE-Ω 本体・パッチ等の最新ダウンロード
  - name: ROHM - Solist-AI™ Solution 総合ページ
    url: https://www.rohm.com/support/solist-ai
  - name: ROHM - Solist-AI™ MCU 製品検索
    url: https://www.rohm.com/products/micon/solist-ai
  - name: LAPIS - ML63Q2500 グループ データシート (FEDL63Q2500.pdf)
    url: https://fscdn.rohm.com/lapis/en/products/databook/datasheet/ic/micon/FEDL63Q2500.pdf
    note: SoC ブロック図・周辺機能レジスタ仕様
  - name: LAPIS - リファレンスボード RB-D63Q2557TB64 ユーザーズガイド (FEBL63Q2557TB64RB.pdf)
    url: https://fscdn.rohm.com/lapis/en/products/databook/applinote/ic/micon/FEBL63Q2557TB64RB.pdf
    note: 公式リファレンスボードでの開発フロー・接続例
  - name: ROHM - Solist-AI™ Solution プロモーション資料 (PDF)
    url: https://fscdn.rohm.com/en/products/databook/catalog/common/N_Solist-AI_Solution_Promotional_materials_EN.pdf
    note: AxlCORE-ODL アーキテクチャ図と開発フロー図
---

## 概要

ROHM(LAPIS Technology)は Solist-AI™ MCU (ML63Q2557 等) の開発を支援するため、統合開発環境・AI モデル生成ツール・シミュレータ・デバッグアダプタを **一式** 提供しています。Cortex-M0+ ベースなので Arm 標準のエコシステムにも乗っており、CMSIS-DAP/DAPLink/J-Link で書込み・デバッグが可能です。

## ツール構成

```
┌──────────────────────────────────────────────────────────────────────┐
│                       Host PC (Windows)                              │
│                                                                      │
│  ┌────────────────────────────────────────────┐                      │
│  │ LEXIDE-Ω (Eclipse + CDT)                   │                      │
│  │   - C/C++ ビルド・編集・デバッグ          │                      │
│  │   - LAPIS 8/16bit + ROHM Cortex-M を統合   │                      │
│  └─────────────┬──────────────────────────────┘                      │
│                │                                                     │
│  ┌─────────────▼──────────┐  ┌─────────────────────────────┐        │
│  │ Solist-AI™ (モデル生成) │  │ AISignalInferenceHost       │        │
│  │   学習データ → AIモデル │  │ (DT-EBML63Q2557 同梱、       │        │
│  │   ML63Q2557最適化バイナリ│  │  振動/信号データの取得・     │        │
│  └─────────┬──────────────┘  │  可視化)                     │        │
│            │                 └──────────┬──────────────────┘        │
│  ┌─────────▼──────────────┐             │                           │
│  │ Solist-AI™ Sim          │             │                           │
│  │  PC 上で AI 動作を検証  │             │                           │
│  └─────────────────────────┘             │                           │
│                                          │                           │
│  ┌─────────────────────────┐             │                           │
│  │ Solist-AI™ Scope         │             │                           │
│  │  MCU 内部 AI 動作の      │             │                           │
│  │  リアルタイム波形表示    │             │                           │
│  └─────────────┬───────────┘             │                           │
└────────────────┼─────────────────────────┼───────────────────────────┘
                 │ USB                     │ USB
                 │ (CMSIS-DAP 経由)        │ (FT2232H 経由)
   ┌─────────────▼──────────┐  ┌──────────▼─────────────────────┐
   │ LxEASE™ / LxEASE™       │  │ DT-EBML63Q2557 ボード          │
   │ Isolator / EASE1000 V2  │  │   - ML63Q2557 (Cortex-M0+ 48MHz)│
   │  (CMSIS-DAP デバッガ)   │──┤   - AxlCORE-ODL AI アクセラレータ│
   └─────────────────────────┘  │   - センサI/F / 絶縁I/O / RTC 等 │
                                └──────────────────────────────────┘
```

## 各ツールの役割

### LEXIDE-Ω (統合開発環境)
- **配布元**: [LAPIS Technology - MCU Development Support System](https://www.rohm.com/lapis-tech/product/micon/software)
- Eclipse + CDT プラグインベース。プロジェクト管理・ビルド・デバッグを 1 つで完結
- LAPIS 旧来の 8/16 bit RISC コア(nX-U8/U16)に加えて、ROHM Cortex-M も同じ IDE でサポート
- ライセンス情報はインストールフォルダ `Licenses\LEXIDE\` 以下を参照

### Solist-AI™ (AIモデル自動生成ツール)
- 学習用データから ML63Q2557 向けに最適化された AI モデルを自動生成
- 短時間で学習結果の確認・モデル開発を回せる、Solist-AI 開発の中核ツール
- AxlCORE-ODL の 3 層ニューラルネット構造に合わせた重み・量子化を出力

### Solist-AI™ Sim (AI動作検証シミュレータ)
- PC 上で AI 推論/学習の動作を事前検証する PC 実行型シミュレータ
- 実機書込み前にモデルの妥当性を確認できる

### Solist-AI™ Scope (リアルタイムビューア)
- ML63Q2557 内部の AI 動作を **リアルタイム波形** として表示
- リファレンスソフトウェアに同梱
- 異常検知の閾値調整やノイズ評価に有用

### LxEASE™ / LxEASE™ Isolator (デバッグアダプタ)
- ROHM Cortex-M 用デバッグアダプタ。**CMSIS-DAP 準拠**
- LxEASE™ Isolator は ターゲット系統と PC 系統を電気的に絶縁。産業機器の評価で電位差リスクがある場合向け
- DT-EBML63Q2557 の Debug Connector (10ピン SW-DP) に接続

### EASE1000 V2 (オンチップエミュレータ)
- 小型のオンチップエミュレータ。実機接続でのソフトデバッグと Flash 書込みに対応

### DT-EBML63Q2557 同梱ソフトウェア
- **IO ドライバソース** — ボード上の周辺(LCD/FeRAM/RTC/絶縁I/O/USB/SPI/I²C 等)用 C ソース
- **AISignalInference / AIVibrationInference** — 評価用サンプルアプリ。MCU 側で動かす推論アプリの雛形
- **AISignalInferenceHost** — Windows 側ホストアプリ。USB Type-C(CN9 / FT2232H)経由で信号データ取得・可視化

## 典型的な開発フロー

1. **学習データ収集**: DT-EBML63Q2557 + 付属センサ + AISignalInferenceHost で振動/信号データを PC に収集
2. **AIモデル生成**: 収集データを Solist-AI™ ツールに食わせて、ML63Q2557 最適化済みモデルを生成
3. **PCで事前検証**: Solist-AI™ Sim でモデルの推論動作を PC 上で確認
4. **ファームウェアへ統合**: LEXIDE-Ω 上で IO ドライバソース + AISignalInference サンプル + 生成モデルを統合し、ビルド
5. **書込み・実機デバッグ**: LxEASE™(または CMSIS-DAP/DAPLink、J-Link)で Flash 書込み・ステップ実行
6. **実機チューニング**: Solist-AI™ Scope で AI 動作波形をリアルタイム観測しながらパラメータ調整

## 互換ツールチェーン (任意)

ML63Q2557 は **標準の Arm Cortex-M0+ コア** を採用しているため、ROHM 公式ツールに加えて以下も利用可能です(レジスタヘッダや SVD は ROHM 提供のものを使用)。

- **コンパイラ**: Arm GCC / Arm Compiler 6 (Keil MDK)
- **デバッガ**: SEGGER J-Link PLUS / Strawberry Linux ARM-JTAG-20-10 / CMSIS-DAP / DAPLink
- **書込み**: pyOCD / OpenOCD (CMSIS-DAP 経由)
- **CMSIS パック**: ROHM/LAPIS から提供される SVD/CMSIS Device ヘッダを利用

> ⚠️ AxlCORE-ODL(AI アクセラレータ)を活用するには **Solist-AI™ ツールで生成したモデル** が必須です。汎用 Arm ツールチェーンだけでは AI アクセラレータを使った推論は組めません。コアの C プログラム部分のみ汎用ツールで開発する選択は可能です。

## ライセンス・入手

- LEXIDE-Ω 本体・関連ツール: [LAPIS Technology MCU Development Support System](https://www.rohm.com/lapis-tech/product/micon/software) からダウンロード(無償、登録要)
- Solist-AI™ ツール群(Sim/Scope 含む): [Solist-AI™ Development Support System](https://www.rohm.com/lapis-tech/product/micon/solistai-software) から取得
- DT-EBML63Q2557 同梱サンプル: ボード購入者向けに [データ・テクノ](https://www.datatecno.co.jp/prod_info/solistai_board/) から提供

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。各ツールの最新版・対応OS・ライセンス条件は必ず[LAPIS Technology 公式](https://www.rohm.com/lapis-tech/product/micon/solistai-software)で確認してください。
