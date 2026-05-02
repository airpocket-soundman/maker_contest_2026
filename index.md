---
layout: default
title: トップ
---

# 2026年メイカー向けコンテスト情報まとめ

2026年に開催されるメイカー(電子工作・ものづくり)向けコンテストのレギュレーション、エントリー方法、賞金、使用ハードウェアなどを統一フォーマットでまとめています。

> **注意**: 本サイトは個人が公開情報をまとめた非公式サイトです。応募の際は必ず各コンテストの公式サイトで最新情報をご確認ください。

## <span id="contests">コンテスト一覧</span>

<table class="index-table">
  <thead>
    <tr>
      <th>コンテスト名</th>
      <th>主催</th>
      <th>エントリー期間</th>
      <th>最大賞金</th>
    </tr>
  </thead>
  <tbody>
    {% assign sorted_contests = site.contests | sort: 'entry_period.start' %}
    {% for c in sorted_contests %}
      <tr>
        <td><a href="{{ c.url | relative_url }}">{{ c.title }}</a></td>
        <td>{{ c.organizer }}</td>
        <td>
          {% if c.entry_period.start %}{{ c.entry_period.start }}{% endif %}
          {% if c.entry_period.end %} 〜 {{ c.entry_period.end }}{% endif %}
        </td>
        <td>
          {% if c.prizes and c.prizes[0].amount %}{{ c.prizes[0].amount }}{% else %}-{% endif %}
        </td>
      </tr>
    {% endfor %}
  </tbody>
</table>

使用ハードウェアおよび開発フレームワークの一覧は、各コンテストページの「使用ハードウェア」欄を参照してください(コンテストごとに対象が異なります)。
