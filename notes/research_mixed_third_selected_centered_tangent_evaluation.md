# Reusable centered third-selection target evaluation

Implementation specification, 6 November 2026. This module replaces
the direct full-reference-box trial value by the
[recentered difference-of-actions enclosure](research_mixed_third_selected_recentered_defect.md).
It retains the original target profiles, reference marginals,
horizontal support correction and signed boundary compensation.
It makes no reference solve, target proposal or cover on import or
during evaluation.

## 1. API and frozen arithmetic

The new [module](../experiments/evaluate_mixed_third_selected_centered_tangent.py)
exposes the same initialize, propose_trial and evaluate interfaces
as the [original evaluator](../experiments/evaluate_mixed_third_selected_tangent.py).
Initialization verifies the old module, centered-enclosure proof and
this specification, merges every verified old dependency, and records
the new module's own hash.

The proposal method delegates exactly to the frozen proposal routine.
The evaluation method accepts reference, anchor, alpha, beta, left,
right, nu and trial, in that order. It uses the supplied rational
trial only. The current and anchor payloads retain their original
certified status and type association. All original profile boxes and
the 256-bit precision requirement are unchanged. The caller owns the
external type/chart association and any bounded coverage protocol.

The old Primitive, outward reconstruction, profile-box validation,
payload checks, marginal formula and exact Cartesian compensation
routine are reused. The old evaluate method is never called:
no direct full-box difference of actions is computed as a fallback.

## 2. One evaluation

From the exact saved endpoints form the exact Cartesian midpoint and
ten real displacement intervals. The full reference box is reconstructed
outward and passes the same broad common-product guards as before.
Its target image uses the saved reference heights for main coordinates,
height \(1/100\) for the selected coordinate, and height zero at cuts.

The literal midpoint defect uses two old phase calls, the two
midpoint boundary marginals, and both exact real boundary displacements.
It keeps the Fourier term \((1-\nu)g(z_H)-2\pi H\nu\) in its real
part. The midpoint is not assumed stationary.

Two explicit gradient calls each evaluate the nine original logarithms:
five own arguments and the four adjacent sums. Four cotangents on
the full reference box supply \(F_{aa},F_{au},F_{bv},F_{bb}\).
Every argument retains the original regular-strip guard. The ten real
derivative intervals are precisely equations (7)--(8) of the centered
proof, including \(F_u,F_z,F_v\) away from the canonical family.
The selected Fourier gradient does not occur in these reference
derivatives because its target coordinate is fixed.

Each derivative interval is multiplied by its corresponding exact
reference displacement interval using all four endpoint products.
Their lower and upper sums, added to the midpoint defect, give
the centered_trial_defect field. The compatible trial_defect field
contains that same centered enclosure and is explicitly labeled as such.

For the original target support, use the full target gradient, subtract
the current \(F_a,F_b\) in the two boundary coordinates, and add
\((1-\nu)g'(z_H)\) in the selected coordinate. The selected logarithm
is already present in the target-gradient calculation. Fixed cuts
have zero displacement intervals, so their support contribution is
zero. The same current marginal values and the original anchor
marginals enter the compensation record; the exact lower endpoint of
\(C_0\) is retained.

Thus the returned original-compatible fields satisfy exactly
\[
 \begin{split}
 U&=D_{\mathrm{centered}}^+
                       +\sum_i U_{\mathrm{support},i},\\
 U_{\mathrm{compensated}}&=U-C_0^- .
 \end{split}
\]
Their names are upper_rational, support_terms, compensation_record
and compensated_upper_rational. These bounds apply to the entire
original real target product. No optional local-curvature or Taylor
derivative refinement is used.

## 3. Witnesses, failures and scope

The result saves both coordinate hashes, all original exact endpoints,
the exact midpoint/displacements, reconstructed full boxes, midpoint
images and action, full reference/target gradients, cotangent arguments
and values, sparse Hessian entries, ten derivative products, support
terms and original compensation. A complete call uses 27 original
primitive values, 56 original logarithms and four cotangents. Of the
56 logarithms, the two midpoint phase calls use 34, the two explicit
full-box gradients use 18, and the original anchor marginals use four.
Both evaluation proposal counters remain zero.

Expected nonfinite or domain failures return inconclusive, preserving
the partial witness and counters. Unexpected failures return error;
the caller must archive and stop according to its own protocol.
There is no retry, precision increase, reference clipping, alternate
trial, or fallback to an unreviewed bound.

The centered proof and the original global target concavity justify
the resulting bound. The signed-compensation maximum principle still
requires all cells and labels of a complete product boundary.
This implementation specification reports no evaluation or completed
source comparison.
