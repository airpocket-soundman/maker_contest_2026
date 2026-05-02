---
title: DigiKey Make ONE Challenge 2026 推奨部品・ボード(NXP 以外)
short_title: 推奨部品(NXP 以外)
slug: digikey-recommended-parts
tagline: NXP 4 ボード以外に DigiKey が推奨する開発ボード・モジュール 9 種
manufacturer: 各社 (STMicroelectronics / Arduino / Raspberry Pi / Seeed / M5Stack / DFRobot)
category: 推奨部品セット (汎用開発ボード / センサ / モジュール)
official_url: https://www.digikey.jp/ja/resources/events/2026/make-one-challenge

features:
  - DigiKey Make ONE Challenge 2026 で「おすすめ製品」として紹介されている NXP 以外の 9 製品をまとめて掲載
  - BLE/Matter 対応 Discovery キット、Wi-Fi 内蔵マイコン、AI カメラ、環境センサ、ステッピングモータ駆動モジュールまで多彩
  - NXP 製品ほど一次審査加点が明示されていないが、DigiKey が推している製品群

specs:
  - label: 数
    value: 9 製品 (BLE/Wi-Fi 開発ボード、AI カメラ、ターミナル、環境センサ、モータドライバ等)
  - label: 共通条件
    value: いずれも DigiKey で取り扱いあり。Make ONE Challenge では DigiKey 製品の使用が必須。

resources:
  - name: DigiKey Make ONE Challenge 2026 公式ページ(おすすめ製品リスト)
    url: https://www.digikey.jp/ja/resources/events/2026/make-one-challenge
  - name: STM32WBA65I-DK1 (STMicroelectronics)
    url: https://www.st.com/en/evaluation-tools/stm32wba65i-dk1.html
  - name: Arduino UNO R4 WiFi (ABX00087)
    url: https://docs.arduino.cc/hardware/uno-r4-wifi/
  - name: Raspberry Pi Pico 2 H (SC1632)
    url: https://www.raspberrypi.com/products/raspberry-pi-pico-2/
  - name: Seeed XIAO ESP32S3 Sense (113991115)
    url: https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/
  - name: Seeed Wio Terminal (102991299)
    url: https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/
  - name: M5Stack Unit Cam (K147-CAM)
    url: https://docs.m5stack.com/en/unit/unit_cam
  - name: M5Stack Stepmotor Driver Module v1.1 (M039-V11)
    url: https://docs.m5stack.com/en/module/stepmotor13.2
  - name: DFRobot Beginner Kit for Arduino (DFR0100)
    url: https://wiki.dfrobot.com/dfr0100/
  - name: DFRobot FireBeetle 2 ESP32-E IoT (DFR0975-U)
    url: https://wiki.dfrobot.com/_SKU_DFR0975_FireBeetle_2_Board_ESP32_E_N16
  - name: DFRobot Gravity Multifunctional Environmental Sensor (SEN0501)
    url: https://wiki.dfrobot.com/SKU_SEN0501_Gravity_Multifunctional_Environmental_Sensor
---

## 概要

DigiKey Make ONE Challenge 2026 公式ページで「おすすめ製品」として紹介されているのは、加点対象の NXP 4 ボードに加え、以下の 9 製品です。BLE/Matter から Wi-Fi マイコン、AI カメラ、環境センサ、モータ制御まで、応募作品でよく使われる定番が揃っています。

## 製品一覧

### 1. STM32WBA65I-DK1 (STMicroelectronics)
- **DigiKey**: [STM32WBA65I-DK1 商品ページ](https://www.digikey.jp/ja/products/detail/stmicroelectronics/STM32WBA65I-DK1/26257424)
- **種別**: BLE 5.4 / 802.15.4 / Zigbee / Thread / Matter 対応 Discovery キット
- **MCU**: STM32WBA65RIV7 (Arm Cortex-M33 + Arm TrustZone, 100MHz, Flash 2MB / SRAM 512KB)
- **無線**: Bluetooth LE 5.4 / IEEE 802.15.4-2015 (Thread / Zigbee / Matter)
- **拡張**: Arduino UNO V3 互換ヘッダ
- **デバッガ**: STLINK-V3EC オンボード搭載
- **開発環境**: STM32CubeIDE / STM32CubeMX / Keil MDK / IAR EWARM / Zephyr
- **用途例**: Matter 対応スマートホーム、低電力 BLE センサ、Thread メッシュノード

### 2. Arduino UNO R4 WiFi (ABX00087)
- **DigiKey**: [ABX00087 商品ページ](https://www.digikey.jp/ja/products/detail/arduino/ABX00087/20371539)
- **種別**: Arduino UNO 互換 + Wi-Fi/BLE 拡張ボード
- **MCU**: Renesas RA4M1 (Arm Cortex-M4, 48MHz, Flash 256KB / SRAM 32KB)
- **無線**: ESP32-S3 モジュール経由で Wi-Fi 4 / Bluetooth LE
- **特徴**: 12×8 LED マトリクス内蔵、CAN/SPI/I²C/UART、Qwiic コネクタ対応
- **開発環境**: Arduino IDE / Arduino CLI / PlatformIO / MicroPython
- **用途例**: 入門〜中級レベルの IoT・センサ・LED アート工作

### 3. Raspberry Pi Pico 2 H (SC1632)
- **DigiKey**: [SC1632 商品ページ](https://www.digikey.jp/ja/products/detail/raspberry-pi/SC1632/26241102)
- **種別**: ピンヘッダ実装済み (H = Headers) の RP2350 ボード
- **MCU**: RP2350 (デュアル Arm Cortex-M33 もしくは デュアル RISC-V Hazard3、150MHz)
- **メモリ**: SRAM 520KB / 外付け QSPI Flash 4MB
- **特徴**: 安価・コンパクト、26 GPIO、ADC×4、PIO ステートマシン×12
- **開発環境**: Raspberry Pi Pico SDK (C/C++) / Arduino IDE / MicroPython / CircuitPython / Rust (rp-hal)
- **用途例**: 低コストのセンサ収集、PIO を活用したカスタム I/O、教育用途

### 4. Seeed XIAO ESP32S3 Sense (113991115)
- **DigiKey**: [113991115 商品ページ](https://www.digikey.jp/ja/products/detail/seeed-technology-co-ltd/113991115/18724504)
- **種別**: 小型 (21×17.5mm) AI カメラ ボードキット
- **MCU**: ESP32-S3 (Xtensa デュアルコア, Wi-Fi 4 + BLE 5.0)
- **メモリ**: PSRAM 8MB / Flash 8MB
- **センサ**: OV2640 カメラ + デジタルマイク内蔵 (キット時)
- **電源**: USB-C / バッテリー充電回路あり、U.FL アンテナ同梱
- **開発環境**: Arduino IDE / ESP-IDF / PlatformIO / MicroPython / Edge Impulse
- **用途例**: 組込み画像認識・音声認識、ウェアラブル AI

### 5. Seeed Wio Terminal (102991299)
- **DigiKey**: [102991299 商品ページ](https://www.digikey.jp/ja/products/detail/seeed-technology-co-ltd/102991299/11689373)
- **種別**: LCD・ボタン・ジョイスティック付き Arduino 互換ターミナル
- **MCU**: Microchip ATSAMD51 (Arm Cortex-M4F, 120MHz)
- **無線**: Realtek RTL8720DN 経由で Wi-Fi + Bluetooth
- **ディスプレイ**: 320×240 LCD 内蔵、3 ボタン、5 方向ジョイスティック、各種センサ(IMU/光/マイク)、Grove I²C/UART ポート
- **開発環境**: Arduino IDE / ArduPy (MicroPython) / PlatformIO / Mbed
- **用途例**: スタンドアロンの IoT ガジェット、教育用ハンドヘルド

### 6. M5Stack Unit Cam (K147-CAM / AtomS3R Cam)
- **DigiKey**: [K147-CAM 商品ページ](https://www.digikey.jp/ja/products/detail/m5stack-technology-co-ltd/K147-CAM/26772241)
- **種別**: AtomS3R をベースとした AI カメラ Unit
- **MCU**: ESP32-S3 (Xtensa デュアルコア, Wi-Fi/BLE)
- **カメラ**: 内蔵カメラセンサ
- **接続**: Grove インターフェース / USB-C
- **開発環境**: Arduino IDE / UIFlow (M5Stack ビジュアル) / ESP-IDF / PlatformIO
- **用途例**: 軽量画像認識、QR コード読取、監視カメラ

### 7. M5Stack Stepmotor Driver Module v1.1 (M039-V11)
- **DigiKey**: [M039-V11 を DigiKey で検索](https://www.digikey.jp/ja/products/result?keywords=M039-V11)
- **種別**: M5Core 用ステッピングモータ駆動モジュール
- **構成**: STM32 + HR8825 ×3 (3 軸独立 / 連動制御)、リミットスイッチ 4 入力対応
- **電流**: ドライバごとに調整可、マイクロステッピング対応
- **開発環境**: Arduino IDE / UIFlow / PlatformIO (M5Core 用ライブラリ経由)
- **用途例**: 3 軸 CNC・3D プリンタ・自動装置のプロトタイプ

### 8. DFRobot Beginner Kit for Arduino (DFR0100)
- **DigiKey**: [DFR0100 商品ページ](https://www.digikey.jp/ja/products/detail/dfrobot/DFR0100/6579320)
- **種別**: Arduino UNO R3 互換ボードを中心にした入門学習キット
- **構成**: DFRduino UNO R3 + プロトタイプシールド + センサ・アクチュエータ・抵抗・ジャンパ等
- **開発環境**: Arduino IDE / PlatformIO
- **用途例**: 初学者向けプロトタイピング、ワークショップ

### 9. DFRobot FireBeetle 2 ESP32-E IoT (DFR0975-U)
- **DigiKey**: [DFR0975-U 商品ページ](https://www.digikey.jp/ja/products/detail/dfrobot/DFR0975-U/20500161)
- **種別**: 低消費電力 ESP32 系 IoT ボード (FireBeetle シリーズ)
- **MCU**: ESP32-E (Xtensa デュアルコア, Wi-Fi + Bluetooth)
- **電源**: 5V USB / リチウム電池ソケット
- **特徴**: スリープ時 13µA、IoT 向け省電力設計
- **開発環境**: Arduino IDE / ESP-IDF / MicroPython / PlatformIO
- **用途例**: バッテリ駆動 IoT センサノード、屋外モニタ

### 10. DFRobot Gravity 多機能環境センサ (SEN0501)
- **DigiKey**: [SEN0501 商品ページ](https://www.digikey.jp/ja/products/detail/dfrobot/SEN0501/18069231)
- **種別**: I²C/UART 接続の環境センサモジュール
- **計測項目**: 温度 (SHTC3) / 湿度 (SHTC3) / 気圧 (BMP280) / 環境光 (VEML7700) / UV (LTR390)
- **電源**: 3.3〜5V DC
- **サイズ**: 32×32 mm
- **対応マイコン**: 任意の I²C/UART マスタ (Arduino / ESP32 / STM32 / RP2040 / NXP MCU 等)
- **用途例**: 屋内・屋外環境ロガー、データ可視化、農業 IoT

## 共通の開発環境ヒント

| ボード/モジュール種別 | 主な選択肢 |
|---|---|
| ESP32 系 (XIAO ESP32S3 / Wio Terminal / FireBeetle / M5Stack) | Arduino IDE / ESP-IDF / PlatformIO / MicroPython / Edge Impulse |
| Arduino UNO R4 WiFi | Arduino IDE / PlatformIO / MicroPython |
| Raspberry Pi Pico 2 | Pico SDK (C/C++) / Arduino IDE / MicroPython / CircuitPython / Rust |
| STM32 (WBA65) | STM32CubeIDE / STM32CubeMX / Keil MDK / IAR / Zephyr |
| センサ単体 (SEN0501 等) | 任意のホスト MCU で I²C/UART ライブラリを使う |

> ⚠️ 本ページは公開情報をもとにまとめた参考情報です。各製品の最新仕様・在庫は[DigiKey 公式](https://www.digikey.jp/)および各メーカーのサイトで確認してください。
