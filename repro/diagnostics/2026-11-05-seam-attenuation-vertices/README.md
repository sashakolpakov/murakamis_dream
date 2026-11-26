# Saved seam configurations at attenuation vertices

This is a bounded floating diagnostic, not an interval certificate or a
uniform sign theorem. It evaluates the exact repaired-halo upper proxy at
the candidate attenuation values proposed by the separate convexity argument:

    lambda in {0, 1, m_left, m_right},
    m_left  = min(L_b_left(x_-2), L_b_left(x_-1)),
    m_right = min(L_b_right(x_1), L_b_right(x_2)).

The cutoff b is .12 for a selected endpoint and .22 otherwise. Coincident
candidates are evaluated once. Every other physical coordinate and selection
is held fixed. The source ceiling is recomputed at each actual height from
the proved piecewise-affine profiles; the full collar, two original tangent
planes, exact physical-minus-repaired AA weights, selected halfcorrections,
and both occupation losses remain in the expression.

The input is the 29 saved physical seam witnesses. Both permitted q2
selections give 49 configurations. For each, this run uses the previously
saved reference inner halos and the previously saved grid-maximizing halos,
giving 98 fixed configurations. There is no new search over the physical
coordinates or inner halos. The actual reference vectors are read from the
archived original critical-reference data, and their original gradient
residuals are checked; no root solver proposes a new reference.

The result is:

| Check | Result |
| --- | ---: |
| Distinct attenuation-candidate evaluations | 214 |
| Interior chord checks | 348 |
| Largest candidate value | −.398044100526 |
| Largest observed interior value minus endpoint chord | 1.11e−16 |
| Largest discrepancy from prior saved proxy values | 1.03e−13 |
| New optimization jobs / interval cells | 0 / 0 |

The largest candidate is at lambda=0 for the actual repeated reference
word `(3,4,4)`, with all four relevant A-endpoint selections equal to one,
physical A reals

    (.2865535646267074, .24614987950139688,
     .4999991697968426, .27582371705838515),

and reference-valued inner halos
`(.3557012251159249,.3557012251159249)`. Both m values equal one.
At lambda=1 its value is `−.477182479916`.

The interior probes use fractions 1/4, 1/2, 3/4 of each interval between
successive distinct candidate values. They test a stronger chord comparison
as a bookkeeping check only. Numerical agreement with convexity does not
prove it. All candidate values are negative at these saved points, but
this does not bound unsampled physical coordinates, selections, or actual
reference windows.

As in the previous repair diagnostic, independent end corrections describe
runs of length at least three. For a length-two run, both repairs affect the
same AA edge and require one joint physical-minus-both-repaired difference.
Singleton runs have no AA edge. Neither short-run case is tested here.

## Reproduction

All helper imports are local to this directory. `phase_helpers.py` contains
only the original floating phase, weight and literal three-step formulas
extracted from the archived diagnostic helpers. It imports NumPy and SciPy;
it has no `/tmp` or absolute-workspace dependency. Data inputs are explicit
repository-relative paths and their hashes are recorded in `results.json`.
The local code hashes and original formula-source hashes are recorded as well.

From the repository root, choose a fresh output path:

```sh
python3 repro/diagnostics/2026-11-05-seam-attenuation-vertices/diagnose.py \
  --output /tmp/seam-attenuation-vertices-reproduction.json
```

The default output is this directory's `results.json`; the driver refuses
to overwrite an existing output. No upstream proof or canonical record was
modified.
