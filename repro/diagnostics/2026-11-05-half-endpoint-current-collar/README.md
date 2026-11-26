# Fixed contour-current diagnostics for a possible .55 collar

Archived 5 November 2026. These are floating diagnostics, **not** interval
enclosures or a complete finite-source theorem. No parameter cover or
expanded search is included. All scripts and inputs needed to reproduce
the fixed tests are local to this archive.

The question is whether the original conditional packet can extend to
a real right argument in [.5,.55], with its other argument in the typed
left cap, plateau, or right taper. The existing
[coherent collar theorem](../../../notes/research_mixed_coherent_half_endpoint_collar.md)
gives only an unquantified width. The
[interface source](../../../notes/research_mixed_left_right_interface_source.md)
and [right square source](../../../notes/research_mixed_unselected_right_taper_products.md)
retain the full finite currents, but do not certify .55.

## Rate and numerical root conventions

The driver uses the original canonical phase

    Q(s;a,b)=g(s+a)+g(s+b)−(2+epsilon)g(s)+2*pi*i*a*s.

Below the axis, g is the periodic dilogarithm primitive. Above the axis
it is the marked continuation
`g_plus(z)=conjugate(g_minus(conjugate(z)))+i*pi*(z-z*z)`.
Thus shifted factorial walls and the upper full-period polynomial are
retained. The alias comparison subtracts `2*pi*abs(Im s)`.

Each root is proposed by the exact-form quadratic or cubic polynomial,
then checked in floating arithmetic for the original zero logarithmic
residual and regular critical factorial strips. This is not a certified
root disk or a proof of contributing-current selection. The
[exact cubic collision note](../../../notes/research_mixed_right_cubic_collision.md)
explains why that distinction matters beyond the half-period.

The ten fixed A values are written in the driver; they are paired with
right arguments .5 and .55, both orientations, and both inner types,
giving 80 cases. The +.02 tests use the wider type-three upper height
even in some cross-type checks; they do not assert that this height is
an actual type-four hybrid target. No actual cyclic reference is inferred
from an endpoint height such as −.057.

## What the fixed tests found

* `old_remote_upper.json`: the inherited remote height +2 loses its
  absolute upper-alias gap at the fixed real point
  `(a,b,epsilon)=(.1,.55,1)`: the gap is approximately −.36548096.
  At height +.5 the same point has gap approximately +.10778967.
* `selected_height_currents.json`: at
  `(a,b,epsilon)=(.22−.057i,.55,1)`, the selected-height right endpoint
  exceeds the proposed saddle action by approximately .00079004.
  Thus the old whole-horizontal maximum argument cannot simply be reused.
* `cut_04_currents.json`: returning to the real axis at .4 fails even
  at `(a,b,epsilon)=(.1,.5,1)`, with sampled tail/join gap −.08576108.
* `cut_half_currents.json`: moving the return cut to .5 gives positive
  sampled margins on the same 80 cases. Their minima are .032045 for
  the left tail/join, .161242 for the real right tail, .077109 for the
  right join, .003104 for the saddle-height segment outside radius .04,
  and 1.17752/.250368 for the lower/upper aliases at heights ±.35.

These positive values are only feasibility evidence. The current
records do not bound intervals between grid points or between parameter
samples. Missing ingredients include a uniform low-horizontal maximum,
the joining-current bounds over the whole parameter domain, and the
wall-safe contour implementation with the original finite rows and
normalization. No .55 packet, geometric gap, or full-period asymptotic
is concluded. The failed current comparisons are also not finite-sum
counterexamples: another coherent contour may work.

## Reproduction

From the repository root, choose a separate output directory:

    python3 repro/diagnostics/2026-11-05-half-endpoint-current-collar/replay_fixed_diagnostics.py --output-dir YOUR_OUTPUT_DIRECTORY

This needs NumPy and SciPy. It repeats the fixed diagnostic only, with
no optimizer, parameter subdivision, or new cover. Floating results
may differ in the last digits across library versions. The manifest
hashes the archived scripts/results and the source notes read during
the investigation; those source notes are not silently enlarged.
