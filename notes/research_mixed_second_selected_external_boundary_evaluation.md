# A complete-boundary test for the second-position comparison

Research evaluation specification, 6 November 2026. The proposed
calculation covers both typed external domains for each outgoing flag,
with first flag one and second type four. Its purpose is to bound the
original central phase on the entire permitted reference family. The
two previously certified references at external coordinate \(1/3\)
are starting data for numerical proposals; they do not supply a bound
on the rest of either domain.

## 1. The theorem the calculation would establish

Use the domains \(K_3,K_4\) and the original phase defects
\(D_\nu\), with both complex boundary tangents retained, from the
[boundary-extension theorem](research_mixed_stationary_reference_boundary_extension.md).
The selected height is \(1/100\). For each fixed outgoing flag
\(\beta=0,1\) and external domain \(K_j\), a complete boundary
calculation must prove
\[
 D_\nu\le-\gamma\quad(\nu=0,1),\qquad
 \mathcal B=|p_L'a'|+|p_R'b'|\le B_0,
 \qquad \gamma>0.
\]
The target coordinates still range over their original horizontal
product. The proved index barriers and the fixed forced-branch interval
\([.4,.45]\) may reduce the scalar calculation; factorial dominance
below \(.4\) recovers both alternatives there.

On the whole boundary, also verify the strict image-height conditions
needed for target concavity. Each reference coordinate is holomorphic
on a neighborhood of \(K_j\) by the original existence and uniqueness
theorem. Applying the harmonic maximum and minimum principles to its
imaginary part extends these strict boundary height bounds throughout
the domain. The finite cover supplies uniform strict margins.

The [response theorem](research_mixed_second_selected_external_response.md)
then proves a uniform central gap if
\[
 \eta_j=\gamma-\frac{r_j^2B_0}{2}>0,
 \qquad r_3=83/1000,\quad r_4=3/50.
\]
The minimum boundary gap and maximum response are taken independently
over the entire boundary for the same flag and domain. They are not
paired cell by cell. The compensated gap has no whole-domain meaning
before that boundary is fully covered.

## 2. Exact boundary coverage

The [rational chart construction](research_mixed_second_selected_external_boundary_charts.md)
has five charts for \(K_3\) and four for \(K_4\), each with
real parameter interval \([-1,1]\). They include both semicircles,
both horizontal clipping segments, and the type-three oblique clipping
segment. With the two values of \(\beta\), there are exactly
18 cases. Junctions may occur in more than one chart and are retained.

The driver maintains a binary interval tree for every case. An exact
strict violation of a defining disk or half-plane inequality excludes
an entire chart interval. A failed or inconclusive numerical estimate
never does. A validated reference enclosure may also exclude actual
parameters if it has empty intersection with an independently proved
necessary canonical domain; its residual certificate and the exact
contradiction are then retained. All accepted, excluded, unresolved and pending leaves must
be prefix-free and have total binary mass one for each of the 18 trees.
This is a coverage check, not a replacement for the estimates at the
accepted leaves.

Before proposing a reference, split a nonexcluded interval whenever
the largest side of its exact Cartesian external-coordinate image
exceeds \(1/200\). These preliminary splits use only rational chart
geometry. For a line chart not excluded by its exact quadratic disk
test, some point of the line segment lies in the smaller typed disk.
After the width test, its midpoint is within \(\sqrt2/400<1/250\)
of that point. It therefore lies in the original existence disk:
the smaller and original radii are \(.083,.09\) for type three
and \(.060,.064\) for type four. Circle midpoints already lie in
the smaller disk. The full Cartesian image also lies strictly inside
the original external rectangle \(Q\); the provider checks this
directly as well.

## 3. Certified references and their responses

The [original-equation provider](../experiments/mixed_second_selected_external_reference.py)
uses one deterministic numerical proposal for each attempted cell.
The seed is always the saved canonical solution for that beta value.
There is no choice among replacement external parameters or alternate
initializations within a cell. Numerical proposals have no proof role.

For the exact chart midpoint \(c_0\), the provider records a rational
center \(q_0\) and rational derivative predictor \(T\). It bounds
the original gradient residual at
\(q_0+T(c-c_0)\), using its constant residual, linear defect and
the original third-derivative remainder. The entire affine image and
all connecting arguments must lie in their regular domains before
this Taylor estimate is used. The [residual theorem](research_mixed_prefix_residual_localization.md)
then encloses the canonical reference for every actual parameter in
the chart interval intersected with its typed domain. Existence is
supplied by the original geometric theorem, not inferred from a small
residual or a retained rectangle.

The raw affine/Taylor boxes remain separate from any intersection
with independently proved pointwise canonical bounds. Such certified
pointwise intersections may enclose the actual Hessian and derivative;
they may not replace the full-box inputs to the residual Taylor bound.
The provider certifies the derivative with respect to the complex
external coordinate \(c\), not with respect to the chart parameter.

The [response provider](../experiments/mixed_second_selected_external_response.py)
receives these same reference and derivative enclosures. It checks
the required common product and strict image heights, and encloses
the two original marginal derivatives and \(\mathcal B\).
The [curvature evaluator](research_mixed_second_selected_curvature_evaluation.md)
receives the same reference coordinates and negative-sign shapes.
It calls the frozen scalar evaluator once, then applies only its
proved guarded upper-bound improvements. Both original and improved
results are saved.

## 4. Resolution, limits and output

The [driver](../experiments/certify_mixed_second_selected_external_boundary.py)
uses 256-bit outward arithmetic and breadth-first subdivision over
all 18 trees. Its fixed caps are 12,000 visited nodes, 4,000 reference
attempts and binary depth 18. Every cell permits one numerical
reference proposal, one response calculation and one scalar-wrapper
call. A scalar call has at most two branch attempts, three node
conjugates and twelve centered primitive calls. No old source,
rational-transport or finite-quantum-sum routine is called.

Write \(g>0\) for the smaller of the two proved phase deficits on
a cell, and let \(w\) be the larger width of the two original scalar
budget enclosures. A cell has adequate phase resolution when either
\(g\ge1/200\), or \(w\le g/2\). This prevents a wide original
interval from delaying an already strong refined bound. The response
interval must have width at most \(\max(1/100,B_{\rm upper}/4)\).
These are computational refinement rules only. They are not extra
mathematical premises, and failure to meet them is not a counterexample
to a phase estimate. A finite positive upper bound may be refined
within the prescribed caps.

An interval that cannot be resolved at maximum depth is retained as
unresolved while the other cases continue. A cap preserves the entire
pending queue. An unexpected calculation error preserves its current
leaf as unresolved and stops the attempt. Final coverage or input-binding
failures are recorded and prevent any global conclusion.
An interrupt or termination signal requests a stop after the current
bounded cell calculation, so that the same frontier can be saved.

The output contains the complete new trees, exact geometric exclusions,
rational proposals and residual certificates, reference and derivative
enclosures, response witnesses, both scalar results, and the remaining
frontier. It computes compensated whole-domain gaps only after all
18 cases are complete and all immutable inputs still match. The frozen
348-leaf auxiliary-parameter frontier is neither changed nor replayed.

Even a successful uniform central comparison would leave the type-three
half-row terms, simultaneous boundary selections and other portions
of the full source to be treated. No knot-family or finite-exception
conclusion follows from this calculation alone.
