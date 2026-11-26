# Fixed-witness source-to-geometry assessment

This archive evaluates functions of the 4,409 existing reduced-disk
conditional-source witnesses. It proposes no roots, refines no cell and
changes no source certificate. `diagnose.py` checks all six type families
and both incidences at 320-bit precision. Its summary is diagnostic: in
particular midpoint positivity is not a uniform domain proof, and a wide
whole-cell enclosure is not a counterexample.

The evaluated vertex parameters are

    A3 = (1-U)(1-V)/4,    A4 = (2-U-V)/4,
    U = exp(-2*pi*i*s),   V = exp(-2*pi*i*t).

The edge-inferred neighbor parameter is

    B = -(1-L)^2*(1-U)/(4*L*(1-U*L)),  L = exp(-2*pi*i*a).

The exact shared cotangent simplifies to

    q = cot(pi*s) + cot(pi*a) - i.

The complete fixed witnesses give positive real and imaginary parts for
the own vertex A (whole-cell minima above .16396 and .24033). All type-four
own parameters also lie in both geometric lens disks. The corresponding
whole type-three lens claim is false on these independent external disks.

`verify_fixed_lens_failures.py` revalidates two already saved midpoint
root disks, retaining their original logarithmic lifts, and verifies the
strict inequalities |A3| > 1.02 and |1-A3| > 1.12. The exact parameter
angles, rational outward bounds and current source bindings are stored
in `fixed-lens-failures.json`. These are independent block parameters;
no actual coupled open-word critical point, positive unit-period solution,
or invariant is contradicted.

All saved midpoint cell-positivity and original unit-period tests were
favorable. The direct whole-cell nonlinear enclosures are inconclusive;
some branch expressions become nonfinite on those large enclosing boxes.
No uniform cell-positivity or logarithmic-period theorem follows from this
archive. The source proof and both source replays remain unchanged.

Reproduce:

    python3 repro/diagnostics/2026-11-05-source-geometry-signs/diagnose.py
    python3 repro/diagnostics/2026-11-05-source-geometry-signs/verify_fixed_lens_failures.py

A further proposed sufficient positivity test asks that each inferred
`t = sqrt(A^-1 - 1)` have imaginary part between -1 and 0. For positive
real and imaginary parts of A this is equivalent to

    4 Re(A)|A|^2 - Im(A)^2 > 0.

`verify_fixed_tangent_height_failure.py` uses the saved type-three
midpoint at the exact external angle pair (9/64,9/64). It verifies the
opposite strict inequality, with upper bound -1/100, from the original
tiny root disk. Here A is approximately .22385943+.73320560i and the
polynomial is approximately -.01133857. The record
`fixed-tangent-height-failure.json` binds every current source input.
This defeats a uniform test on the independent disk family. Actual
coupled-word restrictions exclude some of these external inputs and
remain a distinct possible route; no actual-word sign is inferred.

    python3 repro/diagnostics/2026-11-05-source-geometry-signs/verify_fixed_tangent_height_failure.py
