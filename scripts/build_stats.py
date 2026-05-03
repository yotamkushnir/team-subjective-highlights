#!/usr/bin/env python3
"""Read enriched spreadsheet; write docs/stats.json for the static report."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DOWNLOADS = Path.home() / "Downloads" / "pl_highlight_links_ENRICHED.xlsx"


def num(x):
    if pd.isna(x):
        return np.nan
    if isinstance(x, str) and ("not found" in x.lower() or x.strip() == ""):
        return np.nan
    try:
        return float(x)
    except (TypeError, ValueError):
        return np.nan


def paired(df: pd.DataFrame, col_w: str, col_l: str) -> dict:
    w = df[col_w].values
    l = df[col_l].values
    mask = np.isfinite(w) & np.isfinite(l)
    if not mask.any():
        return {"n": 0}
    d = w[mask] - l[mask]
    return {
        "n": int(mask.sum()),
        "winner_mean": float(np.mean(w[mask])),
        "loser_mean": float(np.mean(l[mask])),
        "mean_diff_w_minus_l": float(np.mean(d)),
        "median_diff": float(np.median(d)),
        "pct_winner_higher": float(100 * np.mean(d > 0)),
    }


def main() -> int:
    src = Path(os.environ.get("HIGHLIGHTS_XLSX", ""))
    if not src.is_file():
        src = ROOT / "data" / "pl_highlight_links_ENRICHED.xlsx"
    if not src.is_file():
        src = DEFAULT_DOWNLOADS
    if not src.is_file():
        print("Missing spreadsheet. Set HIGHLIGHTS_XLSX or copy file to data/", file=sys.stderr)
        return 1

    df = pd.read_excel(src)
    df.columns = [str(c).strip() for c in df.columns]

    for c in df.columns:
        if c in (
            "Game id",
            "date",
            "matchday",
            "game name",
            "score",
            "Winning Team",
            "Losing Team",
            "who won",
            "home highlight link",
            "away highlight link",
            "winner highlight link",
            "loser highlight link",
            "Comments",
            "Unnamed: 42",
        ):
            continue
        df[c] = df[c].apply(num)

    df = df[df["who won"].isin(["Home", "Away"])].copy()
    df = df.dropna(subset=["winner total lenght", "loser total lenght"], how="all")

    stats: dict = {
        "source_file": str(src),
        "fixture_count_decisive": int(len(df)),
        "matchdays": sorted(df["matchday"].dropna().unique().tolist()),
        "matchday_count": int(df["matchday"].nunique()),
    }

    stats["rival_non_goal_chances"] = paired(
        df,
        "winner amount of rival non-goal chances",
        "loser amount of rival non-goal chances",
    )
    stats["rival_non_goal_replays"] = paired(
        df,
        "winner total rival replays - non goals",
        "loser total rival replays - non goals",
    )
    stats["self_non_goal_chances"] = paired(
        df,
        "winner amount of self non-goal chances",
        "loser amount of self non-goal chances",
    )
    stats["avg_clip_length"] = paired(
        df, "winner average clip lenght", "loser average clip lenght"
    )
    stats["total_length"] = paired(df, "winner total lenght", "loser total lenght")
    stats["clip_count"] = paired(
        df, "winner amount of total clips", "loser amount of total clips"
    )

    for side in ("winner", "loser"):
        pcols = [
            f"{side} total self celebrations time",
            f"{side} total rival celebrations time",
            f"{side} total self reaction time",
            f"{side} total rival reaction time",
        ]
        for c in pcols:
            df[c] = df[c].fillna(0)
        df[f"{side}_persona_sec"] = df[pcols].sum(axis=1)

    stats["persona_total_sec"] = paired(df, "winner_persona_sec", "loser_persona_sec")

    df["w_persona_rate"] = df["winner_persona_sec"] / df["winner total lenght"]
    df["l_persona_rate"] = df["loser_persona_sec"] / df["loser total lenght"]
    mask = (
        np.isfinite(df["w_persona_rate"])
        & np.isfinite(df["l_persona_rate"])
        & (df["winner total lenght"] > 0)
        & (df["loser total lenght"] > 0)
    )
    if mask.any():
        d = df.loc[mask, "w_persona_rate"] - df.loc[mask, "l_persona_rate"]
        stats["persona_share_of_runtime"] = {
            "n": int(mask.sum()),
            "winner_mean": float(df.loc[mask, "w_persona_rate"].mean()),
            "loser_mean": float(df.loc[mask, "l_persona_rate"].mean()),
            "mean_diff_w_minus_l": float(d.mean()),
            "median_diff": float(d.median()),
            "pct_winner_higher": float(100 * (d > 0).mean()),
        }

    df["w_persona_per_clip"] = df["winner_persona_sec"] / df["winner amount of total clips"]
    df["l_persona_per_clip"] = df["loser_persona_sec"] / df["loser amount of total clips"]
    mask2 = (
        np.isfinite(df["w_persona_per_clip"])
        & np.isfinite(df["l_persona_per_clip"])
        & (df["winner amount of total clips"] > 0)
        & (df["loser amount of total clips"] > 0)
    )
    if mask2.any():
        d2 = df.loc[mask2, "w_persona_per_clip"] - df.loc[mask2, "l_persona_per_clip"]
        stats["persona_sec_per_clip"] = {
            "n": int(mask2.sum()),
            "winner_mean": float(df.loc[mask2, "w_persona_per_clip"].mean()),
            "loser_mean": float(df.loc[mask2, "l_persona_per_clip"].mean()),
            "mean_diff_w_minus_l": float(d2.mean()),
            "median_diff": float(d2.median()),
            "pct_winner_higher": float(100 * (d2 > 0).mean()),
        }

    df["w_rival_face"] = df["winner total rival celebrations time"].fillna(0) + df[
        "winner total rival reaction time"
    ].fillna(0)
    df["l_rival_face"] = df["loser total rival celebrations time"].fillna(0) + df[
        "loser total rival reaction time"
    ].fillna(0)
    stats["rival_persona_sec"] = paired(df, "w_rival_face", "l_rival_face")

    # Score / exposure-normalized emotional metrics (control for goals & chance volume)
    wg = df["winner goals"].fillna(0)
    lg = df["loser goals"].fillna(0)
    df["w_celeb_per_goal"] = np.where(
        wg > 0,
        df["winner total self celebrations time"].fillna(0) / wg,
        np.nan,
    )
    df["l_celeb_per_goal"] = np.where(
        lg > 0,
        df["loser total self celebrations time"].fillna(0) / lg,
        np.nan,
    )

    wsng = df["winner amount of self non-goal chances"].fillna(0)
    lsng = df["loser amount of self non-goal chances"].fillna(0)
    df["w_rx_per_sng"] = np.where(
        wsng > 0,
        df["winner total self reaction time"].fillna(0) / wsng,
        np.nan,
    )
    df["l_rx_per_sng"] = np.where(
        lsng > 0,
        df["loser total self reaction time"].fillna(0) / lsng,
        np.nan,
    )

    wrng = df["winner amount of rival non-goal chances"].fillna(0)
    lrng = df["loser amount of rival non-goal chances"].fillna(0)
    df["w_rival_rx_per_rng"] = np.where(
        wrng > 0,
        df["winner total rival reaction time"].fillna(0) / wrng,
        np.nan,
    )
    df["l_rival_rx_per_rng"] = np.where(
        lrng > 0,
        df["loser total rival reaction time"].fillna(0) / lrng,
        np.nan,
    )

    stats["self_celebration_per_goal"] = paired(df, "w_celeb_per_goal", "l_celeb_per_goal")
    stats["self_reaction_per_self_non_goal_chance"] = paired(
        df, "w_rx_per_sng", "l_rx_per_sng"
    )
    stats["rival_reaction_per_rival_non_goal_chance"] = paired(
        df, "w_rival_rx_per_rng", "l_rival_rx_per_rng"
    )

    out = ROOT / "docs" / "stats.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
