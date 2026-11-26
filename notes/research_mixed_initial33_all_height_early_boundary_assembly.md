# The initial 3,3 enlarged boundary rectangle at every actual height

Private written corollary, 10 November 2026. The complete signed
one-wall estimate removes the first-height restriction from the earlier
initial33 boundary assembly. The added rectangular integral is still
exponentially smaller than the original plateau contribution. Its
addition preserves that contribution's nonzero coefficient. The same
complete pair supplies a left state for the existing unrestricted-middle
reduction, with its original protected triples and source-chart scope.

## 1. Exact source and the now unrestricted pair input

Fix a positive three/four open word of length \(m\ge3\) beginning
with \(3,3\). Put \(n_j=3+\epsilon_j\),
\(\epsilon_1=\epsilon_2=0\), \(h=m-1\), and
\(k_4=\sum_{j=1}^m\epsilon_j\). Retain its actual complete-color
reference \(r_j=a_j+ic_j\), original markings, logarithmic lifts and
additive action. There is no sign restriction on \(c_1,c_2\), or on
the private height of the second ordinary factor. This is a statement
at actual references, not at arbitrary points of an auxiliary box.

Write \(z_j=x_j+ic_j\), \(X_j=e^{-2\pi iz_j}\), and set
\[
 P=[11/50,9/20],\qquad E=[1/10,11/50],\qquad
 \kappa_0=1/2500000,\qquad
 \gamma_{33}=\kappa_0(a_1-11/50)^2>0.
\tag{1}
\]
The last inequality uses the original first-three image \(a_1>.278\).
Every rectangular target below keeps its fixed reference height.

The literal terminal-contracted unselected integrand is
\[
 \mathscr J_N^c=
 U_{0,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal V_{\epsilon_m,N}(w_R,X_h)
 \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j},
\tag{2}
\]
with original scalar
\(\kappa_N^{m+k_4}N^{m+k_4-1}\), \(|\kappa_N|=1\).
Every terminal row, terminal weight and terminal Fourier alternative
is already inside \(\mathcal V\). All retained alternatives in (2)
are unselected. There is no first or second diagonal weight, because
their exponents are zero; later type-four coordinates retain both
incident halfweights.

Let \(L_0,\phi_j,\Pi\) be the original allocated phases. Thus
\[
 \Phi(\mathbf z)=L_0(z_1)+\sum_{j=2}^{h}
                  \phi_j(z_{j-1},z_j)+\Pi(z_h),\qquad
 M=\Re\Phi(\mathbf r),\qquad \nabla\Phi(\mathbf r)=0.
\tag{3}
\]
Corollary 2 of the
[signed one-wall theorem](research_mixed_negative_height_wrapped_contour.md)
now bounds the complete finite product
\(U_{0,N}(w_L,X_1)C_{0,N}(X_1,X_2)\) on \(E\times P\),
with rate
\[
 \Re L_0(r_1)+\Re\phi_2(r_1,r_2)
 +\Re\partial_2\phi_2(r_1,r_2)(x_2-a_2)
 -\kappa_0(x_2-a_2)^2-\gamma_{33}+\tau_2.
\tag{4}
\]
It retains both parities, every low, central and high row, and a small
fixed ordinary-color disk. In its wrapped part the estimate controls
the signed finite sum. Here it is used only as the bound for the
complete product in (4); that sum is not subsequently replaced by its
sum of absolute rows. The positive-height case and both private-height
signs are included in the cited corollary.

## 2. Rectangle extension and the unchanged nonzero coefficient

**Corollary 1.** For every \(\tau>0\), on \(E\times P^{h-1}\),
\[
 |\mathscr J_N^c|\le C_{m,\tau}N^{A_{m,\tau}}
 \exp N\left\{M-\gamma_{33}
       -2\kappa_0\sum_{j=2}^{h}(x_j-a_j)^2+\tau\right\}.
\tag{5}
\]
It holds on sufficiently small fixed ordinary-color disks about
\((-2,-2)\), through both parities, and for every fixed color
derivative on smaller disks.

*Proof.* Multiply (4) by the complete ordinary supporting planes for
\(j=3,\ldots,h\) and the complete terminal supporting plane from
[the whole plateau theorem](research_mixed_full_unselected_plateau.md).
All their targets are independently in \(P\), at the unchanged
actual heights. The phase identity (3) cancels every surviving marginal
and adds the constants to \(M\). Every retained coordinate \(j\ge2\)
receives two quadratic losses. At \(m=3\), the terminal factor directly
supplies the second loss at coordinate two; there is no intervening
ordinary factor and its neighboring halfweight has exponent zero.
All later nonzero halfweights multiply to exactly (2), including at
their zeros. Choose the finitely many source tolerances within \(\tau\)
and intersect their color disks. Cauchy's formula on smaller disks
proves the derivative assertion. \(\square\)

Let \(\mathcal Z_N^+\) be the original scalar following (2) times
its integral over
\[
                       [1/10,9/20]\times P^{h-1}
\tag{6}
\]
at the fixed heights and original angular orientation. Let
\(\mathcal Z_N^P\) be the original integral over \(P^h\).
Their difference is exactly the integral over \(E\times P^{h-1}\),
up to the measure-zero shared boundary. Equation (5) therefore gives
\[
 |\mathcal Z_N^+-\mathcal Z_N^P|
                 \le CN^A e^{N(M-\gamma_{33}+\tau)}.
\tag{7}
\]
This is addition of restricted integrals with the same measure, not
a contour deformation or an equality with the whole torus period.

The whole plateau theorem supplies its original holomorphic local
phase \(\mathcal F_m\) and nonzero amplitude \(A_m\). Consequently
\[
 \mathcal Z_N^+(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)e^{N\mathcal F_m(\mathbf w)}
                 \{1+O_{\rm hol}(N^{-1})\},\qquad A_m\ne0.
\tag{8}
\]
Indeed, choose \(\tau<\gamma_{33}/8\), then shrink the fixed
color disks until \(\Re\mathcal F_m>M-\gamma_{33}/8\) and
\(A_m\) is bounded away from zero. Dividing (7) by that leading
term gives an exponentially small holomorphic error, including its
polynomial prefactor. Cauchy's formula proves the same statement for
fixed normalized color jets on smaller disks. The original coefficient,
Gaussian branch, orientation and scalar power are unchanged. No
condition on a color-dependent critical height is introduced.

## 3. The new left boundary state in either exact chart

Use safe ordinary cuts \(p,\ldots,q\), \(q\ge p\), from
[completed boundary propagation](research_mixed_completed_boundary_state_propagation.md),
with its original eight-vertex safety halo and the contracted-graph
inheritance condition when that chart is used. Require
\[
 T_L=\{p-2,p-1,p\},\qquad T_R=\{q-1,q,q+1\},\qquad
 F=[p+1,q-2]
\tag{9}
\]
to have unselected \(P\) targets on the protected triples. Keep the
first pair outside these triples and wholly in the physical prefix
through \(p-1\). Put \(x_1\in E\), all
\(x_2,\ldots,x_{p-1}\in P\), and all prefix selections zero,
at their original heights. The free interval \(F\) may contain
every original alphabet state, with its unchanged height rules.

The literal left cut modulus and calibrated rate are
\[
\begin{split}
 L_N&=|U_{0,N}|\prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|d_N(X_j)|^{\epsilon_j}
                   |d_N(X_{p-1})|^{\epsilon_{p-1}/2},\\
 G_{L,N}&=N^{-1}\log L_N-M_L+
                    \Re[P_{p,a}(z_{p-1}-r_{p-1})],\\
 M_L&=\Re\left\{L_0(r_1)+\sum_{j=2}^{p-1}
                          \phi_j(r_{j-1},r_j)\right\},\qquad
 P_{p,a}=\partial_1\phi_p(r_{p-1},r_p).
\end{split}
\tag{10}
\]
Use \(\log0=-\infty\). The first two diagonal exponents are zero;
the other half of the cut weight belongs to the middle factor.
Multiplying (4) and the remaining prefix planes, and using
\(\partial_2\phi_{p-1}+P_{p,a}=0\), proves
\[
 G_{L,N}\le-\gamma_{33}-\kappa_0
 \left\{2\sum_{j=2}^{p-2}(x_j-a_j)^2+(x_{p-1}-a_{p-1})^2\right\}
                       +\eta+O_m(\log N/N).
\tag{11}
\]

Choose one source chart throughout. The contracted chart is (2) with
retained weights \(D_j=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}\),
\(\sigma_j\in\{0,\epsilon_j\}\), and the same scalar as (2).
The uncontracted chart is instead
\[
 \mathscr J^u_{\sigma,N}=U_{0,N}(w_L,X_1)
    \prod_{j=2}^{m}C_{\epsilon_j,N}(X_{j-1},X_j)
    \mathcal H_N(w_R,X_m^{-1})\prod_{j=1}^{m}D_j,
\tag{12}
\]
with scalar \(\kappa_N^{m+k_4}N^{m+k_4}\). The terminal inverse
argument is retained. A right state must satisfy all type, selection,
height, window-placement and neighborhood hypotheses of its own chart
in the propagation theorem. No terminal selection is reintroduced
inside the already contracted \(\mathcal V\).

If that state has calibrated bound
\(G_{R,N}\le-\Delta_R-K_R+\eta+O_m(\log N/N)\), its exact
middle inequality and (11) give, after one total tolerance allocation,
\[
 |\mathscr J_{\sigma,N}|\le CN^A
  \exp N\left\{M-\gamma_{33}-\Delta_R-K_R
                  -\frac1{20000}\sum_{i\in F}p_i+\tau\right\},
 \quad p_i=\min\{1,\sigma_i+400(\operatorname{clamp}_P x_i-a_i)^2\}.
\tag{13}
\]
The discarded prefix quadratic terms are nonpositive. In particular
the contracted unselected \(P\) suffix has \(\Delta_R=K_R=0\).
The original right menus remain distinct between charts. Empty free
intervals, overlapping protected triples and shorter words retain the
old safe-cut and physical-window conditions; the length-three rectangle
does not create a safe middle at that length.

The fixed ordinary-color disks and jets have exactly the source scope
used above. Integer-weighted complete products are holomorphic; no
modulus halfweight is differentiated. The bound applies pointwise and
to specified bounded pieces of this domain with the correct external
scalar. Its deficit is \(\gamma_{33}\), not the older catalog's larger
common active-state deficit.

## 4. Scope and source versions

This removes only the hypothesis \(c_1\ge0\) from the earlier
[initial33 assembly](research_mixed_initial33_nonnegative_early_boundary_assembly.md).
It covers every actual initial33 reference at each fixed length
\(m\ge3\), without any independent-box realization claim. The first
two type-three coordinates have no selected Fourier alternative.
Later selections retain only the stated middle or right-source domains.

The nonzero coefficient in (8) belongs to the enlarged fixed-height
rectangle (6). Other first-coordinate intervals, height-changing joins,
general boundary departures and the rest of the whole period are not
estimated here. Neither (8) nor (13) is a whole-word asymptotic, a new
closed-knot theorem or a stability result for arbitrary short fillings.

| Direct source | SHA-256 |
|---|---|
| research_mixed_negative_height_wrapped_contour.md | 0f024a3f54087ab3b4fee6f6c992a2e9292644590fc78b21072d6104a0f5c2e6 |
| research_mixed_initial33_nonnegative_early_boundary_assembly.md | 76869191eb85d5155a8537854bf9c0d5edeff1007f823fd3eb692942b44b33ae |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_completed_boundary_state_propagation.md | cc7b2fc0db168d00e2b75b54ec3ff51496f178e819e4e5c8d5c6b53af563cb48 |

The complete proof and directly used source implications were read back.
Only written analysis and source-hash metadata checks were used; there
was no mathematical numerical evaluation, saved-value arithmetic,
import, compilation, test or change to a frozen source.
