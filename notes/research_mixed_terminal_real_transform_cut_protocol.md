# A fixed whole-disk protocol for the remaining real transform cuts

Research protocol, 6 November 2026. This calculation is unrun when
frozen. It applies the [direct-cut theorem](research_mixed_terminal_real_transform_cut_budget.md)
to exactly two canonical families, without new roots or source cells.
It produces sufficient upper bounds and retains every outcome.

## 1. Cases, original sources and inherited data

The external flag is \(\beta=1\), the selected height is
\(H=1/100\), and the external parameter is the whole disk
\[
 |b-b_0|\le r,\qquad b_0=.30-.052i,\qquad r=8/125.
 \tag{1}
\]
Use precisely \((\epsilon,\tau)=(0,1/2),(1,3/20)\).
The exact centers and responses and the posterior radii come from
the completed quadratic refinement, SHA256
2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331:
\[
 q_j=q_j^0+u_j\delta+\zeta_j,
 \qquad |\delta|\le r,\quad |\zeta_j|\le\eta_j.
 \tag{2}
\]
The original order is \((e,\xi,t,a,s)\). Verify the complete
refinement-to-posterior-to-split-to-affine chain, exact centers,
responses and parameter disk, and containment in the original
posterior radii and regular primitive disks. Every input hash is
checked before and after the calculation.

Reuse the immutable original integral record
9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e
and its saved audit. In particular reuse its exact outward \(\pi\)
interval, every old \(C_a,C_s,I_a,I_s\) slab enclosure,
\(Q=\Re g'(A+iH)\), and its upper \(G_H\) for
\(\Re g(A+iH)\). No old elementary value is reevaluated.
The new root images lie in the old images on which these data were
proved; all original height and target guards are retained.

The complete uniform face extraction, SHA256
37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3,
supplies the bare \(U\) values for exactly three families:
type-three mixed family 1 (real right cut), type-three raw-half
family 0 (entropy), and type-four family 0 (real left cut).
Each is combined with both complete Fourier alternatives, giving
six comparisons. The original source-domain theorem restricts
these source comparisons to actual \(K_4\); phase bounds on
\(D_4\) do not enlarge the source domain. No target is restricted
by a reference-image enclosure.

## 2. The new center and whole-tube data

Write \(a_*=A+ic\), \(\Delta=H-c>0\), and define
\[
 D=D_\tau(a_*)
   =j(\tau+a_*)-j(t_*+a_*)+i\pi(\tau-t_*),
 \quad j(z)=\Log(2\sin\pi z).
 \tag{3}
\]
This is the original chirped logarithmic difference, not a new lift.
The original zero-lift equation identifies it on the canonical
family; no enclosing midpoint is declared stationary.

The old affine record already contains \(j,j'\) at \(t^0+a^0\)
and a full regular disk bounding \(|j''|\). The only new center
argument is \(\tau+a^0\). With
\[
 w_a=r|u_a|+\eta_a,\qquad
 w_{ta}=r|u_t+u_a|+\eta_t+\eta_a,
 \tag{4}
\]
check that the old \(t+a\) radius contains \(w_{ta}\), and that
the new disk of radius \(w_a\) about \(\tau+a^0\) lies strictly
in \(0<\Re z<1\). Evaluate the new center \(j\) by one complex
sine and one logarithm, and \(j'\) by one cotangent times the
saved \(\pi\) enclosure. Require a positive real part of
\(2\sin\pi(\tau+a^0)\), fixing the prescribed logarithm.
For the new disk put \(d=\min(\Re(\tau+a^0)-w_a,
1-\Re(\tau+a^0)-w_a)>0\). One real sine supplies
\(m_\tau\ge\pi^2/\sin^2(\pi d)\ge|j''|\) on that disk.

Set, without imposing a center equation,
\[
 \begin{split}
 D^0&=j(\tau+a^0)-j(t^0+a^0)+i\pi(\tau-t^0),\\
 D_t&=-j'(t^0+a^0)-i\pi,\qquad
 D_a=j'(\tau+a^0)-j'(t^0+a^0),\\
 L&=D_tu_t+D_au_a,\qquad
 R_D=\tfrac12(m_\tau w_a^2+m_{ta}w_{ta}^2).
 \end{split}
 \tag{5}
\]
Then \(D=D^0+L\delta+D_t\zeta_t+D_a\zeta_a+E\),
\(|E|\le R_D\). Its real component gives an outward interval
\(D_R\) for \(\Re D\). Choose exact midpoint anchors
\(p_0\) for \(\Im D^0\) and \(L_0\) for \(L\), and put
\[
 \rho=\rho_0+r\rho_L+\eta_t|D_t|^+
                       +\eta_a|D_a|^++R_D.
\]
With \(\Delta_0=H-\Im a^0\), a signed upper for the linear
height term is
\[
 \begin{split}
 U_D={}&-\Delta_0p_0+r|\Delta_0L_0-p_0u_a|^+\\
 &+\frac{r^2}{2}
       (|u_a|^+|L_0|^++\Re(u_a\overline{L_0}))\\
 &+\Delta^+\rho+\eta_a(|p_0|+r|L_0|^+)
                 \ \ge -\Delta\Im D .
 \end{split}
 \tag{6}
\]
The dot-product sign is positive because the quadratic here is
\(\Im(u_a\delta)\Im(L_0\delta)\). The value (6) is never
replaced by its maximum with zero. Exact interval arithmetic and
integer square-root enclosures at mesh \(2^{-256}\) suffice for
(4)--(6).

## 3. Thirty-two fixed new height-slab enclosures

Use only \(J_j=[j/16,(j+1)/16]\), \(j=0,\ldots,15\),
in each case. The new argument is
\[
 z_\tau(\theta)=\tau+A+i\{(1-\theta)c+\theta H\}.
 \tag{7}
\]
Its real support is \(\tau+\Re a^0\pm w_a\). For either slab
endpoint its imaginary support is
\((1-\theta)\Im a^0+\theta H\pm(1-\theta)w_a\).
These endpoint supports enclose the entire slab. Check the regular
strip before and after outward Arb conversion, then evaluate one
complex cotangent on the whole argument rectangle. Keep both its
real and imaginary intervals, denoted \(C_{\tau j},I_{\tau j}\).

The exact weights are \(\lambda_j=1/16\) and
\(\omega_j=(31-2j)/512\). With all old \(a,s\) data reused,
form
\[
 V_\tau=\sum_j\omega_j(3C_{aj}-C_{sj}-C_{\tau j}),
 \qquad I_\tau=\sum_j\lambda_jI_{\tau j}.
 \tag{8}
\]
These are whole-slab integral inclusions, with no quadrature error.
Put \(\kappa=\pi\Delta\) and \(W_\tau=\pi\Delta^2V_\tau\).
The direct-cut theorem gives the exact forces and trial
\[
 \begin{split}
 F_s&=\kappa(1-I_s),\\
 F_{a,\nu}&=\Re D+\kappa(3I_a-I_s-I_\tau-1)+(1-\nu)Q,\\
 T_{\tau,\nu}&=-\Delta\Im D+W_\tau
                      +(1-\nu)\Re g(A+iH)-2\pi\nu H.
 \end{split}
 \tag{9}
\]
Use (6), the upper endpoint of \(W_\tau\), and the saved
\(G_H\) to bound the trial. Both branches keep the full selected
target \(P\); no forced-domain reduction is used.

## 4. Fixed force vertices, gains and source comparisons

Use the original scalar target intervals \([.22,.5]\) and
\(P=[.22,.45]\), the same refined real center intervals, and
\[
 K_s=88/5,\qquad
 K_a=(49/5)(\nu+1/2+\sigma_\tau),\quad
 \sigma_{1/2}=5/3,\quad\sigma_{3/20}=3/5.
 \tag{10}
\]
The gains are convex functions of their forces. The force map (9)
is multiaffine in the five intervals
\((\kappa,I_a,I_s,I_\tau,D_R)\), and also \(Q\) in the
forced case. Successive one-coordinate convexity bounds the gain
sum by its maximum at all 32 factorial or 64 forced vertices.
The rounded gain routine need not itself be convex: every evaluated
vertex upper bounds the underlying convex gain.

Evaluate precisely these 192 vertices and 384 cubic gains, using
only the pinned exact scalar routine, with an independent exact
check of all 384 witnesses. Its original main and analytic entry
points are not called. Add the appropriate uniform bare \(U\)
from the same family to each branch maximum. All six resulting
uppers, their signed margins and attaining vertices are retained.
Positive uppers remain inconclusive; no lower-bound obstruction is
inferred. No complete terminal or knot theorem is declared here.

The [driver](../experiments/certify_mixed_terminal_real_transform_cut_budget.py)
uses fixed 256-bit arithmetic and the old \(\pi\) enclosure.
The only new elementary enclosures are 34 cotangents, four sines
(two complex center sines and two real disk sines), and two logs.
There is no dilogarithm, private action, root, parameter grid,
source evaluation, changed source cell, subdivision or retry.
All counts are capped explicitly. Failure preserves the active
case, any partial witnesses and every pending case. The sole
reviewed run must use a fresh output:
repro/results/research-mixed-terminal-real-transform-cut-budget.json.gz.
