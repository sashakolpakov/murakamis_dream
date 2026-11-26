# Removing the second-index period factor on the complete adjacent cycle

Research deduction, 7 November 2026. In the exact merged source,
the paired first-variable currents have terms proportional to the
second-index sampling factor. Those terms vanish after the entire
second residue contour is kept together. The remaining first-current
kernels are precisely their physical-second-index values, although
the second variable itself is still free on the contour.

This is an identity of complete cycles. It is not a pointwise
replacement of a free-variable kernel, and it does not bound the
remaining coupled current. The first zero-mode integral and the
explicit free-endpoint period factor are retained. No numerical
evaluation is used.

## 1. The exact source and its bounded second contour

Use all conventions of
[the merged source](research_mixed_two_adjacent_merged_source.md),
equations (1), (14), (16), (17), (28)--(35). In particular
\[
\begin{gathered}
 D=N-1,\quad N\ge2,\quad
 0<\Re x,\Re y<1,\quad
 \alpha=-\frac1{3N},\quad\beta=\alpha+1,\\
 A=e^{-2\pi iNa},\quad B=e^{-2\pi iNs},\quad
 C=e^{-2\pi iNx},\qquad
 k_a=\frac1{1-A},\quad k_s=\frac1{1-B},
\end{gathered}
 \tag{1}
\]
and the literal row is
\[
 \mathscr R(a,s)=e^{2\pi iNas}
 \Pi_N(a+s)\Pi_N(a+x)\Pi_N(s+y)
              E_N(a)^2E_N(s)^2E_N(x)E_N(y).
 \tag{2}
\]
All parameter dependence suppressed in \(\mathscr R\) remains
unchanged. The exact source is
\[
 V_{22,N}(x,y)
 =e^{\pi iD(x+y)}
      \sum_{u,v=0}^{D}\mathscr R(u/N,v/N).
 \tag{3}
\]
The physical terms with \(u+v\ge N\) are the original numerator
zeros of \(\Pi_N((u+v)/N)\). They are not deleted off grid.

Let \(\Gamma_s\) be the positively oriented boundary of a
bounded rectangle with real sides \(\alpha,\beta\) and lower
and upper heights of opposite signs. Both heights are finite.
Every physical \(s=v/N\) is inside. For every \(a=\alpha+it\),
the function
\[
                          s\longmapsto \mathscr R(a,s)/B
 \tag{4}
\]
is holomorphic on a neighborhood of this closed rectangle.
Indeed \(\Re(a+s)\ge2\alpha=-2/(3N)>-1/N\), so the shared
numerator is in its original global holomorphic domain.
The other numerator arguments also have real part \(>-1/N\);
the reciprocal arguments have real part \(<1\).
Finally \(1/B=e^{2\pi iNs}\) is entire.
In particular neither the numerator support walls nor the
physical second indices are singularities of (4).

The residue of \(k_s\) at \(s=v/N\) is \(1/(2\pi iN)\).
Consequently \(\sum_v f(v/N)=N\oint_{\Gamma_s}k_sf\,ds\)
for each holomorphic \(f\) on this rectangle. The coefficient
is \(N\), with no additional \(1/(2\pi i)\).

## 2. An exact split of the paired first-variable kernels

For an arbitrary fixed real height \(h\), the merged-source
Proposition 4 expresses the first finite sum as \(N\) times
a horizontal integral plus its two upward paired currents.
Its side kernels are
\[
\begin{split}
 K_+(A,B;C)
 &=\frac{(1-B)+A(B-C)+A^2B(C-1)}
                  {B(1-A)^3},\\
 K_-(A,B;C)&=A K_+(A,B;C).
\end{split}
 \tag{5}
\]
The upper current runs from \(\alpha+ih\) to \(\alpha+i\infty\);
the lower one from \(\alpha-i\infty\) to \(\alpha+ih\).
All vertical integrals below have these upward orientations.

Put
\[
\begin{split}
 K_+^{\,0}(A;C)&=(1-C)\frac{A}{(1-A)^2},\\
 K_-^{\,0}(A;C)&=(1-C)\frac{A^2}{(1-A)^2}.
\end{split}
 \tag{6}
\]
These are the values of (5) at \(B=1\). The exact differences
at free \(B\) are
\[
\begin{split}
 K_+-K_+^{\,0}
   &=(B^{-1}-1)\frac{1-CA}{(1-A)^3},\\
 K_--K_-^{\,0}
   &=(B^{-1}-1)\frac{A(1-CA)}{(1-A)^3}.
\end{split}
 \tag{7}
\]
This follows by expanding the numerator of (5); in particular
the coefficient \(C=X^N\) has not been replaced by one.
Multiplication by the actual outer sampling kernel cancels
the entire second-index factor:
\[
                         k_s(B^{-1}-1)=B^{-1}.
 \tag{8}
\]
Thus the second-variable integrands of the differences (7)
are holomorphic, rather than smaller in modulus.

## 3. Complete-cycle identity and the justified interchange

Define
\[
\begin{split}
 \mathcal J_h^{\,0}(s)={}&
       \int_{\alpha+ih}^{\beta+ih}\mathscr R(a,s)\,da\\
 &+\int_{\alpha-i\infty}^{\alpha+ih}
                  K_-^{\,0}(A;C)\mathscr R(a,s)\,da\\
 &+\int_{\alpha+ih}^{\alpha+i\infty}
                  K_+^{\,0}(A;C)\mathscr R(a,s)\,da .
\end{split}
 \tag{9}
\]

**Theorem 1.** At each fixed level, for either parity and the
original source parameters in (1),
\[
 \boxed{\quad
 V_{22,N}(x,y)
   =e^{\pi iD(x+y)}N^2
        \oint_{\Gamma_s}k_s(s)\mathcal J_h^{\,0}(s)\,ds .
 \quad}
 \tag{10}
\]
The inner currents converge absolutely and locally uniformly
on the bounded second contour. The same is true of the
differences removed in (7). The equality retains the entire
outer closed contour and the horizontal zero mode in (9).

*Proof.* Apply merged-source Proposition 4 to the first sum
in (3), then apply the outer residue formula. This gives
(10) with \(K_\pm\) in place of \(K_\pm^{\,0}\), with the
outside coefficient \(N^2\) and exactly the displayed chirp.

We first justify the interchange needed only for the
differences. On the first line \(a=\alpha+it\), \(1-A\)
never vanishes:
\[
                   |1-A|^2=1+e^{2\pi Nt}+e^{4\pi Nt}.
 \tag{11}
\]
For \(t\to-\infty\), the lower difference kernel in (7),
after multiplication by \(k_s\), is
\(O(A/B)\). The original row has its exact leading
first-variable exponent \(e^{2\pi iNas}\). Its modulus
therefore decays after this multiplication at rate
\[
                         2\pi N(1-\Re s).
 \tag{12}
\]
For \(t\to+\infty\), the upper difference kernel is
\(O(A^{-2}/B)\), while the row has its exact leading
exponent \(e^{-2\pi iNxa}\). The decay rate is then
\[
                         2\pi N(2-\Re x).
 \tag{13}
\]
The fixed-level asymptotics, their original constants, and
their locally uniform versions are those proved in (34)
of the merged-source note. Shared factors independent of
\(a\) are kept multiplicatively; if such a factor vanishes,
the row vanishes and no quotient is taken.

On the entire bounded second contour,
\(1-\Re s\ge1-\beta=1/(3N)\).
Thus the lower rate (12) is at least \(2\pi/3\), including
the actual right side of that contour. All its other
parameters, including \(1/B\), are bounded at fixed \(N\).
The upper rate (13) is strictly positive as well.
These estimates give an absolutely integrable majorant
uniform on \(\Gamma_s\). The same argument with upper
rate \(2\pi N(1-\Re x)\) proves convergence of (9).
This is a fixed-\(N\), one-unbounded/one-bounded interchange,
not an exchange of two infinite currents.

Fubini and (7)--(8) now reduce the upper difference to
\[
 \int_{\alpha+ih}^{\alpha+i\infty}
    \frac{1-CA}{(1-A)^3}
        \left\{\oint_{\Gamma_s}\frac{\mathscr R(a,s)}B\,ds\right\}da
                         =0,
 \tag{14}
\]
by the holomorphy in (4). The lower difference has the same
zero inner integral and the additional factor \(A\).
This proves (10), including all signs and orientations.
\(\square\)

For example one can split \(\Gamma_s\) into its upper,
lower and two side pieces, but the four integrals of (4)
need not vanish separately. Their sum is what is zero in
(14). A later deformation must retain the corresponding
joining pieces and their exact cancellation.

## 4. Relation to the homogeneous conditional representative

For every regular \(s\), retain the exact factorization
\[
\begin{split}
 \mathscr R(a,s)
  &=A_N^{\rm pre}(s;y)\,T_N(a;s,x),\\
 A_N^{\rm pre}(s;y)&=\Pi_N(s+y)E_N(s)E_N(y),
\end{split}
 \tag{15}
\]
where \(T_N\) is the original conditional factorial row.
This is a multiplication identity, including any zeros of
the prefix factor.
At physical \(s=v/N\), that factor is exactly \(p_v(W)/P_v\).

The conditional particular current has the exact form
\[
 C_{0,N}(e^{-2\pi is},e^{-2\pi ix})-H_N(s,x)
    =\frac N2(1-C)(B^{-1}-1)
         \int_{\alpha-i\infty}^{\alpha+i\infty}
                        k_{3,N}(a)T_N(a;s,x)\,da,
 \quad
 k_{3,N}(a)=\frac{A(1+A)}{(1-A)^3}.
 \tag{16}
\]
The first contour can be moved from its original midpoint
line to \(\Re a=\alpha\): the swept strip lies strictly
between the same two physical poles and all factorial
arguments remain holomorphic. The original fixed-level
tails justify that move. No normalization changes.

After multiplication by the actual prefix in (15) and the
outer kernel \(k_s\), the complete second residue integral
of (16) vanishes. This can be seen either at its physical
nodes or directly: (8) leaves the holomorphic factor
\(\mathscr R/B\), whose complete contour integral is zero.
The absolute fixed-level bounds needed to interchange
this one vertical line with the bounded contour are the
same as in Section 3; \(k_3\) has lower order \(A\) and
upper order \(A^{-1}\).

The stronger identity (10) also removes the other terms
proportional to \(B^{-1}-1\) from the paired first currents.
It is therefore a concrete complete-cycle cancellation,
not the unsupported replacement of \(C_0\) by \(H_N\) at a
free complex argument.

For clarity, (9) can be written equivalently as
\[
\begin{split}
 \mathcal J_h^{\,0}(s)
   ={}&\int_{\alpha+ih}^{\beta+ih}\mathscr R(a,s)\,da\\
      &+(1-C)\mathcal I_2^{\rm row}(s)
          +(C-1)\mathcal L_h^{\rm row}(s),\\
 \mathcal I_2^{\rm row}(s)
   &:=\int_{\alpha-i\infty}^{\alpha+i\infty}
                       \frac{A}{(1-A)^2}\mathscr R(a,s)\,da,\\
 \mathcal L_h^{\rm row}(s)
   &:=\int_{\alpha-i\infty}^{\alpha+ih}
                       \frac{A}{1-A}\mathscr R(a,s)\,da .
\end{split}
 \tag{17}
\]
This uses
\(A^2/(1-A)^2=A/(1-A)^2-A/(1-A)\).
Both terms in (17) remain coupled to the outer contour.
In particular the generally exponentially large factor
\(C-1\) has not been discarded.

The whole expression (10) is independent of the arbitrary
cut height \(h\), because it is the exact source (3).
There is no claim that \(\mathcal J_h^{\,0}(s)\) is
pointwise independent of \(h\) at free \(s\).

## 5. What remains to estimate

The new identity removes all explicit free-\(B\) dependence
from the two first-current kernels on the complete sampled
cycle. The row \(\mathscr R(a,s)\), the outer kernel, the
free-endpoint factor \(1-C\), and every part of
\(\Gamma_s\) remain. The first horizontal integral is
still present with positive density \(N\).

Neither (12)--(13) nor exact annihilation in (14) is an
\(N\)-uniform bound at the merged critical action
\(\mathcal S_{22}(x_0,x_0)\). The next estimate must
control the surviving coupled terms in (9) or (17),
together with the whole first horizontal complement,
after an admissible deformation of the outer closed
contour. No bound for an isolated side or a prescribed
knot closing functional follows from this identity alone.

## 6. Exact excision of the whole upper-right product cycle

There is a second complete-cycle cancellation for the region in
which both physical indices are large. It removes the entire
contour surrounding that region, rather than its principal
horizontal surface alone.

Let
\[
 L_N=\lceil N/2\rceil,\qquad
 \gamma_N=\frac{L_N-1/4}{N},\qquad
 I_-=[\alpha,\gamma_N],\quad I_+=[\gamma_N,\beta].
 \tag{18}
\]
No cut is a physical node. The low interval contains precisely
the indices \(0,\ldots,L_N-1\), and the high interval contains
\(L_N,\ldots,D\).
For each variable choose any fixed finite lower and upper
heights of opposite signs, and use these same heights in its
low, high, and full rectangles. Denote their positively
oriented boundary contours by
\(\Gamma_a^-,\Gamma_a^+,\Gamma_a\) and
\(\Gamma_s^-,\Gamma_s^+,\Gamma_s\).
As oriented contour chains,
\[
        \Gamma_a=\Gamma_a^-+\Gamma_a^+,\qquad
        \Gamma_s=\Gamma_s^-+\Gamma_s^+ .
 \tag{19}
\]
The vertical segments on the artificial cuts cancel in these
chain equalities.

On the product of the two closed high rectangles define the
shifted row
\[
 \mathscr R^{\rm sh}(a,s)
 =e^{2\pi iNas}\Pi_N(a+s-1)
    \Pi_N(a+x)\Pi_N(s+y)
            E_N(a)^2E_N(s)^2E_N(x)E_N(y).
 \tag{20}
\]
It is holomorphic on a neighborhood of that entire product,
at arbitrary fixed finite heights. In fact
\[
 2\gamma_N-1=
 \begin{cases}
 -1/(2N),&N\ \text{even},\\
 +1/(2N),&N\ \text{odd},
 \end{cases}
 \qquad
 2\beta-1=1-\frac2{3N}<1 .
 \tag{21}
\]
Thus the shifted shared argument has real part \(>-1/N\),
including the lower-left corner. The other numerator and
reciprocal arguments retain the domains used in Section 1.

The exact one-period factorial recurrence gives
\[
       \mathscr R=(1-AB)\mathscr R^{\rm sh}.
 \tag{22}
\]
Indeed \(e^{-2\pi iN(a+s-1)}=AB\).
It follows that the full two-variable sampling form satisfies
\[
 \boxed{\qquad
 k_a k_s\mathscr R
          =(k_a+k_s-1)\mathscr R^{\rm sh}.
 \qquad}
 \tag{23}
\]
The identity
\((1-AB)/[(1-A)(1-B)]=k_a+k_s-1\) fixes all signs.
The double sampling poles have canceled. Single-variable
poles can remain, and their contour contributions must be
kept.

**Theorem 2.** The full upper-right product cycle is zero:
\[
 \oint_{\Gamma_a^+}\oint_{\Gamma_s^+}
                k_a k_s\mathscr R\,ds\,da=0 .
 \tag{24}
\]
Consequently the entire original Fourier source has the exact
two-rectangle expression
\[
\boxed{\begin{split}
 V_{22,N}(x,y)=e^{\pi iD(x+y)}N^2
 \bigg\{&
 \oint_{\Gamma_a^-}\oint_{\Gamma_s}
                 k_a k_s\mathscr R\,ds\,da\\
 &+\oint_{\Gamma_a^+}\oint_{\Gamma_s^-}
                 k_a k_s\mathscr R\,ds\,da
 \bigg\}.
\end{split}}
 \tag{25}
\]
It holds for every \(N\ge2\), both parities, with the original
source and normalizations.

*Proof.* In (23), the \(k_a\) term has zero integral in \(s\),
since \(\mathscr R^{\rm sh}\) is holomorphic inside
\(\Gamma_s^+\). The \(k_s\) term has zero integral in \(a\);
interchanging these two bounded contour integrals is valid.
The constant term is holomorphic in both variables and
also integrates to zero. This proves (24) without an
estimate or a division by a numerator zero.

Equivalently, the physical nodes on this product have
\(u,v\ge L_N\), hence \(u+v\ge N\); their original rows
are all zero. Identity (23) exhibits how their complete
contour contributions cancel.
Expand the product of the two chain equalities (19) in
the original full-square residue formula. Removing only
the zero term (24) yields exactly (25). The common outer
coefficient is \(N^2e^{\pi iD(x+y)}\), as in (3), (10).
\(\square\)

For large \(N\), the proved central critical rectangle is
inside the low-low part of (25). The competing fixed
square near \((1,1)\) found in
[the raised-corner obstruction](research_mixed_two_adjacent_raised_corner_obstruction.md)
lies inside the excised high-high part.
Thus its entire contour can be removed exactly.
Its horizontal integral is generally nonzero and large:
(24) instead cancels it with the other pieces of that
same product cycle.

Formula (25) keeps the artificial-cut side currents and
every original outer side, horizontal alias, and joining
current when its two product cycles are decomposed.
It does not authorize retaining only their two principal
horizontal surfaces. The remaining high-low and low-high
wings can still contain off-grid points beyond \(a+s=1\);
no dominance estimate for those wings is asserted here.
Replacing the staircase of all such zero rows by a
straight diagonal cut would require retaining the
additional single-pole boundary currents visible in
(23). None is discarded by this theorem.
