# Transferring the proved inner currents to two shortened edges

Private finite-source transfer theorem, 8 November 2026.
No mathematical numerical evaluation or frozen-source edit is used.

The trace-level first-edge deletion leaves a source with both
edge sums ending at \(U=\lfloor N/2\rfloor-1\). This note proves
which previous contour estimates remain valid for that actual
source. The center, positive partial Gaussian, far negative
segment, removed real samples, and complete endpoint verticals
are retained. The negative middle arc and the two connections
to the far angular endpoints remain unestimated.

## 1. Exact source and trace

Use the original notation
\[
 \begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad
 \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\quad
 m=\lfloor N/2\rfloor,\quad U=m-1,\\
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),\qquad
 K_N^<(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 f_N(t,u)=K_N(t,0)K_N^<(t,u),\qquad
 f_N^{<<}(t,u)=K_N^<(t,0)K_N^<(t,u),\\
 g_N^{<<}(t,u)=\sin t\,f_N^{<<}(t,u)e^{3iNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
 \end{gathered}                                                     \tag{1}
\]
Let \(Q_N\) and \(Q_N^{<<}\) be the original full Hermite
traces of \(R_N^3f_N\) and \(R_N^3f_N^{<<}\), respectively.
The [first-edge tail contraction](research_mixed_next_inner_three_first_edge_tail_contraction.md)
has proved on the actual family
\[
 \begin{gathered}
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},\\
 t_*(u)=a_*(u)-iH(u),\quad 0<a_*<\pi/2,\quad1/2<H<1,\\
 S(u)=\Phi(t_*(u),u),\quad
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,\\
 Q_N(u)=Q_N^{<<}(u)
                       +O(e^{N(\Re S(u)-1/300)}).
 \end{gathered}                                                     \tag{2}
\]
The last line is a trace-level comparison. It will not be
used as a pointwise bound on any angular path.

The new product is an ordinary spectral polynomial:
\[
 f_N^{<<}(t,u)=F_N^{<<}(-2\cos t,u),\qquad
                    \deg_x F_N^{<<}(x,u)\le 2U<N.
                                                                    \tag{3}
\]
Both finite sums and every original trace normal remain
present in \(Q_N^{<<}\).

## 2. A separate pointwise comparison on the eligible angular box

Define the literal complete-end tail
\[
                    \mathcal T_N(t)=K_N(t,0)-K_N^<(t,0).
                                                                    \tag{4}
\]
On a fixed bounded-height angular strip its two parity
descriptions are
\[
 \begin{cases}
 \mathcal T_N(t)=\displaystyle\sum_{r=0}^{m-1}
       e_{D-r}(-2\cos t)e_{D-r}(-2),&N=2m,\\[2mm]
 \mathcal T_N(t)=e_m(-2\cos t),&N=2m+1.
 \end{cases}                                                       \tag{5}
\]
The odd identity includes \(e_m(-2)=1\); all higher
complete-end coefficients vanish exactly.

The even formula is bounded by
\[
 |\mathcal T_N(t)|\le N^2 e^{D|\Im t|}
                                                                    \tag{6}
\]
using [the original radical Fourier estimate, Section 7](research_high_newton_radical_contraction.md).
The odd half-index estimate proved directly from the
zero-safe finite product in
[the far-negative source, equations (11)--(13)](research_mixed_next_inner_three_far_negative_source.md)
gives
\[
 |\mathcal T_N(t)|\le C N^A e^{N|\Im t|/2}.
                                                                    \tag{7}
\]
The proof of (7) is uniform on any fixed bounded-height
strip, including a small neighborhood of the present box:
its entropy at \(1/2\) is \(|\Im t|/2\), and the odd
half-index displacement costs only \(O(\log N)\).

On
\[
                |\Re t|\le\pi/2,\qquad|\Im t|\le1,
                                                                    \tag{8}
\]
[complete-edge gap, Theorem 2 and Corollary 3](research_internal_pair_complete_edge_gap.md)
and the exact evenness and real-coefficient Schwarz symmetries
give a nonzero full kernel with logarithmic rate satisfying
\[
                 \Re\psi(t,0)>|\Im t|+1/500.
                                                                    \tag{9}
\]
Here \(\psi(t,0)\) on the signed box is the same calibrated
primitive, as recorded in
[negative-horizontal phase, Section 1](research_mixed_next_inner_three_negative_horizontal_phase.md).
The normalized full-kernel logarithm costs \(O(\log N)\).
These source statements hold on fixed neighborhoods, and
the strict gap survives after their size is decreased.

Equations (6)--(9) therefore imply, for some fixed \(c>0\),
\[
 \boxed{\quad
 K_N^<(t,0)=K_N(t,0)(1+\epsilon_N(t)),\qquad
 |\epsilon_N(t)|\le C e^{-cN}
 \quad}                                                           \tag{10}
\]
uniformly on a fixed smaller neighborhood of (8).
Every fixed derivative of \(\epsilon_N\) has the same
conclusion on further smaller neighborhoods, by Cauchy's
formula. For example the neighborhoods and the exponent
may be chosen so that \(c=1/2000\). No version of (10)
outside the stated angular box is used below.

Consequently on (8)
\[
                    f_N^{<<}(t,u)=(1+\epsilon_N(t))f_N(t,u)
                                                                    \tag{11}
\]
for every \(u\), including zeros of the second factor.
No division by that factor is involved.

## 3. Center and positive partial current

Take the fixed \(\eta>0,\epsilon_c>0\) from
[the center bridge](research_mixed_next_inner_three_center_bridge.md).
Its choices give
\(\eta<\tfrac12\min_{\mathcal U_+}a_*(u)\).
Then the new exact source satisfies
\[
 \frac{N^2}{\pi}\int_{-\eta}^{\eta}
 |g_N^{<<}(a-iH(u),u)W_N(a-iH(u))|\,da
                 \le C e^{N(\Re S(u)-\epsilon_c)}.
                                                                    \tag{12}
\]
One proof is the pointwise identity (11) on the entire
center interval. The underlying finite polynomial argument
also transfers directly, which checks that no new degree
assumption is hidden here. With \(x=\tan(a/2)\),
\[
 (1+x^2)^{2U}
 F_N^{<<}\left(
 -2\frac{\cosh H(1-x^2)+2i\sinh H\,x}{1+x^2},u\right)
                                                                    \tag{13}
\]
is a polynomial of degree at most \(4U<2N\).
The positive input interval in that source has the same
finite bound by (10) and the original positive-horizontal
packet. Its clearing-factor cost is at most
\(N\log(1+x_A^2)\), and its Chebyshev cost at most
\(2N\rho_\eta\). Both are smaller than the original
\((3N/2)\log(1+x_A^2)\) and \(3N\rho_\eta\).
The same fixed choices of \(A,\eta,\epsilon_c\), with the
exact denominator restored, thus prove (12).

Define the literal new partial current
\[
 \mathcal P_N^{<<}(u)=
 -\frac{N^2C_{N,3}}{\pi i}
   \int_{-\eta-iH(u)}^{\pi/2-iH(u)}
                  g_N^{<<}(t,u)W_N(t)\,dt .
                                                                    \tag{14}
\]
It has the same original Gaussian asymptotic:
\[
 \boxed{\quad
 \mathcal P_N^{<<}(u)=C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                                     (1+O(N^{-1})),
 \quad}                                                           \tag{15}
\]
\[
 \mathcal A(u)=\frac{i\sqrt{2\pi}}{\pi}
     \frac{\sin t_*(u)\,a_e(t_*(u),0)a_e(t_*(u),u)}
                       {\sqrt{-\Phi_{tt}(t_*(u),u)}}\ne0 .
                                                                    \tag{16}
\]
The root is the original left-to-right Gaussian root with
positive real part. This is exactly the coefficient in
[the original partial-horizontal theorem](research_mixed_next_inner_three_partial_horizontal_packet.md).

Here is the finite-source justification of its transfer.
On \(\eta\le a\le\pi/2\), the positive-horizontal packet
and complete first-edge source give
\[
 |f_N^{<<}(a-iH,u)|\le C N^A
      e^{N\Re\{\psi(a-iH,0)+\psi(a-iH,u)\}},
                                                                    \tag{17}
\]
by (10). Actual horizontal concavity gives the same
strict remote loss
\((a-a_*)^2/(8\pi)\). The exact denominator satisfies
\[
 W_N(a-iH)=e^{-iN(a-iH)}(1+O(e^{-NH_0})),
             \qquad H_0=\min_{\mathcal U_+}H>1/2,
                                                                    \tag{18}
\]
so all higher angular charges are still paid using (17).
Near \(t_*(u)\), the first complete-edge packet multiplied
by (10) has the same \(N^{-3/2}\) symbol \(a_e(t,0)\)
and normalized \(O(N^{-1})\) error, with fixed local
derivative control. The second packet is unchanged.
The nondegenerate angular Gaussian therefore has factor
\[
            N^{-3}N^{-1/2}N^2=N^{-3/2},\qquad
                         -1/(\pi i)=i/\pi ,
                                                                    \tag{19}
\]
and yields (15)--(16). The center is paid by (12).
Equivalently, (11), (17) and the center bound show that
the change of the whole old partial current is
exponentially smaller than its nonzero leading term.
No derivative assertion for the current's real-valued
moving height is made.

## 4. Far negative horizontal

The entire interval \(t=-a-iH(u)\), \(5\pi/12\le a\le\pi/2\),
lies in (8). The pointwise comparison (11) therefore
transfers [the complete far-negative source theorem](research_mixed_next_inner_three_far_negative_source.md)
without a new loss:
\[
 \begin{split}
 &\sup_{5\pi/12\le a\le\pi/2}
       |g_N^{<<}(-a-iH,u)W_N(-a-iH)|\\
 &\quad+
 \frac{N^2}{\pi}\int_{5\pi/12}^{\pi/2}
       |g_N^{<<}(-a-iH,u)W_N(-a-iH)|\,da
               \le C e^{N(\Re S(u)-1/10)} .
 \end{split}                                                       \tag{20}
\]
In particular this includes the endpoint \(a=\pi/2\).
The original proof's degree-\(U\) outside continuation is
unchanged. If its final first-variable continuation is
repeated with this source, the clearing polynomial has
degree at most \(4U<2N\), so its old \(3N\rho_R\) budget
also remains valid. No mixed-height saddle packet is used.

## 5. Removed real samples and complete endpoint verticals

These endpoints lie outside (8), so (10) is not invoked
there. Instead apply the original finite Newton bounds
term by term to the two sums, now both \(0\le j\le U\).
With the exact cutoffs of
[the complete inner boundary theorem](research_mixed_next_inner_three_far_samples_and_verticals.md),
\[
 a_F=\pi-\frac{\pi}{2000},\quad
 m_N=\lfloor N/4000\rfloor,\quad
 T_N=\pi-\frac{2\pi m_N}{N},\quad
 \tau_j=\frac{2\pi}{N}(D/2-j),
                                                                    \tag{21}
\]
the real source still obeys
\[
 \sup_{a_F\le|\theta|\le\pi}|f_N^{<<}(\theta,u)|
       \le C N^A e^{NE_{\rm far}},\qquad
 E_{\rm far}=b_2+\frac23+\frac1{1000}
                           <\frac{18763}{15000}.
                                                                    \tag{22}
\]
Indeed the complete-end coefficients have rate at most
\(b_2\); the outgoing coefficients with \(|\Im u|\le1/2\)
have rate at most \(2/3\); and each of the two traced-angle
Newton polynomials has real far rate at most \(1/2000\).
Every retained term is bounded separately, so shortening
does not require an estimate of a partial coherent sum
by a larger coherent sum.

The real spectral interval is
\(I=[2\cos(\pi/2000),2]\). Markov's inequality for the
degree-\(2U\) polynomial (3) retains every required first
normal at polynomial cost. Chebyshev continuation to the
same fixed filled ellipse of parameter \(e^{1/6000}\)
costs at most \(2U/6000<N/6000<N/4000\).
Hence the old fixed \(h_c\le1/2000\) may be used for
the whole interval \(T_N+iv,\ |v|\le h_c\).
The exact crossing and denominator still satisfy
\[
 \frac1{4\cosh^2(Nv/2)}\le e^{-N|v|},\qquad
 \left|e^{3iN(T_N+iv)^2/(4\pi)}\right|
                               \le e^{3N|v|/2}.
                                                                    \tag{23}
\]
Thus the total vertical extra rate is at most \(1/2000\),
just as in the original boundary proof.

Define the actual new removed terms by
\[
 \begin{split}
 \mathcal R_N^{<<}(u)
    &=\eta_NC_{N,3}
        \sum_{|\tau_j|\ge T_N}
                    \partial_t g_N^{<<}(\tau_j,u),\\
 \mathcal V_N^{<<}(u)
    &=\frac{\eta_NN^2C_{N,3}}{\pi}
       \int_{-h_c}^{h_c}
       \frac{g_N^{<<}(T_N+iv,u)}
                       {4\cosh^2(Nv/2)}\,dv .
 \end{split}                                                       \tag{24}
\]
Using the unchanged action floor and rational reserve,
\[
 \Re S(u)>\frac{79}{63},\qquad
 \frac{79}{63}
   -\left(\frac{18763}{15000}+\frac1{2000}\right)
                  =\frac{1639}{630000}>\frac1{400},
                                                                    \tag{25}
\]
gives
\[
 |\mathcal R_N^{<<}(u)|+|\mathcal V_N^{<<}(u)|
                   \le C e^{N(\Re S(u)-1/500)}.
                                                                    \tag{26}
\]
The corresponding absolute derivative sum and absolute
vertical integral obey the same bound.

## 6. Exact remaining contour inventory

The complete trace identity applies directly to the new
polynomial source. For every eligible lower-half-plane
path \(\Gamma_N\) from \(-T_N-ih_c\) to \(T_N-ih_c\),
\[
 Q_N^{<<}(u)=
 -\frac{N^2C_{N,3}}{\pi i}
       \int_{\Gamma_N}g_N^{<<}(t,u)W_N(t)\,dt
                 +O(e^{N(\Re S(u)-1/500)}).
                                                                    \tag{27}
\]
Combining with the separate trace-level deletion (2)
gives the same formula for \(Q_N(u)\).
All physical nodes and normals not in (24) remain in
this exact integral. In particular its odd central
simple pole has not been deleted.

To specify what is still needed, choose any lower
connecting paths
\[
 \Gamma_L:-T_N-ih_c\longrightarrow-\pi/2-iH(u),\qquad
 \Gamma_R:\pi/2-iH(u)\longrightarrow T_N-ih_c
                                                                    \tag{28}
\]
and use the horizontal interval between them. Let
\[
 \begin{split}
 \mathcal M_N(u)&=-\frac{N^2C_{N,3}}{\pi i}
  \int_{-5\pi/12-iH(u)}^{-\eta-iH(u)}
                   g_N^{<<}(t,u)W_N(t)\,dt,\\
 \mathcal C_N^{L,R}(u)&=-\frac{N^2C_{N,3}}{\pi i}
       \int_{\Gamma_{L,R}}g_N^{<<}(t,u)W_N(t)\,dt .
 \end{split}                                                       \tag{29}
\]
Every orientation here is left to right in the assembled
path. Equations (14), (20), and (27) give the actual
remaining-source reduction
\[
 \boxed{\quad
 Q_N(u)=\mathcal P_N^{<<}(u)+\mathcal M_N(u)
             +\mathcal C_N^L(u)+\mathcal C_N^R(u)
                +O(e^{N(\Re S(u)-1/500)}).
 \quad}                                                           \tag{30}
\]
The first term has the nonzero asymptotic (15).
None of the three displayed remaining currents in (30)
is estimated in this note. They must be controlled with
their original signs before a complete inner asymptotic,
and then an outer transfer conclusion, can be inferred.
