#!/usr/bin/env python3
"""Inline docs/stats.json into docs/index.html as const STATS = {...}"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
stats_path = ROOT / "docs" / "stats.json"
html_path = ROOT / "docs" / "index.html"
stats = json.loads(stats_path.read_text(encoding="utf-8"))
js = json.dumps(stats, indent=2)
html = html_path.read_text(encoding="utf-8")

# Idempotent: replace marker block OR existing inlined STATS (after first run).
pattern = re.compile(
    r"(\s*<!-- STATS_EMBED -->\s*<script>\s*)const STATS = .*?;(.*?)</script>",
    re.DOTALL,
)
replacement = r"\1const STATS = " + js + r";\2</script>"
new_html, n = pattern.subn(replacement, html, count=1)
if n != 1:
    raise SystemExit(
        "Could not find STATS embed block in index.html (expected <!-- STATS_EMBED --> + const STATS)."
    )
html_path.write_text(new_html, encoding="utf-8")
print(f"Inlined stats into {html_path}")
