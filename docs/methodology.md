# Team Subjective Highlights — Methodology & Parameter Relationships

Internal reference for tagging, QA, and analysis (Premier League official highlight comparisons).

---

## Clip accounting (sanity check)

**Identity (per video: winner’s edit or loser’s edit):**

`self non-goal chances` + `rival non-goal chances` + `goal clips` ≈ `total clips`

- **`goal clips`** = number of **goal** clips in **this** edit (each scored goal shown as its own clip). **Not** the spreadsheet match-score columns (`winner goals` / `loser goals`), which are fixture metadata.

- **Non-goal chances** and **goals** are the usual building blocks; **each goal is one clip** (per project rules, including VAR-cancelled goals as one non-goal clip — see earlier tagging notes).
- **Yellow cards** (including a caution that is *not* a second yellow → red): **ignore** — do not create a clip, do not treat as a chance.

**Red card — only systematic exception to the simple sum**

| Situation | How to tag |
|-----------|------------|
| Red card **tied to** an existing chance sequence (e.g. foul in the box → red + penalty scored) | **One clip total** for that sequence (do not split into “chance clip” + “red card clip”). Count that clip per your outcome rules (e.g. penalty scored → goal clip). |
| Red card as **standalone** incident (not merged into a single chance/goal sequence) | Still **one clip**, but it is **not** a non-goal chance for either team and **not** a goal. |
| Second yellow → red | Treat as **red-card logic** above (not as “ignore like yellow”). |

**QA implication:** If you have a **standalone** red-card clip, expect:

`self non-goal chances` + `rival non-goal chances` + `goal clips` = `total clips` − `standalone red-card clips`

When there is **no** standalone red card, the identity should close without fudge factors.

---

## Quick recap (units & definitions)

- **Length / celebration / reaction:** seconds.
- **Replays:** **counts** (how many angles), not seconds.
- **Average clip length** = `(total video length − final whistle celebration seconds) ÷ clip count`. Final-whistle block is **not** a clip and is **excluded** from the average’s time base.
- **Home/away link columns:** ignore for current analysis.
- **Comments / empty column AQ:** ignore for v1.

### Aggregate comparisons that control for score / volume

When comparing **winner vs loser** edits, raw **self celebration** totals mostly scale with **goals scored**. Report **self celebration seconds ÷ goals scored** (match score columns) when comparing emotional dwell across outcomes. Similarly use **self reaction ÷ self non-goal chances** and **rival reaction ÷ rival non-goal chances** when denominators exist — paired stats exclude rows with zero denominators (e.g. shutouts for per-goal celebration).

---

## How parameters interact (for analysis & storytelling)

### 1. Cordiality (generous ↔ egoistic)

**Core idea:** Optional **rival exposure** signals generosity — you must show goals; you do **not** have to show rival misses/shots. **Reactions are not the opposite of celebrations:** any extra **rival** screen time (rival celebrations you still include, **rival** reaction close-ups, rival non-goal chances, optional rival replays) trends **cordial** in the same direction — you are **ceding airtime** to the opponent.

**Primary inputs**

- **Rival non-goal chances** (clip counts): exposure of opponent attacking moments you could omit.
- **Rival non-goal replay counts**: optional **re-showing** of rival non-goal actions (counts, not duration).
- **Rival persona time** (rival celebration + rival reaction seconds): dwell on **rival** faces/crowds after goals or on non-goal beats.

Pair **rival goal replay counts** with **rival non-goal** metrics to separate mandatory goal dwell from optional emphasis.

**Interpretation guardrail:** High rival exposure can read “generous,” or strategic (dominance). Use **winner vs loser** pairing and match context before labeling tone.

### 2. Exposure vs dwell (don’t conflate)

| Dimension | What it measures | Typical fields |
|-----------|------------------|----------------|
| **Exposure** | Did this moment appear as its own clip? | Non-goal chance counts; goal clips |
| **Dwell (time)** | How long you linger on **people** | Celebration (post-goal), reaction (non-goal emotional close-ups) — aggregate as **persona time** when comparing generosity |
| **Dwell (replays)** | How many extra angles you give | Replay **counts** (goal vs non-goal; self vs rival) |

### 3. Pacing and density

- **Total length** + **clip count** + **average clip length** (whistle-adjusted) describe how **compressed** or **extended** the edit is.
- **Avg clip length** is the best **normalized** pacing metric because it removes the **final-whistle celebration** block from both numerator and clip list.

### 4. Persona / emotional focus (winner edit vs loser edit)

- **Celebration** = post-goal window (project timer rules).
- **Reaction** = close-up emotional beats; **often** frustration or protest — not only frustration.

For **headline comparisons**, **aggregate** self + rival celebration + self + rival reaction into **total persona seconds**, then normalize by **runtime** and/or **per clip** to describe how much of the edit is **people-focused** vs pure play.

### 5. Goal emphasis vs non-goal emphasis

- **Goal replay counts** (self vs rival): **who scored** owns the goal replay; **one replay per angle**.
- **Non-goal replay counts** + **non-goal chance counts**: optional emphasis — strongest **cordiality** read when focused on **rival** rows.

### 6. End-of-game celebration (seconds)

- Not a clip; subtracted for **avg clip length**.
- Use as **narrative closure**: share of runtime (`end celebration ÷ total length`) — separate from in-match pacing.

### 7. Cross-field consistency checks (for collaborators)

1. **Clip sum** vs **chances + goals**, adjusted for **standalone red cards** only.
2. **Avg clip length** recomputes from total length, whistle duration, and clip count.
3. **Replay columns** stay **integer counts**, never seconds.

---

## Non-goal replay ownership (one-line reminder)

In the **channel’s own video**, attribute ambiguous non-goal replays with **benefit of the doubt** to the editor’s team when the replay flatters them (e.g. save on opponent shot → **self**). If unclear, **ask** before tagging.

---

*Last updated: repo copy; cordiality includes rival persona exposure; aggregate persona metrics.*
