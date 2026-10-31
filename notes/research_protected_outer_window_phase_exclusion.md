# Regular-window phase exclusion with one protected outer face

31 October 2026. **research local theorem.**
This is the exact scalar-active extension of the
[regular-window phase theorem](research_regular_spectral_window_phase_exclusion.md).
It treats \(y=0\) and \(x,b,c\ne0\), with their moduli uniformly
positive. It does not cover a zero middle weight or two zero outer weights.
Its conclusion is relative to the original positive window envelope,
not a comparison with hyperbolic volume.

## 1. The literal protected specialization has three states

Use \(N\ge3\), \(d=N-1\), \(\sigma=-2\cos(2\pi\delta)\), and
\[
 \alpha_r=2\cos\frac{(2r+1)\pi}{N}-\sigma,
 \qquad \beta_r=4\sin^2\frac{\pi r}{N},\qquad a_r=\beta_rx.
 \tag{1}
\]
Setting the original outer variable \(y\) equal to zero removes exactly
the dimer terms of the original continuant. Thus, for every \(i\le j\),
\[
 K_{i,j}(x,0)=x^{j-i}\prod_{r=i+1}^{j}\beta_r,
 \qquad K_{i,i}=1.
 \tag{2}
\]
This is a polynomial specialization, not a limiting estimate involving
an inverse power of \(y\).

Set \((B_{-1},R_{-1},Z_{-1})=(1,0,0)\). The exact recurrence is
\[
 \begin{aligned}
 B_r&=b\alpha_rB_{r-1},\\
 R_r&=B_{r-1}+a_rR_{r-1},\\
 Z_r&=R_r+c\alpha_rZ_{r-1}.
 \end{aligned}\tag{3}
\]
Equivalently,
\[
 \begin{pmatrix}B_r\\R_r\\Z_r\end{pmatrix}
 =\begin{pmatrix}
 b\alpha_r&0&0\\1&a_r&0\\1&a_r&c\alpha_r
 \end{pmatrix}
 \begin{pmatrix}B_{r-1}\\R_{r-1}\\Z_{r-1}\end{pmatrix}.
 \tag{4}
\]
The direct before-to-after entry \(1\) retains the path \(i=j\).
Induction gives
\[
 Z_M=\sum_{0\le i\le j\le M}
 b^ic^{M-j}\prod_{r<i}\alpha_r\prod_{j<r\le M}\alpha_r
 K_{i,j}(x,0).
 \tag{5}
\]
For the original LEFT half-row source take
\(M=\lfloor N/2\rfloor-1\) and
\(A_{\mathrm{rest}}^\alpha=\prod_{r=M+1}^{d}\alpha_r\). The raw source is
\[
 (-1)^dH_{V,\mathrm{LEFT}}(x,b,c,0)
       =A_{\mathrm{rest}}^\alpha c^{d-M}Z_M.
 \tag{6}
\]
For the full numerator take \(M=d\) and the empty omitted product:
\((-1)^dH_V(x,b,c,0)=Z_d\). These are the same source normalization and
sign as in the [four-state identity](research_original_one_sided_four_state_transfer.md).
All omitted-half modes and sampled zeros remain exact.

## 2. Strict regular windows and their three-phase alignment

Let \(x_0,b_0,c_0\) range over a fixed positive compact set and
\(\delta\) over a compact subset of \((0,1/2)\). Put
\[
 \alpha(t)=4[\cos^2(\pi t)-\sin^2(\pi\delta)],\qquad
 L_\delta(t)=\frac{4x_0\sin^2(\pi t)}{|\alpha(t)|}.
\]
Choose fixed disjoint row windows \(I_\mu<I_\nu\) inside \((0,1)\),
both staying away from \(1/2\pm\delta\). In the half-row case they lie
inside \((0,1/2)\). Assume
\[
 F(\mu,\nu)=\mu\log b_0+(1-\nu)\log c_0
          +\int_{\mu}^{\nu}\log L_\delta(t)\,dt,
 \tag{7}
\]
has a uniformly strict interior maximum \((\mu_*,\nu_*)\) on those
windows. The logarithmic poles in the integral are interpreted integrably.
The maximum stays a fixed distance from each boundary, and the boundary
values of each separated endpoint action have a fixed strict loss. This
last formulation makes the required uniformity explicit.

Restrict (5) to all integers \(i\in NI_\mu\), \(j\in NI_\nu\), and
multiply by the exact prefactor in (6). Call the resulting raw polynomial
\(W_N\). Let \(E_N\) be the same window sum using \(x_0,b_0,c_0\),
absolute values of unused \(\alpha\)'s and of the omitted product,
and the positive monomer product (2). The windows are disjoint, so the
diagonal path is outside this restricted piece, while (4) retains it in
the full source.

Write \(x=x_0e^{i\vartheta_x}\), and similarly for \(b,c\). Define
\[
 s_\mu=\arg\alpha(\mu_*),\qquad
 s_\nu=\arg\alpha(\nu_*),\qquad s_\mu,s_\nu\in\{0,\pi\}.
\]
The exact local alignment is
\[
 \vartheta_x=\vartheta_b+s_\mu
            =\vartheta_c+s_\nu\pmod{2\pi}.
 \tag{8}
\]
There is no phase assigned to the zero variable \(y\). In a LEFT
straddling window \(s_\mu=0\), \(s_\nu=\pi\), so (8) is
\(\vartheta_x=\vartheta_b=\vartheta_c-\pi\).

For every fixed \(\varepsilon>0\), there are uniform
\(C,\kappa>0\) and \(N_0\) such that
\[
 \boxed{|W_N|\le Ce^{-\kappa N}E_N}\tag{9}
\]
whenever the supported phase triple stays at least \(\varepsilon\)
from (8). The distance can be the minimum over the common phase of the
maximum of the three circular errors, or the equivalent maximum of the
two relative-phase errors.

## 3. Exact start and stop switches

Write \(p_-\le i\le p_+<q_-\le j\le q_+\) for the integer windows.
The start and stop matrices are the scalar-block matrices
\[
 T_r^{\mathrm{start}}=
 \begin{pmatrix}a_r&1\\0&b\alpha_r\end{pmatrix},
 \qquad
 T_r^{\mathrm{stop}}=
 \begin{pmatrix}c\alpha_r&a_r\\0&a_r\end{pmatrix}.
 \tag{10}
\]
Let \(U_N,V_N\) be their respective off-diagonal product entries. Then
\[
 \begin{aligned}
 W_N={}&(-1)^dA_{\mathrm{rest}}^\alpha c^{d-M}
 \left(\prod_{q_+<r\le M}c\alpha_r\right)V_N
 \left(\prod_{p_+<r<q_-}a_r\right)U_N
 \left(\prod_{r<p_-}b\alpha_r\right).
 \end{aligned}\tag{11}
\]
A start at \(i\) inserts \(1\), and the stop at \(j\) includes the
active step \(a_j\). Thus (11) contains exactly (2), not a shifted path.
There is no extra factor of \(N\) or auxiliary normalization.

## 4. Scalar separation and both boundary terms

If (8) fails by a fixed amount, at least one supported middle phase
mismatches \(\vartheta_x\) by a fixed amount. On its window,
\(a_r\) and the relevant middle scalar have strictly positive moduli
bounded above and below. For two such moduli \(u,v\ge m_*>0\),
\[
 |ue^{i\phi}-ve^{i\psi}|
       \ge2m_*\left|\sin\frac{\phi-\psi}{2}\right|.
 \tag{12}
\]
The exact coefficients are analytic in the scaled row variable, with
\[
 \alpha_h(t)=4\cos^2(\pi(t+h/2))-4\sin^2(\pi\delta),
 \qquad a(t)=4x\sin^2(\pi t),\qquad h=N^{-1}.
\]
The scalar gap (12) therefore extends to a fixed complex neighborhood
of the selected window, uniformly for large \(N\). This is the full
Sylvester hypothesis in the
[analytic switching theorem](research_analytic_switching_suppression.md).
No secondary eigenvalue, positive two-state gauge or outer-relative-phase
estimate is involved.

Apply that theorem to the mismatched matrix in (10). Keep both pure
endpoint terms and the residual switch sum. The residual coupling is
\(O(e^{-cN})\); it remains multiplied by the original scalar products.
Here those active products concatenate exactly:
\[
 K_{v,w}(x,0)K_{u,v}(x,0)=K_{u,w}(x,0).
 \tag{13}
\]
Their absolute values are exactly the corresponding positive products.

To compare with \(E_N\), first factor out all common unused products
outside the two windows. These may include sampled zeros in the full-row
case, and the omitted-half product may also vanish. If a common factor
vanishes, both sides of (9) vanish. Otherwise the same estimate applies to
the remaining variable products, with no bound on an inverse common factor.
The variable \(\alpha\)'s stay away from zero, while \(\beta\) stays
positive on the active compact interval. Their logarithmic Riemann sums
give uniform rate differences equal to the differences of (7), with
\(O(\log N)\) errors.

Each gauge endpoint term places the relevant start or stop at a window
boundary, up to one mesh step. Strict endpoint maximality and separation
of the two endpoint actions give a fixed exponential loss relative to
the positive interior window sum. Both endpoint terms are retained.
For the residual, (13) reassembles the active products exactly; the
one-row factors and their reciprocals on the selected windows are
uniformly bounded. Each insertion is therefore bounded by its
\(e^{-cN}\) residual factor times a constant multiple of an original
positive switch summand, up to one mesh shift. Summing polynomially many
locations costs only a polynomial factor. Absorb it in a smaller
exponential constant and restore all common factors. This proves (9).

## 5. Protected targets and the shared phase graph

In the original marked coefficient the protected face has target zero.
All polynomial exponents are nonnegative, so specializing that variable
to zero is exactly the required constant-term restriction. No phase or
Cauchy integration variable is supplied for that face.

Consequently these ports may be combined with the four-positive ports in
the [cycle-packing criterion](research_regular_window_cycle_packing.md).
Use just the three supported incidences \((x,b,c)\), with labels
\((0,s_\mu/\pi,s_\nu/\pi)\). The local loss and the unconditional
positive-envelope bound have exactly the forms needed there. The circular
telescoping, fractional packing and original shared-target Cauchy arguments
are unchanged.

The case \(x=0\), \(y,b,c\ne0\), follows by exchanging the two outer
variables in the literal recurrence. Neither case permits a forced zero
middle, two zero outers, a boundary maximum or a window touching a pole.
No universal packing capacity, envelope margin or filled-volume theorem
is inferred from this extension.

The finite dictionary is an algebraic specialization of the already
four-state and restricted-window identities, whose existing
audits include a zero outer weight. The exponential estimate above is
analytical; no additional finite-level test is claimed as its proof.