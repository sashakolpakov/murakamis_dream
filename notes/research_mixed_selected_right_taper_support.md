# Original selected-block bounds through the whole right taper

Research proof, 4 November 2026. The canonical outward certificate and independent written/code
review have passed.
Completed plateau, unselected-taper and manuscript files are unchanged.

This covers all plateau/right-taper products with at least one selected
four-type leg and at least one right-taper coordinate. The height of
each taper is allowed to range over its entire segment independently
of its real coordinate. A convexity argument reduces those segments
to their endpoints, preserving the full original finite source.

## 1. Exact block, phase and targets

Use the original finite kernel, Fourier polynomial and allocated modulus
\[
 \begin{split}
 C_{\epsilon,N}(X,Y)&=\sum_{j=0}^{N-1}
       \frac{X^{-j}(rX;r)_j(rY;r)_j}{(r;r)_j^{\,2+\epsilon}},
                                      \qquad r=e^{-2\pi i/N},\\
 B_N(z)&=|C_{\epsilon,N}(X,Y)|
       |d_N(X)X^{-N\sigma_a}|^{\eta/2}
       |d_N(Y)Y^{-N\sigma_b}|^{\epsilon/2},\\
 X&=e^{-2\pi iz_1},\qquad Y=e^{-2\pi iz_2}.
 \end{split}
 \tag{1}
\]
The normalized primitive, original conditional root and allocated phase are
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 \phi(a,b)&=Q_\epsilon(s_*(a,b);a,b)
                  -(1+\eta/2)g(a)-(1+\epsilon/2)g(b).
 \end{split}
 \tag{2}
\]
The [full right-square source theorem](research_mixed_unselected_right_taper_products.md),
Theorem 1, supplies the unique original logarithmic root and the
whole nonzero canonical packet on all parameter boxes used here,
including their neighborhoods. It keeps all \(N\) finite rows and
all original cotangent currents.

Let \(r_*=(a_*,b_*)\) range over the independent reference rectangles
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02],
 \tag{3}
\]
with types \(3+\eta,3+\epsilon\), and define
\[
 \Gamma_{r_*}(z)=\phi(r_*)+
                \phi_a(r_*)(z_1-a_*)+\phi_b(r_*)(z_2-b_*).
 \tag{4}
\]
In particular these include every actual cyclic critical pair,
with its original zero lift.

Put \(P=[.22,.45]\), \(T=[.45,.50]\), and \(H=7/500\).
Each real target coordinate independently lies in \(P\) or \(T\);
at least one lies in \(T\). The selected indicators satisfy
\(\sigma_a\le\eta,\sigma_b\le\epsilon\) and
\(\sigma_a+\sigma_b>0\). A plateau height is \(H\) for a selected
leg and its original reference height for an unselected leg.
A taper height may be any point of
\[
 [0,H]\quad\text{if selected},\qquad
 [0,\Im r_{*,j}]\quad\text{if unselected},
 \tag{5}
\]
where the latter denotes the closed segment with those endpoints,
regardless of their order. This contains the actual quadratic taper
heights \(H\chi_1(x)\) and \(\Im r_{*,j}\chi_1(x)\).

**Theorem 1.** Uniformly for all these targets and references,
for both parities and every sufficiently large integer level,
\[
 B_N(z)\le\operatorname{poly}(N)
             \exp N\left(\Re\Gamma_{r_*}(z)-\frac1{2000}\right).
 \tag{6}
\]
It is a bound for the entire original function in (1), not a
termwise index estimate or a prepared stationary-phase model.

## 2. All Fourier branches and height convexity

For \(f_a\in\{0,\ldots,\sigma_a\}\),
\(f_b\in\{0,\ldots,\sigma_b\}\), put
\[
 \psi_f(z)=\phi(z)+\tfrac12[f_ag(z_1)+f_bg(z_2)]
                      +\pi i\sum_{j=a,b}(\sigma_j-f_j)z_j.
 \tag{7}
\]
For a selected height \(h\ge0\), the exact upper rate of its
allocated Fourier factor is
\[
 \tfrac12\max\{-\Re g(z),2\pi h\}-\pi h.
 \tag{8}
\]
The maximum of \(\Re\psi_f\) is therefore exactly the total
kernel-plus-Fourier rate, before its arbitrarily small tolerance.
For unselected four-type targets, \(h\le0\) and
\(0<\Re z\le.5\), so the true rate is
\(\max\{-\Re g(z),0\}=-\Re g(z)\).
This includes the forcing tie at .5. There is no deletion of a
forcing branch and no relative-factorial claim at that tie.

The five nonempty selection/type patterns are
\[
 (0,1,0,1),\ (1,0,1,0),\ (1,1,1,0),\
 (1,1,0,1),\ (1,1,1,1)
 \tag{9}
\]
in the order \((\eta,\epsilon,\sigma_a,\sigma_b)\).
They have twelve smooth branches (7).

**Lemma 2.** For every branch, on the full independent target boxes
with real parts in \([.22,.50]\), selected heights in \([0,H]\),
unselected type-three heights in \([-.03,.02]\), and unselected
type-four heights in \([-.057,0]\),
\[
                             -\Re\psi_f''>\tfrac54 I.
 \tag{10}
\]
In particular the branch defect
\(\Re[\psi_f(z)-\Gamma_{r_*}(z)]\) is separately convex in each
target height, with second derivative at least \(5/4\).

The matrix is the exact allocated Schur Hessian (13) in the
[selected-plateau proof](research_mixed_selected_plateau_support.md),
minus \(\operatorname{diag}(f_ag''(z_1),f_bg''(z_2))/2\).
The linear terms in (7) have no Hessian. At each fixed real test
vector the corresponding real quadratic form is harmonic in
either complex parameter. Whole-product root holomorphy is already
proved by the source theorem. Its minimum therefore reduces to
the sixteen products of parameter sides. For all twelve branches
the checker covers all 192 products, enclosing the original root
by affine logarithmic Newton self-maps. Both shifted diagonal
entries and the determinant of the real matrix in (10) are
strictly positive. The cover passed with 62,560 accepted cells.
Two minimum principles then prove the full independent-box bound.

The height assertion follows from holomorphy:
\(\partial_{h_j}^2\Re\psi_f=-\Re\psi_{f,jj}>5/4\).
The plane (4) contributes only a linear function of height.
Thus, at fixed real targets and reference, the maximum over (5)
occurs at its height corners. Apply this successively to both
taper coordinates and separately to every branch. A plateau
height is kept fixed. This is an exact continuous-height reduction.

## 3. Constrained support on every height corner

At a height corner write \(m_j=0\) for height zero and \(m_j=1\)
for the nonzero endpoint, \(H\) when selected and the reference
height when unselected. A plateau coordinate has \(m_j=1\).
The three real rectangle choices \(T\times P\), \(P\times T\),
\(T\times T\), together with (9), give fifteen geometric patterns.
All their branches and height corners are retained.

For fixed reference and height corner, let \(F(v)\) be the real
branch defect on the corresponding real rectangle
\([L_1,U_1]\times[L_2,U_2]\). For any rational point \(c\) in
that rectangle, Lemma 2 gives
\[
 \max F\le F(c)+\sum_{j=1}^2
       \max_{u\in[L_j-c_j,U_j-c_j]}
           \left\{G_j u-\frac{5}{8}u^2\right\},
 \qquad G_j=\partial_{v_j}F(c).
 \tag{11}
\]
The one-dimensional maximum is at
\(u=\operatorname{clip}(4G_j/5,L_j-c_j,U_j-c_j)\).
The constraint is retained; replacing it by an unconstrained
quadratic maximum is not part of this certificate.

For an interval enclosure of \(G_j\), the positive half of the
\(u\)-interval uses its upper endpoint and the negative half uses
its lower endpoint. The checker evaluates the clamped quadratic
maximum outward, retaining zero and both endpoint alternatives
at an uncertain transition. Hence every true gradient in the
interval is bounded. Floating constrained optimization proposes
the rational point \(c\) only. Its membership in the exact target
rectangle and the outward value of (11) determine acceptance.

A reference coordinate can be reduced harmonically to its boundary
whenever its corner target height is independent of it. This includes
all selected references and also an unselected reference whose
target height corner is zero. For a fixed real target, the defect
is harmonic in such a reference coordinate, and its supremum over
the fixed compact target rectangle is locally bounded and
subharmonic. The maximum principle applies to that supremum.
If the unselected corner height equals the reference height, both
the real and imaginary parts of that reference remain explicit.
Thus every reference product has dimension two or three.

The exact full-cell derivative used in the reference check is
\[
 \partial_\tau F(c)=\Re\left[
       \bigl(\psi_f'(z)-\phi'(r_*)\bigr)\cdot\partial_\tau z
       +\sum_{j,k}(-\phi''(r_*))_{jk}(z_j-r_{*,j})
                                      \partial_\tau r_{*,k}
                         \right].
 \tag{12}
\]
It includes the linear frequency term of (7). In a coupled
unselected-height direction, \(\partial_\tau z\) is its literal
imaginary increment. In every decoupled direction it is zero.
No holomorphic reference argument is made across a moving
unselected target height.

For every cell the checker stores original reference-root and
target-root affine Newton witnesses, with rational centers,
response coefficients and remainder radii. Point Newton tests
enclose the center value of \(F(c)\). Formula (12) controls its
variation through the entire cell, while the root enclosures
bound both real target gradients in (11). The resulting outward
upper bound is strictly below \(-1/1000\).

There are ninety-six branch/height profiles and 1,056 reference-side
products. The complete rational binary covers passed with 25,393
accepted cells. The checker verifies the exhaustive profile list,
both orientations, every height corner and multiplicity-one
binary coverage. Subharmonic extension in the decoupled reference
coordinates then proves
\[
                \Re[\psi_f(z)-\Gamma_{r_*}(z)]<-1/1000
 \tag{13}
\]
at every corner for every independent reference (3).
Height convexity extends it to the full segments (5).

## 4. The original finite source

The full right-square packet bounds the literal finite sum
\(C_{\epsilon,N}\) with rate
\(\Re[Q_\epsilon(s_*)-g(z_1)-g(z_2)]\).
Its original coefficient, complete index tails, revived rows,
both aliases and all joining currents are already part of that
proved source statement.
The actual \(d_N\) upper bound contributes at most a total
\(\delta\) from the two allocated half-weights. Choose
\(\delta<1/2000\). Taking the maximum over the exact branches
(7)--(8) and using (13) proves (6).

For fixed derivatives of original contractions with integer powers,
use the source neighborhoods and Cauchy's inequality after a small
thickening. The true Fourier upper rate, including its forcing term,
is continuous there. Consequently the strict gap survives a sufficiently
small thickening even at height zero or real coordinate .5.
The boxed height-convexity formula is not extended into a different
forcing branch to justify this step. The half-modulus notation itself
is not differentiated.

## 5. All selected subsets on the region above .22

For the original fixed cyclic word, let
\(M=\Re\mathcal F_*\) be the real critical rate, and use the exact
\(\chi_1\) subset-density and graph-contour formulation. Partition
each real coordinate of \([.22,1]^m\) into \(P\), \(T\), and
\(R=[.5,1]\). Every local block has one of the following bounds:

| Target block | Bound relative to its original complex tangent |
|---|---|
| At least one \(R\) coordinate | Whole right-half gap \(1/2000\), for every selected indicator. |
| \(P/T\), with a taper and a selected leg | This theorem, gap \(1/2000\). |
| \(P/T\), with a taper and no selected leg | Whole unselected-taper gap \(1/80000\). |
| \(P/P\), with a selected leg | Selected-plateau gap \(1/200\). |
| \(P/P\), no selected leg | Its own supporting plane with an arbitrarily small Fourier tolerance. |

Spend that last tolerance only once globally, by choosing
\[
                         0<\delta_m<\frac1{160000m}
 \tag{14}
\]
per unselected plateau block. Every box containing a taper or a
right-half coordinate has at least one gapped block. Every nonempty
selected subset on the pure plateau box also has a gapped block.
The allocated half-weights restore the literal integer Fourier
powers, and all complex linear tangent terms cancel by the original
zero-lift critical equations. This uses original incidences before
identification and applies also to cyclic lengths one and two.
Thus every contribution except the unselected pure-plateau one has
absolute rate at most
\[
                                M-\frac1{160000}.
 \tag{15}
\]
For the fixed word there are finitely many boxes and selected subsets;
the graph Jacobians and original scalar densities cost only polynomial
factors. The existing central coefficient of the unselected plateau
integral is therefore unchanged when all original subset terms over
\([.22,1]^m\) are included.

This is a contribution of the exact original source, not the entire
outer cycle. Any coordinate below .22 remains outside this assembly.
No total mixed-word asymptotic or knot-volume conclusion is asserted.

## 6. Reproduction

    python3 experiments/certify_mixed_selected_right_taper_support.py --precision 256

The checker first verifies all 192 target Hessian covers and then
all 1,056 reference support covers. It validates current source
records, exact profile lists, every binary cover and start/end
immutability. Optimizers only propose rational support points;
they are never used as a certificate of a maximum.
