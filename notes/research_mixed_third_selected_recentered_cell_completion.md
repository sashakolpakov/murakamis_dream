# The centered calculation resolves the previously inconclusive cell

Research result, 6 November 2026. All twelve original profile comparisons
on the prescribed saved parameter cell have a strict compensated gap
greater than \(1/40\). This resolves the cell that stopped the first
product-boundary calculation. It does not resolve the remaining cells
or establish the uniform third-position theorem.

## 1. Same mathematical comparison, sharper enclosure

The [original attempt](research_mixed_third_selected_product_boundary_attempt.md)
stopped at case zero, address `0000110000111110`. The
[fixed follow-up protocol](research_mixed_third_selected_recentered_diagnostic_protocol.md)
retained its certified reference rectangle, all twelve rational target
trials, their full-target support corrections, and the centered boundary
correction \(C_0\). No reference or target was reoptimized.

The only new step was to enclose the original action difference by the
[centered mean-value formula](research_mixed_third_selected_recentered_defect.md).
Its derivatives retain the cancellation of the reference action with
the boundary affine terms. Internal derivatives are kept throughout
the reference rectangle; they are not set to zero away from the actual
critical point.

For each label \(\rho\), let \(U_\rho\) be the resulting
upper bound after adding the original target-support correction and
subtracting the original lower endpoint \(C_0^-\). The sole
[diagnostic run](../experiments/diagnose_mixed_third_selected_recentered_defect.py)
proves
\[
                   \max_{\rho} U_\rho<-1/40.
\]
The largest upper bound belongs to the main/main factorial profile.
Its value is approximately \(-0.02808980447\). The original
required gap was only \(1/2000\).

## 2. Where the improvement comes from

For the limiting profile, the earlier direct enclosure of the trial
defect was contained in
\[
 [-0.075354,-0.018630].
\]
The new centered enclosure is contained in
\[
 [-0.047042,-0.046944].
\]
Its exact midpoint defect is enclosed near \(-0.04699306965\),
and the ten mean-value contributions have total upper cost less than
\(0.000048207\). The target-support cost remains less than
\(0.002673\); the same compensation lower endpoint, approximately
\(-0.01618276814\), is retained. No favorable boundary term was
dropped to obtain the sign.

Thus the earlier uncertainty in this cell was caused by the enclosure
of the action difference. This statement concerns a comparison over
the whole saved parameter cell and all its original real targets,
rather than a value at one numerical target.

## 3. Saved result and verification

The [diagnostic record](../repro/results/research-mixed-third-selected-recentered-diagnostic.json)
has SHA-256
`951944582a63523c90f6a493fb6665678075acb91fac45c888b9684bb455e713`.
It contains twelve midpoint evaluations, twenty-four gradient
enclosures on full rectangles, and forty-eight cotangent evaluations.
There were no new root proposals, target optimizations, or subdivisions.
All 33 input bindings remained unchanged.

The [saved-data checker](../experiments/check_mixed_third_selected_recentered_record.py)
verified the source associations, full-box derivative recombinations,
120 mean-value terms, and the unchanged target supports and boundary
corrections. Its [result](../repro/results/research-mixed-third-selected-recentered-saved-audit.json)
has SHA-256
`1633d0de63f0672e77cd2da6fcd1c9aa237a60718dba66082bca670992915dac`.
The strict common gap \(1/40\) was checked by exact rational
arithmetic. This verification performs no new analytic evaluation.

The first product-boundary record remains unchanged, including its
170 pending cells. A new uniform calculation must apply the improved
enclosure to a complete set of parameter-domain partitions before a
whole-domain theorem can be asserted.
