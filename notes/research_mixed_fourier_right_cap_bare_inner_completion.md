# Complete bare inner-source bound for the Fourier right cap

Research completion, 7 November 2026. All three real-row comparisons
in the bare inner-contour theorem are now proved. The result bounds
the whole literal own-four conditional source, multiplied by its
original incoming halfweight and exact cardinal coefficient, on the
actual outgoing critical-height plateau. The outgoing finite sum
remains a separate operation.

## 1. Reference, exact source and supporting plane

Fix \(y=x_0\), \(Y=e^{2\pi iy}\), and an actual correlated
last-four reference
\[
 \eta\in\{0,1\},\qquad a_*\in K_{3+\eta},\qquad
 (s_*,q_*)\in O_4^2.
 \tag{1}
\]
These are the original branches in the
[correlated endpoint theorem](research_mixed_fourier_right_cap_correlated_endpoint.md).
They include the last ordinary vertex of every actual Fourier-ended
prefix of length at least two whose last type is four.
The [completed annulus theorem](research_mixed_fourier_right_cap_annulus_completion.md)
puts the auxiliary exterior leg \(\beta_Y(q_*)\) in \(K_3\),
so the old complete own-four source estimates apply to the same
coupled reference and original logarithmic lifts.

Keep \(P=[11/50,9/20]\), and set
\[
 a=x+i\Im a_*,\quad q=z+i\Im q_*,\quad x,z\in P.
 \tag{2}
\]
The heights and incoming allocation are exactly those in the
[bare inner-contour theorem](research_mixed_fourier_right_cap_bare_inner_contour.md):
\(|\Im a_*|\le.108\), \(-.102\le\Im s_*,\Im q_*\le-.001\);
when \(\eta=1\), the incoming height is negative and unselected.
No selected-height or independent-height extension is made.

Use the original primitive and cardinal phase to define
\[
 \begin{split}
 \mathscr F_\eta(s,a,q)
 &=g(s+a)+g(s+q)-3g(s)-(1+\eta/2)g(a)-g(q)
                       +2\pi ias+\ell_q(y),\\
 M_\eta&=\Re\mathscr F_\eta(s_*,a_*,q_*),\qquad
 p_\eta=\Re\mathscr F_{\eta,a}(s_*,a_*,q_*),\\
 \mathcal L_\eta(x,z)
 &=M_\eta+p_\eta(x-\Re a_*)
       -\kappa\{(x-\Re a_*)^2+(z-\Re q_*)^2\},
 \qquad \kappa=\frac1{2500000}.
 \end{split}
 \tag{3}
\]
The outgoing marginal is zero by the original Fourier critical
equation. The incoming marginal and all action constants are retained.

The finite factors have their literal normalization. With
\(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\) and \(p_j(X)=(rX;r)_j\),
\[
 C_{1,N}(X,Z)=\sum_{j=0}^{N-1}
                 \frac{X^{-j}p_j(X)p_j(Z)}{P_j^3}.
 \tag{4}
\]
The incoming \(d_N\) is the original degree-less-than-\(N\)
polynomial with \(d_N(r^j)=P_j^{-1}\). The exact cardinal
interpolation on (2) is
\[
 f_N(q;y)=\frac{e^{-\pi i(N-1)y}}N(1-Y^N)
       \frac{e^{2\pi iNyq}}{\mathcal P_N(q+1/N,Y)}.
 \tag{5}
\]
Here \(\mathcal P_N\) is the specific original root-Pochhammer
interpolation. The factor \(1/N\), lifted Fourier scalar and
level-parity dependence are part of (5); no outside crossing or
summation scalar is inserted into (4).

## 2. The three proved margins

Let \(\mathcal T_\eta(c;x,z)\) denote the full real-row rate
from the bare inner-contour theorem, equation (17), including its
chirp, incoming halfweight and \(\Re\ell_q(y)\).
Uniformly on (1)--(2),
\[
 \begin{split}
 \mathcal T_\eta(1/8;x,z)&<\mathcal L_\eta(x,z)-1/35000,\\
 \mathcal T_\eta(1/2;x,z)&<\mathcal L_\eta(x,z)-1/35000,\\
 \mathcal T_\eta(1;x,z)&<\mathcal L_\eta(x,z)-37/70000.
 \end{split}
 \tag{6}
\]

The first two are the
[allocation-curvature theorem](research_mixed_fourier_allocation_curvature.md).
For the last, the successful fixed
[saved-margin check](../repro/results/research-mixed-fourier-right-cap-last-row-saved-margin.json)
certifies all 36 own-four ordinary-boundary chart maxima below
\(-1/50\). The quantitative reference-boundary principle limits
the whole-domain deficit by \(-1/1000\), using the original
matched entropy gap. It does not transfer the larger boundary
reserve unchanged into the interior.

The [saved-margin proof](research_mixed_fourier_right_cap_last_row_saved_margin.md)
then uses the exact difference \(H(q)=g(q)/2+\ell_q(y)\)
between the old allocated phase and the bare phase. Its horizontal
tangent remainder is strictly less than \(33/70000\). Thus
\[
 1/1000-33/70000=37/70000>1/2000,
 \tag{7}
\]
which proves the third line of (6). Every revived carrier,
both conditional orientations and the original reference
correlation remain included. No finite \(d_N(q)\) was divided out.

The new result has SHA-256
349c06026359e7cb4521354c1df79c6e35d1112dac98e3f7c4a53f7275e1fb89.
It records 36 passed rational comparisons, 72 author/replay chart
associations, 71 reconstructed complete dyadic trees and the
unchanged imported own-three tree. All 49 before/after bindings
agree. There were no analytic, root, gain, proposal, refinement
or source-replay calls. The inherited analytic maxima are from
the completed original 320-bit replay; the new check parses their
outward decimal displays and verifies exact provenance and margins.

The checker SHA-256 is
e9f87139abe5e02292c046537275dd221a9bf8efd8d5e6298a5c6b0ed9c88a08;
its fixed protocol SHA-256 is
e6d69c7afa5dc7fadd9425dbe5ce85983dcc0c7ba8ffb76d7b93c9d7af300679.
The completed record was inspected without replay after the sole run.

## 3. Full inner-source conclusion and its boundary

**Theorem.** For every prescribed \(\tau>0\), there are
\(C_\tau,A_\tau,N_\tau\) such that, for every \(N\ge N_\tau\)
of either parity, uniformly on (1)--(2),
\[
 \boxed{\quad
 |C_{1,N}(e^{-2\pi ia},e^{-2\pi iq})|\,
 |d_N(e^{-2\pi ia})|^{\eta/2}|f_N(q;y)|
 \le C_\tau N^{A_\tau}
                 e^{\,N(\mathcal L_\eta(x,z)+\tau)}.
 \quad}
 \tag{8}
\]

Indeed the exact source envelope in the bare inner-contour theorem,
equation (19), is the maximum of \(\mathcal L_\eta\) and
the three rates in (6). Those rates are all strictly smaller.
That theorem already includes the whole physical inner-row interval,
the revived endpoint, both horizontal aliases, vertical currents,
unpenalized joins, half-grid shifts and the exact zero-mode
coefficient \(+N\). Substituting (6) therefore proves (8) for the
whole finite factor (4), not merely its central critical current.
The arbitrary tolerance in (8) is one aggregate finite-source
tolerance; the polynomial prefactor is retained.

The [outer-contour theorem](research_mixed_fourier_right_cap_outer_contour.md)
uses a different exact interpolation \(\widehat f_N(q;y)\),
defined by a remaining factorial product. On the compact negative
critical-height strip (2), its equation (6) and the original
root-Pochhammer expansion have the same nonzero leading symbol
and exactly the same calibrated phase. Hence
\[
       \widehat f_N(q;y)/f_N(q;y)=1+O(N^{-1})
 \tag{8a}
\]
uniformly there. Bound (8) therefore also holds with
\(\widehat f_N\), after changing its constant. This is a comparison
of two proved expansions on that strip, not exact off-grid equality
of the interpolations or a bound at the tall outer contour heights.

Compactness and the strict row gaps also give a small complex
neighborhood of \(y=x_0\) on the same actual critical branches.
After shrinking that neighborhood, the analogous assertions hold
with the original varying action and incoming marginal, coefficient
\(\kappa/2\), and common row gap \(1/70000\).
This uses continuity of the original profiles and compact reference
family, together with the annulus theorem's local continuation;
it is not a statement on the whole outgoing Fourier period.

In particular, (8) does not evaluate or lower-bound
\[
 V_N^{\rm F}(y,e^{-2\pi ia})
       =\sum_{l=0}^{N-1}C_{1,N}(e^{-2\pi ia},r^l)f_l(y).
 \tag{9}
\]
Its outgoing \(q\)-source remains to be controlled. The
[outer-contour reduction](research_mixed_fourier_right_cap_outer_contour.md)
keeps the physical-height faces and the wedge
\(s>1/2,\ 0\le q<11/50,\ s+q\le1\) explicitly.
The negative-critical-height comparisons (6) do not replace those
real-height comparisons. No whole right-cap asymptotic, boundary
contraction or open-source noncancellation is asserted here.
