# Team Subjective Highlights — Results (Club-blind)

Primary question: **Do winner-channel videos vs loser-channel videos differ in pacing, exposure, and persona focus—holding club identity out of the headline analysis?**

---

## Opening scope

### Club-blind aggregate

This phase compares **official match highlights** published by the **winning** club’s channel vs the **losing** club’s channel for the same fixtures. Every metric is labeled **winner** or **loser** by **match outcome role** (which channel the video **belongs to**), not by **club brand**. The goal is **systematic differences tied to winning vs losing**, not league-table storytelling.

### What we did *not* score

We **did not** analyze **which specific plays** made the cut at PBP level—whether chances were volleys, corners, three-star saves, etc. Match facts are **given**; goals and obvious highlight moments appear across videos. **Editorial voice** here is modeled through **pacing** (length, PBP count, average PBP length), **how volume splits across PBP types**, **persona / emotional screen time** (celebrations + reactions, self and rival), **replay counts**, and **optional rival exposure**—not through cherry-picking exotic PBPs.

### Cordiality read (exposure)

More **rival airtime**—rival non-goal chances, **rival celebration + rival reaction** seconds, and (in the sheet) optional rival non-goal replays—tracks **ceding space** to the opponent on channels where producers control discretion. **Reaction is not treated as the opposite of celebration**; both are **persona exposure** buckets.

> **Live dashboard:** `rival_non_goal_replays` remains in `stats.json` but is **not charted** (small _n_). Tables below still document the aggregate for reference. Bar charts encode **winner** vs **loser** with WSC **`palette.success[100]`** (green) and **`palette.neutral[200]`** (grey); see `docs/assets/wsc-theme.css`.

### Later / exploratory (not primary inference)

- **Per-club** breakdowns: winner-role vs loser-role patterns **by team name**.
- **Rival identity**: whether videos shift when the opponent is a **big-six / legacy draw** vs the rest.
- **Small aggregate _n_**: headline metrics below come from **five matchweeks** of tagging; treat findings as **directional**, not definitive.

---

## Data window

| Item | Value |
|------|-------|
| Source spreadsheet | See `docs/stats.json` → `source_file` |
| Decisive fixtures (Home/Away, excludes draws in sheet) | **36** |
| Matchweeks represented | **30–34** (**5** rounds) |
| Paired rows (_n_) | **31–36** depending on column completeness |

_Draw rows remain in the workbook but are excluded from decisive-role analysis._

---

## Paired summary — headline metrics

Metrics compare **winner-channel value − loser-channel value** per fixture (negative ⇒ loser channel higher on average).

### Optional rival “football” exposure

| Metric | Winner mean | Loser mean | Mean Δ (W−L) | Median Δ | % fixtures where winner video higher |
|--------|-------------|------------|--------------|----------|--------------------------------------|
| Rival non-goal **chances** (_n_=32) | 1.91 | 1.94 | **−0.03** | 0.0 | 40.6% |
| Rival non-goal **replay count** (_n_=31) | 0.16 | 0.52 | **−0.35** | 0.0 | 9.7% |

**Read:** **Rival non-goal chance counts** are essentially **flat** between roles on average (median tie at 0 difference). Rival non-goal **replay** means skew **loser-role** in this sample but are treated cautiously and **not shown as a figure** on the current HTML dashboard.

### Pacing / structure

_(Sheet / JSON: `total_length`, `pbp_count` [or legacy `…total clips`], `avg_pbp_length` [or legacy average clip length columns].)_

| Metric | Winner mean | Loser mean | Mean Δ (W−L) | Median Δ | % winner higher |
|--------|-------------|------------|--------------|----------|-----------------|
| Total length (s), _n_=32 | 144.1 | 138.5 | **+5.6** | +8.5 | 59.4% |
| PBP count (`pbp_count`), _n_=32 | 7.22 | 8.81 | **−1.59** | −1.0 | 31.3% |
| Avg PBP length (s) (`avg_pbp_length`), _n_=32 | 20.27 | 17.97 | **+2.29** | +3.37 | 59.4% |

**Read:** Winner-role videos are **slightly longer** and **slightly fewer PBPs** ⇒ **longer average PBP length**—a **looser** pacing signature vs loser-role videos in this sample.

### Persona exposure (aggregate celebration + reaction, self + rival)

| Metric | Winner mean | Loser mean | Mean Δ (W−L) | Median Δ | % winner higher |
|--------|-------------|------------|--------------|----------|-----------------|
| Total persona seconds, _n_=36 | 21.56 | 12.69 | **+8.86** | +8.0 | 83.3% |
| Share of runtime (persona / length), _n_=32 | 0.152 | 0.102 | **+0.050** | +0.038 | 78.1% |
| Persona seconds **per PBP**, _n_=32 | 3.37 | 1.91 | **+1.46** | +1.23 | 75.0% |

**Read:** Winner-role videos devote **more clock time to people-focused beats** (celebration + reaction, all sides), both **absolutely** and **normalized** by runtime and by PBP.

### Rival-only persona seconds (rival celebration + rival reaction)

| Winner mean | Loser mean | Mean Δ (W−L) | Median Δ | % winner higher |
|-------------|------------|--------------|----------|-----------------|
| 4.17 s | 6.25 s | **−2.08** | 0.0 | 36.1% |

**Read:** **Loser-role** videos spend **more time on rival personas** in aggregate across this sample (alongside higher optional rival replay counts in the sheet), while **overall** persona share still skews **winner-role** because **self** persona time jumps after victories.

---

## Short synthesis (observational)

1. **Pacing:** Winner-role videos = **longer**, **fewer PBPs**, **higher avg PBP length** vs loser-role in this tranche.
2. **Optional rival mechanics:** **Rival non-goal replay counts** skew **loser-role** in the sheet (see table); **rival non-goal chance counts** do **not** separate cleanly on average.
3. **Persona budget:** **Total** persona time skews heavily **winner-role**; **rival-only** persona time skews **loser-role**—so winner-role videos look **more self-focused** while loser-role videos grant **more rival face time** per these rules.

These patterns describe **this dataset**, not universal Premier League editorial law.

---

## Exploratory — per-club views

**Not part of the primary claim.** The sample spans **many clubs** with **very few games each** when sliced by team (**five matchweeks**). Any **per-team** chart is an **invitation for follow-up** if stakeholders want deeper tagging—not a stable league portrait.

Regenerate aggregate numbers after spreadsheet updates:

```bash
python3 scripts/build_stats.py
```

---

## Next steps

- Refresh stats after new rows land in the enriched workbook.
- HTML dashboard: regenerate `stats.json` (`build_stats.py`), then serve `docs/` with a local HTTP server (e.g. `cd docs && python3 -m http.server 8000`) so `index.html` can load `stats.json`.
