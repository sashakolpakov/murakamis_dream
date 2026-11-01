#!/usr/bin/env python3
"""Check generated navigation, local assets, and archive coverage."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re


# A malformed delimiter can bypass Pandoc's math spans altogether. Check
# visible prose as well; literal examples inside code and hidden MathML
# annotations are intentionally excluded.
RAW_TEX = re.compile(
    r"\\(?:[()\[\]]|(?:frac|dfrac|tfrac|operatorname|mathrm|mathbb|mathcal|"
    r"begin|end|sum|prod|lim|sqrt|alpha|beta|gamma|theta|lambda|sigma|"
    r"Omega|Phi|ell|zeta)\b)"
)
LITERAL_ELEMENTS = {"math", "pre", "code", "script", "style"}


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.images = []
        self.math_stack = []; self.math_errors = []; self.ids = set()
        self.literal_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in LITERAL_ELEMENTS:
            self.literal_depth += 1
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        if tag == "span" and "math" in attrs.get("class", "").split():
            self.math_stack.append({"depth": 1, "mathml": False, "text": []})
        elif tag == "span" and self.math_stack:
            self.math_stack[-1]["depth"] += 1
        if tag == "math" and self.math_stack:
            self.math_stack[-1]["mathml"] = True
        if tag == "merror":
            self.math_errors.append("MathML contains an error element")
        for key in ("href", "src"):
            if attrs.get(key): self.links.append(attrs[key])
        if tag == "img": self.images.append(attrs)

    def handle_data(self, data):
        if self.math_stack:
            self.math_stack[-1]["text"].append(data)
        if not self.literal_depth and not self.math_stack and RAW_TEX.search(data):
            self.math_errors.append("Literal TeX in prose: " + data.strip()[:180])

    def handle_endtag(self, tag):
        if tag in LITERAL_ELEMENTS:
            self.literal_depth -= 1
        if tag == "span" and self.math_stack:
            entry = self.math_stack[-1]
            entry["depth"] -= 1
            if not entry["depth"]:
                self.math_stack.pop()
                if not entry["mathml"]:
                    self.math_errors.append("Unrendered formula: " + "".join(entry["text"])[:180])


def main():
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    pages = sorted(docs.rglob("*.html"))
    if not pages: raise SystemExit("Build the guide first: python3 tools/build_book.py")
    failures = []; link_count = 0; image_count = 0
    parsed = {}
    for page in pages:
        parser = Links(); parser.feed(page.read_text())
        parsed[page.resolve()] = parser
    for page in pages:
        parser = parsed[page.resolve()]
        if "sphinx" not in page.relative_to(docs).parts:
            failures.extend({"page": str(page.relative_to(root)), "math": error}
                            for error in parser.math_errors)
        for value in parser.links:
            url = urlsplit(value)
            if url.scheme or url.netloc: continue
            target = (page.parent / unquote(url.path)).resolve() if url.path else page.resolve()
            if url.fragment and target in parsed and not url.fragment.startswith(":~:"):
                if unquote(url.fragment) not in parsed[target].ids:
                    failures.append({"page": str(page.relative_to(root)), "missing_fragment": value})
            if not url.path: continue
            link_count += 1
            if not target.is_relative_to(docs) or not target.is_file():
                failures.append({"page": str(page.relative_to(root)), "link": value})
        for image in parser.images:
            image_count += 1
            if not image.get("alt", "").strip():
                failures.append({"page": str(page.relative_to(root)), "missing_alt": image.get("src")})
    records = json.loads((docs / "assets/search.json").read_text())
    browse = json.loads((docs / "assets/browse.json").read_text())
    identity = lambda rows: [(r["url"], r["type"], r["topic"], r["status"]) for r in rows]
    if identity(browse) != identity(records):
        failures.append({"browse_index": "Metadata and full-text indexes disagree"})
    if not (docs / "library.html").is_file():
        failures.append({"library": "Research library was not built"})
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
