# The exact even CROSS endpoint is not real stable, and the remaining parity adapter

31 October 2026. Research result: exact-source reduction and obstruction.
The local nonstability and stable-reference comparison are proved in the
stated scope; the actual global even negative-axis adapter remains open.
The finite counterexample uses the original even CROSS projection at
sigma=-2. It is not a nearby complete-circle model. The obstruction is
local; no failure of stability or of an absolute bound for a globally
extracted original exterior is inferred from it.

## 1. Literal even source and an exact N=6 counterexample

Use the central factorization in
[actual cofactor factorization](actual_cross_cofactor_factorization.md), sections 1–2. For N=2m,
theta=pi/N, put

$$
\begin{aligned}
a_j&=2+2\cos((2j+1)\theta),\qquad s_j=2\sin(j\theta),\qquad A=x+y,\\
R_0(b)&=1,\\
R_j(b)&=b^j\prod_{0\le r<j}a_r+s_j^2 A R_{j-1}(b)
+s_js_{j-1}a_{j-1}xyR_{j-2}(b).
\end{aligned}\tag{1}
$$

with absent negative-index terms zero. Set

$$
D_b=R_{m-1}(b),\qquad E_b=a_{m-1}R_{m-2}(b).
$$

The ACTUAL polynomial, with its fixed common raw sign removed, is

$$
P_{\mathrm{cross}}=s_m^2 A D_bD_c
+s_ms_{m-1}xy(D_bE_c+E_bD_c).\tag{2}
$$

All three central path types remain. No unused factor, spectral
derivative, or CROSS-support condition has been replaced.

Take N=6, m=3 and x=y=1. Write r=sqrt3. Then

$$
\begin{aligned}
a_0&=2+r,\quad a_1=2,\quad a_2=2-r,\\
s_1&=1,\quad s_2=r,\quad s_3=2,\\
L(z)&=R_1(z)=(2+r)z+2,\\
D(z)&=R_2(z)=2(2+r)z^2+6(2+r)z+12+2r.
\end{aligned}\tag{3}
$$

Thus (2), exactly, is

$$
\begin{aligned}
P_{\mathrm{cross}}(1,b,c,1)
&=4\bigl[2D(b)D(c)+k(D(b)L(c)+L(b)D(c))\bigr],\\
k&=\frac{2r-3}{2}>0.
\end{aligned}\tag{4}
$$

Specialize the remaining real variable c=-2. Since
D(-2)=4-2r and L(-2)=-2-2r, the original source becomes

$$
P_{\mathrm{cross}}(1,b,-2,1)
=(8-8r)b^2+(12-16r)b+72-48r.\tag{5}
$$

Its discriminant is

$$
\Delta=-6000+3456\sqrt3<0.\tag{6}
$$

For a fully rational sign certificate, sqrt3<125/72 because
3*72^2=15552<15625=125^2; multiplying gives (6).

A real-stable polynomial remains stable or zero after real
specializations. The nonzero quadratic (5) has one upper-half-plane
zero, contradicting that condition. Equivalently, perturb
x,y,c to 1+i epsilon,1+i epsilon,-2+i epsilon. The simple nonreal
root b of (5) continues to an upper-half-plane root for all sufficiently
small positive epsilon, providing a zero with ALL four imaginary
parts positive. Therefore:

$$
\begin{gathered}
\text{The original even CROSS endpoint polynomial is not real stable}\\
\text{in its four face variables, already at }N=6.
\end{gathered}\tag{7}
$$

This is an exact source counterexample, not a numerical root plot.
The symbolic expansion of (1)--(4) independently reproduces (5)--(6).

## 2. Why the simplest auxiliary-cofactor pencil cannot repair this

The candidate joint pencil R_(m-1)(b)+t R_(m-2)(b) also fails at
the same original level and the same positive x=y=1. Indeed

$$
D(b)-4L(b)=2(2+\sqrt3)(b^2+b+1).\tag{8}
$$

A real-stable polynomial in b,t could not have this nonstable
specialization t=-4. Multiplying the t coefficient by the original
positive a_(m-1) only rescales the real counterexample t and does not
repair it. Thus a Hermitian PSD pencil realizing this exact auxiliary
cofactor pair is impossible. This does not exclude a different
source-level decomposition or a globally extracted stability theorem.

For comparison, the operator
(x+y)+kxy partial_t DOES preserve real stability when applied to a
polynomial stable jointly in all its indicated variables: after
division by xyP, both 1/x+1/y and partial_t log P have nonpositive
imaginary part, with the first strictly negative. The failure here
is the required actual input pencil, not that elementary operator
fact. No substitute complete-node pencil is inserted.

Even the proposal to treat the three central summands separately as
stable products fails: an individual cofactor appearing in them need
not be stable. At N=8, M=3, set x=y=1 and put

$$
r=\sqrt2,\qquad u=\sqrt{2+\sqrt2},\qquad
v=\sqrt{2-\sqrt2},\qquad uv=r.
$$

The literal recurrence (1) gives

$$
R_2(b)=(2+u)(2+v)b^2+4(2+u)b+v^2(8+2u+r).\tag{8a}
$$

since s_1=v, s_2=r, a_0=2+u and a_1=2+v. Its discriminant is

$$
\Delta_2=4(2+u)\bigl[4(2+u)-(2+v)v^2(8+2u+r)\bigr]<0.\tag{8b}
$$

The sign requires no root computation: u<2, u>3/2, v>3/4 and r>1
give the bracket strictly less than
16-(11/4)(9/16)12=16-297/16<0. The bound v>3/4 follows from
sqrt2<23/16, whose square is a rational inequality. Thus the ACTUAL
E_b=a_3 R_2(b) in (2) is not stable. A constant-size stable decomposition
does not follow by viewing the three displayed central terms as its
components. This does not exclude a different decomposition of the
original polynomial.

## 3. The exact stable even comparison polynomial survives globally

There IS a genuine positive stable comparison, but its logical scope
must be kept exact. The [original even half-block theorem](actual_fejer_half_block_entropy.md), section 5,
defines the actual nearest complete-channel lower cofactors

$$
D_b^*=R_M(b;u_*),\qquad M=m-1,\qquad
u_*=-2+2\cos(\pi/N).
$$

and proves the coefficientwise inequalities

$$
\begin{aligned}
B_{\mathrm{cross}}&=4(x+y)D_b^*D_c^*
\le_{\mathrm{coef}} P_{\mathrm{cross}}(-2)<_{\mathrm{coef}}3B_{\mathrm{cross}},\\
D_b^*&=C_{\mathrm{front}}D_M(x,b,y),\qquad
C_{\mathrm{front}}=\frac{N}{2\sin(\pi/N)}.
\end{aligned}\tag{9}
$$

Here D_M is the original positive Hermitian determinant. The
polynomials in (9) retain the original level N and the ONE forced
x-or-y unit. The shift u_* is the actual closest complete folded
node; (9) does not assert it equals the full endpoint coupon.

Since x+y and both determinant factors are real stable, B_cross is
real stable. For an original one-cap exterior with R-1 CROSS coupons,
let Q_N(A,C) be obtained by using these B_cross coupons and performing
the SAME protected specialization and EVERY same exterior face
coefficient extraction as for P_N(A,C). Then

$$
\begin{gathered}
Q_N\text{ is zero or nonnegative real stable},\qquad
\deg Q_N=d=N-1\quad\text{when }Q_N\ne0,\\
Q_N\le_{\mathrm{coef}}P_N\le_{\mathrm{coef}}3^{R-1}Q_N.
\end{gathered}\tag{10}
$$

The exact coefficient inequalities follow under products and
extractions; no face target changes. Under the standing nonzero
complete-source hypotheses Q_N is nonzero at all sufficiently large
levels. Its degree is d because B_cross has the same exact degree d
as P_cross, including the forced outer unit.

Consequently P_N and Q_N have the SAME normalized pressure at every
positive boundary fugacity, whenever either limit exists. In
particular, using the original both-parity positive coefficient
theorem near the strict stationary exterior, that common limit is
the same classical F(z) used at odd levels.

The compact-measure argument requires only convergence on a small
REAL interval here. The root measures of Q_N have bounded mass on
[0,1]. Any weak subsequential limit mu gives
integral log(1+p(e^z-1)) dmu(p)=F(z)-F(0) for real z in that interval,
since its kernel is bounded continuous in p. The integral is analytic
near z=0; equality on the real interval determines all moments.
Thus every subsequential limit is the SAME odd-level mu_D.

It follows rigorously that the stable REFERENCE exterior has the same
Mahler and negative-axis supremum rates as the odd original exterior:

$$
\begin{aligned}
\frac1N\log\operatorname{Mahler}(Q_N)&\longrightarrow M_{\mathrm{cap}}-\ell_D,\\
\frac1N\log\sup_{0\le t\le1}|Q_N(-t,1)|&\longrightarrow M_{\mathrm{cap}}+m^-,\\
\frac1N\log\sup_{0\le t\le1}|Q_N(-1,t)|&\longrightarrow M_{\mathrm{cap}}+m^+.
\end{aligned}\tag{11}
$$

This uses the logarithmic-supremum continuity theorem.
The passage from Q_N back to P_N at negative fugacity is NOT supplied
by (10).

## 4. Even exponentially sharp positive comparison is insufficient

Here is a concise general warning, not an original-source example.
For d>=1, j=floor(d/2) and fixed 0<a<log2, set

$$
Q_d(A,C)=(A+C)^d,\qquad
P_d(A,C)=Q_d(A,C)+e^{ad}A^jC^{d-j}.\tag{12}
$$

All coefficients are nonnegative. The central binomial coefficient
is at least 2^d/(d+1), so even the coefficientwise comparison is

$$
Q_d\le_{\mathrm{coef}}P_d
\le_{\mathrm{coef}}\bigl[1+(d+1)e^{-(\log2-a)d}\bigr]Q_d.\tag{13}
$$

The normalized positive pressure, and all coefficient exponential
rates, are unchanged. On any fixed real z interval, the pressure
also has the same locally uniform complex continuation in a small
neighborhood, because the added term is exponentially smaller than
(1+e^z)^d there.

Nevertheless for BOTH negative-axis intervals,

$$
\begin{aligned}
e^{ad}&\le\sup_{0\le t\le1}|P_d(-t,1)|\le1+e^{ad},\\
e^{ad}&\le\sup_{0\le t\le1}|P_d(-1,t)|\le1+e^{ad}.
\end{aligned}\tag{14}
$$

by evaluation at t=1 and the triangle inequality. The corresponding
two suprema of Q_d are exactly1. Thus neither positive pressure nor
even an exponentially sharp coefficientwise comparison transfers
negative-axis exponential rates. In particular the genuine
constant-factor source comparison (10) cannot by itself do so.

This example does not assert that the correction in (12) is realized
by an original CROSS exterior. It identifies the precise extra
signed/structural estimate that an even-parity adapter would need.

## 5. Current conclusion and remaining original-source question

The direct all-parity local stability extension is false by (5)--(7).
The stable nearest-fold comparison Q_N is an EXACT original-level,
same-target reference and has the desired limiting root measure.
What remains is a negative-axis/source contraction for the ACTUAL
difference P_N-Q_N, or a different exact positive decomposition with
controlled signed boundary values. A proof that the globally extracted
P_N itself is stable remains possible despite the local failure; no
such proof or counterexample is given here.

The original even and odd signed-cap finite moment identities remain
valid independently of stability. This note supplies no spectral
neighborhood, no signed-source lower rate, and no general filled
volume theorem.

## Inputs

Actual three central terms:
[actual cofactor factorization](actual_cross_cofactor_factorization.md), sections 1–2.
Nearest-fold comparison and its exact scalar:
[even half-block coefficient theorem](actual_fejer_half_block_entropy.md), section 5.
Positive physical determinant:
[positive physical determinant](actual_complete_circle_positive_face_polynomial.md), sections 1 and 3.
Original global extraction and odd root measure:
[original cap extraction and Mahler bound](research_global_cap_negative_axis_and_mahler_bound.md) and
[root measure and negative-axis supremum rates](research_cap_root_measure_from_classical_pressure.md).

The N=6 counterexample and N=8 individual-cofactor calculation are exact finite source obstructions. The nearest-fold positive comparison retains the same targets, but it does not control the actual negative-axis rate.
