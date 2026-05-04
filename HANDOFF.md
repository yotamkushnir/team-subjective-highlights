# Agent handoff — Team Subjective Highlights

Paste this file (or `@HANDOFF.md`) at the start of a **new** chat so an agent or collaborator aligns quickly with the **current** repo.

---

## What this project is

Research kit comparing **official Premier League match highlights** published on the **winner’s channel** vs the **loser’s channel** for the **same fixtures**.

**Headline analysis is club-blind:** we aggregate by **winner video vs loser video** (role in that match), not by club name or brand.

The **live dashboard** is a static Chart.js page on GitHub Pages. Charts read embedded JSON inside `docs/index.html`; there is no backend.

---

## URLs

| What | URL |
|------|-----|
| **Live report (GitHub Pages)** | https://yotamkushnir.github.io/team-subjective-highlights/ |
| **Git repository** | https://github.com/yotamkushnir/team-subjective-highlights |

After a push, Pages may take **1–2 minutes** to update; use a **hard refresh** if charts or copy look stale.

---

## Definitions that matter

- **Winner / loser** = which **channel’s video** (by match result). **Self / rival** = the two teams **as shown in that channel’s cut** (our side vs opponent).
- **Cordiality:** optional extra **rival** exposure (rival non-goal chances, rival reaction time, etc.) reads as **ceding space** in the **video**. **Celebration** and **reaction** are **not** opposites — both are persona dwell.
- **Replays** in the sheet are **counts** (how many angles), **not** seconds. **`rival_non_goal_replays`** remains in `stats.json` but is **not charted** on the dashboard (small _n_).
- **Avg PBP length** (narrative term for the sheet’s avg clip length) follows project rules: **total length minus final-whistle celebration**, divided by PBP count (`clip_count`) — see `docs/methodology.md` for full accounting. JSON keys stay **`avg_clip_length`**, **`clip_count`**.
- **Full tagging rules** and QA expectations: **`docs/methodology.md`**.
- **Written narrative / tables:** **`docs/results.md`** (may lag the HTML dashboard).

---

## Repo layout (what lives where)

| Path | Role |
|------|------|
| `docs/index.html` | **Dashboard:** Chart.js + embedded `const STATS = { ... }` + layout prose (hero, **Executive summary** with video-editor playbook + desk line, **Highlights from the data** `<details>`, figures, **Deep dive** `<details>`). |
| `docs/assets/wsc-theme.css` | **WSC design tokens** snapshot for GitHub Pages (synced from `vendor/wsc-components-library` — see below). |
| `vendor/wsc-components-library` | **Git submodule** — WSC component library / `wscTheme` source (`src/theme/wscTheme.ts`). |
| `docs/stats.json` | Machine-readable aggregates — output of `build_stats.py`. |
| `scripts/build_stats.py` | Reads enriched **Excel** → writes `docs/stats.json`. |
| `scripts/embed_stats_in_html.py` | Reads `docs/stats.json` → inlines into `docs/index.html` after `<!-- STATS_EMBED -->`. |
| `data/pl_highlight_links_ENRICHED.xlsx` | **Portable master workbook** (optional but recommended in-repo copy). See spreadsheet resolution below. |
| `docs/methodology.md` | Source of truth for metrics and tagging. |
| `docs/results.md` | Long-form results / paired tables. |
| `requirements.txt` | Python deps: `pandas`, `openpyxl` (for `build_stats.py`). |
| `README.md` | Short contributor-facing overview; points here for agents. |

**Static copy:** Executive playbook bullets, deep-dive prose, and section order live in **`docs/index.html`**. Data bullets under **Highlights from the data** are filled by JavaScript from `STATS`.

---

## Design system (`wsc-components-library`)

After clone, run **`git submodule update --init --recursive`** so `vendor/wsc-components-library` is populated.

- **Source of truth** for color/type: submodule `src/theme/wscTheme.ts`.
- **Published site** uses **`docs/assets/wsc-theme.css`** (same values; safe for GitHub Pages). When the library changes, update that file and bump the sync comment at the top.

---

## Spreadsheet resolution (`build_stats.py`)

The enriched workbook is resolved in this **order**:

1. Environment variable **`HIGHLIGHTS_XLSX`** (absolute or relative path), if set and the file exists.
2. **`data/pl_highlight_links_ENRICHED.xlsx`** at repo root.
3. **`~/Downloads/pl_highlight_links_ENRICHED.xlsx`**.

If none exist, the script exits with an error.

To add more matches for analysis: **append rows** to the master `.xlsx` using the same columns as the existing sheet (see `build_stats.py` for column names used in aggregates).

---

## Refresh workflow (numbers + deploy)

After changing the **workbook** or regenerating stats:

```bash
cd /path/to/team-subjective-highlights
python3 -m pip install -r requirements.txt   # if needed
python3 scripts/build_stats.py && python3 scripts/embed_stats_in_html.py
git add docs/stats.json docs/index.html
git commit -m "Refresh stats" && git push
```

- **`build_stats.py`** updates `docs/stats.json` only.
- **`embed_stats_in_html.py`** replaces the `const STATS = ...` block in **`docs/index.html`**. It does **not** rewrite other HTML.

**Copy-only (no data change):** edit **`docs/index.html`** (including `<details>` sections), then commit and push. No Python step required.

---

## Critical: embedded stats in `index.html`

The charts require **`const STATS = { ... }`** inside `docs/index.html` (after `<!-- STATS_EMBED -->`). If `STATS` is empty `{}`, the UI shows an error and **no real numbers**.

- A **fully embedded** `index.html` is **very large** (~1100+ lines) because JSON is inlined.
- If you see a **short** `index.html` and empty stats, the embed step was **not** run or the file on disk is stale — run `embed_stats_in_html.py` again.

---

## What `stats.json` encodes (high level)

Rows are **paired decisive fixtures** (`who won` ∈ {Home, Away}), with winner/loser columns coming from the sheet.

Paired aggregates include (among others):

- **Rival exposure:** `rival_non_goal_chances`, `rival_non_goal_replays` (replays not charted on dashboard)
- **Own-team optional PBPs:** `self_non_goal_chances`
- **Pacing / length:** `avg_clip_length`, `clip_count`, `total_length`
- **Score-adjusted persona** (normalize by goals / chance volume where relevant):
  - `self_celebration_per_goal`
  - `self_reaction_per_self_non_goal_chance`
  - `rival_reaction_per_rival_non_goal_chance`

Older keys may still appear in JSON for backward compatibility even if not every key is charted.

---

## Report structure in `index.html` (current)

1. Header + **What this is** (two videos per fixture; winner/loser vs self/rival) + **Role-based scope**.
2. **Executive summary** — subheader *How a video editor interprets the data*; **When we win / When we lose** bullets with nested `<details>`; **One-line takeaway for the desk**.
3. **Highlights from the data** (`<details>`) — % convention + JS-filled bullets from `STATS`.
4. Meta pill (fixture counts, source path).
5. **Figure 1** — Rival non-goal chances only (`rival_non_goal_replays` omitted from charts).
6. **Figure 2** — Self non-goal chances.
7. **Figure 3** — Pacing (avg PBP length + PBP count).
8. **Figure 4** — Total runtime.
9. **Figure 5** — Persona / emotion (score-adjusted charts).
10. **Deep dive context for future use** (`<details>`) — caveat, cordiality, what the study does not claim, metric definitions, exploratory notes, per-team warning, references.

Percent conventions for deltas are explained under **Highlights from the data**.

---

## Out of scope for the main claim

- **Per-club** views, **“big six”** opponent tiers, etc. — **small n**, exploratory only unless the tagging window grows.

---

## Maintainer note

Update **`HANDOFF.md`** when you change: metrics, figure order, spreadsheet filename/locations, embed scripts, design tokens, or anything agents must not get wrong about this repo.

---

*Last consolidated: dashboard restructure, `wsc-theme.css`, submodule `vendor/wsc-components-library`, rival replay suppressed in charts only.*
