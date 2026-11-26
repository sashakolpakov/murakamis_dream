# Whole mixed-envelope minimum derivatives: bounded diagnostic

These are floating tests of the actual derivative after the one right
coordinate has been fixed at .5. They do not prove a uniform sign.
The four references are the original archived critical references for
types (0,1,1), (1,1,1), (0,1,0,1) and (1,1,1,1).
All their original gradient residuals are checked. No new reference,
word search or interval cover is constructed.

The driver makes 96 seeded trials per reference. Each chooses a moving
minimum adjacent to the right coordinate, all remaining real coordinates
between that minimum and .5, and permitted selections. It then runs one
bounded optimization per reference, retaining the selection pattern of
the lowest sampled derivative: 24 iterations, population multiplier 5,
no polishing. Thus there are four low-dimensional optimizations after
384 samples. The actual hybrid heights, moving neighbor heights,
chirp, Fourier halves and selected corrections are retained.

The four smallest derivatives found were approximately
.350830, .414382, .385041 and .355659, all positive. Three finite-difference
step sizes agree with the explicit envelope derivatives. The values
include all physical edge contributions; individual contributions can
be negative. The conservative local star, which omits positive height
contributions, is also recorded. Neither a floating positive minimum nor
the finite differences certify a global lower bound.

The separate relax.py replaces the two raw optimizing rows at those
four configurations by all four pairs from {.2,.4} squared. The smallest
whole directional trial is about +.080170. These are fixed endpoint
trials, with no additional parameter optimization. The exact derivative
endpoint reduction is established separately in
[the raw-row stationarity note](../../../notes/research_mixed_raw_row_stationarity.md);
the uniform outer-parameter inequality is still unproved.

Both drivers are standalone repository imports and retain input hashes.
Run from the repository root:

    python3 repro/diagnostics/2026-11-05-right-minimum-whole-star/diagnose.py
    python3 repro/diagnostics/2026-11-05-right-minimum-whole-star/relax.py

## A precise finite local inequality that would suffice

This specification is a reduction, not a claim that its inequality has
passed. Center the five positions at a moving nonright minimum
x_0=t in [.12,.22]. Fix the five types, their permitted selections, and
which of positions -2,-1,1,2 are right positions. A right target is
.5 at height zero. Every other x_j lies in [t,.5]; the endpoint
.5 may be retained as a closure of a nonright domain.

Write r=(t-.1)/.12, and use the original quadratic right profile
R(x)=1 up to .45, R(x)=400(.5-x)^2 afterward. For unselected
coordinates, let c_j=Im(reference_j). Their targets are

    z_0=t+i c_0 r,
    z_{±1}=x_{±1}+i c_{±1}R(x_{±1})r.

For an unselected outer coordinate at ±2, retain the actual immediate
cutoff correlation:

    z_{±2}=x_{±2}+i c_{±2}R(x_{±2})lambda_{±2},
    r <= lambda_{±2}
      <= min(rho_slow(x_{±2}),rho_slow(x_{±1})).

This releases only the unspecified positions ±3: any value in this
interval is obtained by an exterior slow cutoff between r and one.
If an outer position is right, its target is simply .5. Every selected
target is x_j+i(.014)R(x_j), because all fast left cutoffs are already
one. Its height derivative is zero. The five coefficients may be kept
in their actual correlated reference window. Replacing them by independent
typed intervals or conditional interval boxes is a further enlargement,
whose uniform inequality must also be proved before use.

Introduce three switches chi_{-1},chi_0,chi_1 in {0,1}, forced zero
at selected or right positions, and velocities

    v_0=1+i chi_0 c_0/.12,
    v_{±1}=i chi_{±1}c_{±1}R(x_{±1})/.12,
    v_{±2}=0.

Sum the directional derivatives on the four literal edges
-2 to -1 to 0 to 1 to 2. Coherent edges use the original partials
of phi. Raw edges use their original allocated row partial at one of
the two rows .2,.4, as justified by the separate endpoint reduction;
an RR edge contributes zero. Both original chirp orientations remain.
The selected correction has zero derivative here: stationary selected
targets do not move, and the only moving selected target is at t≤.22,
where the established strict branch is -2 pi H.

The desired sufficient inequality is that this **whole four-edge sum
is nonnegative for every retained switch and raw-row endpoint choice**.
Minimizing the switches gives exactly

    Re G_0 + sum_{j=-1,0,1} min{-(c_j R(x_j)/.12) Im G_j,0},

with the coefficient replaced by zero for selected or right positions
and with the corresponding raw partials substituted in G.
This is the old negative-height-cost local criterion, without splitting
it into separately nonnegative gauged halves. Its repeated-incidence
proof then applies to any set of simultaneous minima. For short cycles,
independently released positions enlarge the actual repeated-variable
domain; no edge or derivative incidence may be removed.

There are at most two affected raw edges in this five-position star,
so at most four independent raw-row endpoint assignments are needed.
Only cases whose four-edge neighborhood meets a right position are new
for the raw/coherent distinction. Additional tapered-A cases with real
coordinates above .45 must still be included even when a half is
coherent: a type-four coefficient c R(x) can lie above -.02 while
its height derivative remains nonzero. Such cases are not inherited
from the old 192/78 covers.

## Harmonic reduction of the outer A variable

If position +1 is right and position -1 is A, fix the center and
neighbor targets, their original height coefficients, and the switches.
The only dependence on an A outer target at -2 is

    Re[i chi_{-1} c_{-1}R(x_{-1})/.12
                       * phi_{outer,neighbor,b}(z_{-2},z_{-1})].

It is harmonic in that outer target on the established original
cotangent/source domain. Thus its minimum over an admitted closed
outer region is on that region's boundary. Convexity of the region
is not required. If chi_{-1}=0, the outer variable disappears.

After independently enlarging the outer reference coefficient to its
whole typed interval, an explicit containing region is given by
x_o in [t,.5] and the following two height boundaries. Set
m_o=min(rho_slow(x_o),rho_slow(x_{-1})).

    type3:              -.03 R(x_o)m_o <= h_o <= .02 R(x_o)m_o;
    unselected type4:   -.057 R(x_o)m_o <= h_o <= -.02 R(x_o)r.

A selected type4 outer target is the single curve h_o=.014R(x_o).
The lower/upper boundaries are piecewise linear, constant or quadratic,
with breakpoints t, min(x_{-1},.22), .45 and .5; there is also the
left vertical boundary. Every such target stays in the completed
early-cap/right-guard domain. This reduction retains the shared
neighbor coordinate in m_o rather than replacing it by an unrelated
height bound.

Consequently a whole star with one adjacent R has at most five
continuous parameters after this reduction: t, the other neighbor's
real coordinate, the two original center/neighbor height coefficients,
and one outer boundary parameter. A selected center or neighbor
removes the corresponding height parameter or switch. If the outer
position on the other side is also R, there are only four continuous
parameters; the focused face check fixes its first two.

This is not yet a universal five-dimensional theorem. A center with
no adjacent R but an R at distance two can retain another independent
coherent outer variable on the opposite side. Without a separately
proved half decomposition its whole-star domain can have seven
continuous parameters after harmonic reductions. Nor does this
argument establish monotonicity in t or in either neighboring real
coordinate. Those are precise remaining issues before a universal
checker can be claimed.
