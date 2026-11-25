#!/usr/bin/env python3
"""Render the revised manuscript guide without publishing new research notes.

Reuses the guide template and Pandoc settings. Updates only the manuscript
chapter, first-edition errata, paper index, manuscript PDF/figures, and their
existing search entries. Other research notes are not published by this command.
"""
from __future__ import annotations

import hashlib
from html import escape, unescape
import json
from pathlib import Path
import posixpath
import re
import shutil
import subprocess
from urllib.parse import quote, unquote, urlsplit

import build_book
from check_book import Links

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs"
SOURCES = {
    "book/chapters/manuscript.md": "guide/manuscript.html",
    "manuscript/ERRATA.md": "guide/errata.html",
    "papers/README.md": "papers/index.html",
}


def main() -> None:
    mapping = dict(SOURCES)
    for slug, _ in build_book.CHAPTERS:
        mapping[f"book/chapters/{slug}.md"] = (
            "index.html" if slug == "index" else f"guide/{slug}.html")
    mapping.update({
        "book/figures.md": "figures.html",
        "book/library.html": "library.html",
        "book/archive.html": "archive.html",
        "manuscript/build/main.pdf": "papers/conway-composition.pdf",
    })
    for name in ("dependencies.html", "dependencies.svg", "dependencies.json",
                 "dependency-analysis.json"):
        mapping[f"docs/papers/{name}"] = f"papers/{name}"
    for item in json.loads((ROOT / "papers/catalog.json").read_text())["papers"]:
        name = item["directory"]
        mapping[f"docs/papers/{name}.pdf"] = f"papers/{name}.pdf"
    for source in (ROOT / "notes").glob("*.md"):
        target = f"notes/{source.stem}.html"
        if (OUT / target).is_file():
            mapping[source.relative_to(ROOT).as_posix()] = target
    for source in (ROOT / "book/figures").iterdir():
        if source.suffix in {".png", ".svg", ".pdf", ".tex"}:
            mapping[source.relative_to(ROOT).as_posix()] = f"assets/figures/{source.name}"

    copied = {"manuscript/build/main.pdf": "papers/conway-composition.pdf"}
    for source in (ROOT / "manuscript/build/figures").glob("*"):
        if source.suffix in {".png", ".pdf"}:
            copied[source.relative_to(ROOT).as_posix()] = (
                f"assets/figures/manuscript-{source.name}")
    mapping.update(copied)
    for source, target in copied.items():
        (OUT / target).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / source, OUT / target)

    records = json.loads((OUT / "assets/search.json").read_text())
    positions = {row["url"]: i for i, row in enumerate(records)}
    for source, target in SOURCES.items():
        text = (ROOT / source).read_text()
        result = subprocess.run([
            "pandoc", "--from=markdown-raw_html+tex_math_dollars+tex_math_single_backslash",
            "--to=html5", "--mathml", "--wrap=none",
        ], input=text, text=True, capture_output=True, check=True)
        if result.stderr.strip():
            raise RuntimeError(f"Pandoc warning in {source}: {result.stderr}")

        def link(match: re.Match) -> str:
            attr, raw = match.groups()
            parts = urlsplit(unescape(raw))
            if parts.scheme or parts.netloc or not parts.path:
                return match.group(0)
            path = posixpath.normpath(posixpath.join(
                posixpath.dirname(source), unquote(parts.path)))
            if path in mapping:
                value = posixpath.relpath(mapping[path], posixpath.dirname(target))
            elif (ROOT / path).is_file() and not path.startswith("../"):
                value = build_book.REPO + "/blob/main/" + quote(path)
            else:
                raise RuntimeError(f"Unresolved source link in {source}: {raw}")
            if parts.query:
                value += "?" + parts.query
            if parts.fragment:
                value += "#" + parts.fragment
            return f'{attr}="{escape(value, quote=True)}"'

        body = re.sub(r'(href|src)="([^"]*)"', link, result.stdout)
        title = build_book.title_of(text, Path(source).stem)
        is_papers = source == "papers/README.md"
        adjacent = None if is_papers or source == "manuscript/ERRATA.md" else [
            ("guide/starting.html", "← Start with the diagram"),
            ("guide/results.html", "Next: Equality results"),
        ]
        html = build_book.page(
            target, title, body, "papers" if is_papers else "manuscript", source,
            "Research papers" if is_papers else "Research guide",
            "" if is_papers else "Guide", adjacent,
        ).replace("Research edition · 1 November 2026",
                  "Research edition · 25 November 2026")
        parser = Links()
        parser.feed(html)
        if parser.math_errors:
            raise RuntimeError(f"Unrendered math in {source}: {parser.math_errors}")
        (OUT / target).write_text(html)
        row = {"title": title, "url": target, "type": "Guide",
               "topic": "Research papers" if is_papers else "Research guide",
               "status": "" if is_papers else "Guide",
               "text": re.sub(r"\s+", " ", text).strip()}
        if target in positions:
            records[positions[target]] = row
        else:
            records.append(row)
        print(f"Rendered {target}; formulas are MathML.")

    for filename, data in [
        ("search.json", records),
        ("browse.json", [{**r, "text": r["text"][:260]} for r in records]),
    ]:
        (OUT / "assets" / filename).write_text(
            json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    report = {
        "scope": "Only the three manuscript-guide pages and their PDF/figures/search entries; no research-note publication or mathematical proof verification.",
        "source_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                          for p in SOURCES},
        "rendered_pages": list(SOURCES.values()),
        "copied_assets": copied,
    }
    destination = ROOT / "repro/results/manuscript-and-lean"
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "guide-build.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
