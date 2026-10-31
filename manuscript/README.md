# Long-twist volume manuscript

[Read the manuscript (PDF)](build/main.pdf)

`main.tex` is the authored mathematical manuscript for the completed-root Conway theorem. It includes explicit invariant normalization, finite Hermite–Newton source identities, strict-state geometry, exact alias certificates, the complex packet, and the complete filling transform. Technical appendices carry the detailed finite and analytic arguments.

Build from the repository root:

```sh
python3 tools/build_manuscript.py
python3 tools/build_sphinx.py
python3 tools/build_book.py
python3 tools/check_book.py
```

The paper is written to `manuscript/build/main.pdf`; the Sphinx reading site is written to `docs/sphinx/`; the existing Markdown book remains in `docs/`. The book build copies the paper to `docs/papers/conway-composition.pdf`. Building documentation does not execute research scripts.

Replay the exact finite certificates separately:

```sh
python3 repro/verify.py --output repro/results
```

See `repro/README.md` and `repro/PROOF_INPUTS.md` for the distinction between proof, exact certificate verification, and supporting finite audits. TeX Live/MacTeX with `latexmk` and the ordinary LaTeX packages used by `main.tex` is required. Sphinx dependencies are listed in `repro/requirements-docs.txt`.

The theorem fixes the finite expression and half-twist pattern first, then permits all independently sufficiently long signed integral auxiliary fillings, fixed before the all-level limit. It does not assert the volume conjecture for every arborescent knot. The main knot cusp remains unfilled. No author attribution or external peer-review claim is inferred from this repository's internal review records.
