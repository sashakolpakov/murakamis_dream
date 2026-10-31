# The actual Mellin source has a rigid selected quantum-normal line

Research theorem, 27 October 2026. For every knot, the actual bounded
Fourier--Mellin source gives an observable monodromy covector which
detects its selected rational root section. Its first quantum-normal
symbol is therefore nonzero without a simple-root or semisimplicity
hypothesis. The actual coefficientwise whole-Q lift makes that
selected section horizontal for the rational kernel-to-cokernel
normal operator. Together these facts exclude nonconstant central
scalar multipliers compatible with the same whole operator.

The retained scalar is exactly the Kashaev residue at infinity. This
does not estimate that residue, identify its regulator norm, or
transfer rigidity to a different meridian source object.

## 1. The specified actual source and its admissible roots

Retain the [actual finite-color construction](fourier_mellin_actual_source.md):

\[
 Z(Q,X)=\sum_{n\ge n_0}C_n(Q)X^n,\qquad
 A(Q,X,S)Z=B(Q,X),\qquad Sf(X)=f(QX).                 \tag{1.1}
\]

The coefficients \(C_n(Q)\) are the original reduced color periods,
Laurent polynomial in \(Q\), with \(C_n(1)=1\). The specified fixed
starting color makes \(B\) a nonzero fixed Laurent polynomial in
\(X\), with rational Q-coefficients, built from finitely many actual
colors. Its lowest coefficient is explicitly nonzero. The formal
lattice \(X^{n_0}\mathbb Q(Q)[[X]]\) and (1.1) specify the actual
series uniquely. No generic rationality of \(Z\) is assumed.

Apply any fixed left S-power needed to make A's shift support
\(0,\ldots,r\), and apply the same shift to B. Write

\[
 A=\sum_{j=0}^{r}a_jS^j,\qquad a_0a_r\ne0.             \tag{1.2}
\]

Order zero is allowed. For all sufficiently large N, at
\(\zeta=\exp(2\pi i/N)\), all coefficients required below are regular
over \(E=\mathbb C(X)\), and \(a_0,a_r,B\) remain nonzero in E.
Indeed each possible failure says that one of finitely many fixed
nonzero rational functions of Q vanishes or has a pole. Thus only
finitely many Q-values, hence finitely many levels, are excluded.
An X-dependent zero or pole is retained as an element of E; it is
not removed by choosing a numerical X-point.

By the independently proved
[actual all-color root periodicity](cyclotomic_mellin_residue.md),
the specialization \(Z_N=Z(\zeta,X)\) is rational. Explicitly,

\[
 Z_N=\frac{\sum_{j=1}^{N-1}C_j(\zeta)X^j+K_NX^N}{1-X^N}
             -\sum_{j=1}^{n_0-1}C_j(\zeta)X^j.          \tag{1.3}
\]

This is equality with the same formal expansion at zero. It holds
even if \(K_N=0\). The rational source equation is still
\(A_NZ_N=B_N\).

## 2. An observable source quotient detects the selected symbol

Use the canonical homogeneous operator attached to this source:

\[
 \widehat A=(S-\sigma_Q(B)/B)A,\qquad
 \sigma_Q f(X)=f(QX).                                 \tag{2.1}
\]

It has order \(d=r+1\), with both endpoint coefficients nonzero.
Let C be its forward solution companion, so
\(\sigma_Qv=Cv\) for \(v=J_df=(f,Sf,\ldots,S^rf)^t\), and put
\(T=C^{-1}\sigma_Q\). There is a literal observable row

\[
 \ell=\frac1B(a_0,\ldots,a_r),\qquad
 \ell J_df=Af/B.                                      \tag{2.2}
\]

The coefficient identity (2.1), with no chosen solution, implies

\[
 \sigma_Q(\ell)C=\ell,\qquad
 \ell T=\sigma_Q\circ\ell.                            \tag{2.3}
\]

For example, the first equality says that the source quotient of
any homogeneous solution of (2.1) is shift-invariant; its coefficient
of the highest jet is precisely the companion relation. The second
follows by right multiplication by \(C^{-1}\).

At the root let \(T_0=T|_{Q=\zeta}\), \(H_0=T_0^N\), and
\(v_0=J_dZ_N\in E^d\). Since \(\sigma_\zeta^N=1\), (2.3) gives

\[
 T_0v_0=v_0,\qquad \ell_0H_0=\ell_0,\qquad
 \ell_0v_0=1.                                        \tag{2.4}
\]

Set \(L_0=H_0-I\), \(K=\ker L_0\),
\(\mathcal C=\operatorname{coker}L_0\), and let
\(\iota:K\to\mathcal C\) be inclusion followed by quotient.
The row \(\ell_0\) kills \(\operatorname{im}L_0\). Consequently

\[
                 \ell_0\iota(v_0)=1,
                 \qquad \iota(v_0)\ne0.               \tag{2.5}
\]

This is a dual source certificate, not a characteristic-polynomial
guess. No assertion about other eigenvalue-one Jordan blocks is
needed. In fact \(p=v_0\ell_0\) is a root difference-equivariant
projection onto \(Ev_0\): (2.3)--(2.4) give \(pT_0=T_0p\) and
\(p^2=p\). Thus this selected line is a direct summand of the root
module even if the complementary module is nonsemisimple.

The quotient is observable in the original scalar state and its
shifts. It is not an unused unit line adjoined to force (2.5).
For another supplied original annihilator, including a left multiple,
one may rebuild its finite-color source B and apply the same proof.
One may not erase that source and apply the conclusion to an
arbitrary homogeneous left multiple.

For order zero, (1.1) itself already determines a rational function
\(Z=B/a_0\) generically. The same rank-one homogenization and
observable row remain valid for this selected normal statement;
they assert no geometric block or additional geometric order.

## 3. The actual formal lift kills the rational normal obstruction

Put \(Q=\zeta(1+\epsilon)\), \(D_X=X\partial_X\), and retain every
moving argument in the specified whole companion. As in the
[first quantum-normal construction](first_quantum_normal_connection.md),

\[
 \begin{split}
 T(Q)^N-I&=L_0+\epsilon L_1+O(\epsilon^2),\\
 L_1&=H_1+NH_0D_X,\\
 D_N:K\longrightarrow\mathcal C,\qquad
 D_N(v)&=[L_1v]/N^2.                                  \tag{3.1}
 \end{split}
\]

Every \(C_n\) is regular at the root. Coefficientwise differentiation
therefore gives an actual first lift
\(Z=Z_N+\epsilon Z_1+O(\epsilon^2)\) with
\(Z_1\in F=\mathbb C((X))\) and the same fixed lower X-bound.
No convergence in X, uniform Q-radius, or bound on color derivatives
is needed. Rational coefficients of the companion and of \(B^{-1}\)
expand in \(E[[\epsilon]]\subset F[[\epsilon]]\); the orders of
their X-poles may depend on the epsilon coefficient.

The actual formal whole solution of (2.1) has jet
\(v=v_0+\epsilon v_1+O(\epsilon^2)\), \(v_1\in F^d\), satisfying

\[
                 L_0v_1+L_1v_0=0.                    \tag{3.2}
\]

Both \(L_0\) and \(L_1v_0\) are over E. For a matrix over any field
E and any extension F/E,

\[
 \operatorname{im}(L_0:F^d\to F^d)\cap E^d
                  =\operatorname{im}(L_0:E^d\to E^d). \tag{3.3}
\]

To prove it, row-reduce over E. The zero rows and the corresponding
augmented consistency conditions stay zero or nonzero under field
extension. Thus (3.2) implies that its right-hand side lies in the
rational image, and

\[
                       D_N(v_0)=0.                    \tag{3.4}
\]

This proves vanishing of a rational obstruction class. It does not
assert that the actual \(Z_1\), actual jet \(v_1\), or normal cut
functional is rational, and does not replace them by a rational lift.

The usual cyclic descent applies to K, \(\mathcal C\), and this
normal map. Its constant field is \(\mathbb C(U)\), \(U=X^N\), and
its symbol on that field is \(U\partial_U\,\iota\).

## 4. Whole first-normal compatibility removes central scalars

Let \(c(U)\in\mathbb C(U)\), or more generally \(\mathbb C((U))\).
Suppose \(c(U)v_0\) has a first-order lift for the SAME specified
whole homogeneous companion (2.1). Then

\[
 0=D_N(cv_0)=cD_N(v_0)+Uc'(U)\iota(v_0)
                       =Uc'(U)\iota(v_0).             \tag{4.1}
\]

After scalar extension if necessary, applying the source covector
(2.5) gives \(Uc'=0\). In characteristic zero, c is constant.
The actual source value one or a fixed nonzero color-prefix anchor
then fixes that constant to one. For all sufficiently large N a
fixed anchor \(C_{n_0}(\zeta)\) is nonzero, since the fixed Laurent
polynomial \(C_{n_0}\) is nonzero and has finitely many roots.

There is a direct scalar check which avoids choosing a rational
normal lift. For any compatible whole first-order solution W set
\(h=AW/B\). Equation (2.1) says \(\sigma_Qh=h\) modulo
\(\epsilon^2\). If \(W_0=c(U)Z_N\), then \(h_0=c(U)\).
Iterating N times yields

\[
 (\sigma_Q^N-I)h=\epsilon N D_Xc(U)+O(\epsilon^2)
               =\epsilon N^2Uc'(U)+O(\epsilon^2)=0.   \tag{4.2}
\]

Thus this rigidity uses only the actual source quotient and the
first whole quantum jet. It excludes a central scalar change of
the selected section, not arbitrary source-kernel additions.

## 5. Actual presentations distinguish the selected criterion

The actual unknot has \(C_n(Q)=1\). With start one,
\(Z=X/(1-X)\), \(g=X^{-1}-1\), its Mellin source is \(gZ=1\).
The canonical homogeneous operator is \((S-1)g\). After the exact
gauge \(h=gf\), its selected solution is \(h=1\), with visible
source row one and nonzero selected symbol.

The equally actual annihilator \((S-1)^2g\) has, in h coordinates,
forward companion

\[
 C=\begin{pmatrix}0&1\\-1&2\end{pmatrix}=I+J,
 \qquad J^2=0,\quad J\ne0.
\]

At a level-N root, \(H_0=C^{-N}=I-NJ\). Its actual selected vector
\((1,1)^t\) lies in both \(\ker(H_0-I)\) and
\(\operatorname{im}(H_0-I)\), so its selected symbol vanishes.
Indeed \((\sigma_Q-1)^2c(X^N)=O(\epsilon^2)\) for EVERY c.
The unnecessary left factor destroys the first-normal scalar test
if the observable source is forgotten. This is a diagnostic on the
actual unknot, rather than a replacement knot state.

Conversely, simplicity is stronger than needed. Still for the actual
unknot, use the supplied original operator
\((Y-1)(T-1)\) and start two. Its exact Mellin pair is

\[
 A=(S-1)g,\quad Z=X^2/(1-X),\quad B=(Q-1)X.
\]

Canonical homogenization is \((S-Q)(S-1)g\). In h coordinates its
companion has distinct eigenvalues 1 and Q. At every primitive
level-N root its monodromy is \(I_2\), so the eigenvalue one is
double and semisimple, while the observable selected symbol is
nonzero. A simple norm root is not an all-knot premise of Sections
2--4, even for canonically rebuilt nonminimal source objects.

## 6. A genuine affine nonresonance criterion and an actual input

For a supplied rational affine equation
\(\sigma v=C_Av+c\), its augmented monodromy has the form

\[
               H_{\mathrm{aug}}=\begin{pmatrix}H_A&s\\0&1\end{pmatrix}.
                                                               \tag{6.1}
\]

If \(I-H_A\) is invertible, its characteristic polynomial satisfies

\[
 \Delta_{\mathrm{aug}}(t)=(t-1)\det(tI-H_A),\qquad
 \Delta'_{\mathrm{aug}}(1)=\det(I-H_A)\ne0.                 \tag{6.2}
\]

Thus it has a simple eigenvalue one. Translation by the unique
rational particular solution block-diagonalizes (6.1). This uses
a genuine supplied source equation; it cannot be inferred merely
from an arbitrary homogeneous root annihilator.

The [actual quantum extremal-coefficient criterion](affine_quantum_a_period.md#4-a-simple-algebraic-criterion-for-nonresonance)
proves \(I-H_A\) invertible whenever the homogeneous scalar operator
has a unique strictly least Y-order coefficient (or unique greatest
degree at infinity). Its proof already includes cyclic descent;
no growing determinant or classical-symbol inference is needed.

There is a concrete actual input here. The independently proved
[whole figure-eight identity](figure_eight_whole_source_identity.md)
and its [explicit root source operator](peripheral_normal_period.md#9-independent-operator-and-actual-state-calibration)
give, at every level N,

\[
 \begin{split}
 (c_-S^{-1}+c_0+c_+S)F_N&=D(Y)(3-U-U^{-1}),\\
 U&=Y^N,\\
 D&=Y(Y+1)(Q-Y^2)(QY^2-1),\\
 g_0&=Q^2Y^2-QY^4+QY^3+QY-Q+Y^2,\\
 c_-&=Y^2(Q-Y)(QY^2-1),\\
 c_0&=-(Y-1)^2(Y+1)g_0,\\
 c_+&=Y^2(QY-1)(Q-Y^2).
 \end{split}                                                     \tag{6.3}
\]

Here \(c_0\) alone has Y-order zero, with coefficient Q; both
neighbors have order two. This persists at EVERY primitive root,
including level two. Hence the homogeneous order-two monodromy has
no eigenvalue one. The genuine rank-three source homogenization
has a simple eigenvalue one for every N over \(\mathbb C(Y)\).
Its selected observable source is \(3-U-U^{-1}\ne0\); one may
normalize the covector by that central factor generically.

This is an actual root-module statement. The known off-root finite
cyclotomic calibration is not thereby the original auxiliary
finite-Verma Q-lift. No assertion identifying those whole normal
connections is made, and no intrinsic norm is identified with the
classical geometric A-polynomial. At a special U-value where the
source factor vanishes, its marked lattice must be retained instead
of dividing by it.

## 7. The original period and the remaining comparison

For the SAME section (1.3),

\[
                 K_N=\operatorname{Res}_{X=\infty}
                                Z_N(X)\,dX/X.         \tag{7.1}
\]

The full ideal ADO factor remains \(\eta_NK_N/N\), with its
specified parity and meridian germ. Nothing in the normal argument
replaces that factor by a number before cancellation or estimates
the exponential growth of (7.1).

The central coordinate in Sections 3--4 is X^N in the Mellin
polarization. A comparison to an original meridian profile in Y^N
requires an actual source/co-source map. In particular, for the
earlier regularized equation \(\mathcal A R=b_N\), a meridian
change of the original F acts as

\[
 (R,1)\longmapsto(cR+(c-1)p,1),
\]

rather than multiplying the full augmented section by c. It is a
homogeneous source-kernel addition, so the scalar theorem above
does not remove it automatically. The selected regulator norm,
geometric source comparison, and asymptotic residue bound remain
additional problems.

The stronger [cyclotomic jet reconstruction](mellin_cyclotomic_jet_uniqueness.md)
also handles arbitrary homogeneous source-kernel additions in
this canonical Mellin realization. It retains the exact pole
lattice and a bounded number of quantum levels of the same
inhomogeneous source equation. Under those additional conditions
the entire rational root function is unique, not just its
selected scalar line. This remains a uniqueness theorem rather
than a regulator or residue-growth estimate.

[Independent proof audit and presentation certificates](source_symbol_duality_and_presentation.md).
[Exact diagnostics](../experiments/audit_actual_mellin_normal_source_rigidity.py).
[Results](../experiments/actual_mellin_normal_source_rigidity_results.json).
