# Research guide sources

`chapters/` contains the readable guide. `figures/` contains editable TikZ sources and their compiled figures. `catalog.json` adds explicit topic and status labels to selected technical notes; uncatalogued notes retain the neutral “See note” status.

Run `python3 tools/build_book.py` from the repository root to regenerate `docs/`. Pandoc is required. Run `python3 tools/render_figures.py` to rebuild the figures with pdfLaTeX and PyMuPDF.

Run `python3 tools/check_book.py` after a build. It checks local navigation and image assets and verifies that every technical note is indexed. Rebuild and check the guide whenever notes or chapters are added or changed, before publishing the updated snapshot.

The original `notes/` and `experiments/` paths remain stable. The generated site provides topic navigation, full-text note search, and a separate audit/data archive without moving those dependencies.
