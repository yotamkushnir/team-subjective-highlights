#!/usr/bin/env python3
"""Refresh embedded content in docs/index.html (stats JSON + editorial playbook).

Delegates to embed_stats_in_html.py, which inlines stats then editorial markdown.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "embed_stats_in_html.py")],
        cwd=str(ROOT),
    )
    raise SystemExit(r.returncode)
