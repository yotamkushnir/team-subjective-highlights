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

- **Winner / loser** = which **channel’s video** (by match result). The intro under the title states the **club-blind** rule (no brand names in the headline claim).
- **Cordiality:** optional extra **rival** exposure (rival non-goal chances, rival reaction time, etc.) reads as **ceding space** in the **video**. **Celebration** and **reaction** are **not** opposites — both are persona dwell.
- **Replays** in the sheet are **counts** (how many angles), **not** seconds. **`rival_non_goal_replays`** remains in `stats.json` but is **not charted** on the dashboard (small _n_).
- **PBP** = play-by-play. The spreadsheet may use **PBP** column names (e.g. `winner amount of total pbps`, `winner average pbp lenght`) or **legacy** “clip” names; `build_stats.py` resolves either via `pick_col()`. JSON keys: **`avg_pbp_length`**, **`pbp_count`**, **`persona_sec_per_pbp`**, etc. — see `docs/stats.json`.
- **Full tagging rules** and QA expectations: **`docs/methodology.md`**.
- **Written narrative / tables:** **`docs/results.md`** (may lag the HTML dashboard).

---

## Repo layout (what lives where)

| Path | Role |
|------|------|
| `docs/index.html` | **Dashboard:** Chart.js + embedded `const STATS = { ... }` + layout (header + lead, **Executive summary** with white “When we win/lose…” section titles and yellow collapsible rows, **Highlights from the data**, figures, **Deep dive** in topic cards). |
| `docs/assets/wsc-theme.css` | **WSC design tokens** for Pages (yellow accent; chart fills = light yellow / light orange 100; logo loads from `assets/` with GitHub Pages URL fallback on error). |
| `vendor/wsc-components-library` | **Git submodule** — `wscTheme` source (`src/theme/wscTheme.ts`). |
| `docs/stats.json` | Machine-readable aggregates — output of `build_stats.py`. |
| `scripts/build_stats.py` | Reads enriched **Excel** → writes `docs/stats.json` (PBP column aliases supported). |
| `scripts/embed_stats_in_html.py` | Reads `docs/stats.json` → inlines into `docs/index.html` after `<!-- STATS_EMBED -->`. |
| `data/pl_highlight_links_ENRICHED.xlsx` | **Portable master workbook** (optional). See spreadsheet resolution below. |
| `docs/methodology.md` | Source of truth for metrics and tagging. |
| `docs/results.md` | Long-form results / paired tables. |
| `requirements.txt` | Python deps: `pandas`, `openpyxl`. |
| `README.md` | Short contributor-facing overview. |

**Static copy:** Executive playbook, deep-dive prose, and section order live in **`docs/index.html`**. Data bullets under **Highlights from the data** are filled by JavaScript from `STATS`.

---

## Visual / UX (current dashboard)

- **Accent:** WSC **yellow** (`--primary-300`, etc.) for links, tags, figure titles, collapsible summaries.
- **Executive block:** Section lines **“When we win…” / “When we lose…”** are **white**; each **row label** (e.g. “Breathe more.”) is the `<details>` summary and stays **yellow**.
- **Charts:** **Winner** series ≈ **light yellow 100**, **Loser** series ≈ **light orange 100** (from `wsc-theme.css`), with a thin dark bar outline.
- **Logo:** `assets/wsc-mark-white.svg` — if a relative path fails on Pages, `onerror` falls back to the absolute `github.io` asset URL.

---

## Design system (`wsc-components-library`)

After clone, run **`git submodule update --init --recursive`** so `vendor/wsc-components-library` is populated.

- **Source of truth** for color/type: submodule `src/theme/wscTheme.ts`.
- **Published site** uses **`docs/assets/wsc-theme.css`**. When the library changes, update that file and bump the sync comment at the top.

---

## Spreadsheet resolution (`build_stats.py`)

The enriched workbook is resolved in this **order**:

1. Environment variable **`HIGHLIGHTS_XLSX`** (absolute or relative path), if set and the file exists.
2. **`data/pl_highlight_links_ENRICHED.xlsx`** at repo root.
3. **`~/Downloads/pl_highlight_links_ENRICHED.xlsx`**.

If none exist, the script exits with an error.

To add more matches: **append rows** using the same columns as the existing sheet. For **PBP** naming, prefer columns such as `winner amount of total pbps` / `winner average pbp lenght` (see `pick_col` calls in `build_stats.py`); legacy “clip” column names still work.

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

- **`build_stats.py`** updates **`docs/stats.json`** only.
- **`embed_stats_in_html.py`** replaces the `const STATS = ...` block in **`docs/index.html`**.

**Copy-only:** edit **`docs/index.html`**, then commit and push (no Python).

---

## Publish to GitHub / Pages

Local commits are not live until pushed:

```bash
git push origin main
```

If you use submodules, fresh clones need:

```bash
git submodule update --init --recursive
```

---

## Critical: embedded stats in `index.html`

The charts require **`const STATS = { ... }`** inside `docs/index.html` (after `<!-- STATS_EMBED -->`). If `STATS` is empty `{}`, the UI shows an error and **no real numbers**.

- A **fully embedded** `index.html` is **very large** because JSON is inlined.
- If stats look empty, run **`embed_stats_in_html.py`** again after **`build_stats.py`**.

---

## What `stats.json` encodes (high level)

Rows are **paired decisive fixtures** (`who won` ∈ {Home, Away}).

Paired aggregates include (among others):

- **Rival exposure:** `rival_non_goal_chances`, `rival_non_goal_replays` (replays not charted on dashboard)
- **Own-team optional PBPs:** `self_non_goal_chances`
- **Pacing / length:** `avg_pbp_length`, `pbp_count`, `total_length`
- **Persona:** `persona_total_sec`, `persona_share_of_runtime`, `persona_sec_per_pbp`, `rival_persona_sec`
- **Score-adjusted:** `self_celebration_per_goal`, `self_reaction_per_self_non_goal_chance`, `rival_reaction_per_rival_non_goal_chance`

---

## Report structure in `index.html` (current)

1. **Header** — logo, tag, **H1**, one **lead** paragraph (club-blind scope).
2. **Executive summary** — *How a video editor interprets the data*; **When we win / When we lose** (white headings); yellow collapsible rows; **One-line takeaway for the desk**.
3. **Highlights from the data** (`<details>`) — % convention + JS bullets from `STATS`.
4. Meta pill (fixtures, matchweeks, source path).
5. **Figures 1–5** — rival chances; self NG chances; pacing; runtime; persona (score-adjusted).
6. **Deep dive** (`<details>`) — **cards by topic:** (a) caveat + cordiality + what the study does not claim, (b) what each metric means, (c) later/exploratory + before per-team view, (d) references.

Percent conventions sit under **Highlights from the data**.

---

## Out of scope for the main claim

- **Per-club** views, **“big six”** opponent tiers, etc. — **small n**, exploratory only unless the tagging window grows.

---

## Maintainer note

Update **`HANDOFF.md`** when you change metrics, figure order, spreadsheet paths, embed scripts, tokens, or agent-critical behavior.

---

*Last consolidated: yellow/orange chart series, white exec section titles, deep-dive topic cards, logo fallback, PBP JSON keys + spreadsheet aliases.*
