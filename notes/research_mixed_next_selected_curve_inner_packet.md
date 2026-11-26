# The original shortened-output inner packet on the full selected curve

Private finite-source assembly, 9 November 2026. The four paid
pieces of the right connection close the last current in the
original shortened-output inner trace. The resulting nonzero
relative asymptotic is uniform along the entire selected charged
curve, including zero charge.

No mathematical numerical evaluation, saved-value arithmetic,
or frozen-source edit is used. The theorem is stated on this
compact curve. It does not assert an open complex neighborhood
or replace the full second kernel at complex spectral values.

## 1. The exact source and selected family

Use the original Newton polynomials, crossing, and full
Frobenius functional \(\phi_N\). Put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad
 U=\lfloor N/2\rfloor-1,\quad M=\lceil N/2\rceil,\quad
 \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4}.
\tag{1}
\]
The ordinary kernels and their angular versions are
\[
\begin{gathered}
 K_N^{\mathrm{ord}}(x,y)=\sum_{j=0}^{D}e_j(x)e_j(y),
 \qquad
 K_N^{<,\mathrm{ord}}(x,y)=\sum_{j=0}^{U}e_j(x)e_j(y),\\
 K_N(t,u)=K_N^{\mathrm{ord}}(-2\cos t,-2\cos u),\qquad
 K_N^<(t,u)=K_N^{<,\mathrm{ord}}(-2\cos t,-2\cos u).
\end{gathered}
\tag{2}
\]
Define precisely the trace proved below:
\[
 \boxed{\quad
 Q_N^{\mathrm{sh}}(u)=
 \phi_N^{(x)}
 \bigl[R_N(x)^3K_N^{\mathrm{ord}}(-2,x)
               K_N^{<,\mathrm{ord}}(x,-2\cos u)\bigr].
 \quad}
\tag{3}
\]
Its first kernel is full. Only the outgoing kernel terminates
at \(U\). The inner trace retains all values, first normals,
and the odd simple node. As an ordinary function of
\(-2\cos u\), (3) is a polynomial of degree at most \(U\).

Let \(\mathcal C=\{u_\delta:0\le\delta\le1/2\}\) be the
original selected curve of
[the full-interval phase theorem](research_mixed_next_selected_charged_curve_full_interval.md).
Write
\[
 u_\delta=\beta-iK,\qquad
 t_*(u)=a_*(u)-iH_*(u),\qquad
 S(u)=\Phi(t_*(u),u),\qquad s(u)=\Re S(u),
\]
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it.
\tag{4}
\]
The action, its logarithmic charge, and its constant are
unchanged. The adopted selected guards imply
\[
 \mathcal C\subset
 \mathcal U_+:=\{u:0\le\Re u\le\pi/2,\ -1/2\le\Im u\le0\},
 \qquad
 0<a_*(u)<\pi/2,\quad2/3<H_*(u)<1.
\tag{5}
\]
The original Gaussian coefficient is
\[
 \mathcal A(u)=\frac{i\sqrt{2\pi}}{\pi}\,
 \frac{\sin t_*(u)\,a_e(t_*(u),0)a_e(t_*(u),u)}
                 {\sqrt{-\Phi_{tt}(t_*(u),u)}} .
\tag{6}
\]
The square root is the original left-to-right Gaussian root.
The source theorem cited below proves that this coefficient
is nonzero, with a uniform positive lower bound for its
modulus on \(\mathcal U_+\).

**Theorem.** At both parities, uniformly for
\(0\le\delta\le1/2\),
\[
 \boxed{\quad
 Q_N^{\mathrm{sh}}(u_\delta)
  =C_{N,3}N^{-3/2}\mathcal A(u_\delta)e^{NS(u_\delta)}
                           \{1+O(N^{-1})\}.
 \quad}
\tag{7}
\]
In particular (3) is nonzero on this entire selected curve
for all sufficiently large \(N\). Its logarithmic rate is
uniformly \(s(u_\delta)+O(\log N/N)\).

The claim is for the exact source (3). Neither a pointwise
equality with the full outgoing kernel at complex \(u\),
nor a normalized derivative assertion on an open neighborhood,
is part of (7).

## 2. The unchanged remaining-current representation

For clarity retain the exact finite source used on the inner
angular contour:
\[
\begin{gathered}
 f_N^{<<}(t,u)=K_N^<(t,0)K_N^<(t,u),\\
 g_N^{<<}(t,u)=\sin t\,f_N^{<<}(t,u)e^{3iNt^2/(4\pi)},\\
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
\end{gathered}
\tag{8}
\]
The separate
[first-edge tail contraction](research_mixed_next_inner_three_first_edge_tail_contraction.md)
bounds the change from (3) to the trace with both kernels
shortened by \(Ce^{N(s-1/300)}\) on \(\mathcal U_+\).
That is a trace-level estimate. No pointwise full-first
replacement outside its eligible domain is used here.

The
[shortened-source transfer, (27)--(30)](research_mixed_next_inner_three_short_pair_source_transfer.md)
retains the exact full angular multiplier and all original
far samples and endpoint verticals. After the subsequent
paid currents, the
[one-remaining-current assembly, (6)](research_mixed_next_inner_three_single_remaining_current.md)
gives on all of \(\mathcal U_+\)
\[
 Q_N^{\mathrm{sh}}(u)
 =C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                  \{1+r_N(u)\}
  +\mathcal R_N(u)+E_N(u),
\tag{9}
\]
where
\[
 |r_N(u)|\le C/N,\qquad
 |E_N(u)|\le C e^{N(s(u)-\epsilon_0)}
\tag{10}
\]
for some fixed \(\epsilon_0>0\), at both parities.
The first error in (10) belongs to the surviving original
partial Gaussian. The second includes the first-edge trace
tail, the complete negative and far currents, every original
removed physical sample, and the full endpoint verticals.
There is no second deletion of those terms below.

The remaining current is exactly
\[
 \mathcal R_N(u)=
  -\frac{N^2C_{N,3}}{\pi i}
      \int_{\gamma(u)}g_N^{<<}(t,u)W_N(t)\,dt,\qquad
 \gamma(u):\pi/2-iH_*(u)\longrightarrow5\pi/6-i/10.
\tag{11}
\]
Every piecewise smooth path with these endpoints in the
open lower half-plane gives the same value. The finite
kernels, sine and Gaussian in (8) are entire in \(t\);
all poles of \(W_N\) are real. Thus the integrand is
holomorphic on the simply connected open lower half-plane.
Changing such a path adds no residue or real sample.

## 3. Exact four-piece path and its uniform bound

Put \(a_0=\arccos(-13/20)\) as in
[the low far-horizontal theorem](research_mixed_next_selected_low_far_horizontal.md).
For each \(u\in\mathcal C\), choose in (11) the successive
oriented segments
\[
\begin{aligned}
 \gamma_1:\ &\pi/2-iH_*
                 \longrightarrow2\pi/3-iH_*,\\
 \gamma_2:\ &2\pi/3-iH_*
                 \longrightarrow2\pi/3-i/10,\\
 \gamma_3:\ &2\pi/3-i/10
                 \longrightarrow a_0-i/10,\\
 \gamma_4:\ &a_0-i/10
                 \longrightarrow5\pi/6-i/10.
\end{aligned}
\tag{12}
\]
The second is oriented upwards; the others go left to right.
All four lie at height at most \(-1/10\).
There are no gaps or overlaps except their common endpoints.
Let \(I_{j,N}(u)\) denote their integrals with the literal
prefactor in (11). Then, exactly,
\[
                        \mathcal R_N(u)=\sum_{j=1}^4 I_{j,N}(u).
\tag{13}
\]

Here are the four adopted finite estimates, with their
actual source scope:
\[
\begin{array}{c|c|c}
\text{segment}&\text{uniform bound}&\text{source}\\ \hline
\gamma_1&
 |I_{1,N}|\le C e^{N(s-\epsilon_R)}&
 \text{selected action and endpoint-sector payment}\\
\gamma_2&
 |I_{2,N}|\le C e^{N(s-1/1000)}&
 \text{selected inner vertical payment}\\
\gamma_3&
 |I_{3,N}|\le C e^{N(s-1/1000)}&
 \text{initial low-horizontal theorem}\\
\gamma_4&
 |I_{4,N}|\le C e^{329N/200}&
 \text{low far-horizontal theorem}.
\end{array}
\tag{14}
\]
The first source is
[the action-floor theorem, (24)--(28)](research_mixed_next_selected_action_floor_and_endpoint_payment.md);
its constants are
\[
 d_R=\pi/2-\max_{\mathcal C}a_*(u)>0,\qquad
 \epsilon_R=\frac12\min\{1/200,d_R^2/(8\pi)\}>0.
\tag{15}
\]
The second and third sources are respectively
[the vertical theorem, (5)](research_mixed_next_selected_inner_vertical_payment.md)
and [the initial low horizontal, (5)](research_mixed_next_selected_initial_low_horizontal.md).
The fourth is
[the far horizontal, (3)](research_mixed_next_selected_low_far_horizontal.md).
Every row of (14) also bounds the corresponding absolute
integral, with its original \(N^2/\pi\) factor.

Each theorem uses precisely (8): the same two shortened
kernels, both parity indices \(U\), the full denominator
\(W_N\), and the original crossing. In particular the
first three estimates include the physical endpoint
sectors of the second edge. They do not merely estimate
its formal saddle. Their wire aliases, external caps,
factorial reflection terms and true last indices are
already included in those complete kernel bounds.
No finite source is replaced by its asymptotic packet
inside any of the four small integrals.

The action-floor theorem gives \(s(u)>331/200\) on
\(\mathcal C\). Hence the fourth line of (14) is at most
\(Ce^{N(s(u)-1/100)}\). Define
\[
                   \epsilon_{\mathrm{path}}
                     =\min\{\epsilon_R,1/1000\}>0.
\tag{16}
\]
There are only four terms, so (13)--(16) prove
\[
                 |\mathcal R_N(u)|
                    \le C e^{N(s(u)-\epsilon_{\mathrm{path}})}
                     \qquad(u\in\mathcal C).
\tag{17}
\]
All constants and sufficiently large level thresholds can
be made common by taking the maximum of the finitely many
source constants and thresholds. Compactness of
\(\mathcal C\) proves the strict uniform positivity in
(15); no explicit evaluation of its maximum is needed.

## 4. Relative asymptotic and nonvanishing

Insert (17) into the original decomposition (9).
With
\[
                  \epsilon=\min\{\epsilon_0,
                                      \epsilon_{\mathrm{path}}\}>0,
\]
the sum of the two remaining additive errors has modulus
at most \(Ce^{N(s-\epsilon)}\).
Since \(|C_{N,3}|=1\) and
\(\inf_{\mathcal C}|\mathcal A|>0\), division by the
original leading term is legitimate and gives
\[
 \frac{Q_N^{\mathrm{sh}}(u)}
      {C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}}
      =1+r_N(u)+O(N^{3/2}e^{-N\epsilon}).
\tag{18}
\]
The final term is uniformly \(O(e^{-N\epsilon/2})\) for
large \(N\), hence is smaller than \(O(N^{-1})\).
This proves (7). Taking \(N\) sufficiently large makes
the full relative error less than \(1/2\), proving
uniform nonvanishing. Taking absolute logarithms in
(18) proves the stated uniform logarithmic rate.

This division occurs only after the complete finite
right current has been bounded. No algebraic relative
error is discarded inside an oscillating outer sum.

## 5. Exact relevance to the outer observation

For an ordinary spectator polynomial \(P_N\), let
\[
 Q_N^{\mathrm{full}}(u)=
 \phi_N^{(x)}
 \bigl[R_N(x)^3K_N^{\mathrm{ord}}(-2,x)
               K_N^{\mathrm{ord}}(x,-2\cos u)\bigr].
\tag{19}
\]
The [exact low-edge reduction, Theorem 1 and Corollary 2](research_mixed_next_outer_exact_low_edge_reduction.md)
proves
\[
 e_M(y)\{Q_N^{\mathrm{full}}(y)-Q_N^{\mathrm{sh}}(y)\}=0
      \quad\text{in the original physical spectral algebra},
\tag{20}
\]
where the functions in (20) are written in the ordinary
spectral variable \(y\). Equivalently,
\[
 \phi_N^{(y)}[R_N(y)^3e_M(y)P_N(y)Q_N^{\mathrm{full}}(y)]
 =
 \phi_N^{(y)}[R_N(y)^3e_M(y)P_N(y)Q_N^{\mathrm{sh}}(y)] .
\tag{21}
\]
This is an exact finite identity. At odd levels it also
annihilates the middle second-edge row \(j=\lfloor N/2\rfloor\),
even though that row is not itself radical. The full inner
trace and all its normals are retained.

The two ordinary functions in (19),(3) need not agree
at complex spectral values. Equations (20)--(21), rather
than such an equality, license the shorter source in
the original outer observation. Formula (7) by itself
does not estimate that observation or justify exchanging
its normalized error with a cancelling finite sum.
A source-valid outer contour and its remaining endpoint,
alias and error estimates are still required.

Finally, (7) is uniform on the compact selected curve.
The new bounds are obtained from finite contour families,
but an open-neighborhood packet requires a separate proof
that all earlier finite-source errors and Gaussian charts,
as well as these new contour pieces, persist under the
required complex parameter variations. Curve values alone
do not prove that extension or its derivative bounds.

## Frozen source bindings

- Original selected charged curve:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Original one-current assembly:
  2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421.
- Original shortened-source transfer:
  a835236285224a9df4ac41451c84882609b44b223eaa2c7c359f0f48518bccae.
- First-edge trace-level tail contraction:
  b31ac2d1cbf5f0e3ab4b71b36af9718151bced51e6959ee32b26ccf7fac5dfe6.
- Selected high horizontal and action floor:
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Complete selected vertical payment:
  5813ddfa3f16e81c7907bbf8e11f6be0d07d30e0e71a74f5845d889aa1a4ac85.
- Complete initial low horizontal:
  2f0287cf9655c04d2b9ca0a1545707619b57f23e899c3b76430c73b143929141.
- Complete low far horizontal:
  1cb4d220d4fbf5fddeaf9ecb24b572908a4485e907ac4634ea2623acee0b34bd.
- Exact original low-edge observation reduction:
  76524c28bdbafafe8922993093e3e5b4447ec033e4b0dd3928295047bfde797a.

