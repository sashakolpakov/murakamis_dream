# A uniform opposite-equal-face bound for the original cleared cofactor

31 October 2026. Internally reviewed analytical research theorem.
This concerns the ORIGINAL raw cleared cofactor R_j, not only its
complete determinant. It is a signed evaluation at x=-C,b=C,y=Z>=0,
uniform over every real spectral value. No original shared-source
Phi_D bound or filled-invariant conclusion is asserted.

## 1. Statement and exact source

Put theta=pi/N, J=floor((N-1)/2), and fix a nonnegative integer k.
Set j=J-k, restricting to N large enough that j>=0. Use the original

\[
a_r=2+2\cos((2r+1)\theta),\qquad s_r=2\sin(r\theta),
\qquad u=-(\sigma+2).
\]

The cleared cofactor R_j is defined by R_0=1 and

\[
R_j=b^j\prod_{r<j}(a_r+u)
+s_j^2(x+y)R_{j-1}
+s_js_{j-1}(a_{j-1}+u)xyR_{j-2}.
\tag{1}
\]

with the last term absent at j=1. This is exactly the finite source in
[original cleared cofactor source](actual_cross_cofactor_factorization.md) section 1. Every original
inhomogeneous term is retained.

For C in a fixed compact subinterval of (0,infinity) and Z in a
fixed compact subinterval of [0,infinity), the claim is

\[
\limsup_{N\to\infty}\ \sup_{\substack{C,Z\\-4\le u\le0}}
\left\{\frac1N\log|R_{J-k}(-C,C,Z;u)|
-\frac12\log\max(C,Z)\right\}\le0.
\tag{2}
\]

The logarithm at a zero is -infinity. Both level parities are included.
Equivalently there is a uniform o(N) upper error in (2). A fixed
finite set of k can be included uniformly.

On the spectral fold u(delta)=-4sin^2(pi delta), polynomial Bernstein
also gives

\[
|R_{J-k}(-C,C,Z;u(\delta))|
\le
\exp\left[N\left(\frac12\log\max(C,Z)+o(1)\right)
+2\pi j|\operatorname{Im}\delta|\right].
\tag{3}
\]

The zero third face is included; C stays bounded away from zero.
The real estimate is the mathematical point; (3) is only its exact
degree-j spectral extension.

## 2. Exact nodal adapter and a uniform positive tail estimate

At the LOWER physical nodes u_a=-a_a, 0<=a<=j, the original source
adapter gives

\[
R_j(-C,C,Z;u_a)=S_{2a}D_a(-C,C,Z)K_{a,j}(-C,Z;u_a),
\qquad S_r=\prod_{v=1}^r s_v.
\tag{4}
\]

This is [original nodal cofactor adapter](actual_cross_cofactor_global_angular_gap.md) section 1,
equations (3)-(4), specialized without taking coefficientwise
absolute values. Here K_(a,a)=1, K_(a,a-1)=0 and the tail satisfies
the original homogeneous two-step recurrence.

Write B=|Z-C| and H=CZ. On the actual half-range a<r<=j<=J,
a_a-a_(r-1)>=0. A fixed sign change by sign(Z-C)^(r-a), when
Z!=C, therefore turns K into the nonnegative continuant

\[
\begin{aligned}
L_a&=1,\qquad L_{a-1}=0,\\
L_r&=p_rL_{r-1}+q_rL_{r-2},\\
p_r&=s_r^2B,\qquad
q_r=s_rs_{r-1}(a_a-a_{r-1})H.
\end{aligned}
\tag{5}
\]

Thus |K|=L. When Z=C the same statement follows directly: odd-length
terms are zero, and even-length terms are nonnegative. In particular
no absolute value has been inserted into an oscillatory sum of two
different signs.

Both p_r and q_r are nondecreasing in r on this ACTUAL range:
s_r,s_(r-1) increase before the fold, and a_(r-1) decreases.
The first q_(a+1) is zero. Add a FIXED epsilon>0 to B in p_r;
this only increases every L_r. Let p_r^epsilon=s_r^2(B+epsilon)
and define its local Perron root

\[
\lambda_r^\epsilon
=\frac{p_r^\epsilon+\sqrt{(p_r^\epsilon)^2+4q_r}}2>0.
\]

These roots increase with r. For
T_r=[[p_r^epsilon,q_r],[1,0]], the vector
v_r=(lambda_r^epsilon,1)^T is a positive right eigenvector.
Since v_(r-1)<=v_r componentwise, induction from (1,0)^T gives

\[
L_j\le
\frac{\lambda_j^\epsilon}{\lambda_{a+1}^\epsilon}
\prod_{r=a+1}^j\lambda_r^\epsilon
\le C_\epsilon N^2\prod_{r=a+1}^j\lambda_r^\epsilon.
\tag{6}
\]

For the empty interval K_(a,a)=1, no prefactor is needed.
The bound uses lambda_(a+1)^epsilon
=s_(a+1)^2(B+epsilon)>=c epsilon/N^2, while lambda_j^epsilon
is bounded above on the parameter compact. It therefore includes
a=0, a near the fold, and B=0. There is no hypothesis of distinct
tail eigenvalue moduli or a nonzero asymptotic seed.

For alpha in [0,.5] define the continuum root

\[
\begin{aligned}
\Lambda_\epsilon(t;\alpha)
=2\sin(\pi t)\Bigl[
&(B+\epsilon)\sin(\pi t)\\
&+\sqrt{(B+\epsilon)^2\sin^2(\pi t)
+4CZ\bigl(\sin^2(\pi t)-\sin^2(\pi\alpha)\bigr)}
\Bigr],
\qquad \alpha\le t\le\tfrac12.
\end{aligned}
\tag{7}
\]

In fact the exact finite roots are bounded DIRECTLY by (7) at
t=r/N, alpha=a/N. The p terms agree, while

\[
\begin{aligned}
q_r
&=16CZ\sin(r\theta)\sin((r-1)\theta)
\left[\sin^2((r-\tfrac12)\theta)
-\sin^2((a+\tfrac12)\theta)\right]\\
&\le16CZ\sin^2(r\theta)
\left[\sin^2(r\theta)-\sin^2(a\theta)\right].
\end{aligned}
\]

Every sine argument is in the increasing half-range; the exact
bracket is nonnegative for r>=a+1. Increasing the nonnegative q
increases the Perron root, proving the asserted upper bound.
The positive addition epsilon also supplies the uniform lower bound
Lambda_epsilon(t;alpha)>=4epsilon sin^2(pi t).
Consequently monotone Riemann upper sums in (6) give

\[
\limsup_{N\to\infty}\ \sup_{a,C,Z}
\left\{
\frac1N\log|K_{a,J-k}(u_a)|
-\int_{a/N}^{1/2}\log\Lambda_\epsilon(t;a/N)\,dt
\right\}\le0.
\tag{8}
\]

Here and below an empty tail has logarithm zero. For completeness,
log Lambda_epsilon is increasing in t. Its right-Riemann sum at
r/N differs from the integral by O_epsilon(log N), uniformly in
a, before division by N: the first cell is controlled by
4epsilon sin^2(pi t)<=Lambda_epsilon<=C_epsilon, and all remaining
cell discrepancies telescope. The fixed terminal defect k omits
only O(1) fold cells, with the same bound. Thus no half-step or
uncontrolled moving-alpha replacement is needed in (8).

As epsilon decreases to zero, these tail integrals decrease to

\[
I_{\mathrm{tail}}(\alpha;C,Z)
=\int_\alpha^{1/2}\log\Lambda(t;\alpha)\,dt,
\qquad \Lambda=\Lambda_0.
\tag{9}
\]

Their limit is finite and continuous jointly on the compact
parameter set and alpha in [0,.5], including Z=0. To see a uniform
integrable lower bound, if B>=C/2 then
Lambda>=2C sin^2(pi t); otherwise CZ>=C^2/2. These two cases give

\[
\Lambda(t;\alpha)\ge
c\sin(\pi t)\sqrt{\sin^2(\pi t)-\sin^2(\pi\alpha)}.
\]

with c>0 uniform on the stated compact. In particular B=0 has

\[
\Lambda(t;\alpha)
=4\sqrt{CZ}\sin(\pi t)
\sqrt{\sin^2(\pi t)-\sin^2(\pi\alpha)}.
\]

whose moving endpoint logarithm is integrable; the identity
sin^2(pi t)-sin^2(pi alpha)
=sin(pi(t-alpha))sin(pi(t+alpha))
gives uniform integrable logarithmic bounds, including alpha=0,.5.
Together with a uniform upper bound, these logarithmic bounds prove
continuity also as B tends to zero or Z tends to zero. Compact
monotone convergence of the
continuous integrals therefore makes epsilon->0 UNIFORM.
Equations (6)-(8) prove (8) with epsilon=0. This is an upper
estimate only; a zero odd-length tail causes no difficulty.

## 3. The exact integral cancellation

For C>0 and Z>=0 set

\[
S=C+Z,\qquad \rho=\frac{4CZ}{S^2},\qquad
\beta=\frac{|Z-C|}{S}=\sqrt{1-\rho},
\qquad \alpha\in[0,\tfrac12].
\]

Define, with integrable endpoint values,

\[
\begin{aligned}
I(\alpha)
={}&\int_0^{2\alpha}\log(2\sin(\pi t))\,dt\\
&+\int_0^\alpha
\log\frac{|Z+Ce^{2\pi it}|}{4\cos^2(\pi t)}\,dt
+\int_\alpha^{1/2}\log\Lambda(t;\alpha)\,dt.
\end{aligned}
\tag{10}
\]

Then EXACTLY

\[
I(\alpha)=\frac12\log\max(C,Z),
\qquad 0\le\alpha\le\frac12.
\tag{11}
\]

Here Lambda is (7) with epsilon=0 and its ACTUAL scale; no
undetermined normalization constant remains.

Proof first suppose 0<rho<1 and 0<alpha<.5. Put
v=sin^2(pi alpha), h=sqrt(1-rho v), beta=sqrt(1-rho)>0.
The derivatives of the first two integrals and the moving lower
endpoint of the third add to

\[
\log(h/\beta).
\]

Indeed Lambda(alpha;alpha)=4|Z-C|v, and
|Z+C exp(2pi i alpha)|=S h. For the remaining derivative, first
differentiate with respect to v and then put u=cot(pi t):

\[
\begin{aligned}
\int_\alpha^{1/2}\partial_v\log\Lambda(t;\alpha)\,dt
&=-\frac{\rho}{2\pi}
\int_0^{\cot(\pi\alpha)}
\frac{du}{A(u)(\beta+A(u))},\\
A(u)&=\sqrt{1-\rho v-\rho v u^2}.
\end{aligned}
\tag{12}
\]

Substitute
u=sqrt((1-rho v)/(rho v)) sin theta. At the upper endpoint
cos theta_*=beta/h. The elementary tangent-half-angle integral is

\[
\int_0^{\theta_*}\frac{d\theta}{\beta+h\cos\theta}
=\frac{\log(h/\beta)}{\sqrt{\rho(1-v)}}.
\]

Thus (12), multiplied by dv/dalpha=2pi sqrt(v(1-v)), equals
-log(h/beta). This cancels the moving-endpoint contribution exactly,
so I'(alpha)=0.

At alpha=0 the first two integrals vanish and

\[
\Lambda(t;0)=4\max(C,Z)\sin^2(\pi t).
\]

Since integral_0^(.5)log(4sin^2(pi t))dt=0, this gives (11).
The same uniform integrable logarithmic bounds as in section 2
justify alpha->0,.5, beta->0 and Z->0. In particular C=Z is
included by continuity; the derivation does not divide beta at that
limit. At Z=0 one may instead use Lambda=4C sin^2(pi t) directly.

## 4. Uniform nodal bound for the ACTUAL cofactor

The separately proved original determinant prefix bound is

\[
\frac1N\log|D_a(-C,C,Z)|
\le
\int_0^{a/N}\log\frac{|Z+Ce^{2\pi it}|}
{4\cos^2(\pi t)}\,dt+o(1).
\tag{13}
\]

UNIFORMLY for all 0<=a<=J and the stated parameter compact.
Its exact source and proof are in
[opposite-equal determinant prefix theorem](research_opposite_equal_triangle_determinant_bound.md) (5a):
the original tridiagonal determinant roots are
(Z+C exp(+-2pi i t))/(4cos^2(pi t)), both moduli retained.
This input is a genuine determinant upper, not an inference from
a coefficientwise positive comparison.

The elementary sine-product estimate gives, also uniformly in a,

\[
\frac1N\log S_{2a}
=\int_0^{2a/N}\log(2\sin(\pi t))\,dt
+O\!\left(\frac{\log N}{N}\right).
\tag{14}
\]

The products have no zero since 2a<=N-1. Splitting at the midpoint
and bounding the endpoint harmonic sums proves (14).

Combine the exact source (4), tail upper (8)-(9), determinant
upper (13), and sine product (14). Identity (11) proves

\[
\max_{0\le a\le j}|R_j(-C,C,Z;u_a)|
\le
\exp\left[N\left(\frac12\log\max(C,Z)+o(1)\right)\right].
\tag{15}
\]

The o(1) is uniform in a,C,Z and both parities. No coefficient
lower asymptotic or nodal nonvanishing is used.

## 5. Interpolation with the omitted nodes retained correctly

The polynomial R_j has degree at most j in u. The full physical
distinct-node grid has J+1 points u_a,0<=a<=J. We know (15) only
for a<=j=J-k. Define

\[
Q(u)=R_j(u)\prod_{a=j+1}^J(u-u_a).
\]

Then deg Q<=J; at each omitted node Q=0 exactly. Interpolation on
the original Chebyshev/Radau full grid has Lebesgue norm O(log N).
At retained nodes, the added product is bounded by 4^k. Therefore

\[
\sup_{[-4,0]}|Q|
\le C_k\log(N+1)
\exp\left[N\left(\frac12\log\max(C,Z)+o(1)\right)\right].
\]

Recovering R_j costs only a fixed polynomial. If q(t0)=0 for
t0 in [-4,0], then q(t)/(t-t0)=integral_0^1
q'(t0+s(t-t0))ds, so its interval supremum is at most sup|q'|.
The ordinary polynomial derivative bound costs O(J^2) per
removed factor (O(J^3) would also suffice). Repeat k times.
This proves (2). It also shows why no uncontrolled value at an
omitted node or division by a sampled zero enters the argument.

Finally apply the degree-j cosine Bernstein bound to obtain (3).
The nodal factorization, all scalar sine products and the odd
central endpoint remain literal original-source quantities.

## 6. Scope and useful consequence

The same actual positive cofactor has weighted rate
Q(C,C,Z) at u=0, by the [original complete half-triangle theorem](actual_fejer_half_block_entropy.md).
Thus (2) gives the explicit strictly positive asymptotic loss

\[
Q(C,C,Z)-\frac12\log\max(C,Z)>0.
\]

This is uniform on the stated compacts, including Z=0. The strict
inequality follows by a small positive triangle-corner perturbation
of the largest pure weight, retaining its entropy gain. At the protected
third face Z=0 this loss is exactly

\[
2f(\tfrac14)>0,\qquad
f(t)=-\int_0^t\log\tan(\pi s)\,ds.
\]


This upgrades the determinant-only result to the raw cleared
cofactor for ALL real spectra and a sufficiently thin fixed
spectral strip. It does NOT automatically give a coefficientwise
bound, an all-face-phase bound, a Green-star endpoint comparison,
or an absolute bound by the original complete source volume.
Other shared face targets and other coupons remain to be controlled.

Inputs are the exact source/node adapter, the reviewed determinant
prefix bound, and elementary positive transfer/interpolation.
No numerical scan or finite asymptotic test is used.
Internal review: root full analytical/source read, PASS; coherent partner
full independent analytical/source read, PASS, including the closed Z=0
extension. Geometry independently checked the exact integral identity
and the closed-face uniformity, PASS. The reviews concern the original
raw cofactor and its stated real face specialization; no arbitrary-face
torus or Phi_D conclusion is included. No numerical audit is required
for these exact identities and analytical upper bounds.
