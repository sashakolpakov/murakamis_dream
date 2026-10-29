#!/usr/bin/env python3
"""Check generated navigation, local assets, and archive coverage."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            if attrs.get(key): self.links.append(attrs[key])
        if tag == "img": self.images.append(attrs)


def main():
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    pages = sorted(docs.rglob("*.html"))
    if not pages: raise SystemExit("Build the guide first: python3 tools/build_book.py")
    failures = []; link_count = 0; image_count = 0
    for page in pages:
        parser = Links(); parser.feed(page.read_text())
        for value in parser.links:
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path: continue
            link_count += 1
            target = (page.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(docs) or not target.is_file():
                failures.append({"page": str(page.relative_to(root)), "link": value})
        for image in parser.images:
            image_count += 1
            if not image.get("alt", "").strip():
                failures.append({"page": str(page.relative_to(root)), "missing_alt": image.get("src")})
    records = json.loads((docs / "assets/search.json").read_text())
    expected = {"notes/" + p.stem + ".html" for p in (root / "notes").glob("*.md")}
    indexed = {row["url"] for row in records if row["type"] == "Note"}
    if expected != indexed:
        failures.append({"archive_coverage_missing": sorted(expected - indexed), "archive_coverage_extra": sorted(indexed - expected)})
    for row in records:
        if not row["url"].startswith("https:") and not (docs / row["url"]).is_file():
            failures.append({"search_link": row["url"]})
    build = json.loads((docs / "build-info.json").read_text())
    failures.extend(build["unresolved_source_links"])
    result = {"status": "PASS" if not failures else "FAIL", "HTML_pages": len(pages), "local_resource_links": link_count, "images_with_alt": image_count, "technical_notes_indexed": len(indexed), "search_records": len(records), "failures": failures}
    print(json.dumps(result, indent=2))
    if failures: raise SystemExit(1)


if __name__ == "__main__":
    main()
