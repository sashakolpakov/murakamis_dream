# Extending the initial 4,4 boundary interval with its complete first weight

Private research corollary, 10 November 2026. The completed first-four/four
estimate gives the same rectangular enlargement and boundary propagation
as the initial-three/four assembly. The first diagonal weight is now
present in full. It is already paid inside the joint first-pair bound;
no additional estimate or deletion of that weight is made.

## 1. Exact source and allocation

Fix an actual positive three/four open word of length \(m\ge3\) beginning
with \(4,4\). Write \(n_j=3+\epsilon_j\), so
\(\epsilon_1=\epsilon_2=1\), and put
\[
 h=m-1,\qquad k_4=\sum_{j=1}^{m}\epsilon_j,\qquad
 r_j=a_j+ic_j,\quad z_j=x_j+ic_j,\quad X_j=e^{-2\pi iz_j}.
\tag{1}
\]
The reference, heights, markings and logarithmic lifts are the original
ones. With the terminal variable contracted exactly, the retained
unselected integrand is
\[
 \mathscr J^c_N=
 U_{1,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal V_{\epsilon_m,N}(w_R,X_h)
 \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}.
\tag{2}
\]
Its external scalar is
\(\kappa_N^{m+k_4}N^{m+k_4-1}\), with \(|\kappa_N|=1\).
The full terminal transform includes every terminal row, its own weight
and Fourier alternatives. There is no further terminal selection in (2).

Set
\[
 P=[11/50,9/20],\quad E=[1/10,11/50],\quad
 \kappa_0=1/2500000,\quad
 \gamma_{44}=\kappa_0(a_1-11/50)^2
                  >\kappa_0(13/500)^2>0.
\tag{3}
\]
The strict bound is the actual first-four endpoint bound, not a new
restriction on an independently chosen reference.

Let \(L_1,\phi_j,\Pi\) be the allocated phases of the
[whole unselected plateau theorem](research_mixed_full_unselected_plateau.md).
In particular \(L_1=\mathcal T_1-g/2\); each ordinary incidence and
the terminal incidence retain their original halfweights. Write
\[
 \Phi(\mathbf z)=L_1(z_1)+\sum_{j=2}^{h}
                   \phi_j(z_{j-1},z_j)+\Pi(z_h),\qquad
 M=\Re\Phi(\mathbf r).
\tag{4}
\]
This is the original calibrated action, with \(\nabla\Phi(\mathbf r)=0\).
The [complete first-four/four theorem](research_mixed_first_four_four_true_last_row_calibration.md),
Corollary 3, bounds the literal product
\[
 |U_{1,N}(w_L,X_1)C_{1,N}(X_1,X_2)|
                   |d_N(X_1)|\,|d_N(X_2)|^{1/2}
\tag{5}
\]
at rate
\[
 \Re L_1(r_1)+\Re\phi_2(r_1,r_2)
 +\Re\partial_2\phi_2(r_1,r_2)(x_2-a_2)
 -\kappa_0(x_2-a_2)^2-\gamma_{44}+\tau_2.
\tag{6}
\]
Thus (5) has already consumed the entire first weight. Only the other
half of the second weight remains for the next incidence.

## 2. Rectangular enlargement and the same nonzero coefficient

**Corollary 1.** For every \(\tau>0\), on
\(E\times P^{h-1}\), the complete integrand (2) satisfies
\[
 |\mathscr J^c_N|
 \le C_{m,\tau}N^{A_{m,\tau}}
 \exp N\left\{M-\gamma_{44}
               -2\kappa_0\sum_{j=2}^{h}(x_j-a_j)^2+\tau\right\}.
\tag{7}
\]
Both parities and sufficiently small fixed ordinary-color disks about
\((-2,-2)\) are included. Fixed color derivatives obey the same rate
on smaller disks.

*Proof.* Multiply (5)--(6) by the complete ordinary supporting planes
for \(j=3,\ldots,h\) and the complete terminal plane. Their remaining
halfweights multiply to exactly (2). Original stationarity cancels all
linear terms; their constants sum to \(M\), and each coordinate
\(j\ge2\) receives two quadratic losses. If \(m=3\), then \(h=2\):
the terminal transform supplies the other halfweight and quadratic
loss at coordinate two directly. No further ordinary factor is needed.
Allocate the finitely many source tolerances within \(\tau\), intersect
their fixed color disks, and use Cauchy's formula on smaller disks.
All weight identities are modulus identities at zeros as well; no
Fourier factor is divided out. This proves (7). \(\square\)

Let \(\mathcal Z_N^+\) be the scalar following (2) times its integral
over
\[
 [1/10,9/20]\times P^{h-1}
\tag{8}
\]
at the same fixed heights and inherited angular orientation. Let
\(\mathcal Z_N^P\) be the known integral over \(P^h\). Their difference
is exactly the integral over \(E\times P^{h-1}\), up to a shared
measure-zero boundary. Consequently
\[
 |\mathcal Z_N^+-\mathcal Z_N^P|
             \le CN^A e^{N(M-\gamma_{44}+\tau)}.
\tag{9}
\]
This is an additive identity of restricted integrals; no contour
homology is asserted for any omitted region.

The whole plateau theorem therefore gives, on smaller fixed color disks,
\[
 \mathcal Z_N^+(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
 e^{N\mathcal F_m(\mathbf w)}
                    \{1+O_{\rm hol}(N^{-1})\},\qquad A_m\ne0,
\tag{10}
\]
with exactly its original action, coefficient, Gaussian branch and
orientation. Indeed choose \(\tau<\gamma_{44}/8\) in (9), then shrink
the disks so that \(\Re\mathcal F_m>M-\gamma_{44}/8\) and \(A_m\)
is bounded away from zero. The normalized difference is holomorphic
and exponentially small. Cauchy's formula preserves every fixed
normalized color jet. The first-four weight changes neither the
inherited power \(N^{-3/2}\) nor its coefficient: it was already in
both the plateau source and (5).

## 3. A left boundary state with arbitrary controlled middle

Use the safe ordinary cuts \(p,\ldots,q\), eight-vertex safety halo
and protected triples of
[completed boundary-state propagation](research_mixed_completed_boundary_state_propagation.md).
These triples are \(T_L=\{p-2,p-1,p\}\) and
\(T_R=\{q-1,q,q+1\}\), with \(q\ge p\).
Keep the first pair outside the protected triples and inside the
physical prefix through \(p-1\). In that prefix let \(x_1\in E\),
\(x_2,\ldots,x_{p-1}\in P\), with every selection zero and every
height fixed at its actual reference height. Its exact cut modulus is
\[
 L_N=|U_{1,N}|
 \prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
 \prod_{j=1}^{p-2}|d_N(X_j)|^{\epsilon_j}
                 |d_N(X_{p-1})|^{\epsilon_{p-1}/2}.
\tag{11}
\]
In particular its first weight is present in full. Put
\[
 \begin{split}
 M_L&=\Re\left\{L_1(r_1)+\sum_{j=2}^{p-1}
                                  \phi_j(r_{j-1},r_j)\right\},\\
 P_{p,a}&=\partial_1\phi_p(r_{p-1},r_p),\\
 G_{L,N}&=N^{-1}\log L_N-M_L+
                      \Re[P_{p,a}(z_{p-1}-r_{p-1})].
 \end{split}
\tag{12}
\]
Use \(\log0=-\infty\). The same multiplication as in Corollary 1,
stopped at this cut, proves
\[
 G_{L,N}\le-\gamma_{44}-\kappa_0
 \left\{2\sum_{j=2}^{p-2}(x_j-a_j)^2+(x_{p-1}-a_{p-1})^2\right\}
                  +\eta+O_m(\log N/N).
\tag{13}
\]
The last tangent cancels by
\(\partial_2\phi_{p-1}+P_{p,a}=0\). The other half of the cut weight
belongs to the middle factor.

Choose one exact source chart from the propagation theorem. Its
contracted selected source is (2) with each retained weight replaced
by \(D_j=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}\), where
\(\sigma_j\in\{0,\epsilon_j\}\). Its uncontracted
source is instead
\[
 \mathscr J^u_{\sigma,N}=U_{1,N}(w_L,X_1)
 \prod_{j=2}^{m}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal H_N(w_R,X_m^{-1})\prod_{j=1}^{m}D_j,
\tag{14}
\]
with scalar \(\kappa_N^{m+k_4}N^{m+k_4}\). The inverse terminal
argument and the one-power difference in the two scalars are retained.
The right boundary must be one of the completed states for the chosen
chart, with its original type, height, selection and neighborhood
conditions; sectors from the two charts are not combined.

Every coordinate in the protected triples is unselected in \(P\).
The free middle \(F=[p+1,q-2]\) may contain every original alphabet
state, with the original height rules. The exact clean-closing reduction
then gives
\[
 N^{-1}\log|\mathscr J_{\sigma,N}|-M
 \le G_{L,N}+G_{R,N}-\frac1{20000}\sum_{i\in F}p_i
                              +\eta+O_m(\log N/N),
\tag{15}
\]
where \(p_i=\min\{1,\sigma_i+400(\operatorname{clamp}_P x_i-a_i)^2\}\).
If the chosen right state has calibrated bound
\(G_{R,N}\le-\Delta_R-K_R+\eta+O_m(\log N/N)\), inserting (13)
and allocating all tolerances once yields
\[
 |\mathscr J_{\sigma,N}|\le CN^A
 \exp N\left\{M-\gamma_{44}-\Delta_R-K_R
                   -\frac1{20000}\sum_{i\in F}p_i+\tau\right\}.
\tag{16}
\]
The omitted prefix quadratic terms are nonpositive. The contracted
unselected plateau suffix is one allowed case, with
\(\Delta_R=K_R=0\). Fixed ordinary-color disks and jets have the
same scope as the source theorems. Empty free intervals are interpreted
as in the safe-cut theorem; no short-word safety condition is invented.

Equations (13)--(16) use this new prefix only through its literal
boundary rate. The middle estimate is not reapplied to its first
coordinate. The loss is \(\gamma_{44}\), not the larger common loss
for the older active-boundary catalog. These are pointwise bounds and
bounds for integrals on specified bounded parts of the stated domain;
they supply no vertical join to a different prefix-height contour.

## 4. Scope and sources

This proves the initial44 counterpart of the
[initial34 rectangular assembly](research_mixed_initial34_early_boundary_assembly.md),
with its additional full first weight explicitly retained. The nonzero
coefficient belongs to (8). Selected first weights, moving-height joins,
other boundary intervals and general boundary departures are not
estimated here. There is no whole-word, closed-knot or arbitrary
short-partial-filling conclusion.

| Direct source | SHA-256 |
|---|---|
| research_mixed_first_four_four_true_last_row_calibration.md | 52c149d8500e88c6e4e3fdf1c9e699baf376dfaac8b96d3461dc81f9d1725e0d |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_completed_boundary_state_propagation.md | cc7b2fc0db168d00e2b75b54ec3ff51496f178e819e4e5c8d5c6b53af563cb48 |
| research_mixed_initial34_early_boundary_assembly.md | b71f6d11e69a6afdc97bf2009975d71e51931d6b949f3ab805e2e17400a2b43d |

All directly used source statements and proofs were read. This is a
written deduction with no mathematical numerical evaluation, saved-value
arithmetic, import, compilation, test or change to a frozen source.
