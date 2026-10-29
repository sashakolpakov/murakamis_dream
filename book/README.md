# Research guide sources

`chapters/` contains the readable guide. `figures/` contains editable TikZ sources and their compiled figures. `collections.json` defines the research library's seven reading routes, entry arguments, and supporting notes. `catalog.json` adds explicit topic and status labels to selected technical notes; uncatalogued notes retain the neutral “See note” status.

Read the guide as chapters: [overview](chapters/index.md), [results](chapters/results.md), [mechanism](chapters/mechanism.md), [geometry](chapters/geometry.md), [frontier](chapters/frontier.md), [notation](chapters/notation.md), and [audits](chapters/audits.md). The published [research library](https://sashakolpakov.github.io/murakamis_dream/library.html) is the thematic entrance to the detailed work.

Each diagram in the guide includes links to its scalable SVG, print-ready PDF, and editable TikZ source.

The [figure gallery](figures.md) gathers the diagrams with explanations and links to the chapters that use them. It is built as a separate reference page, leaving the seven-chapter reading sequence intact.

From the repository root, rebuild in this order:

```sh
# Only when TikZ sources change; requires pdfLaTeX with TikZ and PyMuPDF.
python3 tools/render_figures.py

# Requires Pandoc; copies the compiled figures into the site.
python3 tools/build_book.py
python3 tools/check_book.py
```

PyMuPDF is an optional documentation dependency; install it with `python3 -m pip install PyMuPDF` in your Python environment. Reading the committed guide requires none of these build dependencies.

The check verifies local navigation, image assets, and that every technical note is indexed. Rebuild and check the guide whenever notes or chapters are added or changed, before publishing the updated snapshot.

The original `notes/` and `experiments/` paths remain stable. The generated site provides topic navigation, full-text note search, and a separate audit/data archive without moving those dependencies.

To maintain the organization, add an entry to `collections.json` only when it helps a reader follow a research route; place an explicit topic/status in `catalog.json` when its scope has been checked. The builder links a note to `audit_<note-stem>.py` and `<note-stem>_results.json` when those exact files exist. This is a navigation relationship, not a claim that a computation proves the note.

Archive browsing loads `assets/browse.json`, a short metadata index. Full-text search loads `assets/search.json` on demand. Query, type, and topic filters are retained in the URL, so a filtered archive can be bookmarked or shared.
