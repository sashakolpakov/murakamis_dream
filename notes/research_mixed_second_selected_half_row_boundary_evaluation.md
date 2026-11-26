# A boundary calculation for the outgoing type-three half row

Research evaluation specification, 6 November 2026.

The central comparison is complete for first type four and either
outgoing type. This calculation addresses the remaining outgoing
type-three half row. It uses the already certified references around
both complete external boundaries. There is no new critical-point
calculation or parameter subdivision.

## 1. The two bounds to be checked

Use the exact original phases, trial values, and gradients of
[the coupled half-row estimate](research_mixed_second_selected_half_row_budget.md),
with \(\alpha=1,\beta=0,H=1/100\). For each reference, equation
(28) of that note bounds the two original defects by
\[
 T_\nu+\phi_u^*(A)
 +\Gamma_{\mu_\nu}(P_\nu;.22-\Re z_*,.45-\Re z_*)
 +\Gamma_{57/10}(D_b;.22-\Re b_*,.45-\Re b_*),
 \qquad \nu=0,1,
 \tag{1}
\]
where \(\mu_0=32/5\), \(\mu_1=69/10\). The factorial branch
is \(\nu=1\), and the forced branch is \(\nu=0\).
Both are evaluated on the entire original interval \([.22,.45]\).
No main/main branch-domain restriction is imported.

The [half-row extension](research_mixed_second_selected_half_row_boundary_extension.md)
proves that the same reference response
\[
             \mathcal B=|p_L'a_*'|+|p_R'b_*'|
 \tag{2}
\]
and the same disk corrections apply as in the completed central
calculation. The original boundary height certificates, extended
harmonically, supply the hypotheses of that result. The new input
needed is a negative bound for (1) on each complete boundary.

For each domain, take the smallest proved boundary deficit
\(\gamma_R\) over both branches and every accepted reference interval.
Independently take the largest saved response upper bound \(B_0\)
over that entire domain. The whole-domain deficit is
\[
             \eta_R=\gamma_R-\frac{R^2B_0}{2},\qquad
 R=.083\ \text{for }K_3,\quad R=.060\ \text{for }K_4.
 \tag{3}
\]
It has proof status only when every nonexcluded terminal interval
has a finite valid bound. Positive values prove the uniform half-row
comparison. The additional comparison \(\eta_R>1/3200\) records
whether it preserves the common central theorem's stated gap; it
is not imposed as an unproved premise.

## 2. Reusing the entire certified reference cover

The input is the
[compact reference bank](../repro/results/research-mixed-second-selected-boundary-reference-bank.json),
with SHA-256
3e6e227ac78afcf214844376f7f0069259a4c3f0e7a9a755a6a57a8081a24bbb.
Its extraction retains the original source and audit associations,
all terminal geometry, coordinate and negative-shape enclosures,
derivative bounds, and boundary responses. It is a projection of the
completed certificate, not a replacement root certificate.

For outgoing flag zero there are 785 accepted reference intervals:
388 on \(K_3\) and 397 on \(K_4\). The other 58 terminal intervals
have strict geometric exclusions. Together these form complete
partitions on all nine boundary charts. The driver checks the case
inventory, terminal associations, payload hashes, prefix-free
partitions of total binary mass one, and every inherited input binding.
The reference boxes remain conditional on actual parameters in their
original chart intervals; no assertion of a finite suffix realizing
each box is used.

Each accepted reference is evaluated once with its own saved
coordinates and negative shapes. The new evaluator uses the same
original centered primitive and left scalar conjugate as the central
calculation. The other two gains are rigorous quadratic upper bounds.
Their displacement intervals contain every displacement allowed by
the saved center interval, and their force bounds retain both signs.
All values belong to the same reference interval. Reference coordinates
are never replaced by convenient midpoint parameters.

At most one left conjugate and eleven centered primitive calls are
permitted per reference. Both branch values and the scalar witnesses
are retained. There are no source-critical roots, derivatives of new
roots, matrix inversions, reference transport calls, or parameter
subdivisions. The driver disables the old reference/source callbacks.

## 3. Completion and unresolved estimates

The arithmetic precision is 256 bits. The fixed attempt visits all
785 saved references unless an unexpected error or explicit stop
signal prevents completion. A routine arithmetic failure is recorded
as unresolved and does not exclude that interval. A finite upper bound
of the wrong sign is also retained; it is an unsuccessful bound, not
a proof that the actual phase has that sign.

The [standalone driver](../experiments/certify_mixed_second_selected_half_row_boundary.py)
requires a new output path. Its scalar provider is specified in
[the half-row evaluation note](research_mixed_second_selected_half_row_evaluation.md).
The input bindings are checked before and after the run, and the
driver records its own source hash.

After the run, the driver records the successful, inconclusive, and
unvisited reference intervals together with the preserved exclusions.
Only a complete collection of finite half-row bounds allows (3) to
be interpreted on the entire domain. Input changes or an unexpected
error prevent a theorem claim. The original central certificate and
its reference bank remain unchanged.

Even if this attempt proves both half-row comparisons, it only
completes the second-selection finite product when the first two
blocks have type four and the first coordinate is unselected.
Simultaneous selections at the first two positions, first type three,
the other boundary positions and the regions outside the plateau
remain separate questions. No full knot-invariant conclusion follows
from this calculation alone.
