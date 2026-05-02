# 2026年メイカー向けコンテスト情報まとめ

2026年に開催されるメイカー(電子工作・ものづくり)向けコンテストのレギュレーション、エントリー方法、賞金、使用ハードウェアなどを統一フォーマットでまとめたサイトのソースリポジトリです。

GitHub Pages で公開しています。

## ディレクトリ構成

```
.
├── _config.yml              # Jekyll設定
├── index.md                 # トップページ(コンテスト・ハードウェア一覧)
├── _layouts/                # 共通HTMLテンプレート
│   ├── default.html         # サイト全体の枠
│   ├── contest.html         # コンテストページ用
│   └── hardware.html        # ハードウェアページ用
├── _contests/               # 各コンテストの情報(Jekyll Collection)
│   ├── rohm-edge-hack-challenge-2026.md
│   └── digikey-make-one-challenge-2026.md
├── _hardware/               # 各ハードウェアの情報(Jekyll Collection)
│   ├── solist-ai.md
│   └── nxp-eval-boards.md
├── assets/
│   └── style.css            # スタイルシート
└── README.md                # このファイル
```

## 新しいコンテストを追加する手順

1. `_contests/<コンテスト識別子>.md` を新規作成
2. ファイル先頭の YAML Front Matter に以下の項目を埋める:
   - `title`: コンテスト名
   - `tagline`: 一行のキャッチコピー(任意)
   - `organizer`: 主催者
   - `cosponsors`: 協賛・協力(任意、リスト)
   - `official_url`: 公式サイトURL
   - `target_audience`: 対象者
   - `submission_format`: 提出物の形式
   - `entry_period`: `start` / `end` / `note`
   - `schedule`: `date` / `event` のリスト
   - `judges`: 審査員(`name` / `affiliation` / `role` のオブジェクト、または文字列)
   - `criteria`: 審査基準(リスト)
   - `regulations`: レギュレーション・応募条件(リスト)
   - `prizes`: 賞金(`name` / `amount` / `description` のリスト)
   - `hardware`: 使用ハードウェア(`name` / `slug` / `required` / `recommended` / `note`)
3. ハードウェアの `slug` は `_hardware/<slug>.md` のスラッグと一致させること(自動でリンクが張られる)

既存ファイルを雛形としてコピーするのが最も簡単です。

## 新しいハードウェアを追加する手順

1. `_hardware/<ハードウェア識別子>.md` を新規作成
2. Front Matter に以下を埋める:
   - `title`: 製品名
   - `slug`: コンテスト側からの参照に使うID(ファイル名と一致させる)
   - `manufacturer`: メーカー
   - `category`: カテゴリ
   - `official_url`: 公式ページ
   - `features`: 特徴(リスト)
   - `specs`: 主要スペック(`label` / `value`)
   - `resources`: 関連リソース(`name` / `url` / `note`)

## ローカルで確認する方法

Ruby と Bundler が必要です。

```bash
# 初回のみ
gem install bundler jekyll

# プロジェクト直下で
jekyll serve --baseurl ""
```

ブラウザで `http://localhost:4000/` を開いて確認できます。

## GitHub Pages での公開設定

1. リポジトリの **Settings** → **Pages** を開く
2. **Build and deployment** の **Source** で `Deploy from a branch` を選択
3. **Branch** で `main` / `/ (root)` を指定して **Save**
4. 数分待って `https://airpocket-soundman.github.io/maker_contest_2026/` にアクセス

> `_config.yml` の `baseurl` はリポジトリ名と一致させてください(現在は `/maker_contest_2026`)。
> リポジトリ名を変えた場合は `_config.yml` の `baseurl` と `url` も合わせて更新が必要です。

## 注意事項

本サイトの内容は公開情報をもとに個人がまとめた**非公式の情報**です。応募の際は必ず各コンテストの公式サイトで最新情報をご確認ください。
