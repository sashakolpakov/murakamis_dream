# Centered enclosure of the original primitive

Research deduction and diagnostic specification, 6 November 2026.
The direct half-row scalar covers remain partial and frozen. This
note gives a valid alternative enclosure of their original primitive,
and specifies one fixed-box comparison of the two arithmetic forms.
It asserts no new uniform scalar sign.

Let \(W\) be a closed complex rectangle contained in
\(0<\Re w<1\), and let \(w_0\) be its exact dyadic center.
The original branch satisfies
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}{2\pi i},
 \qquad g'(w)=\Log(1-e^{-2\pi iw}).
 \tag{1}
\]
Both functions are holomorphic throughout this strip. In particular,
the argument of the logarithm never meets its negative real cut:
if its imaginary part vanishes in this strip, then \(\Re w=1/2\)
and its real part is positive. This is the original logarithmic
lift, not a new branch choice.

Suppose \(G_0\) encloses \(g(w_0)\), and the rectangular complex
interval \(D\) encloses every \(g'(w)\) for \(w\in W\). Then
\[
                       g(W)\subseteq G_0+D(W-w_0).
 \tag{2}
\]
Indeed for each \(w\in W\), the straight segment remains in \(W\),
and the exact integral identity is
\[
 g(w)-g(w_0)=(w-w_0)\int_0^1 g'(w_0+t(w-w_0))\,dt.
 \tag{3}
\]
The integral belongs to the convex rectangle \(D\). Thus ordinary
outward complex interval multiplication proves (2). No derivative
at a proposed saddle or finite-source evaluation is involved.

The new helper evaluates \(G_0\) by the already audited original
dilogarithm formula at \(w_0\), and \(D\) by (1) on the whole
rectangle. The regular-strip check remains mandatory. A nonfinite
interval logarithm is inconclusive, never a reference exclusion.
If \(W\) is itself a tiny numerical enclosure, the same proof
still applies. All constants are made at the requested precision.

The single diagnostic selects the accepted leaf with the largest
saved main-factorial upper bound in the immutable second half-row
record, using exact rational serialized endpoints. It deletes the
last two binary digits of that leaf's address and reconstructs the
resulting coarser box exactly. On that one box it calls the frozen
four-test evaluator twice: once with its original primitive and
once with only the enclosure (2) substituted. It uses the same
160-bit precision, reference maps, filters, gradients, clipping,
and gain arithmetic. There is no subdivision or second test box.

The result reports all four majorant intervals and their width and
upper-bound changes. A numerical improvement on this fixed box
does not imply a complete cover, and no unsuccessful scalar upper
bound is a source counterexample. The old scripts, proofs,
accepted leaves and pending frontier remain unchanged.
