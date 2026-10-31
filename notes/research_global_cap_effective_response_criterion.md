# Effective boundary response and the original global cap variance

31 October 2026. **Internally reviewed analytical research theorem.**
Unpublished. This concerns the exact ONE-cap
coefficient at cap spectrum +2 and all other original CROSS spectra -2,
on ODD levels. It supplies a classical positive Hessian test for the
variance criterion, not a spectral-neighborhood or filled-knot theorem.

## 1. The same exterior and the two boundary weights

Retain the source and binary polynomial P_N(A,C) in
[the global negative-axis reduction](research_global_cap_negative_axis_and_mahler_bound.md), including all actual ordinary
coefficient targets. Suppose a strict one-cap stationary configuration
exists, with all other ports CROSS, finite positive ordinary weights,
and L_A=L_C. Normalize their common value to one. Let I be the set of
ordinary faces other than A,C; write A=exp(z), C=1 and L_i=exp(w_i).
The original protected variables u,v remain exactly zero.

Let t run over the original triangles EXCLUDING the two cap triangles.
Write Q_t for its actual endpoint half-triangle potential. Define

\[
 \mathcal F(z,w)=\sum_{t}Q_t(L)-\sum_{i\in I}w_i.
 \tag{1}
\]

There is no target term in z: A has not been extracted in the binary
polynomial. At the stationary exterior, w=w_* solves
\(\partial_w\mathcal F(0,w_*)=0\). Its A-load is the original residual
split nu, and the normalized value is M_cap:

\[
 \mathcal F(0,w_*)=M_{\mathrm{cap}},\qquad
 \partial_z\mathcal F(0,w_*)=\nu.
 \tag{2}
\]

These follow by the same finite-common-weight Legendre attainment used
in the cap-capacity theorem. The target logs cancel at A=C=1.

## 2. Positive Hessian with the original boundary anchor

Let H be the Hessian of (1) in the variables (z,w) at (0,w_*).
It is positive definite. Here is the graph check needed for this claim.
Delete the protected vertices u,v from the original simple triangulated
sphere. Its remaining ordinary graph is connected. Removing the cap
triangles removes no edge needed in that ordinary graph: their only
ordinary edge is AC, and its triangle on the opposite side remains in
the exterior. Every other ordinary edge was unaffected. Thus the graph
of ordinary pairs occurring together in an exterior triangle is still
connected. The face C fixes the common scaling direction.

For a positive triangle the Hessian of Q is nonnegative, and its kernel
on its nonzero coordinates is exactly the common-scaling direction.
For a two-supported-corner triangle this also holds; a pure corner
has zero Hessian and equates no two phases. This can be seen directly
from the strictly concave triangle entropy and its Legendre dual, or
from the actual positive determinant pair-trace identity and its
positive limiting bulk traces. The connected pair graph therefore
makes their sum strictly positive after C is fixed. Linear target
terms in (1) change no Hessian.

In particular H_II is invertible (the empty I case has the usual empty
matrix convention). The implicit-function theorem gives a real analytic
w(z) near zero, and the reduced exterior value

\[
 F(z)=\mathcal F(z,w(z)),\qquad
 \kappa_D:=F''(0)=H_{AA}-H_{AI}H_{II}^{-1}H_{IA}>0.
 \tag{3}
\]

The letters A in H indicate the log-A coordinate z. This is the actual
Schur complement for the original demands, not a separately optimized
star or a replacement graph.

## 3. The exact original odd polynomial has this variance limit

At N=2m+1 each original CROSS endpoint is exactly
N^2 D_m(x,b,y)D_m(x,c,y), with the original Hermitian positive pencils.
Put

\[
 \mathcal F_N(z,w)=\frac1N\log\prod_{e\ne F}
        P_{e,\mathrm{CROSS}}(-2;L)
           -\frac{N-1}{N}\sum_{i\in I}w_i.
 \tag{4}
\]

The local logarithmic derivatives of these actual determinants converge
to those of Q_t on a fixed complex neighborhood of the positive weights.
Their higher normalized derivatives are uniformly bounded there. The
retained N^2 factors are independent of z,w and cost O(log N/N) in
value; they vanish from the derivatives. These are exactly the local
positive-packet and curvature inputs already used in the original
positive face-coefficient theorem.

The same preconditioned implicit-function argument gives finite critical
points w_N(z), analytic on a fixed small disk, with w_N(z) tending to
w(z). Let $F_N(z)=\mathcal F_N(z,w_N(z))$. The coefficient extraction of
EVERY i in I is an exact |I|-torus integral. Its only angular maximum
at z=0 is the zero phase: the determinant contraction pairs every
ordinary phase with its neighbors, and both A and C are fixed at zero
phase. The same connected graph from section 2 rules out every other
phase, including lattice aliases. Every edge character is the primitive
+1,-1 character.

Its finite Hessian in the extracted variables is N times a uniformly
positive matrix. Gaussian evaluation, with the original coefficient
measure retained, therefore gives

\[
 P_N(e^z,1)=
 \frac{e^{NF_N(z)}}{(2\pi N)^{|I|/2}\sqrt{\det H_{N,II}(z)}}
 \left(1+O(N^{-1})\right),
 \tag{5}
\]

where $H_{N,II}(z)=\partial_w^2\mathcal F_N(z,w_N(z))$, and the square root
continues from its positive value at zero. The estimate is relative
and uniform on one fixed smaller complex z disk.

For completeness, the complex extension in (5) uses the same finite
contour argument as the complete coefficient theorem. The stationary
radius and its local integration box move analytically with z. Outside
that box the original positive angular gap persists under sufficiently
small complex perturbations of the weights. The connecting contour
faces stay in that gap. On the moving local box, normalized third and
higher derivatives are bounded, so Gaussian scaling and its odd cubic
cancellation give the uniform O(N^-1) remainder. The finite-dimensional
positive Hessian and compact graph fix the neighborhood before N tends
to infinity. This does not differentiate a merely pointwise coefficient
asymptotic or assume an unknown contributing cycle.

Equations (4)-(5) imply, by Cauchy estimates on that fixed disk,

\[
 \frac1N\log P_N(1,1)\longrightarrow M_{\mathrm{cap}},\qquad
 \frac1N\partial_z\log P_N(e^z,1)\big|_{z=0}\longrightarrow\nu,\qquad
 \frac1N\partial_z^2\log P_N(e^z,1)\big|_{z=0}\longrightarrow\kappa_D.
 \tag{6}
\]

The relative error is nonzero for all sufficiently large N, and the
normalized Hessian determinant stays away from zero, so their analytic
logarithms and the Cauchy differentiation are legitimate.

The exact odd real-root factorization of the SAME P_N is

\[
 P_N(A,C)=P_N(1,1)\prod_{r=1}^{N-1}
               [(1-p_{N,r})C+p_{N,r}A],\quad 0\le p_{N,r}\le1.
\]

Thus the variance in the exact negative-axis estimate is

\[
 V_N=\sum_rp_{N,r}(1-p_{N,r}),\qquad V_N/N\longrightarrow\kappa_D.
 \tag{7}
\]

## 4. A classical sufficient inequality, with its exact scope

The original finite cap reduction and its strict omitted-tail estimate
now give, along odd levels,

\[
 \limsup\frac1N\log|S_N|
 \le\max\{M_{\mathrm{cap}}-\kappa_D,\Phi_D-\gamma_D/2\}.
 \tag{8}
\]

Consequently the explicit response condition

\[
 \kappa_D > M_{\mathrm{cap}}-\Phi_D.
 \tag{9}
\]

implies a strict absolute cap-sector gap at these fixed spectra. The
weaker nonstrict condition gives a weak absolute bound. The original
one-cap chain theorem supplies the sufficient alternative
\(\kappa_D>W(\nu)/\pi-g/(2\pi)\), or the stronger easily stated
\(\kappa_D\ge W(\nu)/\pi\), using its positive fixed-meridian gap.
None of those comparisons is automatic from positivity of kappa_D.

The response can be computed directly from the original common weights:
for a triangle with supported weights a,b,c, put T=sqrt(ab+ac+bc).
When at least two weights are positive, its half-loads are
alpha_j=atan(L_j/T)/pi, with literal protected zeros. A pure supported
corner instead has load1/2 and zero Hessian; no 0/0 formula is used.
For two distinct supported corners, direct differentiation gives

\[
 -\partial_{\log b}\alpha_a
  =\frac{ab}{2\pi(a+b)\sqrt{ab+ac+bc}}=:g_{ab}>0.
 \tag{10}
\]

The diagonal is the sum of the incident g values by homogeneity. A
protected endpoint contributes no log variable and no such edge;
when exactly two weights are supported, (10) still holds with the
third weight zero. Sum these edge conductances over the ORIGINAL
exterior triangles. Then H is their graph Laplacian with the boundary
vertex C grounded, and

\[
 \kappa_D=
 \min_{v_A=1,\ v_C=0}\sum_{\{i,j\}}g_{ij}(v_i-v_j)^2.
 \tag{11}
\]

This is the exact effective conductance between the two ordinary cap
faces. Its minimization eliminates precisely the original interior
log-weight variables. The entries are algebraic in the weights up to
the common factor1/pi, and the Schur operations are finite. The test
uses classical gluing/response and volume data; it is not a condition
on roots of a growing quantum polynomial or a purely algebraic
replacement for the volume comparison.

There is also a useful upper bound which limits the proposed shortcut.
The finite Bernoulli variance and mean satisfy
V_N/d<=bar_p_N(1-bar_p_N). Equations (6)-(7), with d/N->1, give

\[
 0<\kappa_D\le\nu(1-\nu).
 \tag{12}
\]

Thus a positive effective conductance alone is not a universal lower
bound large enough to pay the geometric W budget. Condition (9) must
be checked against the actual excess.

This theorem proves no uniform margin in (9), no even-level stable
factorization, and no extension to varying spectra. Those are separate
requirements for a filled-period theorem. The conclusion in (8) is
only the stated original one-cap/all-CROSS endpoint sector, with every
source normalization and target retained.

## Dependencies and internal review

The local determinant and curvature inputs are
[the actual determinant curvature theorem](actual_q_hahn_boundary_model_curvature.md) and
[the original positive coefficient saddle](actual_positive_face_coefficient_saddle.md).
The original cap Legendre attainment is
[the constrained-capacity theorem](research_cap_constrained_capacity_budget.md).
The odd real stability, exact root-variance bound, and strict finite
omitted-tail gap are in
[the global negative-axis reduction](research_global_cap_negative_axis_and_mahler_bound.md).
The geometric alternative is
[the original one-cap chain budget](research_one_cap_original_chain_volume_budget.md).

Root derivation complete. Coherent independently read sections 1–4
in full and reported analytical/source PASS, including the anchored
Hessian, actual positive coefficient torus, fixed complex neighborhood,
derivative convergence and fixed-spectrum scope. The explicit
conductance formulas (10)–(12) received a separate independent full
written review: PASS, including the zero-corner conventions, absence of
an extra energy factor, and the Bernoulli upper bound. These are internal proof reviews,
not external peer review.
