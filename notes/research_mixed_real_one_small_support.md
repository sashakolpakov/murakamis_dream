# A coherent real one-small source comparison

Research note, 4 November 2026. This result concerns real target
arguments. It retains the original complete conditional kernel and
Fourier weights, and compares them with the actual complex geometric
supporting planes. Neighboring height-reset costs remain separate.

Use the phase \(\phi_{\eta\epsilon}\), real rate
\(f_{\eta\epsilon}=\Re\phi_{\eta\epsilon}\), and allocated finite
source \({\cal B}_{\eta\epsilon,N}\) of the
[real support theorem](research_mixed_real_outer_support.md).
The reference variables range independently over
\[
 r=(a_*,b_*)\in R_{3+\eta}\times R_{3+\epsilon},\qquad
 R_3=[.30,.39]+i[-.03,.02],\quad
 R_4=[.27,.33]+i[-.057,-.02].                         \tag{1}
\]
All roots and derivatives use the original zero logarithmic lift.
The real and reference branches are identified by the unique
cotangent-strip root of the [global root theorem](research_mixed_global_cotangent_roots.md).
Set
\[
 \Gamma_r(x)=\phi_{\eta\epsilon}(r)
               +\phi_{\eta\epsilon}'(r)\cdot(x-r).             \tag{2}
\]

**Theorem 1.** For every ordered type pair, every reference (1), and
every real target in
\[
 \mathcal S=((0,1/10]\times(0,1/2))
                 \cup((0,1/2)\times(0,1/10]),                 \tag{3}
\]
one has
\[
 f_{\eta\epsilon}(x)<\Re\Gamma_r(x)-\frac{11}{200}.            \tag{4}
\]
On each compact subset \(K\) of \(\mathcal S\), uniformly in the
reference rectangles and at both level parities,
\[
 \mathcal B_{\eta\epsilon,N}(x)
 \le C_K N^{-(2+\eta+3\epsilon)/4}
             \exp N\left(\Re\Gamma_r(x)-\frac1{20}\right)
                                                               \tag{5}
\]
for sufficiently large \(N\). Every allowed selection of the original
outer Fourier factors obeys the same bound at these real targets.

## Finite real tangents

Partition the other real angle into the ten closed intervals
\[
 I_j=[j/20,(j+1)/20],\qquad j=0,\ldots,9.
                                                               \tag{6}
\]
For the first orientation put
\(c_j=(1/10,(2j+1)/40)\), and reverse the coordinates for the second
orientation. Each point lies strictly inside the open real half-square.
Global real concavity gives the exact tangent upper bound
\[
 f_{\eta\epsilon}(x)\le
 L_{\eta\epsilon,j}(x):=
 f_{\eta\epsilon}(c_j)+\Re\phi_{\eta\epsilon}'(c_j)\cdot(x-c_j).
                                                               \tag{7}
\]
For a fixed reference, \(L_j(x)-\Re\Gamma_r(x)\) is affine in
the real target coordinates. On \([0,1/10]\times I_j\), or the
reversed rectangle, its maximum occurs at one of the four corners.
Zero and half-period corners are used only to bound this affine
function. No source estimate or root at those corners is invoked.

At each target corner the reference-dependent part is the real part
of the holomorphic function \(-\Gamma_r(x)\). The
[central source theorem](research_mixed_central_conditional_rectangles.md)
supplies that branch on a neighborhood of the entire reference product
before any boundary reduction. The repeated maximum principle reduces
the comparison to the sixteen products of rectangle edges. The four
ordered type pairs require 64 reference boundary products, each
checking both orientations, ten intervals and four target corners.

The outward certificate verifies
\[
 L_{\eta\epsilon,j}(x)-\Re\Gamma_r(x)<-11/200                  \tag{8}
\]
on every such product. This proves (4) using (7).

## Certified comparisons and the original finite source

The checker first encloses all 40 real tangent-point roots by explicit
Newton self-maps of the original logarithmic equations. It verifies
their cotangent-strip membership and all original factorial strips.
On each reference boundary cell it uses a rational affine root
enclosure, with an independently checked point root at the cell center.
The complex Schur derivatives retain the full response of the inner
critical point. The exact cancellation
\[
 d_r\Gamma_r(x)=\phi_{\eta\epsilon}''(r)(x-r)\,dr              \tag{9}
\]
gives the interval mean-value error. Thus the outward test is performed
on entire cells, not just their proposed centers. Each reference product
has an exact prefix-free dyadic cover of total area one. The saved-cover
mode reuses only its rational witnesses and makes no new root proposals.

The real support theorem supplies the nonzero original complete-source
packet with power \(N^{-(2+\eta+3\epsilon)/4}\). Its symbol is uniformly
bounded on each compact \(K\), and all real Fourier selections have
modulus one. Absorbing this fixed symbol bound into the reserve between
\(11/200\) and \(1/20\) proves (5).

The conclusion is uniform for target points in each fixed compact
subset of (3); it is not a uniform estimate when a target approaches
zero or \(1/2\) with the level. It does not replace the reference by a
real point, discard the finite Fourier forcing, or control blocks whose
target heights remain nonzero. In particular a global graph that resets
heights still requires a separate comparison for its neighboring
blocks. No whole-word integral asymptotic follows from (5) alone.

## Reproduction

    python3 experiments/certify_mixed_real_one_small_support.py --precision 256

    python3 experiments/certify_mixed_real_one_small_support.py --precision 320 --input repro/results/research-mixed-real-one-small-support.json --output /tmp/research-mixed-real-one-small-support-review.json

The checker reuses the frozen original-log Newton and Schur routines
from the [both-small certificate](research_mixed_real_small_support.md),
with its own target partition, complete accepted cover and provenance.
