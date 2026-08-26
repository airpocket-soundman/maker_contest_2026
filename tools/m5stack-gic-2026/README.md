# M5Stack Global Innovation Contest 2026 — 分析パイプライン

Hackster.io のコンテストカテゴリ(category_id=595)からエントリー作品を収集し、
サマリページ(`/gic2026-entries/`)を生成する一連のスクリプトです。

## 公開ページと保護について

- 公開ページ: `gic2026-entries/index.html`
  - 個人利用目的のため、`encrypt_page.py` により AES-256-GCM で暗号化されています
    (PBKDF2-HMAC-SHA256 250,000回、WebCrypto でブラウザ内復号)。
  - パスワードはページ管理者のみが保持します(リポジトリには含まれません)。
- パスワード不要版: `gic2026-list/index.html`
  - 作品画像、Gist連携、チェック欄・メモ欄を除いた公開用ページです。
- 過去大会の受賞履歴: `award_history.json`
  - `award_history.py` が年度別集計、複数回受賞者、2020〜2025年の受賞一覧を両ページ共通のHTMLへ変換します。
- 収集データ一式: `data/m5stack-gic-2026-data.enc`
  - `gic_data.tar.gz` を同じ方式・同じパスワードで暗号化したもの。
  - 復号: `python decrypt_data.py <password> ../../data/m5stack-gic-2026-data.enc gic_data.tar.gz`

## パイプライン構成

| スクリプト | 役割 |
|---|---|
| `build_merged.py` | 作品サマリ・画像・ライセンス・投稿者情報を統合し `merged2.json` を生成 |
| `stats.py` | 日別/累積投稿数、所在国別の集計(`stats.json`) |
| `parse_parts.py` | 各作品の「Things used in this project」欄をパース(`parts.json`) |
| `aggregate_tech.py` | コアデバイス・部品カテゴリ・開発環境・技術キーワードの集計(`tech_agg.json`) |
| `predict2.py` | 最終投稿数予測(Opus 5)。2025年大会実績で較正 |
| `predict_fable.py` | 最終投稿数予測(Fable 5)+ Codex 用入力データ生成 |
| `forecast_chart.py` | 予測セクション(3モデル比較)のHTML片を生成 |
| `extract_authors.py` | Hacksterプロフィールから投稿者名・所在国を抽出 |
| `build_html.py` | 最終的なHTMLページとMarkdownを生成 |
| `encrypt_page.py` | 生成したページをパスワード付きページに変換 |
| `award_history.py` | 過去大会の受賞履歴JSONから共通HTMLセクションを生成 |

実行順: `build_merged.py` → `stats.py` → `parse_parts.py` → `aggregate_tech.py` →
`forecast_chart.py` → `build_html.py` → `encrypt_page.py`

必要パッケージ: Python 3.12+, `cryptography`(暗号化のみ)

※ 収集元HTML(作品ページ・プロフィールのキャッシュ、約45MB)はリポジトリに含めていません。
スクリプトはキャッシュディレクトリ(`pages*/`, `profiles/`)がある作業ディレクトリで動く前提です。
