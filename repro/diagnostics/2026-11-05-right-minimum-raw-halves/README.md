# A fixed raw-half check for minimum transport

This archive contains four floating scalar root solves, with no parameter
search. The moving unselected type-four target is fixed at
`t=.22`, `h=-.057`, with left derivative `h'=-.057/.12`; the right
target is `.5`. It tests the two own-factorial indicators and both
orientations as independent enlarged domains, rather than claiming that
all four are actual cyclic configurations. The negative value below is
not an outward certificate or a failure of whole minimum transport.

The complete reduced raw row uses the original chirp. At negative
height the true Fourier half of the moving type-four target is its
factorial branch. Thus its complex target derivative at a row `u` is

    K_d = g'(t+ih+u) - (3/2)g'(t+ih) + 2 pi i d u,

where `d=1` means that the moving argument is first. The old left/right
half decomposition adds `+1.5i` for `d=0` and `-1.5i` for `d=1`.
These gauges cancel only when the two incident halves are added.

The type-four/first-argument case has row approximately
`.2658096999327`. Its ungauged path derivative is approximately
`+.7101823987811`, but its old gauged half is approximately
`-.00231760121889`. Hence separate positivity of those old halves
cannot be presumed on this enlarged height box. A paired derivative
comparison, sharper reference correlation or a different gauge remains
possible. The original conditional sums and the new raw upper envelope
must not be interchanged in making that comparison.

## An analytic row-interval simplification

The strict row concavity proved in
[the raw right-row theorem](../../../notes/research_mixed_complex_right_row_reduction.md)
gives a unique maximizing row. For a moving target with real part
`t in [.12,.22]`, arbitrary `|h| <= .057`, and right angle `.5`, its
row derivative has the form

    E'(u) = log(2 cos(pi u)) + log|1-R exp(-2 pi i(t+u))|
            - (2+epsilon)log(2 sin(pi u)) + lambda,
    R=exp(-2 pi |h|), 0 <= lambda <= 2 pi |h|.

The Fourier branches are constant in the row. Elementary exact bounds
give `R>2/3`, `lambda<.36`. At `u=.2`, `cos(2 pi(t+.2))<0`, so

    E'(.2) > log[(8/5)(sqrt(13)/3)/(6/5)^3]
            = log(25 sqrt(13)/81) > 0.

Here `cos(pi/5)>4/5` and `sin(pi/5)<3/5`; the last inequality follows
from `8125>6561`. At `u=.4`,

    E'(.4) < log[(2/3) 2/(9/5)^2] + .36
            = log(100/243)+.36 < 0,

using `2 cos(2 pi/5)<2/3` and `2 sin(2 pi/5)>9/5`.
The elementary exponential bound
`exp(.36) <= 1+.36+.36^2/[2(1-.36/3)] < 3/2`
proves both the asserted radial bound and the final strict sign.
Therefore the exact maximizing row lies in `(.2,.4)` throughout this
compact target domain. This conclusion uses the proved row concavity,
not the floating solves in the driver.

The new local task is consequently a compact derivative comparison.
It still includes the height changes of adjacent A rows and the true
selected Fourier terms. Existing wholly coherent half-stencil covers
stop at neighbor real `.45`; neither a raw `.5` neighbor nor arbitrary
partly tapered type-four derivatives are imported from those covers.

Run from the repository root:

    python3 repro/diagnostics/2026-11-05-right-minimum-raw-halves/probe.py
