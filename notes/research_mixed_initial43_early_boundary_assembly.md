# Extending the initial four/three boundary interval with its complete first weight

Private written corollary, 10 November 2026. The complete early first
four/three estimate extends the first coordinate of the unselected
plateau integral to one tenth, with all other coordinates still on
the plateau at their original heights. The added integral is
exponentially smaller and preserves the original nonzero coefficient.
The same pair gives a left boundary state for the already controlled
unrestricted middle.

The first Fourier weight is present in full; the second coordinate
has type three and no diagonal weight. The smaller central curvature
reserve in the complete-pair theorem is retained. Neither assertion
estimates a selected first alternative or a changing-height join.

## 1. Literal contracted source and complete-pair input

Fix an actual positive three/four word of length \(m\ge3\) beginning
with \(4,3\). Write \(n_j=3+\epsilon_j\), so
\(\epsilon_1=1\), \(\epsilon_2=0\), and set
\[
 h=m-1,\quad k_4=\sum_{j=1}^m\epsilon_j,\quad
 r_j=a_j+ic_j,\quad z_j=x_j+ic_j,\quad X_j=e^{-2\pi iz_j}.
\tag{1}
\]
The references, markings and logarithmic lifts are the original ones.
Let \(P=[11/50,9/20]\), \(E=[1/10,11/50]\), and
\(\kappa_0=1/2500000\). The exact terminal-contracted unselected
integrand in the
[whole unselected plateau theorem](research_mixed_full_unselected_plateau.md)
is
\[
 \mathscr J^c_N=
 U_{1,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal V_{\epsilon_m,N}(w_R,X_h)
 \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}.
\tag{2}
\]
Its scalar is \(\kappa_N^{m+k_4}N^{m+k_4-1}\),
\(|\kappa_N|=1\). Every terminal row, diagonal weight and
Fourier alternative is already included in \(\mathcal V\).
The retained coordinates in (2) use the unselected alternatives.

Let \(L_1,\phi_j,\Pi\) denote the original allocated cap,
ordinary and terminal phases. Thus \(L_1=\mathcal T_1-g/2\),
and every retained type-four weight has one half on each incidence.
Put
\[
 \Phi(\mathbf z)=L_1(z_1)+\sum_{j=2}^{h}
                   \phi_j(z_{j-1},z_j)+\Pi(z_h),\qquad
 M=\Re\Phi(\mathbf r).
\tag{3}
\]
This is the original calibrated action and
\(\nabla\Phi(\mathbf r)=0\).

The [complete first-four/three theorem](research_mixed_early_four_three_complete_pair.md)
bounds precisely
\[
                 |U_{1,N}(w_L,X_1)C_{0,N}(X_1,X_2)|
                                      |d_N(X_1)|
\tag{4}
\]
on \(E\times P\), at rate
\[
 \Re L_1(r_1)+\Re\phi_2(r_1,r_2)
 +\Re\partial_2\phi_2(r_1,r_2)(x_2-a_2)
       -\kappa_0(x_2-a_2)^2-\gamma_{43}+\tau_2,
\tag{5}
\]
where
\[
 \gamma_{43}=\min\{\kappa_0,\nu/4\}(a_1-11/50)^2>0
\tag{6}
\]
and \(\nu>0\) is the same uniform central Schur constant as in
that theorem. The actual first-four bound is \(a_1>.246\).
There is no \(X_2\) halfweight to insert: \(\epsilon_2=0\).
The complete first weight in (4) has already been paid.

## 2. The enlarged rectangular contribution

**Theorem 1.** For every \(\tau>0\), on \(E\times P^{h-1}\)
at the fixed heights (1),
\[
 |\mathscr J^c_N|\le C_{m,\tau}N^{A_{m,\tau}}
 \exp N\left\{M-\gamma_{43}
           -2\kappa_0\sum_{j=2}^{h}(x_j-a_j)^2+\tau\right\}.
\tag{7}
\]
Both parities and sufficiently small fixed ordinary-color disks about
\((-2,-2)\) are included. Every fixed ordinary-color derivative
obeys the same upper rate on smaller disks.

*Proof.* Multiply (4)--(5) by the complete ordinary supporting
planes for \(j=3,\ldots,h\) and the complete terminal plane.
The remaining halfweights give exactly (2), including the zero
exponent at coordinate two. The original critical equations cancel
every linear term; their constants sum to \(M\). Each retained
coordinate \(j\ge2\) receives two quadratic losses. If \(m=3\),
then \(h=2\), and the terminal plane directly supplies the second
loss at coordinate two. No intervening factor is needed.

Allocate the finitely many source tolerances within \(\tau\),
intersect their fixed ordinary-color disks and apply Cauchy's formula
on smaller disks. The finite weight allocation is a product identity
in modulus even at a zero; no factor is divided out. This proves
(7). \(\square\)

Let \(\mathcal Z_N^+\) be the original scalar following (2)
times its integral over
\[
                  [1/10,9/20]\times P^{h-1}
\tag{8}
\]
at the same fixed heights and original angular orientation. Denote
the known integral over \(P^h\) by \(\mathcal Z_N^P\).
Their difference is exactly the added integral over
\(E\times P^{h-1}\), up to its measure-zero shared face.
Thus (7) gives
\[
           |\mathcal Z_N^+-\mathcal Z_N^P|
              \le CN^A e^{N(M-\gamma_{43}+\tau)}.
\tag{9}
\]
This is an identity between restricted integrals, not a contour
deformation of an unestimated region.

**Corollary 2.** On smaller fixed ordinary-color disks,
\[
 \mathcal Z_N^+(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
 e^{N\mathcal F_m(\mathbf w)}
                  \{1+O_{\rm hol}(N^{-1})\},\qquad A_m\ne0.
\tag{10}
\]
The action, coefficient, Gaussian branch, orientation and every fixed
normalized ordinary-color jet are exactly those of the whole
unselected plateau theorem.

*Proof.* That theorem gives (10) for \(\mathcal Z_N^P\).
Choose \(\tau<\gamma_{43}/8\) in (9), and shrink the color
disks so that \(\Re\mathcal F_m>M-\gamma_{43}/8\) and the
original amplitude remains bounded away from zero. The quotient
of the added integral by the original leading term is then
holomorphic and exponentially small, including its polynomial
prefactor. Cauchy's formula gives the same conclusion for every
fixed normalized jet. Adding it preserves (10). \(\square\)

## 3. The calibrated left boundary state

Choose either exact chart and the safe ordinary cuts \(p,\ldots,q\)
from [completed boundary propagation](research_mixed_completed_boundary_state_propagation.md).
Retain its eight-vertex safety halo, protected triples
\(T_L=\{p-2,p-1,p\}\), \(T_R=\{q-1,q,q+1\}\), and
free interval \(F=[p+1,q-2]\). Require the complete first-pair
window to lie inside the physical prefix through \(p-1\) and
outside the protected triples. These are the existing compatibility
conditions; no new short-word safe cut is assumed.

In that prefix take \(x_1\in E\),
\(x_2,\ldots,x_{p-1}\in P\), every selection zero and every
height fixed at its original value. Its literal cut modulus is
\[
 L_N=|U_{1,N}|\prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|d_N(X_j)|^{\epsilon_j}
                    |d_N(X_{p-1})|^{\epsilon_{p-1}/2}.
\tag{11}
\]
Define
\[
\begin{split}
 M_L&=\Re\left\{L_1(r_1)+\sum_{j=2}^{p-1}
                              \phi_j(r_{j-1},r_j)\right\},\\
 P_{p,a}&=\partial_1\phi_p(r_{p-1},r_p),\\
 G_{L,N}&=N^{-1}\log L_N-M_L
                          +\Re[P_{p,a}(z_{p-1}-r_{p-1})].
\end{split}
\tag{12}
\]
Use \(\log0=-\infty\). The proof of Theorem 1, stopped at
this cut, gives
\[
 G_{L,N}\le-\gamma_{43}-\kappa_0
 \left\{2\sum_{j=2}^{p-2}(x_j-a_j)^2+(x_{p-1}-a_{p-1})^2\right\}
                         +\eta+O_m(\log N/N).
\tag{13}
\]
Its last tangent cancels by
\(\partial_2\phi_{p-1}+P_{p,a}=0\). The other half of the
cut weight remains with the middle factor.

For clarity, the two permitted selected source charts are exactly
\[
\begin{split}
 \mathscr J^u_{\sigma,N}
 &=U_{1,N}(w_L,X_1)\prod_{j=2}^{m}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal H_N(w_R,X_m^{-1})\prod_{j=1}^{m}D_j,\\
 \mathscr J^c_{\sigma,N}
 &=U_{1,N}(w_L,X_1)\prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)\prod_{j=1}^{h}D_j,\\
 D_j&=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j},
                  \qquad\sigma_j\in\{0,\epsilon_j\}.
\end{split}
\tag{14}
\]
Their scalars are respectively
\(\kappa_N^{m+k_4}N^{m+k_4}\) and
\(\kappa_N^{m+k_4}N^{m+k_4-1}\). The inverse argument of
\(\mathcal H_N\) and the one-power difference in the scalars
are retained. A contracted terminal alternative is not added to an
uncontracted terminal sector as if those sectors were disjoint.

All protected coordinates are unselected in \(P\). The free
middle symbols retain their original full alphabet and height rules.
The exact clean-closing reduction in the propagation theorem gives
\[
 N^{-1}\log|\mathscr J_{\sigma,N}|-M
 \le G_{L,N}+G_{R,N}-\frac1{20000}\sum_{i\in F}p_i
                           +\eta+O_m(\log N/N),
\tag{15}
\]
where \(p_i=\min\{1,\sigma_i+
400(\operatorname{clamp}_P x_i-a_i)^2\}\).
Take any completed right state for the chosen chart, with all its
original type, height, selection and neighborhood conditions. If
its bound is \(G_{R,N}\le-\Delta_R-K_R+\eta+O_m(\log N/N)\),
then (13)--(15), with one total tolerance, imply
\[
 |\mathscr J_{\sigma,N}|\le CN^A
 \exp N\left\{M-\gamma_{43}-\Delta_R-K_R
                    -\frac1{20000}\sum_{i\in F}p_i+\tau\right\}.
\tag{16}
\]
The omitted prefix quadratic terms are nonpositive. The contracted
unselected plateau suffix is one allowed example, with
\(\Delta_R=K_R=0\). All fixed ordinary-color disks and jets
retain the source scopes. Empty or overlapping protected intervals
are treated only under the original safe-cut theorem's rules.

The middle estimate is not reapplied to the first coordinate.
The new prefix enters only through its literal rate (12); the
original synthetic closing losses, marginals and middle charges are
unchanged. In particular the small reserve \(\gamma_{43}\)
is not replaced by the larger common deficit of the older active
boundary menu.

## 4. Scope and direct sources

Equation (10) concerns the specified larger restricted integral.
Equation (16) concerns the exact chosen source chart on its stated
physical domain and its bounded restricted integrals. Neither
asserts that the remaining original torus sectors are smaller.
Selected first weights, other boundary intervals, and moving-height
joins remain separate. There is no new whole-word, closed-knot,
arbitrary short-partial-filling or finite-exception theorem.

| Direct source | SHA-256 |
|---|---|
| research_mixed_early_four_three_complete_pair.md | 271c54a8c5bb9a9fd292dcc66bc760f2cd637f8a685d14fa6722f1eab4d70575 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_completed_boundary_state_propagation.md | cc7b2fc0db168d00e2b75b54ec3ff51496f178e819e4e5c8d5c6b53af563cb48 |
| research_mixed_initial44_early_boundary_assembly.md | 8ed393fd2e465d5399c8ffddc46c2d603ef4c5cb6d154ee561e676aa8bfd2c90 |

All directly used source statements and proofs were read. This is a
written deduction with no mathematical numerical evaluation, saved-value
arithmetic, import, test, compilation or change to a frozen source.
