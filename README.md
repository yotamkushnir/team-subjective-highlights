# Team Subjective Highlights

Internal research kit comparing **winner-channel** vs **loser-channel** Premier League official highlight **videos** for the same fixtures (club-blind aggregate).

**New chat / agent context:** see [`HANDOFF.md`](HANDOFF.md) (full, up-to-date project context for agents and collaborators).

**Live report (GitHub Pages):** [https://yotamkushnir.github.io/team-subjective-highlights/](https://yotamkushnir.github.io/team-subjective-highlights/)  
*First deploy can take 1–2 minutes; hard-refresh if charts look empty.*

**Repository:** [https://github.com/yotamkushnir/team-subjective-highlights](https://github.com/yotamkushnir/team-subjective-highlights)

## Design system

This repo vendors [**wsc-components-library**](https://github.com/WSCSportsEngineering/wsc-components-library) as a **git submodule** at `vendor/wsc-components-library`. After cloning, run:

```bash
git submodule update --init --recursive
```

The static dashboard loads approved tokens from **`docs/assets/wsc-theme.css`** (synced from the library’s `wscTheme` — see the comment at the top of that file). Refresh that snapshot when design tokens change upstream.

## Repo layout

| Path | Purpose |
|------|---------|
| `docs/methodology.md` | Tagging definitions, PBP accounting, cordiality framing |
| `docs/results.md` | Narrative + paired summary tables |
| `docs/index.html` | Static dashboard (Chart.js); executive playbook, highlights, figures, deep dive |
| `docs/assets/wsc-theme.css` | WSC palette + semantic aliases for the dashboard |
| `docs/stats.json` | Machine-readable aggregates |
| `scripts/build_stats.py` | Reads spreadsheet → writes `docs/stats.json` |
| `scripts/embed_stats_in_html.py` | Inlines `stats.json` into `docs/index.html` |

## Refresh numbers after editing the workbook

Default spreadsheet path: `~/Downloads/pl_highlight_links_ENRICHED.xlsx`, or set:

```bash
export HIGHLIGHTS_XLSX=/path/to/pl_highlight_links_ENRICHED.xlsx
```

Then refresh aggregates and embed stats into `docs/index.html`:

```bash
python3 scripts/build_stats.py && python3 scripts/embed_stats_in_html.py
```

To change narrative blocks (executive playbook, deep dive, etc.), edit the corresponding sections in **`docs/index.html`** and push.

Optional: copy the workbook to `data/pl_highlight_links_ENRICHED.xlsx` for a portable checkout.

## Dependencies

Python **3**. Install from the repo root:

```bash
python3 -m pip install -r requirements.txt
```

(`pandas` and `openpyxl`.)

## Viewing the HTML report

Open `docs/index.html` in a browser after running `embed_stats_in_html.py`.

## Editing

All artifacts are plain Markdown/HTML/JavaScript—edit directly in Cursor.
