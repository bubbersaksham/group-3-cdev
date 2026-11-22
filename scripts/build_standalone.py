#!/usr/bin/env python3
"""Rebuild STANDALONE_WEBSITE.html from the source files.

Inlines styles.css (with images embedded as base64), model-data.js and app.js
into a copy of index.html, producing a single file that opens offline.
Run from anywhere:  python3 scripts/build_standalone.py
"""
import base64
import mimetypes
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def inline_images(css: str) -> str:
    def repl(m):
        path = ROOT / m.group(1)
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        data = base64.b64encode(path.read_bytes()).decode()
        return f"url('data:{mime};base64,{data}')"

    return re.sub(r"url\('(images/[^']+)'\)", repl, css)


def main():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    css = inline_images((ROOT / "styles.css").read_text(encoding="utf-8"))

    replacements = {
        '<link href="styles.css" rel="stylesheet"/>': f"<style>\n{css}\n</style>",
        '<script src="model-data.js"></script>': "<script>\n" + (ROOT / "model-data.js").read_text(encoding="utf-8") + "\n</script>",
        '<script src="app.js"></script>': "<script>\n" + (ROOT / "app.js").read_text(encoding="utf-8") + "\n</script>",
    }
    for tag, inline in replacements.items():
        if tag not in html:
            raise SystemExit(f"Could not find {tag!r} in index.html")
        html = html.replace(tag, inline, 1)

    out = ROOT / "STANDALONE_WEBSITE.html"
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out.name} ({out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
