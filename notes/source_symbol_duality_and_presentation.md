# Source-symbol certificates and dependence on the presentation

Independent audit and direct proofs, 27 October 2026. A nonzero
ordinary-color anchor does not imply simple root monodromy. The
correct selected-source condition has an exact dual certificate,
weaker than simplicity. The canonical actual Fourier--Mellin
source supplies that certificate without deleting Jordan blocks.

This complements [the source-corrected normal connection](source_corrected_quantum_normal_connection.md).
It does not identify the Mellin source line with the meridian
regular-profile line or prove the selected regulator norm.

## 1. The exact source/dual certificate

Let \(E=\mathbb C(Y)\), \(T_0=B_0\sigma_\zeta\) be invertible,
\(H=T_0^N\), \(L=H-I\), and let \(0\ne v\in\ker L\)
be the selected root section. Then
\[
 \iota(v)\ne0\text{ in }\operatorname{coker}L
 \quad\Longleftrightarrow\quad
 \operatorname{rank}[L\mid v]>\operatorname{rank}L
 \quad\Longleftrightarrow\quad
 \exists w:\ wL=0,\quad wv\ne0.                         \tag{1}
\]
These are equivalent elementary vector-space statements:
\(\iota(v)=0\) means \(v\in\operatorname{im}L\), and the
annihilator of \(\operatorname{im}L\) is the left kernel of \(L\).
Thus the needed witness is a dual monodromy cocycle that sees
the actual section. A physical cut with nonzero value need
not be such a cocycle.

There is a direct minors certificate at every rank. Choose a
nonzero \(r\)-minor \(A=L_{I,J}\), where \(r=\operatorname{rank}L\).
For \(i\notin I\), put
\[
 w_i=e_i^t-L_{i,J}A^{-1}e_I^t .
\]
The rank assumption gives \(w_iL=0\), and
\[
 \det\begin{pmatrix}A&v_I\\L_{i,J}&v_i\end{pmatrix}
                  =\det(A)\,w_iv.                     \tag{2}
\]
At least one such minor is nonzero exactly when (1) holds.
The rank-zero case uses the empty determinant convention:
the certificate is simply a nonzero coordinate of \(v\).

In corank one, any source cut \(\ell\) with \(\ell v\ne0\)
gives the single bordered certificate
\[
 \det\begin{pmatrix}L&v\\\ell&0\end{pmatrix}
                   =-\ell\,\operatorname{adj}(L)v.     \tag{3}
\]
As \(\ker L=Ev\), the rank-one adjugate satisfies
\(\operatorname{adj}(L)v=\operatorname{tr}(\operatorname{adj}L)v\).
Therefore (3) is nonzero exactly when \(\iota(v)\ne0\).
If \(\Delta(t)=\det(tI-H)\), its exact normalization is
\[
 \frac{\det\left(\begin{smallmatrix}L&v\\\ell&0\end{smallmatrix}\right)}
      {\ell v}
       =(-1)^d\partial_t\Delta(1),\qquad d=\dim_E M.     \tag{4}
\]
This supplies the requested adjugate/source test. A simple norm
root is sufficient, but (1) remains valid in higher corank,
where an adjugate or a first characteristic derivative can vanish
despite a visible selected section.

There is also an exact splitting interpretation. If \(T_0v=v\),
then (1) holds if and only if \(Ev\) has a \(T_0\)-equivariant
retraction from \(E^d\). For a witness normalized by \(wv=1\),
the projection \(p=vw\) commutes with \(H\). Average its conjugates:
\[
 \bar p=\frac1N\sum_{j=0}^{N-1}T_0^jpT_0^{-j}.
\]
Since \(T_0^NpT_0^{-N}=HpH^{-1}=p\), this is a
\(T_0\)-equivariant retraction onto \(Ev\). Conversely any such
retraction has a row \(w\) with \(wL=0,wv=1\).
Thus an invariant source line can fail to split even when it
is an ordinary saturated vector subspace.

## 2. Actual polynomial pointing does not imply simplicity

The actual unknot already distinguishes the statements. Its
color functions are exactly \(C_j(Q)=1\), including their full
polynomial pointing, and its minimal meridian operator is \(S-1\).
Use instead the equally valid actual annihilator
\[
 P_2=(S-1)^2 .
\]
Its solution companion is
\[
 A=\begin{pmatrix}0&1\\-1&2\end{pmatrix}=I+J,\qquad J^2=0,\ J\ne0 .
\]
For \(T=A^{-1}\sigma_\zeta\),
\[
 H=A^{-N}=I-NJ,\qquad
 \ker(H-I)=\operatorname{im}(H-I)=E(1,1)^t .
\]
The actual source \(v=(1,1)^t\) has \(\iota(v)=0\), even
though its first-coordinate cut and every color anchor equal one.
The cut \((1,0)\) does not annihilate \(H-I\).
Thus neither explicit polynomial colors nor their nonzero anchor
forces the source-symbol condition in an arbitrary actual presentation.

Even failure of a simple norm root does not imply failure of the
selected symbol. The actual unknot annihilator
\[
 (S-Q)(S-1)
\]
has a companion with distinct eigenvalues \(1,Q\) at every root
of level \(N\ge2\). Its monodromy is \(H=I\); hence
\(\iota\) is an isomorphism although
\(\Delta(t)=(t-1)^2\) has zero derivative at one.
The dual certificate (1), rather than simplicity alone, is the
appropriate invariant for the selected direction.

Removing a known extra left factor is legitimate only with its
source comparison. Scalar-operator module quotients induce
inclusions of solution modules, so left multiplication is not a
regular gauge of the same normal module. In the squared example,
the inclusion of the true rank-one source line into the enlarged
Jordan module sends its cokernel symbol to zero. This explains
exactly why the first-normal construction was not claimed invariant
under arbitrary annihilator left multiples.

## 3. Root saturation does not choose the whole normal quotient

The exact diagnostic
\[
 \mathcal A=(S-1)(S-Z),\qquad Z=Q^N,\qquad G_N=1+Y^N
\]
from the source-corrected note makes the issue explicit.
The minimal scalar operator of its root section \(1+U\) is \(S-1\),
but
\[
 (S-1)G_N=(Z-1)Y^N,\qquad (S-Z)G_N=1-Z.
\]
Neither whole factor annihilates this source. Replacing the whole
problem by its minimal root factor loses the source-normal rule.

Given the full actual source, one can make a rank-one whole quotient:
\[
 S-\frac{1+Z\,Y^N}{1+Y^N}.
\]
But its first-normal source-corrected connection is
\[
 U\partial_U-\frac{U}{1+U},
\]
so the quotient has retained the chosen source ratio itself.
For the other exact source \(A+B Y^N\), the corresponding quotient
and connection instead contain
\[
 \frac{A+B ZY^N}{A+B Y^N},\qquad
 U\partial_U-\frac{BU}{A+BU}.
\]
All have the same minimal root factor \(S-1\).
When \(A+B=2\), all root color values agree as well.
Consequently a root source-generated or saturated quotient can
restore a rank-one symbol but does not canonically determine its
whole normal lift from the root operator and anchor.

This does not deny the canonical quotient determined by a supplied
full marked source. It prevents using that quotient as an
operator-only proof of the very source comparison still needed.

## 4. The canonical actual Mellin source supplies a visible dual

There is a constructive way to obtain the certificate for every knot,
in the actual sourced Fourier--Mellin polarization. Retain
[the canonical finite-color source](fourier_mellin_actual_source.md):
\[
 Z(Q,X)=\sum_{n\ge n_0}C_n(Q)X^n,\qquad
 A(Q,X,S)Z=B(Q,X),\qquad Sf(X)=f(QX).
\]
Here \(A=P^M\), and \(B\ne0\) is a fixed Laurent polynomial
built from finitely many fixed actual colors. Its nonzero lowest
coefficient was proved in that construction.

Assume positive S-order and retain the canonical homogenization
\[
 P_h=(S-\sigma_QB/B)A .                                 \tag{5}
\]
On its companion vector \(v=(f,\sigma f,\ldots)^t\), the literal
observable source row is
\[
 \ell v=Af/B .
\]
The defining coefficient identity of (5) gives the quotient dynamics
\(\sigma_Q(Af/B)=Af/B\). Equivalently its companion matrix satisfies
\[
 \sigma_Q(\ell)A_h=\ell .
\]
Thus, for its \(T=A_h^{-1}\sigma_Q\), the row intertwines \(T\)
with the scalar shift. At a level-N root,
\[
 \ell H_0=\ell,\qquad \ell v_0=AZ_N/B=1.                 \tag{6}
\]
Equations (1) and (6) prove \(\iota(v_0)\ne0\), whether or not
the rest of \(H_0\) is semisimple. This is an observable quotient
of the same actual scalar state, not an unused adjoined unit.

This construction is robust under the original operator presentation.
If the original actual annihilator is replaced by a left multiple,
one rebuilds its canonical Fourier--Mellin source \(B\) and the
homogenization (5). The same finite-color construction makes that
\(B\) nonzero and (6) holds again. No deletion of Jordan blocks and
no minimal-annihilator assertion is needed. If the transformed
S-order is zero, \(AZ=B\) is its exact rational algebraic equation;
there is no need to manufacture a normal companion.

## 5. Formal first lifts suffice for the rational obstruction

The root rationality of
[the cyclotomic Mellin fiber](cyclotomic_mellin_residue.md)
gives \(Z_N\in E=\mathbb C(X)\). The first derivative of the
actual whole series is only asserted to lie in
\(F=\mathbb C((X))\). This is enough.

Each fixed \(C_n(Q)\) is Laurent polynomial and hence regular at
the root. Coefficientwise differentiation gives a formal \(Z_1\)
with the SAME fixed lower X bound \(n_0\). No common analytic
q-neighborhood, derivative growth bound in \(n\), or convergent
X-series is required. Rational coefficients of the fixed operator
and of \(B^{-1}\) are regular over \(E[[\epsilon]]\) for every
sufficiently large N: nonzero fixed rational Q-coefficients have
only finitely many exceptional root values. A possible moving
X-pole order in their epsilon expansion causes no problem in
\(F[[\epsilon]]\).

Therefore the homogeneous whole companion has a first lift
\(v_1\in F^d\) satisfying
\[
 L_0v_1+L_1v_0=0 .
\]
Both \(L_0\) and \(L_1v_0\) are rational over \(E\).
Solvability of this finite linear system over the field extension
\(F/E\) implies solvability over \(E\), by equality of matrix and
augmented ranks under field extension. Hence
\[
 D_N(v_0)=0\quad\text{in the rational descended cokernel}. \tag{7}
\]
If \(c(X^N)v_0\) also admits a first lift for the SAME whole
homogenized operator, (6), (7), and the Leibniz rule imply
\(U c'(U)\iota(v_0)=0\), and therefore \(c\) is constant.
The marked nonzero source/prefix anchor fixes it to one.

Negative Laurent S-powers must be normalized by a fixed left
shift applied to BOTH \(A\) and \(B\); the observable source
becomes its same shifted quotient. The proof then applies
without changing its pointing. No pole coefficient is discarded
before specialization.

The retained scalar is still the actual residue
\[
 K_N=\operatorname{Res}_{X=\infty} Z_N(X)\,dX/X .
\]
The theorem removes central scalar freedom on this canonical
selected Mellin line. It does not exclude arbitrary homogeneous
source-kernel additions, identify another supplied module with that
line, or estimate this residue.

There is a necessary directional qualification for other affine
objects. In the root regularization \(AR_N=b_N\), the earlier
central transformation acts as
\[
 (R_N,1)\longmapsto(cR_N+(c-1)p_N,1),
\]
rather than multiplying the augmented vector by \(c\).
Its change lies in the homogeneous source-kernel.
A nonzero observable symbol of that augmented basepoint alone
does not remove such an affine change. The Mellin argument above
works because the tested comparison is a central scalar multiple
of the SAME actual scalar \(Z_N\), whose observable quotient is
then multiplied by that scalar.

