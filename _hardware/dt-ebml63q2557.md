---
title: DT-EBML63Q2557 (Solist-AI™ 評価ボード)
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
  - name: ROHM - Solist-AI™ ソリューション総合ページ
    url: https://www.rohm.com/support/solist-ai
  - name: ROHM EDGE HACK CHALLENGE 2026 ニュース
    url: https://www.rohm.co.jp/news-detail?news-title=2026-04-22_rehc2026
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

## 入手方法

- データ・テクノ オンライン注文ページ
- 電話: 075-313-3275(平日 9:00〜17:30)
- 問合せフォーム(24時間受付)
- ROHM EDGE HACK CHALLENGE 2026 のデバイス提供キャンペーン対象者には、本ボードを含む数万円相当のデバイス・部品が支給される予定

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。実際の開発では必ず[ハードウェアユーザーズマニュアル](https://www.datatecno.co.jp/datatecno_core/content/uploads/2025/06/DT-EBML63Q2557_hardware_users_manual_Rev.20250527.pdf)および[ROHM ML63Q2557 データシート](https://www.rohm.com/products/micon/solist-ai/ml63q2500-group/ml63q2557-nnntb_tray_-product)で最新の仕様(ピンアサイン・電気的定格・ジャンパ設定など)を確認してください。
