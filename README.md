# Team Subjective Highlights

Internal research kit comparing **winner-channel** vs **loser-channel** Premier League official highlight edits for the same fixtures (club-blind aggregate).

## Repo layout

| Path | Purpose |
|------|---------|
| `docs/methodology.md` | Tagging definitions, clip accounting, cordiality framing |
| `docs/results.md` | Narrative + paired summary tables |
| `docs/index.html` | Static dashboard (Chart.js) — open locally after refresh |
| `docs/stats.json` | Machine-readable aggregates |
| `scripts/build_stats.py` | Reads spreadsheet → writes `docs/stats.json` |
| `scripts/embed_stats_in_html.py` | Inlines JSON into `docs/index.html` for offline viewing |

## Refresh numbers after editing the workbook

Default spreadsheet path: `~/Downloads/pl_highlight_links_ENRICHED.xlsx`, or set:

```bash
export HIGHLIGHTS_XLSX=/path/to/pl_highlight_links_ENRICHED.xlsx
```

Then refresh aggregates and the offline HTML embed:

```bash
python3 scripts/build_stats.py && python3 scripts/embed_stats_in_html.py
```

Optional: copy the workbook to `data/pl_highlight_links_ENRICHED.xlsx` for a portable checkout.

## Dependencies

Python **3** with `pandas` + `openpyxl`:

```bash
pip install pandas openpyxl
```

## Viewing the HTML report

Open `docs/index.html` in a browser (stats are embedded after running `embed_stats_in_html.py`).

## Editing

All artifacts are plain Markdown/HTML/JavaScript—edit directly in Cursor.
