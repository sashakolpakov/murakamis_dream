# A uniform joined-terminal-plane budget from saved affine data

Research deduction and bounded saved-data protocol, 6 November 2026.

The terminal reference plane can pay a profile that lies strictly
below it, even when it cannot pay the main terminal profile. This
note gives a uniform bound for that joined plane on both canonical
families over \(D_4\). It retains the common complex input parameter
in the plane's first-order vertical term. All required analytic
values are in the completed records; no new analytic evaluation is
needed. The proposed scalar ceilings have not yet been calculated.

## 1. Allocation and the two scalar costs

Use exactly \(B_T,p_T,E_\nu\) from the
[reserved-plane transfer theorem](research_mixed_terminal_reserved_plane_transfer.md),
equations (2)--(4), with \(\beta=1\), \(\epsilon=0,1\),
and \(H=1/100\). Thus the terminal receives half the complete
selected modulus and the neighboring ordinary block receives the
other half. Both alternatives keep \(a_R\in P=[.22,.45]\).
The original incoming affine tangent is subtracted in full.

At an actual canonical reference write \(a_*=A+ic\),
\(\Delta=H-c>0\), and \(a_\theta=A+i(c+\theta\Delta)\).
Shared-leg stationarity gives the exact original marginal
\[
       p_T=\tfrac32g'(a_*)-g'(s_*+a_*).
 \tag{1}
\]
Put \(C_a+iI_a=\cot(\pi a_\theta)\) and
\(C_s+iI_s=\cot(\pi(s_*+a_\theta))\). The lifted joined-plane
values and its two nonzero real forces are
\[
 \begin{split}
 J_1&=\Delta\Im p_T+
       \pi\Delta^2\int_0^1(1-\theta)(\tfrac32C_a-C_s)\,d\theta-\pi H,\\
 J_0&=J_1+\tfrac12\Re g(A+iH)+\pi H,\\
 G_s&=\pi\Delta\int_0^1(1-I_s)\,d\theta,\\
 G_{a,1}&=\pi\Delta\int_0^1(\tfrac32I_a-I_s-\tfrac12)\,d\theta,\\
 G_{a,0}&=G_{a,1}+\tfrac12\Re g'(A+iH).
 \end{split}
 \tag{2}
\]
These are the original formulas (7) of the reserved-plane theorem,
with \(g''=\pi\cot-i\pi\) integrated along the same height
segment. In particular the linear term \(\Delta\Im p_T\) is
retained; it does not cancel as in the actual terminal main action.

The [symmetric pair inequality](research_mixed_terminal_symmetric_pair_costs.md)
applied to the two ordinary pairs improves the plane's simultaneous
Hessian bound to
\[
 -E_\nu''\succeq\operatorname{diag}
   \left(g_{h_b}''(b_R),\ 2g_{h_s}''(s_R),\
                    \tfrac{1+\nu}{2}g_H''(a_R)\right).
 \tag{3}
\]
The plane's own nonnegative quadratic cost is discarded. Its
\(s\)-independence preserves the full-input ordinary index barrier,
so \(s_R\in[.22,.5]\) suffices for the original maximum.
The incoming force is zero. Consequently
\[
 \sup E_\nu\le J_\nu+
   \mathcal B_s(G_s)+\mathcal B_{a,\nu}(G_{a,\nu}),
 \quad K_s=88/5,\quad K_{a,\nu}=(1+\nu)49/10,
 \tag{4}
\]
where the moving-center majorants \(\mathcal B\) are those of
[the shared-force lemma](research_mixed_terminal_shared_force_vertices.md),
on targets \([.22,.5]\) and \(P\). The certified refined
coordinate rectangles supply their reference-center intervals.
All heights and pair domains are inherited from the completed
whole-D4 main comparison; no terminal-index localization is used
in (3)--(4).

## 2. A correlated bound for the linear vertical term

Write the certified common affine family as
\[
 s=s^0+u_s\delta+\zeta_s,\qquad
 a=a^0+u_a\delta+\zeta_a,\qquad
 |\delta|\le r=8/125,\quad |\zeta_j|\le\eta_j.
 \tag{5}
\]
The exact coefficients and errors are those of the completed
[quadratic residual refinement](research_mixed_terminal_quadratic_residual_refinement.md).
Define the explicit holomorphic function
\(P(s,a)=\tfrac32g'(a)-g'(s+a)\). Equation (1) identifies it
with the terminal marginal only on the canonical family. Taylor
expansion of this explicit function on a full containing tube is
valid also at nonstationary points.

At the exact affine center put
\[
 \begin{split}
 P^0&=\tfrac32g'(a^0)-g'(s^0+a^0),\\
 k_a^0&=g''(a^0),\qquad k_{sa}^0=g''(s^0+a^0),\\
 L&=\tfrac32k_a^0u_a-k_{sa}^0(u_s+u_a),\\
 D_s&=-k_{sa}^0,\qquad D_a=\tfrac32k_a^0-k_{sa}^0.
 \end{split}
 \tag{6}
\]
All these are enclosed by saved center logarithms and cotangents.
On the original regular strip,
\(g'(z)=j(z)+i\pi(1/2-z)\),
\(g''(z)=j'(z)-i\pi\), where \(j=\Log(2\sin\pi z)\).
Thus no new logarithm is needed to form (6).

Choose \(p_0\) to be the exact midpoint of the saved interval for
\(\Im P^0\), and \(L_0\) to be the exact Cartesian midpoint of
the computed interval for \(L\). Let \(\rho_0\) enclose
\(|\Im P^0-p_0|\) and \(\rho_L\) enclose \(|L-L_0|\).
Let \(m_a,m_{sa}\) be the original saved bounds for
\(|g'''|=|j''|\) on the respective full multiplier-one argument
disks. Check that the following radii are contained in those disks:
\[
 w_a=r|u_a|+\eta_a,\qquad
 w_{sa}=r|u_s+u_a|+\eta_s+\eta_a.
 \tag{7}
\]
Each common coefficient is added before taking its modulus.
Taylor's formula gives
\[
 \left|\Im p_T-p_0-\Im(L_0\delta)\right|\le\rho_P,
 \quad
 \rho_P=\rho_0+r\rho_L+\eta_s|D_s|^+
       +\eta_a|D_a|^++\tfrac12(\tfrac32m_aw_a^2+m_{sa}w_{sa}^2).
 \tag{8}
\]
The superscript \(+\) denotes an outward modulus upper bound.
The full argument disks are convex, so the straight Taylor segments
from the exact center stay in their original strips. The errors in
(8) cover both the affine motion and the posterior perturbations.

Put \(\Delta_0=H-\Im a^0\), and let \(\Delta^+\) be the
certified upper endpoint of the actual positive displacement.
Since \(\Delta=\Delta_0-\Im(u_a\delta)-\Im\zeta_a\),
equation (8) implies
\[
 \begin{split}
 \Delta\Im p_T\le U_P:={}&\Delta_0p_0
  +r|\Delta_0L_0-p_0u_a|\\
 &+\frac{r^2}{2}\bigl(|u_a||L_0|-\Re(u_a\overline{L_0})\bigr)\\
 &+\Delta^+\rho_P+\eta_a(|p_0|+r|L_0|).
 \end{split}
 \tag{9}
\]
To prove the quadratic term, write \(\delta=x+iy\). The largest
eigenvalue of the real quadratic form
\(-\Im(u_a\delta)\Im(L_0\delta)\) is
\((|u_a||L_0|-\Re(u_a\overline{L_0}))/2\).
It is nonnegative, so its maximum on the radius-\(r\) disk is
exactly the displayed quadratic bound. The linear term is the
support of the combined coefficient, rather than the sum of two
independent supports. The final two terms bound, respectively,
\(\Delta\) times the error in (8), and the posterior height error
times the affine approximation to \(\Im p_T\).

## 3. Finite scalar ceiling and the proposed protocol

Reconstruct from the old sixteen cotangent slabs the normalized
plane interval
\[
 \mathcal V_P=\sum_{j=0}^{15}\frac{31-2j}{512}
                    (\tfrac32\mathcal C_{aj}-\mathcal C_{sj}).
 \tag{10}
\]
With the refined displacement interval, let
\(W_P^+=\sup(\mathcal\Pi\mathcal\Delta^2\mathcal V_P)\).
The old saved upper \(G_H^+\) for \(\Re g(A+iH)\) remains
valid on the same canonical family. Consequently valid trial uppers
are
\[
       J_1^+=U_P+W_P^+-\pi_{\rm lower}H,
       \qquad J_0^+=U_P+W_P^++G_H^+/2.
 \tag{11}
\]
For the gains, retain the common \(\kappa=\pi\Delta\),
\(\overline I_a\), and \(\overline I_s\):
\[
 G_s=\kappa(1-\overline I_s),\quad
 G_{a,1}=\kappa(\tfrac32\overline I_a-\overline I_s-\tfrac12),\quad
 G_{a,0}=G_{a,1}+Q/2,
 \tag{12}
\]
where \(Q=\Re g'(A+iH)\) uses its old saved interval.
The sum of the two gain majorants is convex in the force pair.
The force map is separately affine in these variables. Its upper
therefore requires eight endpoint vertices for \(\nu=1\), and
sixteen for \(\nu=0\). Adding (11) gives a uniform ceiling for
each of the four joined planes. No force sign is assumed.

The fixed proposed calculation uses exactly the two \(\beta=1\)
cases, the existing sixteen cotangent slabs per case, and the new
certified posterior errors. It reconstructs two center marginal
approximations (6)--(9), two normalized intervals (10), and 48 force
vertices in total, each with two scalar cubic gains: 96 gain calls
and 96 independent rational checks. All modulus and square-root
bounds use rational arithmetic and integer square roots. There are
no analytic calls, new roots, input cells, revised tubes, alternate
trials or retries. The maximum per alternative is recorded whatever
its sign or size. The implementation and its bindings require review
before that single saved-only calculation.

If an original terminal profile lies below \(B_T\) by a uniform
reserve \(\rho\), the original halfweight allocation implies a
joint bound \(\sup E_\nu-\rho\), exactly as in the reserved-plane
theorem. A finite-source application remains restricted to its
actual compact reference domain, including every oriented-image
and inverse-feasibility condition. A positive plane ceiling is
useful only when the corresponding proved reserve exceeds it;
this protocol by itself asserts no profile sign or knot theorem.
