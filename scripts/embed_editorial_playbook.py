#!/usr/bin/env python3
"""Inline docs/editorial-playbook.md into docs/index.html (between BEGIN/END markers)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError as e:
    raise SystemExit(
        "Missing dependency: pip install markdown\n"
        "See requirements.txt in the repo root."
    ) from e

ROOT = Path(__file__).resolve().parents[1]
md_path = ROOT / "docs" / "editorial-playbook.md"
html_path = ROOT / "docs" / "index.html"

BLOCK = re.compile(
    r"(<!-- EDITORIAL_PLAYBOOK_BEGIN -->).*?(<!-- EDITORIAL_PLAYBOOK_END -->)",
    re.DOTALL,
)


def md_to_playbook_fragment(raw: str) -> str:
    """Convert playbook markdown to HTML matching dashboard heading styles."""
    text = re.sub(r"^## ", "### ", raw, flags=re.MULTILINE)

    html_fragment = markdown.markdown(
        text,
        extensions=["extra"],
        output_format="html",
    )
    html_fragment = re.sub(
        r"<h1>(.*?)</h1>",
        r'<h2 class="playbook-title">\1</h2>',
        html_fragment,
        count=1,
    )
    html_fragment = re.sub(
        r"(</h2>\s*)<p>",
        r'\1<p class="playbook-lead">',
        html_fragment,
        count=1,
    )
    lines = html_fragment.strip().split("\n")
    return "\n".join("          " + ln if ln.strip() else ln for ln in lines)


def main() -> int:
    if not md_path.is_file():
        print(f"Missing {md_path}", file=sys.stderr)
        return 1

    html = html_path.read_text(encoding="utf-8")
    if not BLOCK.search(html):
        raise SystemExit(
            "Could not find EDITORIAL_PLAYBOOK_BEGIN/END block in index.html."
        )

    inner = md_to_playbook_fragment(md_path.read_text(encoding="utf-8"))

    def repl(m: re.Match[str]) -> str:
        return m.group(1) + "\n" + inner + "\n          " + m.group(2)

    new_html, n = BLOCK.subn(repl, html, count=1)
    if n != 1:
        raise SystemExit("Playbook embed replacement failed.")

    html_path.write_text(new_html, encoding="utf-8")
    print(f"Inlined editorial playbook into {html_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
