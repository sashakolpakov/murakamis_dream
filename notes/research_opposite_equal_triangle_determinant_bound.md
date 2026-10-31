# An explicit cancellation bound for an original half-triangle determinant

31 October 2026. analytical research lemma. This concerns the actual
positive half-determinant at two equal, opposite face arguments. It is
not yet a theorem for a raw cleared cofactor, a whole cap star, or a
filled invariant. In particular, coefficientwise positive comparisons
cannot transfer this estimate to a signed evaluation.

## 1. The finite determinant and the bound

Put theta=pi/N and J=floor((N-1)/2). For a=J-k, where k>=0 is fixed,
use precisely the matrices in [the physical boundary model](actual_q_hahn_boundary_model_curvature.md),
section 1. They are a by a, with diagonal and upper adjacent entries

\[
 d_n=\frac1{\cos(n\theta)\cos((n+1)\theta)},\qquad
 (H_\pm)_{n-1,n}=\sqrt{b_n}\,[\sin(n\theta)\pm i\cos(n\theta)],
\]
\[
 b_n=\frac{\sin^2(n\theta)}
 {\cos^2(n\theta)\sin((2n-1)\theta)\sin((2n+1)\theta)}.
\tag{1}
\]

Their lower entries are the conjugates of their upper entries. The
original homogeneous half-determinant is

\[
 D_a(x,b,y)=\det\bigl(bI+(x/2)H_-+(y/2)H_+\bigr).
\tag{2}
\]

Fix C>0 and specialize x=-C,b=C,y=z, where z may be complex. Define

\[
 \mathcal J_C(z)=\frac1{2\pi}\int_0^\pi
 \log\max\{|z+Ce^{it}|,|z+Ce^{-it}|\}\,dt.
\tag{3}
\]

**Lemma.** Uniformly for C in any positive compact interval and z in
any complex compact set,

\[
 \limsup_{N\to\infty}\ \sup_{C,z}
 \left\{\frac1N\log|D_{J-k}(-C,C,z)|-\mathcal J_C(z)\right\}\le0.
\tag{4}
\]

The convention at a zero determinant is log 0=-infinity. In particular,
for REAL z, including z=0 and z=+-C,

\[
 \mathcal J_C(z)=\frac12\log\max\{C,|z|\}.
\tag{5}
\]

This is an upper bound. Zeros and oscillation preclude inferring a
uniform lower asymptotic. Both parities of N are included.

The same proof gives a prefix version needed by the actual nodal
cofactor adapter. For EVERY 0<=a<=J define

\[
 I_{C,z}(\alpha)=\int_0^\alpha
 \log\frac{\max\{|z+Ce^{2\pi it}|,|z+Ce^{-2\pi it}|\}}
 {4\cos^2(\pi t)}\,dt.
\]

Uniformly over these indices and the same parameter compacts,

\[
 \limsup_{N\to\infty}\ \sup_{a,C,z}
 \left\{\frac1N\log|D_a(-C,C,z)|-I_{C,z}(a/N)\right\}\le0.
\tag{5a}
\]

Here D_0=1. No lower bound for any prefix determinant is used.

## 2. Exact scalar recurrence and its bulk roots

Let Delta_n be the determinant of the leading n by n submatrix of
(2), after the stated specialization. Tridiagonal expansion gives
Delta_0=1, Delta_1=C+(z-C)/(2cos theta), and, for n>=1,

\[
 \Delta_{n+1}=A_{N,n}\Delta_n-B_{N,n}\Delta_{n-1},
\]
\[
 \begin{aligned}
 A_{N,n}&=C+\frac{z-C}{2\cos(n\theta)\cos((n+1)\theta)},\\
 B_{N,n}&=\frac{b_n}{4}
 \left[(z-C)^2\sin^2(n\theta)+(z+C)^2\cos^2(n\theta)\right].
 \end{aligned}\tag{6}
\]

For complex z this uses the product of the actual upper and lower
entries, not their absolute square. All scalar normalizations in (2)
remain present.

For t=n/N in a fixed closed subinterval of (0,1/2), the transfer
matrix [[A,-B],[1,0]] converges, with error O(1/N), to the matrix with

\[
 A(t)=\frac{z+C\cos(2\pi t)}{2\cos^2(\pi t)},\qquad
 B(t)=\frac{z^2+C^2+2Cz\cos(2\pi t)}{16\cos^4(\pi t)}.
\tag{7}
\]

The two roots are EXPLICIT:

\[
 \lambda_\pm(t)=\frac{z+Ce^{\pm2\pi it}}{4\cos^2(\pi t)},
 \qquad \lambda_+(t)-\lambda_-(t)=iC\tan(\pi t).
\tag{8}
\]

They never collide on that bulk interval, independently of z. The
eigenvector matrix with columns (lambda_+,1) and (lambda_-,1), its
inverse, and its first t derivative have uniform bounds on the stated
compact sets. In particular

\[
 \rho(t):=\max(|\lambda_+(t)|,|\lambda_-(t)|)
       \ge\tfrac12 C\tan(\pi t)>0.
\tag{9}
\]

## 3. Product estimate, with both endpoint portions retained

Fix eta>0 and work first on eta<=t<=1/2-eta. Conjugate each exact
transfer matrix by the eigenvector matrices at its two adjacent
mesh points. Equations (6)--(8) give

\[
 E((n+1)/N)^{-1}T_{N,n}E(n/N)
       =\operatorname{diag}(\lambda_+(n/N),\lambda_-(n/N))+O_\eta(N^{-1}).
\tag{10}
\]

Thus its norm is at most rho(n/N)+O_eta(1/N). The positive lower
bound (9) makes the accumulated logarithmic error O_eta(1), not
order N. Taking products and using the endpoint bounds for E proves
the bulk upper bound by the SUM of log rho, with o(N) error.
This retains the larger modulus at each step. For real z the two
moduli coincide, so there is no selection of one unproved action
branch or neglect of a growing transfer mode.

The omitted physical rows are controlled directly. From (1), for
every actual n in the matrix,

\[
 |A_{N,n}|+|B_{N,n}|+1
     \le C_K\bigl(1+\cos^{-4}((n+1)\theta)\bigr).
\tag{11}
\]

For example, sin((2n-1)theta)sin((2n+1)theta)
=sin^2(2n theta)-sin^2 theta; on the actual range 1<=n<=a-1 its
ratio to sin^2(2n theta) is bounded below uniformly for large N.
The first O(eta N) transfers therefore cost O(eta N), and the last
O(eta N) cost at most

\[
 O\bigl(\eta N\log(2/\eta)+\log N\bigr).
\tag{12}
\]

This follows by summing log(N/r) at the actual half-integer or
integer distances from the fold. A fixed k changes only a bounded
number of terminal rows. No inverse determinant, nonzero initial
component, or cancellation assumption is needed for this upper bound.

Uniformly on the compact parameter sets, log rho is integrable at
both ends: (9) bounds it below by log t-O(1) near zero and by
-log(1/2-t)-O(1) near the fold; (8) bounds it above by
O(1)+2|log(1/2-t)|. Its omitted integrals are consequently
O(eta log(2/eta)). First take N to infinity and then eta to zero.
The bulk Riemann sums and (12) give

\[
 \limsup \frac1N\log|D_{J-k}(-C,C,z)|
       \le\int_0^{1/2}\log\rho(t)\,dt=\mathcal J_C(z),
\tag{13}
\]

uniformly as asserted. The last equality uses
integral_0^(1/2) log(4cos^2(pi t))dt=0. The same estimates prove
continuity of (3), including its integrable boundary zeros.

For (5a), stop the same transfer product at the actual index a.
The retained bulk interval is eta<=t<=min(a/N,1/2-eta). If a/N<eta,
the entire product is in the short initial portion. Every omitted
integral and physical endpoint portion still has the bounds just
proved, uniformly in a. This proves the asserted prefix upper bound,
including sequences with a/N tending to either endpoint.

## 4. Real arguments and the positive comparison

If Im z>=0, the first modulus in (3) is larger; if Im z<=0, the
second is larger. For real z they are equal. The integral over a
half circle is then half the full-circle logarithmic mean. Expanding
log(1-w) for |w|<1 shows that this full-circle mean is
log max(C,|z|). The boundary |z|=C follows by the elementary integrable
logarithmic limit. This proves (5) without assuming an asymptotic
lower bound for the finite determinant.

For real z>0 the positive determinant D_{J-k}(C,C,z) has the known
triangle rate Q(C,C,z), with Q normalized by the original half-triangle
entropy. Consequently (4) proves the explicit rate loss

\[
 Q(C,C,z)-\tfrac12\log\max(C,z)>0.
\tag{14}
\]

Strictness follows by perturbing the pure corner of the largest
weight into another positive corner: the entropy gain is of order
-epsilon log epsilon and dominates its finite linear weight cost.
At z=0 the permitted two-corner triangle gives exactly

\[
 Q(C,C,0)-\tfrac12\log C=2f(1/4),\qquad
 f(s)=-\int_0^s\log\tan(\pi t)\,dt.
\tag{15}
\]

The rate for the positive comparator is from the original determinant,
[even half-block entropy normalization](actual_fejer_half_block_entropy.md),
section 5, and [the odd simple-fold determinant](actual_fejer_odd_regularized_full_numerator.md),
sections 2–3. These identify the full J determinant. For fixed k,
successive Schur pivots of the positive matrix
C I+(C/2)H_-+(z/2)H_+ lie between C and their diagonal upper bounds
O_K(N^2). Removing k terminal rows changes its logarithm by only
O_K(k log N). This proves the same comparator rate at J-k, at both
parities. Formula (14) quantifies one special angular loss; it does
not say that this loss pays the whole cap budget in an arbitrary star.

## 5. The adapter still required for the original cap problem

At even levels the original modified cofactor is
R_M*=C_front D_M, C_front=N/(2sin(pi/N)). The actual unmodified
cofactor R_M has a coefficientwise positive comparison with R_M*.
That comparison does NOT bound R_M(-C,C,z) by
R_M*(-C,C,z). It was proved before inserting signs. Likewise a
finite spectral interpolation of the raw CROSS polynomial requires
all its actual nodal cofactors and terminal terms.

Therefore (4) applies directly to (2), its retained polynomial scalar
multiples, and products for which that finite determinant adapter is
already exact. A separate [raw-cofactor theorem](research_opposite_equal_raw_cofactor_bound.md)
now supplies the missing finite-source argument when the third face
is REAL and nonnegative: the exact nodal cofactor, its signed tail,
and an absolutely normalized integral identity give the same bound
for R_(J-k) on the entire real spectral interval. This uses no signed
version of the invalid coefficientwise comparison above.

The arbitrary complex third-face case for that raw cofactor, the full
spectral star with all its shared phases, the absolute shared-volume
comparison, and the maximal Green pairing remain separate. No general
long-twist theorem follows from this determinant lemma alone.

The opposite-equal determinant values are exploratory diagnostics, not lower asymptotic bounds.