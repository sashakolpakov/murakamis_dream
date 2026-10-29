# Murakami’s Dream

Research on Kashaev invariants, pointed quantum A-structures, and hyperbolic volume.

**[Read the illustrated research guide →](https://sashakolpakov.github.io/murakamis_dream/)**

![The route from the original quantum source to actual hyperbolic volume](book/figures/research-map.png)

The guide explains the argument in seven chapters. The **[research library](https://sashakolpakov.github.io/murakamis_dream/library.html)** organizes the detailed work into seven routes, with a main argument, its scope, and supporting notes. Audits and recorded results are linked from the notes they accompany.

The [figure gallery](https://sashakolpakov.github.io/murakamis_dream/figures.html) shows the research route, recoupling, cube channels, geometric cells, and the peripheral torsor. Each figure has SVG, PDF, and TikZ downloads.

**The general volume conjecture remains open.** The repository contains internally reviewed research proofs for specified families, general local identities, and explicit obstructions to proposed extensions. Finite audits and numerical diagnostics retain their stated scope.

## Repository structure

| Directory | Contents |
| --- | --- |
| `book/chapters/` | Readable guide: results, mechanism, geometry, frontier, notation, audits |
| `book/collections.json` | Curated research routes and their main arguments |
| `book/figures/` | Editable TikZ diagrams and compiled PNG, SVG, and PDF figures |
| `docs/` | Generated website, topic navigation, and full-text search |
| `notes/` | Detailed arguments at their original stable paths |
| `experiments/` | Audit scripts and recorded results |
| `tools/` | Guide builder and figure renderer |

All research routes are retained, including the cube, Fourier, torsor, and pretzel approaches. The previous long README is preserved in [the historical research log](RESEARCH_LOG.md).

## Local reading and reproduction

```sh
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000`. The [guide maintenance instructions](book/README.md) cover rebuilding the site and figures. Research-audit dependencies are in `requirements-core.txt`; the guide explains the focused checks and their limits.

The publication manifest records source hashes and exclusions. Private manuscript inputs, credentials, environments, and agent metadata are excluded; the PDFs in `book/figures/` are generated diagrams.
