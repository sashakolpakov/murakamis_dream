# A stronger upper-height bound for every type-four critical leg

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The 192-bit author certificate and independent 256-bit sine/cotangent replay
pass all 48 boundary products and 249 cells, without replay refinements. The
existing localization and window theorems are unchanged.

The earlier window theorems put every actual cyclic critical leg in
\[
 R_3=(.30,.39)+i(-.03,.02),\qquad
 R_4=(.27,.33)+i(-.057,-.001).
 \tag{1}
\]
This note uses those already proved inputs once more in the original two-leg
block map. Its conclusion is a critical-domain estimate. A full mixed-word
finite-sum bound requires its separate source and contour arguments.

## 1. Holomorphy precedes the boundary reduction

Let \(B_1(a,b)=(s(a,b),t(a,b))\) be the type-four block map from
[the universal localization theorem](research_mixed_cyclic_critical_localization.md).
It solves the original zero-lift equations
\[
 \begin{split}
 0={}&\Log(1-e^{-2\pi i(s+t)})
       +\Log(1-e^{-2\pi i(s+a)})
       -3\Log(1-e^{-2\pi is})+2\pi ia,\\
 0={}&\Log(1-e^{-2\pi i(s+t)})
       +\Log(1-e^{-2\pi i(t+b)})
       -3\Log(1-e^{-2\pi it})+2\pi ib .
 \end{split}
 \tag{2}
\]
The logarithms are the original principal branches on the regular strips.

The closed rectangles in (1) lie strictly inside their old typed disks:
the largest squared distances from their disk centers are respectively
\(34/10000\) and \(3501/10^6\), smaller than \((9/100)^2\) and
\((8/125)^2\). Thus the old theorem supplies a holomorphic block map on a
neighborhood of every full product of the closed rectangles before any
maximum principle below is invoked. In particular, existence is not
deduced from boundary sampling.

Successive harmonic maximum principles for each component's imaginary part
reduce its upper bound to the product of the two rectangle boundaries.
Each boundary has four affine edges, with parameter in \([0,1]\).
Reflection gives
\[
 B_1(b,a)=(t(a,b),s(a,b)).
 \tag{3}
\]
It therefore suffices to check the three input type pairs
\((3,3),(3,4),(4,4)\), all sixteen ordered edge products for each pair,
and both output coordinates.

## 2. The finite outward certificate

**Proposition 1.** On every product of the closed rectangles in (1), the
original selected block satisfies
\[
                     \Im s<-1/50,\qquad \Im t<-1/50.
 \tag{4}
\]

For every exact dyadic edge-parameter rectangle, the author evaluates the
unchanged exponential-log self-map primitive used in the original
localization theorem. Its untrusted center, approximate inverse, and
response matrix are accepted only after outward arithmetic proves
\[
 z=z_0+D(p-p_0)+w,\qquad |w_i|\le r_i,\qquad
 b_i+\sum_jE_{ij}r_j<r_i.
 \tag{5}
\]
Here \(b_i\) bounds the preconditioned residual on the whole affine
parameter rectangle, while \(E_{ij}\) bounds the Jacobian defect on its
entire radius enlargement. Every logarithmic remainder and both external
responses are retained. The approximate inverse is verified nonsingular.
The resulting root enclosure lies in the original chamber and typed disk,
and each of its imaginary upper endpoints is less than \(-1/50\).
Uniqueness in the old chamber identifies it with the branch in (2).

The accepted binary addresses are prefix-free and have exact Kraft mass
one on each of the 48 parameter squares. The author accepts 249 cells after
450 visits. They include all edge endpoints;
overlap at rectangle corners is harmless. The independent replay uses
sine logarithms, cotangent differences, and the second-derivative remainder
\(\pi^2|\csc^2(\pi z)|\), rather than the author's rational-exponential
formulas. It separately checks the full list of edge products, exact
coverage, and both output height bounds. The harmonic maximum principle
then proves (4) throughout the entire rectangle products.

## 3. Every cyclic length

**Theorem 2.** At the original zero-lift critical point of every finite cyclic
word in three and four, each type-four leg obeys
\[
            .27<\Re z<.33,\qquad -.057<\Im z<-.02.
 \tag{6}
\]

The earlier [type-three window theorem](research_mixed_type_three_window_strip.md)
and [type-four window theorem](research_mixed_cyclic_critical_height_bounds.md)
give (1). Fix any type-four vertex. Its two external legs lie in their
respective rectangles, and its two internal legs solve (2). The global
uniqueness theorem identifies them with \(B_1(a,b)\), so Proposition 1 gives
the stronger upper-height bound. The old lower-height and real-part bounds
remain unchanged.

This argument also includes cyclic lengths one and two: the external legs
may coincide with other legs of the same block, but at the actual critical
point they have fixed values in (1), and the same two-leg equations and
uniqueness apply with their original incidence multiplicities. No new
finite-source identification, summation contour, or knot conclusion is
inferred from (6).

## 4. Reproduction

    python3 experiments/certify_mixed_type_four_height_refinement.py --precision 192
    python3 experiments/replay_mixed_type_four_height_refinement.py --precision 256

The new files do not modify the completed localization, window, or
boundary-strip certificates.
