#!/usr/bin/env python3
"""Dashboard reads docs/stats.json at runtime (see docs/index.html).

This script regenerates docs/stats.json from the workbook via build_stats.py
when needed; it no longer inlines JSON into index.html (that broke GitHub Pages
Jekyll builds on large pages).

Run after updating the spreadsheet:
  python3 scripts/build_stats.py && python3 scripts/embed_stats_in_html.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
stats_path = ROOT / "docs" / "stats.json"
if not stats_path.is_file():
    raise SystemExit(f"Missing {stats_path} — run python3 scripts/build_stats.py first.")
stats_path.read_text(encoding="utf-8")  # sanity: readable JSON-sized file
print(f"OK: stats present at {stats_path} (loaded by index.html at runtime)")
