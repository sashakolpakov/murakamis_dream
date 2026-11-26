# Sources for the research guide

This directory contains the readable account of the results and their proofs. The guide starts with the knot invariant and the class of diagrams covered by the theorem, explains how the quantum estimates and hyperbolic geometry fit together, and separates those results from questions that remain open.

The main theorem now applies to every fixed strict Conway composition tree with sufficiently long independent signed twist weights, provided its actual endpoint pairing gives a knot. For this class, estimates for the full quantum sum and a nonzero geometric contribution are proved. The resulting limit is the volume of the actual knot complement. A further corollary writes the same limit through a genuine quantum \(A\)-operator with fixed finite initial data, or through a positive determinant ratio. The guide does not assert a theorem for all knots, arbitrary short twists, or all arborescent presentations.

Read the chapters in this order: [overview](chapters/index.md), [results](chapters/results.md), [how the proof works](chapters/mechanism.md), [the geometric volume](chapters/geometry.md), [remaining questions](chapters/frontier.md), [notation](chapters/notation.md), and [reproduction](chapters/audits.md). The [research library](https://sashakolpakov.github.io/murakamis_dream/library.html) then provides reading routes into the detailed proofs. A link to a technical note identifies the precise statement used; the note remains authoritative for its hypotheses and conventions.

## Files and diagrams

The chapter sources are in the chapters directory. The figures directory contains editable TikZ drawings and their PDF, SVG and PNG versions. The [figure gallery](figures.md) explains what each diagram represents and links it to the relevant chapter. A schematic diagram illustrates a construction; it is not a substitute for its labeled face-pairing or analytic proof.

The file collections.json organizes the technical library into reading routes. The file catalog.json records topic and status descriptions where these have been supplied. An uncatalogued note has the neutral label “See note”; absence of a catalog entry does not change its mathematics. The original notes and experiments directories stay in place so existing proof and script links remain usable.

## Rebuilding the guide

Reading the committed guide needs no build software. To rebuild it from the repository root, use:

    python3 tools/build_book.py
    python3 tools/check_book.py

The build requires Pandoc. It converts the formulas to native MathML and copies the figure assets into the static site. The check examines local navigation, image assets and the technical-note index. It checks the publication structure, not the truth of the mathematical proofs.

When a TikZ figure changes, regenerate its PDF, SVG and PNG first:

    python3 tools/render_figures.py
    python3 tools/build_book.py
    python3 tools/check_book.py

Figure rendering requires pdfLaTeX with TikZ and the optional Python package PyMuPDF. The latter can be installed in a suitable environment with:

    python3 -m pip install PyMuPDF

The generated site can be inspected locally with:

    python3 -m http.server 8000 --directory docs

## Maintaining the library

Add a reading-route entry when it helps explain a sequence of arguments, and give a status description only with the scope of the linked result in view. The builder can associate a note with a correspondingly named audit script and result file. That association makes the computation reproducible; it does not mean a finite computation proves an asymptotic theorem.

Archive browsing uses a small metadata index. Full-text search loads its larger index only when requested. Search and topic filters are stored in the URL, so a selected part of the library can be shared without moving any underlying files.
