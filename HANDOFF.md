# Agent handoff — Team Subjective Highlights

Paste this file (or `@HANDOFF.md`) at the start of a **new** chat so context stays light but aligned with the **current** repo.

## Purpose

Compare **official match highlights** (winner-channel vs loser-channel) for the same Premier League fixtures. **Main analysis is club-blind:** aggregate by **winner edit vs loser edit**, not club identity.

## Definitions that matter

- **“Rival”** = **the opponent in that fixture** (other shirt), **not** a historic derby “rival.”
- **Cordiality:** extra **rival** exposure (rival non-goal chances/replays, rival reaction time, etc.) reads as **ceding space** in the edit. Celebration vs reaction are **not** opposites — both are persona dwell.
- **Replays** in the sheet are **counts** (angles), not seconds.
- **Avg clip length** uses `(total length − final-whistle celebration) ÷ clips`.
- Full tagging rules: `docs/methodology.md`.

## URLs

| What | URL |
|------|-----|
| Live report (GitHub Pages) | https://yotamkushnir.github.io/team-subjective-highlights/ |
| Git repo | https://github.com/yotamkushnir/team-subjective-highlights |

## Repo map

| Path | Role |
|------|------|
| `docs/index.html` | Dashboard (**must** have embedded `STATS` JSON — see below) |
| `docs/stats.json` | Output of `build_stats.py` |
| `scripts/build_stats.py` | Reads enriched `.xlsx` → writes `stats.json` |
| `scripts/embed_stats_in_html.py` | Inlines `stats.json` + `editorial-playbook.md` into `index.html` |
| `scripts/embed_editorial_playbook.py` | Markdown → HTML (called by `embed_stats_in_html.py`) |
| `docs/editorial-playbook.md` | Source for the collapsible “video editor” section on the report |
| `docs/methodology.md` | Source of truth for definitions |
| `docs/results.md` | Written narrative (may lag the HTML) |

## Refresh workflow (data and/or narrative)

`embed_stats_in_html.py` **always** re-inlines **stats** and the **editorial playbook** (from `docs/editorial-playbook.md`). You do not need a separate step for the playbook.

```bash
cd /path/to/team-subjective-highlights
python3 scripts/build_stats.py && python3 scripts/embed_stats_in_html.py
git add docs/stats.json docs/index.html
git commit -m "Refresh report" && git push
```

**Playbook / prose only** (no spreadsheet change): run `python3 scripts/embed_stats_in_html.py` (or `python3 scripts/embed_docs.py` — same effect).

Default Excel path in script: `~/Downloads/pl_highlight_links_ENRICHED.xlsx` or env `HIGHLIGHTS_XLSX`.

## Critical: embedded stats in `index.html`

Charts read `const STATS = { ... }` inside `docs/index.html`. If `STATS` is **`{}`** empty, the page shows an error banner and **no real numbers**.

- A **fully embedded** `index.html` is **~1100+ lines** (JSON is large).
- If the editor shows **~400 lines** and `const STATS = {};`, the buffer is **stale** or embed **was not run** — re-run `embed_stats_in_html.py` and save.
- The collapsible **editorial** block is generated from `docs/editorial-playbook.md`. Edit the `.md` file, then run `embed_stats_in_html.py` (no need to touch the HTML body by hand).

## What `stats.json` contains (high level)

Paired **winner mean vs loser mean** on decisive fixtures (`who won` ∈ Home/Away). Key blocks include:

- **Rival exposure:** `rival_non_goal_chances`, `rival_non_goal_replays`
- **Own-team optional clips:** `self_non_goal_chances` (added later — loser edits tended higher in sample)
- **Pacing:** `avg_clip_length`, `clip_count`, `total_length`
- **Score-adjusted persona** (controls skew from goals/chance volume):
  - `self_celebration_per_goal`
  - `self_reaction_per_self_non_goal_chance`
  - `rival_reaction_per_rival_non_goal_chance`
- Legacy aggregates may still exist in JSON (`persona_share_of_runtime`, etc.) even if not charted.

## Report figure order in `index.html` (current)

1. **Figure 1** — Optional **rival** football exposure (rival NG chances + rival NG replays).
2. **Figure 2** — **Self** non-goal chances (optional own-team exposure).
3. **Figure 3** — Pacing (avg clip length + clip count).
4. **Figure 4** — Total runtime.
5. **Figure 5** — Persona / emotion (**score-adjusted** charts).

Hero copy explains club-blind scope; executive summary leads with bullets; `%` conventions are documented on-page.

## Future / out of scope for main claim

- Per-club slices; rival tier (“big six”) analysis — **small n**, exploratory only.

## What changed since early handoff drafts

Earlier chat summaries may omit: split rival vs pacing charts, **“rival” glossary** callout, **Winner/Loser** labels (not “winner-role”), **score-adjusted persona ratios**, **self non-goal chances** as its own figure, figure renumbering, and the **embed** requirement for `index.html`.

---

*Update this file when you change metrics, figure layout, or URLs.*
