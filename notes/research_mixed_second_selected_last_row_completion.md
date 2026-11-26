# Removing both last-row profiles from the second-position comparison

Research theorem, 6 November 2026.

For a selected second coordinate, with the first coordinate unselected,
both periodic last-row profiles are now controlled. The full finite
comparison reduces from thirty-two terms to eighteen. The remaining
terms involve only the two main contours and their real cuts; their
uniform signs have not been proved.

## 1. The original finite product

Use the notation of
[the second-position reduction](research_mixed_second_selected_plateau_reduction.md).
Fix a positive three/four word of length \(m\ge4\), with first flags
\((\alpha,1,\beta)\), where \(\alpha,\beta\in\{0,1\}\).
The selected second height is \(H=1/100\). Coordinates 1 and 3
retain their actual heights, and all three real targets range over
\(P=[.22,.45]\). The finite product to bound is
\[
 \mathcal B_{23,N}
 =|C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)d_N(X_2)X_2^{-N}|
                  |d_N(X_1)|^{\alpha/2}|d_N(X_3)|^{\beta/2}.
 \tag{1}
\]
The original affine function \(\Lambda_{23}\) retains both boundary
derivatives. In particular its reference value is the action of
these two factors with their exact weight allocations.

For either factor, \(R_0\) is the main-contour maximum, \(R_L,R_R\)
are its real cut values, and \(R_1\) is the full periodic last-row
rate. Write
\[
 \begin{split}
 W_{\mathrm{fac}}&=-\Re g(z_2)-2\pi H,\qquad
 W_{\mathrm{force}}=0,\\
 \mathcal E_{ij,\nu}
   &=R_i^2(z_1,z_2)+R_j^3(z_2,z_3)
        -\frac\alpha2\Re g(z_1)-\frac\beta2\Re g(z_3)
                 +W_\nu-\Lambda_{23}.
 \end{split}
 \tag{2}
\]
Superscripts 2 and 3 specify the ordinary factors. Each index
\(i,j\) initially ranges over \(\{0,L,R,1\}\), and \(\nu\)
ranges over the two Fourier alternatives. These are the original
thirty-two upper rates, including every finite row and contour current.

## 2. The two completed comparisons

The
[outgoing-selected own-four comparison](research_mixed_selected_outgoing_four_last_row_domination.md)
has now passed its complete scalar certificate:
\[
                         R_1^2<R_0^2-\frac1{50}.
 \tag{3}
\]
It applies on the containing rectangle
\[
 -27/250\le\Im z_1\le17/250,\qquad
 -51/500\le\Im s_2^*\le-1/1000,
 \tag{4}
\]
which includes both attached first types and every actual own-four
index here. Its proof reduces to four functions of that index
height. The saved
[128-check result](../repro/results/research-mixed-selected-outgoing-four-last-row-domination.json)
uses outward arithmetic at 160 bits and an analytic Lipschitz bound
on each of 32 closed intervals. Its smallest rational lower bound
exceeds \(0.0245897\), hence exceeds the required \(1/50\).
All four corners and every interval are present; there is no pending
parameter region.

The result's SHA256 is
23f975f20c70e2f22a197c705d7225c37a30f175c13e92e59353410543d64eeb.
The fixed-grid check evaluates the original primitive at explicit
points. It does not solve a critical equation or evaluate a quantum sum.

The separate
[outgoing last-row transport theorem](research_mixed_second_selected_outgoing_last_rows.md)
proves
\[
 \mathcal E_{i1,\nu}
       <-\frac1{400}
        -\frac{(x_1-a_1)^2+2(x_2-a_2)^2+(x_3-a_3)^2}{2500000},
 \qquad i=0,L,R,
 \tag{5}
\]
for both alternatives. This proof uses elementary argument bounds
and the already established unselected current comparisons. Its
negative reference height is retained throughout.

## 3. Eighteen remaining terms

Define
\[
 \mathfrak D_{23}^{(18)}
 =\max_{\substack{i,j\in\{0,L,R\}\\
                    \nu\in\{\mathrm{fac},\mathrm{force}\}}}
                           \mathcal E_{ij,\nu}.
 \tag{6}
\]

**Theorem 1.** For every \(\tau>0\), the complete finite product (1)
satisfies
\[
 \mathcal B_{23,N}\le C_\tau N^{A_\tau}
 \exp N\left\{\Lambda_{23}
       +\max\left(-\frac1{400},\mathfrak D_{23}^{(18)}\right)+\tau\right\}.
 \tag{7}
\]
Both parities of \(N\), all original rows and all contour contributions
are included. The assertion is uniform on the stated real plateau
and actual reference families.

*Proof.* By (3), every term with \(i=1\) is strictly below its
counterpart with \(i=0\), with the same \(j,\nu\). Removing those
eight terms from the original maximum changes none of its upper-bound
content. Of the remaining twenty-four terms, (5) bounds the six with
\(j=1\). The other eighteen are exactly (6). Apply Proposition 1 of
the original finite-current reduction, with one total tolerance
\(\tau\). This gives (7). \(\square\)

For a total tolerance less than \(1/800\), the explicitly removed
outgoing-last-row contributions retain an exponential gap \(1/800\).
Equation (3) also covers the two-last-row profile pair: its left
factor is replaced by its main profile, after which (5) applies.
There is no omission of that pair.

Two of the eighteen remaining terms are the main/main comparison,
one for each Fourier alternative. Their exact five-variable objective
and convex dual are written in
[the central-budget deduction](research_mixed_second_selected_central_budget.md).
The [index-barrier proof](research_mixed_second_selected_horizontal_concavity.md)
restricts its maximization to
\[
 P\times[.22,.5]\times P\times[q_\beta,.5]\times P,
                    \qquad q_0=.2,\quad q_1=.22,
 \tag{8}
\]
without changing either maximum. The other sixteen terms involve
at least one real cut. Neither the central scalar signs nor these
sixteen cut comparisons follow from (7).

The case with both first coordinates selected has a different
three-factor product and remains outside this theorem. The remaining
boundary positions, nonplateau regions, whole-source boundary-color
estimates, and arbitrary short partial fillings are also unchanged.
