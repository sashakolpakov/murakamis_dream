# A complete-boundary central test with a first block of type three

Research evaluation specification, 6 November 2026. This is a separate
bounded calculation for first three flags \((0,1,\beta)\),
\(\beta=0,1\). It covers both typed external domains using the
original first-type-three reference equations. The preserved
first-type-four driver, reference records and completed comparisons
are unchanged. No numerical result is supplied by this specification.

## 1. Original comparison and the whole-domain criterion

Use the canonical reference, allocated phase \(F_0\), and exact
central defects from the
[first-type-three extension](research_mixed_second_selected_first_three_extension.md).
Position 1 is unselected, position 2 is selected at \(H=1/100\),
and both real ordinary indices and all three retained real targets
are free on their original intervals. The incoming allocated halfweight
is absent. The original boundary marginals are
\[
 p_L=g'(a+u)-g'(a)+2\pi iu,\qquad
 p_R=g'(v+b)-(1+\beta/2)g'(b).
 \tag{1}
\]
For each fixed \((\beta,j)\), \(j=3,4\), the calculation must
bound both original Fourier alternatives on the entire boundary:
\[
 D_\nu\le-\gamma\quad(\nu=0,1),\qquad
 \mathcal B_0=|p_L'a'|+|p_R'b'|\le B_0,\qquad \gamma>0.
 \tag{2}
\]
The prime denotes differentiation with respect to the same complex
external coordinate \(c=s_4^*\), not a real chart parameter.

The generic index barriers and scalar estimates are proved for both
first flags. The factorial scalar calculation uses the full selected
interval \(P=[.22,.45]\); the forced calculation uses
\([.4,.45]\). The original factorial alternative dominates the
forced one below \(.4\), so both complete Fourier rates are bounded.
Both complex marginals in (1) remain in the underlying phase.

The [first-type-three response theorem](research_mixed_second_selected_first_three_external_response.md)
and original stationary boundary-extension identity imply a uniform
central gap on \(K_j\) if
\[
 \eta_j=\gamma-\frac{r_j^2B_0}{2}>0,
 \qquad r_3=83/1000,\quad r_4=3/50.
 \tag{3}
\]
The boundary minimum phase deficit and maximum response are taken
independently over the whole boundary of the same domain and flag.
Pairing favorable local gap and response values is not sufficient.
No compensated quantity is declared a whole-domain bound before all
eighteen chart cases are complete.

Each accepted cell must also verify the original common product and
strict image-height conditions. The new canonical reference is
holomorphic near each closed typed domain by the already proved
first-type-three existence and uniqueness theorem. Finite strict
boundary margins therefore extend throughout the domain by the harmonic
maximum and minimum principles. The first attached height lies in
\((-.072,.021)\), which is contained in the common target-concavity
interval \((-.078,.021)\). No first-type-four negative-height
bound is assumed for that attached coordinate.

## 2. Exact geometry and complete frontiers

The unchanged [rational chart construction](research_mixed_second_selected_external_boundary_charts.md)
has five charts for \(K_3\) and four for \(K_4\), each with
parameter interval \([-1,1]\). With both values of \(\beta\),
there are exactly eighteen cases. All circular arcs, horizontal and
oblique clipping segments and their junctions are retained.

Maintain a binary interval tree for each case, in deterministic
breadth-first order. A strict rational geometric witness may exclude
a whole chart interval. A validated residual enclosure may also exclude
actual canonical points if a necessary original domain intersection
is empty; its residual and contradiction are preserved. Arithmetic
inconclusiveness never supplies a geometric exclusion. Every accepted,
excluded, unresolved and pending terminal address must be prefix-free,
with total binary mass one in its own chart tree.

Before a reference proposal, split a nonexcluded interval if the largest
side of its exact Cartesian image exceeds \(1/200\). These splits
use only exact chart geometry. The chart midpoint is prescribed, not
chosen among alternatives. A nonexcluded line interval meets its smaller
typed disk; after this width test the midpoint is within
\(\sqrt2/400<1/250\) of such a point and hence in the original
existence disk. The radii are \(.083,.09\) for type three and
\(.060,.064\) for type four. Circle midpoint images lie in their
smaller disks. The provider additionally requires the full outward
Cartesian box to lie in the common rectangle \(Q\). An overhang is
inconclusive, not an exclusion.

## 3. New original references and responses

The [separate original-gradient provider](research_mixed_second_selected_first_three_external_reference_evaluation.md)
uses exactly one bounded proposal from its fixed rational seed for the
given \(\beta\). Every child starts from that same prescribed seed;
no parent-root warm start or replacement parameter is used. The seed
is not a canonical certificate, and no first-type-four canonical data
is used as proof or as a reference enclosure.

The new provider implements the explicit original \(\alpha=0\)
gradient, its analytic symmetric Jacobian and the rank-one forcing.
The separate pinned symbolic checker audits all seven gradient rows,
both Jacobians, external derivatives and Taylor coefficients against
the original unscaled action for both values of \(\beta\). This is
an algebraic identity check, not a numerical root or sign certificate.

For each cell, the provider certifies the full raw affine predictor
\(q_0+T(c-c_0)\), the original residual, linear defect and whole-image
Taylor remainder before applying necessary actual-reference intersections.
The original existence theorem and coercivity \(6\pi/49\) then
localize every canonical point over the chart interval intersected with
its typed domain. The changed private, auxiliary and attached rectangles
are used explicitly. The attached type-three coordinate is not clipped
to an ordinary type-three height rectangle.

On the certified actual-point boxes, the original Jacobian and Neumann
estimate enclose derivatives with respect to complex \(c\). The
[new response provider](../experiments/mixed_second_selected_first_three_external_response.py)
uses those same coordinates and derivatives, checks the entire common
product and strict heights, and evaluates (2). In particular its incoming
cotangent coefficient is one, with no former \(i\pi a'/2\) term.
First-type-four response values or bounds are not reused.

The frozen [curvature wrapper](research_mixed_second_selected_curvature_evaluation.md)
and its original directional helper read only \(u,z,v\), their
negative shapes and \(\beta\). Their reuse for first flag zero
is proved in the extension note, with the new original-reference
premises. They receive this cell's new coordinates and shapes. Both
the frozen result and its guarded rational refinements are preserved.
The new driver adds an explicit first-flag-zero provenance label to
the scalar envelope; this does not alter any frozen branch values.

## 4. Bindings and permitted calls

The [new driver](../experiments/certify_mixed_second_selected_first_three_external_boundary.py)
pins both new providers and specifications, the alpha-zero theory, exact
symbolic checker and result, unchanged geometry and scalar providers,
and the preserved first-type-four driver/specification as its reviewed
control-flow source. It verifies all direct hashes before imports.
It then merges and verifies the reference initialization bindings,
the response module's `PINNED`, the curvature wrapper's `PINNED`,
and the original primitive/conjugate provider's inherited bindings
before any numerical calculation. It verifies them all again at the end.
The old scalar provider's metadata-only dependency reader is used to
bind its unchanged primitive code, not to reuse old reference values.

Old reference, inspection, transfer and main callbacks are disabled.
Only the new original-gradient provider may propose and certify a
reference. Only its certified derivatives enter the new response.
The old evaluator supplies its original scalar conjugate and centered
primitive under the already proved alpha-independent formulas.
There is no finite quantum-source evaluation, old reference replay,
rational transport or old canonical-record input.

Outward precision is 256 bits. The fixed caps are 12,000 visited
nodes, 4,000 reference attempts and binary depth 18. Each cell permits
at most one new reference proposal, one response calculation and one
curvature-wrapper call. The reference's proposal itself has at most
twenty Newton steps at 50 decimal digits and forty-place rational
rounding, with no retry. A scalar call has at most two branch attempts,
three node conjugates and twelve centered primitive calls.

## 5. Acceptance, stopping and exact output

Let \(g\) be the smaller of the two certified cell phase deficits,
and \(w\) the larger width of the two original scalar budget
enclosures. Adequate phase resolution requires \(g>0\) and either
\(g\ge1/200\) or \(w\le g/2\). The response width must be at
most \(\max(1/100,B_{\rm upper}/4)\). These are the same fixed
refinement rules as the preserved driver; they do not change the
mathematical criterion (3). A finite positive upper budget may be
subdivided within the prescribed caps, without being called a source
counterexample or an exclusion.

At maximum depth an unresolved leaf is retained while other cases
continue. A node or reference cap preserves the full pending queue.
An unexpected error preserves the current leaf as unresolved and stops
the attempt. Signals request a stop after the current bounded cell,
so its frontier can still be saved. Coverage or input-binding failure
prevents every whole-domain theorem claim.

The output records first flag zero on nodes, terminal and pending leaves,
scalar envelopes, domain summaries and the overall result. It retains
all eighteen trees, exact chart intervals and boxes, exclusions, fixed
seeds, rational proposals, residual and derivative certificates,
response witnesses, original and improved scalar bounds, counts and
unresolved or pending frontiers. The forest identity is
\(\#\text{visited}+\#\text{pending}=2\#\text{frontier leaves}-18\).
Only complete coverage with unchanged inputs permits the four separate
global minimum-gap/maximum-response corrections in (3).

The fresh output path must end in `.json.gz`. The driver streams the
complete JSON object through `gzip.open` in exclusive text mode at
compression level one; it drops no fields or witnesses. The reported
SHA-256 binds the compressed file bytes. Saved-data readers must decompress
that file before parsing its unchanged JSON structure. No old source
record is compressed or otherwise modified.

The prospective conclusion is a central main/main estimate for first
type three, with the first coordinate unselected. Outgoing type-three
half-row signs remain a separate calculation; the outgoing type-four
half row already has its independent pointwise comparison. No full
finite-source, plateau, whole-invariant or finite-exception theorem is
claimed by this driver. No numerical execution is authorized by this
specification itself.
