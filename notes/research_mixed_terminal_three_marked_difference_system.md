# An exact two-variable difference system for the terminal type-three source

Research theorem, 5 November 2026. Marking the unsummed Newton index
gives two homogeneous finite difference equations for the original
terminal type-three polynomial. Their joint kernel in the stated finite
band has dimension one; its normalization selects the literal source.
The equations retain the triangular support and the whole ordinary
color. They are not a closed scalar equation for the unmarked terminal
polynomial and give no large-level lower asymptotic.

## 1. The marked original polynomial

For \(N\ge2\), set
\[
 q=e^{\pi i/N},\qquad r=q^{-2},\qquad a_0=q^{-1},\qquad
 P_j=(r;r)_j,\qquad
 \rho_i(X)=X^{-i}(rX;r)_i
             =\prod_{j=1}^i(X^{-1}-r^j).
\tag{1}
\]
Use the actual ordinary color \(\omega\) and define
\[
 M_l(\omega)=\prod_{j=0}^{l-1}
       (1-a_0\omega r^j+r^{2j+1}),\qquad M_0=1.
\tag{2}
\]
The original Newton polynomial satisfies the exact identity
\[
                 (-q)^{-l}e_l(\omega)
                          =\frac{r^lM_l(\omega)}{P_l^2}.
\tag{3}
\]
For example, write \(\omega=-(\lambda+\lambda^{-1})\).
The numerator in (2) is
\((-a_0\lambda;r)_l(-a_0\lambda^{-1};r)_l\).
Each paired factor is \(q^{-(2j+1)}(c_j-\omega)\), where
\(c_j=2\cos((2j+1)\pi/N)\). Also
\(P_l^2=(-1)^lq^{-l(l+1)}S_l^2\).
This proves (3) from the
[literal Newton product](research_mixed_complete_boundary_sum.md).
The final formula is polynomial in \(\omega\) and makes no choice
of a color square root.

Define the auxiliary marked Laurent polynomial
\[
 F_N(\omega;X,Y)=
 \sum_{\substack{i,l\ge0\\i+l<N}}
       c_{i,l}(\omega)\rho_i(X)Y^l,\qquad
 c_{i,l}=\frac{r^lM_l(\omega)P_{i+l}}{P_i^3P_l^4}.
\tag{4}
\]
Every denominator index is less than \(N\). The exact
[terminal Newton identity](research_mixed_terminal_three_newton_reduction.md)
gives
\[
                   \mathcal V_{0,N}(\omega,X)
                              =N F_N(\omega;X,1).
\tag{5}
\]
Thus \(Y\) merely records the original Newton index. No row or alias
is removed in its introduction or in (5).

## 2. Ordered operators and exact annihilation

Let \(Z\) denote multiplication by \(X^{-1}\), let
\((\sigma_X f)(X,Y)=f(rX,Y)\), and set
\[
 K=(1-rX)\sigma_X+rX,\qquad
 (Wf)(X,Y)=f(X,rY).
\tag{6}
\]
Products of operators act from right to left. \(K\) commutes with
\(Y,W\), but
\[
 WY=rYW,\qquad KZ=r^{-1}ZK+(r-1).
\tag{7}
\]
The exact Gram-basis identities are
\[
 K\rho_i=r^{-i}\rho_i,\qquad
 Z\rho_i=\rho_{i+1}+r^{i+1}\rho_i,\qquad
 \rho_N=X^{-N}-1.
\tag{8}
\]
They follow directly from (1), as in the
[Gram-shift identity](research_mixed_terminal_gram_shift.md).
In particular
\[
                  (ZK^2-rK)\rho_i=r^{-2i}\rho_{i+1}.
\tag{9}
\]

**Theorem 1.** For every level, ordinary color, nonzero \(X\), and
complex \(Y\), the literal polynomial (4) satisfies
\[
\begin{split}
 L_uF_N&=0,&
 L_u&=K(1-W)^4
       -rY(1-a_0\omega W+rW^2)(K-rW),\\
 L_tF_N&=0,&
 L_t&=r^3(K-1)^3-(ZK^2-rK)(K-rW).
\end{split}
\tag{10}
\]
These are Laurent-polynomial identities, not identities modulo
\(X^N-1\).

*Proof.* The two interior coefficient relations are
\[
\begin{split}
 (1-r^l)^4c_{i,l}
   &=r(1-a_0\omega r^{l-1}+r^{2l-1})
                       (1-r^{i+l})c_{i,l-1},\\
 (1-r^i)^3c_{i,l}
   &=(1-r^{i+l})c_{i-1,l}.
\end{split}
\tag{11}
\]
They follow from (4) by finite products. No factor \(M_l\), and
no possibly zero Newton value, is divided out.

In \(L_uF_N\), the coefficient of \(\rho_iY^l\) is
\(r^{-i}\) times the first difference in (11).
The ordering \(Y(1-a_0\omega W+rW^2)(K-rW)\) is essential:
before raising \(l-1\) to \(l\), its last factor is
\(r^{-i}-r^l\).
At \(l=0\), the first term has factor \((1-r^0)^4=0\).
On the upper support wall, shifting a row with \(i+l=N-1\)
produces the factor \(1-r^N=0\). This includes \(i=0,l=N\).
There is therefore no missing \(Y^N\) boundary term.

By (9), the coefficient of \(\rho_iY^l\) in \(L_tF_N\) is
\(r^{3-3i}\) times the second difference in (11).
Its lower coefficient has \((1-r^0)^3=0\), while raising the
upper wall again produces \(1-r^N=0\).
In particular the possible \(\rho_NY^0=X^{-N}-1\) term has
coefficient zero before any physical value of \(X\) is imposed.
All interior and boundary coefficients vanish. \(\square\)

No inverse of \(K\), \(1-W\), \(K-1\), or \(K-rW\) was used.
The disappearing boundary here is a consequence of the original
two-index triangular coefficient. It does not erase the nonzero
forcing in the distinct one-index Gram transform.

## 3. The finite-band system selects the source uniquely

Consider the full square band
\[
 \mathscr B_N=\operatorname{span}_{\mathbb C}
       \{\rho_i(X)Y^l:0\le i,l<N\}.
\tag{12}
\]
No triangular support is assumed for an arbitrary member of this space.

**Theorem 2.** For each fixed ordinary color, the joint kernel of
\(L_t,L_u\) in \(\mathscr B_N\) has dimension one. Its member
whose \(\rho_0Y^0\) coefficient is one is exactly (4).

*Proof.* Write a joint-kernel member as
\(\sum b_{i,l}\rho_iY^l\). Linear independence of the polynomial
basis and (8)--(9) imply the two relations (11) with \(b\) in
place of \(c\), for every interior index.
At \(i=0\) the first relation becomes
\[
 (1-r^l)^3b_{0,l}
   =r(1-a_0\omega r^{l-1}+r^{2l-1})b_{0,l-1},
                 \qquad 1\le l<N.
\tag{13}
\]
Every multiplier \(1-r^l\) here is nonzero. Thus \(b_{0,0}\)
determines the entire \(i=0\) edge. The second relation in (11),
whose multiplier \(1-r^i\) is nonzero for \(1\le i<N\),
then determines every other coefficient.

For \(l\ge1\), that recurrence forces \(b_{N-l,l}=0\)
at the first upper-wall index, and then every subsequent coefficient
in that row is zero. Hence triangular support is itself forced.
The possible \(\rho_NY^l\) coefficient of \(L_t\) imposes
\((1-r^l)b_{N-1,l}=0\), already satisfied by that support
or by \(l=0\). The possible \(Y^N\) coefficient of \(L_u\)
also vanishes: for \(i=0\) its last factor is zero, and for
\(i>0\) the source coefficient \(b_{i,N-1}\) is zero.
No additional boundary condition remains.

Theorem 1 supplies a joint-kernel member with \(c_{0,0}=1\);
the coefficient determination proves existence and uniqueness with
that normalization. Only nonzero scalar interior multipliers have
been used, never an operator inverse or a root-of-unity wall factor.
This proof works when any Newton numerator factor vanishes.
\(\square\)

The same statement holds over the localized cyclotomic ring
\(R_N=\mathbb Z[q,N^{-1}]\), with the ordinary color left as a
polynomial variable. Indeed \(P_{N-1}=N\), so every factor
\(1-r^j\), \(1\le j<N\), is a unit in \(R_N\). The coefficient
recurrences therefore show that the joint kernel in the free square
band over \(R_N[\omega]\) is the free rank-one module generated
by \(F_N\). Its normalization is the coefficient \(c_{0,0}=1\).
The same explicit proof survives every base change from this ring;
no flatness assumption is needed to recover the normalized kernel.
This is an exact statement at a fixed level. It supplies no
compatibility between different levels, and no asymptotic estimate
for the resulting sequence of normalized sections.

The boundary data can also be read directly:
\[
\begin{split}
 F_N(\omega;X,0)&=\sum_{i<N}\frac{\rho_i(X)}{P_i^2},\\
 F_N(\omega;r^{N-1},Y)
   &=\sum_{l<N}\frac{Y^l(-q)^{-l}e_l(\omega)}{P_l}.
\end{split}
\tag{14}
\]
They are the original finite polynomials, not an asymptotic boundary
condition for a selected homogeneous solution.

## 4. Ordinary derivatives and the classical critical curve

The coefficients of (10) are polynomial in the actual color.
For \(F_N^{[k]}=\partial_\omega^kF_N\), differentiation gives
\[
\begin{split}
 L_tF_N^{[k]}&=0,\\
 L_uF_N^{[k]}&=-k\,r a_0YW(K-rW)F_N^{[k-1]},
                         \qquad k\ge1 .
\end{split}
\tag{15}
\]
Thus every ordinary derivative, including derivatives at odd-level
Newton zeros, is retained. Differentiating does not make all jets
homogeneous solutions of the color-dependent first operator.

As an algebraic comparison only, take the commuting symbols at
\(r=q=1\), and write \(k=z^{-1}\), \(w=W\), \(A=X\).
At \(Y=1\), \(\omega=-2\), the two symbol equations reduce to
\[
 (1+w)^2(1-wz)=(1-w)^4,\qquad
 (1-Az)(1-wz)=A(1-z)^3.
\tag{16}
\]
Multiplication by the nonzero symbol monomials suffices to obtain
these equations; no quantum operator is inverted.
They are exactly the original exponentiated stationary equations
of [the selected terminal critical curve](research_mixed_terminal_three_critical_curve.md).
The original logarithmic lifts and geometric branch remain those
proved there, rather than being selected by a symbol equation alone.

Equations (10) must be applied with \(Y\) present.
Specializing the answer to \(Y=1\) does not turn \(W\) into one:
\((WF_N)(X,1)=F_N(X,r)\). Consequently this is not yet a
closed scalar equation for \(\mathcal V_{0,N}(\omega,X)\).
The one-dimensional joint kernel and its exact normalization select
the finite source, but do not bound its inverse transport, determine
a contributing saddle cycle, or prove a nonzero geometric asymptotic.
