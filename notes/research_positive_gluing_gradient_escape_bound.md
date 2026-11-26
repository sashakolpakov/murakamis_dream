# A quantitative gradient gap for positive logarithmic gluing

Research proof, 23 November 2026.

A realized positive marked gluing system has a full-gradient bound on
its entire positive logarithmic chart. The bound uses curvature only
near its solution. It excludes escape of the selected logarithmic
coordinates to infinity in finite normalized descent time. Finite
flat-angle or cut-boundary exits remain possible and are retained.

This is a classical no-infinite-coordinate-escape statement. It does
not identify an original quantum period with this chart or establish
the no-ends hypothesis for its relative cycle.

## 1. Positive coordinates and the marked constraint

Let \(t\geq1\), and put
\[
 \mathcal S=\{x\in\mathbb C:0<\Im x<\pi\},\qquad
 z=e^x,\qquad v(x)=-\operatorname{Log}(1-e^x).
 \tag{1}
\]
The logarithm is principal. Apply \(v\) coordinatewise on
\(\mathcal S^t\). On this convex product,
\[
 \Im v'(x)=\frac{\Im(e^x)}{|1-e^x|^2}>0.
 \tag{2}
\]
Let \(A,B\) be real \(t\)-by-\(t\) matrices with
\[
 \operatorname{rank}(A\ B)=t,\qquad AB^{\mathsf T}=BA^{\mathsf T},
 \qquad F_R(x)=Ax+Bv(x).
 \tag{3}
\]
Keep one specified affine logarithmic target \(c\). In an actual
ideal triangulation these are the independent edge rows and one
marked primitive peripheral row per cusp of [G]. Every edge winding,
quad constant and peripheral logarithmic lift belongs to \(c\).
We assume a positive solution is supplied, not merely that the
exponentiated equations have a solution.

## 2. Positive quad selection removes the invertible-block restriction

Here is the transversal argument of [Q] in convention (1). Since
\[
 (A+iB)(A+iB)^*=AA^{\mathsf T}+BB^{\mathsf T}>0,
 \tag{4}
\]
the column expansion of \(\det(A+iB)\) has a nonzero term choosing
one of \(A_j,B_j\) in each column. For every selected \(A_j\), make
the positive cyclic quad change
\[
 z'_j=\frac1{1-z_j},\qquad
 (x'_j,v'_j)=(v_j,i\pi-x_j-v_j).
 \tag{5}
\]
Both new coordinates are the principal positive logs of their stated
quad types. The functions \(1/(1-z)\) and \(z/(1-z)\) map the upper
half-plane to itself, so \(0<\Im(x+v)<\pi\). Exponentiating and
checking these arguments proves (5) on the entire positive domain.

For the rotated columns, substitution gives
\[
 A'_j=B_j-A_j,\qquad B'_j=-A_j,\qquad
 c'=c-i\pi\sum_{j\ \mathrm{rotated}}A_j .
 \tag{6}
\]
Other columns are unchanged. The new \(B'\) is the chosen nonzero
transversal up to column signs. The linear part of (5) is real
symplectic, so the rank and isotropy conditions (3) persist.
The marked target is transformed by (6), not reset modulo
\(2\pi i\). This choice depends only on the rows, not on a later
solution or on the quantum level. Drop primes henceforth.

Now \(B\) is invertible and
\[
 P=B^{-1}A=P^{\mathsf T}\in M_t(\mathbb R),\qquad
 u=B^{-1}c,\qquad
 S(x)=\sum_{j=1}^t\operatorname{Li}_2(e^{x_j})
             +\tfrac12x^{\mathsf T}Px-u^{\mathsf T}x,
 \quad \nabla S=B^{-1}(F_R(x)-c).
 \tag{7}
\]
The dilogarithm is its principal upper-half-plane branch, whose
derivative in \(x\) is \(v(x)\). Let \(x_*\in\mathcal S^t\)
denote the supplied solution in these selected coordinates.

The sign and normalization in (7) agree with the positive classical
potential [Q, (4)]. Explicitly its alternative coordinate is
\(y=\operatorname{Log}(1-1/z)=i\pi-x-v\). Thus
\(A_y=A-B\), \(B_y=-B\), \(c_y=c-i\pi B\mathbf1\), and
\(B_y^{-1}A_y=I-P\), \(B_y^{-1}c_y=-u+i\pi\mathbf1\).
Substitution in that displayed potential gives exactly (7).
No claim identifying its additive constant with an unsupplied
quantum-source transformation is needed below.

## 3. Curvature near the solution controls the full chart

Choose \(r>0\) so that the closed Euclidean ball
\(\overline{B(x_*,r)}\) is contained in \(\mathcal S^t\), and put
\[
 m=\min_{\substack{y\in\overline{B(x_*,r)}\\1\leq j\leq t}}
             \Im v'(y_j)>0.
 \tag{8}
\]
For example take \(r\) smaller than half the distance of every
\(\Im x_{*,j}\) from \(0,\pi\). The numerator in (2) then has
a positive lower bound and its denominator a finite upper bound
on this ball. All norms below are Euclidean.

**Theorem.** For every \(x\in\mathcal S^t\),
\[
 \boxed{\quad
 \|\nabla S(x)\|\geq m\min(\|x-x_*\|,r).
 \quad}
 \tag{9}
\]
In particular the full gradient is bounded away from zero outside
the ball, including at every escaping sequence in this chart.

**Proof.** Set \(d=x-x_*\). The joining segment remains positive.
As in the secant comparison of [G],
\[
 \Im\bigl(d^*\nabla S(x)\bigr)
   =\sum_j|d_j|^2\int_0^1\Im v'(x_{*,j}+sd_j)\,ds.
 \tag{10}
\]
Here \(\nabla S(x_*)=0\), and the contribution \(d^*Pd\) is real.
Every integrand is positive. On the first
\(\min(1,r/\|d\|)\) portion of the segment each is at least \(m\).
Consequently, for \(d\ne0\),
\[
 \Im\bigl(d^*\nabla S(x)\bigr)
       \geq m\|d\|\min(\|d\|,r).
 \tag{11}
\]
Cauchy--Schwarz and division by \(\|d\|\) prove (9).
At \(d=0\) the assertion is immediate. \(\square\)

This also gives \(\|F_R(x)-c\|\geq mr/\|B^{-1}\|\) outside
the ball. Thus approximate full fixed-log gluing cannot escape
within the positive chart. Neither a representation-volume theorem
nor control of a weighted residual at infinity is required for
this restricted conclusion.

The constants can be uniform in families. Suppose real symmetric
\(P_a\) and targets \(u_a\) have supplied critical points
\(x_{*,a}\) in a compact subset of \(\mathcal S^t\).
A common positive radius \(r\) makes the union of the closed balls
have compact closure in \(\mathcal S^t\), and (2) supplies a common
\(m>0\) there. The proof gives (9) for
every member, without a bound on its filling coefficients in \(P_a\).
For varying constraint rows, use a specified common invertible
quad chart wherever that family has one. No unrecorded transition
between different selected charts is included in the assertion.

## 4. Growing phase and finite descent time

For the growing classical exponential and its height, use
\[
 e^{NS(x)/(2\pi i)},\qquad
 h(x)=\Re\frac{S(x)}{2\pi i}=\frac{\Im S(x)}{2\pi},
 \qquad \|\nabla_{\mathbb R}h\|=\frac{\|\nabla S\|}{2\pi}.
 \tag{12}
\]
At fixed parameters, consider the normalized lowering flow away
from the critical point,
\[
 \frac{dx}{ds}=-\frac{\nabla_{\mathbb R}h}{
                              \|\nabla_{\mathbb R}h\|^2},
 \qquad \frac{dh}{ds}=-1.
 \tag{13}
\]
Outside \(B(x_*,r)\) its speed is at most \(2\pi/(mr)\).
For any trajectory remaining in the positive chart, its distance
from the center therefore satisfies
\[
 \|x(s)-x_*\|
 \leq\max(r,\|x(0)-x_*\|)+\frac{2\pi s}{mr}.
 \tag{14}
\]
Indeed every excursion outside the ball starts either at the initial
point or on its radius-\(r\) sphere; its total outside time is at
most \(s\). Inside the ball the distance is already at most \(r\).
Thus no selected logarithmic coordinate can diverge in finite
normalized descent time, equivalently during a finite height drop.
These bounds are uniform for the families just described. They
do not construct a continuation of an arbitrary target path.

## 5. Boundary and source scope

The flow may reach a finite flat-angle or logarithmic cut boundary,
or approach the critical point, where the normalized field is
singular. No such exit is removed. A positive quad rotation can send
an old \(z\to0\) end to \(z'\to1\); hence boundedness of the
selected logs is not a quad-invariant exclusion of ideal
degenerations. All finite \(0,1,\infty\) interpretations and the
corresponding boundary currents remain to be treated in the actual
coordinates and with their marks.

The Legendre contour of [L] already has a calibrated volume maximum,
controlled radial homotopies and explicit alias bulk translations.
The estimate here concerns instead the full principal gradient over
the entire positive product, using only a local curvature constant.
It settles the infinite-coordinate part of a normalized-flow check
while that flow stays in this specified positive chart. It proves
neither a boundary-action gap nor absence of relative-cycle handles
from cuts, finite boundaries or other logarithmic charts.

In particular no original Kashaev source, cap, normal direction or
relative current has been replaced. A source-preserving passage to
this positive polarization and control of its actual boundary terms
remain necessary. There is no selected-cycle, scalar lower-bound or
finite-exception conclusion.

## Complete sources and coverage

- [G] [Global positive marked log gluing](research_global_positive_log_gluing.md), 226 lines, SHA-256 `8b712324fb10211e2b5f253c934bac1f0270a719645b7cad6493a85437c2286f`: the actual marked incidence interpretation and secant comparison. The quantitative estimate is proved above.
- [Q] [Positive quad selection and classical torus](positive_quad_chart_and_actual_torus_signature.md), 213 lines, SHA-256 `eee291f797da0d19c327612ab6fd46a6fa13fd5b270880c0c05c138242e3d93f`: quad-transversal coverage and the exact positive classical potential. Its linear selection argument is supplied above in convention (1).

[L] [Global Legendre contour](general_legendre_rivin_contour.md), 421 lines,
SHA-256 `b51be11036b05fbccd586c2d0a4505559631870357cf128dd256dcc87e26970b`,
is complete coverage, not an additional premise of (9)--(14).
No claim of historical novelty is made for positive symplectic
gluing or monotonicity. Only written mathematics and source-text
operations are used; no frozen file is changed.
