#!/usr/bin/env python3
"""Build the static research guide, full note archive, and search index.

Only Python's standard library and Pandoc are required. Source note and
experiment paths remain unchanged. The generated site needs no CDN.
"""
from concurrent.futures import ThreadPoolExecutor
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
import ast
import json
import os
import posixpath
import re
import shutil
import subprocess
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs"
REPO = "https://github.com/sashakolpakov/murakamis_dream"
CHAPTERS = [
    ("index", "Overview"), ("results", "Equality results"),
    ("mechanism", "The mechanism"), ("geometry", "Actual geometry"),
    ("frontier", "Current frontier"), ("notation", "Notation"),
    ("audits", "Reproducing audits"),
]


def title_of(text, fallback):
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else fallback.replace("_", " ")


class Headings(HTMLParser):
    def __init__(self):
        super().__init__(); self.current = None; self.items = []

    def handle_starttag(self, tag, attrs):
        if tag == "h2":
            self.current = [dict(attrs).get("id", ""), []]

    def handle_data(self, data):
        if self.current is not None:
            self.current[1].append(data)

    def handle_endtag(self, tag):
        if tag == "h2" and self.current is not None:
            self.items.append((self.current[0], "".join(self.current[1])))
            self.current = None


def page(url, title, body, active, source=None, topic="Research guide", status="", adjacent=None):
    depth = len(Path(url).parts) - 1
    base = "../" * depth or "./"
    nav = "".join(
        f'<a href="{base}{"index.html" if slug == "index" else "guide/" + slug + ".html"}"'
        f' class="{"active" if active == slug else ""}">{escape(label)}</a>'
        for slug, label in CHAPTERS
    )
    nav += '<div class="nav-label">Explore the research</div>'
    nav += f'<a href="{base}figures.html" class="{"active" if active == "figures" else ""}">Figure gallery</a>'
    nav += f'<a href="{base}archive.html" class="{"active" if active == "archive" else ""}">Search the archive</a>'
    headings = Headings(); headings.feed(body)
    toc = '<aside class="toc" aria-label="On this page"><p>On this page</p>' + "".join(
        f'<a href="#{escape(identifier)}">{escape(label)}</a>'
        for identifier, label in headings.items if identifier
    ) + '</aside>'
    context = ""
    if source and source.startswith("notes/"):
        context = f'<div class="note-context"><span class="badge">{escape(status)}</span> Technical research note. Exact scope and later corrections are stated in the text.<br><a href="{REPO}/blob/main/{quote(source)}">Markdown source</a><a href="{base}guide/frontier.html">Read the current frontier</a></div>'
    chapter_nav = ""
    if adjacent:
        chapter_nav = '<nav class="chapter-nav" aria-label="Chapter navigation">' + "".join(
            f'<a href="{base}{target}">{escape(label)}</a>' if target else '<span></span>'
            for target, label in adjacent
        ) + '</nav>'
    source_link = f'<a href="{REPO}/blob/main/{quote(source)}">Edit or inspect source</a>' if source else ""
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title) if title == 'Murakami’s Dream' else escape(title) + ' · Murakami’s Dream'}</title><meta name="description" content="Research guide to original quantum sources, A-structures and actual hyperbolic volume. General conjecture remains open.">
<link rel="stylesheet" href="{base}assets/site.css"><link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
<script src="{base}assets/site.js" defer></script></head>
<body data-base="{base}"><a class="skip" href="#main">Skip to content</a>
<div class="mobile-bar"><a href="{base}index.html">Murakami’s Dream</a><button class="mobile-menu" id="menu-toggle" aria-expanded="false" aria-controls="sidebar">Menu</button></div>
<aside class="sidebar" id="sidebar"><a class="brand" href="{base}index.html">Murakami’s<br>Dream</a><div class="brand-sub">A research notebook</div>
<button class="search-trigger" data-search-open>Search research <kbd>/</kbd></button><div class="nav-label">Read the argument</div><nav aria-label="Main navigation">{nav}</nav>
<div class="sidebar-bottom">Research edition · 29 October 2026<br>General conjecture remains open.<a href="{REPO}">Repository ↗</a><a href="{REPO}/blob/main/RESEARCH_LOG.md">Historical research log ↗</a></div></aside>
<main id="main" class="layout"><div class="eyebrow">{escape(topic)}</div><div class="reading-grid"><article class="content">{context}{body}{chapter_nav}
<footer class="page-footer">{source_link}<a href="{REPO}">Source repository</a><p>Written arguments, exact audits, and numerical diagnostics retain their distinct scopes.</p></footer></article>{toc}</div></main>
<dialog class="search-dialog" id="search-dialog" aria-label="Search research"><div class="dialog-head"><input id="search-input" type="search" aria-label="Search notes and audits" placeholder="Search notes, formulas, or audit names…"><button id="search-close" aria-label="Close search">Esc</button></div><div class="dialog-body"><p id="search-status" class="dialog-hint" role="status">Search guide chapters, full technical notes, and audit filenames.</p><div id="search-results"></div></div></dialog>
</body></html>'''


def main():
    if not shutil.which("pandoc"):
        raise SystemExit("Pandoc is required. Install it, then run this script again.")
    catalog = json.loads((ROOT / "book/catalog.json").read_text())
    mapping = {}
    for slug, _ in CHAPTERS:
        mapping[f"book/chapters/{slug}.md"] = "index.html" if slug == "index" else f"guide/{slug}.html"
    mapping["book/figures.md"] = "figures.html"
    for source in sorted((ROOT / "notes").glob("*.md")):
        mapping[source.relative_to(ROOT).as_posix()] = f"notes/{source.stem}.html"
    figures = [p for p in (ROOT / "book/figures").iterdir() if p.suffix in (".png", ".svg", ".pdf", ".tex")]
    for source in figures:
        mapping[source.relative_to(ROOT).as_posix()] = f"assets/figures/{source.name}"
    (OUT / "assets/figures").mkdir(parents=True, exist_ok=True)
    for source in figures:
        shutil.copyfile(source, OUT / mapping[source.relative_to(ROOT).as_posix()])
    for filename in ("site.css", "site.js"):
        shutil.copyfile(ROOT / "book" / filename, OUT / "assets" / filename)
    (OUT / "assets/favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="8" fill="#183444"/><path d="M10 30V10h4v9l10-9h6L18 21l13 9h-7l-10-8v8" fill="#fff"/></svg>')
    (OUT / ".nojekyll").touch()
    broken = []
    restored_math = []

    def rewrite(body, source, target):
        # Older notes write products such as [a](b;Q) as plain text.
        # Markdown mistakes these for links. Restore the literal notation
        # instead of creating a spurious URL or altering the source note.
        def restore_literal(match):
            raw, label = match.groups(); value = unescape(raw)
            parts = urlsplit(value)
            path = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(parts.path)))
            if not parts.scheme and not parts.netloc and parts.path and re.search(r'[(),;^]|^1[+-]|^[A-Za-z]$', unquote(parts.path)) and path not in mapping and not (ROOT / path).exists():
                restored_math.append({"source": source, "expression": value})
                return '[' + label + '](' + escape(value) + ')'
            return match.group(0)
        body = re.sub(r'<a href="([^"]*)">(.*?)</a>', restore_literal, body, flags=re.S)
        def replace(match):
            attribute, raw = match.groups(); value = unescape(raw)
            parts = urlsplit(value)
            if parts.scheme or parts.netloc or not parts.path:
                return match.group(0)
            path = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(parts.path)))
            if path in mapping:
                href = posixpath.relpath(mapping[path], posixpath.dirname(target) or ".")
            elif (ROOT / path).is_file() and not path.startswith("../"):
                href = REPO + "/blob/main/" + quote(path)
            else:
                broken.append({"source": source, "link": value})
                href = REPO + "/blob/main/" + quote(path)
            if parts.query: href += "?" + parts.query
            if parts.fragment: href += "#" + parts.fragment
            return f'{attribute}="{escape(href, quote=True)}"'
        body = re.sub(r'(href|src)="([^"]*)"', replace, body)

        def figure_downloads(match):
            figure = match.group(0)
            picture = re.search(r'<img\b[^>]*\bsrc="([^"]+)"[^>]*>', figure)
            if not picture:
                return figure
            image_url = unescape(picture[1])
            stem = Path(urlsplit(image_url).path).stem
            if not all((ROOT / "book/figures" / (stem + ext)).is_file()
                       for ext in (".png", ".svg", ".pdf", ".tex")):
                return figure
            prefix = image_url.rsplit(".", 1)[0]
            links = " · ".join(
                f'<a href="{escape(prefix + ext, quote=True)}">{label}</a>'
                for ext, label in ((".svg", "Open vector figure"),
                                   (".pdf", "PDF"), (".tex", "TikZ source"))
            )
            return figure.replace('</figure>',
                                  f'<p class="figure-downloads">{links}</p></figure>')

        return re.sub(r'<figure\b[^>]*>.*?</figure>', figure_downloads, body, flags=re.S)

    md_sources = [(source, target) for source, target in mapping.items() if source.endswith(".md")]
    records = []

    def convert(item):
        source, target = item; text = (ROOT / source).read_text()
        result = subprocess.run(["pandoc", "--from=markdown-raw_html+tex_math_dollars+tex_math_single_backslash", "--to=html5", "--mathml", "--wrap=none"], input=text, text=True, capture_output=True, check=True)
        body = rewrite(result.stdout, source, target)
        stem = Path(source).stem; is_guide = source.startswith("book/")
        topic, status = ("Research guide", "Guide") if is_guide else catalog.get(stem, ["Research archive", "See note"])
        adjacent = None
        if is_guide and stem in {slug for slug, _ in CHAPTERS}:
            i = [s for s, _ in CHAPTERS].index(stem); adjacent = []
            for delta in (-1, 1):
                j = i + delta
                if 0 <= j < len(CHAPTERS):
                    slug, label = CHAPTERS[j]; adjacent.append((mapping[f"book/chapters/{slug}.md"], ("← " if delta < 0 else "Next: ") + label))
                else: adjacent.append(("", ""))
        title = title_of(text, stem)
        html = page(target, title, body, stem if is_guide else "archive", source, topic, status, adjacent)
        # Preserve explicit TeX spaces in MathML annotations without storing
        # trailing whitespace in generated HTML source lines.
        html = re.sub(r'(<annotation encoding="application/x-tex">)(.*?)(</annotation>)',
                      lambda m: m[1] + re.sub(r' +(?=\n)', lambda s: '&#32;' * len(s[0]), m[2]) + m[3],
                      html, flags=re.S)
        destination = OUT / target; destination.parent.mkdir(parents=True, exist_ok=True); destination.write_text(html)
        return {"title": title, "url": target, "type": "Guide" if is_guide else "Note", "topic": topic, "status": status, "text": re.sub(r"\s+", " ", text).strip()}

    with ThreadPoolExecutor(max_workers=min(8, os.cpu_count() or 2)) as executor:
        records.extend(executor.map(convert, md_sources))
    for source in sorted((ROOT / "experiments").iterdir()):
        if source.suffix not in (".py", ".json") or not source.is_file(): continue
        text = source.read_text(); scope = ""
        if source.suffix == ".py":
            try: scope = ast.get_docstring(ast.parse(text)) or ""
            except SyntaxError: scope = "See script for assumptions and dependencies."
        else:
            try:
                data = json.loads(text)
                if isinstance(data, dict): scope = str(data.get("scope", data.get("limits", "Recorded output; see the linked audit and technical note.")))
            except json.JSONDecodeError: scope = "Recorded output; inspect its format."
        records.append({"title": source.stem.replace("_", " "), "url": REPO + "/blob/main/experiments/" + quote(source.name), "type": "Audit script" if source.suffix == ".py" else "Recorded data", "topic": "Audits and data", "status": "Check stated scope", "text": scope})
    (OUT / "assets/search.json").write_text(json.dumps(records, ensure_ascii=False, separators=(",", ":")))
    fallback = ''.join(f'<li><a href="{escape(row["url"])}">{escape(row["title"])}</a></li>' for row in records if row['type'] == 'Note')
    body = f'''<h1>Research archive</h1><p>Search the complete technical notes, audit scripts, and recorded data. Start with the guide for the current argument; archived notes retain their own hypotheses, dates, and corrections.</p><p><strong>“PASS” in an audit is not a general proof.</strong> Uncatalogued notes carry the neutral “See note” status.</p>
<div class="archive-controls"><input id="archive-query" type="search" aria-label="Search archive" placeholder="Search full notes or audit names…"><select id="archive-type" aria-label="Record type"><option value="">All types</option><option>Guide</option><option>Note</option><option>Audit script</option><option>Recorded data</option></select><select id="archive-topic" aria-label="Research topic"><option value="">All topics</option></select></div><p id="archive-count" class="archive-count" role="status">Loading the index…</p><div id="archive-results"></div><button id="archive-more" class="more" hidden>Show more</button><noscript><h2>Technical notes</h2><p>Enable JavaScript for search and topic filtering.</p><ul>{fallback}</ul></noscript>'''
    (OUT / "archive.html").write_text(page("archive.html", "Research archive", body, "archive"))
    info = {"guide_chapters": len(CHAPTERS), "technical_notes": sum(r['type'] == 'Note' for r in records), "search_records": len(records), "figures": len([f for f in figures if f.suffix == '.png']), "literal_math_links_restored": len(restored_math), "unresolved_source_links": sorted(broken, key=lambda r: (r['source'], r['link']))}
    (OUT / "build-info.json").write_text(json.dumps(info, indent=2) + "\n")
    print(json.dumps({k: v for k, v in info.items() if k != 'unresolved_source_links'}, indent=2))
    print(f"Unresolved historical source links: {len(broken)} (recorded in docs/build-info.json)")
    current_broken = [row for row in broken if row['source'].startswith('book/')]
    if current_broken: raise SystemExit(f"Guide has unresolved links: {current_broken}")


if __name__ == "__main__":
    main()
