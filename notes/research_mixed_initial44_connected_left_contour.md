# A connected left contour for the two initial-four/four Fourier currents

Private written assembly, 10 November 2026. For an actual positive
three/four word beginning with two fours, the specified unselected
and selected first-coordinate paths can each start at zero, run to
one tenth on the real axis, and join their respective horizontal
intervals through real part \(9/20\). Their sum has the same nonzero
leading coefficient as the original unselected plateau integral.
The second and every later retained coordinate stay unselected on
their original horizontal plateaux.

These are connected partial paths, not complete first-coordinate
periods. Their right connectors, later-coordinate departures and
other retained Fourier choices remain outside the conclusion.

## 1. Exact source, paths and statement

Fix an actual positive three/four open word
\(n_j=3+\epsilon_j\), \(1\le j\le m\), with
\[
 m\ge3,\qquad \epsilon_1=\epsilon_2=1,\qquad
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j.
\tag{1}
\]
Keep its original reference \(r_j=a_j+ic_j\), logarithmic lifts,
ordinary colors \(\mathbf w=(w_L,w_R)\), finite kernels and marking.
Put
\[
 P=[11/50,9/20],\quad E=[1/10,11/50],\quad
 J=[1/10,9/20],\quad
 \kappa_0=1/2500000,\quad
 \gamma_{44}=\kappa_0(a_1-11/50)^2.
\tag{2}
\]
The actual first-four bound gives
\[
 \gamma_{44}>\kappa_0(13/500)^2>0,\qquad
                      \gamma_{44}<1/2000.
\tag{3}
\]

After the original exact terminal contraction, the two finite
summands considered here are
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
\tag{4}
\]
Every other retained Fourier choice is zero. The terminal transform
\(\mathcal V\) already contains every terminal row, its entire own
weight and both terminal Fourier alternatives. There is no further
terminal selection in (4).

The exact external scalar, from equation (13) of the
[terminal contraction](research_mixed_reversed_cap_assembly.md), is
\[
                         S_N=\kappa_N^{m+k_4}N^{m+k_4-1},
                         \qquad |\kappa_N|=1.
\tag{5}
\]
It has not been replaced by the uncontracted scalar, which has one
more power of \(N\). The identity uses the original chirped
conditional kernel; no symmetry in its two arguments is assumed.

Define the two first paths by their ordered vertices
\[
 \mathcal C_\sigma:\quad
 0\ \longrightarrow\ \frac1{10}
 \longrightarrow\ \frac1{10}+iH_\sigma
 \longrightarrow\ \frac9{20}+iH_\sigma,\qquad
 H_0=c_1,\quad H_1=\frac1{100}.
\tag{6}
\]
Thus \(\mathcal C_0\) goes down on its vertical segment, while
\(\mathcal C_1\) goes up. All later coordinates have
\[
                         z_j=x_j+ic_j,\qquad x_j\in P,\quad 2\le j\le h.
\tag{7}
\]
Use the original increasing-angle orientation and define
\[
\begin{split}
 \mathcal L_N(\mathbf w)
   &=S_N\sum_{\sigma=0}^1
      \int_{\mathcal C_\sigma\times\prod_{j=2}^{h}(P+ic_j)}
        \mathscr J_{\sigma,N}(\mathbf z;\mathbf w)\,
                                    dz_1\cdots dz_h,\\
 \mathcal Z_N^P(\mathbf w)
   &=S_N\int_{\prod_{j=1}^{h}(P+ic_j)}
        \mathscr J_{0,N}(\mathbf z;\mathbf w)\,
                                    dz_1\cdots dz_h.
\end{split}
\tag{8}
\]
The convention on angular orientation is exactly that of the
plateau theorem: its real horizontal measure is increasing
\(dx_1\cdots dx_h\). On a vertical piece it becomes \(dz_1=i\,dy\)
with the sign of the prescribed direction. No new \(2\pi\), sign
or normalization is introduced.

Let \(L_1,\phi_j,\Pi\) be the original allocated first-cap,
ordinary and terminal phases, and write
\[
 \Phi(\mathbf z)=L_1(z_1)+\sum_{j=2}^{h}\phi_j(z_{j-1},z_j)+\Pi(z_h),
 \qquad
 M_{\rm open}=\Re\Phi(\mathbf r),\qquad \nabla\Phi(\mathbf r)=0.
\tag{9}
\]

**Theorem 1.** For every \(\tau>0\), both level parities obey
\[
 |\mathcal L_N(\mathbf w)-\mathcal Z_N^P(\mathbf w)|
 \le C_{m,\tau}N^{A_{m,\tau}}
              e^{N\{M_{\rm open}-\gamma_{44}+\tau\}}
\tag{10}
\]
on sufficiently small fixed ordinary-color disks about \((-2,-2)\).
Every fixed ordinary-color derivative obeys the corresponding
estimate on smaller disks with polynomial cost.

Consequently the connected partial-path sum has exactly the original
plateau asymptotic
\[
 \mathcal L_N(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
 e^{N\mathcal F_m(\mathbf w)}
                       \{1+O_{\rm hol}(N^{-1})\},
 \qquad A_m\ne0.
\tag{11}
\]
Here \(\mathcal F_m(-2,-2)=\Phi(\mathbf r)\), and \(A_m\), its
Gaussian branch, marking and orientation are precisely those of the
original whole unselected plateau theorem. Every fixed normalized
ordinary-color jet has the same asymptotic. Neither (10) nor (11)
asserts that the paths (6) are whole periods or that \(\mathcal L_N\)
is the entire open-word polynomial or a knot invariant.

## 2. The complete first-pair inputs

For \(a=z_1\), \(b=x_2+ic_2\), retain the literal pair
\[
 K_{\sigma,N}(w;a,b)=U_{1,N}(w,e^{-2\pi ia})
      C_{1,N}(e^{-2\pi ia},e^{-2\pi ib})
      d_N(e^{-2\pi ia})e^{2\pi iN\sigma a}.
\tag{12}
\]
It consumes the whole first diagonal weight and the indicated first
selection. Its outgoing allocation is the separate modulus
\(|d_N(e^{-2\pi ib})|^{1/2}\).
Set
\[
 M_{12}=\Re\{L_1(r_1)+\phi_2(r_1,r_2)\},\quad
 p_R=\partial_2\phi_2(r_1,r_2),\quad
 \Lambda_{12}(x_2)=M_{12}+\Re p_R(x_2-a_2).
\tag{13}
\]
All the following inputs use exactly this affine rate and the same
actual second height \(c_2\).

Each row of this table gives the full finite bound
\[
 |K_{\sigma,N}(w;a,b)|\,|d_N(e^{-2\pi ib})|^{1/2}
 \le C_\eta N^{A_\eta}
                  e^{N\{\Lambda_{12}(x_2)-\delta+\eta\}},
\tag{14}
\]
uniformly for \(x_2\in P\), with one arbitrarily small prescribed
allowance \(\eta\), both parities and fixed ordinary-color disks.

| First path piece | Selection | Retained gap \(\delta\) | Complete source |
|---|---|---|---|
| \(a=x,\ 0\le x\le1/10\) | \(0\) or \(1\) | \(1/2000\) | Closed real-interval theorem |
| \(a=1/10+iy,\ c_1\le y\le0\) | \(0\) | \(\gamma_{44}\) | Negative-height face |
| \(a=x+ic_1,\ x\in E\) | \(0\) | \(\gamma_{44}\) | Initial44 early assembly |
| \(a=1/10+iy,\ 0\le y\le1/100\) | \(1\) | \(1/2000\) | Convex positive envelope and its two endpoints |
| \(a=x+i/100,\ x\in J\) | \(1\) | \(1/2000\) | Selected early and plateau assembly |

The [closed real-interval theorem](research_mixed_four_four_real_first_endpoint.md),
Theorem 2, proves the first row for both original monomials, including
\(X_1=1\). It uses the exact Laurent degree of the complete product,
not a factorial symbol at the logarithmic endpoint. There is no
small-collar or length-\(m\ge4\) restriction.

The [negative-height face](research_mixed_first_four_four_negative_height_face.md),
Theorem 1 and equation (23), proves the second row. Its common
ordinary contour has upper height four. Its two raw endpoint
calibrations are proved separately before interpolation. In fact it
retains the additional nonpositive term
\(-(1-\theta)\kappa_0(x_2-a_2)^2\), where
\(\theta=(y-c_1)/(-c_1)\).

Equations (5)--(6) of the
[initial44 early assembly](research_mixed_initial44_early_boundary_assembly.md)
prove the third row with the additional term
\(-\kappa_0(x_2-a_2)^2\). Its full first weight is already paid.
The [selected early assembly](research_mixed_selected_early_boundary_assembly.md),
Section 1 and Theorem 1, provides the last row from the complete
early first44 source and the complete selected plateau source.
Both keep the same fixed positive height \(1/100\), whole selected
factor and outgoing half allocation. These are comparisons of the
literal complete kernels, not their main integrals alone.

We verify the fourth row explicitly, since its use of a common raw
envelope matters. In the
[positive-height convex-envelope theorem](research_mixed_first_positive_join_convex_envelope.md)
take own flag one and \(H=1/100\). Its complete envelope
\(\mathcal E_1(y,b)\) retains the five cap profiles and separate true
ends, all ordinary main, cut, join and alias rates, the raw high
rates through \(9/10\), the last carrier, and both complete selected
Fourier upper alternatives. Its own-four upper index height is two.
It bounds the literal product for every \(0\le y\le H\) and is convex
in \(y\).

Proposition 2, equation (34), of the
[zero-height face](research_mixed_selected_four_four_zero_height_face.md)
pays precisely each of these raw profile products at \(y=0\),
with gap \(1/1000\). At \(y=H\), equations (27), (33)--(37) of the
[complete selected first44 source](research_mixed_selected_four_four_early_complete_source.md)
pay the same profile products with gap \(1/2000\). In particular its
high-row argument is the continuous all-angle half-row comparison
before finite summation, so it controls the raw high supremum in
the convex envelope. Its ordinary zero-mode joins and all four
vertical alias halves are separately retained. Thus
\[
 \mathcal E_1(0,b)\le\Lambda_{12}(x_2)-1/1000,\qquad
 \mathcal E_1(H,b)\le\Lambda_{12}(x_2)-1/2000.
\]
Convexity gives (14) on the entire positive vertical segment, with
\(\delta=1/2000\). This uses one selected monomial at both endpoints;
it is not interpolation between different Fourier choices or an
assumption of convexity of the finite modulus.

All source estimates in this section are valid on the actual
length-\(m\ge3\) reference family, including the attached next-input
case at length three. Every complete cap and ordinary physical row,
both parity stops, original alias and Fourier forcing is already
inside those estimates. Their all-real ordinary-color bounds permit
the common fixed disks; no estimate is continued from a single
ordinary-color value.

## 3. Restoring the remaining factors and their weights

For later coordinates (7), define the nonnegative common loss
\[
 \mathcal Q_{\rm rem}(\mathbf x)
  =\kappa_0(x_2-a_2)^2
                  +2\kappa_0\sum_{j=3}^{h}(x_j-a_j)^2.
\tag{15}
\]
The sum is empty when \(m=3\). For each of the added path pieces in
Section 2, multiplying (14) by the remaining complete unselected
supporting planes gives
\[
 |\mathscr J_{\sigma,N}|
 \le C_{m,\tau}N^{A_{m,\tau}}
   e^{N\{M_{\rm open}-\delta-\mathcal Q_{\rm rem}(\mathbf x)+\tau\}}.
\tag{16}
\]

To check the exact allocation, (12) consumes \(d_N(X_1)X_1^{-N\sigma}\)
in full and one modulus half of \(d_N(X_2)\). The remaining factors
are
\[
 \prod_{j=3}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)\,
 \mathcal V_{\epsilon_m,N}(w_R,X_h)
\]
with their original unselected halfweights. The other half at
coordinate two belongs to factor three if it exists, and directly
to the terminal transform if \(h=2\). All later halves multiply to
their original integer powers in (4), also at zeros. No finite
Fourier factor is divided out, and no holomorphic square root is
chosen.

The ordinary bounds are Theorem 1 of the
[complete ordinary source assembly](research_mixed_three_row_source_assembly.md);
the terminal bound is the terminal entry of equation (5) in the
[whole unselected plateau theorem](research_mixed_full_unselected_plateau.md).
Every target required for these remaining factors is in \(P\) at
its unchanged reference height. Their constant terms and \(M_{12}\)
sum to \(M_{\rm open}\). The first uncancelled marginal is cancelled
by the original stationary equation
\[
 p_R+\partial_1\phi_3(r_2,r_3)=0\quad(h\ge3),\qquad
 p_R+\Pi'(r_2)=0\quad(h=2).
\tag{17}
\]
All later marginals cancel in the same way by (9).

There is one remaining incidence at coordinate two after the pair,
giving its one quadratic term in (15). Every coordinate \(j\ge3\)
has two remaining incidences and receives the stated two terms.
At length three, the single terminal incidence at coordinate two
gives both the other halfweight and that one quadratic term; no
extra ordinary factor is inserted. Any extra outgoing quadratic
already supplied by a pair input is favorable and may be retained
or dropped. This proves (16), after choosing the finitely many
source allowances inside one prescribed \(\tau\).

The color disks can be intersected since the word is fixed.
Derivative bounds apply to the complete holomorphic product by
Cauchy's formula on smaller disks; no modulus halfweight is
differentiated. The terminal contraction and all bounds include
both level parities.

## 4. An additive identity for the six extra pieces

Let
\[
\begin{gathered}
 R=[0,1/10],\qquad
 V_\sigma=[\,1/10,\ 1/10+iH_\sigma\,],\\
 E_0=E+ic_1,\qquad H_1^+=J+i/100,\qquad
 \mathcal P'=\prod_{j=2}^{h}(P+ic_j).
\end{gathered}
\tag{18}
\]
All segments have the orientations induced by (6). Decomposing
those paths and splitting the unselected horizontal interval at
\(11/50+ic_1\) gives the exact finite identity
\[
\begin{split}
 S_N^{-1}(\mathcal L_N-\mathcal Z_N^P)
 ={}&
 \int_{R\times\mathcal P'}\mathscr J_{0,N}
 +\int_{V_0\times\mathcal P'}\mathscr J_{0,N}
 +\int_{E_0\times\mathcal P'}\mathscr J_{0,N}\\
 &+\int_{R\times\mathcal P'}\mathscr J_{1,N}
 +\int_{V_1\times\mathcal P'}\mathscr J_{1,N}
 +\int_{H_1^+\times\mathcal P'}\mathscr J_{1,N}.
\end{split}
\tag{19}
\]
The product additive differential from (8) is understood in each
term. Shared endpoints have zero one-dimensional measure. The two
real-segment terms are different Fourier summands even though their
selected monomial has unit modulus there; neither has been replaced
by twice the other.

Each of the six terms in (19) is controlled by (16), with
\(\delta\ge\gamma_{44}\) by (3). All domains have fixed finite
length and volume. Their integral bounds retain the same exponential
gap, while the exact scalar (5) contributes only its original
polynomial power. This proves (10).

Equation (19) is additivity of the specified restricted currents.
It does not deform an unestimated contour segment or identify an
omitted region with zero. Each original finite summand is Laurent
polynomial in the retained variables, so the paths themselves
introduce no new source singularity, including at \(X_1=1\).
The estimates, rather than an unproved homology cancellation,
are what make the six added terms small.

## 5. Preservation of the original nonzero coefficient

Theorem 2 of the whole unselected plateau theorem supplies
\[
 \mathcal Z_N^P(\mathbf w)
 =\kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
          e^{N\mathcal F_m(\mathbf w)}
                   \{1+O_{\rm hol}(N^{-1})\}.
\tag{20}
\]
The amplitude is its original accretive Gaussian coefficient,
\[
 A_m(-2,-2)
   =\frac{(2\pi)^{h/2}b(\mathbf r)}
             {\sqrt{\det[-\Phi''(\mathbf r)]}}\ne0,
\tag{21}
\]
where \(b(\mathbf r)\) is the product of its original cap, ordinary,
terminal and Fourier leading symbols. No inner Gaussian or
terminal scalar is inserted again. The original source calibration
fixes \(\mathcal F_m(-2,-2)=\Phi(\mathbf r)\), including its
additive constant and logarithmic lift.

Choose the total allowance in (10) smaller than \(\gamma_{44}/8\).
Then shrink the common ordinary-color disks so that
\(\Re\mathcal F_m>M_{\rm open}-\gamma_{44}/8\) and \(A_m\)
is bounded away from zero. Equation (10) divided by the leading
term of (20) is an exponentially small holomorphic function, with
its polynomial prefactor absorbed for sufficiently large \(N\).
Cauchy's formula gives the same assertion for every fixed
normalized ordinary-color derivative on smaller disks. Adding it
to (20) proves (11). The power \(N^{-3/2}\), coefficient, phase
and its original geometric marking therefore remain unchanged.

The result is specific to the two paths (6) with every later
retained coordinate unselected on (7). The right first-coordinate
connections from \(9/20+iH_\sigma\) and the remaining part of each
period have not been estimated here. Nor have sectors with later
retained selections or departures from \(P\) been included by this
assembly. The already contracted terminal is complete; that fact
does not complete the remaining retained periods. No whole-word,
ordinary-closure, knot or finite-exception conclusion follows
from this partial-path theorem alone.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_reversed_cap_assembly.md | 79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c |
| research_mixed_four_four_real_first_endpoint.md | 4ceec7f835d08ef971b3b3ccadcf7eecd74e48db3d422cbd09e5611c0572c122 |
| research_mixed_first_four_four_negative_height_face.md | f50598305505a5dde4537fc15d6ed114b8e3a01eb87d69cff5ac36e0829b40a3 |
| research_mixed_first_positive_join_convex_envelope.md | b1f18bb5a79ff958654190c960c933ac7839f1da3fc86635f6222a1ea58cb774 |
| research_mixed_selected_four_four_zero_height_face.md | fe99fcefe1618991471f083febcf4c6043418a4387d76be1ae2015542734810f |
| research_mixed_selected_four_four_early_complete_source.md | 760ab93cc36ccba00eea97c518eb3697f55638b90c43c90d5ce1a9cd029ddc05 |
| research_mixed_selected_early_boundary_assembly.md | 0643c85c8b30bbf5a927551470538e024ae3b8b1ec0be7ec20e845708f6bef73 |
| research_mixed_initial44_early_boundary_assembly.md | 8ed393fd2e465d5399c8ffddc46c2d603ef4c5cb6d154ee561e676aa8bfd2c90 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |

The full written proof and directly used source implications were read.
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was performed.

