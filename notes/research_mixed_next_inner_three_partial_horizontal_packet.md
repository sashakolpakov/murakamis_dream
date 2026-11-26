# The original inner current through the center and positive saddle

Private finite-source assembly, 8 November 2026. The exact inner
horizontal current from a fixed negative cut through the selected
positive saddle has its original nonzero Gaussian asymptotic.
The center interval, every higher Fourier charge, the full first
edge, and every row of the shortened second edge are retained.

This is a partial angular current. The rest of the negative
horizontal and the connecting paths to the original far endpoints
are not included. No mathematical numerical evaluation or
frozen-source edit is used.

## 1. Exact current and statement

Use the original scalar and source conventions:
\[
 \begin{gathered}
 D=N-1,\qquad q=e^{\pi i/N},\qquad
 \eta_N=(-1)^D,\qquad C_{N,3}=q^{3D^2/4},
 \qquad U_N=\lfloor N/2\rfloor-1,\\
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),\\
 K_N^{<}(t,u)=\sum_{j=0}^{U_N}
                       e_j(-2\cos t)e_j(-2\cos u),\\
 f_N(t,u)=K_N(t,0)K_N^{<}(t,u),\qquad
 \widetilde g_N(t,u)=\sin t\,f_N(t,u)e^{3iNt^2/(4\pi)},\\
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
 \end{gathered}
 \tag{1}
\]
The Newton normalization, crossing, and both finite edge cutoffs
are exactly those in
[the full inner-source identity, equations (19)--(20)](research_mixed_next_outer_fold_and_inner_source_lift.md).
In particular the first edge has all \(N\) rows, and the shortened
second edge has its exact parity-dependent cutoff.

Let
\[
 \begin{gathered}
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},\\
 t_*(u)=a_*(u)-iH(u),\qquad
 0<a_*(u)<\pi/2,\quad 1/2<H(u)<1,\\
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,\qquad
 S(u)=\Phi(t_*(u),u),\qquad \Phi_t(t_*(u),u)=0 .
 \end{gathered}
 \tag{2}
\]
These are the original cubic branch, logarithmic charge, and
phase constant. Fix the \(\eta>0\) supplied by
[the center-bridge theorem](research_mixed_next_inner_three_center_bridge.md).
Its construction gives
\[
                 0<\eta<\tfrac12\min_{\mathcal U_+}a_*(u).
 \tag{3}
\]
Define the literal left-to-right horizontal current
\[
 \mathcal P_N(u)=
 -\frac{N^2C_{N,3}}{\pi i}
 \int_{-\eta-iH(u)}^{\pi/2-iH(u)}
             \widetilde g_N(t,u)W_N(t)\,dt .
 \tag{4}
\]
Every point of its path is strictly below the real sampling
line. No pole or physical central sample is removed.

**Theorem.** Uniformly for \(u\in\mathcal U_+\), through all
sufficiently large levels of both parities,
\[
 \boxed{\qquad
 \mathcal P_N(u)=
 C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                                  (1+O(N^{-1})),
 \qquad}
 \tag{5}
\]
where the original coefficient is
\[
 \mathcal A(u)=
 \frac{i\sqrt{2\pi}}{\pi}
 \frac{\sin(t_*(u))\,a_e(t_*(u),0)\,a_e(t_*(u),u)}
                         {\sqrt{-\Phi_{tt}(t_*(u),u)}}\ne0 .
 \tag{6}
\]
The square root is the original left-to-right Gaussian root;
it has positive real part on this family.
Formula (6) is precisely equation (23) of the cited inner-source
identity, now licensed for the entire partial current (4).
No derivative assertion for (4) is made: its height \(H(u)\)
is a real-valued function of the parameter.

## 2. Center and positive horizontal away from the saddle

Write \(s(u)=\Re S(u)\), and put
\[
 H_0=\min_{\mathcal U_+}H(u)>1/2.
 \tag{7}
\]
The adopted center theorem applies to the exact integrand in
(1), with every Fourier charge. It gives a fixed
\(\epsilon_c>0\) such that
\[
 \frac{N^2}{\pi}
 \int_{-\eta}^{\eta}
 |\widetilde g_N(a-iH(u),u)W_N(a-iH(u))|\,da
                 \le C e^{N(s(u)-\epsilon_c)}.
 \tag{8}
\]
This includes both sides of the imaginary axis. There is no
use of the outer radical's center cancellation.

On the whole remaining interval \(\eta\le a\le\pi/2\),
[the positive-horizontal source theorem, equation (45)](research_mixed_next_shortened_edge_positive_horizontal_packet.md)
gives
\[
 |f_N(a-iH(u),u)|
 \le C N^B
 e^{N\Re\{\psi(a-iH(u),0)+\psi(a-iH(u),u)\}} .
 \tag{9}
\]
Its proof retains the full first edge and the exact shortened
second edge; it is not a bound obtained by replacing a partial
sum with a complete one. The source extends to fixed independent
complex neighborhoods, although only the displayed base interval
is needed for the remote bounds here.

The adopted
[horizontal concavity theorem, equations (13)--(14)](research_mixed_next_inner_three_horizontal_concavity.md)
gives
\[
 \Re\Phi_{tt}<-\frac1{4\pi},\qquad
 \Re\Phi(a-iH(u),u)
       \le s(u)-\frac{(a-a_*(u))^2}{8\pi}
                       \quad(0\le a\le\pi/2).
 \tag{10}
\]
The sine factor in (1) is uniformly bounded. Also, for
\(t=a-iH(u)\),
\[
 |e^{-iNt}|=e^{-NH(u)},\qquad
 \left|(1-\eta_Ne^{-iNt})^{-2}-1\right|
                          \le C e^{-NH_0}.
 \tag{11}
\]
The constants hold at both parities. In particular the exact
factor in (11) is uniformly bounded; no absolute sum over a
discarded Fourier sector is being inferred.

Choose a fixed \(r>0\) sufficiently small that
\[
 [a_*(u)-r,a_*(u)+r]\subset(\eta,\pi/2)
 \tag{12}
\]
for every \(u\), and the corresponding local complex angular
neighborhood is eligible for both edge packets used below.
Equations (9)--(11) show that the two complementary positive
horizontal pieces, including the original prefactor in (4),
have a fixed exponential gap. For example their pointwise
phase loss is at least \(r^2/(8\pi)\); polynomial absorption
retains any smaller positive loss.

The entire higher-charge correction on \([\eta,\pi/2]\)
is also paid. Subtract the leading factor \(e^{-iNt}\)
from \(W_N(t)\) and apply (11), while keeping (9)--(10).
Its absolute integral, with the original \(N^2/\pi\),
is bounded by a polynomial times
\[
                         e^{N(s(u)-H_0)}.
 \tag{13}
\]
Thus the leading trace charge \(-it\) used in (2) comes
from an exact decomposition with a strictly smaller
remainder. The center interval was already estimated with
the full denominator in (8).

## 3. Local finite packets and the original angular Gaussian

The actual cubic image satisfies the hypotheses of
[the complete free-edge packet, Theorem 1](research_pair_free_boundary_kernel.md):
\[
        0<\Re t_*<\pi/2,\quad0<H(u)<1,\quad
                         |\cos(t_*/2)|<1 .
 \tag{14}
\]
These are the adopted original cubic guards and have uniform
margins by compactness. Hence the full first edge has
\[
 K_N(t,0)=N^{-3/2}a_e(t,0)e^{N\psi(t,0)}
                                  (1+O(N^{-1}))
 \tag{15}
\]
on a fixed complex neighborhood of that image, with
holomorphic normalized errors. This theorem includes its
original upper Newton rows and radical at both parities.

The adopted positive-horizontal packet supplies, on a fixed
independent neighborhood of \((t_*(u),u)\),
\[
 K_N^{<}(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                                  (1+O(N^{-1})).
 \tag{16}
\]
The two coefficients use the same original phase convention.
The normalized errors and their fixed local derivatives
are uniformly controlled. Multiplying (15)--(16) and
retaining the leading charge in (11) gives
\[
 \widetilde g_N(t,u)e^{-iNt}
 =N^{-3}
   \sin t\,a_e(t,0)a_e(t,u)e^{N\Phi(t,u)}
                                  (1+O(N^{-1})).
 \tag{17}
\]
Every factor in its leading amplitude is holomorphic near
the local interval (12).

The interval in (12) is oriented left to right. At its
center \(\Phi_t=0\), and (10) gives
\(\Re(-\Phi_{tt})>1/(4\pi)\). The uniformly nondegenerate
complex Gaussian expansion along that real displacement
therefore yields
\[
 \begin{split}
 &\int_{a_*(u)-r-iH(u)}^{a_*(u)+r-iH(u)}
       \sin t\,a_e(t,0)a_e(t,u)e^{N\Phi(t,u)}
                                  (1+O(N^{-1}))\,dt\\
 &\quad=
 N^{-1/2}e^{NS(u)}
 \frac{\sqrt{2\pi}\,
          \sin(t_*(u))a_e(t_*(u),0)a_e(t_*(u),u)}
                         {\sqrt{-\Phi_{tt}(t_*(u),u)}}
                                  (1+O(N^{-1})).
 \end{split}
 \tag{18}
\]
The derivative bounds on the normalized packet errors
justify the same uniform relative order in (18).
The original square root agrees with the positive-real-part
root on this horizontal by (10); the orientation is unchanged
from the local trace calculation in the fold/source theorem.

Now multiply by \(N^{-3}\) from (17) and by the exact
\(-N^2C_{N,3}/(\pi i)\) in (4). The power and sign are
\[
 N^{-3}N^{-1/2}N^2=N^{-3/2},\qquad
                         -\frac1{\pi i}=\frac{i}{\pi}.
 \tag{19}
\]
This gives exactly (5)--(6). The sine does not vanish at
\(t_*(u)\), since \(H(u)>0\); the two edge coefficients
are nonzero, as is the angular Hessian. Compactness
therefore bounds \(|\mathcal A(u)|\) away from zero.
The exponentially smaller terms (8), (13), and the remote
positive pieces can be absorbed into the stated relative
\(O(N^{-1})\), uniformly in \(u\).

## 4. Scope of the assembled current

The theorem proves the coefficient of the entire original
partial horizontal current (4), not only a small saddle arc.
It includes the full center interval and all Fourier charges.
At odd levels the inner physical central pole is still part
of the full trace identity; this proof has remained at a
fixed positive depth and has neither crossed nor deleted it.

No claim is made here for the rest of the negative horizontal,
for paths joining either horizontal endpoint to the original
far angular endpoints, or for the remaining outer functional.
Those contributions must be added with their original
orientations before (5) can become an asymptotic for the
complete inner trace.
