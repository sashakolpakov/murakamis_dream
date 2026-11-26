# Connected left contours for the two initial-four/three Fourier currents

Private written assembly, 10 November 2026. For an actual positive
three/four word beginning with four and three, the specified two
first-coordinate paths can start at zero, run to one tenth on the
real axis, and join their original unselected or selected horizontal
intervals through real part \(9/20\). Their sum retains the original
nonzero unselected plateau coefficient. Every later retained
coordinate stays unselected in its plateau at its actual height.

The paths end at different right endpoints. They are partial paths,
not full periods; no missing right connection or later-coordinate
departure is identified with zero.

## 1. Exact source, paths and theorem

Fix an actual positive three/four open word \(n_j=3+\epsilon_j\),
\(1\le j\le m\), with
\[
 m\ge3,\qquad \epsilon_1=1,\quad\epsilon_2=0,\qquad
 h=m-1,\quad k_4=\sum_{j=1}^m\epsilon_j.
\tag{1}
\]
Keep its reference \(r_j=a_j+ic_j\), logarithmic lifts, marking and
ordinary colors \(\mathbf w=(w_L,w_R)\). Put
\[
 P=[11/50,9/20],\quad E=[1/10,11/50],\quad
 J=[1/10,9/20],\quad \kappa_0=1/2500000,
\]
\[
 \gamma_{43}=\min\{\kappa_0,\nu/4\}(a_1-11/50)^2,\qquad
                         0<\gamma_{43}<1/2000.
\tag{2}
\]
Here \(\nu>0\) is exactly the original central Schur constant
retained by the [complete first-four/three source](research_mixed_early_four_three_complete_pair.md).
The actual bound \(a_1>.246\) makes this gap uniformly positive on
the stated family. It is not replaced by a larger numerical gap.

After the original exact terminal contraction, retain the two
summands
\[
\begin{split}
 \mathscr J_{\sigma,N}(\mathbf z;\mathbf w)
 ={}&U_{1,N}(w_L,X_1)
       \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)\\
 &\quad\cdot d_N(X_1)X_1^{-N\sigma}
                 \prod_{j=2}^{h}d_N(X_j)^{\epsilon_j},
 \qquad X_j=e^{-2\pi iz_j},\quad \sigma\in\{0,1\}.
\end{split}
\tag{3}
\]
Every other retained Fourier choice is zero. The terminal transform
\(\mathcal V\) already contains all terminal physical rows, its
entire own weight and both terminal Fourier alternatives. No further
terminal selection is made in (3).

Equation (13) of the
[exact terminal contraction](research_mixed_reversed_cap_assembly.md)
gives the unchanged outside scalar
\[
                         S_N=\kappa_N^{m+k_4}N^{m+k_4-1},
                         \qquad |\kappa_N|=1.
\tag{4}
\]
The contraction removes one power of \(N\) from the uncontracted
scalar and retains the original asymmetric conditional kernel.
No symmetry of its two arguments is invoked.

Define the ordered first paths
\[
 \mathcal C_\sigma:\quad
 0\longrightarrow\frac1{10}
 \longrightarrow\frac1{10}+iH_\sigma
 \longrightarrow\frac9{20}+iH_\sigma,\qquad
 H_0=c_1,\quad H_1=\frac7{625}.
\tag{5}
\]
The first vertical piece goes down for \(\sigma=0\) and up for
\(\sigma=1\). Every later retained coordinate has
\[
                         z_j=x_j+ic_j,\quad x_j\in P,\quad 2\le j\le h.
\tag{6}
\]
With the original increasing-angle orientation, set
\[
\begin{split}
 \mathcal L_N(\mathbf w)
 &=S_N\sum_{\sigma=0}^1
   \int_{\mathcal C_\sigma\times\prod_{j=2}^{h}(P+ic_j)}
     \mathscr J_{\sigma,N}(\mathbf z;\mathbf w)\,
                                      dz_1\cdots dz_h,\\
 \mathcal Z_N^P(\mathbf w)
 &=S_N\int_{\prod_{j=1}^{h}(P+ic_j)}
     \mathscr J_{0,N}(\mathbf z;\mathbf w)\,dz_1\cdots dz_h.
\end{split}
\tag{7}
\]
This is the same angular convention as the plateau theorem:
the increasing horizontal measure is \(dx_1\cdots dx_h\), and a
vertical piece uses \(dz_1=i\,dy\) with its prescribed direction.
No new sign or \(2\pi\) factor is inserted.

Let \(L_1,\phi_j,\Pi\) be the original allocated cap, ordinary and
terminal phases. Write
\[
 \Phi(\mathbf z)=L_1(z_1)+\sum_{j=2}^{h}\phi_j(z_{j-1},z_j)+\Pi(z_h),
 \qquad M_{\rm open}=\Re\Phi(\mathbf r),\qquad
                         \nabla\Phi(\mathbf r)=0.
\tag{8}
\]

**Theorem 1.** For every \(\tau>0\), both parities satisfy
\[
 |\mathcal L_N(\mathbf w)-\mathcal Z_N^P(\mathbf w)|
 \le C_{m,\tau}N^{A_{m,\tau}}
            e^{N\{M_{\rm open}-\gamma_{43}+\tau\}}
\tag{9}
\]
on sufficiently small fixed ordinary-color disks about \((-2,-2)\).
Every fixed ordinary-color derivative obeys the corresponding
estimate on smaller disks, with polynomial cost.
Consequently
\[
 \mathcal L_N(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)e^{N\mathcal F_m(\mathbf w)}
                 \{1+O_{\rm hol}(N^{-1})\},\qquad A_m\ne0.
\tag{10}
\]
The phase, coefficient, Gaussian branch, marking and every fixed
normalized ordinary-color jet are exactly those of the original
unselected plateau theorem. In particular
\(\mathcal F_m(-2,-2)=\Phi(\mathbf r)\).
This statement concerns the defined connected partial-path sum (7).

## 2. The complete first-pair bounds

For \(a=z_1\), \(b=x_2+ic_2\), retain the literal pair
\[
 K_{\sigma,N}(w;a,b)=
 U_{1,N}(w,e^{-2\pi ia})
 C_{0,N}(e^{-2\pi ia},e^{-2\pi ib})
 d_N(e^{-2\pi ia})e^{2\pi iN\sigma a}.
\tag{11}
\]
There is no outgoing halfweight at coordinate two, because
\(\epsilon_2=0\). The whole first weight and its indicated
selection are already in (11). Define
\[
 M_{12}=\Re\{L_1(r_1)+\phi_2(r_1,r_2)\},\quad
 p_R=\partial_2\phi_2(r_1,r_2),\quad
 \Lambda_{12}(x_2)=M_{12}+\Re p_R(x_2-a_2).
\tag{12}
\]
Every input below uses exactly this affine rate, the same actual
second height, both parities and fixed ordinary-color disks:
\[
 |K_{\sigma,N}(w;a,b)|
 \le C_\eta N^{A_\eta}
       e^{N\{\Lambda_{12}(x_2)-\delta+\eta\}},
                         \qquad x_2\in P.
\tag{13}
\]

| First path piece | Selection | Gap \(\delta\) | Complete source |
|---|---|---|---|
| \(a=x,\ 0\le x\le1/10\) | \(0\) or \(1\) | \(1/2000\) | Real first-interval theorem |
| \(a=1/10+iy,\ c_1\le y\le0\) | \(0\) | \(\gamma_{43}\) | Signed negative-height connection |
| \(a=x+ic_1,\ x\in E\) | \(0\) | \(\gamma_{43}\) | Complete actual-height pair |
| \(a=1/10+iy,\ 0\le y\le7/625\) | \(1\) | \(1/2000\) | Positive-height connection |
| \(a=x+7i/625,\ x\in J\) | \(1\) | \(1/2000\) | Selected early and plateau assembly |

The [real-interval theorem](research_mixed_four_three_real_first_interval.md),
Theorem 1, includes \(x=0\) by exact Laurent continuation from
a proved nondegenerate real interval. It does not continue a
factorial symbol through its logarithmic endpoint.

The [negative connection](research_mixed_first_four_three_negative_height_face.md),
Theorem 1 and equation (21), keeps the wrapped ordinary block as a
signed sum. Its common convex envelope contains the two wall rates,
not an absolute envelope of its wrapped rows. Its stronger bound
also retains
\(-(1-\theta)\kappa_0(x_2-a_2)^2\), where
\(\theta=(y-c_1)/(-c_1)\).

The complete actual-height pair, Theorem 1, and equations (4)--(5)
of the [initial43 early assembly](research_mixed_initial43_early_boundary_assembly.md)
give the third row with the additional outgoing term
\(-\kappa_0(x_2-a_2)^2\). Its reserve is the full original
\(\gamma_{43}\), including the smaller central Schur constant.

The [positive connection](research_mixed_selected_four_three_positive_height_connection.md)
proves the fourth row by the same selected raw envelope at its
two endpoints. All cap profiles, ordinary joins and aliases,
physical rates and both Fourier upper alternatives are retained.
No convexity of a finite modulus or interpolation between different
Fourier choices is used.

Finally Section 1 and Theorem 1 of the
[selected early assembly](research_mixed_selected_early_boundary_assembly.md)
give the last row on \(J\times P\). The early complete selected
source and its plateau source have the same height \(7/625\),
allocation (11) and outgoing derivative (12). No cap or ordinary
main-integral approximation replaces these complete finite kernels.

All five source inputs hold on the actual length-\(m\ge3\) family,
including the attached next-input case at length three. Their
complete real-color bounds supply the fixed disks used in (13).

## 3. Remaining weights, marginals and the length-three case

For the later real targets define
\[
 \mathcal Q_{\rm rem}(\mathbf x)=
 \kappa_0(x_2-a_2)^2+
                     2\kappa_0\sum_{j=3}^{h}(x_j-a_j)^2.
\tag{14}
\]
The sum is empty at \(m=3\). Multiplying (13) by the remaining
complete unselected supporting planes gives, on each added piece,
\[
 |\mathscr J_{\sigma,N}|
 \le C_{m,\tau}N^{A_{m,\tau}}
 e^{N\{M_{\rm open}-\delta-\mathcal Q_{\rm rem}(\mathbf x)+\tau\}}.
\tag{15}
\]

Indeed, the consumed pair is exactly \(U_1C_0d_N(X_1)X_1^{-N\sigma}\).
Coordinate two has no diagonal factor, so neither an outgoing
halfweight nor a compensating halfweight at the next factor is
inserted. The remaining factors are
\[
 \prod_{j=3}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
                      \mathcal V_{\epsilon_m,N}(w_R,X_h)
\]
with their original unselected half allocations at coordinates
of type four. These halves multiply to the integer powers in
(3), including at their zeros. No division or choice of a
holomorphic halfpower is used.

The ordinary estimates are Theorem 1 of the
[complete ordinary source assembly](research_mixed_three_row_source_assembly.md);
the terminal estimate is the terminal entry of equation (5) of
the [whole unselected plateau theorem](research_mixed_full_unselected_plateau.md).
All their targets are in \(P\) at their actual heights. Their
constants and \(M_{12}\) sum to \(M_{\rm open}\). The first
uncancelled marginal is cancelled by
\[
 p_R+\partial_1\phi_3(r_2,r_3)=0\quad(h\ge3),\qquad
 p_R+\Pi'(r_2)=0\quad(h=2).
\tag{16}
\]
Every later marginal cancels by (8).

After the consumed pair, coordinate two has one remaining
incidence and receives one quadratic loss. Every \(j\ge3\)
has two remaining incidences and receives two. This proves
(14)--(15). At \(m=3\), \(h=2\), the terminal transform directly
supplies the one remaining coordinate-two loss and the second
equation of (16). Its incoming flag is zero, since coordinate
two has type three; its own flag \(\epsilon_m\) is already
inside \(\mathcal V_{\epsilon_m,N}\). No intervening ordinary
factor or extra diagonal power is introduced.
The additional outgoing quadratic of the unselected early or
negative-vertical pair remains favorable and can be retained.

For the fixed word, choose the finitely many source tolerances
inside one prescribed \(\tau\) and intersect their fixed color
disks. Derivative bounds apply to the entire holomorphic product
by Cauchy's formula on smaller disks. No modulus halfweight is
differentiated.

## 4. Exact additive identity and preservation of the coefficient

Let \(R=[0,1/10]\),
\(V_\sigma=[1/10,1/10+iH_\sigma]\),
\(E_0=E+ic_1\),
\(J_1=J+7i/625\), and
\(\mathcal P'=\prod_{j=2}^{h}(P+ic_j)\), all with the
orientations induced by (5). Splitting only the unselected
horizontal interval at \(11/50+ic_1\) gives exactly
\[
\begin{split}
 S_N^{-1}(\mathcal L_N-\mathcal Z_N^P)
 ={}&
 \int_{R\times\mathcal P'}\mathscr J_{0,N}
 +\int_{V_0\times\mathcal P'}\mathscr J_{0,N}
 +\int_{E_0\times\mathcal P'}\mathscr J_{0,N}\\
 &+\int_{R\times\mathcal P'}\mathscr J_{1,N}
 +\int_{V_1\times\mathcal P'}\mathscr J_{1,N}
 +\int_{J_1\times\mathcal P'}\mathscr J_{1,N}.
\end{split}
\tag{17}
\]
The additive product differential from (7) is understood in every
term. Shared endpoints have measure zero. The two real pieces are
distinct Fourier currents, although their monomials have the same
modulus there; they are not replaced by twice one summand.

Every term in (17) is controlled by (15), with
\(\delta\ge\gamma_{43}\). All lengths and volumes are fixed.
The original scalar (4) contributes its polynomial power and unit
phase, so integration proves (9). This is additivity of specified
restricted paths, not a deformation through an unestimated region.
The exact Laurent functions have no singularity on these paths,
including the point \(X_1=1\).

Theorem 2 of the whole unselected plateau theorem gives
\[
 \mathcal Z_N^P(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
 e^{N\mathcal F_m(\mathbf w)}
                       \{1+O_{\rm hol}(N^{-1})\}.
\tag{18}
\]
Its original complete-color coefficient is
\[
 A_m(-2,-2)=
       \frac{(2\pi)^{h/2}b(\mathbf r)}
             {\sqrt{\det[-\Phi''(\mathbf r)]}}\ne0,
\tag{19}
\]
with the original accretive root, source symbols and orientation.
The terminal coefficient already includes its inner Gaussian;
no extra terminal scalar or Gaussian is inserted. The original
calibration fixes \(\mathcal F_m(-2,-2)=\Phi(\mathbf r)\),
including the additive constant and logarithmic lift.

Choose the total allowance in (9) below \(\gamma_{43}/8\).
Shrink the common ordinary-color disks so that
\(\Re\mathcal F_m>M_{\rm open}-\gamma_{43}/8\) and \(A_m\)
is bounded away from zero. The quotient of (9)'s holomorphic
error by the original leading term of (18) is exponentially small,
including its polynomial prefactor. Cauchy's formula gives the
same assertion for every fixed normalized ordinary-color jet on
smaller disks. Adding the error proves (10), with precisely the
original coefficient and power \(N^{-3/2}\).

This assembly pays only the two paths (5) with all later retained
coordinates as in (6). Their right endpoints
\(9/20+ic_1\) and \(9/20+7i/625\) have separate unestimated
connections and remaining periods. Later retained selections and
departures from \(P\) are also outside this theorem. Completeness
of the already contracted terminal does not complete these other
periods. No whole-word, ordinary-closure, knot or finite-exception
conclusion is asserted.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_reversed_cap_assembly.md | 79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c |
| research_mixed_four_three_real_first_interval.md | 158b92274fa70b67623568babe0b67089fc17221e24242981f4bdbfb6bdd6c5b |
| research_mixed_first_four_three_negative_height_face.md | a9780a1837dc23b01e2e6582d8e865733fe158eaa713feb9e8907f284590ea03 |
| research_mixed_selected_four_three_positive_height_connection.md | 014e2ccd25f55d7e9e8ba231af1c2b377366fe62f37c583ab05df4524c5c9eb8 |
| research_mixed_early_four_three_complete_pair.md | 271c54a8c5bb9a9fd292dcc66bc760f2cd637f8a685d14fa6722f1eab4d70575 |
| research_mixed_initial43_early_boundary_assembly.md | 8174ad95137353bdcb0acec24497d8fa0087ece417e0f2ddd72ceaf2a26f72fd |
| research_mixed_selected_early_boundary_assembly.md | 0643c85c8b30bbf5a927551470538e024ae3b8b1ec0be7ec20e845708f6bef73 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |

The full written proof and directly used source implications were
read. No mathematical numerical evaluation, saved-value arithmetic,
import, test, compilation or frozen-source edit was performed.
