# Murakami’s Dream

Kashaev invariants, Conway tangle composition, and hyperbolic knot complements.

**[Read the illustrated research guide →](https://sashakolpakov.github.io/murakamis_dream/)**

[Manuscript and PDF](manuscript/README.md) ·
[Reproduce the certificates](repro/README.md) ·
[Sphinx documentation](https://sashakolpakov.github.io/murakamis_dream/sphinx/)

The current paper studies knots obtained from a specified class of
arbitrarily large finite Conway tangle trees, with independently
sufficiently long fixed signed twists. Its volume identity concerns the
resulting knot complement. Auxiliary crossing-circle cusps are filled;
the knot cusp remains unfilled. The composition rules and closure
restriction are part of the theorem.

![The route from the original quantum source to actual hyperbolic volume](book/figures/research-map.png)

The guide explains the argument in eight chapters. The **[research library](https://sashakolpakov.github.io/murakamis_dream/library.html)** organizes the detailed work into reading routes, with a main argument, its scope, and supporting notes. Audits and recorded results are linked from the notes they accompany.

The [figure gallery](https://sashakolpakov.github.io/murakamis_dream/figures.html) shows the research route, recoupling, cube channels, geometric cells, and the peripheral torsor. Figures include PDF and editable TikZ downloads, with SVG versions where available.

**The general volume conjecture remains open.** The repository contains internally reviewed research proofs for specified families, general local identities, and explicit obstructions to proposed extensions. Finite audits and numerical diagnostics retain their stated scope.

## Repository structure

| Directory | Contents |
| --- | --- |
| `manuscript/` | Detailed TeX manuscript, bibliography, editable figures and compiled paper |
| `repro/` | Serial exact-certificate runner, expected inputs and verification scope |
| `book/chapters/` | Readable guide: results, mechanism, geometry, frontier, notation, audits |
| `book/collections.json` | Curated research routes and their main arguments |
| `book/figures/` | Editable TikZ diagrams and compiled PNG, SVG, and PDF figures |
| `docs/` | Generated research guide; `site/` contains Sphinx sources and `sphinx/` its rendered edition |
| `notes/` | Detailed arguments at their original stable paths |
| `experiments/` | Audit scripts and recorded results |
| `tools/` | Guide builder and figure renderer |

All research routes are retained, including the cube, Fourier, torsor, and pretzel approaches. The previous long README is preserved in [the historical research log](RESEARCH_LOG.md).

## Local reading and reproduction

```sh
python3 repro/verify.py --output repro/results
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000`. The [guide maintenance instructions](book/README.md) cover rebuilding the site and figures. Research-audit dependencies are in `requirements-core.txt`; the guide explains the focused checks and their limits.

The publication manifest records source hashes and exclusions. The authored
paper and generated illustrations are included. Private background
manuscripts, credentials, environments, and session metadata are excluded.
