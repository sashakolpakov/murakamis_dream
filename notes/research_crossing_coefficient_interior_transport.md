# The actual coefficient branch before it reaches the unit circle

Written research proof, 22 November 2026.

The initialized coefficient asymptotic extends from a small fixed
fraction of the indices to the whole interval \(0<t<(h+k)/2\).
One root of its exact characteristic quadratic lies inside the
unit circle and the other outside. The canonical amplitude
satisfies the discrete transport equation, and a stable difference
estimate propagates the actual source with relative error \(O(N^{-1})\).

## 1. The original scalar and the theorem

Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 p=e^{-2\pi i/N},\quad \omega=2\pi i,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2}.
 \tag{1}
\]
Use the full centered basis with
\(\phi(f_if_j)=\delta_{ij}\) and \(U_t=\sum_{j=0}^d t^jf_j\).
The coefficients studied here are those of the actual scalar
\[
 \Phi_N(C,H,K)=\phi(f_0U_{-C}U_{-H}U_{-K})
             =\sum_{n=0}^dc_{n,N}(H,K)C^n,\qquad
 H=e^{-2\pi ih},\quad K=e^{-2\pi ik}.
 \tag{2}
\]
In particular \(c_{n,N}=(-1)^n(x_N)_n\) for the original output
\(x_N=f_0U_{-H}U_{-K}\); no distinct-root quotient is taken.
Write
\[
 \begin{split}
 J(u)&=\int_0^u\log|2\sin\pi v|\,dv,\\
 V(h,k)&=J(h+k)-2J(h)-2J(k),\\
 \Omega&=\{h,k>0:\ h+k<1,\ V(h,k)>0\},\\
 \mathcal I&=\{(h,k,t): (h,k)\in\Omega,\ 0<t<(h+k)/2\}.
 \end{split}
 \tag{3}
\]
The specified canonical origin factor is
\[
 \Gamma_{0,N}(h,k)=\frac{\kappa^2}{N^2}
 \frac{\mathfrak F_N(N(1-h)-1/2)^2
       \mathfrak F_N(N(1-k)-1/2)^2}
      {\mathfrak F_N(N(1-h-k))}.
 \tag{4}
\]
All factorial and square-root marks are inherited from [O,S].

Define by power series at zero
\[
 \begin{split}
 a(C)&=-\frac{2\operatorname{Li}_2(C)
           -\operatorname{Li}_2(HC)-\operatorname{Li}_2(KC)}
           {\omega},\\
 \alpha(C)&=[(1-HC)(1-KC)]^{-1/2},\qquad \alpha(0)=1 .
 \end{split}
 \tag{5}
\]
The branch \(C_t\), initially
\[
 C_ta'(C_t)=t,\qquad
 C_t=\frac{t}{z}+O(t^2),\qquad
 z=\frac{2-H-K}{-\omega},
 \tag{6}
\]
continues throughout \(\mathcal I\). Set
\[
 \beta_t=C_ta'(C_t)+C_t^2a''(C_t),\qquad
 S(t)=a(C_t)-t\Log C_t .
 \tag{7}
\]
The logarithm is continued from (6), and
\(\sqrt{\beta_t}=\sqrt t\,\sqrt{\beta_t/t}\) is continued
from \(\beta_t/t=1\) at zero.

**Theorem.** On every compact subset of \(\mathcal I\), uniformly
for all physical integers \(n,N\) with \(t=n/N\),
\[
 \boxed{\quad
 c_{n,N}(H,K)=
 \Gamma_{0,N}(h,k)
 \frac{\alpha(C_t)e^{NS(t)}}{\sqrt{2\pi N\beta_t}}
                         (1+O(N^{-1})).
 \quad}
 \tag{8}
\]
The estimate persists on a fixed small complex neighborhood in
\(h,k\) of that compact parameter family, and fixed \(h,k\)
derivatives of its normalized error are \(O(N^{-1})\) on a
smaller neighborhood. The third coordinate is the actual index
\(t=n/N\); no analytic continuation of that index is asserted.
The original coefficients are nonzero there for all sufficiently
large integer levels, both parities and composite levels.

On real compact subsets of \(\mathcal I\), the corresponding rate is
\[
 \log|c_{n,N}|=
 N\{V(h,k)+\Re a(C_t)-t\log|C_t|\}+O(\log N).
 \tag{9}
\]
The positivity assumption \(V>0\) is used to initialize the actual
source. The algebraic root separation below holds more broadly,
but does not by itself extend this source theorem to \(V\le0\).

## 2. The root inside the disc is separated from the other root

Let \(R=h+k<1\), initially with real \(h,k>0\), and put
\[
 B(C)=\frac{(1-HC)(1-KC)}{(1-C)^2},\qquad
 T=e^{-\omega t}.
 \tag{10}
\]
Equation (6) has the precise logarithmic form
\(\Log B(C_t)=-\omega t\), continued from zero.
Its quadratic is
\[
 (HK-T)C^2+(2T-H-K)C+1-T=0 .
 \tag{11}
\]

There is a useful global disc calculation. Put
\[
 w=\frac{1+C}{1-C},\quad
 A=\frac{\cot\pi h+\cot\pi k}{2},\quad
 D=\frac{\cot\pi h-\cot\pi k}{2},\quad
 s=\sin\pi h\sin\pi k>0 .
 \]
Direct substitution gives
\[
             e^{\pi iR}B(C)
                 =-s\{(w-iA)^2+D^2\}.
 \tag{12}
\]
The map \(C\mapsto w\) sends the unit disc to \(\Re w>0\).
Translation by \(-iA\) preserves that half-plane. Squaring
maps it bijectively onto the plane cut along the nonpositive
real axis. Thus (12) maps the disc conformally onto
\[
       \mathbb C\setminus
               e^{-\pi iR}[-sD^2,\infty).
 \tag{13}
\]
For \(0<t<R/2\), the rotated target
\(e^{\pi iR}T=e^{\pi i(R-2t)}\) lies strictly in the upper
half-plane. It has exactly one preimage \(C_t\) in the disc.
This is (6)'s branch by continuation.

The quadratic has degree two, since \(HK\ne T\) on this
interval. Its other root \(C_t^{\rm out}\) is finite.
No root is on the unit circle: there \(w\) is imaginary,
and (12) is real, while the rotated target is not.
The roots are distinct, because the conformal map has
nonzero derivative at its interior preimage.
Consequently
\[
 |C_t|<1<|C_t^{\rm out}|,\qquad
 \lambda_t=C_t^{-1},\quad \mu_t=(C_t^{\rm out})^{-1},
 \qquad |\lambda_t|>1>|\mu_t|.
 \tag{14}
\]
Neither root is zero, since \(T\ne1\).
Also
\[
                  \beta_t=-\frac{C_tB'(C_t)}{\omega B(C_t)}
                            \ne0 .
 \tag{15}
\]
All root and denominator separations are uniform on compact
subsets of the stated interval. They persist on small fixed
complex parameter neighborhoods. The branches in (5)--(7)
are fixed by continuation from their small-\(t\) values.
On these buffered domains the logarithms, square roots,
and their derivatives are bounded wherever used.
In particular no assumption \(\Re\beta_t>0\) is needed
away from the initial coefficient-circle domain.

## 3. The exact finite recurrence and its half-steps

The exact source equation [D, equation (10)], modulo \(C^N\), is
\[
 (1-C/q)^2\Phi_N(pC)-(1-HC)(1-KC)\Phi_N(C)=Cj_{0,N}.
 \tag{16}
\]
Here \(j_{0,N}=\eta(2+H^N+K^N)/N\).
For \(2\le n<N\), its coefficient of \(C^n\) is exactly
\[
 (p^n-1)c_{n,N}
 =(2q^{-1}p^{n-1}-H-K)c_{n-1,N}
                    +(HK-p^{n-1})c_{n-2,N}.
 \tag{17}
\]
Only the coefficient at \(n=1\) has the separate source
term. Every denominator \(p^n-1\) in (17) is nonzero,
including at composite levels.

Set \(\epsilon=N^{-1}\), \(T=e^{-\omega t}=p^n\). Then
\[
 c_n=a_\epsilon(t)c_{n-1}+b_\epsilon(t)c_{n-2},\qquad
 a_\epsilon=\frac{2Te^{\omega\epsilon/2}-H-K}{T-1},
 \quad b_\epsilon=\frac{HK-Te^{\omega\epsilon}}{T-1}.
 \tag{18}
\]
The subscript \(N\) is suppressed here. On compact domains
with \(t>0\),
\[
 a_\epsilon=a_0+\epsilon a_1+O(\epsilon^2),\quad
 b_\epsilon=b_0+\epsilon b_1+O(\epsilon^2),\quad
 a_1=\frac{\omega T}{T-1},\quad b_1=-a_1 .
 \tag{19}
\]
The \(q\) half-step in the first numerator is essential.
The roots of \(\lambda^2-a_0\lambda-b_0=0\) are exactly
the \(\lambda_t,\mu_t\) in (14).

## 4. The canonical amplitude has residual \(O(\epsilon^2)\)

Let
\[
 W_n=\Gamma_{0,N}
       \frac{\alpha(C_t)e^{NS(t)}}{\sqrt{2\pi N\beta_t}},
 \qquad \ell(t)=\log\{\alpha(C_t)/\sqrt{\beta_t}\}.
 \tag{20}
\]
Differentiating the saddle equation gives
\[
                 S'(t)=-\Log C_t,\qquad S''(t)=-1/\beta_t.
 \tag{21}
\]
For \(C=C_t\), put \(A_0=a_0C\), \(B_0=b_0C^2\), and
\(\mathcal D=A_0+2B_0\). The characteristic equation
gives \(A_0+B_0=1\).
Taylor expansion in \(t\) gives uniformly on buffered compacts
\[
 \begin{split}
 W_{n-1}/W_n
   &=C[1+\epsilon(S''/2-\ell')+O(\epsilon^2)],\\
 W_{n-2}/W_n
   &=C^2[1+\epsilon(2S''-2\ell')+O(\epsilon^2)].
 \end{split}
 \tag{22}
\]
The first-order transport condition is therefore
\[
 \ell'=\frac{a_1C+b_1C^2+(A_0/2+2B_0)S''}{\mathcal D}.
 \tag{23}
\]
We verify this condition explicitly for the specified amplitude.

Use the auxiliary polynomials
\[
 \begin{split}
 \sigma&=H+K,\quad u=HK,\quad E=1-C,\quad
 P=1-\sigma C+uC^2,\\
 L&=2-\sigma+(u-1)C,\qquad
 M=u-1+(\sigma-2u)C,\qquad
 K_0=2-\sigma+(2u-\sigma)C .
 \end{split}
 \]
Substituting \(T=P/E^2\) gives
\[
 T-1=CL/E^2,\quad B_0=CM/L,\quad
 \mathcal D=EK_0/L,\quad
 \beta=-CK_0/(\omega EP),\quad
 \frac{\alpha^2}{\beta}=-\frac{\omega E}{CK_0}.
 \tag{24}
\]
All displayed denominators are nonzero on the selected branch.
For example \(T-1,C,E,P\) are nonzero, and (15) gives
\(K_0\ne0\); then the other assertions follow.
Primes on these auxiliary polynomials denote \(C\)-derivatives;
\(\ell'\) remains a \(t\)-derivative.
Taking a logarithmic derivative of the last expression yields
\[
       2\beta\ell'=-1-C/E-CK_0'/K_0 .
 \tag{25}
\]
Two elementary identities complete the check:
\[
 EK_0'=K_0+2M,\qquad
 \frac{\beta a_1CE}{\mathcal D}=-C/E,\qquad
 \frac{CK_0'}{K_0}=C/E+\frac{2B_0}{\mathcal D}.
 \tag{26}
\]
The third follows from the first and (24).
Since \(b_1=-a_1\), \(S''=-1/\beta\),
\(A_0/2+2B_0=(1+3B_0)/2\), and
\(\mathcal D=1+B_0\), twice \(\beta\) times the right
side of (23) is
\[
 -2C/E-\frac{1+3B_0}{\mathcal D}
   =-1-2C/E-\frac{2B_0}{\mathcal D}
   =-1-C/E-CK_0'/K_0 .
 \]
This is (25), proving the exact transport identity.
The identity concerns the derivative of the amplitude;
its multiplicative constant and square-root sign remain
those fixed by the actual source initialization.

Equations (18)--(23) now show
\[
 \rho_n:=
 \frac{W_n-a_\epsilon(t)W_{n-1}
                   -b_\epsilon(t)W_{n-2}}{W_n}
                           =O(\epsilon^2)
 \tag{27}
\]
uniformly on every buffered compact subset of \(\mathcal I\).

## 5. Stable comparison with the initialized actual source

Fix a compact \(\mathcal K\subset\mathcal I\).
Choose a fixed positive \(t_s\) so small that the source theorem
[S] applies at indices near \(Nt_s\) for every projected
\((h,k)\), and \(t_s<\tfrac12\min_{\mathcal K}t\).
The union of the segments from \(t_s/2\) to each target \(t\),
with its \(h,k\) fixed, is a compact subset of \(\mathcal I\).
All previous estimates hold on a fixed buffered neighborhood
of this union.

Take \(n_s=\lfloor Nt_s\rfloor\).
At the two consecutive indices \(n_s-1,n_s\), [S] gives
\[
          c_{n_s-1}/W_{n_s-1}=1+O(\epsilon),\qquad
          c_{n_s}/W_{n_s}=1+O(\epsilon).
 \tag{28}
\]
The phase and square-root markings in (20) were chosen to
be exactly those of this initialization.

No actual coefficient is divided by in the subsequent argument.
Put
\[
 y_n=c_n/W_n,\qquad d_n=y_n-y_{n-1},\qquad
 \widetilde b_n=b_\epsilon(t)W_{n-2}/W_n .
 \tag{29}
\]
The trial coefficients \(W_n\) are nonzero by construction.
Equations (18) and (27) give the exact identity
\[
                 d_n=-\widetilde b_n d_{n-1}
                                 -\rho_n y_{n-1}.
 \tag{30}
\]
On the buffered path set,
\[
 \widetilde b_n=b_0C_t^2+O(\epsilon)
                  =-\mu_t/\lambda_t+O(\epsilon).
 \]
The strict gap in (14) therefore gives
\(|\widetilde b_n|\le r<1\) uniformly for large \(N\),
including on a smaller fixed complex parameter neighborhood.

Iterate (30) and sum its geometric bound. With
\(Y_m=\max_{n_s-1\le j\le m}|y_j|\) and at most \(N\) steps,
(27)--(28) give
\[
 \begin{split}
 \sum_{j=n_s+1}^{m}|d_j|
 &\le \frac{r}{1-r}|d_{n_s}|
       +\frac{C\epsilon^2(m-n_s)}{1-r}Y_m\\
 &\le C\epsilon+C\epsilon Y_m,\\
 \max_{n_s-1\le j\le m}|y_j-1|
 &\le C\epsilon+C\epsilon Y_m .
 \end{split}
 \tag{31}
\]
It follows first that \(Y_m\le2\) for sufficiently large \(N\),
after increasing harmless constants, and then
\(\max|y_j-1|\le C\epsilon\).
This proves (8) and the asserted nonvanishing.
The proof is valid for the original finite recurrence;
it neither assigns a coefficient to an uninitialized branch
nor divides by an unproved nonzero \(c_n\).

The same estimates hold on a fixed larger complex neighborhood
of the real compact path set. Cauchy's formula on a smaller
neighborhood proves the fixed \(h,k\)-jet assertion for the
normalized error. These are external coherent-parameter
derivatives, not an additional ordinary main-color continuation.
Finally [O] gives
\(\log|\Gamma_{0,N}|=NV(h,k)+O(\log N)\);
the remaining amplitudes are bounded above and away from
zero on the compact set. This proves (9).

## Complete proof sources and scope

All three complete matching proof texts were read:

| Label | Complete source | SHA-256 |
|---|---|---|
| S | [Initialized coefficient source, 391 lines](research_crossing_linear_head_coefficient_source.md) | 125d13d37424b9fac28cbd754f3393cab0a59042275adbe9308abb3ffa593e56 |
| D | [Exact source on a fixed disc, 288 lines](research_crossing_origin_disc_normalization.md) | 821bcc32af228845e93b2b8dcf91ea3c9f10226cfb1df75ecea90c68ab4e0ae8 |
| O | [Origin normalization and rate, 385 lines](research_crossing_origin_fourier_normalization.md) | 6a516e08422f1645b6bea4281662b4c6db1465114de8eed610fb775607e6d3c8 |

The proof propagates a proved actual source, rather than
postulating selection of a characteristic root.
The root separation is lost as the selected root reaches
the unit circle; this is not claimed to be a collision of
the two roots. No assertion is made at or beyond \(t=R/2\).
The physical coordinate count remains of order \(N\), and
the result is not a bound for the fixed degree of a
variational objective.

The original scalar, sign \(c_{n,N}=(-1)^n(x_N)_n\),
all \(N\) ambient coordinates and all Hermite directions
remain specified. No arbitrary signed crossing/turn word,
general Conway gluing, original full-cap lower bound,
filled-knot volume or finite-exception theorem follows.

Only written mathematics and text/hash inspection were used.
No program, numerical experiment, test, build, git action
or earlier-final file edit was performed.
