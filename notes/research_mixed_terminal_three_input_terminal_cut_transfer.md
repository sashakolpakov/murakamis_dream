# A terminal-coordinate enclosure for the remaining real cut

Research deduction and fixed saved-data protocol, 6 November 2026.
The completed whole-input calculation leaves the factorial left
transform cut of terminal type four inconclusive. Its height integrals
are already enclosed. This note changes only the enclosure of the
original cut marginal, using the better-controlled terminal coordinate.
It requires no new analytic evaluation. The resulting scalar sign is
not asserted here.

## 1. The same marginal on the original stationary family

Keep the incoming type-three family, preceding ordinary type four,
terminal type four, and the complete disk
\(D_3=\{|b-(.35-.01i)|\le.09\}\). Use the same exact reference
\(q_*=(e,\xi,t,a,s)\), with the original logarithmic lifts. Set
\(\tau=.15\), \(H=.01\), and \(\Delta=H-\Im a_*\).
The original cut marginal is
\[
 D_\tau(t,a)=g'(\tau+a)-g'(t+a)+2\pi i(\tau-t).
 \tag{1}
\]
The original shared-leg stationary equation gives, at \(q_*\),
\[
 D_\tau(t_*,a_*)
 =g'(\tau+a_*)+g'(s_*+a_*)-3g'(a_*)+2\pi i\tau.
 \tag{2}
\]
The [whole-input protocol](research_mixed_terminal_three_input_budget_protocol.md)
enclosed the right side as a holomorphic function of \(s,a\).
We instead enclose (1), as its own holomorphic function of \(t,a\).
Equation (2) is used only at the true stationary reference. The two
functions need not agree at the saved approximate center.

Write the saved affine enclosures as
\[
 t_*=t^0+u_t\delta+\zeta_t,\qquad
 a_*=a^0+u_a\delta+\zeta_a,\qquad
 |\delta|\le r=.09,\quad |\zeta_j|\le\eta_j.
 \tag{3}
\]
Put \(w_a=r|u_a|+\eta_a\) and
\(w_{ta}=r|u_t+u_a|+\eta_t+\eta_a\). At the saved center define
\[
 \begin{split}
 D_0&=g'(\tau+a^0)-g'(t^0+a^0)+2\pi i(\tau-t^0),\\
 D_t^0&=-g''(t^0+a^0)-2\pi i,\\
 D_a^0&=g''(\tau+a^0)-g''(t^0+a^0),\\
 L_D&=D_t^0u_t+D_a^0u_a.
 \end{split}
 \tag{4}
\]
In particular \(D_t^0=-j'(t^0+a^0)-i\pi\), where
\(g''=j'-i\pi\). Both imaginary constants in (4) are retained.

Let \(m_\tau,m_{ta}\) bound \(|g'''|\) on the full disks
centered at \(\tau+a^0,t^0+a^0\), with respective radii
\(w_a,w_{ta}\). Taylor's formula on these disks gives
\[
 \begin{split}
 D_\tau(t_*,a_*)&=D_0+L_D\delta+\varepsilon_D,\\
 |\varepsilon_D|&\le\rho_D:={}|D_t^0|\eta_t+|D_a^0|\eta_a
              +\tfrac12(m_\tau w_a^2+m_{ta}w_{ta}^2).
 \end{split}
 \tag{5}
\]
These derivative disks are not clipped to typed coordinate rectangles.
They contain every center-to-reference segment, including its posterior
error. The cut disk and its bound were saved by the completed input
calculation. The original correlated-affine record supplies the center
logarithm, center cotangent and full-disk derivative bound at \(t+a\).
Its multiplier-two tube must contain the full refined disk in (5).

## 2. Signed height product and a common real-force interval

Set \(\Delta_0=H-\Im a^0\), \(d_0=\Im D_0\), and let
\(\Delta_{\rm hi}\) be the saved upper bound for \(\Delta\).
The same elementary disk-product calculation as in the
[direct-cut proof](research_mixed_terminal_real_transform_cut_budget.md)
gives
\[
 \begin{split}
 -\Delta\Im D_\tau(t_*,a_*)\le{}&
 -\Delta_0d_0+r|\Delta_0L_D-d_0u_a|\\
 &+\tfrac{r^2}{2}
       (|u_a||L_D|+\Re(u_a\overline{L_D}))\\
 &+\Delta_{\rm hi}\rho_D
       +\eta_a(|d_0|+r|L_D|)=:U_T.
 \end{split}
 \tag{6}
\]
The positive sign before the dot product is essential. For interval
center data every operation is outward, including the linear term and
the signed constant; no midpoint is substituted without its error.
Also
\[
 \Re D_\tau(t_*,a_*)\in
 \Re D_0+[-r|L_D|-\rho_D,\ r|L_D|+\rho_D]=:\mathcal R_T.
 \tag{7}
\]
Let \(U_S,\mathcal R_S\) be the saved bounds from the other
representation (2). Both enclose the same actual value, so we may use
\[
                 U=\min(U_S,U_T),\qquad
                 \mathcal R=\mathcal R_S\cap\mathcal R_T.
 \tag{8}
\]
An empty intersection is an error in this calculation, not permission
to exclude a source point.

## 3. One fixed scalar test

Retain all saved height integrals and target intervals. With
\(I_a,I_s,I_\tau\) the saved mean imaginary cotangents and
\(\kappa=\pi\Delta\), the factorial forces are
\[
 F_s=\kappa(1-I_s),\qquad
 F_a=D_R+\kappa(3I_a-I_s-I_\tau-1),\quad D_R\in\mathcal R.
 \tag{9}
\]
The trial upper is \(U+W_\tau^+-2\pi_{\rm lower}H\), where
\(W_\tau\) is reconstructed from the saved weighted real cotangents
as \(\pi\Delta^2\int(1-\theta)(3C_a-C_s-C_\tau)d\theta\).
Use the original cubic costs \(K_s=88/5\) and
\(K_a=(49/5)(1+1/2+3/5)\), and targets \([.22,.5]\),
\([.22,.45]\). The saved real-center intervals remain unchanged.

The sum of the two cubic gain majorants is convex in \((F_s,F_a)\).
The force map (9) is affine separately in its five parameters.
Its maximum is therefore bounded by the 32 endpoint vertices of
\(\kappa,I_a,I_s,I_\tau,D_R\). This is the same proved
shared-force argument used in the completed calculation.

Perform exactly one saved-only pass: reconstruct (3)--(8), enumerate
these 32 vertices, compute 64 exact rational cubic gains with the
frozen helper, check all 64 saved witnesses independently, and add the
unchanged bare source upper for family \(\texttt{four}:0\).
Keep the old direct upper and every new constituent upper in the
record. The predeclared target is an upper below \(-1/10000\).
Either sign is final for this protocol. The already completed forced
alternative is not recalculated.

Inputs include the completed whole-input record
18f5260f3fcd18461d8dd2859d515d9c5180f53127e917debd628ebcf26a0dec,
its frozen driver 2cdcccac8295666d120d6db4b53e7862bd7e14e538a7e37f854f1b2177bd6dab,
the same refined affine and original correlated records, their proof
chain, and the original gain checker. A concrete implementation must
pin these inputs, verify their associations and containment, preserve
all failed operands, and write to a fresh output. Root and peer must
read its complete code before the sole root execution.

There are no new roots, logarithms, cotangents, source evaluations,
height slabs, parameter subdivisions, private actions or precision
retries. This test concerns one unresolved original source comparison.
It does not assert a whole-source or finite-exceptions theorem.
