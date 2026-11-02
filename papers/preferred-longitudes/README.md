# Preferred longitudes of Conway tree complements

This classical paper proves the preferred-longitude product for the actual marked Conway tree representation. It separates boundary isotropy, the generic constant field, regular reconstruction through every nonzero main-meridian value, preferred-cusp calibration, and the determinant-one sign. Zero-circle insertion then identifies the same formula for arbitrary strict bare junctions, including the possible half-label fold.

The geometric inputs are the original ordered representation and positive filled germ in `nonparabolic-tree-geometry`, and the strict complete/marked filling construction in `strict-conway-geometry`. The only finite polynomial input is the local complete Newton trace; its elementary sine-coefficient rate identifies a hub action. No knot-invariant asymptotic or recurrence theorem is a premise.

Build from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The bounded exact checker requires Python 3 and SymPy. From the repository root:

```sh
python3 -I papers/preferred-longitudes/check.py --output /tmp/preferred-longitudes-check.json
```

It checks rational identities symbolically, including the actual character transports and cusp rebasing matrices. The finite integer cases check the framing convention and lift parity; they are not the proof for all integers. The checker deletes any old output before rejecting optimized Python, pins its own source and paper files before and after execution, and includes four controls that fail for altered inverse, differential, endpoint-orientation, and surgery conventions.

The written proof, rather than the checker, supplies the algebraic generic-fiber argument, existence of open sets in every nonzero fiber, actual peripheral paths, spin sign, and analytic stationary elimination. It does not identify a different unfilled exterior or infer a geometric branch from exponentiated slope equations alone. There is no claim of a quantum volume limit or an annihilator in this paper.
