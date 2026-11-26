# Determining the longitude from the auxiliary peripheral equations

1 November 2026. A proposed application of algebraic rigidity, with the
remaining regularity hypothesis stated explicitly.

The local source equation determines both auxiliary peripheral pairs.
It also supplies a candidate contribution to the main longitude. This
note explains why a discrepancy between that candidate and the actual
main longitude has very little freedom. The first restriction follows
from the boundary pairing of a three-manifold; the second is algebraic.
The final restriction requires checking the representations over every
nonzero meridian value, including values far from the complete structure.

## 1. The edge equation and a closed differential

For an edge with endpoint variables \(Q,P\), let \(E\) satisfy
\[
 (E+Q)(E+Q^{-1})(E+P)(E+P^{-1})
      =(E-1)^2(1-EM^2)(1-E/M^2).
 \tag{1}
\]
The variables are nonzero. We work first where all displayed factors
are nonzero and the selected root is simple. Write
\[
 u=\log M,\quad q=\log Q,\quad p=\log P,\quad z=\log E,
 \qquad
 f=\frac{M^2-E}{1-M^2E},\quad
 \rho_Q=\frac{Q+E}{1+QE},\quad
 \rho_P=\frac{P+E}{1+PE}.
 \tag{2}
\]
Only the differentials of the logarithms will be used. Their branches
therefore do not affect the identities below.

Let \(F\) be the logarithm of the quotient of the two sides of
(1), holding \(z,q,p,u\) independent before differentiating.
Direct differentiation gives
\[
 F_u=2(\log f)_z,\qquad
 F_q=-(\log\rho_Q)_z,\qquad
 F_p=-(\log\rho_P)_z.
 \tag{3}
\]
On the edge surface \(dF=0\). Moreover \(f\) has no direct
\(q,p\) dependence, and each \(\rho\) has no direct
\(u\) dependence or dependence on the other endpoint. Thus
\[
 \begin{aligned}
 &du\wedge d\log f+
   \tfrac12d\log\rho_Q\wedge dq+
   \tfrac12d\log\rho_P\wedge dp\\
 &\quad=\tfrac12(F_u\,du+F_q\,dq+F_p\,dp)\wedge dz=0.
 \end{aligned}
 \tag{4}
\]
This proof uses the rational equation itself. It does not identify a
geometric volume by comparing numerical critical values. Since (4) is
an identity of rational differential forms, it holds on every smooth
part of the same algebraic component.

## 2. The actual boundary pairing

Suppose the ordered pieces have been assembled into a representation
of the original augmented link exterior. Let \(L\) be the
eigenvalue of its preferred main longitude on the main
\(M\)-eigenline. At each auxiliary circle let \(U_v\) be the
logarithm of the primitive meridian similarity, and let the selected
longitude eigenvalue be \(-Q_v\). The exact local construction and
the original half-twist convention give
\[
 U_v=\sum_{e\ni v}\log\rho_{v,e}-\epsilon_v\log Q_v,
 \qquad \epsilon_v\in\{-1,0,1\},
 \tag{5}
\]
up to locally constant logarithmic periods. The summands and the
primitive word must be established by the actual boundary gluing.

The infinitesimal boundary pairing is
\[
 du\wedge d\log L+
             \tfrac12\sum_v dU_v\wedge d\log Q_v=0.
 \tag{6}
\]
Here all tori use the meridian--longitude orientations induced by the
same oriented exterior. The factor one half occurs because \(U_v\)
is a logarithm of an eigenvalue ratio, whereas \(\log Q_v\) is
a logarithm of a single determinant-one eigenvalue.

For completeness, (6) has a direct topological proof. Infinitesimal
variations of a representation are one-cocycles with values in its
adjoint local system. Pair two such cocycles by
\(\operatorname{tr}(XY)\) and take their cup product. The result
is a closed ordinary two-cochain, because the trace pairing is
invariant under conjugation. Its total evaluation on the boundary
of a fundamental three-chain is zero by the cochain Stokes identity.
On a torus with commuting diagonal holonomies, write their logarithms
as \(x\operatorname{diag}(1,-1)\) and
\(y\operatorname{diag}(1,-1)\). The alternating trace pairing
is \(2(dx\wedge dy)\). Summing over the boundary tori gives
\(\sum dx\wedge dy=0\). Substitute
\((x,y)=(u,\log L)\) at the main torus and
\((x,y)=(U_v/2,\log Q_v)\) at the auxiliary tori. This proves
(6) where the peripheral matrices are diagonalizable. The rational
identity extends over the remaining points where its terms are defined.

Subtract the sum of (4) over all edges from (6). The half-twist term
in (5) has zero wedge product with \(d\log Q_v\). The result is
\[
       du\wedge d\log\left(\frac{L}{\prod_e f_e}\right)=0.
 \tag{7}
\]
In particular, the discrepancy has no infinitesimal dependence on any
auxiliary variable. To avoid choosing determinant-one lifts globally,
use the squared discrepancy
\[
                         R=\frac{L^2}{\prod_e f_e^2}.
 \tag{8}
\]
It is a rational function whenever the original projective peripheral
representation is rational on the source variety: \(L^2\) is the
ratio of the two eigenvalues of the main longitude, with its ordered
main flag retained.

## 3. Why the discrepancy is rational in the main meridian

Let \(k=\mathbb C(M)\), and let the graph have distinct unordered
edges. In particular this applies to a tree. The edge equations are
quadratic after putting \(Z=E+E^{-1}\):
\[
 Z=\frac{2(M^2+M^{-2})-(Q+Q^{-1})(P+P^{-1})}
 {Q+Q^{-1}+P+P^{-1}+M^2+M^{-2}+2}.
 \tag{9}
\]
Work on the open set where these denominators are invertible; it
contains the complete branch. The squareclass of \(Z^2-4\) is
\[
 H_e=(Q_v-1)^2(Q_w-1)^2
                  -4(M+M^{-1})^2Q_vQ_w.
 \tag{10}
\]
To see that the edge squareclasses are independent, extend the
coefficient field to an algebraic closure \(\overline{k}\).
Put \(t=(M+M^{-1})^2\ne0\) in this field. As a quadratic in
\(Y\), the polynomial
\((X-1)^2(Y-1)^2-4tXY\) has discriminant
\[
                    16tX[X^2+(t-2)X+1].
 \tag{11}
\]
Its order of vanishing at \(X=0\) is one, so it is not a square
in \(\overline{k}(X)\). Its coefficients in \(Y\) have no
common factor: at \(X=1\) the middle coefficient is \(-4t\).
It is therefore irreducible in \(\overline{k}[X,Y]\).

Different edges give different such prime polynomials, since they
involve different pairs of independent vertex variables. The valuation
at the prime \(H_e\) is odd for its own squareclass and zero for
every other edge. Hence every nonempty product of edge squareclasses
is nonsquare. Adjoining their square roots has degree \(2^{|E|}\)
even after extending \(k\) to \(\overline{k}\). This proves
geometric integrality of the generic source fiber over \(M\).
In particular \(k\) is algebraically closed in its function
field \(\mathcal F\).

The logarithmic derivatives in all the \(Q_v\) extend uniquely
to the finite separable field \(\mathcal F\). If an element of
\(\mathcal F\) is killed by every such derivative, its relative
differential over \(k\) vanishes. In characteristic zero it is
algebraic over \(k\), and therefore belongs to \(k\) by the
preceding paragraph. Applying this to (7)--(8) gives
\[
                              R\in\mathbb C(M)^*.
 \tag{12}
\]
The specialization of (10) at \(M=\pm i\) is a square. This
does not invalidate the generic integrality proof; it does mean that
those fibers need a separate check in the next step.

## 4. The unit criterion and its consequence

The following regularity condition is sufficient. For every
\(M_0\in\mathbb C^*\), require a point over \(M=M_0\)
at which:

* the assembled projective representation and its chosen main
  eigenvalue ratio extend regularly along a local section through
  nearby values of \(M\);
* that eigenvalue ratio is nonzero;
* all the edge factors \(f_e\) are finite and nonzero.

The point can have generic auxiliary variables. It need not describe
a positive or faithful hyperbolic structure. A local algebraic cover
in the section is harmless: a nonzero order of vanishing of a rational
function in \(M\) remains nonzero after such a cover.

Under this condition, (8) has neither a zero nor a pole at any
\(M_0\ne0\). A nonzero rational function with this property
is a unit of \(\mathbb C[M,M^{-1}]\). Thus
\[
                              R=cM^k,
                 \qquad c\ne0,\quad k\in\mathbb Z.
 \tag{13}
\]
This assertion is elementary: factor the numerator and denominator
over \(\mathbb C\); every surviving finite root must be zero.

At the complete main cusp, \(f_e=1\) and \(L^2=1\), so
\(c=1\). If the already established marked cusp calculation is
\[
 \left.\frac{d\log L}{d\log M}\right|_{M=1}
  -\left.\frac{d\log\prod_e f_e}{d\log M}\right|_{M=1}
                         =a_{\rm aug},
 \tag{14}
\]
then \(k=2a_{\rm aug}\), and
\[
                    L^2=M^{2a_{\rm aug}}\prod_e f_e^2.
 \tag{15}
\]
For the original preferred augmented longitude the existing framing
calculation gives \(a_{\rm aug}=-\sum_v\epsilon_v-w_\epsilon\).
The preferred longitude after the auxiliary fillings adds
\(\sum_v p_v\ell_v^2\) to that exponent. The original identities
\(n_v=\epsilon_v-2p_v\) and
\(\ell_v^2=2(1+o_v)\) then give the source exponent
\(a(D)=-w(D)-\sum_v n_v\).

Passing from (15) to an unsquared longitude also requires its actual
complete determinant-one lift. Once that lift has value \(-1\),
holomorphic continuation fixes the sign as
\(L=-M^{a_{\rm aug}}\prod_e f_e\) near completeness.

The proposed application still requires the regularity condition
above for the actual assembled representation. The differential and
generic-field arguments alone do not prove (13). If an exceptional
main value forces a pole in every admissible chart, an extra rational
factor can remain and must be calculated. This is the specific
point being checked.
