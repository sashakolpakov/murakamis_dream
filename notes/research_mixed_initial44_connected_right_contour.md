# Connecting the initial four/four partial contours to the real point seven tenths

Private written consequence, 10 November 2026. The two original first
Fourier summands admit specified right extensions from real part
\(9/20\) to the real point \(7/10\). The unselected extension first
keeps its actual negative height; the selected extension first keeps
height \(1/100\). Each then reaches the real axis at real part \(1/2\).
The complete first pair is paid along every added piece.

With all later retained coordinates unselected on their original
plateaux, adding these paths to the established connected left
contours gives paths from zero to \(7/10\), with the same original
nonzero coefficient. The rectangular partial integrals admit the
same right enlargement. These are additive assertions about
specified currents, not whole-period deformations.

## 1. Literal source, paths and measure

Fix an actual positive three/four word \(n_j=3+\epsilon_j\), with
\[
 m\ge3,\qquad \epsilon_1=\epsilon_2=1,\qquad
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j .
 \tag{1}
\]
Keep its original reference \(r_j=a_j+ic_j\), marking, logarithmic
lifts and ordinary colors \(\mathbf w=(w_L,w_R)\). Put
\[
 P=[11/50,9/20],\quad J=[1/10,9/20],\quad
 H_0=c_1,\quad H_1=1/100,\quad
 \kappa_0=1/2500000,\quad
 d_R=\frac{\kappa_0}{2}(9/20-a_1)^2 .
 \tag{2}
\]
The actual first-four bound \(a_1<.350\) gives
\(d_R>\kappa_0/200>0\). All later retained coordinates stay on
\[
 \mathcal P'=\prod_{j=2}^{h}(P+ic_j).
 \tag{3}
\]
The ranges and all attached-input conditions of the four cited pair
theorems are those of this same actual word, including \(m=3\).

Let \(\mathcal R_\sigma\) have the ordered vertices
\[
 \frac9{20}+iH_\sigma
 \ \longrightarrow\ \frac12+iH_\sigma
 \ \longrightarrow\ \frac12
 \ \longrightarrow\ \frac7{10},\qquad \sigma=0,1.
 \tag{4}
\]
Thus its middle segment is upward for \(\sigma=0\) and downward
for \(\sigma=1\). Its last segment is real in both cases, but the
two finite Fourier summands on it remain distinct.

After the exact terminal contraction, those summands are
\[
\begin{split}
 \mathscr J_{\sigma,N}(\mathbf z;\mathbf w)
 ={}&U_{1,N}(w_L,X_1)
       \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)\\
 &\quad{}\cdot d_N(X_1)X_1^{-N\sigma}
                  \prod_{j=2}^{h}d_N(X_j)^{\epsilon_j},
 \qquad X_j=e^{-2\pi iz_j}.
\end{split}
 \tag{5}
\]
All later retained selections are zero. The complete terminal
transform already contains its own rows, entire diagonal weight,
terminal Fourier alternatives and ordinary-color dependence.
The source is exactly equation (13) of
[terminal contraction](research_mixed_reversed_cap_assembly.md), with
outside scalar
\[
 S_N=\kappa_N^{m+k_4}N^{m+k_4-1},\qquad |\kappa_N|=1.
 \tag{6}
\]
In the inherited increasing-angle convention, the additive measure is
\(dz_1\cdots dz_h\). Equivalently the same normalization is
\[
 S_N\,dz_1\cdots dz_h
   =\kappa_N^{m+k_4}N^{k_4}\prod_{j=1}^{h}(N\,dz_j).
 \tag{7}
\]
This displays the original positive \(N\,dz_j\) outer residue
measures without inserting another power of \(N\). On a vertical
segment \(dz_1=i\,dy\), with its prescribed orientation. The
angular convention is precisely that of the plateau theorem:
the clockwise exponential parametrization cancels the sign in
\(dX_j/(2\pi iX_j)=-dz_j\). No new sign or \(2\pi\) is supplied.

## 2. Every right-path piece has the same complete-pair bound

Use the original allocated phases \(L_1,\phi_j,\Pi\), and set
\[
\begin{split}
 M_{12}&=\Re\{L_1(r_1)+\phi_2(r_1,r_2)\},&
 p_R&=\partial_2\phi_2(r_1,r_2),\\
 \Lambda(x_2)&=M_{12}+\Re p_R(x_2-a_2),&
 \Phi(\mathbf z)&=L_1(z_1)+\sum_{j=2}^{h}\phi_j(z_{j-1},z_j)
                       +\Pi(z_h),\\
 M&=\Re\Phi(\mathbf r),& \nabla\Phi(\mathbf r)&=0 .
\end{split}
 \tag{8}
\]
These are the original action and marginal, including their additive
constants. For any prescribed positive allowance \(\tau\), the four
complete finite-source inputs give
\[
\begin{split}
 &|U_{1,N}(w_L,X_1)C_{1,N}(X_1,X_2)
                  d_N(X_1)X_1^{-N\sigma}|\,
                  |d_N(X_2)|^{1/2}\\
 &\hspace{22mm}\le C_\tau N^{A_\tau}
           \exp N\{\Lambda(x_2)-d_R+\tau\},
 \qquad z_1\in\mathcal R_\sigma,\quad z_2=x_2+ic_2,\quad x_2\in P .
\end{split}
 \tag{9}
\]
Here is the separate source for each piece:

| Piece | Original complete-source bound |
|---|---|
| Unselected horizontal \(9/20+ic_1\) to \(1/2+ic_1\) | Theorem 1 of [the right-half interval](research_mixed_initial44_right_half_interval.md), with gap \(2d_R\) and an additional favorable outgoing quadratic. |
| Selected horizontal \(9/20+i/100\) to \(1/2+i/100\) | Theorem 1 of [the selected right-half interval](research_mixed_selected44_right_half_interval.md), with gap \(1/4000>d_R\). |
| Either vertical at real part \(1/2\) | Theorem 1 of [the half-face height connections](research_mixed_initial44_half_face_height_connections.md), with gap \(d_R\). |
| Either real horizontal from \(1/2\) to \(7/10\) | The theorem of [the real-right interval](research_mixed_initial44_real_right_horizontal.md), with gap \(d_R\). |

Each input includes all finite cap and conditional rows, both physical
ends, aliases, joins and parity stops. The Fourier factor in (9)
is the full \(d_N(X_1)X_1^{-N\sigma}\), not a chosen asymptotic
branch. The vertical and real-interval sources explicitly retain both
upper alternatives for that polynomial. In particular the selected
monomial is not deleted on the real segment merely because its
modulus is one. The outgoing halfweight has the same allocation
throughout. The bounds hold for all real \(w_L\) and on small fixed
ordinary-color disks at a separately assigned arbitrary allowance.

Define the nonnegative remaining loss
\[
 \mathcal Q_{\rm rem}(\mathbf x)
   =\kappa_0(x_2-a_2)^2+
                    2\kappa_0\sum_{j=3}^{h}(x_j-a_j)^2 .
 \tag{10}
\]
The sum is empty for \(m=3\).

**Proposition 1.** For every \(\tau>0\), the literal full integrand
satisfies, on either right path times (3),
\[
 |\mathscr J_{\sigma,N}|
 \le C_{m,\tau}N^{A_{m,\tau}}
       \exp N\{M-d_R-\mathcal Q_{\rm rem}(\mathbf x)+\tau\}.
 \tag{11}
\]
Both parities and fixed sufficiently small ordinary-color disks about
\((-2,-2)\) are included. Every fixed color derivative has the
corresponding upper rate on smaller disks.

*Proof.* Apply (9), then multiply by the complete unselected
ordinary and terminal supporting planes in equation (5) of the
[whole plateau theorem](research_mixed_full_unselected_plateau.md).
The ordinary inputs are Theorem 1 of
[ordinary source assembly](research_mixed_three_row_source_assembly.md);
all their targets still lie in \(P\) at the original heights.

The first weight in (5) has already been consumed in full by (9).
The other half of \(|d_N(X_2)|\) belongs to factor three when
\(h\ge3\), or directly to the terminal transform when \(h=2\).
The remaining halves multiply to their original integer powers at
every later coordinate. These are modulus identities also at zeros;
there is no division by a Fourier polynomial or choice of a
holomorphic square root.

The constants sum to \(M\). The first remaining linear term cancels
by the original stationary equation
\[
 p_R+\partial_1\phi_3(r_2,r_3)=0\quad(h\ge3),\qquad
 p_R+\Pi'(r_2)=0\quad(h=2).
 \tag{12}
\]
All later marginals cancel by (8). Coordinate two receives one
remaining quadratic incidence; each later coordinate receives two.
This is exactly (10). Any stronger outgoing loss from a pair input
may be dropped. At \(m=3\) the single terminal incidence supplies
both the other halfweight and the one quadratic at coordinate two;
no extra ordinary kernel is inserted.

Split the total allowance among the fixed finite number of factors
and intersect their color disks. Cauchy's formula on smaller disks
applies to the complete holomorphic product (5); no modulus
halfweight is differentiated. This proves the proposition. \(\square\)

## 3. Connected paths from zero to seven tenths

Use the paths of the adopted
[connected-left theorem](research_mixed_initial44_connected_left_contour.md):
\[
 \mathcal C_\sigma:\quad
 0\longrightarrow\frac1{10}\longrightarrow
 \frac1{10}+iH_\sigma\longrightarrow\frac9{20}+iH_\sigma .
 \tag{13a}
\]
Concatenate \(\mathcal G_\sigma=\mathcal C_\sigma*\mathcal R_\sigma\).
The full ordered path is therefore
\[
 0\longrightarrow\frac1{10}\longrightarrow
 \frac1{10}+iH_\sigma\longrightarrow
 \frac12+iH_\sigma\longrightarrow\frac12
                                      \longrightarrow\frac7{10}.
 \tag{13b}
\]
The horizontal point \(9/20+iH_\sigma\) is still the source
partition between the left and right theorems.
Define
\[
\begin{split}
 \mathcal L_N(\mathbf w)
    &=S_N\sum_{\sigma=0}^1
       \int_{\mathcal C_\sigma\times\mathcal P'}\mathscr J_{\sigma,N}
                                      \,dz_1\cdots dz_h,\\
 \mathcal G_N(\mathbf w)
    &=S_N\sum_{\sigma=0}^1
       \int_{\mathcal G_\sigma\times\mathcal P'}
                         \mathscr J_{\sigma,N}\,dz_1\cdots dz_h .
\end{split}
 \tag{13}
\]
The first line is precisely the current of the connected-left
theorem, with unchanged source, scalar and orientation.

Path additivity gives the exact finite identity
\[
 \mathcal G_N-\mathcal L_N
  =S_N\sum_{\sigma=0}^1
     \int_{\mathcal R_\sigma\times\mathcal P'}
                          \mathscr J_{\sigma,N}\,dz_1\cdots dz_h .
 \tag{14}
\]
Each right integral splits into its three ordered pieces in (4).
Shared endpoints have zero measure. The two real-segment integrals
are retained separately. Equation (14) does not identify either
summand with an unestimated current at a different height.

All path lengths and later volumes are fixed. Proposition 1 and
the polynomial modulus of (6) therefore give
\[
 |\mathcal G_N-\mathcal L_N|
       \le C_{m,\tau}N^{A_{m,\tau}}e^{N(M-d_R+\tau)} .
 \tag{15}
\]
This estimate and its fixed color derivatives have the same fixed
ordinary-neighborhood scope as the proposition.

Let \(\mathcal Z_N^P\) be the original unselected plateau integral.
The connected-left theorem has gap
\(\gamma_{44}=\kappa_0(a_1-11/50)^2>0\) against that integral.
Thus, with \(\gamma_*=\min\{\gamma_{44},d_R\}>0\), the triangle
inequality and (15), allocating one total allowance, give
\[
 |\mathcal G_N-\mathcal Z_N^P|
       \le C_{m,\tau}N^{A_{m,\tau}}e^{N(M-\gamma_*+\tau)} .
 \tag{15a}
\]

**Corollary 2.** The connected restricted sum (13) has exactly the
original plateau asymptotic
\[
 \mathcal G_N(\mathbf w)=
   \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
       e^{N\mathcal F_m(\mathbf w)}
                      \{1+O_{\rm hol}(N^{-1})\},\qquad A_m\ne0 .
 \tag{16}
\]
Its action, leading coefficient, Gaussian branch, marking, orientation
and every fixed normalized ordinary-color jet are unchanged.

*Proof.* The whole plateau theorem gives (16) for
\(\mathcal Z_N^P\). In particular
\(\mathcal F_m(-2,-2)=\Phi(\mathbf r)\), with its original
additive constant. Choose the allowance in (15a) below \(\gamma_*/8\),
then shrink the common color disks so that
\(\Re\mathcal F_m>M-\gamma_*/8\) and \(A_m\) is bounded away
from zero. The quotient of (15a) by the original leading term is
exponentially small and holomorphic; its polynomial factor is
absorbed for sufficiently large \(N\). Cauchy's formula supplies
the same conclusion for fixed normalized jets on smaller disks.
Adding this error proves (16). No new local Gaussian calculation
or scalar renormalization is made. \(\square\)

The rectangular version follows by the identical additive identity.
Take \(J_\sigma=J+iH_\sigma\) and
\(\mathcal D_\sigma=J_\sigma*\mathcal R_\sigma\). The sum of
integrals over \(J_\sigma\times\mathcal P'\) is the established
initial44 case of
[the selected early assembly](research_mixed_selected_early_boundary_assembly.md),
with its unselected part from
[the initial44 rectangular assembly](research_mixed_initial44_early_boundary_assembly.md).
Adding the right integrals in (14) therefore preserves that sum's
same nonzero coefficient as well. These two shorter paths start
at \(1/10+iH_\sigma\); no left-path theorem is needed for this
rectangular variant.

The later retained coordinates in this theorem are still precisely
(3), with zero selections. The terminal factor is complete, but
this does not complete any remaining retained period. The real
interval beyond \(7/10\), the periodic endpoint connection and
later-coordinate departures or selections remain outside the
conclusion. No whole-word, ordinary-closing, knot-volume or
short-partial-filling assertion follows from this restricted sum.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_initial44_right_half_interval.md | 309d6869f7438a9ed0a407c43666198ce1a039db7545c404a5e97f4ba2538c9c |
| research_mixed_selected44_right_half_interval.md | 50d7d9daaf5e33f45749b7c5ca9e2dba4fd0dca2298986d337cb58e35979ebc1 |
| research_mixed_initial44_half_face_height_connections.md | 4d83ce42628d9dcd9d965be4f75a6538c4a150ec767b436c42847a177eb352f8 |
| research_mixed_initial44_real_right_horizontal.md | bc745bb9421efd910dc8eac028fbe6391c82f84ddca4f7f03abadeb1001e4e1a |
| research_mixed_initial44_connected_left_contour.md | fca8af9ffd728962f97c4e243e19031049a94d001ae83272faaca903479f085e |
| research_mixed_initial44_early_boundary_assembly.md | 8ed393fd2e465d5399c8ffddc46c2d603ef4c5cb6d154ee561e676aa8bfd2c90 |
| research_mixed_selected_early_boundary_assembly.md | 0643c85c8b30bbf5a927551470538e024ae3b8b1ec0be7ec20e845708f6bef73 |
| research_mixed_reversed_cap_assembly.md | 79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |

The complete written deduction and directly used source implications
were read, and all ten bindings checked. No mathematical numerical
evaluation, saved-value arithmetic, import, test, compilation or
frozen-source edit was used. Independent review is required before
adoption.
