# A regularized convex problem for the actual main-color energy

20 November 2026. Research note; the manuscripts and previous research
finals remain unchanged.

The full matrix balance required by the tree capacity theorem can always
be obtained for the actual all-main-color source by minimizing one
explicit regularized convex objective. The definition uses the original
local tensors, their norms, and their original cap. It uses no unknown
Kashaev value. The ordinary trivial main color supplies the lower bound
needed for existence of a minimizer.

The resulting unpenalized objective approximates the logarithm of the
actual positive energy with an absolute error of order \(N^{-1}\).
Thus a separate nonzero cycle coefficient is not an additional premise
in this formulation. The remaining volume problem is to compare this
positive variational value with the Casson--Rivin geometric value.
That comparison is not proved here.

## 1. The prescribed tree and its positive objective

Use the vector-valued tree compiler of
[A positive variational formula for an actual source on a tree](research_scalar_tree_full_gauge_capacity.md),
Section 5. At level \(N\ge2\), its output is
\[
                   Y_N=(c_1,\ldots,c_N),\qquad
 \|Y_N\|^2=E_N=|K_N|^2+R_N,
 \qquad 0\le R_N\le(N-1)(N/2)^{2b-2}.
\tag{1}
\]
Here \(b\) is the fixed braid width, \(c_j\) are the original reduced
main-color values, and the prescribed partial pivotal trace and marked
cut are part of the root tensor. In particular \(c_1=1\), so
\[
                               \|Y_N\|\ge1.
\tag{2}
\]
This is an unconditional ordinary-color anchor. It does not assert
\(K_N\ne0\).

Let the tree have \(m\ge2\) vertices. Its internal edge spaces are
\(H_e\), of dimensions \(n_e\). They may be the full bundled operator
spaces of that compiler; the theorem does not restrict gauges to
individual physical wires. Write \(T_{v,N}\) for its actual local
tensors. They are all nonzero, since a zero local tensor would make
the output zero, contrary to (2).

For positive Hermitian edge matrices \(H=(H_e)_e\), let
\[
 L_N(H)=\sum_v\log\|T_{v,N}\|_H,
 \qquad F_N(H)=e^{L_N(H)}.
\tag{3}
\]
The local norms include \(H_e\) at one end and
\(\overline H_e^{-1}\) at the other, precisely as in the direct source.
That source proves
\[
 L_N(H)\ge\log\|Y_N\|\ge0,
 \qquad \inf_H L_N(H)=\log\|Y_N\|.
\tag{4}
\]
It also proves geodesic convexity of \(L_N\).

## 2. An elementary coercive regularizer

Define
\[
 Z(H)=1+\sum_e\operatorname{tr}(H_e+H_e^{-1}),
 \qquad \mathcal R(H)=\log Z(H),
 \qquad J_{N,\varepsilon}(H)=L_N(H)+\varepsilon\mathcal R(H),
 \quad\varepsilon>0.
\tag{5}
\]
All coefficients in this objective are known from the original finite
source. In particular its regularizer has no selected invariant in it.

**Proposition 1.** The function \(J_{N,\varepsilon}\) is strictly
geodesically convex and has a unique global minimizer in the product
of the positive cones.

**Proof.** Consider a simultaneous geodesic
\(H_e(t)=P_e e^{tX_e}P_e\), with \(P_e>0\) and \(X_e=X_e^*\).
After diagonalizing \(X_e\), both
\[
 \operatorname{tr}(P_e e^{tX_e}P_e),\qquad
 \operatorname{tr}(P_e^{-1}e^{-tX_e}P_e^{-1})
\]
are finite sums of real exponentials with positive coefficients.
The same is true of \(Z(H(t))\), including its constant term one.
Its logarithm is convex by the variance formula for the second
derivative of a logarithmic exponential sum. On a nonconstant geodesic,
some \(X_e\) has a nonzero eigenvalue. Its exponential and the constant
term one both have positive weights and distinct exponents. The variance
is then strictly positive. Together with (4), this proves strict
convexity.

For existence, take a minimizing sequence with objective at most
\(J_{N,\varepsilon}(I)+1\). By (4), its regularizer is bounded above.
Thus \(Z\) is bounded. Every eigenvalue \(\lambda\) of every edge
matrix satisfies a common bound on \(\lambda+\lambda^{-1}\). The
matrices consequently lie in a compact set bounded away from the
boundary of the positive cone. The finite tensor norms are continuous
and nonzero there. A convergent subsequence attains the infimum.
Two different minimizers would contradict strict convexity on the
positive-matrix geodesic joining them.
\(\square\)

No effective numerical minimization is needed in what follows.

## 3. The minimizer is approximately balanced in the full matrix norm

At a given metric, gauge by \(g_e=H_e^{1/2}\), normalize each local
tensor, and let \(\rho_{v,e}\) denote its reduced density matrix on
an incident leg. The original bilinear edge pairing prescribes the
full mismatch
\[
                  \Delta_e=\rho_{v,e}-\rho_{w,e}^{\mathsf T},
             \qquad S(H)=\sum_e\|\Delta_e\|_1.
\tag{6}
\]
No diagonal entries or first normal directions have been discarded.

**Theorem 2.** Every global minimizer \(H^{(\varepsilon)}\) of (5)
satisfies
\[
 \Delta_e=-\frac{2\varepsilon}{Z(H^{(\varepsilon)})}
                         (H_e^{(\varepsilon)}-(H_e^{(\varepsilon)})^{-1}),
 \qquad S(H^{(\varepsilon)})\le2\varepsilon.
\tag{7}
\]
The final bound is independent of all edge dimensions.

**Proof.** Orient an edge so that \(g_e\) acts at \(v\) and its
inverse transpose at \(w\). Vary it by
\(g_e(s)=e^{sX}P\), where \(P=H_e^{1/2}\) and \(X=X^*\).
The metric varies through \(H_e(s)=P e^{2sX}P\). The full norm
derivative proved in the direct source is
\[
                      \left.\frac{dL_N}{ds}\right|_0
                                        =\operatorname{tr}(X\Delta_e).
\tag{8}
\]
The two trace derivatives in (5) are elementary:
\[
 \left.\frac d{ds}\right|_0\operatorname{tr}H_e(s)
                  =2\operatorname{tr}(XH_e),\qquad
 \left.\frac d{ds}\right|_0\operatorname{tr}H_e(s)^{-1}
                  =-2\operatorname{tr}(XH_e^{-1}).
\]
Stationarity for every Hermitian \(X\) gives the matrix equality
in (7). Since \(H_e\) and \(H_e^{-1}\) have common eigenvectors,
\[
 \|H_e-H_e^{-1}\|_1\le\operatorname{tr}(H_e+H_e^{-1}).
\]
Summing the first equality of (7) therefore gives
\[
 S(H^{(\varepsilon)})
 \le\frac{2\varepsilon}{Z(H^{(\varepsilon)})}
               \sum_e\operatorname{tr}(H_e^{(\varepsilon)}
                                      +(H_e^{(\varepsilon)})^{-1})
 <2\varepsilon.
\]
The weak inequality stated in (7) follows. \(\square\)

## 4. A regularized objective which preserves the full energy rate

Set
\[
       \varepsilon_N=\frac1{m^2N^2},\qquad
       H_N\in\operatorname*{argmin}_{H>0}J_{N,\varepsilon_N}(H),
       \widehat F_N=F_N(H_N).
\tag{9}
\]
This definition uses only original local tensors, their edge spaces,
and the explicit numbers \(m,N\). It makes no assumption about the
complete main color.

**Corollary 3.** Whenever
\(a_{N,m}=1-4\sqrt2/N-10/(mN^2)>0\),
\[
        \boxed{\qquad
          a_{N,m}\widehat F_N\le\sqrt{E_N}\le\widehat F_N.
        \qquad}
\tag{10}
\]
For a fixed tree, in particular,
\[
 0\le\log\widehat F_N-\tfrac12\log E_N=O(N^{-1}),
 \qquad
 \frac{2\pi}{N}\log\widehat F_N
       -\frac\pi N\log E_N=O(N^{-2}).
\tag{11}
\]

**Proof.** Theorem 2 gives \(S(H_N)\le2/(m^2N^2)\). Insert this
in the full-marginal tree estimate of the direct source,
\[
 \frac{\|Y_N\|}{F_N(H_N)}\ge[1-4m\sqrt{S(H_N)}-5mS(H_N)]_+.
\]
This is the first inequality in (10); tree Cauchy gives the second.
Taking logarithms and using \(-\log a_{N,m}=O(N^{-1})\) proves
(11). \(\square\)

The quantity \(\widehat F_N\) is the **unpenalized** product of local
norms, evaluated at a minimizer of the penalized problem. There is
no assertion here that
\(\varepsilon_N\mathcal R(H_N)=o(N)\). Substituting the minimum
value of \(J_{N,\varepsilon_N}\) for \(\log\widehat F_N\) without
controlling that penalty would be an additional step.

There is a useful exact stability under blocking. Contract any connected
subtree, with all its original phases and marked tensors, into one
tensor. The resulting tree has exactly the same output \(Y_N\).
Apply (9) separately to the two presentations, using their respective
numbers of vertices. For every \(m\ge2\),
\(a_{N,m}\ge a_N=1-4\sqrt2/N-5/N^2\). Thus, for \(N\ge8\),
\[
 \left|\log\widehat F_N^{\rm before}
             -\log\widehat F_N^{\rm after}\right|
                         \le-\log a_N=O(N^{-1}).
\tag{11a}
\]
Both logarithms lie in the same interval
\([\log\|Y_N\|,\log\|Y_N\|-\log a_N]\), which proves this
bound without an estimate for an intermediate source. If blocking
leaves one tensor, its unpenalized norm is exactly \(\|Y_N\|\).
The bound is independent of block complexity and edge dimensions.
It applies in particular after exact contraction of any fixed short
component. It does not identify that component's geometric asymptotic,
or assert equality of the penalized objective values.

## 5. The optimizing matrices are algebraic at a fixed level

There is also a finite-level algebraic statement, distinct from any
bound as \(N\) grows. Suppose all local tensor entries are algebraic
numbers and \(\varepsilon\) is positive rational. These assumptions
hold for the original root-of-unity matrices and (9). Then every entry
of the minimizing matrices is algebraic.

To prove this, use real coordinates for the Hermitian matrices
\(P_e=H_e^{1/2}\). Their real and imaginary entries form an open
coordinate domain. Each squared local norm \(s_v=\|T_{v,N}\|_H^2\)
and \(Z\) is a rational function in these coordinates with algebraic
coefficients. They have no zero denominator and are positive in this
domain. Consequently
\[
           dJ_{N,\varepsilon}
                 =\tfrac12\sum_v\frac{ds_v}{s_v}
                                      +\varepsilon\frac{dZ}{Z}
\tag{11b}
\]
is a vector of rational functions. Clearing nonzero denominators in
its stationary equations gives polynomial equations with algebraic
coefficients.

At the minimum the Hessian is positive definite: along every nonzero
tangent the second derivative of the regularizer is strictly positive,
and the local norm objective is geodesically convex. Because the first
derivative vanishes there, the ordinary coordinate Hessian has the
same positive quadratic form. The Jacobian of the cleared stationary
equations is therefore invertible.

For completeness, a solution of polynomial equations in characteristic
zero with invertible Jacobian has algebraic coordinates over their
coefficient field. Otherwise its finitely generated coordinate field
has a nonempty transcendence basis. Differentiation in one basis
variable extends through its finite separable algebraic extension:
differentiate each minimal polynomial and divide by its nonzero
derivative. Applying this derivation to the stationary equations and
using their invertible Jacobian makes the derivatives of every
coordinate zero. That contradicts differentiation of the chosen
transcendence basis variable. This proves the assertion.

The size and degree of these algebraic points are not bounded here
uniformly in \(N\). Algebraicity alone does not determine the limiting
value of (3), and no such inference is used.

## 6. A regularized flow on the actual compiler edges

The minimizing metrics can also be specified by a convergent flow.
Keep \(N\) and \(\varepsilon>0\) fixed, and put
\[
 P_e=H_e^{1/2},\qquad
 G_e=\Delta_e+\frac{2\varepsilon}{Z(H)}(H_e-H_e^{-1}).
\tag{11c}
\]
Starting at any positive metrics, solve
\[
                         \dot H_e=-\tfrac12 P_eG_eP_e.
\tag{11d}
\]
Everything on the right is computed from the original local tensors,
the current edge metrics, and the one positive scalar \(Z\). In
particular no value of \(K_N\) or selected geometric coefficient is
used in this equation.

The flow exists for all nonnegative time and converges to the unique
minimizer of (5). Here is a direct verification. In the positive-matrix
metric \(\langle U,V\rangle_H=\operatorname{tr}(H^{-1}UH^{-1}V)\),
the derivative formulas above give gradient
\(\tfrac12 P_eG_eP_e\). Thus
\[
                  \frac{dJ_{N,\varepsilon}}{dt}
                             =-\tfrac14\sum_e\operatorname{tr}(G_e^2).
\tag{11e}
\]
The entire trajectory stays in a compact positive sublevel set, by
Proposition 1's coercivity proof and (4). The smooth vector field is
bounded there, so finite-dimensional local existence continues for
all time. Equation (11e) and the lower bound on \(J\) show that the
squared norm of \(G\) is integrable in time. It is uniformly continuous,
since both the vector field and its derivatives are bounded on that
compact set. It therefore tends to zero: otherwise disjoint intervals
of uniformly positive length would give an infinite integral.
Every accumulation point is consequently critical. Geodesic convexity
makes each critical point a global minimum, and strict convexity makes
that point unique. Compactness then gives convergence of the entire
trajectory.

This is a full matrix flow on the compiler edges, with its original
source retained. It has not been identified with a classical flow of
dihedral angles on an ideal triangulation.

## 7. What is now required for the finite-exception program

For a fixed hyperbolic knot of complement volume \(V>0\), (1) and
(10)--(11) give the equivalence
\[
 \lim_N\frac{2\pi}{N}\log|K_N|=V
 \quad\Longleftrightarrow\quad
 \lim_N\frac{2\pi}{N}\log\widehat F_N=V.
\tag{12}
\]
The implication from energy to the original scalar uses the polynomial
ordinary-color remainder, as proved in the direct source. It does not
assume eventual nonvanishing of \(K_N\).

Consequently the remaining task in this formulation is a quantum to
classical variational comparison. One must determine the leading
unpenalized objective at these actual full matrix minimizers and show
that it is the hyperbolic volume. Classical angle balance by itself
does not prove that comparison. The construction above does supply
the full matrix balance, including the original source, but gives no
description of the minimizing matrices by geometric shapes.

Fix any short partial assignment. For each completion of the remaining
integer coefficients that gives a one-component knot, apply the
construction to that completed knot's original compiler. Its ordinary
trivial main color again equals one, so existence and the estimates
above apply to that completion. This makes no assertion about the
source of an intermediate unfilled link or an open family of boundary
variables, and requires no intermediate exterior to be hyperbolic.
To obtain the proposed finite-exception theorem, the
comparison in (12) must hold for all sufficiently long remaining
fillings after each required fixed short partial assignment. The
coefficients are fixed before the level tends to infinity. Infinite
fibers representing a fixed hyperbolic core still require the same
volume comparison for that core.

This reformulation has removed an independent lower-bound hypothesis
for the closing overlap. It has not proved (12)'s geometric limit,
exchanged an uncontrolled infimum and limit, or added a new knot class
with a proved volume identity.

## Direct proof source

The complete direct source was read, including its zero-output proof,
full marginal estimate, actual all-main-color compiler and limitations:

* [A positive variational formula for an actual source on a tree](research_scalar_tree_full_gauge_capacity.md),
  SHA-256 `2997b732aa73e063c66e81d6487a1d9927509609d61842c1dbb43d9345df1d6d`.

The coercive regularizer, its elementary convexity proof, the stationarity
identity (7), and estimates (10)--(11) are proved above. Only written
mathematics and text/hash operations were used. No mathematical program,
numerical test, build, git operation, frozen-file edit, or public-document
change was performed.
