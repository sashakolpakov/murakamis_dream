# Exact source-retaining tensor closure for ordinary endpoint products

Private written proof, 16 November 2026.

The ordinary product of a fixed number of original endpoint kernels
has an exact rational matrix recurrence of bounded rank, including
its endpoint forcing. Its differentiated recurrence retains the
first spectral normals. A finite elimination gives a polynomial
operator relation of bounded order and degree, with a nonzero
coefficient vector at every fixed specialization. Original turns
transport this relation without changing factor order.

This is an algebraic closure theorem, not a stability or source-rate
estimate. The tensor-product and restriction-of-scalars arguments are
elementary elimination methods; the point here is their application
to the actual forced kernel and its full quotient.

## 1. Original source and the augmented three-state recurrence

Use the original notation
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},\quad c_0=q+q^{-1},
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 k_i(Z)=K_N(w_i,Z).
 \tag{1}
\]
Here \(T_N\) is the usual Chebyshev polynomial, \(T\) below is the
original physical turn, and \(K_N\) is the original Newton kernel
from the pinned source. Write \(s_y=2\sin(\pi y/N)\) and
\(c_j=2\cos((2j+1)\pi/N)\). The \(w_i\) are arbitrary fixed
complex numbers. In particular they
may be the microscopic parameters \(2\cosh(\alpha_i/N)\).
Multiplication below is ordinary multiplication, followed by
canonical reduction when an element of \(\mathcal A_N\) is intended.
It is not the transported product \(f\star g=T(Tf\,Tg)\).

Let \(C\) be spectral multiplication, \(J=TCT\), and
\[
 V_n=\kappa^nTR^{-n}T,\qquad D_n=V_nCV_{-n},\qquad n\in\mathbb Z,
 \tag{2}
\]
with exactly the original crossing and carrier. The pinned source
proves \(V_nJ=JV_n\).

For a complex index \(x\), set
\[
 v=e^{(2x+1)\pi i/N},\quad z(v)=v+v^{-1}=c(x),\qquad
 (Ef)(v)=f(Qv).
\]
The two original difference coefficients have the rational forms
\[
 a(v)=-\frac{(qv-1)^3}{q(v^2-1)(qv+1)},\qquad
 b(v)=-\frac{(v-q)^3}{q(v^2-1)(v+q)}.
 \tag{3}
\]
Indeed these are respectively
\(s_{x+1}^4/(s_{2x+1}s_{2x+2})\) and
\(s_x^4/(s_{2x}s_{2x+1})\). Thus
\[
 \mathcal L=(c_0+a+b)-aE-bE^{-1}.
 \tag{4}
\]
On ordinary spectral polynomials \(\mathcal L\) is polynomial,
descends to \(J\), and satisfies
\(\mathcal L(P_Nh)=P_N\mathcal Lh\).

The full ordinary source identities, before quotient reduction, are
\[
 (w_i-\mathcal L)k_i=\frac{\eta P_N(w_i)}{N^2}e_D,\qquad
 e_D(Z)=\frac{\eta P_N(Z)}{N^2(Z-c_0)}.
 \tag{5}
\]
The second quotient is an ordinary polynomial. Put
\[
 p(v)=P_N(z(v)),\qquad \beta_i=\frac{P_N(w_i)}{N^4}.
\]
Crucially \(p(Qv)=p(v)\). Solving (5) forward gives the exact
rational identity
\[
 y_i(Qv)=M_i(v)y_i(v),\qquad
 y_i(v)=
 \begin{pmatrix}k_i(z(v))\\ k_i(z(Q^{-1}v))\\p(v)\end{pmatrix},
\]
\[
 M_i(v)=
 \begin{pmatrix}
 (c_0+a+b-w_i)/a&-b/a&\beta_i/[a(z-c_0)]\\
 1&0&0\\0&0&1
 \end{pmatrix}.
 \tag{6}
\]
Its determinant is \(b/a\), a nonzero rational function for every
\(N\ge2\). Consequently \(M_i^{-1}\) exists over \(\mathbb C(v)\).
No inverse at an individual singular physical row is asserted.

The factor \(p/(z-c_0)\) in (6) must be retained as a rational
function with its prescribed removable continuation. Substituting
\(p=0\) at the physical nodes before this continuation would erase
the original endpoint normal source.

## 2. Exact tensor closure, normals, and frozen matrix roots

Fix \(r\ge1\), put \(d=3^r\), and form
\[
 Y(v)=y_1(v)\otimes\cdots\otimes y_r(v),\qquad
 M(v)=M_1(v)\otimes\cdots\otimes M_r(v).
\]
Then
\[
                         Y(Qv)=M(v)Y(v).
 \tag{7}
\]
The component selected by
\(\ell_0=(1,0,0)^{\otimes r}\) is exactly the ordinary product
\[
                         F(Z)=\prod_{i=1}^r k_i(Z).
 \tag{8}
\]
All mixed-difference channels are present in (7). Channels with
one or more third coordinates contain the corresponding powers
of the same \(p\); they have not been replaced by independent
sources or dropped.

Differentiate with respect to the original index \(x\), so
\(\partial_x=(2\pi i/N)v\partial_v\). With a dot denoting this
derivative, the exact prolonged system is
\[
 \begin{pmatrix}Y\\\dot Y\end{pmatrix}(x+1)
 =
 \begin{pmatrix}M&0\\\dot M&M\end{pmatrix}(x)
 \begin{pmatrix}Y\\\dot Y\end{pmatrix}(x).
 \tag{9}
\]
Its rank is \(2\cdot3^r\). The selected derivative is
\[
                         \ell_0\dot Y(x)=c'(x)F'(c(x)).
 \tag{10}
\]
Thus on regular double-node charts (9) contains the literal
product-rule spectral normal. At the odd simple node only the
value is required. At a singular row one retains the rational
identity and its removable limits; (9) does not supply a
division-free numerical propagation through that row. The
polynomial identities below are valid in the entire quotient,
at both parities and also at \(N=2\).
The tensor identity is holomorphic in every \(w_i\); any fixed
collection of exterior parameter derivatives follows by
differentiating (7) and retaining all coefficient derivatives.
This assertion uses the tensor system, not a choice of scalar
elimination coefficients.

For clarity, one can compute the eigenvalues of the matrix in
(7) with its coefficients frozen at a regular \(v\). Let
\[
 u_i=(c_0+a+b-w_i)/a,\qquad t=b/a,
 \qquad \lambda_{i,\pm}^2-u_i\lambda_{i,\pm}+t=0.
 \tag{11}
\]
Here the notation means that \(\lambda_{i,+},\lambda_{i,-}\)
are the two roots of that quadratic, counted with multiplicity.
The eigenvalues of \(M_i\) are these two roots and \(1\).
The eigenvalues of \(M\), with algebraic multiplicity, are all
\[
 \prod_{i=1}^r\lambda_{i,\epsilon_i},\qquad
 \epsilon_i\in\{+,-,0\},\quad\lambda_{i,0}=1.
 \tag{12}
\]
Those of the prolonged matrix are repeated twice. This follows
by triangularizing each finite matrix; no distinct-root
assumption is needed. The all-\(+/-\) choices are the homogeneous
microscopic tensor roots. The other choices are the retained
source channels. Formula (12) is a frozen-matrix statement,
not an asymptotic selection rule, a diagonalizability assertion,
or a characteristic theorem for an eliminated scalar equation.

## 3. A bounded-order scalar operator with specialization retained

The following elimination is at the actual fixed values of
\(N,w_1,\ldots,w_r\). It does not specialize a single generic
minor and assume that minor remains nonzero.

**Theorem.** Put \(m=2\cdot3^r\). There is a constant \(B_r<\infty\),
depending only on \(r\), and polynomials \(A_k(Z)\), \(0\le k\le m\),
not all zero, such that
\[
 \deg A_k\le B_r,\qquad
 \sum_{k=0}^m A_k(Z)\mathcal L^k F(Z)=0
                         \quad\hbox{as an ordinary polynomial}.
 \tag{13}
\]
Consequently, for \(P_r=\operatorname{can}F\),
\[
 \mathscr A(C,J)P_r=0,\qquad
 \mathscr A(C,J)=\sum_{k=0}^m A_k(C)J^k.
 \tag{14}
\]
The coefficient vector is nonzero at every fixed specialization.
No bounds on its size, on a leading coefficient away from zero,
or on a companion-matrix inverse are included.

### Proof and degree bookkeeping

For a rational row \(\ell(v)\) of length \(d\), define
\[
 \begin{split}
 \mathfrak L\ell(v)={}&(c_0+a(v)+b(v))\ell(v)\\
 &-a(v)\ell(Qv)M(v)
 -b(v)\ell(Q^{-1}v)M(Q^{-1}v)^{-1}.
 \end{split}
 \tag{15}
\]
By (7), \(\mathcal L(\ell Y)=(\mathfrak L\ell)Y\).
Set \(\ell_{k+1}=\mathfrak L\ell_k\). Then, identically,
\[
                         \mathcal L^kF=\ell_kY.
 \tag{16}
\]

The extension \(\mathbb C(v)/\mathbb C(z)\), \(z=v+v^{-1}\),
has degree two with basis \(1,v\). Split each entry of \(\ell_k\)
uniquely as \(A(z)+vB(z)\). This gives a row \(R_k\) of length
\(2d=m\) over \(\mathbb C(z)\). There are \(m+1\) such rows,
so they are linearly dependent over that field.

Here is an explicit bound showing that the dependence has
degree independent of \(N\). Say a rational row has height at
most \(H\) if it has one polynomial denominator of degree at
most \(H\), and all numerator degrees are at most \(H\).
All quantities here are rational functions of \(v\); the
parameters are constants for this bookkeeping.

The entries of each \(M_i\) and \(M_i^{-1}\) admit numerator
and denominator degrees at most \(20\), directly from (3),(6).
Tensoring adds these degrees. Taking a product of the finitely
many denominators, including \(a,b,c_0+a+b\), shows that the
three matrix coefficients in (15) have a common denominator
and numerators of degree at most
\[
                         D_r=200r\,9^r.
 \tag{17}
\]
This deliberately loose bound also covers all their shifts.
If \(\ell_k\) has height \(H_k\), multiply its three shifted
denominators and this common matrix denominator. It gives
\[
 H_0=0,\qquad H_{k+1}\le3H_k+D_r,\qquad
 H_k\le D_r3^m\quad(0\le k\le m).
 \tag{18}
\]
Cancellation or a vanishing numerator can only improve the bound.

To restrict scalars, write an entry as \(U(v)/W(v)\) using the
common row denominator. Multiply numerator and denominator by
\(W(v^{-1})\). The denominator is an invariant Laurent
polynomial and hence a polynomial in \(z\). Every numerator
Laurent polynomial is uniquely \(A(z)+vB(z)\), by
\(v^2-zv+1=0\). A safe bound for the resulting row denominator
and all its polynomial numerators is
\[
                         B=2D_r3^m+2.
 \tag{19}
\]
Thus each \(R_k\) can be multiplied by a nonzero polynomial
\(h_k(z)\), of degree at most \(B\), to obtain a polynomial
row \(\widetilde R_k\) whose entries have degree at most \(B\).

Let \(s\le m\) be the actual rank of these rows over
\(\mathbb C(z)\). Choose \(s\) independent rows and \(s\)
columns giving a nonzero minor \(\Delta(z)\). Choose any
additional row among the \(m+1\) rows. Cramer's cofactors express
that row in the span of the selected rows; the relation holds
in every column because the full row rank is \(s\).
Its coefficient at the additional row is \(\Delta\ne0\).
The cofactor degrees are at most \(sB\). Replacing each
\(\widetilde R_k\) by \(h_kR_k\) gives a relation with
\[
                         \deg A_k\le(s+1)B\le(m+1)B.
 \tag{20}
\]
The additional coefficient is \(\Delta h_k\ne0\). Take
\(B_r=(m+1)(2D_r3^m+2)\).

The corresponding relation among the \(\ell_k\), applied to
\(Y\), proves (13) as a rational identity. Its left side is an
ordinary polynomial because \(\mathcal L\) preserves ordinary
polynomials. It therefore vanishes identically, including all
apparent singular points. Since \(\mathcal L\) preserves the
ideal \((P_N)\), reduction gives (14).

This also describes a finite rank/minor stratification:
there are only finitely many choices of \(s\), rows and
columns. At each fixed specialization one chooses a nonzero
minor for its actual rank. A generic choice is not asserted
to work on another stratum. The formulas need not form a
single holomorphic family through a rank change.

The expression in (14) is a nonzero formal normal-ordered
polynomial. Indeed its highest nonzero \(J\)-power has, in the
formal difference algebra, highest shift coefficient equal to
its nonzero \(A_k(z)\) times
\((-1)^k\prod_{\ell=0}^{k-1}a(Q^\ell v)\).
This does not assert that the resulting endomorphism of every
finite-dimensional \(\mathcal A_N\) is nonzero. In particular,
finite-level identities and small levels can make an
annihilator impose fewer conditions. The theorem asserts a
nonzero coefficient relation, not an invertible propagation
equation. This completes the proof.

## 4. Original turns, full normals, and the indispensable source factor

The original conjugation rule from the pinned source gives
\[
 \boxed{\quad
 \sum_{k=0}^m A_k(D_n)J^k\,V_nP_r=0 .
 \quad}
 \tag{21}
\]
Order is literal: \(A_k(D_n)\) is on the left of \(J^k\).
For fixed \(r,n\), this is also a fixed-band Newton operator:
the source bounds the shifts of \(D_n\) by \([-|n|,1]\)
and those of \(J\) by \([-1,0]\), so (21) has shifts within
\[
                         [-B_r|n|-m,\ B_r].
 \tag{22}
\]
This counts bands only. It does not bound the inverse,
the actual solution, or any original closed trace.

Both (14) and (21) are identities in the original
nonsemisimple algebra. They include all double-root first
normals, the odd simple value, and \(N=2\). One may multiply
them by any original spectator and apply the original
Frobenius functional. Ordinary outside variables remain
ordinary variables; no quotient is imposed on them. On a
parameter neighborhood on which fixed scalar coefficient
formulas give the identity, one may also differentiate it,
retaining the derivatives of its coefficients. On a
lower-dimensional rank stratum this only asserts derivatives
tangent to that stratum. For unrestricted exterior derivatives
at rank changes, the original tensor identity remains available;
no derivative of a merely specialized relation is inferred.

The one-factor case explains why the source cannot be
discarded in a subsequent asymptotic analysis. Equations (5)
give the particularly short exact ordinary identity
\[
 (Z-c_0)(w-\mathcal L)K_N(w,Z)
                         =\frac{P_N(w)P_N(Z)}{N^4}.
 \tag{23}
\]
Therefore in the quotient, and then after the original turn,
\[
 (C-c_0)(w-J)K_N(w,\cdot)=0,
\]
\[
 \boxed{\quad
 (D_n-c_0)(w-J)V_nK_N(w,\cdot)=0.
 \quad}
 \tag{24}
\]
The exact stronger inhomogeneous equation is still
\[
 (w-J)V_nK_N(w,\cdot)
       =\frac{\eta P_N(w)\kappa^n}{N^2}\,T(R^{-n}).
 \tag{25}
\]
Clearing the source denominator produces the extra factor
\(D_n-c_0\); it does not eliminate the source channel.
Equation (24) alone does not recover the coefficient in
(25), the actual endpoint anchors, or a boundary current.
Likewise (21) may impose no condition where a left coefficient
vanishes. The homogeneous tensor roots in (12) therefore
cannot replace the source-retaining system, nor can a
bounded-order annihilator establish analytic stability.

## 5. Direct source and scope

The complete direct source was freshly read, with its hash and
all directly used implications checked:

* [Exact finite-band conjugation and branching forcing](research_unit_turn_finite_band_branching_operator.md),
  SHA256
  31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb.
  It supplies the original polynomial difference operator,
  ordinary endpoint forcing, quotient descent, full turn
  normalization, and ordered conjugation rule.

The tensor matrix, differentiated system, specialization-safe
elimination and degree bounds are proved above. General
annihilator and restriction-of-scalars methods already appear
elsewhere in this archive; no novelty of those methods is
claimed. This theorem retains the specific endpoint source
that an unforced product recurrence would omit.

Only written mathematics and text/hash reads were used.
No mathematical program, numerical experiment, test or build
was run. Adopted notes and public manuscripts are unchanged.
