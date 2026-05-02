---
title: FRDM-MCXC444 (NXP MCX C444 評価ボード)
short_title: FRDM-MCXC444
slug: frdm-mcxc444
tagline: Cortex-M0+ 48MHz + 加速度/光センサ + SLCD を搭載した低消費電力 Freedom ボード
manufacturer: NXP Semiconductors
category: 評価ボード(汎用 Cortex-M0+ MCU)
official_url: https://www.nxp.com/

features:
  - MCX C シリーズ MCU "MCXC444" を搭載した Freedom フォームファクタの評価ボード
  - Arm Cortex-M0+ 48MHz、Flash 256KB / SRAM 32KB、内蔵 USB FS 2.0
  - 3軸加速度センサ FXLS8974CFR3 と 可視光センサ をオンボード搭載(I²C 接続)
  - セグメント LCD ドライバ(SLCD、最大 24×8 / 28×4 セグメント)を内蔵し、外部 LCD 無しで動作
  - Arduino R3 / FRDM / mikroBUS / Pmod の 4 種ヘッダ互換、拡張性が高い
  - オンボード MCU-Link デバッガ(CMSIS-DAP 準拠)。USB Type-C 1 本で書込み・デバッグ・電源供給
  - DigiKey Make ONE Challenge 2026 で「おすすめ製品」として一次審査の加点対象

specs:
  - label: 搭載 MCU
    value: NXP MCXC444VLH (Arm Cortex-M0+ 48MHz、64ピン LQFP)
  - label: 内蔵メモリ
    value: Flash 256KB / SRAM 32KB / EEPROM (FlexNVM 領域)
  - label: 通信ペリフェラル
    value: 2× LPUART / 1× UART / 2× I²C / 2× SPI / USB FS 2.0 / I²S
  - label: 周辺機能
    value: 16bit ADC / 12bit DAC / DMA / PWM (FlexTimer) / RTC / SLCD ドライバ / アナログコンパレータ
  - label: AI アクセラレータ
    value: なし(CPU で eIQ ライブラリの軽量 TFLite Micro 推論は可)
  - label: 搭載センサ
    value: 3軸加速度 FXLS8974CFR3 (I²C0、P3V3 給電) / 可視光センサ
  - label: 搭載ディスプレイ
    value: SLCD ドライバ内蔵(セグメント LCD を直接駆動。8×24 または 4×28 セグメント)
  - label: 拡張ヘッダ
    value: Arduino R3 互換 (J1〜J4) / FRDM ヘッダ / mikroBUS / Pmod
  - label: デバッガ
    value: オンボード MCU-Link (CMSIS-DAP 準拠) / SWD コネクタ
  - label: 電源
    value: USB Type-C 5V → 内部 LDO で 3.3V (P3V3) 生成
  - label: ロジックレベル
    value: 3.3V CMOS (5V Arduino シールドは要レベル変換)
  - label: ボード寸法
    value: 約 81 × 53 mm (Freedom 標準フォーム)
  - label: 価格目安
    value: ¥1,750 (DigiKey JP)

resources:
  - name: NXP - FRDM-MCXC444 製品ページ
    url: https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-MCXC444
  - name: ユーザーマニュアル UM12120 (PDF)
    url: https://docs.rs-online.com/00be/A700000012839604.pdf
    note: ピン配置・回路図・ジャンパ・センサ接続など詳細仕様
  - name: クイックスタートガイド
    url: https://manualzz.com/doc/81199989/nxp-frdm-mcxc444-development-board-owner%E2%80%99s-manual
  - name: DigiKey JP - FRDM-MCXC444 商品ページ
    url: https://www.digikey.jp/ja/products/detail/nxp-usa-inc/FRDM-MCXC444/24374774
  - name: MCUXpresso SDK ドキュメント (FRDM-MCXC444)
    url: https://mcuxpresso.nxp.com/mcuxsdk/24.12.00/html/boards/frdmmcxc444/index.html
  - name: Zephyr Project - FRDM-MCXC444 ボードドキュメント
    url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxc444/doc/index.html
  - name: NXP App Code Hub - SLCD + FXLS8974 motion detection サンプル
    url: https://github.com/nxp-appcodehub/dm-slcd-and-fxls8974-on-mcxc444
    note: 加速度センサ + SLCD 表示の実装例
  - name: NXP App Code Hub - LCD + FXLS8974CF 動作検出サンプル
    url: https://github.com/nxp-appcodehub/dm-mcxc444-lcd-and-fxls8974cf-motion-detection
---

## 概要

FRDM-MCXC444 は NXP MCX C シリーズの評価用 Freedom ボードで、超低消費電力の **Cortex-M0+ 48MHz** コアと **3 軸加速度センサ・可視光センサ・SLCD ドライバ** を 1 枚に集約しています。USB Type-C 1 本で給電・書込み・デバッグまで完結し、Arduino / mikroBUS / Pmod の各シールドが接続できるため、入門〜量産プロトタイプまで幅広く利用できます。

DigiKey Make ONE Challenge 2026 では「おすすめ製品」(NXP 4 ボードの 1 つ) として、一次審査の加点対象になります。

## ボード ブロック図

<svg class="board-diagram" viewBox="0 0 820 460" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="FRDM-MCXC444 ボード ブロック図">
  <defs>
    <marker id="arrow-mcxc" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#4b5563"/>
    </marker>
  </defs>
  <!-- USB / 電源 -->
  <rect class="box box-power" x="10" y="10" width="200" height="50" rx="4"/>
  <text class="label label-bold" x="110" y="32" text-anchor="middle">USB Type-C (J10)</text>
  <text class="label label-small" x="110" y="48" text-anchor="middle">5V 給電 + デバッグ + UART CDC</text>
  <rect class="box box-power" x="220" y="10" width="200" height="50" rx="4"/>
  <text class="label label-bold" x="320" y="32" text-anchor="middle">内部 LDO → P3V3</text>
  <text class="label label-small" x="320" y="48" text-anchor="middle">3.3V CMOS, FXLS8974 給電</text>
  <!-- MCU-Link -->
  <rect class="box box-io" x="430" y="10" width="190" height="50" rx="4"/>
  <text class="label label-bold" x="525" y="32" text-anchor="middle">MCU-Link デバッガ</text>
  <text class="label label-small" x="525" y="48" text-anchor="middle">CMSIS-DAP / SWD コネクタ</text>
  <!-- MCU -->
  <rect class="box box-mcu" x="10" y="100" width="800" height="80" rx="6"/>
  <text class="label label-bold" x="410" y="126" text-anchor="middle" font-size="15">NXP MCXC444VLH (LQFP64)</text>
  <text class="label" x="410" y="146" text-anchor="middle">Arm Cortex-M0+ 48MHz</text>
  <text class="label label-small" x="410" y="164" text-anchor="middle">Flash 256KB / SRAM 32KB / SLCD ドライバ内蔵 / USB FS / 16bit ADC / 12bit DAC</text>
  <!-- 搭載センサ -->
  <rect class="box box-mem" x="10" y="210" width="260" height="60" rx="4"/>
  <text class="label label-bold" x="140" y="232" text-anchor="middle">FXLS8974CFR3</text>
  <text class="label label-small" x="140" y="248" text-anchor="middle">3軸加速度センサ</text>
  <text class="label label-small" x="140" y="262" text-anchor="middle">I²C0 (SDA=PTE25, SCL=PTE24)</text>
  <rect class="box box-mem" x="280" y="210" width="260" height="60" rx="4"/>
  <text class="label label-bold" x="410" y="232" text-anchor="middle">可視光センサ</text>
  <text class="label label-small" x="410" y="248" text-anchor="middle">アナログ / I²C 接続</text>
  <text class="label label-small" x="410" y="262" text-anchor="middle">P3V3 給電</text>
  <rect class="box box-io" x="550" y="210" width="260" height="60" rx="4"/>
  <text class="label label-bold" x="680" y="232" text-anchor="middle">SLCD インターフェース</text>
  <text class="label label-small" x="680" y="248" text-anchor="middle">セグメント LCD 直接駆動</text>
  <text class="label label-small" x="680" y="262" text-anchor="middle">最大 24×8 / 28×4</text>
  <!-- 拡張ヘッダ -->
  <rect class="box" x="10" y="290" width="800" height="60" rx="4"/>
  <text class="label label-bold" x="410" y="312" text-anchor="middle">拡張ヘッダ (Arduino R3 / FRDM / mikroBUS / Pmod)</text>
  <text class="label label-small" x="410" y="330" text-anchor="middle">GPIO / SPI / I²C / UART / ADC / PWM を引き出し</text>
  <text class="label label-small" x="410" y="344" text-anchor="middle">5V Arduino シールドはレベル変換が必要(本体は 3.3V CMOS)</text>
  <!-- ユーザIF -->
  <rect class="box" x="10" y="370" width="400" height="70" rx="4"/>
  <text class="label label-bold" x="210" y="392" text-anchor="middle">ユーザインターフェース</text>
  <text class="label label-small" x="210" y="408" text-anchor="middle">押しボタン SW2 (PTC3) / SW3 (PTA4)</text>
  <text class="label label-small" x="210" y="422" text-anchor="middle">リセット SW1 (PTA20)</text>
  <text class="label label-small" x="210" y="436" text-anchor="middle">RGB LED 赤 PTE31 / 緑 PTD5 / 青 PTE29</text>
  <rect class="box" x="420" y="370" width="390" height="70" rx="4"/>
  <text class="label label-bold" x="615" y="392" text-anchor="middle">UART コンソール</text>
  <text class="label label-small" x="615" y="408" text-anchor="middle">PTA1 (RX) / PTA2 (TX)</text>
  <text class="label label-small" x="615" y="422" text-anchor="middle">MCU-Link 仮想 COM 経由で PC に接続</text>
  <text class="label label-small" x="615" y="436" text-anchor="middle">115200 8N1 が標準</text>
  <!-- Arrows -->
  <path d="M 110 60 L 110 100" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-mcxc)"/>
  <path d="M 320 60 L 320 100" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-mcxc)"/>
  <path d="M 525 60 L 525 100" stroke="#4b5563" stroke-width="1.5" fill="none" marker-end="url(#arrow-mcxc)"/>
  <path d="M 140 180 L 140 210" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 410 180 L 410 210" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 680 180 L 680 210" stroke="#2563eb" stroke-width="2" fill="none"/>
  <path d="M 410 270 L 410 290" stroke="#2563eb" stroke-width="2" fill="none"/>
  <text class="label-small" x="145" y="200" font-size="9" fill="#2563eb">I²C0</text>
  <text class="label-small" x="415" y="200" font-size="9" fill="#2563eb">ADC/I²C</text>
  <text class="label-small" x="685" y="200" font-size="9" fill="#2563eb">SLCD</text>
</svg>

> 詳細なブロック図・回路図は [ユーザーマニュアル UM12120](https://docs.rs-online.com/00be/A700000012839604.pdf) を参照。

## 主要 GPIO / 周辺ペリフェラル

ボード上で割当済みの主要ピンを一覧します(出典: Zephyr の board overlay と UM12120)。

| 機能            | ピン            | 接続先                          |
| --------------- | --------------- | ------------------------------- |
| UART コンソール RX | PTA1            | MCU-Link 仮想 COM               |
| UART コンソール TX | PTA2            | MCU-Link 仮想 COM               |
| I²C0 SDA        | PTE25           | FXLS8974CFR3 加速度センサ        |
| I²C0 SCL        | PTE24           | FXLS8974CFR3 加速度センサ        |
| LED 赤          | PTE31           | RGB LED                         |
| LED 緑          | PTD5            | RGB LED                         |
| LED 青          | PTE29           | RGB LED                         |
| リセット SW1    | PTA20           | リセットボタン                  |
| ユーザ SW2      | PTC3            | プッシュボタン                  |
| ユーザ SW3      | PTA4            | プッシュボタン                  |
| ADC0 ch1        | PTE20           | アナログ入力                    |

その他、Arduino R3 ヘッダ (J1〜J4) には PTB/PTC/PTD/PTE 系の GPIO が引き出され、SPI / 追加 UART / PWM / ADC として再利用できます。**正確な対応表は必ず [UM12120](https://docs.rs-online.com/00be/A700000012839604.pdf) §5「Connectors」で確認してください。**

## 電源系統

| 項目 | 仕様 |
|---|---|
| 主電源 | USB Type-C (J10、5V、500mA) |
| 内部レギュレータ | LDO で **P3V3 (3.3V)** を生成 |
| センサ系電源 | P3V3 から FXLS8974CFR3 / 可視光センサに供給 |
| MCU 動作電圧 | 1.71〜3.6V (本ボードでは 3.3V 固定) |
| ロジックレベル | 3.3V CMOS |
| 外部給電 | Arduino ヘッダの 5V/3.3V 端子からの給電も可(ジャンパ要確認) |
| 消費電流 | MCU 単体は 数 mA 〜 数十 mA(クロック・周辺による) |

## 開発環境

| 種類 | 対応環境 |
|---|---|
| 公式 IDE (Eclipse) | **MCUXpresso IDE** (Eclipse + CDT ベース、NXP 純正) |
| 公式 IDE (VS Code) | **MCUXpresso for VS Code** ([Marketplace](https://marketplace.visualstudio.com/items?itemName=NXPSemiconductors.mcuxpresso))。プロジェクト管理・ビルド・デバッグ・周辺レジスタビュー・RTOS スレッド表示まで VS Code 内で完結 |
| SDK | **MCUXpresso SDK** (FRDM-MCXC444 ボードコンポーネント込み、HAL/ドライバ/サンプル) |
| 設定ツール | MCUXpresso Config Tools (ピンマックス・クロックツリー・周辺機能を GUI 設定) |
| インストーラ | **MCUXpresso Installer** (SDK / GNU Arm Toolchain / Zephyr SDK / デバッグソフト等を統合インストール) |
| 商用 IDE | Keil MDK (Arm Compiler 6) / IAR Embedded Workbench for Arm |
| RTOS | FreeRTOS / Zephyr / NuttX / Mbed OS |
| AI ライブラリ | eIQ ライブラリ(CPU 推論、CMSIS-NN / TFLite Micro による軽量モデル) |
| デバッグ | オンボード MCU-Link (CMSIS-DAP) / 外部 J-Link (SWD コネクタ経由)。NXP / PEmicro / SEGGER 各種プローブ対応 |

### MCUXpresso for VS Code (補足)

NXP は近年 **VS Code 拡張版** を主力として推進しており、Eclipse 版とほぼ同等の開発体験が得られます。

- インストール: VS Code から **NXPSemiconductors.mcuxpresso** 拡張を入れるだけ。依存する C/C++ 拡張も自動で導入される
- 対応 MCU: MCX (本ボード含む) / LPC / Kinetis / i.MX RT の Arm Cortex-M 全般
- プロジェクト形態: **MCUXpresso SDK** / **Zephyr** / **Matter** いずれでも開く事が可能
- 主機能: IntelliSense / ブレークポイント / 変数・レジスタ・メモリビュー / Disassembly / SWO / RTOS スレッド表示 / Heap・Stack 解析
- デバッガ: MCU-Link / PEmicro / SEGGER J-Link をプラグインで認識

> Eclipse の操作感が苦手な人は VS Code 版を選ぶのが現実的。Linux/macOS/Windows いずれもサポート。

### 代表的なサンプルアプリ
- `frdm_mcxc444_lcd_and_fxls8974cf_motion_detection` — 加速度センサ → 動き方向検出 → SLCD 表示
- `frdm_mcxc444_slcd_and_fxls8974` — Y 軸加速度を SLCD に数値表示、向きで RGB LED の色を変える
- MCUXpresso SDK 標準: GPIO・UART・I²C・SPI・ADC・USB CDC・低消費電力モード のリファレンス

## AI / 機械学習 の扱い

FRDM-MCXC444 は **AI 専用アクセラレータを持たない** Cortex-M0+ コア機です。ただし以下が可能です。

- **CMSIS-NN**(Arm の組込み NN ライブラリ)による Cortex-M 用最適化推論
- **TensorFlow Lite for Microcontrollers** で量子化された軽量モデル(数 KB〜数十 KB の MLP / 小規模 CNN)
- 現実的な用途: しきい値ベースの異常検知、加速度データの ML ベース姿勢分類、簡易キーワードスポッティング(モデルサイズと演算量の制約大)

> 本格的なエッジ AI(畳み込み・Transformer・キーワード認識など) を行う場合は、同 NXP の[FRDM-MCXN947](/maker_contest_2026/hardware/frdm-mcxn947/)(eIQ Neutron NPU 搭載) を選択するのが現実的です。

## 入手方法

- DigiKey JP: [FRDM-MCXC444](https://www.digikey.jp/ja/products/detail/nxp-usa-inc/FRDM-MCXC444/24374774) (¥1,750 前後)
- NXP 直販 / Mouser / Arrow Electronics などからも入手可

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。実際の開発では必ず[ユーザーマニュアル UM12120](https://docs.rs-online.com/00be/A700000012839604.pdf) で最新の仕様(ピン対応表・電気的定格・ジャンパ設定など)を確認してください。
