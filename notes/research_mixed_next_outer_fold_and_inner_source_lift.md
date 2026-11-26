# Exact positive-half outer fold and the remaining inner source

Private source deduction, 8 November 2026. No mathematical numerical
evaluation, saved-value calculation, or frozen-source edit is used.

The negative lower half of the remaining outer contour folds exactly
to a positive upper contour. Its center connector is zero, with the
original radical accounting for the odd-level central pole. This
reduces the required negative-half estimate to a positive-upper
estimate; it does not supply that estimate. The complete inner trace
has a different central-node behavior and remains explicit below.

## 1. Original outer functional

Use the original objects and scalars of
[the exact low-edge reduction](research_mixed_next_outer_exact_low_edge_reduction.md):
\[
 D=N-1,\quad q=e^{\pi i/N},\quad
 \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\quad
 \kappa_N=q^{D^2/2},\quad
 M=\lceil N/2\rceil,\quad U=\lfloor N/2\rfloor-1.
 \tag{1}
\]
The complete and shortened edges and the retained inner trace are
\[
 \begin{split}
 K_N(t,u)&=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),\\
 K_N^<(t,u)&=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 Q_N(u)&=\phi_N^{(t)}
       [R_N(t)^3K_N(t,0)K_N^<(t,u)] .
 \end{split}
 \tag{2}
\]
In the last line \(R_N(t)\) denotes the original crossing evaluated
in the traced spectral variable \(-2\cos t\). Its full Hermite
functional, all first-edge rows, and all retained second-edge rows
are unchanged. In particular \(Q_N\) is an even entire function of
\(u\), an ordinary polynomial of degree at most \(U\) in
\(-2\cos u\).

For any ordinary polynomial \(P_N\), the exact annihilator identity
in that source gives
\[
 \mathcal L_N(P_N)
 =\phi_N^{(x)}[R_N(x)^3e_M(x)
                    \mathcal K_{3,N}^<(-2,x)P_N(x)] .
 \tag{3}
\]
No equality of the shortened and full ordinary kernels at arbitrary
complex colors is asserted. Define
\[
 \begin{split}
 g_N(u)&=\sin u\,e_M(-2\cos u)\,Q_N(u)P_N(-2\cos u)
                           e^{3iNu^2/(4\pi)},\\
 W_N(u)&=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2},\qquad
 \mathcal I_N(u)=g_N(u)W_N(u).
 \end{split}
 \tag{4}
\]
Let
\[
 a_N=\pi-\frac{2\pi\lfloor N/24\rfloor}{N},\qquad
 h_c=h_c^<>0
 \tag{5}
\]
be the endpoints and fixed small height in the low-edge theorem.
Its exact formula is
\[
 \mathcal L_N(P_N)=
 -\frac{N^2C_{N,3}}{\pi i}
       \int_{\Gamma_N}\mathcal I_N(u)\,du
       +\mathcal V_N+\mathcal R_N^{\rm far},
 \tag{6}
\]
where \(\Gamma_N\) runs left to right from
\(-a_N-ih_c\) to \(a_N-ih_c\) in the open lower half-plane, and
\[
 \mathcal V_N=
 \frac{\eta_NN^2C_{N,3}}{\pi}
 \int_{-h_c}^{h_c}
 \frac{g_N(a_N+iv)}{4\cosh^2(Nv/2)}\,dv .
 \tag{7}
\]
The removed derivative samples \(\mathcal R_N^{\rm far}\) and this
entire vertical current have the established bound
\[
 |\mathcal R_N^{\rm far}|+|\mathcal V_N|
 \le CN^A\mathfrak B_N e^{N(8/5+1/1000)},\qquad
 \mathfrak B_N=\sup_{\substack{|\theta|\le\pi\\|\sigma|\le1/2}}
                   |P_N(-2\cos(\theta+i\sigma))|.
 \tag{8}
\]
For the actual \(P_N=H_N\), the final allocation in that theorem
pays (8), after the original outside factor
\((-q)^M/(\kappa_N^2N)\), below the actual transfer action by
\(1/200\). This existing boundary estimate is not changed here.

## 2. Exact fold, center connector, and right endpoint

The original radical formulas are
\[
 e_M(-2\cos u)=
 \begin{cases}
 \cos(Nu/2)/N,&N\ \mathrm{even},\\
 -\sin(u/2)\sin(Nu/2)/
       \{N\cos^2(\pi/(2N))\},&N\ \mathrm{odd}.
 \end{cases}
 \tag{9}
\]
They are the exact sine-product identities in
[the outer boundary theorem, equation (28)](research_mixed_next_outer_far_angles_and_verticals.md).
Directly from (4),
\[
 W_N(-u)=W_N(u),\qquad g_N(-u)=-g_N(u).
 \tag{10}
\]
Thus \(\mathcal I_N\) is odd wherever defined.

It is also holomorphic at zero. At even levels \(W_N\) is regular
there. At odd levels \(W_N\) has a double pole, while (9) gives
\(e_M(-2\cos u)=O(u^2)\), so \(g_N(u)=O(u^3)\).
The pole is removable and \(\mathcal I_N(u)=O(u)\).
There are no other poles on the imaginary axis. Consequently the
oriented center connector has the exact value
\[
                 \int_{-ih_c}^{ih_c}\mathcal I_N(u)\,du=0 .
 \tag{11}
\]
This is cancellation of an odd holomorphic function on a symmetric
segment, not an estimate at an omitted physical node.

Choose any lower path \(\gamma_-\) from \(-ih_c\) to
\(a_N-ih_c\), and any upper path \(\gamma_+\) from \(ih_c\) to
\(a_N+ih_c\). They may be taken in the respective open right
half-strips, with bounded piecewise smooth geometry. All poles of
\(\mathcal I_N\) lie on the real axis. Reflecting the left part
of a lower contour by \(u=-v\), and retaining its orientation,
gives exactly
\[
 \int_{\Gamma_N}\mathcal I_N(u)\,du
       =\int_{\gamma_-}\mathcal I_N(u)\,du
         -\int_{\gamma_+}\mathcal I_N(u)\,du .
 \tag{12}
\]
For example, the reflected left path runs from \(a_N+ih_c\)
to \(ih_c\); its integral is the negative of the displayed
left-to-right upper path. Arbitrary such paths then follow by
Cauchy's theorem separately in the two half-planes.

In particular the original source has the exact positive-half form
\[
 \boxed{\quad
 \mathcal L_N(P_N)=
 -\frac{N^2C_{N,3}}{\pi i}
 \left\{\int_{\gamma_-}\mathcal I_N(u)\,du
             -\int_{\gamma_+}\mathcal I_N(u)\,du\right\}
       +\mathcal V_N+\mathcal R_N^{\rm far}.
 \quad}
 \tag{13}
\]
Both Fourier sectors and the original scalar remain present.
No conjugation of a crossing or of a quantum coefficient was used.

There is also a closed-contour version that verifies the endpoint
accounting. At the right midpoint,
\[
 W_N(a_N+iv)=-\frac{\eta_N}{4\cosh^2(Nv/2)} .
 \tag{14}
\]
Hence the coefficient in (6) times the upward integral of
\(\mathcal I_N\) on \([a_N-ih_c,a_N+ih_c]\) is precisely
\(\mathcal V_N\), with its displayed sign. Together with (11),
(13) equals the same coefficient times the positively oriented
right-half rectangle, plus \(\mathcal R_N^{\rm far}\).
Thus the fold has neither deleted nor duplicated either original
vertical contribution. The odd-level central derivative sample
is zero because of the exact radical in (9).

## 3. The available positive-upper decay

For \(u=a+iH\), \(0\le a\le\pi/2\), and fixed
\(0<H_0\le H\le1/2\), equations (9) and (10) give
\[
 |e_M(-2\cos u)|\le \frac{C}{N}e^{NH/2},\qquad
 |W_N(u)|\le
       \frac{e^{-NH}}{(1-e^{-NH})^2}.
 \tag{15}
\]
The remaining original factors satisfy
\[
 \left|e^{3iNu^2/(4\pi)}\right|
                  =e^{-3NaH/(2\pi)},\qquad |\sin u|\le C.
 \tag{16}
\]
It follows, uniformly on that compact height interval, that
\[
 |\mathcal I_N(a+iH)|
 \le \frac{C}{N}|Q_N(a+iH)P_N(-2\cos(a+iH))|
          e^{-N\{H/2+3aH/(2\pi)\}} .
 \tag{17}
\]
This is an actual favorable multiplier, not a bound for \(Q_N\).
The connector near zero remains exactly zero by (11), rather than
being assigned the fixed-height estimate (17).

For clarity, degree continuation alone can consume the first term
in this saving. If
\[
 M_N^{\rm real}=\sup_{-\pi\le a\le\pi}|Q_N(a)|,
\]
the ordinary Chebyshev coefficient estimate for its degree \(U\)
gives
\[
 |Q_N(a+iH)|\le(2U+1)M_N^{\rm real}e^{UH}.
 \tag{18}
\]
Indeed each Chebyshev coefficient is bounded by twice the real
supremum, and \(|\cos(j(a+iH))|\le e^{jH}\).
Since \(U=\lfloor N/2\rfloor-1\), combining (18) with
\(e^{-NH/2}\) gives only a bounded extra factor at fixed \(H\);
it supplies no fixed positive exponential gap in \(N\).
The crossing saving in (17) remains, but an eligible quantitative
inner-source bound is still required. Neither (17) nor (18)
asserts suppression of the positive-upper integral.

## 4. The inner trace does not inherit the center cancellation

For each fixed complex \(u\), put
\[
 f_N(t,u)=K_N(t,0)K_N^<(t,u),\qquad
 \widetilde g_N(t,u)=\sin t\,f_N(t,u)e^{3iNt^2/(4\pi)}.
 \tag{19}
\]
Put \(\tau_j=2\pi(D/2-j)/N\), \(0\le j<N\).
The exact complete-trace identity gives, for a physical midpoint
\(T_N=\pi-2\pi m_N/N\), \(0\le m_N<N/2\), any \(h_t>0\),
and any eligible lower path \(\Gamma_t\) between
\(-T_N-ih_t\) and \(T_N-ih_t\),
\[
 \begin{split}
 Q_N(u)={}&-\frac{N^2C_{N,3}}{\pi i}
      \int_{\Gamma_t}\widetilde g_N(t,u)W_N(t)\,dt\\
 &+\frac{\eta_NN^2C_{N,3}}{\pi}
      \int_{-h_t}^{h_t}
       \frac{\widetilde g_N(T_N+iv,u)}
                            {4\cosh^2(Nv/2)}\,dv
       +\mathcal R_N^{\rm inner}(u).
 \end{split}
 \tag{20}
\]
Here \(\mathcal R_N^{\rm inner}\) is literally the removed sum
\(\eta_NC_{N,3}\sum_{|\tau_j|\ge T_N}
\partial_t\widetilde g_N(\tau_j,u)\).
The inner first normals are retained in both terms of this
decomposition. This is
[the complete trace, Corollary 3](research_exact_complete_trace_contour.md)
applied to the polynomial (19), without an inner annihilator.

At odd levels,
\[
 W_N(t)=-\frac1{N^2t^2}+O(1),\qquad
 \widetilde g_N(t,u)=t f_N(0,u)+O(t^3).
 \tag{21}
\]
Thus the inner integrand has in general the simple pole
\(-f_N(0,u)/(N^2t)\). Its central physical contribution is
the original \(C_{N,3}f_N(0,u)\). There is no factor \(e_M\)
in (19), so the outer cancellation (11) cannot be copied into
the inner trace.

## 5. What a second-edge packet would provide locally

Keep
\[
 \mathcal U_+=\{u:0\le\Re u\le\pi/2,\ -1/2\le\Im u\le0\}.
\]
[The original cubic continuation](research_mixed_next_inner_three_cubic_continuation.md)
proves a holomorphic selected \(t=t(u)\),
the original zero logarithmic charge, and
\(\Phi_{tt}(t(u),u)\ne0\), where
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)
                         +\frac{3it^2}{4\pi}-it.
 \tag{22}
\]
[The complete-edge theorem](research_pair_free_boundary_kernel.md)
already supplies the full \(K_N(t,0)\)
packet on a fixed complex neighborhood of this compact critical
image. A completed shortened-second-edge proof must likewise
retain a fixed independent complex neighborhood of
\(\{(t(u),u):u\in\mathcal U_+\}\), with holomorphic normalized
errors. A statement only on that graph does not supply the
nearby \(t\)-values in an angular saddle integral.

If that additional packet is established, multiplication gives
the local product \(N^{-3}a_e(t,0)a_e(t,u)
e^{N\{\psi(t,0)+\psi(t,u)\}}(1+O(N^{-1}))\).
Consequently a local angular descent arc through \(t(u)\) has
the original order \(C_{N,3}N^{-3/2}\), with coefficient
\[
 \frac{i\sqrt{2\pi}}{\pi}
 \frac{\sin(t(u))\,a_e(t(u),0)a_e(t(u),u)}
                         {\sqrt{-\Phi_{tt}(t(u),u)}} .
 \tag{23}
\]
All displayed factors are nonzero; the square root and orientation
are calibrated to the original complete-point trace. Equation (23)
is only this local Gaussian calculation under the stated packet
input. It is not a statement that the full original trace has that
coefficient.

To identify it with (20), the full angular path must still be
constructed in the correct homology class, its nonlocal finite
source must be bounded, and its removed samples and complete
vertical current must be paid. The old nineteen-surface
[single-three proof](research_all_nonzero_degree_two_fillings.md)
licenses a small outer bidisk, not this entire
outer rectangle. Once a full source bound holds on a lower path
at distance at least \(h>0\) from the real axis, all angular
charges greater than one follow from the exact identity
\[
 W_N(t)=e^{-iNt}(1+O(e^{-Nh})).
 \tag{24}
\]
The normal-derived charge multiplicities are already summed in
this rational kernel. They cannot be dropped before that global
path bound is proved.

Finally, evenness sends negative lower \(u\) to positive upper
\(-u\), rather than to the currently studied positive lower
rectangle. The exact fold (13) permits the different, potentially
cheaper positive-upper estimate (17); it does not require a second
geometric packet there if a complete source bound suffices.
No complete inner packet, full outer bound, or short-filling
transfer asymptotic is asserted in this note.
