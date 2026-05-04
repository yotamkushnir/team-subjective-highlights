# Team Subjective Highlights

Internal research kit comparing **winner-channel** vs **loser-channel** Premier League official highlight **videos** for the same fixtures (club-blind aggregate).

**New chat / agent context:** see [`HANDOFF.md`](HANDOFF.md).

**Live report (GitHub Pages):** [https://yotamkushnir.github.io/team-subjective-highlights/](https://yotamkushnir.github.io/team-subjective-highlights/)  
*After `git push`, wait 1–2 minutes and hard-refresh if the site looks stale.*

**Repository:** [https://github.com/yotamkushnir/team-subjective-highlights](https://github.com/yotamkushnir/team-subjective-highlights)

---

## Quick start (clone + stats)

```bash
git clone https://github.com/yotamkushnir/team-subjective-highlights.git
cd team-subjective-highlights
git submodule update --init --recursive
python3 -m pip install -r requirements.txt
export HIGHLIGHTS_XLSX=/path/to/pl_highlight_links_ENRICHED.xlsx   # optional
python3 scripts/build_stats.py && python3 scripts/embed_stats_in_html.py
```

Open **`docs/index.html`** in a browser.

---

## Design system

Submodule: **`vendor/wsc-components-library`** ([WSCSportsEngineering/wsc-components-library](https://github.com/WSCSportsEngineering/wsc-components-library)). After clone:

```bash
git submodule update --init --recursive
```

Published styling is **`docs/assets/wsc-theme.css`** (synced from `wscTheme` — see file header).

---

## Data & naming (PBP)

The workbook may use **PBP** column labels (e.g. `winner amount of total pbps`, `winner average pbp lenght`) or **legacy** “clip” labels. `scripts/build_stats.py` resolves either.

Aggregates in **`docs/stats.json`** / embedded **`STATS`** use **`avg_pbp_length`**, **`pbp_count`**, **`persona_sec_per_pbp`**, etc. Tagging rules: **`docs/methodology.md`**.

---

## Repo layout

| Path | Purpose |
|------|---------|
| `docs/index.html` | Static dashboard (Chart.js + embedded stats) |
| `docs/assets/wsc-theme.css` | Design tokens for the dashboard |
| `docs/assets/wsc-mark-white.svg` | Header logo |
| `docs/stats.json` | Aggregates from `build_stats.py` |
| `scripts/build_stats.py` | Spreadsheet → `stats.json` |
| `scripts/embed_stats_in_html.py` | Inline stats into `index.html` |
| `docs/methodology.md` | Definitions & QA |
| `docs/results.md` | Narrative + tables |

---

## Publish updates to GitHub Pages

```bash
git add -A
git status   # review
git commit -m "Your message"
git push origin main
```

Include **`docs/index.html`** and **`docs/stats.json`** whenever you rerun the embed step after changing numbers.

---

## Dependencies

Python **3** + `pandas`, `openpyxl` (`requirements.txt`).

---

## Editing

Markdown/HTML/JS in-repo; no build step except stats embed for numbers.
