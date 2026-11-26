# Joining the terminal plane on its original source cells

Research deduction and fixed saved-data protocol, 6 November 2026.

The completed whole-disk plane estimate is valid but does not pay
every available terminal reserve. Its two terminal-type ceilings
are taken independently of the source cell on which a reserve was
proved. This note retains that association. It uses the existing
source partition and the same saved canonical family; it creates
no new parameter grid and reevaluates no analytic function.

## 1. Inverting the common affine coordinate

Keep the notation and hypotheses of the
[uniform joined-plane proof](research_mixed_terminal_uniform_joined_plane.md).
For each of its two \(D_4\) families, the certified reference obeys
\[
 a=a^0+u_a\delta+\zeta_a,\qquad
 s=s^0+u_s\delta+\zeta_s,\qquad
 |\delta|\le r=8/125,\quad |\zeta_j|\le\eta_j.
 \tag{1}
\]
The exact saved coefficient \(u_a\) is nonzero. Define the exact
Gaussian rationals
\[
            \lambda=L_0/u_a,\qquad v=u_s/u_a,
 \tag{2}
\]
where \(L_0\) is the already prescribed midpoint coefficient in
the marginal approximation. Its old proved bound is
\[
 \Im p_T=p_0+\Im(L_0\delta)+e,
                         \qquad |e|\le\rho_P.
 \tag{3}
\]
Substitution of (1) into (3), with no approximation to the inverse,
gives
\[
 \Im p_T=p_0+\Im\{\lambda(a-a^0)\}+\widetilde e,
 \qquad |\widetilde e|\le\rho_P+\eta_a|\lambda|.
 \tag{4}
\]
The old \(\rho_P\) already pays the posterior errors in (3).
The additional term pays the new substitution error
\(-\Im(\lambda\zeta_a)\). Counting an occurrence of the same
posterior perturbation in both terms is conservative; it does not
omit any error or justify subtracting one of them.

A sharper alternative follows from the actual Taylor decomposition
used to prove (3). With its saved \(\rho_0,\rho_L,D_s,D_a\)
and Taylor remainder \(R_P\), the same substitution yields
\[
 |\widetilde e|\le
 \rho_0+r\rho_L+\eta_s|D_s|^+
                         +\eta_a|D_a-\lambda|^++R_P.
 \tag{5}
\]
Indeed the coefficient of \(\zeta_a\) becomes \(D_a-\lambda\)
before taking its modulus. The uncertainty in \(L-L_0\) still costs
\(r\rho_L\). Both (4) and (5) are valid on the entire family, so
let \(\rho_*\) be the smaller of their proved upper bounds.
All terms are saved intervals or rational complex coefficients;
modulus uppers need only integer square roots.

Similarly,
\[
 s=s^0+v(a-a^0)+\widetilde\zeta_s,
 \qquad |\widetilde\zeta_s|\le\eta_s+|v|\eta_a.
 \tag{6}
\]
This enclosure is simultaneous with (4)--(5). No derivative of a
clipped interval and no new canonical solution is used.

## 2. An exact cellwise maximum for the vertical plane term

Let \(C\) be one of the original source cells retained in the
[uniform face extraction](research_mixed_terminal_uniform_face_reserves.md).
Let
\[
 J_C=[A_-,A_+]\times[c_-,c_+]
 \tag{7}
\]
be its saved closed intersection with the complete refined
\(a_*\)-image rectangle. This cell restricts the **reference**
\(a_*=A+ic\); all current real targets, including \(a_R\),
continue to range independently over their original full intervals.
Only actual canonical parameters whose reference belongs to \(J_C\)
are being bounded on that cell.

Write \(a^0=A^0+ic^0\) and \(\lambda=\lambda_R+i\lambda_I\).
Because \(H-c>0\), equation (4) implies
\[
 \Delta\Im p_T\le
 \max_{(A,c)\in J_C}
 (H-c)\{p_0+\lambda_R(c-c^0)+\lambda_I(A-A^0)\}
                         +(H-c_-)\rho_*.
 \tag{8}
\]
The maximization has a closed exact formula. Its expression is affine
in \(A\), so use the two endpoints \(A_-,A_+\). For either endpoint
put
\[
 b_A=p_0-\lambda_Rc^0+\lambda_I(A-A^0),\qquad
 f_A(c)=Hb_A+(H\lambda_R-b_A)c-\lambda_Rc^2.
 \tag{9}
\]
If \(\lambda_R>0\), its maximum on \([c_-,c_+]\) is at
\[
 c=\operatorname{clip}
       \left(\frac{H\lambda_R-b_A}{2\lambda_R},c_-,c_+\right).
 \tag{10}
\]
If \(\lambda_R\le0\), the maximum is the larger of the two
endpoint values. This includes the linear case \(\lambda_R=0\).
Equations (9)--(10) use exact rational arithmetic, not an optimizer
proposal or a search for a new reference point. They also cover
zero-width boundary intersections.

For the ordinary-index center, apply (6) to the full rectangle (7),
using exact real-linear interval arithmetic, then intersect its
resulting real interval with the proved global \(\Re s_*\) interval.
Both contain the actual center, so the intersection remains valid.
An empty intersection proves that this cell contains no canonical
reference of the family; retain that contradiction as a witness
rather than silently removing the cell. Otherwise it supplies a
narrower center interval for the ordinary scalar cost.

## 3. The joined defect paired with its own reserve

Keep the old saved normalized cotangent means
\(\overline I_a,\overline I_s\) and plane integral interval
\(\mathcal V_P\). They remain valid on the same family and hence
on every subset selected by (7).

The old own-force interval \([q_-,q_+]\) encloses the scalar function
\(Q(A)=\Re g'(A+iH)\) on its full original real interval
\([a_-^{\rm old},a_+^{\rm old}]\). The frozen integral proof also
gives its value bound \(G_H^+\) at the specific upper endpoint:
\(\Re g(a_+^{\rm old}+iH)\le G_H^+\), by the log-sine chord
bound there. This endpoint fact, not just a family-wide value bound,
justifies the following narrower cell bound:
\[
 G_{H,C}^+=G_H^+-q_-(a_+^{\rm old}-A_+).
 \tag{11}
\]
Indeed integrate \(\partial_A\Re g(A+iH)=Q(A)\ge q_->0\)
backwards from that old upper endpoint. Every cell is contained in
the old interval, and all these scalar points remain on the original
regular strip; they need not themselves be canonical references.

The cubic curvature bound at height \(H\) also gives
\(Q'(A)\ge(49/5)(.5-A)\). Set
\(K_0(A)=(49/10)(A-A^2)\). A new force interval is
\[
 \begin{split}
 Q_C^-&=\max\{q_-,q_-+K_0(A_-)-K_0(a_-^{\rm old})\},\\
 Q_C^+&=\min\{q_+,q_+-K_0(a_+^{\rm old})+K_0(A_+)\}.
 \end{split}
 \tag{12}
\]
For example \(Q(A_-)\ge Q(a_-^{\rm old})+
K_0(A_-)-K_0(a_-^{\rm old})\), and the old lower endpoint bounds
\(Q(a_-^{\rm old})\). The upper bound is the same integral from
\(A_+\) to \(a_+^{\rm old}\). The old interval endpoints are
bounds, not assumed attained values. Monotonicity covers every
\(A\) in the cell. Equations (11)--(12) require only exact saved
endpoints and rational polynomials. No cotangent, logarithm or height
integral is evaluated again.

Set \(\mathcal\Delta_C=[H-c_+,H-c_-]\) and
\(\mathcal K_C=\mathcal\Pi\mathcal\Delta_C\).
Use (8) as \(U_{P,C}\), and put
\[
 \begin{split}
 W_{P,C}^+&=\sup(\mathcal\Pi\mathcal\Delta_C^2\mathcal V_P),\\
 J_{1,C}^+&=U_{P,C}+W_{P,C}^+-\pi_{\rm lower}H,\\
 J_{0,C}^+&=U_{P,C}+W_{P,C}^++G_{H,C}^+/2.
 \end{split}
 \tag{13}
\]
Use the exact shared force formulas
\[
 G_s=\kappa(1-I_s),\quad
 G_{a,1}=\kappa(\tfrac32I_a-I_s-\tfrac12),\quad
 G_{a,0}=G_{a,1}+Q/2,\qquad Q\in[Q_C^-,Q_C^+]
 \tag{14}
\]
with \(\kappa\in\mathcal K_C\). The two scalar costs have
\(K_s=88/5\), \(K_{a,\nu}=(1+\nu)49/10\), center intervals
from (6)--(7), and unchanged target intervals \([.22,.5]\) and \(P\).
The same convex-vertex argument as before gives a cellwise plane
ceiling \(E_{C,\nu}^+\) from eight factorial or sixteen forced
vertices, each with two scalar gains.

For each source family \(f\), retain its own original-cell bound
\(u_{C,f}\), not the maximum over other cells. The source reserve
transport and halfweight allocation then give the exact implication
\[
 \sup D_{\epsilon,\nu,f}
       \le\max_{C\ {\rm retained}}
                     \{E_{C,\nu}^++u_{C,f}\}.
 \tag{15}
\]
The source cells cover the complete reference image. At every actual
reference choose a cell containing it; both its plane ceiling and
its own source reserve apply to that same reference and every
original target. Taking the maximum proves (15). Any source-null
job remains unresolved unless an exact empty-reference witness
already removes that entire intersection. No average reserve or
unrelated cell's best bound is substituted.

## 4. Fixed protocol and scope

Use the immutable
[face extraction](../repro/results/research-mixed-terminal-uniform-face-reserves.json),
SHA256 37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3,
and only its two \(\beta=1\) cases. They contain 45 source-cell
intersections for terminal type three and 25 for terminal type four.
The already completed
[plane result](../repro/results/research-mixed-terminal-uniform-joined-plane.json),
SHA256 4bfa03e1c61a4e34d9b6d549b5e9d666b15df606078d02258dae340055e3ee88,
supplies (3), its Taylor witnesses, and the saved plane integrals and
forces. Bind the refined family record and all inherited inputs.

Verify exact case/reference associations, each recorded cell and
closed intersection, the inherited coverage and all source-job
associations. Each family's `contributing_jobs` entry carries its
`original_cell_index` and exact `decoded_upper_rational`; those
identify \(u_{C,f}\) without parsing or reevaluating the old source.

Process these 70 intersections once, with no subdivision, replacement
or new grid. The maximum work is 1,680 force vertices and 3,360 scalar
cubic gains, with an independent rational check of each gain. The
exact two-endpoint quadratic formula (9)--(10) is evaluated once per
cell. Retain every cell, all nine source-family comparisons, all
intermediate bounds, and any empty-image or unresolved witness.
All planned outcomes remain visible regardless of sign.

The plane statements concern the canonical family on \(D_4\).
Combining them with source reserves in (15) is restricted to the
original source domain. The
[canonical source-domain theorem](research_mixed_terminal_canonical_source_domain.md)
supplies those conditions throughout \(K_4\), including the actual
word references in its scope. It does not identify the whole
auxiliary \(D_4\), or every independent point of (7), with the
finite source. No new root, analytic function, target search or
source evaluation is part of this protocol. Its scalar signs have
not been calculated, and no complete kernel or knot theorem is
asserted here.
