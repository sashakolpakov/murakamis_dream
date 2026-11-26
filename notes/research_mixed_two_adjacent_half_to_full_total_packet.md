# The complete total-index packet from one half to the support edge

Research deduction, 7 November 2026. The golden-ratio modulus
comparison extends the complete full-width inner packet to every
compact total-index interval in \([1/2,1)\), at nonnegative complex
height. The exact finite interpolant, its full physical-node
equality, and its normalized joint derivatives are retained.
This includes the actual positive-height total saddle and the
whole real interval beneath it.

The theorem concerns the complete inner source. The outer sum,
its parity aliases and endpoint currents, and complementary
physical total indices remain separate. No numerical evaluation
is used.

## 1. Exact source and a sufficient holomorphic domain

Use the original factorial row
\[
\begin{split}
 T_N(a;c,x)={}&e^{2\pi iNa(c-a)}
  \Pi_N(c)\Pi_N(a+x)\Pi_N(c-a+x)\\
 &\qquad\cdot E_N(a)^2E_N(c-a)^2E_N(x)^2
\end{split}
 \tag{1}
\]
and the fixed full-width sums
\[
 \mathcal B_{\sigma,N}(c,x)=
   \sum_{\substack{d\in\mathbb Z+\sigma\\ |d|\le N/2}}
                          T_N(c/2+d/N;c,x),
                 \qquad \sigma\in\{0,1/2\}.
 \tag{2}
\]
They are the same exact sources as in
[the full-width theorem](research_mixed_two_adjacent_full_width_total_index_packet.md);
the larger parameter domain is established here.

Let
\[
 \mathcal U=\left\{(c,x):
  0<\Re c<1,\quad \frac16<\Re x<\frac14,\quad
  \Im x>0,\quad \Im(c/2+x)>0\right\}.
 \tag{3}
\]
Every inner argument in (1) satisfies
\[
                  -1/2<\Re a,\Re(c-a)<1.
 \tag{4}
\]
Thus both \(E_N\) factors are in their original holomorphic
reciprocal continuation. The two shifted numerator arguments
have strictly positive imaginary part by (3), regardless of
their real parts. The original global upper factorial is
holomorphic and nonzero there, with its specified Gamma
normalization; see the
[uniform half-plane continuation](research_factorial_uniform_halfplane_continuation.md).
The remaining arguments \(c,x\) are in the original regular
real strips. Hence (2) is holomorphic on (3) for every \(N\).

This argument deliberately does not extend to arbitrary lower
total heights. In particular, shifted numerator poles can occur
when \(\Im c=-2\Im x\), outside (3).

For every physical \(c=m/N\in(0,1)\), select the parity
\(\sigma\equiv m/2\pmod1\). Every original \(0\le j\le m\)
appears in (2), and any extra integer \(j=m/2+d\) has either
\(E_N(j/N)=0\) or \(E_N((m-j)/N)=0\). Its other factors
are finite on (3). Therefore
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
The equality includes every physical inner row, both parities,
the exact \(P_m\), and all external \(x\) derivatives.
No off-grid identity with a differently specified interpolant
is asserted.

## 2. The larger phase domain

Let \(\varphi_{\mathrm g}=(1+\sqrt5)/2\), and consider compact
subsets of
\[
 \mathcal K_+=\left\{(c,x)\in\mathcal U:
     \frac12\le\Re c<1,\quad \Im c\ge0,\quad
                          e^{2\pi\Im x}>\varphi_{\mathrm g}\right\}.
 \tag{6}
\]
The original \(x_0\) satisfies this strict radius inequality:
the proved \(e^{2\pi\Im x_0}>163/100\) is sufficient.

[The golden-ratio theorem](research_mixed_two_adjacent_golden_ratio_inner_dominance.md)
proves that the full upper phase of (1), on
\(a=c/2+t\), \(-1/2\le t\le1/2\), has its unique real
maximum at \(t=0\), for every parameter in (6). This
includes its continuous boundary values when an own
argument is a nonpositive real number. Its center is
an actual zero derivative by exact symmetry, and the
real part of the original inner Hessian is strictly
negative.

Consequently the action, Hessian, and nonzero symbol are
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
 \tag{7}
\]
Every midpoint argument is regular. The square root of
\(-\mathcal K\) has positive real part. On a fixed compact
set in (6), this branch and the negative Hessian floor
persist on a sufficiently small open neighborhood.

Fix such a compact set \(K\). Strict global dominance
and continuity give a positive uniform loss for
\(1/5\le|t|\le1/2\). On \(|t|\le1/5\), the arguments
\(a,c-a,a+x,c-a+x\) all lie in fixed compact regular
strips, since \(\Re c\ge1/2\), \(\Re c<1\), and
\(1/6<\Re x<1/4\). There is a uniform quadratic
loss near \(t=0\), and a positive loss on the rest of
this central interval.

Thus the symmetric Gaussian proof can be applied on
the expanded domain. It is not an invocation of the
earlier central theorem outside that theorem's stated
real-part interval.

## 3. Uniform finite bounds through all real own zeros

Only the own reciprocals require an additional domain
check at the lower endpoint \(\Re c=1/2\). On \(K\),
their real parts lie in
\[
                [-1/4,b_K],\qquad b_K<1.
 \tag{8}
\]
The one-sided logarithmic mesh bound proved in section 3
of the full-width theorem is uniform on every bounded
real-height box:
\[
 \sum_{k=1}^m \log|1-e^{-2\pi i(z+k/N)}|
 \le N\int_0^{m/N}\log|1-e^{-2\pi i(z+t)}|\,dt
                                                   +C\log N.
 \tag{9}
\]
It retains exact zero factors. Its proof uses
\(|f'_h(u)|\le\pi|\cot\pi u|\) away from integers and
the integrable logarithmic lower bound on the finitely
many near-zero mesh cells.

For \(\Re z\ge1/8\), use the original regular bound for
\(E_N(z)\). For \(-1/4\le\Re z\le1/8\), use the exact
fixed shift
\[
 m_N=\lfloor N/3\rfloor,\qquad
 E_N(z)=E_N(z+m_N/N)
            \prod_{k=1}^{m_N}(1-e^{-2\pi i(z+k/N)}).
 \tag{10}
\]
For large \(N\), the shifted real parts stay in a fixed
compact subinterval of \((0,1)\). Equations (9)--(10)
therefore give a polynomial-prefactor upper bound for
\(E_N(z)\) through every negative-index zero, uniformly
down to zero height.

Its continuous real rate is
\[
 \mathcal G(z)=\Re g(z+1/3)
       -\int_0^{1/3}\log|1-e^{-2\pi i(z+t)}|\,dt
 \tag{11}
\]
in this low-real-part region, and \(\Re g(z)\) on the
regular overlap. On the upper half-plane and its real
boundary it equals \(\Re g_+(z)\). The same expression
is continuous for small negative heights and for a
small enlargement of the real interval in (8).
The original derivative identity makes (11) independent
of replacing \(1/3\) by \(m_N/N\) in the exact derivation.

All shifted numerator arguments retain uniformly positive
height near \(K\), so their global upper packets remain
uniform even where their real parts are negative or
greater than one. The remaining factors are regular.
Combining these bounds gives a polynomial-prefactor
upper bound for every full-width row, with the original
upper real phase on \(K\). The continuous rate (11)
extends this upper bound to a small open neighborhood.

The strict loss outside \(|t|<1/5\) therefore persists
on some open neighborhood \(U_K\Subset\mathcal U\),
including the points with \(\Re c<1/2\) or \(\Im c<0\)
that are close to the corresponding boundary part of
\(K\). After summing its \(O(N)\) rows, the difference
between the full source (2) and its smaller central
cutoff is exponentially smaller than \(e^{N\Re\Phi}\)
throughout \(U_K\). This step uses only an upper bound
at the zeros, not a nonzero symbol there.

## 4. The complete packet

**Theorem.** For every compact \(K\subset\mathcal K_+\),
there is an open neighborhood \(U_K\Subset\mathcal U\)
such that, uniformly on smaller compact subsets of
that neighborhood,
\[
 \boxed{\quad
 \mathcal B_{\sigma,N}(c,x)
     =N^{-1}\mathcal A(c,x)e^{N\Phi(c,x)}
                                       (1+O(N^{-1})),
             \qquad \sigma\in\{0,1/2\}.
 \quad}
 \tag{12}
\]
Both level parities are included. Every fixed mixed
\(c,x\) derivative of the normalized error is
\(O(N^{-1})\) on a smaller neighborhood.

*Proof.* On the regular central interval, the exact
row has its original packet
\(N^{-3/2}b_c(a;x)e^{NF_c(a;x)}(1+O(N^{-1}))\).
The phase and symbol are even in \(t=a-c/2\).
The strict negative central Hessian from the
golden-ratio theorem gives the centered Gaussian
sum on \(\mathbb Z+\sigma\), with factor
\(\sqrt{2\pi N}/\sqrt{-\mathcal K}\).
The quartic phase and quadratic symbol errors have
relative size \(O(N^{-1})\) by Gaussian moments,
uniformly on \(U_K\) after decreasing it.
Every remaining central row has a fixed or Gaussian
loss by section 2. Section 3 pays every row outside
the central interval, including all zero-extended
rows. The resulting coefficient is exactly (7).

The finite sum and its nonzero normalization are
holomorphic on \(U_K\). Cauchy estimates on nested
bidisks give the normalized mixed derivatives.
This also covers the real-total boundary and the
endpoint \(\Re c=1/2\). \(\square\)

The theorem supplies an exact full-source representative
from the real half-index region to the actual complex
total saddle. Equation (5) is its interface to the
original physical sum. A subsequent outer contour
must still use the appropriate even or odd
representative, retain its spacing \(2/N\), and
control its actual endpoint currents and aliases.
No ordinary normal is replaced by raw differentiation
in \(c\), and no conclusion about the complete outer
signed sum follows from (12) alone.

