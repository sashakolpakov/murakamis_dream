# Finite boundary windows after the exact terminal contraction

Research deduction, 6 November 2026. The general finite-window
reduction can be applied to the original source after its entire
terminal variable has been summed. Its right boundary functional
then contains the literal terminal polynomial \(\mathcal V\),
including the cancellations inside that polynomial. This applies
to arbitrary physical boundary states; the plateau restrictions
in the existing contracted-collar sign theorem are unnecessary for
the reduction itself. No new boundary sign is asserted.

## 1. Contract first, then choose the retained torus graph

Fix a positive three/four word of length \(m\ge2\), put
\(h=m-1\), \(\epsilon_j=n_j-3\), and \(k_4=\sum_j\epsilon_j\).
The original [terminal contraction](research_mixed_reversed_cap_assembly.md),
Proposition 1, is the exact identity
\[
 \mathcal V_{\epsilon,N}(w,X)
 =N\oint C_{\epsilon,N}(X,Y)H_N(w,Y^{-1})
       \{d_N(Y)(1+Y^{-N})\}^{\epsilon}
                         \frac{dY}{2\pi iY}.
 \tag{1}
\]
The circle may have any positive radius. The left side is a finite
Laurent polynomial in \(X\), with band \([-N+1,0]\), and
a polynomial in the ordinary color. This identity retains all
physical rows, normal data and the full private Fourier alternative.
Write \(W_{\epsilon,N}(Y)=\{d_N(Y)(1+Y^{-N})\}^{\epsilon}\).

Expand only the remaining retained selections
\(0\le\sigma_j\le\epsilon_j\), \(1\le j\le h\), and set
\[
 \begin{split}
 D_j(X_j)&=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j},\\
 \mathscr J_{\sigma,N}(\mathbf X;w_L,w_R)
 &=U_{\epsilon_1,N}(w_L,X_1)
      \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
      \mathcal V_{\epsilon_m,N}(w_R,X_h)
      \prod_{j=1}^{h}D_j(X_j).
 \end{split}
 \tag{2}
\]
The entire original ordinary-color polynomial is
\[
 \mathcal Z_N=\kappa_N^{m+k_4}N^{m+k_4-1}
       \sum_{\sigma\le\epsilon}
       \oint\mathscr J_{\sigma,N}
                    \prod_{j=1}^{h}\frac{dX_j}{2\pi iX_j}.
 \tag{3}
\]
In particular \(\sigma_h\) is still summed. The terminal own
selection \(\sigma_m\) has already been summed inside (1),
and must not be inserted again. These are identities of the signed
source, before any absolute value or sector localization, and hold
at both parities and after ordinary-color differentiation.

Each summand of (3) is Laurent polynomial on
\((\mathbb C^\times)^h\). Choose its retained periodic hybrid
graph directly in this space, with the original interior rule and
baseline cutoff one at a missing retained neighbor. The straight
height homotopy from the product torus stays in
\((\mathbb C^\times)^h\); hence it preserves the integral of
the original holomorphic top form. Piecewise smooth graphs, or
their Lipschitz limits, have the same conclusion and the original
bounded graph-Jacobian prefactor.

This is not projection of the earlier \(m\)-variable graph.
That graph could make retained heights depend on the eliminated
private coordinate. Instead (1)--(3) are established on product
circles first, and a new homotopic graph is chosen for their exact
Laurent polynomial. No old localized sector or graph Jacobian is
identified with a projected sector. As usual a different retained
selection may use its own valid graph.

## 2. The actual reference, cuts and calibrated boundary products

Keep the actual complete-color open critical reference
\(r_j=t_j^*\), \(1\le j\le h\). Its allocated action is
\[
 \Phi=L(z_1)+\sum_{j=2}^{h}\phi_j(z_{j-1},z_j)+\Pi(z_h),
                  \qquad M=\Re\Phi(\mathbf r),
 \tag{4}
\]
with \(L,\Pi\) and the original halfweights from the
[whole unselected plateau theorem](research_mixed_full_unselected_plateau.md),
equations (4)--(7). These phases identify the reference action
and slopes. They are not claimed to bound the finite caps at
arbitrary nonplateau targets.

Choose ordinary cuts \(p\le q\), and let
\(I=[p-2,q+1]\) be safe with its eight-vertex halo, as in the
[open boundary comparison](research_mixed_open_boundary_comparison_reduction.md),
Section 1. For example \(p=16,q=m-15\) works whenever the
middle exists: the halo of \([14,m-14]\) lies inside
\([6,m-5]\). The
[open-window inheritance theorem](research_mixed_open_word_window_inheritance.md),
Corollary 2, transfers every required original local certificate
to this same open reference. No periodic critical point is used.

Allocate the exact nonnegative moduli as
\[
 \begin{split}
 L_N={}&|U_{\epsilon_1,N}|\prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
          \prod_{j=1}^{p-2}|D_j|\,|D_{p-1}|^{1/2},\\
 R_N^{\rm con}={}&|\mathcal V_{\epsilon_m,N}|
          \prod_{j=q+1}^{h}|C_{\epsilon_j,N}|
          |D_q|^{1/2}\prod_{j=q+1}^{h}|D_j|.
 \end{split}
 \tag{5}
\]
Together with the allocated middle factors these multiply to
\(|\mathscr J_{\sigma,N}|\). There is no division by a
possibly vanishing factor and no holomorphic square root of \(d_N\).
All physical boundary states and all retained selections in (5)
remain free over their complete original periods and graph heights.

Write \(P_{j,a}=\partial_1\phi_j(r_{j-1},r_j)\) and
\(P_{j,b}=\partial_2\phi_j(r_{j-1},r_j)\). The calibrated
boundary actions are exactly
\[
 \begin{split}
 M_L&=\Re\{L(r_1)+\sum_{j=2}^{p-1}\phi_j(r_{j-1},r_j)\},\\
 M_R^{\rm con}&=\Re\{\sum_{j=q+1}^{h}\phi_j(r_{j-1},r_j)
                                                    +\Pi(r_h)\}.
 \end{split}
 \tag{6}
\]
In particular the right action uses the coherently contracted
\(\Pi\), with its original additive constant and halfweight.

Use the original four-symbol allocated defects \(w_j\), and
replace symbols outside \(I\) by their unselected reference
values to form the synthetic configuration \(\widetilde q\).
Set
\[
 \begin{split}
 A_p&=\sum_{j=p-3}^{p-1}w_j(\widetilde q),\qquad
 E_q=\sum_{j=q+1}^{q+3}w_j(\widetilde q),\\
 D_I&=-\sum_{j=p-3}^{q+3}w_j(\widetilde q),\\
 B_{L,N}&=N^{-1}\log L_N-M_L
             +\Re[P_{p,a}(z_{p-1}-r_{p-1})]-A_p,\\
 B_{R,N}^{\rm con}&=N^{-1}\log R_N^{\rm con}-M_R^{\rm con}
             +\Re[P_{q,b}(z_q-r_q)]-E_q,\\
 F_N^{\rm con}&=B_{L,N}+B_{R,N}^{\rm con}-D_I.
 \end{split}
 \tag{7}
\]
Here \(\log0=-\infty\). The protected closing triples and
the two complex tangents are unchanged. The complete middle-source
bound and original stationarity give, for any aggregate tolerance
\(\eta>0\),
\[
 N^{-1}\log|\mathscr J_{\sigma,N}|-M
       \le F_N^{\rm con}+\eta+O_m(\log N/N).
 \tag{8}
\]
This is the six-edge identity used in the
[contracted collar theorem](research_mixed_contracted_boundary_collar_completion.md),
Section 3. Its derivation does not use the plateau restrictions
subsequently imposed there to prove a sign.

## 3. The complete finite-window reduction survives the contraction

**Proposition 1.** On every fixed compact ordinary-color set there
is a finite uniform upper budget
\(B_{L,N}+B_{R,N}^{\rm con}\le K\), independent of \(N\)
and total word length when the initial physical boundary widths
are fixed. Moreover the complete safe-middle occupation bound is
\[
 D_I\ge\kappa\sum_{j\in I}p_j,\qquad \kappa=1/20000,
 \quad p_j=\min\{1,\sigma_j+400(\operatorname{clamp}_P x_j-\Re r_j)^2\}.
 \tag{9}
\]
Thus the relative-pinning theorem and its finite-window sufficient
criterion apply with \(B_{R,N}^{\rm con}\) in place of the
uncontracted right boundary function.

*Proof.* The occupation statement is the
[full-period occupation theorem](research_mixed_full_period_occupation.md)
for a safe compact perturbation of the actual open reference.
All bulk weights, incidence counts, closing stencils and local
reference domains are unchanged. Only the literal right endpoint
product was replaced. In particular the proof does not import
a cyclic conclusion without its open-reference boundary accounting.

For the finite budget, use the exact sum for \(\mathcal V\)
in equation (9) of the terminal contraction:
\[
 \mathcal V_{\epsilon,N}(w,X)
   =\sum_{i<N}\frac{X^{-i}(rX;r)_i}{(r;r)_i^{1+\epsilon}}
                                  U_{\epsilon,N}(w,r^i),
           \qquad r=e^{-2\pi i/N}.
 \tag{10}
\]
On the compact hybrid annuli, all products and Laurent powers
have a fixed exponential upper bound. The elementary factorial
inequalities in Section 2 of
[finite boundary windows](research_mixed_open_finite_boundary_windows.md)
give the same bound for inverse factorials and the finite cap sums,
including all ordinary colors in the fixed compact set. Equation
(10) has only \(N\) terms. Hence it supplies a finite exponential
ceiling for \(|\mathcal V|\), without a favorable rate assertion
or deletion of any internal cancellation. The remaining finitely
many boundary factors and the compact reference actions and slopes
are treated exactly as in that section. This proves existence of
\(K\), not a calibrated sign. \(\square\)

For precision, fix \(\zeta\ge0\), put
\(B=\lfloor(K+\zeta)/\kappa\rfloor\), \(d=352\),
\(\ell=2d+7=711\), and \(R=(B+1)\ell\). If
\(|I|\ge6+2R\), every configuration with
\(F_N^{\rm con}>-\zeta\) has two unselected plateau blocks
of length \(\ell\), outside the protected boundary triples.
Relative triple pinning inside them leaves both functions in
(7) fixed. With \(a_d=1000(99/101)^{2d}\), define the
finite left and right functionals exactly as in the cited theorem:
\[
 \begin{split}
 \mathcal T_{L,N}^{R,d}
   &=\sup\{B_{L,N}-D_L+a_d(x_{u_L}-\Re r_{u_L})^2\},\\
 \mathcal T_{R,N}^{R,d,\rm con}
   &=\sup\{B_{R,N}^{\rm con}-D_R
                          +a_d(x_{v_R}-\Re r_{v_R})^2\}.
 \end{split}
 \tag{11}
\]
The suprema include every physical boundary state, every selection,
the bounded retained window and its possible good-block positions;
only that chosen block is required to be unselected plateau.
The same exact fee payment and disjoint residual splitting give
\[
 \sup F_N^{\rm con}
 \le\max\{-\zeta,
        \mathcal T_{L,N}^{R,d}+\mathcal T_{R,N}^{R,d,\rm con}\}.
 \tag{12}
\]
Before taking suprema the stronger estimate retains
\(-\kappa\sum_{j\in M}p_j/2\) in the remaining middle.
The reference data of both functionals may be kept coupled;
independent maximization is only a sufficient relaxation.
Shorter words remain bounded-length complete source problems.

## 4. The precise improvement and the remaining sign

Equation (12) is a sufficient criterion for the full retained
source (3), not just for a prescribed plateau collar sector.
It permits the established complete \(\mathcal V\) envelopes
to be used directly wherever their original target and reference
conditions hold. No plateau supporting plane for \(\mathcal V\)
is extended to a reset height or a nonplateau target without its
own proved source bound. Elsewhere (11) keeps the literal polynomial.

The benefit is exact terminal cancellation before modulus, not a
pointwise ordering of differently parametrized old and new graphs.
For fixed retained inputs, (1) does give
\[
 |\mathcal V_{\epsilon,N}(w,X)|
 \le N\int_{|Y|=\rho}
    |C_{\epsilon,N}(X,Y)H_N(w,Y^{-1})W_{\epsilon,N}(Y)|
                               \frac{|dY|}{2\pi|Y|}.
 \tag{13}
\]
Thus a fiber-integrated old absolute bound on those same retained
inputs implies the contracted bound, while the converse need not
hold. The factor \(N\) agrees with the outer normalization in
(3). If old retained heights varied with the private variable,
they are not these fixed inputs; no pointwise comparison of its
old boundary function with (11) follows. Both torus constructions
still represent the same entire original source.

The unresolved estimate is a calibrated upper sign for (11) over
all its boundary states, with strict complementary losses away
from the geometric packet and uniform ordinary-color control.
The already proved plateau, selected-end and active-first-collar
theorems settle subdomains of those states; they do not settle the
remaining suprema. Mere global nonpositivity also does not establish
noncancellation of the local packet. This reduction proves no full
open-source asymptotic, new knot theorem, or finite-exceptions claim.
