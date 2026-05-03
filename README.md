# Team Subjective Highlights

Internal research kit comparing **winner-channel** vs **loser-channel** Premier League official highlight edits for the same fixtures (club-blind aggregate).

**New chat / agent context:** see [`HANDOFF.md`](HANDOFF.md) (full, up-to-date project context for agents and collaborators).

**Live report (GitHub Pages):** [https://yotamkushnir.github.io/team-subjective-highlights/](https://yotamkushnir.github.io/team-subjective-highlights/)  
*First deploy can take 1–2 minutes; hard-refresh if charts look empty.*

**Repository:** [https://github.com/yotamkushnir/team-subjective-highlights](https://github.com/yotamkushnir/team-subjective-highlights)

## Repo layout

| Path | Purpose |
|------|---------|
| `docs/methodology.md` | Tagging definitions, clip accounting, cordiality framing |
| `docs/results.md` | Narrative + paired summary tables |
| `docs/index.html` | Static dashboard (Chart.js); includes inline collapsible “video editor” copy |
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

To change the collapsible editorial copy under **Executive summary**, edit the `<details class="card editorial-disclosure">` block in **`docs/index.html`** and push.

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
