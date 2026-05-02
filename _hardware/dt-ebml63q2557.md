---
title: DT-EBML63Q2557 (Solist-AI™ 評価ボード)
short_title: DT-EBML63Q2557
slug: dt-ebml63q2557
tagline: ROHM ML63Q2557(Solist-AI™ MCU)を搭載した データ・テクノ製評価ボード
manufacturer: 株式会社データ・テクノ (MCUはローム株式会社)
category: 評価ボード(エッジAI MCU搭載)
official_url: https://www.datatecno.co.jp/prod_info/solistai_board/

features:
  - ROHM Solist-AI™ MCU「ML63Q2557」(Arm Cortex-M0+ 48MHz + AIアクセラレータ AxlCORE-ODL)を搭載
  - マイコン単体で機械学習(オンデバイス学習)と推論を実行可能、サーバ/クラウド/ネットワーク不要
  - 12bit ADC・FFT機能内蔵で振動監視/異常検知などのアプリケーションに適合
  - SPI/I²C/USB/LCD インターフェース、2Mbit FeRAM、RTC(CR1220バックアップ) を搭載
  - 評価キット版では MEMS 加速度センサ(ROHM製) もしくは サーモパイルアレイセンサ(SSC製) と樹脂筐体が同梱
  - 購入者向けに IOドライバソース、評価サンプル(AISignalInference / AIVibrationInference)、Windows ホストアプリ を配布

specs:
  - label: 搭載 MCU
    value: ROHM ML63Q2557 (Arm Cortex-M0+ 48MHz, TQFP64, AIアクセラレータ AxlCORE-ODL 内蔵)
  - label: 内蔵メモリ
    value: ROM 256KB / RAM 16KB / データフラッシュ 8KB
  - label: 外付けメモリ
    value: 2Mbit FeRAM (ソフトウェアSPI接続)
  - label: クロック
    value: メイン 32.768kHz水晶 + 内蔵PLLで 48MHz / USB 12MHz水晶 / サブ 20MHz(未実装オプション、CAN用)
  - label: 電源入力
    value: USB Type-C 5V (通信/給電兼用) または 単三電池×2 (2.4〜3.0V)
  - label: 内部レギュレータ
    value: 1.8〜5V入力 → 3.3V / 5V / 24V を出力(センサ・SSR駆動用)
  - label: ロジックレベル
    value: 3.3V CMOS (内蔵12bit ADC レンジは 0〜3.3V)
  - label: A/D 変換
    value: MCU内蔵 12bit ADC(0〜3.3V) / オプションで 16bit ADC TI ADS8860 を搭載可能
  - label: 通信インターフェース
    value: USB (Type-C) / SPI / I²C / UART / LCD インターフェース
  - label: 拡張コネクタ
    value: SPI/I²C 一体型 14ピン MIL規格準拠コネクタ ×1(センサボード接続用)
  - label: デジタル入出力
    value: フォトカプラ絶縁デジタル入力 ×4 / ソリッドステートリレー(SSR)出力 ×2 (JST XH 12ピン)
  - label: ユーザインターフェース
    value: ユーザ用押しボタン ×4 / 電源スイッチ ×1 / ユーザ用赤色LED ×4
  - label: RTC
    value: 内蔵 RTC + CR1220 ボタン電池でバックアップ
  - label: 同梱センサ(キット版)
    value: MEMS加速度センサボード(ROHM製、40cmケーブル) / サーモパイルアレイセンサモジュール(SSC製、100cmケーブル)
  - label: 基板寸法
    value: 125 × 66 mm (突起部除く)
  - label: 動作温度
    value: 0〜50℃ (結露なきこと)

resources:
  - name: データ・テクノ - 製品情報ページ
    url: https://www.datatecno.co.jp/prod_info/solistai_board/
    note: 製品概要・キット構成・ソフトウェア提供内容
  - name: データ・テクノ - 仕様情報ページ
    url: https://www.datatecno.co.jp/prod_info/solistai_board_spec/
    note: ハードウェア仕様一覧(電源、クロック、I/Oなど)
  - name: ハードウェアユーザーズマニュアル (PDF)
    url: https://www.datatecno.co.jp/datatecno_core/content/uploads/2025/06/DT-EBML63Q2557_hardware_users_manual_Rev.20250527.pdf
    note: ピンアサイン・回路詳細・ジャンパ設定など、開発時に必須
  - name: 発売のお知らせ(データ・テクノ)
    url: https://www.datatecno.co.jp/solist-ai%E3%83%9E%E3%82%A4%E3%82%B3%E3%83%B3%E6%90%AD%E8%BC%89%E3%83%9C%E3%83%BC%E3%83%89%E3%80%8Cdt-ebml63q2557%E3%80%8D%E7%99%BA%E5%A3%B2%E3%81%AE%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B/
  - name: ROHM - Solist-AI™ パートナー(データ・テクノ)
    url: https://www.rohm.co.jp/support/solist-ai/partner/datatecno
  - name: ROHM - ML63Q2557 製品ページ
    url: https://www.rohm.com/products/micon/solist-ai/ml63q2500-group/ml63q2557-nnntb_tray_-product
    note: MCU側のデータシート・周辺機能(CAN FD/3相モータPWM/I²C/SPI/UART/12bit ADC等)を参照
  - name: ROHM/LAPIS - ML63Q2500グループ データシート (FEDL63Q2500.pdf)
    url: https://fscdn.rohm.com/lapis/en/products/databook/datasheet/ic/micon/FEDL63Q2500.pdf
    note: SoC内部ブロック図・MCU 64ピン配置・電気的特性は本データシートで確認(英文)
  - name: ROHM/LAPIS - リファレンスボード RB-D63Q2557TB64 ユーザーズガイド (FEBL63Q2557TB64RB.pdf)
    url: https://fscdn.rohm.com/lapis/en/products/databook/applinote/ic/micon/FEBL63Q2557TB64RB.pdf
    note: ROHM公式リファレンスボード側の構成図・回路例
  - name: ROHM - Solist-AI™ ソリューション総合ページ
    url: https://www.rohm.com/support/solist-ai
  - name: ROHM - Solist-AI™ Solution プロモーション資料 (PDF)
    url: https://fscdn.rohm.com/en/products/databook/catalog/common/N_Solist-AI_Solution_Promotional_materials_EN.pdf
    note: AxlCORE-ODL アーキテクチャ概念図あり
  - name: ROHM - Solist-AI™ algorithm and learning, AxlCORE-ODL features (アプリケーションノート PDF)
    url: https://fscdn.rohm.com/lapis/en/products/databook/applinote/ic/micon/solist-ai_algorithm_axlcore-odl_an-e.pdf
    note: ELM ベースの3層FFNN、最大入力512・最大4モデル、教師あり/なし学習、FFT前処理 等の AI 詳細仕様(本ページの「AI 能力と適用範囲」節の根拠資料)
  - name: ROHM EDGE HACK CHALLENGE 2026 公式特設サイト
    url: https://rehc.jp/
    note: スケジュール・審査員・賞金など最新情報の一次ソース
  - name: ROHM EDGE HACK CHALLENGE 2026 プレスリリース(ローム)
    url: https://www.rohm.co.jp/news-detail?news-title=2026-04-22_rehc2026
    note: コンテスト概要およびデバイス提供キャンペーンの初出
---

## 概要

DT-EBML63Q2557 は、株式会社データ・テクノが製造・販売するエッジAI評価ボードで、ローム株式会社のスタンドアロンAI MCU「**ML63Q2557**」(Solist-AI™シリーズ) を搭載しています。マイコン単体でAIの**学習と推論**を行えるのが最大の特徴で、振動監視・異常検知・予知保全といったアプリケーションを **クラウド接続なしで** 構築できます。

ROHM EDGE HACK CHALLENGE 2026 のデバイス提供キャンペーン対象品の中核ボードでもあり、コンテストの主役デバイスとして利用が想定されます。

## 開発時に押さえておきたいポイント

### 電源系統
- USB Type-C(5V) からの給電と、単三電池×2(2.4〜3.0V) からの給電を切り替え可能
- 基板上の内部レギュレータで **3.3V / 5V / 24V** を生成。24V系は SSR 出力やセンサ駆動を想定
- バッテリ駆動を前提とした低消費電力(AI処理時 約40mW)アプリケーションを試作しやすい構成

### ロジックレベルとI/O
- MCU・I/O ともに **3.3V CMOS** ベース。内蔵 12bit ADC のレンジは **0〜3.3V**
- 外部ロジックを 5V や産業用信号レベルで扱う場合は、フォトカプラ絶縁の **デジタル入力×4** と **SSR出力×2** を経由するのが基本
- 拡張センサは SPI/I²C 兼用の **14ピン MIL コネクタ** で接続。同梱の加速度センサ/サーモパイルセンサもこのコネクタ経由

### センサ・周辺機能
- ボード単体ではセンサ非搭載。**評価キット版** を選ぶと、加速度センサ(MEMS) もしくは サーモパイルアレイセンサ + 樹脂筐体が同梱される
- **2Mbit FeRAM**(ソフトウェアSPI)・**RTC(CR1220バックアップ)**・**LCD インターフェース**・USB を搭載しており、データロガー/監視機器のプロトタイプを単体で構築可能
- MCU側の周辺機能としては CAN FD / 3相モータPWM / アナログコンパレータ / UART などが利用可能(基板側で外部に出していない信号もあるためマニュアル要確認)

### ソフトウェア
- 購入者には **IOドライバソース**、**AISignalInference / AIVibrationInference**(評価用サンプル)、**Windows ホストアプリ**(AISignalInferenceHost) が提供される
- ROHM 公式の Solist-AI™ 統合開発環境・ドライバと組み合わせて使うことが想定されている

## AI 能力と適用範囲(AxlCORE-ODL の制約と可能性)

ML63Q2557 に内蔵された AI アクセラレータ **AxlCORE-ODL** は、汎用ニューラルネット推論器ではなく **特定アーキテクチャ専用のハードウェア** です。応募テーマを決める前に、何が動かせて何が動かせないかを把握することが重要です。

### アーキテクチャ(動かせる範囲)

| 項目 | 仕様 |
|------|------|
| ネット構造 | **3層 FFNN(入力 → 隠れ層×1 → 出力)固定** |
| アルゴリズム | **ELM(Extreme Learning Machine)派生**(ROHM 改良版) |
| 学習対象 | **β(隠れ→出力)のみ更新**。α(入力→隠れ)は **ランダム値で固定** |
| 学習方式 | (1) **教師なし**(y≈x、再構成誤差=異常スコア) (2) **教師あり**(y≈t、ワンホット分類 or 連続値回帰) |
| 入力チャンクサイズ | **最大 512 入力 / モデル**(ML63Q2500 グループ) |
| 同時搭載 AI モデル数 | **最大 4 モデル** — 各モデルの入力数に応じてスライド(512入力→1モデル、〜128入力→4モデル) |
| 推論時間 | **〜30ms / モデル**(入力サイズに応じて 0〜30ms 程度) |
| AI 処理時消費電力 | **約 40 mW**(MCU 側はほぼ並列に他処理可能) |
| HW 内蔵前処理 | **FFT(片側振幅スペクトル)・窓関数・正規化** |

> **ELM の本質**: α が学習されない代わりに β を最小二乗で一発フィットできるため、**約1秒で学習完了**。一方、汎用 DNN のような特徴抽出学習はできず、表現力は限定的。

### ❌ できないこと

- **ONNX / TFLite / Keras 等 外部学習済みモデルの取り込み** — アーキテクチャ・学習則がハードウェアで固定されているため、変換パスは存在しない
- **CNN / RNN / Transformer 等 任意のネット構造** — 3層 FFNN 固定
- **画像認識**(28×28 ですら入力 784 点で 512 制約超え。CNN 前提なら不可)
- **多クラス分類**(出力ノード×β重みのメモリ要求で、20+ クラスは厳しい)
- **系列出力**(LSTM 等)・**汎用音声認識**

### ✅ 公式に実証されている用途

公式アプリケーションノート(2025-04-21)に記載のデモ事例:

1. **モータベアリング異常検知**(教師なし、電流センサ単独)
2. **モータ異常の早期兆候検出**(教師なし、電流 + 2軸加速度を結合 = 256×3 → 768×1 リシェイプ入力)
3. **物体識別 4クラス分類**(教師あり、測定ばらつき・個体差を吸収)
4. **非時系列データの OK/NG 分類**(教師あり、製造検査のような単発測定データ)
5. **状態予測 / 劣化予測**(教師あり回帰、出力を連続値に)

### 🎯 実装可能性が高い応募アイデア(REHC2026 想定)

| 想定アプリ | 実装可能性 | 主な入力 |
|------------|------------|----------|
| モータ・ポンプ・コンプレッサ等の **振動 / 電流による異常検知** | ◎ 本命 | 加速度・電流(時系列+FFT) |
| **温度分布(サーモパイルアレイ)による盤面・機器異常監視** | ◎ | サーモパイル(評価キット B) |
| **音響(マイク + FFT)による異音検知** | ○ | マイク(数百Hz〜数kHz) |
| **2〜4 クラスの状態識別**(正常/異常/警告/故障 等) | ◎ | 各種センサ |
| **バッテリ・部品の劣化推定** | ○ | 電圧・温度・電流(回帰) |
| 画像認識(CNN想定) | ✕ | — |
| 汎用音声認識(ASR) | ✕ | — |
| 多クラス分類(20+ クラス) | ✕ | — |

### 開発フロー(現実的な手順)

```
[1] PC で CSV 等のセンサデータ収集(正常 / 異常 / 各クラスのラベル付き)
[2] Solist-AI™ Sim で chunk size・前処理(FFT等)・隠れ層サイズ・モデル数を試行
    → 約1秒のシミュレーションで PR/Recall や anomaly score 分布を確認
[3] LEXIDE-Ω で AI ライブラリと組み合わせてファームウェアを実装
[4] LxEASE / J-Link で書込み、Solist-AI™ Scope で実機波形を観察
[5] 現場で β の追加学習(個体差・環境差の吸収)
```

> **要点**: 「**外部の学習済みモデルを持ち込めない**」「**特徴設計と前処理(特に FFT 周辺)で勝負が決まる**」「**最大 512 入力 × 最大 4 モデル** という枠の中で問題を分割設計する」――この3点が AxlCORE-ODL を活かす鍵となります。

詳細は ROHM 公式アプリケーションノート [*Solist-AI™ algorithm and learning, AxlCORE-ODL features*(PDF)](https://fscdn.rohm.com/lapis/en/products/databook/applinote/ic/micon/solist-ai_algorithm_axlcore-odl_an-e.pdf) を参照。

## ボード ブロック図(図1-1)

ハードウェアユーザーズマニュアル §1.5 図1-1 にボード全体のブロック図が掲載されています。本サイト内の概念図は以下のとおり。

<svg class="board-diagram" viewBox="0 0 820 540" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="DT-EBML63Q2557 ボード ブロック図">
  <defs>
    <marker id="arrow-dt" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#4b5563"/>
    </marker>
  </defs>
  <!-- 上段: 給電源 -->
  <rect class="box box-power" x="10" y="10" width="190" height="50" rx="4"/>
  <text class="label label-bold" x="105" y="32" text-anchor="middle">USB Type-C (CN9)</text>
  <text class="label label-small" x="105" y="48" text-anchor="middle">通信 + 電源</text>
  <rect class="box box-power" x="220" y="10" width="190" height="50" rx="4"/>
  <text class="label label-bold" x="315" y="32" text-anchor="middle">USB Type-C (CN8)</text>
  <text class="label label-small" x="315" y="48" text-anchor="middle">電源専用</text>
  <rect class="box box-power" x="430" y="10" width="190" height="50" rx="4"/>
  <text class="label label-bold" x="525" y="32" text-anchor="middle">電池 CN7 (単三×2)</text>
  <text class="label label-small" x="525" y="48" text-anchor="middle">2.4–3.0V / 電源SW SW7</text>
  <rect class="box box-io" x="640" y="10" width="170" height="50" rx="4"/>
  <text class="label label-bold" x="725" y="32" text-anchor="middle">FT2232H</text>
  <text class="label label-small" x="725" y="48" text-anchor="middle">USB→UART/SPI Bridge</text>
  <!-- 中段: レギュレータ -->
  <rect class="box box-power" x="10" y="90" width="610" height="50" rx="4"/>
  <text class="label label-bold" x="315" y="112" text-anchor="middle">3.3V / 5V / 24V Boost (U13/U14/U15)</text>
  <text class="label label-small" x="315" y="128" text-anchor="middle">JP8/JP9/JP10 で各系統 ON/OFF・PGOOD で MCU へ通知</text>
  <!-- MCU -->
  <rect class="box box-mcu" x="10" y="170" width="800" height="80" rx="6"/>
  <text class="label label-bold" x="410" y="196" text-anchor="middle" font-size="15">ROHM ML63Q2557 (TQFP64)</text>
  <text class="label" x="410" y="216" text-anchor="middle">Arm Cortex-M0+ 48MHz + AxlCORE-ODL AI アクセラレータ</text>
  <text class="label label-small" x="410" y="234" text-anchor="middle">ROM 256KB / RAM 16KB / DataFlash 8KB / 12bit ADC / I²C / SPI / UART / CAN FD / 3相 PWM</text>
  <!-- 下段: 周辺メモリ・LCD・ADC -->
  <rect class="box box-mem" x="10" y="280" width="190" height="50" rx="4"/>
  <text class="label label-bold" x="105" y="302" text-anchor="middle">2 Mbit FeRAM</text>
  <text class="label label-small" x="105" y="318" text-anchor="middle">Soft-SPI / 10¹³回 書込み</text>
  <rect class="box box-mem" x="210" y="280" width="190" height="50" rx="4"/>
  <text class="label label-bold" x="305" y="302" text-anchor="middle">RTC + CR1220</text>
  <text class="label label-small" x="305" y="318" text-anchor="middle">Soft-SPI / バックアップ</text>
  <rect class="box box-io" x="410" y="280" width="190" height="50" rx="4"/>
  <text class="label label-bold" x="505" y="302" text-anchor="middle">LCD 16×2</text>
  <text class="label label-small" x="505" y="318" text-anchor="middle">I²C Fast-mode</text>
  <rect class="box box-io" x="610" y="280" width="200" height="50" rx="4"/>
  <text class="label label-bold" x="710" y="302" text-anchor="middle">ADS8860 (任意実装)</text>
  <text class="label label-small" x="710" y="318" text-anchor="middle">16bit ADC / SPI#1</text>
  <!-- 拡張コネクタ群 -->
  <rect class="box box-io" x="10" y="360" width="195" height="60" rx="4"/>
  <text class="label label-bold" x="107" y="382" text-anchor="middle">CN1 SPI/I²C 14pin</text>
  <text class="label label-small" x="107" y="398" text-anchor="middle">MEMSセンサ等</text>
  <text class="label label-small" x="107" y="412" text-anchor="middle">付属 加速度/サーモパイル</text>
  <rect class="box box-io" x="215" y="360" width="195" height="60" rx="4"/>
  <text class="label label-bold" x="312" y="382" text-anchor="middle">CN5 絶縁I/O 12pin</text>
  <text class="label label-small" x="312" y="398" text-anchor="middle">フォトカプラ入力 ×4</text>
  <text class="label label-small" x="312" y="412" text-anchor="middle">SSR 出力 ×2</text>
  <rect class="box box-io" x="420" y="360" width="195" height="60" rx="4"/>
  <text class="label label-bold" x="517" y="382" text-anchor="middle">CN4 RS-485 / CAN</text>
  <text class="label label-small" x="517" y="398" text-anchor="middle">3pin / 終端 JP3</text>
  <text class="label label-small" x="517" y="412" text-anchor="middle">PHY 排他切替</text>
  <rect class="box box-io" x="625" y="360" width="185" height="60" rx="4"/>
  <text class="label label-bold" x="717" y="382" text-anchor="middle">CN6 アナログ入力</text>
  <text class="label label-small" x="717" y="398" text-anchor="middle">3pin OpAmp 経由</text>
  <text class="label label-small" x="717" y="412" text-anchor="middle">12bit ADC AIN0</text>
  <!-- ユーザIF / デバッグ -->
  <rect class="box" x="10" y="450" width="400" height="60" rx="4"/>
  <text class="label label-bold" x="210" y="472" text-anchor="middle">ユーザインターフェース</text>
  <text class="label label-small" x="210" y="488" text-anchor="middle">押しボタン×4(SW2-SW5) / DIP-SW(SW1, SW6)</text>
  <text class="label label-small" x="210" y="502" text-anchor="middle">LED×4 / 電源SW SW7</text>
  <rect class="box" x="420" y="450" width="390" height="60" rx="4"/>
  <text class="label label-bold" x="615" y="472" text-anchor="middle">デバッグ</text>
  <text class="label label-small" x="615" y="488" text-anchor="middle">10pin SW-DP (Serial Wire Debug)</text>
  <text class="label label-small" x="615" y="502" text-anchor="middle">CMSIS-DAP / DAPLink / J-Link / ARM-JTAG-20-10 対応</text>
  <!-- Arrows -->
  <path d="M 105 60 L 105 90" class="arrow" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-dt)"/>
  <path d="M 315 60 L 315 90" class="arrow" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-dt)"/>
  <path d="M 525 60 L 525 90" class="arrow" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-dt)"/>
  <path d="M 725 60 L 725 170" class="arrow" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-dt)"/>
  <path d="M 315 140 L 315 170" class="arrow" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-dt)"/>
  <path d="M 105 250 L 105 280" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 305 250 L 305 280" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 505 250 L 505 280" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 710 250 L 710 280" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 107 330 L 107 360" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 312 330 L 312 360" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 517 330 L 517 360" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 717 330 L 717 360" stroke="#2563eb" stroke-width="2" fill="none"/>
  <text class="label-small" x="120" y="270" font-size="9" fill="#2563eb">Soft-SPI</text>
  <text class="label-small" x="320" y="270" font-size="9" fill="#2563eb">Soft-SPI</text>
  <text class="label-small" x="515" y="270" font-size="9" fill="#2563eb">I²C</text>
  <text class="label-small" x="720" y="270" font-size="9" fill="#2563eb">SPI#1</text>
  <text class="label-small" x="120" y="350" font-size="9" fill="#2563eb">SPI#0/I²C</text>
  <text class="label-small" x="325" y="350" font-size="9" fill="#2563eb">GPIO</text>
  <text class="label-small" x="525" y="350" font-size="9" fill="#2563eb">UART</text>
  <text class="label-small" x="725" y="350" font-size="9" fill="#2563eb">ADC</text>
</svg>

> SoC 内部のブロック図(AxlCORE-ODL を含む)は [LAPIS ML63Q2500 データシート (FEDL63Q2500.pdf)](https://fscdn.rohm.com/lapis/en/products/databook/datasheet/ic/micon/FEDL63Q2500.pdf) 冒頭の Block Diagram を参照してください。AI アクセラレータの位置付けや 3 層ニューラルネットの構成イメージは [Solist-AI™ Promotional Materials (PDF)](https://fscdn.rohm.com/en/products/databook/catalog/common/N_Solist-AI_Solution_Promotional_materials_EN.pdf) に図示されています。

ボード現物の部品配置・シルクは、ハードウェアマニュアル §2 (図2-1〜2-7) と §3 (図3-1〜3-3) に表面/裏面/MEMSセンサボードの写真が掲載されています。

## コネクタ一覧

ハードウェアマニュアル §4 (表2) より。

| 番号 | 用途 |
|---|---|
| CN1 | デジタルセンサ I/F (SPI/I²C 14ピン MIL、付属の加速度/サーモパイルセンサもここに接続) |
| CN2 | 未使用 / 予備 (実装はマニュアル参照) |
| CN3 | 予備コネクタ |
| CN4 | RS-485 / CAN (任意実装、3ピン JST XH) |
| CN5 | 絶縁デジタル I/O (12ピン JST XH、絶縁IN×4 / SSR OUT×2) |
| CN6 | アナログ入力 (3ピン) |
| CN7 | 電池入力 (単三×2、2.4〜3.0V) |
| CN8 | USB Type-C (電源専用) |
| CN9 | USB Type-C (通信 + 電源) |

> CN2/CN3 の正確な用途はマニュアル PDF §4 表2 で確認してください(本ページの抽出では字化けして判別困難なため省略)。

## コネクタ ピンアサイン

### CN1 — デジタルセンサ I/F (14ピン MIL、SPI + I²C)

| Pin | 信号 | Pin | 信号 |
|----:|------|----:|------|
| 1 | P73 / SCL (I²C) | 2 | GND |
| 3 | P74 / SDA (I²C) | 4 | GND |
| 5 | Power Out | 6 | P23 / INT2 |
| 7 | P22 / INT1 | 8 | Power Out |
| 9 | P41 / MOSI (SPI) | 10 | P42 / MISO (SPI) |
| 11 | GND | 12 | P40 / SCK (SPI) |
| 13 | GND | 14 | P43 / CS (SPI) |

- Power Out は基板の 3.3V または 5V を選択(JP1 で切替、デフォルトは要マニュアル確認)
- I²C は LCD と共通(Fast-mode)。SPI は MCU の SPI#0 を共有

### CN4 — RS-485 / CAN (3ピン JST XH、任意実装)

| Pin | 信号 |
|----:|------|
| 1 | RS-485 B(−) / CAN-L |
| 2 | RS-485 A(+) / CAN+ |
| 3 | GND |

JP3 で終端抵抗の有効/無効を選択。RS-485 と CAN はトランシーバ IC 実装で排他切替。

### CN5 — 絶縁デジタル I/O (12ピン JST XH)

| Pin | 信号 |
|----:|------|
| 1 | SW4 外部入力 + |
| 2 | SW4 外部入力 − |
| 3 | SW5 外部入力 + |
| 4 | SW5 外部入力 − |
| 5 | IN0 (絶縁入力) + |
| 6 | IN0 (絶縁入力) − |
| 7 | IN1 (絶縁入力) + |
| 8 | IN1 (絶縁入力) − |
| 9 | OUT0 a (SSR0) |
| 10 | OUT0 c (SSR0) |
| 11 | OUT1 a (SSR1) |
| 12 | OUT1 c (SSR1) |

- IN0/IN1 はフォトカプラ絶縁入力。SW4/SW5 は基板上の押しボタンを外部からも駆動できるよう端子化されたもの
- OUT0/OUT1 は SSR (ソリッドステートリレー) で、絶対最大 24V 系を制御可能

### CN6 — アナログ入力 (3ピン)

| Pin | 信号 |
|----:|------|
| 1 | Power Out (センサ駆動用) |
| 2 | Analog Input (0〜3.3V、内蔵12bit ADC AIN0 接続) |
| 3 | GND |

- DIP-SW SW6 でゲイン(0.741〜20倍)切替、JP7 で AC/DC 結合切替、JP4 で OpAmp 有効化
- AC 入力時は 1.65V バイアス。10kHz まで対応(マニュアル §5.12 表4 参照)

### CN7 — 電池入力 (2ピン)

単三電池 ×2 (2.4〜3.0V)。逆接保護 Q2 経由で内部レギュレータへ。

### CN8 / CN9 — USB Type-C

- CN8: 電源専用 (5V, 500mA)
- CN9: 通信(FT2232H 経由 UART/SPI) + 電源 (5V, 500mA)

### Debug Connector — 10ピン SW-DP

ARM Cortex Debug Connector (Serial Wire Debug)。CMSIS-DAP / DAPLink / SEGGER J-Link PLUS / Strawberry Linux ARM-JTAG-20-10 で接続可能。CMSIS-DAP/DAPLink は 1番ピン (Vcc) からターゲット給電も可。

## MCU ピンアサイン (ML63Q2557 / TQFP64)

ハードウェアマニュアル §7.3 表5 より、本ボードでの結線。

| Pin | 信号(MCU) | I/O | TP | 用途 |
|---:|------|:---:|---|------|
| 1 | SWD | I/O | TP12 | SW-DP データ (要外部プルアップ) |
| 2 | SWC | I | TP11 | SW-DP クロック (要外部プルアップ) |
| 3 | P72 | O | — | EXT_RESET_B (外部デバイスリセット) |
| 4 | TXDF1 | O | — | FT2232H からの RXD |
| 5 | RXDF1 | I | — | FT2232H への TXD |
| 6 | RESET_N | I | — | MCU RESET_B (要外部プルアップ) |
| 7 | VREF | — | TP9 | VCC 接続 |
| 8 | VREFN | — | TP10 | GND 接続 |
| 9 | HXT0 | I | TP5 | 20MHz水晶 (未実装オプション、CAN用) |
| 10 | HXT1 | I | TP6 | 同上 |
| 11 | VDDL | — | TP7 | Power |
| 12 | VSS | — | TP8 | GND |
| 13 | VDD | — | TP23 | Power |
| 14 | NC | — | — | 未接続 |
| 15 | XT1 | I | TP20 | 32.768kHz水晶 |
| 16 | XT0 | O | TP21 | 32.768kHz水晶 |
| 17 | P22 / INT | I | TP22 | デジタルセンサ INT1 (要外部プルアップ) |
| 18 | P23 / INT | I | TP19 | デジタルセンサ INT2 (要外部プルアップ) |
| 19 | SCKF0-2 | O | TP18 | SPI#0 SCK (CN1) |
| 20 | SOUTF0-2 | O | TP16 | SPI#0 MOSI (CN1) |
| 21 | SINF0-2 | I | TP15 | SPI#0 MISO (CN1) |
| 22 | SSNF0-2 | O | TP14 | SPI#0 CS (CN1) |
| 23 | P44 | O | TP13 | POWSW_CHK 入力検出 |
| 24 | P45 | O | TP17 | POWER_KEEP |
| 25 | P46 | I | TP32 | REG5V_ON |
| 26 | P47 | O | TP33 | REG24V_ON |
| 27 | P80 / INT | O | TP34 | RTC INT (要外部プルアップ) |
| 28 | P81 | I | TP35 | CS3 (RTC、要外部プルダウン) |
| 29 | P82 | O | TP36 | CS2_B (FeRAM、要外部プルアップ) |
| 30 | P83 | O | TP37 | Soft-SPI MISO2 (要外部プルアップ) |
| 31 | P84 | I | TP38 | Soft-SPI MOSI2 (要外部プルアップ) |
| 32 | P85 | O | TP39 | Soft-SPI SCK2 (要外部プルアップ) |
| 33 | VDD | — | TP40 | Power |
| 34 | P30 | O | TP41 | FeRAM /WP 信号 (要外部プルダウン) |
| 35 | P31 | O | TP42 | VDET モニタ Enable |
| 36 | AIN0 | A | TP43 | アナログ入力(CN6) |
| 37 | AIN1 | A | TP31 | VDET アナログ入力 (電源電圧監視) |
| 38 | P34 | I | TP30 | DIP-SW SW1-1 |
| 39 | P35 | I | TP29 | DIP-SW SW1-2 |
| 40 | P36 | I | TP28 | DIP-SW SW1-3 |
| 41 | P37 | I | TP27 | DIP-SW SW1-4 |
| 42 | P50 | I | TP26 | 押しボタン SW2 |
| 43 | P51 | I | TP25 | 押しボタン SW3 |
| 44 | P52 | I | TP24 | 押しボタン SW4 |
| 45 | P53 | I | — | 押しボタン SW5 |
| 46 | P54 | I | — | LED1 |
| 47 | P55 | I | — | LED2 |
| 48 | P56 | I | — | LED3 |
| 49 | P57 | O | — | (LED4 / 予備) |
| 50 | BRMPN | O | — | ISOOUT1 (SSR1 駆動) |
| 51 | P66 | I | — | ROM Address Remap Enable |
| 52 | P65 | I | — | ISOOUT0 (SSR0 駆動) |
| 53 | P64 | O | — | ISOIN1 (絶縁入力1) |
| 54 | SSNF1-1 | I | — | ISOIN0 (絶縁入力0) |
| 55 | SINF1-1 | I | — | FT2232H SPI CS |
| 56 | SOUTF1-1 | O | — | FT2232H SPI MOSI |
| 57 | SCKF1-1 | I | — | FT2232H SPI MISO |
| 58 | P77 | I | — | FT2232H SPI SCK |
| 59 | P76 | O | — | RS-485 DE / CAN STB (要外部プルダウン) |
| 60 | P75 | I/O | — | 未接続 (NC) |
| 61 | SDAF0-2 | O | — | LCD_BACKLIGHT 制御 |
| 62 | SCLF0-2 | I | — | I²C SDA (CN1, LCD 共有) |
| 63 | RXDF0 / CAN_RX0 | O | — | I²C SCL (CN1, LCD 共有) |
| 64 | TXDF0 / CAN_TX0 | — | — | RS-485 / CAN RXD/TXD |

> ⚠️ 上記の I/O 方向や内部結線は PDF テキスト抽出時に列がずれる可能性があるため、実際の実装の前に必ず[ハードウェアユーザーズマニュアル §7.3](https://www.datatecno.co.jp/datatecno_core/content/uploads/2025/06/DT-EBML63Q2557_hardware_users_manual_Rev.20250527.pdf) の表5原本で確認してください。

## 主なテストポイント (TP1〜TP48 抜粋)

ハードウェアマニュアル §7.4 表6 より。デバッグ・信号観測時に有用。

| TP | 信号 | 用途 |
|---|---|---|
| TP1〜TP4 | GND | グランド |
| TP5〜TP8 | ACC_SCK / MOSI / MISO / CS | デジタルセンサ I/F SPI |
| TP9 / TP10 | ACC_INT1 / INT2 | センサ割込み |
| TP11 | RESET_B | パワーオンリセット |
| TP12 | EXT_RESET_B | 外部デバイスリセット |
| TP13〜TP16 | SCK2 / MOSI2 / MISO2 / CS2_B | Soft-SPI (FeRAM 用) |
| TP17 | WP_B | FeRAM /WP |
| TP18 | CS3 | Soft-SPI CS for RTC |
| TP19 | RTCINT_B | RTC 割込み |
| TP20 | POWER_KEEP | 3.3V 電源維持信号 |
| TP21 | REG5V_ON | 5V レギュレータ ON |
| TP22 | REG24V_ON | 24V レギュレータ ON |
| TP23 | POWSW_CHK | 電源SW 押下検出 |
| TP24 / TP25 | LCD_SCL / LCD_SDA | LCD I²C |
| TP26 | LCD_BACKLIGHT | バックライト制御 |
| TP28〜TP31 | SLAVE_SPI_SCK/MISO/MOSI/SEL | USB-SPI (FT2232H) |
| TP32 | AnalogIN | CN6 アナログ入力(OpAmp前) |
| TP33〜TP36 | SW1_1〜SW1_4 | DIP-SW SW1 各列 |
| TP37〜TP40 | SW2 / SW3 / SW4 / SW5 | 押しボタン |
| TP41〜TP43 | LED1 / LED2 / LED3 | ユーザ LED |
| TP44 / TP45 | AMP_IN / AMP_OUT | アナログ OpAmp 入出力 |
| TP46 | VDET_GATE | 電源電圧監視 Enable |
| TP47 | VDET | 電源電圧 |
| TP48 | AIN1 | VDET 測定入力 |

> 電源電圧の算出式: `VDET[V] = AIN1 × 6.6 / 4096` (ハードウェアマニュアル §5.1.9)

## ジャンパ・スイッチ (表3 抜粋)

| 番号 | 用途 |
|---|---|
| JP1 | デジタル電源電圧選択 (3.3V / 5V) |
| JP2 | ROM アドレス リマップ |
| JP3 | RS-485 / CAN 終端抵抗 |
| JP4 | アナログ OpAmp 有効化 |
| JP5 | アナログ 24V 注入 |
| JP6 | アナログ電源電圧選択 |
| JP7 | アナログ DC/AC 結合切替 |
| JP8 | 3.3V 電源 ON 維持 |
| JP9 | 24V DC-DC 強制 ON |
| JP10 | 5V DC-DC 強制 ON |
| SW1 | DIP-SW(汎用4ビット) |
| SW6 | DIP-SW(アナログ ゲイン調整、4ビット) |
| SW7 | 電源スイッチ |

## 電気的定格 (マニュアル §6 抜粋)

### 推奨動作 (出力電流の代表値)

| 系統 | 値 |
|---|---|
| 3.3V | 100mA (代表) |
| 5V | 100mA (代表) |
| 24V | 3.5mA |
| センサ駆動出力 | 50mA (代表) |
| MCU 動作 | ML63Q2557 規格に準ずる |

### 絶対最大定格

| 入力 | 値 |
|---|---|
| USB Type-C | 6V |
| 電池 (単三×2) | 5V |
| MCU GPIO | 3.6V |
| アナログ入力 (OpAmp 経由) | 28V |
| 絶縁デジタル入力 | 24V |
| RS-485 / CAN ライン | 24V |

## 入手方法

- データ・テクノ オンライン注文ページ
- 電話: 075-313-3275(平日 9:00〜17:30)
- 問合せフォーム(24時間受付)
- ROHM EDGE HACK CHALLENGE 2026 のデバイス提供キャンペーン対象者には、本ボードを含む数万円相当のデバイス・部品が支給される予定

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。実際の開発では必ず[ハードウェアユーザーズマニュアル](https://www.datatecno.co.jp/datatecno_core/content/uploads/2025/06/DT-EBML63Q2557_hardware_users_manual_Rev.20250527.pdf) および [LAPIS ML63Q2500 データシート (FEDL63Q2500.pdf)](https://fscdn.rohm.com/lapis/en/products/databook/datasheet/ic/micon/FEDL63Q2500.pdf) で最新の仕様(SoC ブロック図・MCUピン配置・ジャンパ設定・電気的定格など)を確認してください。
