# The first product-boundary calculation stops without a uniform bound

Research record, 6 November 2026. The bounded calculation specified in
[the center-comparison note](research_mixed_third_selected_center_comparison.md)
has now been performed. It stopped at the first unresolved interval at
the prescribed subdivision depth. It therefore does not prove the
comparison over the whole parameter domain. The earlier eight-center
result remains valid with its original scope.

## 1. What was evaluated

The [driver](../experiments/certify_mixed_third_selected_product_boundary.py)
started with all 162 products of boundary charts. Each retained cell
used the original four-leg equations, one numerical reference proposal,
and a residual enclosure justified by the previously proved accretive
Hessian bound. Numerical convergence was not used as a root certificate.
The [implementation proof](research_mixed_third_selected_implementation.md)
explains both this residual bound and the target estimates.

For every enclosed reference, the calculation retained all twelve or
six required profiles. A rational target and the proved concavity gave
an upper bound on the entire real target box. The centered boundary
correction was then subtracted with its lower endpoint. This correction
is required by the maximum-principle argument; its nonpositive sign
does not permit it to be omitted.

The fixed limits were 256-bit arithmetic, combined binary depth sixteen,
4,000 visited cells, and 2,000 reference proposals. The requested gap
was \(\delta=1/2000\). No limit was increased and no alternative
seed was tried.

The [saved record](../repro/results/research-mixed-third-selected-product-boundary-attempt01.json.gz)
has SHA-256
`e63cdc8ceb70046bac13ba855542657623c4b00e792ad367b0d7369c914a461e`.
It contains 26 visited cells: 17 subdivided cells, six strict geometric
exclusions, two accepted cells, and one unresolved cell. The untouched
frontier contains 170 cells. All 162 chart domains retain complete
prefix partitions when the unresolved and pending cells are included.
There were twenty reference proposals and twenty residual certificates,
followed by 240 target proposals and interval-comparison attempts.
Of these, 192 returned completed bounds and 48 returned inconclusive
enclosures. All 27 input bindings were unchanged at completion.

Complete bookkeeping is not a completed inequality: unresolved and
pending cells are part of the recorded domain, not accepted cells.

The [saved-data checker](../experiments/check_mixed_third_selected_product_boundary_record.py)
subsequently verified the exact chart images, all 162 partitions,
residual bounds and necessary intersections, and the 192 completed
support bounds with their original boundary corrections. Its
[result](../repro/results/research-mixed-third-selected-product-boundary-saved-audit.json)
has SHA-256
`9aa582ab0e3ab3914bd89737ed84e5963ee7bf65280ba1e2084bacf7e7b50647`.
It checks saved rational arithmetic and file associations; it performs
no new root or special-function evaluation. The result explicitly
retains the negative answer to the question of full-domain completion.

## 2. The comparison that prevented acceptance

The unresolved cell is in the first chart case, with both external
coordinates on the left semicircle of \(K_3\), and outgoing flag
\(\beta=0\). Its binary address is `0000110000111110`. Its exact
parameter intervals are
\[
 I_a=[-89/128,-11/16],\qquad I_c=[-45/64,-89/128].
\]
The reference radius from the full affine residual was less than
\(4\cdot10^{-6}\). The unresolved comparison uses the main
index profile on both factors and the factorial alternative
\(\nu=1\).

Let \(U\) be the saved original support upper bound and let
\(C_0^-\) be the lower endpoint of the centered boundary correction.
Rounded values for this profile are
\[
 U\simeq-0.0159584880,\qquad
 C_0^-\simeq-0.0161827681,\qquad
 U-C_0^-\simeq0.0002242801.
\]
The necessary acceptance test is \(U-C_0^-<-1/2000\), which
this enclosure does not establish. The other eleven profiles in this
cell pass that test.

The saved enclosure for the original defect at the proposed target is
contained in
\[
 [-0.075354,-0.018630].
\]
The additional target-support cost is less than \(0.002673\).
Thus the direct evaluation has a substantial interval width before
the compensation is subtracted. This is a failure of the present upper
enclosure to certify the desired sign. It proves neither a positive
maximum of the corrected defect nor a competing contribution to the
original quantum sum.

## 3. Consequence for the proof

The calculation does not complete the third-position theorem. It also
does not change the completed first-two-position and interior results.
The source-geometric action identity near the complete boundary colors
is unaffected.

A useful next question is whether evaluating the difference of the
actions in a centered form, with its exact first-order cancellations,
can reduce the interval width. Such a reformulation needs its own
written bound and fixed evaluation protocol. The present record is
terminal; increasing its subdivision depth or rerunning it is not part
of this result.
