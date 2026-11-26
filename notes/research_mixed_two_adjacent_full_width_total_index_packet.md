# A complete full-width total-index interpolant for the merged pair

Research deduction, 7 November 2026. A fixed symmetric difference-index
cutoff includes every physical inner row. Its extra physical rows vanish
exactly through the original reciprocal-factorial zeros. On a complex
total-index corridor containing the actual saddle, the complete finite
interpolant has a nonzero Gaussian packet. The proof controls all its
rows, including the negative-index continuation and the zero-height
transition; no endpoint current remains in this inner representation.

This gives a packet for a specified exact interpolant, with complete
physical-node equality. The remaining outer total-index sum and its
contours are not evaluated here. No numerical evaluation is used.

## 1. The finite source and exact full physical equality

Retain the exact factorial row
\[
\begin{split}
 T_N(a;c,x)={}&e^{2\pi iNa(c-a)}
 \Pi_N(c)\Pi_N(a+x)\Pi_N(c-a+x)\\
 &\qquad\cdot E_N(a)^2E_N(c-a)^2E_N(x)^2
\end{split}
 \tag{1}
\]
from [the original merged source](research_mixed_two_adjacent_merged_source.md).
For \(\sigma\in\{0,1/2\}\), define
\[
 \mathcal W_{\sigma,N}=\{d\in\mathbb Z+\sigma:|d|\le N/2\},
 \qquad
 \mathcal B_{\sigma,N}(c,x)
   =\sum_{d\in\mathcal W_{\sigma,N}}T_N(c/2+d/N;c,x).
 \tag{2}
\]
The fixed index set is symmetric and independent of every parameter.

Use
\[
 \mathcal D=
 \left\{(c,x):\frac{13}{20}<\Re c<\frac{17}{20},\quad
                  \frac9{50}<\Re x<\frac{19}{100}\right\}.
 \tag{3}
\]
For \(|t|\le1/2\), the two inner arguments \(a=c/2+t\),
\(s=c/2-t\) obey
\[
 -\frac7{40}<\Re a,\Re s<\frac{37}{40},\qquad
 \frac1{200}<\Re(a+x),\Re(s+x)<\frac{223}{200}.
 \tag{4}
\]
The numerator factorial is holomorphic on \(\Re z>-1/N\)
by the [positive-wall continuation](research_mixed_fourier_right_cap_joint_global_chart.md),
section 1. The reciprocal \(E_N\) is holomorphic on
\(\Re z<1\), with precisely the retained negative-index zeros
specified by the
[global reciprocal chart](research_mixed_fourier_global_factorial_cardinal.md),
Proposition 1. Thus (1)--(2) are holomorphic on all of (3),
including zero parameter heights and numerator real parts greater
than one. No division by a support zero has been made.

Let \(c=m/N\) lie in (3), and choose \(\sigma=0\) for even \(m\)
and \(\sigma=1/2\) for odd \(m\). Then \(j=m/2+d\) is an integer.
Every \(0\le j\le m\) occurs in (2), since \(|j-m/2|\le m/2<N/2\).
If an additional row has \(j<0\), its factor \(E_N(j/N)^2\)
is exactly zero; if \(j>m\), its factor \(E_N((m-j)/N)^2\)
is exactly zero. Every other factor is finite by (4).
Consequently, with the original \(r,P_j,p_j,X\) conventions,
\[
 \boxed{\quad
 \mathcal B_{\sigma,N}(m/N,x)
   =P_m\sum_{j=0}^{m}
       \frac{r^{-j(m-j)}p_j(X)p_{m-j}(X)}
                         {P_j^2P_{m-j}^2}
   =B_{N,m}(x).
 \quad}
 \tag{5}
\]
This is the entire physical inner sum, not a central truncation.
It holds for every free external \(x\) in (3), hence for its
derivatives. The parity choice remains part of the identity.

## 2. Full-width phase dominance at nonnegative total height

For \(\Im z>0\), use the original upper primitive
\[
 g_+(z)=\pi iz(1-z)+\frac{i}{2\pi}
                \{\operatorname{Li}_2(e^{2\pi iz})-\pi^2/6\}.
 \tag{6}
\]
It agrees with \(g\) on the original strip. Its continuous
upper boundary values, including at integers, are used at
zero height. The global upper-half-plane factorial theorem is
[the uniform continuation lemma](research_factorial_uniform_halfplane_continuation.md),
with the original marking included. In particular it applies
at both negative real parts and real parts above one when
the height is strictly positive.

Suppose \(\Im c\ge0\) and \(\Im x>0\). In the phase
\[
 F_c^+(a;x)=g_+(c)+g_+(a+x)+g_+(c-a+x)
            -2g_+(a)-2g_+(c-a)-2g_+(x)+2\pi ia(c-a),
 \tag{7}
\]
put \(a=c/2+t\), \(-1/2\le t\le1/2\). Set
\(C=\Re c,\xi=\Re x,h=\Im c/2,\upsilon=\Im x\),
\(r_h=e^{2\pi h}\), \(R=e^{2\pi(h+\upsilon)}\).
Away from a possible zero-height inner integer, its real
derivative is exactly
\[
\begin{split}
 \frac{d}{dt}\Re F_c^+(c/2+t;x)
 ={}&
 \log\frac{|1-R e^{-2\pi i(C/2+t+\xi)}|}
               {|1-R e^{-2\pi i(C/2-t+\xi)}|}\\
 &-2\log\frac{|1-r_h e^{-2\pi i(C/2+t)}|}
                  {|1-r_h e^{-2\pi i(C/2-t)}|}.
\end{split}
 \tag{8}
\]
The chirp derivative is purely imaginary. For \(0<t<1/2\),
the squared numerator differences in these two ratios are
respectively
\[
       4R\sin\pi(C+2\xi)\sin(2\pi t)<0,\qquad
       4r_h\sin(\pi C)\sin(2\pi t)>0.
 \tag{9}
\]
Indeed \(101/100<C+2\xi<123/100\) and \(13/20<C<17/20\).
Thus (8) is strictly negative. By symmetry it is strictly
positive on the left half.

At \(h=0\), the inner argument may pass through zero.
The singular logarithmic derivative is locally integrable,
and (7) is continuous there. Integrating (8) on either side
and taking the common limit preserves strict monotonicity.
The values at \(t=\pm1/2\) are also strictly below the center,
although their one-sided derivative can tend to zero.

It follows that the unique full-width maximum is the
actual midpoint \(a=c/2\). Its action, Hessian and amplitude
are exactly
\[
\begin{split}
 \Phi(c,x)&=g(c)+2g(c/2+x)-4g(c/2)-2g(x)
                                      +\frac{\pi i}{2}c^2,\\
 \mathcal K(c,x)&=
       2\pi\cot\pi(c/2+x)-4\pi\cot(\pi c/2)-2\pi i,\\
 \mathcal A(c,x)&=
 \frac{\sqrt{2\pi}\,\mathfrak a(c)\mathfrak a(c/2+x)^2}
 {\mathfrak a(x)^2\mathfrak a(c/2)^4\sqrt{-\mathcal K(c,x)}}.
\end{split}
 \tag{10}
\]
These midpoint arguments stay in the original regular strips.
In particular \(\Re\mathcal K<0\), and the square root with
positive real part is the original Gaussian branch.

For every compact \(K\subset\mathcal D\cap\{\Im c\ge0,\Im x>0\}\)
there is \(\delta_K>0\) such that
\[
 \Re F_c^+(c/2+t;x)\le\Re\Phi(c,x)-\delta_K,
                       \qquad 1/5\le|t|\le1/2,\quad(c,x)\in K.
 \tag{11}
\]
This uses continuity on the full compact set, including \(h=0\).
A uniform factorial bound through that boundary is established
next; no regular symbol is assumed at an inner zero.

## 3. A finite product upper bound retaining every zero

For bounded real \(u,h\), define
\[
                   f_h(u)=\log|1-e^{-2\pi i(u+ih)}|.
 \tag{12}
\]
If a finite product factor vanishes, its upper bound below
is immediate. Otherwise, for an interval of bounded length,
the right-endpoint mesh satisfies
\[
 \sum_{k=1}^{m}f_h(u+k/N)
       \le N\int_0^{m/N}f_h(u+t)\,dt+C\log N,
 \tag{13}
\]
uniformly in the interval location and in bounded \(h\), with
\(m/N\) bounded. The integral includes its logarithmic
singularities.

Here is a direct proof of the uniform one-sided estimate.
Writing \(\rho=e^{2\pi h}>0\) gives
\[
 |f_h'(u)|
  =\left|\frac{2\pi\rho\sin(2\pi u)}
                {(1-\rho)^2+4\rho\sin^2(\pi u)}\right|
  \le \pi|\cot(\pi u)|
 \tag{14}
\]
away from integers. Also \(f_h\) is bounded above on the
stated compact range and
\[
 f_h(u)\ge \pi h+\log(2|\sin\pi u|)
          \ge -C+\log\operatorname{dist}(u,\mathbb Z).
 \tag{15}
\]
On mesh cells at distance at least \(1/N\) from every
integer, the sum of the variations in (14) is \(O(\log N)\).
Only a bounded number of cells are excluded near the
integers. Their endpoint values are bounded above, while
their \(N\)-weighted integrals are bounded below by
\(-C-\log N\) using (15). This proves (13), including arbitrary
locations of the zero within a cell.

For \(z\) in a fixed compact real-height box with
\[
                     -7/40\le\Re z\le37/40,
 \tag{16}
\]
the original regular-strip theorem already bounds \(E_N(z)\)
when \(\Re z\ge1/8\). When \(\Re z\le1/8\), use exactly
\(m_N=\lfloor N/4\rfloor\). For all sufficiently large \(N\),
\(z+m_N/N\) has real part in a fixed compact subset of \((0,1)\).
The exact, undivided formula is
\[
 E_N(z)=E_N(z+m_N/N)
            \prod_{k=1}^{m_N}(1-e^{-2\pi i(z+k/N)}).
 \tag{17}
\]
Applying (13) and the regular denominator bound yields
\[
                  |E_N(z)|\le C N^A e^{-N\mathcal G(z)}.
 \tag{18}
\]
Here the continuous real rate is
\[
 \mathcal G(z)=
   \Re g(z+\tau)-\int_0^\tau
             \log|1-e^{-2\pi i(z+t)}|\,dt,
                  \qquad \tau=1/4
 \tag{19}
\]
in the low-real-part region, and \(\mathcal G(z)=\Re g(z)\)
in the original regular strip. These definitions agree on
their overlap by the original logarithmic derivative.
Replacing \(\tau\) by \(m_N/N\) in the derivation changes no
value: both terminal arguments are regular, so the difference
is exactly its intervening integral.

The function in (19) is continuous across all the real
zeros, by the elementary integrable logarithmic bound.
For \(\Im z>0\), it is exactly \(\Re g_+(z)\), by the
original continuation and horizontal integration. For
\(\Im z=0\), it is the corresponding continuous upper value.
Formula (18) remains valid at every reciprocal zero and
also for small negative heights. It is only an upper bound;
no nonzero symbol is asserted at a zero.

## 4. Uniform passage through zero total height

On a compact \(K\) as in (11), the numerator arguments
\(a+x,c-a+x\) have heights bounded strictly above zero.
Their global upper-half-plane packets therefore give
uniform bounds even when their real parts exceed one.
The argument \(c\) is regular, as is \(x\).
Apply (18) to both inner reciprocals. This gives
\[
 |T_N(c/2+t;c,x)|
       \le C N^A \exp\{N\Re F_c^+(c/2+t;x)\}
 \tag{20}
\]
uniformly for \(|t|\le1/2\), all \((c,x)\in K\), including
\(\Im c=0\). Every negative-index zero is retained in (17).

For completeness this comparison also persists on an
open complex neighborhood of \(K\), after decreasing its
size. Use the continuous rate \(\mathcal G\) from (19)
for the two inner reciprocals, while keeping the numerator
arguments at positive height. The resulting row rate is
continuous and agrees with \(\Re F_c^+\) on \(K\).
The action \(\Re\Phi\) is continuous there as well.
The strict loss (11) therefore survives, for example
with loss \(\delta_K/2\), on some open neighborhood
\(U_K\Subset\mathcal D\). In particular (20), with this
continuous rate, controls small negative total heights
near the zero-height part of \(K\). This is a finite
upper-bound argument, not an application of an
upper-half-plane asymptotic on its boundary.

Let \(\mathcal H_{\sigma,N}\) be the smaller exact central
source with \(|d|\le N/5\) from
[the central total-index packet](research_mixed_two_adjacent_central_total_index_packet.md).
The complete difference between (2) and that source is a
literal finite sum over \(N/5<|d|\le N/2\). Equations
(11), (18)--(20), and the \(O(N)\) row count show, after
absorbing fixed powers of \(N\), that
\[
 |\mathcal B_{\sigma,N}(c,x)-\mathcal H_{\sigma,N}(c,x)|
   \le C e^{N(\Re\Phi(c,x)-\varepsilon_K)}
                                      \qquad(c,x)\in U_K
 \tag{21}
\]
for some \(\varepsilon_K>0\) and all sufficiently large \(N\).
This comparison is uniform for both parity sources.

## 5. The complete complex-total packet and its exact scope

**Theorem.** On compact subsets of
\[
              \mathcal D\cap\{\Im c\ge0,\ \Im x>0\},
 \tag{22}
\]
and also on sufficiently small open neighborhoods of each
such compact subset, the exact full-width source satisfies
\[
 \boxed{\quad
 \mathcal B_{\sigma,N}(c,x)
     =N^{-1}\mathcal A(c,x)e^{N\Phi(c,x)}
                                     (1+O(N^{-1})),
 \qquad \sigma\in\{0,1/2\}.
 \quad}
 \tag{23}
\]
All fixed mixed \(c,x\) derivatives of the normalized error
are \(O(N^{-1})\) on smaller neighborhoods.

*Proof.* The central finite-source theorem supplies (23)
for \(\mathcal H_{\sigma,N}\) on its full regular complex
domain (3). Equation (21) transfers it to
\(\mathcal B_{\sigma,N}\), with an exponentially smaller
normalized difference. Both sources and the nonzero
normalization are holomorphic on \(U_K\). Nested Cauchy
estimates give the mixed derivatives, including at real
total parameters. No limiting derivative of a moving
physical cutoff is used. \(\square\)

The explicit domain contains the full actual complex
point \((c_*,x_0)\) from (6) of the central packet.
By (5), its two parity representatives coincide with the
whole original inner source at every admitted physical
total index. Thus there is no discarded inner physical
source in this representation. The intermediate central
cutoff is only a tool for proving the complete packet.

An outer summation must still retain the even and odd
total-index sums as their respective exact representatives,
with spacing \(2/N\), and must bound their own endpoint
currents and aliases. It cannot replace the complete
outer signed sum by an absolute sum or propagate a
physical-axis relative error through cancellation.
The original scalar remains \(e^{2\pi i(N-1)x}\).
No equality between the two off-grid parity interpolants,
and no substitution of their raw \(c\)-derivatives for
ordinary normal adapters, is claimed.

