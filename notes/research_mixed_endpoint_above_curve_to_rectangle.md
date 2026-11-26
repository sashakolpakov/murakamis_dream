# Extending the shallower endpoint region to the existing rectangle

Research deduction, 8 November 2026. The endpoint theorem between
the real axis and the auxiliary-real curve extends through real
part \(27/100\), with private depth at most \(3/50\). This reaches
the left edge of the previously proved deeper endpoint rectangle.
It covers the shallower side of the curve; points below it still
require their separate proof. No numerical evaluation is used.

## 1. Region and complete source statement

Keep the source \(C_N\), phase \(F\), and original root \(u_c\) of
[the theorem above the auxiliary-real curve](research_mixed_endpoint_region_above_real_curve.md).
Extend the explicit curve
\[
p(t)=1-2t^2+2it,\qquad
e(t)=\frac{\Log p(t)}{2\pi i}=E(t)-i\eta_0(t)
                                                               \tag{1}
\]
to \((\sqrt3-1)/2\le t\le4/5\). Its real part increases strictly.
At the right endpoint,
\[
\arg p(4/5)=\pi/2+\arctan(7/40)>27\pi/50,
                                                               \tag{2}
\]
since \(\arctan(7/40)\ge7/40-(7/40)^3/3>1/6>\pi/25\).
Thus (1) defines a unique depth \(\eta_0(E)\) for every
\(1/8\le E\le27/100\). Set
\[
\mathcal W_1=
\left\{E-i\eta:\frac18\le E\le\frac{27}{100},\
0\le\eta\le\min\{\eta_0(E),3/50\}\right\}.
                                                               \tag{3}
\]

**Theorem.** On a fixed complex neighborhood of
\(\mathcal W_1\times\{-2\}\), the complete original endpoint sum
satisfies
\[
C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                 (1+O_{\rm hol}(N^{-1})),\qquad A(e,w)\ne0,
                                                               \tag{4}
\]
with the original normalization, both level parities, and all
fixed normalized mixed derivatives on smaller neighborhoods.

## 2. The curve and critical branch on the added interval

No new critical equation is needed. Along (1),
\[
u_0=\frac{\arctan t}{\pi},\qquad
\omega=\frac{1+it}{1-it},\qquad
\frac p\omega=\frac{1+t^2+2t^4+2it^3}{1+t^2}.
                                                               \tag{5}
\]
Here \(0<u_0<E<1/2\). The last ratio has positive real and
imaginary parts, fixing the argument difference without a
logarithmic ambiguity. The original exponentiated equation is
one, and its imaginary derivative belongs to
\((-\pi/2,\pi E)\); therefore \(F_u(e,u_0)=0\) on its original
zero lift.

The force factorization of the curve theorem is still exact:
\[
e^{2R_x(e,x)}-1=\frac{(y-1)Q_T(y)}{T^2},\qquad
y=t\cot\pi x,\quad T=t^2,
\]
\[
Q_T(y)=(1+T)y^5+(T-1)y^4+T^2(1+y+y^2+y^3).
                                                               \tag{6}
\]
Its proof of positivity used only \(T>2/15\), not \(T\le1/2\):
\(\partial_TQ_T>0\) for \(y\ge0\), and the fixed polynomial
at \(T=2/15\) is positive. Consequently the whole lower-half
real row rate still increases to \(u_0\) and decreases after it,
including the rows past the private endpoint.

Sections 2--3 of the shallower-region theorem now apply for
every \(E\le27/100\). Their branch argument uses \(E<1/2\),
the uniqueness of the real auxiliary root in (5), and the
upper-half-plane root of the original quadratic. It proves
\[
0<\Re u_c<E,\qquad \Im u_c\ge0
                   \quad(0\le\eta\le\eta_0(E)).
                                                               \tag{7}
\]
The two endpoint-gap derivatives retain their signs. The
left gap begins at the positive real profile \(h(E)\), and
the right gap begins at the strictly smaller curve value
\(R(e,E)<R(e,u_0)\) established by (6).
This proves both gaps, and in particular the original-action
lower bound
\[
\Re S(E-i\eta)>-2J(1/2-E)-3J(E)
                                                               \tag{8}
\]
on (3). The intermediate branch argument may use curve
depths greater than \(3/50\); it uses only the regular
critical equations there and asserts no finite-sum asymptotic
outside (3).

## 3. The additional upper-half comparison

Only the range \(1/4\le E\le27/100\) requires a new source
comparison. The original real primitive increases on
\([1/6,1/2]\), with \(J'(s)\le\log2<7/10\).
The printed Catalan-series inequality used in the curve
theorem gives \(-J(1/4)>14/99\). Thus
\[
\begin{split}
-J(1/2-E)&\ge-J(1/4)>14/99,\\
-J(E)&\ge-J(1/4)-(E-1/4)\log2
                             >14/99-7/500.
\end{split}
                                                               \tag{9}
\]
Combining (8)--(9) yields
\[
\Re S(E-i\eta)>
\frac{70}{99}-\frac{21}{500}
                         =\frac{32921}{49500}.
                                                               \tag{10}
\]

The exact reflected upper-half estimate remains
\[
R(e,x)<1/6+5\pi\eta/2 \qquad(1/2\le x\le1).
                                                               \tag{11}
\]
Indeed the proof uses \(0<E+1-x<1\), which still holds on
(3), the continuous real primitive bound \(-J<1/6\), and
the original sine argument bound by \(\pi/2\).
Since \(\eta\le3/50\), (11) is less than
\[
\frac16+\frac{3\pi}{20}<\frac{67}{105}.
                                                               \tag{12}
\]
The own-action gap is strictly greater than \(1/50\):
\[
\frac{32921}{49500}-\frac{67}{105}
 =\frac{9347}{346500}>\frac1{50}.
                                                               \tag{13}
\]
For \(E\le1/4\), retain the two previously proved upper-half
comparisons. Every physical and revived upper row is therefore
paid throughout (3).

## 4. Completion of the original finite sum

The lower-half force is monotone in private depth, exactly
as equation (16) of the shallower-region theorem. Its value
at any point of (3) is at most its value on the curve with
the same \(E\). Equation (6) therefore pays the entire
upper lower-half tail after a cut just before \(E\).
The cubic singularity of the force at zero pays the lower
tail. The two endpoint gaps of Section 2 permit uniform
cuts surrounding the actual auxiliary critical point on
the compact region (3).

Use the original finite interpolation and cotangent identity
with density \(+N\). The horizontal main line passes through
the critical point at its nonnegative auxiliary height.
The symmetric-height reflection comparison retains the loss
\[
\pi(1-2E)H\ge(23\pi/50)H>0 \qquad(H>0).
\]
Vertical convexity pays both weighted side halves and both
unweighted joining segments. At zero critical height use
the fixed small rectangle, with the same strict cut gaps.
All source arguments remain in their original regular
strips on retained contours; omitted rows retain the
zero-safe bounds, including every reciprocal zero.

Thus every source group in Section 5 of the shallower-region
theorem is present and paid. Its original nonzero Gaussian
symbol gives (4). Fixing cuts and paths at base parameters,
then taking a finite cover and applying Cauchy's formula,
gives the stated holomorphic error and fixed mixed derivatives.

The theorem supplies the shallower part of the previously
missing private-index strip up to \(27/100\). It does not
cover \(\eta>\eta_0(E)\), construct an outer-cap contour,
or enlarge the established knot family.
