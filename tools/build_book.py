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
    ("index", "Overview"), ("starting", "Start with the diagram"),
    ("manuscript", "The manuscript"), ("results", "Equality results"),
    ("mechanism", "How the proof works"), ("methods", "Methods and approaches"),
    ("algebraic", "Algebraic approaches"),
    ("geometry", "Hyperbolic geometry"),
    ("frontier", "Open questions"), ("notation", "Notation"),
    ("audits", "Reproducing calculations"),
]
COLLECTIONS = json.loads((ROOT / "book/collections.json").read_text())


def repair_numbered_fragments(directory):
    """Resolve GitHub-style numbered headings against actual Pandoc anchors."""
    class Anchors(HTMLParser):
        def __init__(self):
            super().__init__()
            self.ids = set()

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if attrs.get("id"):
                self.ids.add(attrs["id"])

    pages = {}
    for path in directory.rglob("*.html"):
        content = path.read_text()
        parser = Anchors()
        parser.feed(content)
        pages[path.resolve()] = (content, parser.ids)
    repaired = 0
    for path, (content, _) in pages.items():
        def replace(match):
            nonlocal repaired
            value = unescape(match[1])
            parts = urlsplit(value)
            if parts.scheme or parts.netloc or not parts.fragment:
                return match[0]
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if target not in pages:
                return match[0]
            ids = pages[target][1]
            fragment = unquote(parts.fragment)
            candidate = re.sub(r"^[0-9][0-9.\-]*", "", fragment)
            candidates = [candidate,
                          re.sub(r"^[0-9]+([a-z])-", r"\1.-", fragment),
                          candidate.replace("--", "")]
            candidate = next((item for item in candidates if item in ids), None)
            if fragment not in ids and candidate is not None:
                repaired += 1
                fixed = value.rsplit("#", 1)[0] + "#" + candidate
                return 'href="' + escape(fixed, quote=True) + '"'
            return match[0]
        revised = re.sub(r'href="([^"]*)"', replace, content)
        if revised != content:
            path.write_text(revised)
    return repaired


def note_context(source, base, status):
    stem = Path(source).stem
    related = [c for c in COLLECTIONS if stem in [c["entry"], *c["notes"]]]
    links = [f'<a href="{REPO}/blob/main/{quote(source)}">Markdown source</a>']
    for candidates, label in (((f"audit_{stem}.py",), "Audit script"),
                              ((f"{stem}_results.json", f"audit_{stem}_results.json"), "Recorded output")):
        filename = next((name for name in candidates if (ROOT / "experiments" / name).is_file()), None)
        if filename:
            links.append(f'<a href="{REPO}/blob/main/experiments/{quote(filename)}">{label}</a>')
    routes = " · ".join(f'<a href="{base}library.html#{c["id"]}">{escape(c["title"])}</a>' for c in related)
    return (f'<div class="note-context"><a href="{base}library.html">Research library</a>'
            + (f' / {routes}' if routes else '')
            + f'<p><span class="badge">{escape(status)}</span> Technical research note. Exact scope and later corrections are stated in the text.</p>'
            + '<div class="note-resources">' + " ".join(links)
            + f'<a href="{base}guide/frontier.html">Open questions</a></div></div>')


def title_of(text, fallback):
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else fallback.replace("_", " ")


class Headings(HTMLParser):
    def __init__(self):
        super().__init__(); self.current = None; self.items = []; self.annotation = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"annotation", "annotation-xml"}:
            self.annotation += 1
        if tag == "h2":
            self.current = [dict(attrs).get("id", ""), []]

    def handle_data(self, data):
        if self.current is not None and not self.annotation:
            self.current[1].append(data)

    def handle_endtag(self, tag):
        if tag in {"annotation", "annotation-xml"}:
            self.annotation -= 1
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
    nav += f'<a href="{base}library.html" class="{"active" if active == "library" else ""}">Research library</a>'
    nav += f'<a href="{base}figures.html" class="{"active" if active == "figures" else ""}">Figure gallery</a>'
    nav += f'<a href="{base}archive.html" class="{"active" if active == "archive" else ""}">Search the archive</a>'
    headings = Headings(); headings.feed(body)
    toc = '<aside class="toc" aria-label="On this page"><p>On this page</p>' + "".join(
        f'<a href="#{escape(identifier)}">{escape(label)}</a>'
        for identifier, label in headings.items if identifier
    ) + '</aside>'
    context = ""
    if source and source.startswith("notes/"):
        context = note_context(source, base, status)
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
<div class="sidebar-bottom">Research edition · 1 November 2026<br>General conjecture remains open.<a href="{REPO}">Repository ↗</a><a href="{REPO}/blob/main/RESEARCH_LOG.md">Historical research log ↗</a></div></aside>
<main id="main" class="layout"><div class="eyebrow">{escape(topic)}</div><div class="reading-grid"><article class="content">{context}{body}{chapter_nav}
<footer class="page-footer">{source_link}<a href="{REPO}">Source repository</a><p>Written arguments, exact audits, and numerical diagnostics retain their distinct scopes.</p></footer></article>{toc}</div></main>
<dialog class="search-dialog" id="search-dialog" aria-label="Search research"><div class="dialog-head"><input id="search-input" type="search" aria-label="Search notes and audits" placeholder="Search notes, formulas, or audit names…"><button id="search-close" aria-label="Close search">Esc</button></div><div class="dialog-body"><p id="search-status" class="dialog-hint" role="status">Search guide chapters, full technical notes, and audit filenames.</p><div id="search-results"></div></div></dialog>
</body></html>'''


def main():
    if not shutil.which("pandoc"):
        raise SystemExit("Pandoc is required. Install it, then run this script again.")
    catalog = json.loads((ROOT / "book/catalog.json").read_text())
    for collection in COLLECTIONS:
        for stem in [collection["entry"], *collection["notes"]]:
            if not (ROOT / "notes" / f"{stem}.md").is_file():
                raise SystemExit(f"Collection {collection['id']} refers to missing note {stem}")
    mapping = {}
    for slug, _ in CHAPTERS:
        mapping[f"book/chapters/{slug}.md"] = "index.html" if slug == "index" else f"guide/{slug}.html"
    mapping["book/figures.md"] = "figures.html"
    # Authored chapters may link to these generated navigation pages.
    mapping["book/library.html"] = "library.html"
    mapping["book/archive.html"] = "archive.html"
    manuscript_pdf = ROOT / "manuscript/build/main.pdf"
    if manuscript_pdf.is_file():
        mapping["manuscript/build/main.pdf"] = "papers/conway-composition.pdf"
        (OUT / "papers").mkdir(parents=True, exist_ok=True)
        shutil.copyfile(manuscript_pdf, OUT / "papers/conway-composition.pdf")
    for source in sorted((ROOT / "notes").glob("*.md")):
        mapping[source.relative_to(ROOT).as_posix()] = f"notes/{source.stem}.html"
    figures = [p for p in (ROOT / "book/figures").iterdir() if p.suffix in (".png", ".svg", ".pdf", ".tex")]
    for source in figures:
        mapping[source.relative_to(ROOT).as_posix()] = f"assets/figures/{source.name}"
    manuscript_figures = sorted(
        p for p in (ROOT / "manuscript/build/figures").glob("*")
        if p.suffix in (".png", ".pdf")
    )
    for source in manuscript_figures:
        mapping[source.relative_to(ROOT).as_posix()] = f"assets/figures/manuscript-{source.name}"
    (OUT / "assets/figures").mkdir(parents=True, exist_ok=True)
    for source in [*figures, *manuscript_figures]:
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
            if any(f'href="{escape(prefix + ext, quote=True)}"' in body
                   for ext in (".svg", ".pdf", ".tex")):
                return figure
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
        if result.stderr.strip():
            raise RuntimeError(f"Cannot publish {source}:\n{result.stderr.strip()}")
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
        note_stem = source.stem.removeprefix("audit_").removesuffix("_results")
        note_topic = catalog.get(note_stem, ["Audits and data", ""])[0]
        records.append({"title": source.stem.replace("_", " "), "url": REPO + "/blob/main/experiments/" + quote(source.name), "type": "Audit script" if source.suffix == ".py" else "Recorded data", "topic": note_topic, "status": "Check stated scope", "text": scope})
    records.append({"title": "Research library", "url": "library.html", "type": "Guide",
                    "topic": "Research guide", "status": "Reading routes",
                    "text": " ".join(c["title"] + ": " + c["summary"] for c in COLLECTIONS)})
    (OUT / "assets/search.json").write_text(json.dumps(records, ensure_ascii=False, separators=(",", ":")))
    (OUT / "assets/browse.json").write_text(json.dumps(
        [{**row, "text": row["text"][:260]} for row in records],
        ensure_ascii=False, separators=(",", ":")))
    by_url = {row["url"]: row for row in records}
    cards = []
    for number, collection in enumerate(COLLECTIONS, 1):
        c = collection
        preview = (f'<a class="collection-picture" href="guide/{c["guide"]}.html" aria-label="Read the guide to {escape(c["title"], quote=True)}">'
                   f'<img src="assets/figures/{c["figure"]}.png" alt="{escape(c["title"], quote=True)} — explanatory diagram" loading="lazy"></a>') if c.get("figure") else ''
        selected = ''.join(f'<li><a href="notes/{stem}.html">{escape(by_url[f"notes/{stem}.html"]["title"])}</a></li>' for stem in c["notes"])
        cards.append(f'''<section class="collection-card" id="{c['id']}">
<div class="collection-number">{number:02d} · {escape(c['topic'])}</div>
<h2 id="{c['id']}-heading">{escape(c['title'])}</h2>{preview}<p>{escape(c['summary'])}</p>
<p class="collection-scope">{escape(c['scope'])}</p>
<a class="collection-entry" href="notes/{c['entry']}.html">{escape(c['entry_label'])} →</a>
<details><summary>Supporting arguments ({len(c['notes'])})</summary><ul>{selected}</ul></details>
<div class="collection-links"><a href="guide/{c['guide']}.html">Read the explanation</a><a href="archive.html?type=Note&amp;topic={quote(c['topic'])}">Browse topic</a></div></section>''')
    library = ('<h1>Research library</h1><p>Choose a question, then follow its main argument and supporting notes. Each route states its scope; the archive keeps the full research history.</p>'
               '<div class="library-intro"><a href="guide/results.html"><strong>Start with the results</strong><span>Families, hypotheses, and exact conclusions</span></a>'
               '<a href="guide/frontier.html"><strong>Find the remaining gap</strong><span>What the general conjecture still needs</span></a>'
               '<a href="figures.html"><strong>Explore the diagrams</strong><span>Geometry, source operations, and peripheral data</span></a></div>'
               '<div class="collection-grid">' + ''.join(cards) + '</div>'
               '<h2 id="complete-archive">The complete archive</h2><p>These routes are curated entry points. All technical notes, including uncatalogued and historical work, remain available in the <a href="archive.html">searchable archive</a>. A note’s audit and recorded output are linked beside its source when a matching pair exists.</p>')
    (OUT / "library.html").write_text(page("library.html", "Research library", library, "library", "book/collections.json"))
    fallback = ''.join(f'<li><a href="{escape(row["url"])}">{escape(row["title"])}</a></li>' for row in records if row['type'] == 'Note')
    body = f'''<h1>Research archive</h1><p>Search the complete technical notes, audit scripts, and recorded data. For an organized starting point, <a href="library.html">browse the research library</a>. Archived notes retain their own hypotheses, dates, and corrections.</p><p>Recorded computations check their stated finite identities; the mathematical arguments and hypotheses are given in the associated notes. Uncatalogued notes carry the neutral “See note” status. Notes are shown first; select another record type to browse scripts or data.</p>
<div class="archive-controls"><input id="archive-query" type="search" aria-label="Search archive" placeholder="Search full notes or audit names…"><select id="archive-type" aria-label="Record type"><option value="">All types</option><option>Guide</option><option selected>Note</option><option>Audit script</option><option>Recorded data</option></select><select id="archive-topic" aria-label="Research topic"><option value="">All topics</option></select><button id="archive-reset" type="button">Reset filters</button></div><p id="archive-count" class="archive-count" role="status">Loading the index…</p><div id="archive-results"></div><button id="archive-more" class="more" hidden>Show more</button><noscript><h2>Technical notes</h2><p>Enable JavaScript for search and topic filtering.</p><ul>{fallback}</ul></noscript>'''
    (OUT / "archive.html").write_text(page("archive.html", "Research archive", body, "archive"))
    # Keep previously published companion URLs useful without maintaining a
    # second set of explanations or requiring a second documentation tool.
    legacy = OUT / "sphinx"
    if legacy.exists():
        shutil.rmtree(legacy)
    legacy.mkdir()
    redirects = {
        "index": "index.html", "manuscript": "guide/manuscript.html",
        "mathematics": "guide/mechanism.html", "research": "guide/results.html",
        "scope": "guide/results.html", "reproducibility": "guide/audits.html",
        "genindex": "archive.html", "search": "archive.html",
    }
    for name, target in redirects.items():
        url = "../" + target
        (legacy / (name + ".html")).write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta http-equiv="refresh" content="0; url={url}">'
            f'<link rel="canonical" href="{url}">'
            '<title>Murakami’s Dream — illustrated guide</title></head>'
            '<body><p>This material is now part of the illustrated guide. '
            f'<a href="{url}">Continue to the guide.</a></p></body></html>\n')
    repaired_fragments = repair_numbered_fragments(OUT)
    info = {"guide_chapters": len(CHAPTERS), "technical_notes": sum(r['type'] == 'Note' for r in records), "search_records": len(records), "figures": len([f for f in figures if f.suffix == '.png']), "literal_math_links_restored": len(restored_math), "numbered_heading_links_repaired": repaired_fragments, "unresolved_source_links": sorted(broken, key=lambda r: (r['source'], r['link']))}
    (OUT / "build-info.json").write_text(json.dumps(info, indent=2) + "\n")
    print(json.dumps({k: v for k, v in info.items() if k != 'unresolved_source_links'}, indent=2))
    print(f"Unresolved historical source links: {len(broken)} (recorded in docs/build-info.json)")
    current_broken = [row for row in broken if row['source'].startswith('book/')]
    if current_broken: raise SystemExit(f"Guide has unresolved links: {current_broken}")


if __name__ == "__main__":
    main()
