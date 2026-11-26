# Real both-small sources versus the geometric supporting planes

Research note, 4 November 2026. The target variables in this result are
real. The reference variables may be the actual complex geometric legs.
No assertion is made here for the original complex taper or for targets
approaching zero uniformly in the level.

Use the allocated phase \(\phi_{\eta\epsilon}\) and its real restriction
\(f_{\eta\epsilon}\) from the
[real supporting-plane theorem](research_mixed_real_outer_support.md).
The two reference rectangles are
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].                         \tag{1}
\]
For \(r=(a_*,b_*)\in R_{3+\eta}\times R_{3+\epsilon}\), define
\[
 \Gamma_r(x)=\phi_{\eta\epsilon}(r)
                +\phi_{\eta\epsilon}'(r)\cdot(x-r).
                                                               \tag{2}
\]
The original zero-lift branch on a neighborhood of this entire product
is supplied by the [central source theorem](research_mixed_central_conditional_rectangles.md).
Both this branch and the all-real branch are identified by the unique
cotangent-strip solution, with its original zero logarithmic lift, in
the [global root theorem](research_mixed_global_cotangent_roots.md).
The reference rectangles satisfy that theorem's outer cotangent
conditions. No intersection of the type-four reference rectangle with
the real target domain is assumed.

**Theorem 1.** For every type pair, every reference in (1), and every
real \(x=(a,b)\in(0,3/20]^2\),
\[
 f_{\eta\epsilon}(x)<\Re\Gamma_r(x)-\frac1{25}.       \tag{3}
\]
Consequently, on each compact target subset of \((0,3/20]^2\), the
literal allocated source, including either selection of its outer
Fourier factors, satisfies for all sufficiently large levels
\[
 {\cal B}_{\eta\epsilon,N}(x)
 \le C N^{-(2+\eta+3\epsilon)/4}
           e^{N(\Re\Gamma_r(x)-1/30)}.              \tag{4}
\]
The constants and the level threshold can be chosen uniformly in the
reference rectangles. Both level parities are included.

## Reduction to four affine targets and 64 boundary products

Put \(c=(3/20,3/20)\). Global real concavity gives
\[
 f_{\eta\epsilon}(x)\le L_{\eta\epsilon}(x)
 :=f_{\eta\epsilon}(c)+\Re\phi_{\eta\epsilon}'(c)\cdot(x-c).
                                                               \tag{5}
\]
This is valid on the whole open real half-square, even when the segment
passes far outside the existing complex source rectangles. For a fixed
reference, \(L(x)-\Re\Gamma_r(x)\) is affine in the two real target
coordinates. Its maximum on \([0,3/20]^2\) is therefore at one of the
four corners. The corners with a zero coordinate are used only to bound
this affine expression; no finite-source packet at zero is invoked.

At each of these four targets, \(-\Gamma_r(x)\) is holomorphic in the
two reference variables on a neighborhood of the full closed product
(1). The repeated maximum principle reduces its real part to the
sixteen products of rectangle edges. Thus the four ordered type pairs
require 64 two-real-parameter reference products, checking all four
target corners on each product.

The checker encloses the two original conditional roots at the real
point \(c\), and then the original logarithmic roots on every reference
boundary cell, by affine Newton self-maps. It checks every original
sine strip, identifies the globally unique root, and retains the full
complex Schur derivatives. Every accepted cell verifies
\[
       L_{\eta\epsilon}(x)-\Re\Gamma_r(x)<-1/25
       \quad\text{for all four affine target corners}.          \tag{6}
\]
For clarity, the derivative used to bound variation in a reference
cell is the exact cancellation
\[
 d_r\Gamma_r(x)=\phi_{\eta\epsilon}''(r)(x-r)\,dr.              \tag{7}
\]
The root centers and affine coefficients are rational-decimal proposals;
only the outward residual, contraction and mean-value bounds accept a
cell. Alternating dyadic addresses have disjoint interiors, are
prefix-free and have total area one on every product. No sampled
maximum is used in (6).

Equations (5)--(6) prove (3). The original-source power and nonzero
symbol are exactly those in the real supporting-plane theorem.
The Fourier selections have modulus one at these real targets.
Absorbing their uniform symbol bounds on a compact target set proves
(4), with its smaller exponential margin. This does not provide a
uniform estimate as a target tends to zero with \(N\).

The result is a local comparison for a block whose two target arguments
are real and small. A graph that resets neighboring heights may still
increase the action of other blocks; the
[reset obstruction](research_mixed_left_support_obstructions.md)
is unaffected. No cyclic integral or whole-word lower bound follows
from this comparison alone.

## Reproduction

    python3 experiments/certify_mixed_real_small_support.py --precision 256

A saved-cover replay, with no new root proposals, is:

    python3 experiments/certify_mixed_real_small_support.py --precision 320 --input repro/results/research-mixed-real-small-support.json --output /tmp/research-mixed-real-small-support-review.json
