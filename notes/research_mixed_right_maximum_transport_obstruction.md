# A right-maximum phase flow can decrease at an actual cyclic reference

Research proof, 4 November 2026. The counterexample below rejects a
proposed monotone flow on the minimum-neighbor contour, even when all
real coordinates are at least .22. It does not reject a net supporting
bound on a group of blocks, a different contour, or the original
mixed-word asymptotic. Completed source estimates are unchanged.

Use the normalized primitive and original allocated phase
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 Q_e(s;a,b)&=g(s+a)+g(s+b)-(2+e)g(s)+2\pi ias,\\
 \phi_{\eta e}(a,b)&=Q_e(s_*(a,b);a,b)
                         -(1+\eta/2)g(a)-(1+e/2)g(b).
 \end{split}                                                       \tag{1}
\]
The root \(s_*\) solves the original zero logarithmic lift, not
merely its exponentiated polynomial equation. The
[full right-square source theorem](research_mixed_unselected_right_taper_products.md),
Theorem 1, supplies this phase and a nonzero original finite packet
on all the compact parameter products used below.

## 1. An original five-cycle and an interior target

Take the cyclic word \((3,3,3,4,4)\), with indicators
\(e=(0,0,0,1,1)\). Let \((s_j^*,t_j^*)_{j=0}^4\) be its unique
critical point from the
[universal cyclic localization theorem](research_mixed_cyclic_critical_localization.md),
and put \(r_j=t_j^*\), \(c_j=\Im r_j\). In particular these are
the actual correlated heights of one original word. Outward
enclosures give the following values, displayed only approximately:
\[
\begin{array}{c|rr}
 j&\Re r_j&c_j\\\hline
0&.321231964077922&-.009675323218954\\
1&.337832495175289&-.003912773921447\\
2&.369643551416540&-.008239945927581\\
3&.307953614816794&-.048831545974913\\
4&.276142558575543&-.044504373968779
\end{array}                                                        \tag{2}
\]
All subsequent tests use the full outward intervals, not this table's
rounded entries.

Choose the exact real targets
\[
 x=(11/50,\ 2499/5000,\ 4999/10000,\ 11/50,\ 2499/5000).
                                                                    \tag{3}
\]
Coordinate 2 is the unique maximum. On \([.22,.5]\) write
\(\rho(x)=\min\{1,20(.5-x)\}\), and use the unselected
[minimum-neighbor contour](research_mixed_minimum_neighbor_contour.md)
\[
 H_j(x)=c_j\min\{\rho(x_{j-1}),\rho(x_j),\rho(x_{j+1})\},
 \qquad z_j=x_j+iH_j(x).
                                                                    \tag{4}
\]
Its five height fractions at (3) are exactly
\((.004,.002,.002,.002,.004)\).

Increase the smallest cutoff level \(\tau\) from
\(\tau_0=1/500\), lowering the maximal real coordinate by
\[
 x_2(\tau)=\tfrac12-\tfrac1{20}\tau,
 \qquad x_j(\tau)=x_j\quad(j\ne2).
                                                                    \tag{5}
\]
For \(\tau_0\le\tau<1/250\), coordinate 2 remains the unique
maximum. Exactly the heights numbered 1, 2 and 3 change, with
derivatives \(c_1,c_2,c_3\); heights 0 and 4 remain fixed.
This is the literal minimum-neighbor graph, with no independent
height relaxation.

## 2. The actual derivative is negative

Let
\[
 \Phi(z)=\sum_{j=0}^4\phi_{e_j e_{j+1}}(z_j,z_{j+1}),\qquad
 G_j=\partial_2\phi_{e_{j-1}e_j}
                   +\partial_1\phi_{e_j e_{j+1}},
                                                                    \tag{6}
\]
with cyclic indices. The original two incidences determine each
gradient. Direct differentiation along (5) gives
\[
 \left.\frac{d}{d\tau}\Re\Phi(z(x(\tau)))\right|_{\tau=\tau_0}
       =-\frac1{20}\Re G_2-\sum_{j=1}^3c_j\Im G_j.
                                                                    \tag{7}
\]

**Proposition 1.** At the original reference and target (2)--(4),
\[
 -\frac1{300}
 < -\frac1{20}\Re G_2-\sum_{j=1}^3c_j\Im G_j
 < -\frac3{1000}.
                                                                    \tag{8}
\]
The enclosed value is approximately \(-.0032005822398866\).
Even the actual derivative, retaining its positive neighbor term,
is negative. The more conservative proposed sufficient expression
\[
 D_2=-\frac1{20}\Re G_2+
                \sum_{j=1}^3\min\{-c_j\Im G_j,0\}
                                                                    \tag{9}
\]
is less than \(-1/250\), approximately \(-.0042251067426071\).
Thus restricting all real coordinates to \([.22,.5]\) does not
make this local monotonicity criterion valid.

Here is the exact validation behind (8). The checker encloses the
ten original cyclic logarithmic equations at fixed rational-decimal
centers by a complex polydisk of radius \(10^{-24}\). If \(f\)
is that original system and \(B=f'(z_0)^{-1}\), it proves
\[
 \sup\|I-Bf'(z)\|_\infty<10^{-18},\qquad
 \|Bf(z_0)\|_\infty+
       10^{-24}\sup\|I-Bf'(z)\|_\infty<10^{-24}.              \tag{10}
\]
All single and pair arguments remain in their original logarithmic
strips, and the whole polydisk lies in the universal injectivity
chamber. This identifies its zero with the already proved actual
cyclic critical point; no independent reference choice is made.

For each of the five target blocks the checker then constructs a
scalar Newton self-map of radius \(10^{-20}\), using the full
interval target parameters obtained from (10). These roots lie in
\(.20<\Re s<.46, |\Im s|<.17\), and the arguments
\(s,s+a,s+b\) all remain in \(0<\Re w<1\). Uniqueness in the
existing source theorem identifies the original conditional branch.
The exact first derivatives
\[
 \phi_a=g'(s+a)+2\pi is-(1+\eta/2)g'(a),\qquad
 \phi_b=g'(s+b)-(1+e/2)g'(b)
                                                                    \tag{11}
\]
then give (7)--(9) by directed arithmetic. In particular the positive
term \(-c_1\Im G_1\) is retained in (7).

Every target is strictly below real part \(.5\), with negative
height and positive \(-\Re g(z_j)\). Therefore the original
Fourier factors are in their relative regime, and the already
proved full conditional packets give the actual unaliased density's
rate \(\Re\Phi\) on a neighborhood of this target. The failure is
not caused by choosing a saddle that fails to represent its finite
source. By continuity, the derivative is negative on a short forward
interval in (5).

The assertion is local. It does not compare the starting phase with
the phase after every right coordinate has reached \(.45\). In
particular it neither disproves a net grouped support gap nor says
anything adverse about the original contour integral's asymptotic.

## Reproduction

```sh
python3 experiments/check_mixed_right_maximum_transport_obstruction.py
```

All decimal centers are proposals only. The original logarithmic
self-maps, source-branch rectangles, exact cutoff incidences and
strict derivative signs are independently checked at the requested
precision; the completed source record and its dependencies are bound
before and after the run.
