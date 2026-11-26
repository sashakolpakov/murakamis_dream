# One saved-cell test of the centered action difference

Fixed diagnostic protocol, 6 November 2026. The first product-boundary
pass stopped at its prescribed depth, with one unresolved comparison.
This protocol tests whether the
[centered difference-of-actions enclosure](research_mixed_third_selected_recentered_defect.md)
resolves that same cell. It changes the enclosure of the trial value,
not the mathematical comparison, its parameter domain, or its target.

## 1. Frozen inputs and exact scope

Use only the final unresolved node in
[the first product-boundary record](../repro/results/research-mixed-third-selected-product-boundary-attempt01.json.gz),
whose SHA-256 is
`e63cdc8ceb70046bac13ba855542657623c4b00e792ad367b0d7369c914a461e`.
Its case index is zero and its binary address is
`0000110000111110`. Both charts are `k3_circle_left`, and all three
type flags are zero. Its parameter intervals are
\[
 I_a=[-89/128,-11/16],\qquad I_c=[-45/64,-89/128].
\]
The independent
[saved-data check](../repro/results/research-mixed-third-selected-product-boundary-saved-audit.json)
has SHA-256
`9aa582ab0e3ab3914bd89737ed84e5963ee7bf65280ba1e2084bacf7e7b50647`.

Retain the stored certified coordinate rectangle, all twelve original
profile labels, each stored rational trial, all original target-support
terms, and the original centered boundary correction. No new root,
target optimization, parameter subdivision, or reference point is
proposed. The new midpoint is merely the exact Cartesian midpoint of
the saved reference rectangle; it is not assumed stationary.

## 2. The one prescribed evaluation

Use 256-bit outward interval arithmetic. For each of the twelve saved
labels, perform the following operations once.

1. Evaluate the literal original defect at the exact midpoint, with
   the original primitive and boundary marginals. Both boundary
   displacements are real: target real part minus reference real part.
2. Enclose the original gradient at the entire saved reference box
   and at its associated target image. These use nine logarithms each.
   Check every own and summed argument against the original regular
   strip. Retain the off-stationary internal derivatives.
3. Enclose the four cotangents needed for the two boundary Hessian
   rows. Use exactly equations (7)--(8) of the centered-enclosure note
   for all ten real reference derivatives. The selected target
   coordinate has fixed height and real trial, so its Fourier terms
   contribute no reference derivative.
4. Form the exact interval mean-value products with the ten saved
   reference halfwidths. Add their upper endpoints to the midpoint
   defect upper endpoint. This is the new trial upper bound.
5. Add the unchanged sum of the five saved target-support terms and
   subtract the unchanged lower endpoint of the boundary correction.

The sufficient inequality is the original one:
\[
 U_{\mathrm{centered\ trial}}
   +U_{\mathrm{target\ support}}-C_0^-<-1/2000.
\]
Do not replace the midpoint by a new stationary solution or replace
any internal derivative by zero. Do not reoptimize the target after
examining the bounds. The optional derivative refinements in the
centered-enclosure note are not part of this diagnostic.

All twelve labels are retained even if an earlier comparison is
inconclusive. Nonfinite arithmetic is saved as inconclusive, with no
retry or precision increase. Unexpected errors stop the diagnostic and
leave explicit entries for every unexamined label.

## 3. Record and permitted conclusion

The record preserves the exact midpoint, reconstructed full reference
and target rectangles, original gradients, boundary Hessian entries,
boundary displacements, ten derivative intervals and their exact
mean-value products, midpoint defect, original support correction,
original compensation, and the final upper bound for each label.
Every original input binding and the new proof and script identities
are checked before and after the pass.

If all twelve tests pass, the conclusion is the comparison on this one
saved parameter cell and its entire original real target domains.
The other pending cells in the old product-boundary record remain
pending. The old record is neither altered nor promoted to a completed
cover. A nonnegative new upper bound is inconclusive, rather than a
positive lower bound for the original defect.

No source or special-function evaluation has yet been carried out under
this protocol. The diagnostic has no automatic fallback or subsequent
parameter search.
