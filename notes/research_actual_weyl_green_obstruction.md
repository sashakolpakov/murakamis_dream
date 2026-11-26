# The actual Weyl reflection is not the adjoint Green source

Research deduction, 6 November 2026.

The exact cyclic Green identity distinguishes two different dual
problems for the actual normal meridian operator. Every homogeneous
left zero mode annihilates its first normal source. The complete
evaluation instead requires an inhomogeneous dual Green column.
This distinction persists for the primitive minimal operator of the
actual unknot, with the full ordinary pointing and the required
special-fiber rank. It is therefore not caused by an extraneous
annihilator factor or a manufactured source.

## 1. The whole kernel makes the unbordered determinant identically zero

Use the original conventions of
[actual Weyl descent](actual_weyl_descent.md), Section 4:
\[
 Q=e^{2\pi i/N},\qquad U=Y^N,\qquad
 B=\sum_{j=0}^d b_j(q,Y)T^j,\qquad Tf(Y)=f(QY).
 \tag{1}
\]
All cleared coefficients and the normal lattice are retained.
At each level where the recorded operator identity holds, take
the marked roots \(Y_r(U)=Q^rU^{1/N}\). Let \(B_N(U)\) be
the cyclic matrix and let
\[
 v_N(U)_r=(Y_r(U)-1)F_N(Y_r(U)),\qquad
 B_N(U)v_N(U)=0.
 \tag{2}
\]
The actual ordinary anchor gives
\(v_N(1)_1=Q-1\ne0\). Thus (2) has a nonzero analytic kernel
vector on a neighborhood of \(U=1\), without a rank hypothesis.
Consequently
\[
 \det B_N(U)\equiv0.
 \tag{3}
\]
In particular every meridian-normal derivative of this determinant
vanishes. It is not a simple eigenvalue-crossing determinant from
which the complete value could be recovered by differentiating once.

Write \(B_N(U)=B_0+(U-1)B_1+\cdots\) and
\(v_N(U)=v_0+(U-1)v_1+\cdots\). The exact first normal equation is
\[
 B_0v_1=-s_N,\qquad s_N=B_1v_0,
 \qquad K_N=N e_0^*v_1.
 \tag{4}
\]
Every bilinear left zero mode \(\ell B_0=0\) therefore satisfies
\[
                              \ell s_N=0.
 \tag{5}
\]
The ordinary data determine \(v_0\), but their first normal
forcing is orthogonal to the entire adjoint nullspace. This is an
exact solvability identity for the actual source, not an estimate
that permits replacing its complete observation by a zero-mode
overlap.

Equation (3) concerns the unbordered cyclic determinant only.
The pointed cofactor ratios in
[root-orbit pointing](root_orbit_pointing.md), Sections 4--5,
and the bordered first lifting equation in
[the peripheral normal period](peripheral_normal_period.md),
Section 5, retain additional source data and are not ruled out.

## 2. The cyclic Green identity retains an inhomogeneous dual equation

For the bilinear orbit pairing \(\sum_{r=0}^{N-1}g_rf_r\),
the exact transpose operator is
\[
 B^{\mathsf t}=\sum_{j=0}^d T^{-j}b_j(q,Y).
 \tag{6}
\]
The order in (6) is literal: first multiply, then shift backwards.
For any two orbit functions, put
\[
 \mathcal C_B(f,g)=
 \sum_{j=1}^d\sum_{a=0}^{j-1}
           T^a\!\left(f\,T^{-j}(b_jg)\right).
 \tag{7}
\]
The finite telescoping identity gives
\[
           gBf-fB^{\mathsf t}g=(T-1)\mathcal C_B(f,g).
 \tag{8}
\]
Indeed the \(j\)-th inner sum becomes
\((T^j-1)(fT^{-j}(b_jg))\), whose two terms are exactly the
corresponding terms on the left. Summing around the actual cyclic
orbit kills \(T-1\); no endpoint or quotient residual is dropped.
The Hermitian version follows by conjugating the dual vector.

The Weyl identity \(BJ=J'B\) is a different identity: it does
not identify (6) with \(B\), or turn its homogeneous right
kernel into the dual point source below.

Retain the rank hypothesis of the actual inverse formula: it is
enough that \(B_-:E_-\to E'_-\) be injective, or more generally
that \(e_0^*\) annihilate its kernel. Since the actual source
belongs to its image, the least-norm dual solution
\[
 g_N=(B_-^+)^*e_0,\qquad B_-^*g_N=e_0
 \tag{9}
\]
exists under precisely that condition. The Green identity applied
to (4) then gives
\[
                         K_N=-N g_N^*s_N.
 \tag{10}
\]
A homogeneous dual vector cannot replace \(g_N\): it satisfies
the zero right side in (9) and gives zero in (5). Constructing or
estimating this inhomogeneous dual solution remains a legitimate
route. Neither (8) nor Weyl reciprocity proves a positive or
nonzero value for its pairing in (10).

## 3. An exact test using the primitive minimal unknot operator

For the actual zero-framed unknot, \(F_N(Y)=1\) at every level,
all ordinary colors equal one, and the normal state is \(v(Y)=Y-1\).
Its primitive minimal operator is
\[
               B=(Y-1)T-(QY-1).
 \tag{11}
\]
It annihilates \(Y-1\) identically. Its two coefficients are
coprime over the Laurent ring in \(q,Y\), and no nonzero
order-zero rational operator annihilates this state. Thus the
order-one operator is genuinely minimal. It is also the actual
operator used in the
[initial-rank example](torsion_initial_rank.md), Section 6;
no extra left factor is used here.

Its original Weyl intertwiners are
\[
                   J=-YR,\qquad J'=-QY^2TR,\qquad
                   Rf(Y)=f(Y^{-1}),\qquad BJ=J'B.
 \tag{12}
\]
Direct multiplication proves (12), with both intertwiners unitary
involutions on the root orbit. The special matrix equation is
\[
 (B_0 f)_r=(Q^r-1)f_{r+1}-(Q^{r+1}-1)f_r,
                     \qquad r\pmod N.
 \tag{13}
\]
The row \(r=0\) forces \(f_0=0\). The rows
\(1\le r\le N-2\) then fix the ratios
\(f_r/(Q^r-1)\), and the last row adds no constraint. Hence
\[
 \begin{split}
 \ker B_0&=\mathbb C v_0,\qquad (v_0)_r=Q^r-1,
                         \qquad \operatorname{rank}B_0=N-1,\\
 \ker B_0^{\mathsf t}&=\mathbb C\ell^{\mathsf t},\qquad
                    \ell=e_0^{\mathsf t}-Qe_{N-1}^{\mathsf t}.
 \end{split}
 \tag{14}
\]
The left-kernel formula is checked directly from (13).
Moreover \(Jv_0=v_0\) and \(Je_0=-e_0\), so the negative
restriction is injective. Thus this example satisfies the rank
hypothesis of (9)--(10), rather than evading it.

The left kernel is not the Weyl image or conjugate of the right
kernel. In particular its zeroth coordinate is nonzero whereas
that of \(v_0\) is zero. No invertible diagonal metric identifies
these kernel lines. For \(N\ge4\), their support sizes are two
and \(N-1\), so even composing with root clock, shift, and Weyl
monomial transformations cannot identify them. These are exact
statements about this primitive actual operator; they do not
exclude a separately constructed non-diagonal duality.

The marked derivative is completely explicit. With
\(\mathbf y=(Q^r)_r\),
\[
 s_N=B_1v_0=\frac{Q-1}{N}\mathbf y,\qquad
 v_1=\frac1N\mathbf y,\qquad
 \ell s_N=0,\qquad K_N=N(v_1)_0=1.
 \tag{15}
\]
Thus the homogeneous dual coupling vanishes while the actual
complete period is nonzero. No source scalar has been changed.

For comparison, an actual inhomogeneous dual row is simply
\[
             \widetilde g_N^*=\frac{e_0^*}{1-Q},\qquad
             \widetilde g_N^*B_0=e_0^*,\qquad
                         -N \widetilde g_N^*s_N=1.
 \tag{16}
\]
Projecting this row to the negative range sector gives the same
pairing and the explicit row
\((e_0^*+Qe_{N-1}^*)/[2(1-Q)]\). Both choices retain the
original point source; their norms are only polynomial in \(N\).
This calculation shows exactly which dual equation succeeds in
the example, rather than asserting that no useful Green estimate
can exist.

## 4. Consequence for the source problem

Actual minimality, ordinary-color pointing, and Weyl reciprocity
do not identify the right zero mode with an adjoint Green vector.
The unbordered cyclic determinant has no meridian derivative to
exploit, and homogeneous left modes annihilate the forcing by
(5). The next quantitative object is therefore the marked
inhomogeneous dual column (9), or an equivalent bordered normal
period that preserves its source and complete evaluation.

Nothing here rules out a further source-specific identity for
that column, a useful non-diagonal reciprocal pairing, or a
calibrated lower bound for (10). No operator is replaced by a
left multiple, no nonunit factor is removed, and no numerical
source or rank computation is used.
