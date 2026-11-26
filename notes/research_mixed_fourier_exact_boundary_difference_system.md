# Exact difference equations for the Fourier boundary function

Research theorem, 7 November 2026. The complete finite Fourier boundary
function satisfies two difference equations involving only its two
boundary variables. Their joint kernel in its original finite band is
one-dimensional. The coefficient normalization selects the original
finite sum, and the commuting symbols recover its previously derived
algebraic critical equations.

This is the Fourier counterpart of the
[marked terminal type-three system](research_mixed_terminal_three_marked_difference_system.md).
Here the second variable is the actual Fourier output; there is no
auxiliary index variable to eliminate before applying the equations
to that output. The result does not identify the variables with a
knot's peripheral eigenvalues or replace the original short-filling
trace by a boundary shift.

## 1. Finite source and boundary shifts

Fix an integer \(N\ge2\), and put
\[
 r=e^{-2\pi i/N},\qquad q=e^{\pi i/N},\qquad r^{1/2}=q^{-1},
 \qquad P_j=(r;r)_j.
 \tag{1}
\]
Only \(P_0,\ldots,P_{N-1}\) occur in denominators. Set
\[
 \begin{split}
 b_j(X)&=X^{-j}(rX;r)_j
            =\prod_{k=1}^j(X^{-1}-r^k),\\
 c_l(Y)&=Y^l\prod_{k=l+1}^{N-1}(1-Yr^k),\\
 a_{jl}&=\frac{P_{j+l}}{P_j^3P_l}\qquad(j+l<N),\\
 H_N(X,Y)&=\sum_{j+l<N}a_{jl}b_j(X)c_l(Y).
 \end{split}
 \tag{2}
\]
The function whose nonzero asymptotic was proved in the
[complete boundary theorem](research_mixed_fourier_right_cap_full_asymptotic.md)
is exactly
\[
 Z_N(a,y)=V_N^{\rm F}(y,e^{-2\pi ia})
     =\frac{e^{-\pi i(N-1)y}}N H_N(X,Y),
 \qquad X=e^{-2\pi ia},\quad Y=e^{2\pi iy}.
 \tag{3}
\]
Thus (2) removes a specified scalar and chirp for algebraic convenience;
(3) restores both. In particular the sign from shifting that chirp
will be retained below.

On Laurent polynomials define
\[
 (T_XF)(X,Y)=F(rX,Y),\qquad
 (T_YF)(X,Y)=F(X,r^{-1}Y),
 \tag{4}
\]
and ordered operators
\[
 \mathsf D=(1-rX)T_X+rX,
 \qquad \mathsf E=(1-Y/r)T_Y+Y.
 \tag{5}
\]
Multiplication by \(X,Y\) is an operator. Products act from right
to left. In particular \(\mathsf D,\mathsf E\) commute, but
\[
 \mathsf D X^{-1}=r^{-1}X^{-1}\mathsf D+(r-1),\qquad
 \mathsf E Y^{-1}=rY^{-1}\mathsf E+(1-r).
 \tag{6}
\]
Direct finite-product identities give
\[
 \mathsf D b_j=r^{-j}b_j,\qquad
 \mathsf E c_l=r^{-l}c_l,\qquad
 b_{j+1}=(X^{-1}-r^{j+1})b_j,
 \tag{7}
\]
and
\[
             (1-Yr^l)c_l=Yc_{l-1}\quad(1\le l<N).
 \tag{8}
\]
For example
\((1-Y/r)c_l(Y/r)=(r^{-l}-Y)c_l(Y)\), which proves
the second identity in (7) without dividing by a polynomial zero.

## 2. Two exact equations with bounded operator order

Define
\[
 \begin{split}
 \mathsf Q_1&=(\mathsf D-rX)\mathsf D
                       (\mathsf D\mathsf E-r)
                   -r^3X\mathsf E(\mathsf D-1)^3,\\
 \mathsf Q_2&=Y\mathsf E(\mathsf D\mathsf E-r)
                   -r^2\mathsf D(\mathsf E-Y)(\mathsf E-1).
 \end{split}
 \tag{9}
\]

**Theorem 1.** The full polynomial (2) satisfies
\[
                    \mathsf Q_1 H_N=\mathsf Q_2 H_N=0.
 \tag{10}
\]
These are identities for arbitrary \(X\ne0,Y\), not identities
only at the physical root-of-unity nodes. The number of shifts in
each operator is bounded independently of \(N\).

*Proof.* Extend \(a_{jl}\) by zero outside its triangle within the
square \(0\le j,l<N\). Its interior recurrences are
\[
 \begin{split}
 (1-r^j)^3a_{jl}&=(1-r^{j+l})a_{j-1,l},\qquad 1\le j<N,\\
 (1-r^l)a_{jl}&=(1-r^{j+l})a_{j,l-1},\qquad 1\le l<N.
 \end{split}
 \tag{11}
\]
They follow from the products in (2). At the first index beyond
the support triangle, the right factor is \(1-r^N=0\);
all subsequent coefficients are zero.

On the span of the products \(b_jc_l\), write
\(\mathsf S b_jc_l=r^j b_jc_l\) and
\(\mathsf T b_jc_l=r^l b_jc_l\). These are the inverses
of \(\mathsf D,\mathsf E\) on this finite band. The two
summed relations (11) are
\[
 \begin{split}
 \mathsf R_1H_N&=0,&
 \mathsf R_1&=(1-\mathsf S)^3
             -(X^{-1}-r\mathsf S)(1-r\mathsf S\mathsf T),\\
 \mathsf R_2H_N&=0,&
 \mathsf R_2&=(1-Y\mathsf T)(1-\mathsf T)
             -Y(1-r\mathsf S\mathsf T).
 \end{split}
 \tag{12}
\]
For the first line, the second term raises \(b_j\) to
\(b_{j+1}\) by (7). Its possible coefficient at \(b_Nc_0\)
vanishes because the raising factor is \(1-r^N\).
For \(l>0\), the upper-row coefficient is already zero.
The lower row on the left has \((1-r^0)^3=0\).

For the second line, use (8) on the first term. After extracting
the common factor \(Y\), the coefficient of \(b_jc_{l-1}\)
is precisely the second difference in (11). The last coefficient
is \(-(1-r^j)a_{j,N-1}\), zero either by triangular support
or by \(j=0\). The lower term has \(1-r^0=0\). Thus
both identities include every support boundary.

It remains to remove the inverse operators in (12). In the
calculations below they act only on the original finite band.
Using (6) gives, as identities applied to that band,
\[
 \mathsf Q_1=-r^3X\mathsf D^3\mathsf E\mathsf R_1,
 \qquad
 \mathsf Q_2=-Y\mathsf D\mathsf E^2Y^{-1}\mathsf R_2.
 \tag{13}
\]
Here \(\mathsf R_2F\) is divisible by \(Y\) for every
band member \(F\), by the same use of (8), so this intermediate
\(Y^{-1}\) introduces no pole.
For completeness, the only higher commutations needed are
\[
 \begin{split}
 \mathsf D^3X^{-1}
   &=r^{-3}X^{-1}\mathsf D^3+(r-r^{-2})\mathsf D^2,\\
 \mathsf E^2Y^{-1}
   &=r^2Y^{-1}\mathsf E^2+(1-r^2)\mathsf E.
 \end{split}
 \tag{14}
\]
Expanding (12), applying (14), and collecting terms gives (9)
in precisely its displayed order. Equations (12)--(13) prove (10).
No inverse operator remains in the conclusion. \(\square\)

## 3. The equations and one coefficient determine the finite sum

Let
\[
 \mathscr B_N=\operatorname{span}_{\mathbb C}
             \{b_j(X)c_l(Y):0\le j,l<N\}.
 \tag{15}
\]
This is the full square band: degree at most \(N-1\) in
\(X^{-1}\) and in \(Y\). Indeed the \(b_j\) are monic
in \(X^{-1}\), and \(c_l=Y^l+O(Y^{l+1})\).
No triangular support is assumed for an arbitrary band member.

**Theorem 2.** The joint kernel of \(\mathsf Q_1,\mathsf Q_2\)
in \(\mathscr B_N\) is the line spanned by \(H_N\).
Its unique member with \(b_0c_0\) coefficient one is (2).

*Proof.* First, the clearances in (13) create no additional
solutions on this band. The operator \(\mathsf D\) is
injective on polynomials in \(X^{-1}\): it preserves each
degree, and its leading coefficient in degree \(k\) is
multiplied by the nonzero scalar \(r^{-k}\). The operator
\(\mathsf E\) is injective on polynomials in \(Y\), even
outside degree \(N-1\). In fact
\[
       \mathsf E Y^k=r^{-k}Y^k+(1-r^{-k-1})Y^{k+1},
 \tag{16}
\]
so the first nonzero coefficient is multiplied by \(r^{-k}\).
These arguments also hold with the other variable as a coefficient.
Multiplication by \(X\) or \(Y\) is injective, and
\(\mathsf R_2F\) has the factor \(Y\) just noted.
Thus \(\mathsf Q_1F=\mathsf Q_2F=0\) implies
\(\mathsf R_1F=\mathsf R_2F=0\).

Write \(F=\sum u_{jl}b_jc_l\). The coefficient computation
in the preceding proof gives (11) with \(u\) in place of
\(a\), together with its upper boundary conditions.
At \(j=0\), the second recurrence gives
\(u_{0l}=u_{0,l-1}\) for \(1\le l<N\), because
\(1-r^l\ne0\). Hence all \(u_{0l}=u_{00}\).
For each \(l\), the first recurrence then determines every
\(u_{jl}\), since its multiplier \((1-r^j)^3\) is
nonzero for \(1\le j<N\). It gives exactly
\[
 u_{jl}=u_{00}\frac{P_{j+l}}{P_j^3P_l}\quad(j+l<N),
 \qquad u_{jl}=0\quad(j+l\ge N).
 \tag{17}
\]
At the first upper-wall index the recurrence forces zero and
continues it. These coefficients satisfy both upper boundary
conditions, as already verified in Theorem 1. The normalized
solution exists by (2), proving the assertion. \(\square\)

The same conclusion holds over
\(R_N=\mathbb Z[q,N^{-1}]\), with a free rank-one kernel,
and after any base change from this ring. To see this directly,
\(P_{N-1}=N\), so every \(1-r^j\), \(1\le j<N\),
is a unit in \(R_N\). All coefficient recurrences therefore
remain valid with invertible multipliers. The injectivity arguments
use unit leading or lowest coefficients and remain valid over a
coefficient ring with zero divisors. There is no appeal to an
unproved descent or flatness assertion.

## 4. Restoring the chirp and taking the commuting symbols

Let \(T_a,T_y\) shift \(a,y\) by \(1/N\), respectively.
Conjugating (5) by (3) replaces its operators by
\[
 \mathsf D_Z=(1-rX)T_a+rX,
 \qquad
 \mathsf E_Z=Y-r^{1/2}(1-Y/r)T_y.
 \tag{18}
\]
Indeed the chirp ratio is
\(e^{-\pi i(N-1)/N}=-q=-r^{-1/2}\). Its inverse gives
the minus sign and \(r^{1/2}\) in (18).
Use these two operators in the same ordered formulas (9).
They annihilate the literal \(Z_N\), including its original
scalar and chirp. No change of peripheral normalization has been
made by unchirping the proof.

In the commuting symbol at \(r=1\), denote the symbols of
\(T_a,T_y\) by \(L,U\). Then
\[
          D=X+(1-X)L,
 \qquad E=Y-(1-Y)U,
 \tag{19}
\]
and (9) becomes
\[
 \begin{split}
 D(D-X)(DE-1)-XE(D-1)^3&=0,\\
 YE(DE-1)-D(E-Y)(E-1)&=0.
 \end{split}
 \tag{20}
\]
These are exactly the polynomials in
[the boundary-shift limit theorem](research_mixed_fourier_boundary_shift_relations.md).
Its proved holomorphic asymptotic selects
\(L=e^{\Phi_a},U=e^{\Phi_y}\) and the original logarithmic
branch. Thus the finite difference equations and the analytic
critical equations concern the same normalized finite function.

The rank-one kernel supplies a precise finite-level algebraic
uniqueness statement. Over \(\mathbb C\), its nonzero elements
form a multiplicative torsor, and the coefficient in Theorem 2
fixes a section. The analytic lower asymptotic is still a separate
theorem: uniqueness of the finite-band solution does not bound its
growth or prevent cancellation under another functional.
In particular the original fixed short filling applies its Newton
trace, with its first normal derivatives. Neither \(T_a\) nor
\(T_y\) has been identified with that operation. Controlling
that trace, the contributing global contour, and the marked volume
after arbitrary short partial fillings remains necessary for the
finite-exception theorem.

The [exact closing interface](research_mixed_fourier_boundary_closing_interface.md)
writes the corresponding full-period integral and its missing
complementary-contour estimate. It also distinguishes the diagonal
boundary mark from the original crossing's repeated-root normal
action.
