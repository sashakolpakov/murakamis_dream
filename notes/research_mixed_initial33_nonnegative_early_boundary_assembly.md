# Extending the initial 3,3 boundary interval at nonnegative first height

Private research corollary, 10 November 2026. The complete first-three/three
bound at nonnegative first retained height enlarges the first rectangular
integration interval and supplies a left state for the exact unrestricted
middle reduction. The second retained height may have either sign. The
restriction is on the original reference, and is not removed by this
assembly.

## 1. Actual reference and exact contracted source

Fix a positive three/four open word of length \(m\ge3\) beginning
with \(3,3\). Write \(n_j=3+\epsilon_j\), so that
\(\epsilon_1=\epsilon_2=0\), and put
\[
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j,\qquad
 r_j=a_j+ic_j,\qquad z_j=x_j+ic_j,\quad X_j=e^{-2\pi iz_j}.
\tag{1}
\]
Retain the original actual complete-color reference, markings and
logarithmic lifts, with the additional hypothesis
\[
                              c_1\ge0.
\tag{2}
\]
There is no sign condition on \(c_2\) or on the private height of the
second ordinary vertex. Every target in the rectangular estimates below
has its fixed original height.

The exact terminal-contracted unselected integrand from
[the whole plateau theorem](research_mixed_full_unselected_plateau.md) is
\[
 \mathscr J_N^c=
 U_{0,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal V_{\epsilon_m,N}(w_R,X_h)
 \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}.
\tag{3}
\]
Its original scalar is
\(\kappa_N^{m+k_4}N^{m+k_4-1}\), with \(|\kappa_N|=1\).
All terminal rows, the terminal own weight and its Fourier alternatives
have already been summed inside \(\mathcal V\). The retained coordinates
in (3) use their unselected alternatives.

Set
\[
 P=[11/50,9/20],\quad E=[1/10,11/50],\quad
 \kappa_0=1/2500000,\qquad
 \gamma_{33}=\kappa_0(a_1-11/50)^2>0.
\tag{4}
\]
The strict inequality follows from the actual first-three image
\(a_1>.278\). Let \(L_0,\phi_j,\Pi\) be the original allocated
cap, ordinary and terminal phases, and write
\[
 \Phi(\mathbf z)=L_0(z_1)+\sum_{j=2}^{h}
               \phi_j(z_{j-1},z_j)+\Pi(z_h),\qquad
 M=\Re\Phi(\mathbf r),\qquad \nabla\Phi(\mathbf r)=0.
\tag{5}
\]
These identities retain the original additive calibration.

Theorem 2 of
[the nonnegative-height first33 proof](research_mixed_early_three_nonnegative_first_height.md)
controls the complete product
\[
                         |U_{0,N}(w_L,X_1)C_{0,N}(X_1,X_2)|
\tag{6}
\]
on \(E\times P\), at rate
\[
 \Re L_0(r_1)+\Re\phi_2(r_1,r_2)
 +\Re\partial_2\phi_2(r_1,r_2)(x_2-a_2)
 -\kappa_0(x_2-a_2)^2-\gamma_{33}+\tau_2.
\tag{7}
\]
There is no first or second diagonal weight in (6): their exponents
are exactly zero, rather than weights omitted from a norm estimate.
All later nonzero weights retain one half at each incident factor.
The complete pair bound includes both parities and a sufficiently small
fixed ordinary-color disk. Its assumption (2) concerns the fixed base
reference even when \(c_1=0\); continuation in \(w_L\) does not require
the height of a color-dependent critical point to remain nonnegative.

## 2. The enlarged rectangle retains the original nonzero coefficient

**Proposition 1.** For every \(\tau>0\), the exact integrand (3)
satisfies, on \(E\times P^{h-1}\),
\[
 |\mathscr J_N^c|\le C_{m,\tau}N^{A_{m,\tau}}
 \exp N\left\{M-\gamma_{33}
       -2\kappa_0\sum_{j=2}^{h}(x_j-a_j)^2+\tau\right\}.
\tag{8}
\]
The estimate holds through both level parities on sufficiently small
fixed ordinary-color disks about \((-2,-2)\), with every fixed color
derivative obeying the same rate on smaller disks.

*Proof.* Multiply (6)--(7) by the complete ordinary supporting planes
for \(j=3,\ldots,h\), and the complete terminal supporting plane.
The original incidence allocations multiply to (3). At coordinates
one and two the diagonal exponents are zero; at every later retained
type-four coordinate the two allocated halves give its full weight.
Equation (5) cancels every surviving linear marginal and adds the
constants to \(M\). Each coordinate \(j\ge2\) receives two quadratic
losses. When \(m=3\), \(h=2\), the terminal factor supplies the second
loss at coordinate two directly, and no additional ordinary factor is
present. Its neighboring halfweight also has exponent zero.

Allocate the finitely many source tolerances within \(\tau\) and
intersect their fixed color disks. The weight identities hold at zeros
without division. Cauchy's formula on smaller disks proves the derivative
assertion. This proves (8). \(\square\)

Let \(\mathcal Z_N^+\) be the scalar following (3) times its integral
over
\[
                     [1/10,9/20]\times P^{h-1}
\tag{9}
\]
at the fixed heights and original angular orientation. Let
\(\mathcal Z_N^P\) be the known integral over \(P^h\).
Their difference is exactly the integral over \(E\times P^{h-1}\),
up to the measure-zero shared boundary. Thus (8) gives
\[
 |\mathcal Z_N^+-\mathcal Z_N^P|
                    \le CN^A e^{N(M-\gamma_{33}+\tau)}.
\tag{10}
\]
This is an additive identity of restricted integrals, with the inherited
measure; it asserts no homology for an omitted part of the full period.

**Corollary 2.** The enlarged rectangular contribution has the unchanged
nonzero asymptotic
\[
 \mathcal Z_N^+(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
 e^{N\mathcal F_m(\mathbf w)}
                  \{1+O_{\rm hol}(N^{-1})\},\qquad A_m\ne0,
\tag{11}
\]
on sufficiently small fixed ordinary-color disks, through both parities.
Its phase, coefficient, Gaussian branch, orientation and normalized
color jets are exactly those of the whole plateau theorem.

*Proof.* That theorem gives (11) for \(\mathcal Z_N^P\). Choose
\(\tau<\gamma_{33}/8\) in (10) and shrink the fixed disks until
\(\Re\mathcal F_m>M-\gamma_{33}/8\) and \(A_m\) is bounded away
from zero. Dividing the holomorphic difference by its original leading
term gives an exponentially small holomorphic function, including its
polynomial prefactor. Cauchy's formula gives the same conclusion for
every fixed normalized color jet on smaller disks. Hence adding that
difference leaves both the coefficient and relative error unchanged.
The source restriction (2) has not been continued to an independent
family of references. \(\square\)

## 3. A height-restricted left state for the unrestricted middle

Choose one exact source chart and the safe ordinary cuts \(p,\ldots,q\)
of [completed boundary propagation](research_mixed_completed_boundary_state_propagation.md).
Retain its eight-vertex safety halo and the protected triples
\[
 T_L=\{p-2,p-1,p\},\qquad T_R=\{q-1,q,q+1\},\qquad q\ge p.
\tag{12}
\]
Keep the first pair outside those triples and in the physical prefix
through \(p-1\). In that prefix take \(x_1\in E\), every
\(x_2,\ldots,x_{p-1}\in P\), zero selections, and the unchanged
actual heights satisfying (2). Its literal cut modulus is
\[
 L_N=|U_{0,N}|\prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|d_N(X_j)|^{\epsilon_j}
                |d_N(X_{p-1})|^{\epsilon_{p-1}/2}.
\tag{13}
\]
The first two exponents remain zero in this formula. Define
\[
 \begin{split}
 M_L&=\Re\left\{L_0(r_1)+\sum_{j=2}^{p-1}
                                \phi_j(r_{j-1},r_j)\right\},\\
 P_{p,a}&=\partial_1\phi_p(r_{p-1},r_p),\\
 G_{L,N}&=N^{-1}\log L_N-M_L+
                       \Re[P_{p,a}(z_{p-1}-r_{p-1})].
 \end{split}
\tag{14}
\]
With \(\log0=-\infty\), multiplication of (7) and the remaining
prefix planes gives
\[
 G_{L,N}\le-\gamma_{33}-\kappa_0
 \left\{2\sum_{j=2}^{p-2}(x_j-a_j)^2+(x_{p-1}-a_{p-1})^2\right\}
                         +\eta+O_m(\log N/N).
\tag{15}
\]
The last tangent cancels by
\(\partial_2\phi_{p-1}+P_{p,a}=0\). The other half of the cut weight
belongs to the middle factor.

For clarity, the contracted selected chart is (3) with each retained
weight replaced by
\(D_j=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}\),
\(\sigma_j\in\{0,\epsilon_j\}\). Its scalar remains
\(\kappa_N^{m+k_4}N^{m+k_4-1}\). The uncontracted chart is instead
\[
 \mathscr J^u_{\sigma,N}=U_{0,N}(w_L,X_1)
  \prod_{j=2}^{m}C_{\epsilon_j,N}(X_{j-1},X_j)
  \mathcal H_N(w_R,X_m^{-1})\prod_{j=1}^{m}D_j,
\tag{16}
\]
with scalar \(\kappa_N^{m+k_4}N^{m+k_4}\).
The terminal inverse argument is part of the exact identity. Choose a
right state proved for the chosen chart, with all its original type,
selection, height and neighborhood restrictions. Do not combine sectors
from the two charts.

Every protected target is unselected in \(P\); the free interval
\(F=[p+1,q-2]\) may contain every original alphabet state, with its
original height rules. The exact middle inequality is
\[
 N^{-1}\log|\mathscr J_{\sigma,N}|-M
 \le G_{L,N}+G_{R,N}-\frac1{20000}\sum_{i\in F}p_i
                         +\eta+O_m(\log N/N),
\tag{17}
\]
where \(p_i=\min\{1,\sigma_i+400(\operatorname{clamp}_P x_i-a_i)^2\}\).
If the right state gives
\(G_{R,N}\le-\Delta_R-K_R+\eta+O_m(\log N/N)\), then (15)--(17)
and one total tolerance imply
\[
 |\mathscr J_{\sigma,N}|\le CN^A
 \exp N\left\{M-\gamma_{33}-\Delta_R-K_R
                      -\frac1{20000}\sum_{i\in F}p_i+\tau\right\}.
\tag{18}
\]
The discarded prefix quadratic terms are nonpositive. The contracted
unselected plateau suffix is included with \(\Delta_R=K_R=0\).
Empty free intervals and shorter words retain exactly the old safe-cut
and window-placement requirements; the rectangular result at length
three does not create a safe middle there.

The ordinary-color disks and jets in (18) have the scope of the exact
boundary sources. The first-coordinate bound is inserted only as (15);
no middle argument is reapplied to it. The deficit is \(\gamma_{33}\),
not the older catalog's larger common active-state deficit. These are
pointwise estimates and estimates of integrals on specified bounded
parts of this domain, not bounds on a missing height-changing join.

## 4. Scope and direct sources

This is the height-restricted initial33 counterpart of the
[initial34 assembly](research_mixed_initial34_early_boundary_assembly.md).
It does not assert \(c_1\ge0\) for all actual first33 references.
The case \(c_1<0\), other first-coordinate intervals, moving-height
joins and general boundary departures remain separate. There is no
first or second selected Fourier alternative for these two type-three
coordinates; selections at later coordinates retain only the stated
middle or right-source scope.

The nonzero coefficient belongs to the enlarged fixed-height rectangle
(9), not the whole torus source. Neither (11) nor (18) proves a
whole-word asymptotic, new closed-knot family or stability under arbitrary
short partial fillings.

| Direct source | SHA-256 |
|---|---|
| research_mixed_early_three_nonnegative_first_height.md | ffa42bf7baeafde8598b1ca87645e4a4069bd3381d80446db70e13d6cffeb5e8 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_completed_boundary_state_propagation.md | cc7b2fc0db168d00e2b75b54ec3ff51496f178e819e4e5c8d5c6b53af563cb48 |
| research_mixed_initial34_early_boundary_assembly.md | b71f6d11e69a6afdc97bf2009975d71e51931d6b949f3ab805e2e17400a2b43d |

All directly used source statements and proofs were read. This deduction
uses no mathematical numerical evaluation, saved-value arithmetic, import,
compilation, test or change to a frozen source.
