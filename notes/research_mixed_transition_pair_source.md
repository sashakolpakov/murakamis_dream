# Complete sources for adjacent transition parameters

Research proof, 4 November 2026.
This is a separate source result for two transition arguments. It neither
extrapolates the transition-by-plateau estimate nor asserts an outer
supporting-plane or cyclic-integral bound.

Use the exact factorial, canonical finite sum, original zero-lift action
and nonzero Gaussian symbol in
[the whole-period transition source theorem](research_mixed_transition_whole_period_source.md),
equations (2)--(5). Put
\[
 T_3=\operatorname{conv}\{.10,.22-.03i,.22+.02i\},\qquad
 T_4=\operatorname{conv}\{.10,.22-.057i,.22+.014i\}.          \tag{1}
\]

**Theorem 1.** For every \(\eta,\epsilon\in\{0,1\}\), the complete
canonical source on a fixed open neighborhood of
\(T_{3+\eta}\times T_{3+\epsilon}\) satisfies
\[
 L_{\epsilon,N}(a,b)=N^{(1-\epsilon)/2}
       A_\epsilon(a,b)e^{NQ(s_*;a,b)}(1+O(N^{-1})),          \tag{2}
\]
uniformly, with the same original action and nowhere-zero holomorphic
symbol. All fixed derivatives are uniform on smaller neighborhoods.
The literal conditional polynomial
\(C_{\epsilon,N}=L_{\epsilon,N}/[P_N(Na)P_N(Nb)]\)
therefore has power \(N^{-(1+\epsilon)/2}\), action
\(Q(s_*)-g(a)-g(b)\), and symbol
\(A_\epsilon/[a_0(a)a_0(b)]\).

## 1. A fresh boundary certificate

The selected root exists holomorphically before any source estimate:
these triangles lie strictly in the cotangent domain from the
[minimum-neighbor contour theorem](research_mixed_minimum_neighbor_contour.md).
All its critical factorial arguments stay in their original regular
strips, and \(-\Re Q_{ss}>0\). This supplies phase and symbol branches,
not a finite-source bound.

There are four ordered typed products and nine edge products each.
The new checker exhausts all 36 products by rational dyadic covers.
It proves the same explicit sufficient conditions used in the
whole-period source theorem:

* the high-half derivative polynomial has
  \(G(w)=wF'(w)-2F(w)>0\) on \([0,\infty)\), including its positive
  leading coefficient, by exact compactification and subdivided
  Bernstein coefficients;
* the selected action \(M\) is positive, \(|\Im s_*|<1\), and both
  selected-height endpoint gaps exceed \(10^{-4}\);
* all four original real right-midpoint multiplier branches lie at
  least \(10^{-4}\) below \(M\);
* for type four, the complete positive-height concave profile
  \(V(y)+2\pi(\Im b)_+\), \(0\le y\le2\), lies at least
  \(10^{-4}\) below \(M\).

Every root is accepted by an original-logarithm affine Newton self-map,
with a separate exact midpoint enclosure. The coefficient mean-value
bounds retain \(d\Im s_*\), and the vertical profile is bounded on its
whole interval by a concave tangent. The canonical 256-bit outward cover passed
17,580 cells in 32,856 visits, together with 11 exact identities and
two strict scalar alias bounds. An independent full written/code audit
and fresh 320-bit saved-cover replay passed all 36 products and 17,580
cells without refinements or new proposals. These are new tests on (1), not inherited
inequalities asserted beyond the earlier domain.

## 2. Exhausting the original finite source

The analytic current argument now applies verbatim, because both
outer real parts lie in \([.10,.22]\subset[.10,.45]\) and their
height ranges satisfy the same bounds as before. The left-half circle
lemma and the new polynomial criterion control the complete selected
horizontal. The exact midpoint factorial and period identities retain
both joins and every numerator multiplier. The four affine branches of
the right endpoint and the one exceptional type-four concave profile
control all vertical remainders. Both fixed horizontals at heights
\(\pm2\) retain their original cotangent penalties; the previous
strict scalar alias bounds apply on this smaller real range.

Near a vanishing selected or shifted height, freeze the far contour
slightly off all three real factorial axes and move only the regular
central segment through the saddle. Strict gaps persist, including the
short connecting pieces. Thus the original whole-half-plane factorial
expansions apply on every far piece without crossing an unproved
asymptotic wall. The exact zero-mode coefficient remains \(+N\), giving
(2) and its original normalization.

This first proves the complete normalized finite-source error on all
36 edge products. Two maximum principles for that holomorphic error
then extend the packet to the full products. They are not applied to
the selected-height polynomial itself. Strict neighborhoods of the
boundary and compactness give an open product neighborhood; Cauchy
estimates give the derivative statement. Every original finite row,
both midpoint currents and both horizontal aliases remain accounted for.

## 3. The resulting independent polygon source domain

Let
\[
 B_3=[.22,.45]+i[-.03,.02],\qquad
 B_4=[.22,.45]+i[-.057,.014],\qquad D_t=T_t\cup B_t.        \tag{3}
\]
Each \(D_t\) is the convex polygon with its triangular ramp up to
\(.22\) and its constant-height rectangle from \(.22\) to \(.45\).

**Corollary 2.** The same complete source packet, with the same absolute
action, symbol and powers of \(N\), holds on a fixed open neighborhood
of every independent product \(D_{3+\eta}\times D_{3+\epsilon}\).

Indeed Theorem 1 covers \(T\times T\); the preceding whole-period
transition theorem covers \(T\times B\) and \(B\times T\); and the
[full right-square source](research_mixed_unselected_right_taper_products.md)
covers \(B\times B\), including the stated positive type-four heights.
These are open-neighborhood packets for the same literal canonical sum.
Their critical roots are the same original zero-lift branch, and their
regular-strip actions and Gaussian symbols agree on all overlaps.
A finite union of the source neighborhoods therefore gives the claimed
uniform packet. This gluing does not use equality merely on a discrete
grid and does not continue an unproved error estimate.

The corollary supplies prescribed complex source widths for adjacent
transition coordinates. It does not compare their action with the
original geometric supporting plane, pay neighboring reset costs,
bound an outer wrapped term, or prove a mixed-word volume theorem.

## 4. Reproduction

```sh
python3 experiments/certify_mixed_transition_pair_source.py --precision 256
python3 experiments/certify_mixed_transition_pair_source.py --precision 320 --input repro/results/research-mixed-transition-pair-source.json --output /tmp/research-mixed-transition-pair-source-review.json
```

The new canonical record binds the proof, acceptance code, whole-period
current theorem and plateau-square source. Saved replay uses the recorded
rational witnesses and exact covers, with no new root or maximum proposals.
