# Sources for the research guide

This directory contains the illustrated guide. It introduces the knot
invariant, explains the diagram classes covered by the retained results,
and shows how their quantum estimates and hyperbolic geometry fit
together. The guide also explains approaches whose applications remain
open. It is the maintained web exposition; the papers give the detailed
theorem statements and proofs.

The results have several distinct hypotheses. The planar theorem decorates
a diagram encoded by a matched triangulated sphere before imposing long
signed twists. The ordered-tree theorems instead use the stated recursive,
summed, or local degree-and-twist conditions. All require the specified
strand connections to give a knot. The diagram and powers are fixed
before the level tends to infinity. The guide also presents partial
results about finite sources and geometric contributions, with their
more limited conclusions.

Begin with [the knot diagram and its finite evaluation](chapters/starting.md).
It defines tangles, twist counts, auxiliary filling, the finite
contraction, coefficient extraction, and the order of limits. Continue
with [the results and their hypotheses](chapters/results.md),
[how the proofs work](chapters/mechanism.md), and
[the geometric volume](chapters/geometry.md).
The [methods chapter](chapters/methods.md) explains the broader approaches,
their mathematical tools, and their literature references.
The [algebraic approaches chapter](chapters/algebraic.md) works through
the factorial move test, Hilbert 90, Koszul complexes, cyclotomic
rigidity, Regge symmetries, and descent from a cover.
[Remaining questions](chapters/frontier.md), [notation](chapters/notation.md),
and [reproduction](chapters/audits.md) are reference chapters.
The [research library](https://sashakolpakov.github.io/murakamis_dream/library.html)
connects these explanations to the detailed arguments and historical notes.

For a particular theorem, use the
[dependency graph](../docs/papers/dependencies.html) and its **recorded
proof route** to find the prerequisites in order. A shared result appears
once in that route. The [manuscript chapter](chapters/manuscript.md)
explains why the frozen account reached 374 pages and how the current
21 subject drafts, totaling 403 pages, differ from it. The drafts are
provisional groupings; splitting alone has not shortened the collection.

The [closing assessment](../repro/RETAINED_RELEASE_ASSESSMENT.md) states
what the retained-results review covered. Analytic and geometric proofs
remain written proofs; the Lean results verify their stated mathematical
implications without providing an end-to-end formal knot theorem.
Former Sphinx URLs redirect to this guide; there is no separate Sphinx
source or build to maintain.

## Files and diagrams

The chapter sources are in the chapters directory. The figures directory contains editable TikZ drawings and their PDF, SVG and PNG versions. The [figure gallery](figures.md) explains what each diagram represents and links it to the relevant chapter. A schematic diagram illustrates a construction; it is not a substitute for its labeled face-pairing or analytic proof.

The file collections.json organizes the technical library into reading routes. The file catalog.json records topic and status descriptions where these have been supplied. An uncatalogued note has the neutral label “See note”; absence of a catalog entry does not change its mathematics. The original notes and experiments directories stay in place so existing proof and script links remain usable.

## Rebuilding the guide

Reading the committed guide needs no build software. To rebuild it from the repository root, use:

    python3 tools/build_book.py
    python3 tools/check_book.py

The build requires Pandoc. It converts the formulas to native MathML and
copies the figure assets into the static site. It also renders the
[reference errata](../manuscript/ERRATA.md) as a page linked from the
manuscript chapter. The check examines local
navigation, image assets, and the technical-note index. It also detects
failed MathML conversion and common TeX commands left visible in prose,
including malformed delimiters. Literal code examples are excluded.
These are rendering and publication checks; they do not verify the
mathematical proofs.

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
