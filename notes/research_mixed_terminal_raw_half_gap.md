# A calibrated raw comparison on the whole terminal right half

Research deduction, 5 November 2026. This strengthens the coherent
half-point comparison on the same two external-leg rectangles. The
outward record proves its finite bound; the saved replay records its
independent verification. The
external complex leg remains unchanged; this is not a bound after an
arbitrary height attenuation or on all open-reference height boxes.

## 1. The full row envelope and the calibrated reference

Use exactly \(g,J,Q_\epsilon,\mathcal X_\epsilon\), the original
endpoint graph \((e(a),t(a),u(a))\), and rectangles \(R_3,R_4\)
of the [coherent half-point theorem](research_mixed_terminal_half_endpoint_gap.md).
Write
\[
 P_\epsilon(a)=\mathcal X_\epsilon(a,e(a),t(a),u(a)),\qquad
 h_h=\Re\{J(1/2)+F(1/2,1/4+i\log(3)/(4\pi))\}.
\tag{1}
\]
Thus \(P_\epsilon\) is the original holomorphic optimized action
including the full terminal diagonal weight. It is not a real-variable
maximum.

The bare conditional row envelope at the half point is
\[
\begin{split}
 \mathcal R_\epsilon(a)&=\max_{0\le v\le1}
 \{I_a(v)+I_0(v,1/2)-(2+\epsilon)J(v)-2\pi v\Im a\},\\
 I_a(v)&=\int_0^v\log|1-e^{-2\pi i(a+t)}|\,dt.
\end{split}
\tag{2}
\]
Every physical row is retained. The
[complete right-row theorem](research_mixed_complex_right_row_reduction.md)
and [row bracket](research_mixed_right_boundary_row_bracket.md)
apply because the direct target \(a\in R_3\cup R_4\) has
\(\Re a\in[.1,.5]\), \(|\Im a|\le.057\).
They prove that the full maximum in (2) is attained at its unique
lower-row maximizer \(v_*(a)\in(1/5,2/5)\). On that interval
\(a+v\) stays in the original sine strip. Its rate is exactly
\[
 R(v,a)=\Re\{J(a+v)-J(a)+J(v+1/2)
                     -(2+\epsilon)J(v)+i\pi av\}.
\tag{3}
\]
This identity is valid across \(\Im a=0\) and retains the original
chirp. It is not an independently chosen interpolation.

**Theorem 1.** For all four own/external type choices and every direct
target in the corresponding rectangle,
\[
       \Re P_\epsilon(a)-h_h-\mathcal R_\epsilon(a)>1/300.
\tag{4}
\]

## 2. Boundary reduction and its finite check

For fixed \(v\), \(I_a(v)\) is subharmonic in \(a\).
The integrated logarithmic singularities are locally uniformly
integrable, so the row rate is jointly continuous in \((a,v)\).
The compact-row maximum in (2) is consequently continuous and
subharmonic. Explicitly, choose a row attaining the maximum at the
center of any small disk; its submean inequality and its pointwise
upper bound by \(\mathcal R_\epsilon\) give the submean
inequality for the maximum. Therefore
\[
           \Re P_\epsilon-h_h-\mathcal R_\epsilon
\tag{5}
\]
is superharmonic, and its minimum lies on the rectangle boundary.
Equivalently, after the established full-row reduction, every fixed
row in \([1/5,2/5]\) in (3) is harmonic in \(a\), so its
comparison with \(\Re P_\epsilon\) transfers individually
from the boundary and then one takes the row maximum. No
subharmonicity of \(\mathcal R(\Re a+i\lambda\Im a)\)
for a nonholomorphic attenuation is used.

The checker reuses precisely the 258 original endpoint leaves and
275 side incidences from the coherent check. All 16 rectangle sides
and all 10,978 original tree nodes are accounted for. There are no
new endpoint roots or parameter subdivisions.

For clarity the scalar optimizer enclosure is elementary. Set
\[
 T(v,a)=\Re\{J'(a+v)+J'(v+1/2)
                       -(2+\epsilon)J'(v)+i\pi a\}.
\tag{6}
\]
It is the derivative of (3). On \(0<v<1/2\),
\(0<\Re a<1/2\), one has
\[
 T_v\le-\pi\{\tan\pi v+\cot\pi v\}\le-2\pi.
\tag{7}
\]
Indeed if \(\Re(a+v)<1/2\),
\(\Re\cot\pi(a+v)\le\cot\pi\Re(a+v)\le\cot\pi v\);
otherwise that real cotangent is nonpositive. This proof does not
require a small imaginary part. The actual full-row reduction still
uses the stated \(.057\) height hypothesis.

The checker verifies \(T(1/5,a)>0>T(2/5,a)\) on each entire
old parameter cell. At the midpoint it saves a rational bracket of
width at most \(2^{-40}\), whose two original-log signs are
rechecked on replay. If \(v_0\) is its rational midpoint, (7)
gives the whole-cell enclosure
\[
 |v_*(a)-v_0|\le |T(v_0,a)|/(2\pi).
\tag{8}
\]
Intersection with \([1/5,2/5]\) preserves the enclosure.
An enclosing old cell can extend a little beyond the admitted height
band. On that part we only extend the lower-row maximum (3), whose
strict concavity and bracket have just been verified. Equality to the
full-row envelope is used only at the actual side points in \(R_3,R_4\).

The reference action and the raw midpoint value are enclosed
directly. In real differentiation, the unknown optimizer response
multiplies \(T(v_*,a)=0\), while the endpoint responses multiply
the three original zero equations. The exact complex representative
of the remaining two real derivatives is
\[
 G(a)=g'(t(a)+a)+2\pi it(a)
                 -g'(a+v_*(a))-2\pi iv_*(a).
\tag{9}
\]
Thus the gradient is \((\Re G,-\Im G)\). An ordinary
rectangular mean-value bound gives the outward lower bound in (4)
on each retained side cell. This numerical use of Danskin's formula
does not assert that the optimized raw function is holomorphic.
The minimum principle then proves (4) on the whole rectangles.

## 3. The original finite terminal sector

The [polynomial endpoint collar theorem](research_mixed_endpoint_polynomial_collar.md)
now gives the full finite terminal right-angle reduction, including
its endpoint layer and arbitrary fixed complex neighbors. It keeps
every raw row and says
\[
 h(e)+\mathcal R_\epsilon(a,e)
 \le h_h+\mathcal R_\epsilon(a,1/2)-K(e),\qquad
 K(e)=-\int_{1/2}^e\log\sin\pi t\,dt
       \ge\frac{\pi^2}{6}(e-1/2)^3
\tag{10}
\]
for \(1/2\le e\le1\), with a single arbitrarily small finite
source tolerance. The term at \(e=1\) is included, and
\(K(1)=\log2/2\). No coherent replacement of the raw half
envelope is made in this step.

At these real terminal angles the actual Fourier polynomial has
upper exponential rate zero, and every terminal selected monomial
has unit modulus. Hence (4) and (10) give, for either
\(\sigma\in\{0,\epsilon\}\),
\[
\begin{split}
 &\left|C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ie})
 H_N(w_R,e^{2\pi ie})d_N(e^{-2\pi ie})^\epsilon
                          e^{2\pi iN\sigma e}\right|\\
 &\qquad\le C N^A
  \exp N\{\Re P_\epsilon(a)-1/400-K(e)\},
 \quad a\in R_{3+\nu},\quad 1/2\le e\le1 .
\end{split}
\tag{11}
\]
A sufficiently small fixed ordinary-color disk and each fixed
ordinary derivative are allowed; their tolerance is spent once.
All source factors are literal, and no lower bound on the possibly
vanishing terminal Fourier polynomial is used.

For a fixed open word \(m\ge2\) whose last external critical
leg lies in the interior of its rectangle, the local remaining
unaliased coordinates may vary as in the coherent theorem. Its
original one-ended Schur estimate keeps the completion loss. At
the level of complete-color leading rates the resulting bound is
\[
 M_m-1/300-K(e)-\frac{3\pi}{49}\|x-x_*\|_2^2.
\tag{12}
\]
With finite factors, a smaller gap such as \(1/400\) is retained.
Other selected outgoing variables, large motions of the remaining
coordinates, and external targets outside (8) of the coherent
theorem are not covered. In particular the wider open-reference
heights below \(-.057\) remain separate. This proves a strict
calibrated whole-right terminal sector on a meaningful restricted
neighbor region; it does not prove the entire open boundary
function or an arbitrary short-filling theorem.

## 4. Reproduction

    python3 experiments/check_mixed_terminal_raw_half_gap.py --precision 256
    python3 experiments/check_mixed_terminal_raw_half_gap.py --precision 320 --input repro/results/research-mixed-terminal-raw-half-gap.json --output repro/results/research-mixed-terminal-raw-half-gap-replay.json

