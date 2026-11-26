# The finite central packet with two independent Fourier endpoints

Research deduction, 7 November 2026. The exact central finite source
admits a joint holomorphic Gaussian packet when its two Fourier
endpoints vary independently near \(x_0\). Symmetry is used only at
the initial diagonal parameters. The shifted inner critical point
is reached by an actual finite-sum contour identity, with both
parity kernels, both lattice aliases, and every finite side current
retained and bounded.

The proof is uniform on any fixed bounded total-height compact
with \(1/2\le\Re c<1\). It does not evaluate the remaining outer
sum or replace ordinary normal adapters by new derivatives.
No numerical evaluation is used.

## 1. The exact finite source and the moved inner critical point

Use the literal row
\[
\begin{split}
 T_N(a;c,x,y)={}&e^{2\pi iNa(c-a)}
    \Pi_N(c)\Pi_N(a+x)\Pi_N(c-a+y)\\
 &\qquad\cdot E_N(a)^2E_N(c-a)^2E_N(x)E_N(y),
\end{split}
 \tag{1}
\]
with all original scalars and branches. Define
\[
 \mathcal H_{\sigma,N}(c;x,y)=
   \sum_{\substack{d\in\mathbb Z+\sigma\\|d|\le N/5}}
                         T_N(c/2+d/N;c,x,y),
             \qquad \sigma\in\{0,1/2\}.
 \tag{2}
\]
The index sets are fixed independently of every parameter.

Fix a compact set
\[
        K_c\subset\{c:1/2\le\Re c<1\}
 \tag{3}
\]
with bounded imaginary parts. On a sufficiently small open
neighborhood of \(K_c\times\{(x_0,x_0)\}\), every factorial
argument in (1), for \(|d/N|\le1/5\), stays in a fixed
regular strip. The same is true after a sufficiently small
complex displacement of \(d/N\). The finite source is
therefore jointly holomorphic in \(c,x,y\).

In the difference coordinate \(t=a-c/2\), put
\[
\begin{split}
 \mathcal F(t;c,x,y)={}&g(c)+g(c/2+t+x)+g(c/2-t+y)\\
 &-2g(c/2+t)-2g(c/2-t)-g(x)-g(y)\\
 &+2\pi i(c^2/4-t^2),\\
 b(t;c,x,y)={}&
 \frac{\mathfrak a(c)\mathfrak a(c/2+t+x)
                     \mathfrak a(c/2-t+y)}
 {\mathfrak a(x)\mathfrak a(y)
                  \mathfrak a(c/2+t)^2\mathfrak a(c/2-t)^2}.
\end{split}
 \tag{4}
\]
The original row theorem gives
\[
 T_N(c/2+t;c,x,y)=
       N^{-3/2}b(t;c,x,y)e^{N\mathcal F(t;c,x,y)}
                                           (1+O(N^{-1}))
 \tag{5}
\]
on these compact regular complex sets. The symbol is nonzero.

At \(x=y=x_0\), \(t=0\) is an actual critical point, and
[the all-height central theorem](research_mixed_two_adjacent_all_height_central_packet.md)
gives strict global dominance on \(|t|\le1/5\) and
\[
          \Re\mathcal F_{tt}(0;c,x_0,x_0)\le-\mu<0
 \tag{6}
\]
uniformly after a small thickening of \(K_c\).
The uniform implicit-function theorem consequently gives
a unique small holomorphic critical point
\[
 \zeta=\zeta(c,x,y),\qquad
 \mathcal F_t(\zeta;c,x,y)=0,\qquad
 \zeta(c,x_0,x_0)=0 .
 \tag{7}
\]
One may choose one common parameter neighborhood: a uniform
bound on the third derivatives, together with (6), gives a
fixed critical disk and a common parameter radius. Uniqueness
in that disk makes the local implicit branches agree.
In particular \(|\zeta|\le C(|x-x_0|+|y-x_0|)\).

Set
\[
 \begin{split}
 \Phi(c,x,y)&=\mathcal F(\zeta;c,x,y),\\
 \mathcal K(c,x,y)&=\mathcal F_{tt}(\zeta;c,x,y),\\
 \mathcal A(c,x,y)&=
             \frac{\sqrt{2\pi}\,b(\zeta;c,x,y)}
                                   {\sqrt{-\mathcal K(c,x,y)}}.
 \end{split}
 \tag{8}
\]
Shrink the neighborhood so that \(\Re\mathcal K<-\mu/2\).
The square root has positive real part. At \(x=y\) close
to \(x_0\), exact symmetry still gives \(\zeta=0\), and
(8) is the original diagonal normalization.

## 2. Fixed local cuts and uniform reserves

We describe the choice of constants before introducing the
finite contour identity. All are independent of \(N\) and
of \(\sigma\).

Choose a small fixed \(\epsilon\in(0,1/10)\). By (6), it
can be chosen so that a fixed complex neighborhood of
\(|\Re t|\le2\epsilon\) has uniformly bounded derivatives,
and \(|\Im\mathcal F_t|<\pi\) there after the parameter
neighborhood is decreased. At diagonal parameters, the
real central segment has a quadratic loss and every
\(\epsilon/2\le|t|\le1/5\) has a positive fixed loss.

Next choose a fixed \(\eta>0\), sufficiently small relative
to this endpoint loss and with \(\eta<\epsilon/4\).
Continuity ensures that the diagonal phase remains below
its central value by a fixed positive amount on both end strips
\(3\epsilon/4\le|\Re t|\le5\epsilon/4\),
\(|\Im t|\le\eta\). Finally shrink the independent
\(x,y\) neighborhood so that:
\[
\begin{gathered}
 |\zeta|<\min(\epsilon/8,\eta/4),\\
 \sup_{|t|\le3\epsilon/2,\ t\in\mathbb R}
     \{\Re\mathcal F(t;c,x,y)-\Re\Phi(c,x,y)\}
                                       <\pi\eta/4 .
\end{gathered}
 \tag{9}
\]
The derivative bound \(|\Im\mathcal F_t|<\pi\) remains
valid on the needed rectangle. The fixed losses on the
two vertical end strips and on the complementary real
interval \(\epsilon/2\le|t|\le1/5\), measured against
\(\Re\Phi(c,x,y)\), also persist. The same bounds hold on
a small open \(c\)-neighborhood of \(K_c\).

For large \(N\), let \(D_{\sigma,N}\) be the largest
nonnegative \(d\in\mathbb Z+\sigma\) with \(d\le N\epsilon\),
and put
\[
                         b_{\sigma,N}
                          =\frac{D_{\sigma,N}+1/2}{N}.
 \tag{10}
\]
Then \(b_{\sigma,N}=\epsilon+O(1/N)\). The cuts
\(\pm b_{\sigma,N}\) are half-grid cuts for the
\(\sigma\)-lattice. For large \(N\),
\(|b_{\sigma,N}-\epsilon|<\epsilon/8\), so each translated
endpoint segment in (16) stays in the paid end strips above.
The omitted terms of (2) satisfy,
by their actual regular row estimates and the real
phase loss just fixed,
\[
 \sum_{\substack{d\in\mathbb Z+\sigma\\
                       N\epsilon<|d|\le N/5}}
   |T_N(c/2+d/N;c,x,y)|
       \le C e^{N(\Re\Phi(c,x,y)-\gamma_0)}
 \tag{11}
\]
for a common \(\gamma_0>0\), after absorbing a polynomial
factor and decreasing the fixed gap. These are literal
terms of the original central source; no contour argument
has been applied to them.

## 3. The exact parity contour and all its corrections

Abbreviate
\[
 \begin{split}
 \mathcal T_N(t)&=T_N(c/2+t;c,x,y),\qquad b=b_{\sigma,N},\\
 k_{\sigma,N}(t)&=
                \frac1{1-e^{-2\pi i(Nt-\sigma)}},\\
 w_{N,0}(v)&=\frac1{1+e^{2\pi Nv}}-\boldsymbol1_{\{v<0\}}.
 \end{split}
 \tag{12}
\]
The kernel has residue \(1/(2\pi iN)\) at every retained
lattice point \(t=d/N\). On either side cut,
\(k_{\sigma,N}(\pm b+iv)=(1+e^{2\pi Nv})^{-1}\).
The residue theorem on the rectangle with horizontal
heights \(\pm\eta\), followed only by Cauchy's theorem
for the zero mode, gives the exact identity
\[
\begin{split}
 \sum_{\substack{d\in\mathbb Z+\sigma\\|d|\le N\epsilon}}
                       \mathcal T_N(d/N)
 ={}&N\int_{-b}^{b}\mathcal T_N(t)\,dt\\
 &+N\int_{-b-i\eta}^{b-i\eta}
                     (k_{\sigma,N}(t)-1)\mathcal T_N(t)\,dt\\
 &-N\int_{-b+i\eta}^{b+i\eta}
                            k_{\sigma,N}(t)\mathcal T_N(t)\,dt\\
 &+iN\int_{-\eta}^{\eta}w_{N,0}(v)
                  \{\mathcal T_N(b+iv)-\mathcal T_N(-b+iv)\}\,dv.
\end{split}
 \tag{13}
\]
The orientation of both displayed horizontal alias integrals
is left to right. All parity phases remain inside
\(k_{\sigma,N}\); the principal density is exactly \(N\).

For large \(N\), the two horizontal kernel bounds are
\[
 |k_{\sigma,N}(t)-1|\le2e^{-2\pi N\eta}
       \quad(\Im t=-\eta),\qquad
 |k_{\sigma,N}(t)|\le2e^{-2\pi N\eta}
       \quad(\Im t=\eta).
 \tag{14}
\]
By (9) and vertical integration of
\(|\Im\mathcal F_t|<\pi\),
\[
 \Re\mathcal F(u\pm i\eta;c,x,y)
          <\Re\Phi(c,x,y)+5\pi\eta/4,\qquad |u|\le b.
 \tag{15}
\]
Thus each actual horizontal alias in (13) has an
exponential reserve, for example \(\pi\eta/2\) after
absorbing fixed powers of \(N\).
The last current in (13) has its separate endpoint
phase loss, since \(|w_{N,0}|\le1\) and the whole
two vertical end strips were retained in section 2.
It too is exponentially smaller than \(e^{N\Re\Phi}\).
No alias or endpoint term in (13) is omitted without
such a bound.

## 4. The translated main path and its Gaussian

The row is holomorphic throughout the small strip used
above. The exact finite-path translation is
\[
 \begin{split}
 \int_{-b}^{b}\mathcal T_N(t)\,dt
  ={}&\int_{-b+\zeta}^{b+\zeta}\mathcal T_N(t)\,dt\\
    &+\int_{-b}^{-b+\zeta}\mathcal T_N(t)\,dt
             -\int_b^{b+\zeta}\mathcal T_N(t)\,dt .
 \end{split}
 \tag{16}
\]
Both connector segments stay in the paid endpoint strips
by (9). They therefore retain a fixed phase loss. The
translated main path now passes through the actual
moved critical point, at its real coordinate \(t-\zeta=0\).

Combining (11), (13)--(16) gives, for a fixed \(\gamma>0\),
\[
 \mathcal H_{\sigma,N}(c;x,y)
    =N\int_{-b+\zeta}^{b+\zeta}\mathcal T_N(t)\,dt
             +O(e^{N(\Re\Phi(c,x,y)-\gamma)}).
 \tag{17}
\]
This is an estimate for the original exact finite source,
with all four types of corrections identified.

On \(t=\zeta+u\), \(u\in[-b,b]\), the phase has negative
real quadratic part at zero. Its local dominance and the
strict loss on the rest of the segment persist from the
diagonal case by (6), compactness, and the small chosen
parameter neighborhood. The original one-dimensional
Gaussian formula and (5) therefore give
\[
 N\int_{-b+\zeta}^{b+\zeta}\mathcal T_N(t)\,dt
     =N^{-1}\mathcal A(c,x,y)e^{N\Phi(c,x,y)}
                                                (1+O(N^{-1})).
 \tag{18}
\]
The moved phase and symbol need not be even. Nevertheless,
the \(N^{-1/2}\) terms from the cubic phase and linear
symbol are odd after the \(N^{-1/2}\) rescaling on the
symmetric \(u\)-interval. Their integrals vanish. Uniform
quartic and higher bounds then give the stated relative
\(O(N^{-1})\) error.

## 5. Joint packet and its original interface

**Theorem.** For every \(K_c\) in (3), there is a fixed
open parameter neighborhood of
\(K_c\times\{(x_0,x_0)\}\) on which the exact finite
source (2) has
\[
 \boxed{\quad
 \mathcal H_{\sigma,N}(c;x,y)
    =N^{-1}\mathcal A(c,x,y)e^{N\Phi(c,x,y)}
                                               (1+O(N^{-1})),
       \qquad \sigma\in\{0,1/2\}.
 \quad}
 \tag{19}
\]
The estimate is uniform on smaller compact sets, for
both level parities. All fixed mixed \(c,x,y\) derivatives
of the normalized error are \(O(N^{-1})\).

The nonzero coefficient and phase are the original
ones in (8). The derivative assertion follows from
the exact source's holomorphy and nested Cauchy
estimates after (17)--(18); it is not inferred from
an identity on \(x=y\).

At a physical \(c=m/N\in[1/2,1)\), with the correct
parity \(\sigma\equiv m/2\pmod1\), the exact source is
\[
 \mathcal H_{\sigma,N}(m/N;x,y)
  =P_m\sum_{\substack{0\le j\le m\\|j-m/2|\le N/5}}
       \frac{r^{-j(m-j)}p_j(e^{-2\pi ix})
                         p_{m-j}(e^{-2\pi iy})}
                              {P_j^2P_{m-j}^2}.
 \tag{20}
\]
Thus its two independent Fourier parameters are genuine
free parameters of the literal central source. The
complete physical source still retains its other rows
until their original absolute error bounds have been
continued and applied. Likewise, (19) supplies no
estimate at infinite total height: the complete outer
contour must retain its exact finite-level tails and
its own corrections. The original outside scalar
is \(e^{\pi i(N-1)(x+y)}\).

Finally, (19) gives raw analytic derivatives in the
Fourier parameters of this exact finite source.
It does not identify arbitrary ordinary normal
or closing adapters with those derivatives, and
does not itself prove the complete adjacent-pair
asymptotic off the diagonal.

