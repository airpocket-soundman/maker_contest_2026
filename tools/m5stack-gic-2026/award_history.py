"""Render the historical M5Stack contest award data as a reusable HTML section."""
import html
import json
from pathlib import Path


DATA_PATH = Path(__file__).with_name("award_history.json")


def render_award_history(data_path=DATA_PATH):
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    summary = data["summary"]

    annual_rows = []
    for row in data["annual"]:
        awarded = row["awarded_projects"]
        entries = row["entries"]
        if awarded is not None and entries:
            rate = f"{awarded / entries * 100:.1f}%"
        elif row["year"] == 2026:
            rate = "発表待ち"
        else:
            rate = "—"
        annual_rows.append(
            f'<tr><td>{row["year"]}</td><td>{awarded if awarded is not None else "—"}</td>'
            f'<td>{entries if entries is not None else "—"}</td><td>{rate}</td></tr>'
        )

    repeat_rows = "".join(
        f'<tr><td style="text-align:left">{html.escape(row["name"])}</td><td>{row["awards"]}</td></tr>'
        for row in data["repeat_winners"]
    )

    yearly_details = []
    for year, awards in data["history"].items():
        rows = "".join(
            '<tr><td style="text-align:left">{}</td><td style="text-align:left">{}</td></tr>'.format(
                html.escape(award["award"]),
                "、".join(html.escape(winner) for winner in award["winners"]),
            )
            for award in awards
        )
        yearly_details.append(
            f'<details><summary>{year}年の受賞履歴</summary>'
            f'<div class="scroll"><table style="width:100%;margin-top:8px">'
            f'<thead><tr><th>賞</th><th style="text-align:left">受賞者・チーム</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div></details>'
        )

    return f'''<!-- AWARD_HISTORY_START -->
<section id="past-awards">
<h2>過去大会の受賞履歴と集計</h2>
<p class="sub">2020〜2025年の受賞結果を集計。2026年は受賞者発表前のため、エントリー数のみ掲載しています。</p>
<div class="tiles">
  <div class="tile"><div class="v">{summary['awarded_projects']}</div><div class="k">受賞作品数（2020〜2025）</div></div>
  <div class="tile"><div class="v">{summary['winners']}</div><div class="k">受賞者・チーム数</div></div>
  <div class="tile"><div class="v">{summary['max_awards']}</div><div class="k">最多受賞回数</div></div>
  <div class="tile"><div class="v">{summary['max_consecutive_years']}</div><div class="k">最長連続受賞年数</div></div>
  <div class="tile"><div class="v">{summary['max_same_year_projects']}</div><div class="k">同一年の最多受賞作品数</div></div>
</div>
<div class="pair" style="margin-top:12px;align-items:start">
  <div class="scroll"><table style="width:100%">
    <thead><tr><th>年</th><th>受賞作品数</th><th>エントリー数</th><th>受賞作品率</th></tr></thead>
    <tbody>{''.join(annual_rows)}</tbody>
  </table></div>
  <div><h3 class="mh" style="margin-top:0">複数回受賞者・チーム（2回以上）</h3>
    <div class="scroll"><table style="width:100%;margin-top:8px">
      <thead><tr><th style="text-align:left">受賞者・チーム</th><th>受賞回数</th></tr></thead>
      <tbody>{repeat_rows}</tbody>
    </table></div>
  </div>
</div>
<div style="margin-top:10px">{''.join(yearly_details)}</div>
<p class="sub" style="margin-top:10px">※ 表記と集計単位は提供された受賞履歴に準拠しています。同一人物・チームでも表記が異なる場合は別名として扱い、共同受賞では受賞者数と受賞作品数が一致しないことがあります。</p>
</section>
<!-- AWARD_HISTORY_END -->'''


if __name__ == "__main__":
    print(render_award_history())
