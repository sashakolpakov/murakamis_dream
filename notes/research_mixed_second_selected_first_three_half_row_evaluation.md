# A first-type-three adapter for the coupled half-row budget

Research implementation specification, 6 November 2026. This defines
an import-safe metadata adapter around the preserved half-row arithmetic.
It performs no reference or scalar calculation on import and supplies
no numerical half-row sign.

## 1. Why the same arithmetic applies

Use the original stationary reference for first three flags
\((0,1,\beta)\), \(\beta=0,1\), with position 1 unselected
and position 2 selected at \(H=1/100\). The
[first-type-three extension](research_mixed_second_selected_first_three_extension.md)
and the generic
[half-row budget](research_mixed_second_selected_half_row_budget.md)
give the original phase
\[
 F_0=Q_1(u;a,z)+Q_\beta(v;z,b)-g(z)-\frac\beta2g(b),
 \qquad p_L=g'(a+u)-g'(a)+2\pi iu.
 \tag{1}
\]
The incoming halfweight is absent, but this correct marginal still
makes the incoming trial force zero. The incoming joint convex cost
has coefficient \(1/2\) and remains nonnegative, so the proof may
discard it just as it does for first flag one.

The exact relative half-row trial, the forces \(A,P_\nu,D_b\),
the left-index conjugate and both remaining curvature constants are
therefore unchanged in form. They depend only on \(u,z,v,b\),
their original negative shapes and \(\beta\). The first-type-three
attached height \((-.072,.021)\) lies in the containing interval
\([-.078,.021]\) checked by the preserved helper. Its incoming
real reference lies in \(P=[.22,.45]\), and all other helper
coordinate guards are the same necessary ordinary bounds.

Thus the [preserved evaluator](../experiments/evaluate_mixed_second_selected_half_row_budget.py)
and its [outward arithmetic proof](research_mixed_second_selected_half_row_evaluation.md)
compute valid upper bounds for both full-\(P\) Fourier alternatives
when supplied with one certified first-type-three reference. The
caller must establish that reference, its original stationary equations
and its correct boundary tangents. A first-type-four reference record
or completed half-row sign cannot be substituted.

## 2. API and faithful metadata

The separate [adapter](../experiments/evaluate_mixed_second_selected_first_three_half_row_budget.py)
exports `initialize()` and
`evaluate_reference(e, shapes, coordinates, beta, gap)`.
The evaluator and primitive supplied in `e` are exactly the frozen
objects required by the preserved helper. The adapter verifies its
own pins, the preserved helper's initialization bindings, and its own
source hash. It returns first flag zero and the same operation caps.
Initialization performs metadata work only.

An evaluation calls the preserved helper once. Every primitive value,
force, conjugate, clipped rational quadratic, branch upper bound,
acceptance status, counter and partial arithmetic witness is returned
unchanged. The two caller-facing metadata fields `alpha` and `scope`
are replaced by their first-type-three meanings. This changes no phase
formula and does not relabel a first-type-four reference as a new root.

The added `alpha_adapter` record contains the preserved helper's path
and hash, its original hardcoded alpha-one label, the original values
of both replaced metadata fields, the complete original result's
canonical JSON hash, all adapter bindings, and the fact that exactly
one frozen helper call occurred. The original result is recovered
exactly by deleting `alpha_adapter` and restoring its saved `alpha`
and `scope`. Large arithmetic witnesses are stored once, not duplicated.
The old label is explicitly identified as legacy helper metadata, not
the source family of the supplied reference.

## 3. Guards, bounds and scope

The helper's original range and branch checks remain active, including
the positive left-index force, original primitive strip, both signed
quadratic branches, unchanged actual centers and full selected interval
\(P\). Both finite budgets are retained irrespective of their signs.
An arithmetic inconclusiveness stays inconclusive. Unexpected errors
propagate to the future caller, which must stop and archive them.
All bindings are checked before and after the single helper call.

Per reference there are still at most two half-row branch attempts,
six direct logarithmic-modulus calls, nine direct centered primitive
calls, one original left conjugate adding two centered primitive calls,
and three exact rational quadratic calculations. The adapter adds no
primitive, conjugate, reference, root, derivative or response call.
There is no command-line traversal, refinement, retry or precision change.

The adapter does not certify the supplied reference or a boundary cover.
A future uniform first-type-three half-row theorem would require new
same-reference values over complete external boundaries and the new
incoming response from (1), followed by the generic half-row extension.
No previously completed first-type-four response or phase bound is
transferred by correcting the metadata. Both first-type-three half-row
signs remain open until that separate calculation is completed.
