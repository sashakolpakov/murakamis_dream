# Research guide sources

`chapters/` contains the readable guide. `figures/` contains editable TikZ sources and their compiled figures. `catalog.json` adds explicit topic and status labels to selected technical notes; uncatalogued notes retain the neutral “See note” status.

Each diagram in the guide includes links to its scalable SVG, print-ready PDF, and editable TikZ source.

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
