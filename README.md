# Team Subjective Highlights

Internal research kit comparing **winner-channel** vs **loser-channel** Premier League official highlight edits for the same fixtures (club-blind aggregate).

**New chat / agent context:** see [`HANDOFF.md`](HANDOFF.md).

**Live report (GitHub Pages):** [https://yotamkushnir.github.io/team-subjective-highlights/](https://yotamkushnir.github.io/team-subjective-highlights/)  
*First deploy can take 1–2 minutes; hard-refresh if charts look empty.*

**Repository:** [https://github.com/yotamkushnir/team-subjective-highlights](https://github.com/yotamkushnir/team-subjective-highlights)

## Repo layout

| Path | Purpose |
|------|---------|
| `docs/methodology.md` | Tagging definitions, clip accounting, cordiality framing |
| `docs/results.md` | Narrative + paired summary tables |
| `docs/editorial-playbook.md` | Plain-English editing/social takeaways (winner vs loser cuts) |
| `docs/index.html` | Static dashboard (Chart.js) — open locally after refresh |
| `docs/stats.json` | Machine-readable aggregates |
| `scripts/build_stats.py` | Reads spreadsheet → writes `docs/stats.json` |
| `scripts/embed_stats_in_html.py` | Inlines `stats.json` and `editorial-playbook.md` into `docs/index.html` |
| `scripts/embed_docs.py` | Same end result as `embed_stats_in_html.py` (convenience alias) |

## Refresh the report (numbers and/or editorial copy)

Default spreadsheet path: `~/Downloads/pl_highlight_links_ENRICHED.xlsx`, or set:

```bash
export HIGHLIGHTS_XLSX=/path/to/pl_highlight_links_ENRICHED.xlsx
```

Then rebuild aggregates and embed everything into `docs/index.html` (**stats + editorial playbook**):

```bash
python3 scripts/build_stats.py && python3 scripts/embed_stats_in_html.py
```

Edit **`docs/editorial-playbook.md`** for the collapsible “video editor” interpretation; run **`python3 scripts/embed_stats_in_html.py`** afterward (no spreadsheet step needed).

Optional: copy the workbook to `data/pl_highlight_links_ENRICHED.xlsx` for a portable checkout.

## Dependencies

Python **3**. Install from the repo root:

```bash
python3 -m pip install -r requirements.txt
```

(`pandas`, `openpyxl`, `markdown` — the last one renders the editorial playbook into HTML.)

## Viewing the HTML report

Open `docs/index.html` in a browser after running `embed_stats_in_html.py`.

## Editing

All artifacts are plain Markdown/HTML/JavaScript—edit directly in Cursor.
