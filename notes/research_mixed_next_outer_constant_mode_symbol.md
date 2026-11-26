# The leading adjoint coefficient for the constant outer mode

Private exact-source and phase-space calculation, 8 November 2026.
The seven-term equation has a uniformly nonzero leading coefficient
when its adjoint acts on a slowly varying test function with the
original outer weights. This is the constant outer mode; the crossing
phase is already included in the adjoint. On every fixed compact
subinterval of the physical color interval the coefficients extend
holomorphically, and the difference from this leading multiplication
operator has an explicit Cauchy estimate of order \(N^{-1}\).

These are local coefficient statements. They do not give a global
inverse, remove the endpoint terms in summation by parts, or prove
the required outer cancellation. No numerical evaluation is used.

## 1. Exact angular form of the weighted adjoint

Use the full source, operators, and weights of
[the seven-term recurrence](research_mixed_next_physical_inner_seven_term_recurrence.md).
In particular its interior equation is
\[
 (\mathbf D_{3,N}f)_j=\sum_{r=-3}^{3}d_{j,r,N}f_{j+r},
 \qquad
 (\mathbf D_{3,N}^{\dagger}h)_j
 =\sum_{r=-3}^{3}\frac{\mu_{j-r,N}}{\mu_{j,N}}
                         d_{j-r,r,N}h_{j-r}.
 \tag{1}
\]
The adjoint is bilinear for the actual complex observation weights;
it is not a Hermitian adjoint. Write
\[
 \epsilon=1/N,\quad u=\pi-(2j+1)\pi\epsilon,\quad
 q=e^{\pi i\epsilon},\quad
 \mu_{j,N}=(-1)^U\kappa_N^3\omega_N(u)q^{3j(j+1)}.
 \tag{2}
\]
The exact positive nodal amplitudes have the angular formulas
\[
 \omega_N(u)=
 \begin{cases}
       \sin u,&N\text{ even},\\
       \sin u\sin(u/2)/\cos^2(\pi\epsilon/2),&N\text{ odd}.
 \end{cases}
 \tag{3}
\]
They are analytic functions of the displayed variables before
restriction to the physical nodes.

For every eligible shift, the exact ratio is
\[
 \boxed{\quad
 \frac{\mu_{j-r,N}}{\mu_{j,N}}
 =(-1)^r e^{3iru+3\pi i\epsilon r^2}
                 \frac{\omega_N(u+2\pi r\epsilon)}{\omega_N(u)}.
 \quad} \tag{4}
\]
Indeed
\((j-r)(j-r+1)-j(j+1)=-2jr+r^2-r\), and substituting
\(j=(\pi-u)/(2\pi\epsilon)-1/2\) gives (4).
In particular its leading ratio is \((-e^{3iu})^r\).
The sign in this expression retains the half-step of the physical
grid; it cannot be discarded as a slowly varying amplitude.

The angular operator giving the coefficients in (1) is the original
ordered expression
\[
 \mathcal D_{3,N}
 =q^{-2}(\mathcal L^2-I)\mathcal L_1
       +q^{-3}\mathcal L Z-8q^{-2}\mathcal L
                              +(8q^{-1}+2)I,
 \tag{5}
\]
where \(Z=-2\cos u\) acts by multiplication. The coefficients
of the two original shifts are
\[
 A_\epsilon(u)=
  \frac{4\cos^4((u-\pi\epsilon)/2)}
                      {\sin u\sin(u-\pi\epsilon)},
 \qquad C_\epsilon(u)=A_\epsilon(-u).
 \tag{6}
\]
On every fixed compact subset of \(0<u<\pi\), they tend to
\(a(u)=\cot^2(u/2)\). All following leading expressions are
computed from (4)--(6); the finite equation (1) is unchanged.

## 2. The leading coefficient

A shift of the index by one has formal multiplier \(\zeta\).
The leading symbols of the original index operators are
\[
 \ell(u,\zeta)=2+2a-a(\zeta+\zeta^{-1}),\qquad
 m(u,\zeta)=2+2a-a(e^{-iu}\zeta+e^{iu}\zeta^{-1})
 \tag{7}
\]
for \(\mathbf L\) and \(\mathbf L_1\), respectively.
These follow directly from equation (12) of the recurrence theorem:
\(q^{2j+2}\to-e^{-iu}\) and
\(q^{-2j}\to-e^{iu}\). Products of symbols give the leading
coefficient of the ordered products in (5), since their finite
shifts have size \(O(\epsilon)\) on a fixed regular chart.

For the adjoint acting on a constant test function, (4) requires
\(\zeta=-e^{3iu}\). Thus
\[
 \ell=2+4a\cos^2(3u/2),\qquad
 m=2+4a\cos^2u,
 \tag{8}
\]
and the leading coefficient is
\[
 d_0(u)=(\ell^2-1)m-(8+2\cos u)\ell+10.
 \tag{9}
\]
The same coefficient multiplies any test function varying on a
fixed, level-independent analytic scale.

**Theorem.** For every \(0<u<\pi\),
\[
                              d_0(u)\ge\frac14.
 \tag{10}
\]

*Proof.* Put \(x=\cos u\), so \(-1<x<1\), and
\(a=(1+x)/(1-x)>0\). The identity
\(1+\cos3u=(1+x)(2x-1)^2\) rewrites (8) as
\[
 \ell=2+\frac{2(1+x)^2(2x-1)^2}{1-x},\qquad
 m=2+4ax^2.
 \tag{11}
\]
In particular \(\ell\ge2\) and \(m\ge2\). Since
\(\ell^2-1>0\),
\[
 d_0\ge 2\ell^2-(8+2x)\ell+8.
 \tag{12}
\]

If \(-1<x\le-1/4\), the right side increases for
\(\ell\ge2\), because its derivative is
\(4\ell-8-2x\ge-2x>0\). At \(\ell=2\) it is
\(-4x\ge1\).

For \(-1/4\le x\le0\), write
\(p(x)=(1+x)(1-2x)=1-x-2x^2\). Here \(p\ge1\) and
\(1-x\le5/4\), so (11) gives
\(\ell\ge2+8/5>3\). Equation (12) is therefore at least
\(2(\ell-2)^2\ge2\).

For \(0\le x\le1/4\), the function
\(p(x)^2/(1-x)\) decreases: its derivative has numerator
\[
                        p(x)(-1-7x+6x^2)<0.
 \tag{13}
\]
Consequently \(\ell\ge\ell(1/4)=73/24>3\).
The quadratic in (12) increases for \(\ell\ge3\) on this
interval. Its value at three is \(2-6x\ge1/2\).

Finally, suppose \(1/4\le x<1\). Treat (9) as a function
of \(\ell\) with \(x\) fixed. Its derivative for
\(\ell\ge2\) is at least
\[
               4m-(8+2x)=2x(8ax-1)>0,
 \tag{14}
\]
since \(a\ge5/3\). Its value at two is
\[
                   4x(3ax-1)\ge\frac14.
 \tag{15}
\]
Indeed \(4x\ge1\) and \(3ax\ge5/4\). The four intervals
prove (10). \(\square\)

## 3. Actual analytic coefficient control in the interior

Let \(I\) be any fixed compact interval contained in \((0,\pi)\).
For \(r>0\), let \(I_r\) be its complex distance neighborhood.
There is \(R>0\), depending on \(I\), such that all coefficients
below are holomorphic on \(I_R\) for sufficiently small
\(|\epsilon|\), separately for each parity formula in (3).
Indeed the denominators in (3),(6) stay nonzero there. The
coefficients \(d_{j-r,r,N}\) are obtained by finitely many sums,
products, and fixed multiples of \(\epsilon\) in the arguments
of these same analytic functions. Equation (4) gives their
actual observation multipliers as analytic functions as well.

Thus the exact finite adjoint has a regular realization
\[
 (\mathcal A_{\epsilon,p}h)(u)
    =\sum_{r=-3}^{3}b_{r,p}(u,\epsilon)
                              h(u+2\pi r\epsilon),
 \tag{16}
\]
where \(p\) specifies even or odd parity, and evaluation at
interior physical nodes is exactly (1). Both parity families
satisfy
\[
 \sum_{r=-3}^{3}b_{r,p}(u,0)=d_0(u),\qquad
 b_{r,p}(u,\epsilon)=b_{r,p}(u,0)+O(\epsilon)
 \tag{17}
\]
uniformly on a smaller closed tube. By (10) and compactness,
we may shrink \(R\) so that \(|d_0(u)|\ge1/8\) on that tube.

For completeness this gives the precise small-shift estimate
needed by an analytic probe construction. After one further
fixed shrink of \(R\), there is \(C_I\) such that
\[
 \|\mathcal A_{\epsilon,p}h-d_0h\|_{I_s}
       \le C_I\frac{|\epsilon|}{\delta}
                              \|h\|_{I_{s+\delta}}
 \tag{18}
\]
whenever \(0<s<s+\delta<R\), \(\delta\le1\), and
\(12\pi|\epsilon|\le\delta\), for small enough
\(|\epsilon|\). To prove (18), subtract (17) inside (16).
The coefficient differences contribute
\(C|\epsilon|\|h\|\). Each translation has length at most
\(6\pi|\epsilon|\le\delta/2\); integrating \(h'\) along
that segment and using Cauchy's estimate on the remaining
\(\delta/2\) margin gives
\(C|\epsilon|\delta^{-1}\|h\|\). There are seven terms,
and \(\delta\le1\) absorbs the first contribution. This
argument bounds the actual finite coefficients, not just their
formal principal symbols.

Equations (10),(17)--(18) verify the interior coefficient
hypotheses for the analytic probe method in
[whole-kernel adjoint localization](research_whole_kernel_adjoint_ward_localization.md).
The finite-sum application must still use the exact boundary
terms and parity forcing from the recurrence theorem. The tube
and constants here depend on \(I\); they have not been extended
uniformly to colors at distance \(O(N^{-1})\) from zero or
\(\pi\). Nor is a resulting exponential residual rate asserted
to meet \(B_f\). The theorem treats the constant outer mode;
an inserted character whose degree is proportional to \(N\)
changes the leading symbol and needs its own comparison.
