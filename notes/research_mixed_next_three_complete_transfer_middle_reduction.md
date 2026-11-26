# The complete next transfer and its remaining physical middle sum

Private finite-source assembly, 8 November 2026. All component
source theorems, including the complete physical-half-band
application, have completed their source and proof reviews.

The original two-sector transfer is the nonzero local geometric
integral plus one explicit coherent finite sum and an exponentially
smaller error. All contour pieces have been estimated with their
original orientations. The remaining sum retains its physical
index phases and its full unresolved outgoing rows; no bound or
noncancellation statement for that sum is made.

No mathematical numerical evaluation, saved-value calculation,
or modification of a frozen proof is used.

## 1. Actual base reference, transfer and normalization

Fix an actual complete word in the original powers three and four,
beginning \(343\), of length \(m\ge5\). Use its original coupled
reference
\[
 (a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),\qquad
 c=\Im y_*,\qquad H=1/100,\qquad Z_*=e^{-2\pi iz_*}.
 \tag{1}
\]
This note concerns the base outside parameters \(w=-2,z=z_*\).
The actual geometry gives
\[
 7/10<e^{2\pi c}<41/50,\qquad
 3/10<\Re z_*<39/100,\qquad 4/5<|Z_*|<8/7 .
 \tag{2}
\]
Every other reference coordinate and every height remains fixed
and correlated as in the source theorems. In particular both
conditional vertices in the following source are ordinary.
Length-four words, terminal \(343\), and next own type four are
outside the assertion.

Put
\[
 \begin{gathered}
 D=N-1,\quad r=e^{-2\pi i/N},\quad q_N=e^{\pi i/N},
 \quad \kappa_N=q_N^{D^2/2},\\
 P_j=(r;r)_j,\qquad p_j(V)=(rV;r)_j,\\
 C_{0,N}(Y,Z)=\sum_{k=0}^{D}
           \frac{Y^{-k}p_k(Y)p_k(Z)}{P_k^2}.
 \end{gathered}
 \tag{3}
\]
The symbol \(q_N\) is the quantum parameter, not a real contour
coordinate. Retain the complete original prefix
\[
 F_N(w,Y)=F_{34,N}(w,Y)
   =N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)]
 \tag{4}
\]
and the full forced polynomial \(d_N\), of degree at most \(D\),
with \(d_N(r^b)=P_b^{-1}\).

The Laurent powers of \(F_Nd_NC_{0,N}\) lie in \([-D,2D]\).
The original observation is therefore exactly
\[
 \mathcal T_0[F_N](w,Z)
   =N[Y^0](F_N(w,Y)d_N(Y)C_{0,N}(Y,Z))
    +N[Y^N](F_N(w,Y)d_N(Y)C_{0,N}(Y,Z)).
 \tag{5}
\]
Both Fourier sectors occur with their original coefficient \(+N\).
This is the original conditional-message normalization. In
particular no extra \(N\), outgoing halfweight, or final Gram
factor is inserted in (5).

Write
\[
 \mathcal P_*=\mathcal P_0^+(-2,z_*),\qquad
 \mathcal M_*=\Re\mathcal P_*
             =\Lambda_{123}(z_*).
 \tag{6}
\]
The strengthened ordinary-three action floor is
\[
 \mathcal M_*>419/200 ,
 \tag{7}
\]
by [the original pair-action theorem, equation (13)](research_mixed_next_three_real_pair_action_floor.md).
It applies to the actual coupled reference (1); it is not a
lower bound for the complete finite quantum sum.

Let \(I_{{\rm geom},N}\) be the unchanged local geometric integral
from [the actual lower-half assembly, equations (18)--(23)](research_mixed_next_three_actual_complete_lower_left.md).
It has
\[
 I_{{\rm geom},N}
   =N^{-2}\mathcal A_0(-2,z_*)e^{N\mathcal P_*}
       (1+O(N^{-1})),\qquad \mathcal A_0(-2,z_*)\ne0 .
 \tag{8}
\]
The integral itself is retained in the identities below. Its
algebraic asymptotic error in (8) is not moved into an
exponentially small remainder.

## 2. The full remaining physical sum

Keep the old fixed filter cutoff \(0<\delta_{\rm old}<1/40\) and
\[
 l_N=\lfloor\delta_{\rm old}N\rfloor,\quad
 A_N=\lceil23N/24\rceil,\quad B_N=\lceil11N/12\rceil,\quad
 M_N=\lceil N/2\rceil,\quad Q_N=\lceil5N/6\rceil .
 \tag{9}
\]
The letters \(A_N,B_N\) here are the original integer cutoffs.
They are unrelated to the coefficient \(\mathcal A_0\) in (8).

The new physical half-band has a different fixed width.
Following [physical continuation from the complete vertical, equations (10),(12),(16)](research_mixed_next_three_physical_half_band_from_vertical.md),
set
\[
 \begin{gathered}
 \gamma=10^{-13},\qquad
 \varrho=e^{\gamma/12},\qquad
 d_\varrho=\frac{(\varrho+\varrho^{-1})/2-1}{20},\\
 \delta_{\rm ph}=\min\{1/100,d_\varrho/(8\pi)\}>0,\qquad
 b_N^{\rm rem}=\lfloor N(1/2+\delta_{\rm ph})\rfloor+1,\qquad
 k_N^{\rm low}=\lfloor N/4096\rfloor .
 \end{gathered}
 \tag{10}
\]
This width is not a modification of the old cardinal filter.
It only partitions its already retained physical summands.
It is independent of \(N\), and no numerical size is assigned to it.

Use the original coherent coefficients \(\ell_b(w)\), defined
by the exact lowered-word identity
\[
 \frac{F_N(w,r^b)}{P_b}
       =\frac{(-q_N)^b}{\kappa_N^2N}\ell_b(w).
 \tag{11}
\]
Equivalently \(\ell_b(w)=(v(w)^TA_3^2)_b\) in the original
ordinary Newton basis. This is the full coefficient; none of
its internal signed sums is replaced by an absolute majorant.

Define the single unresolved source
\[
 \boxed{\quad
 \begin{split}
 \mathscr S_N^{\rm rem}
 =\frac1{\kappa_N^2N}
  \sum_{b=b_N^{\rm rem}}^{Q_N-1}
     (-q_N)^b\ell_b(-2)
     \sum_{k=k_N^{\rm low}+1}^{D-b}
       \frac{r^{-bk}p_k(r^b)p_k(Z_*)}{P_k^2}.
 \end{split}
 \quad}
 \tag{12}
\]
Empty ranges have value zero. At every retained physical node
\(r^b\), the exact next-kernel termination is \(k\le D-b\).
In particular (12) retains every surviving row above its displayed
lower cutoff, all outgoing numerator zeros, and every original
carrier and root-of-unity phase.

**Theorem.** There is a fixed positive number \(\epsilon\),
specified in Section 6 from the adopted source gaps, such that,
at all sufficiently large levels of either parity,
\[
 \boxed{\qquad
 \mathcal T_0[F_N](-2,Z_*)
     =I_{{\rm geom},N}+\mathscr S_N^{\rm rem}
            +O(e^{N(\mathcal M_*-\epsilon)}).
 \qquad}
 \tag{13}
\]
The original action and scalar normalizations in (5),(8),(11)
are unchanged. The statement is at the actual base reference.
No new outside-parameter jets are inferred from the pointwise
vertical or physical-half-band bounds. In particular (13)
does not say that \(\mathscr S_N^{\rm rem}\) is small.

## 3. Completing the signed contour reduction

Retain the unchanged filtered polynomial
\[
 F_N^{\rm mid}=(I-\Pi_{\rm end})(F_N-R_N^a),\qquad
 E_N^{\rm filt}=F_N-F_N^{\rm mid},\qquad
 K_N(y)=\frac{N F_N^{\rm mid}(-2,Y)d_N(Y)C_{0,N}(Y,Z_*)}{1-Y^N},
 \quad Y=e^{-2\pi iy}.
 \tag{14}
\]
The old filter satisfies
\(F_N^{\rm mid}(-2,r^b)=0\) for \(b\le l_N\) or \(b\ge B_N\).
The complete first-coordinate deletion \(R_N^a\), its cutoff
\(A_N\), and the entire forced \(d_N\) remain in this identity.

Let the fixed \(s\in(0,11/100)\) be exactly the seam-arc cutoff
of [the original top seam removal](research_mixed_next_top_seam_arc_removal.md).
Do not change it to either width in (9)--(10). The actual
lower-half assembly, equations (20)--(23), gives
\[
 \mathcal T_0[F_N](-2,Z_*)=I_{{\rm geom},N}
             +\mathscr R_N^{(3)}+\mathscr E_N^{\rm old},
 \qquad
 e^{-N\mathcal P_*}\mathscr E_N^{\rm old}
                         =O(e^{-\eta_{\rm actual}N}),
 \tag{15}
\]
where its positive \(\eta_{\rm actual}\) is unchanged, and
\[
 \mathscr R_N^{(3)}
 =\int_{[1/2,1]+ic}K_N
  -\int_{[s,11/50]+iH}K_N
  -\int_{[9/20,1-s]+iH}K_N .
 \tag{16}
\]
Every interval integral in this note is oriented toward increasing
real part unless an explicit minus sign is written. The entire
old-filter transfer error is already included in
\(\mathscr E_N^{\rm old}\). It is not decomposed into estimates
for individual Fourier sectors or outgoing rows.

Define
\[
 \begin{split}
 U_N^{\rm left}&=\int_{[s,11/50]+iH}K_N,\qquad
 U_N^{\rm near}=\int_{[9/20,1/2]+iH}K_N,\\
 U_N^{\rm seam}&=\int_{[1-s,1]+iH}K_N,\\
 \mathscr H_N(1/2)&=\int_{[1/2,1]+ic}K_N
                         -\int_{[1/2,1]+iH}K_N .
 \end{split}
 \tag{17}
\]
Since \(1-s>1/2\), exact splitting, with no deformation, gives
\[
 \mathscr R_N^{(3)}
   =\mathscr H_N(1/2)-U_N^{\rm left}
                       -U_N^{\rm near}+U_N^{\rm seam}.
 \tag{18}
\]
In particular the restored right seam arc has a plus sign.
The following complete source bounds apply at (1):

| Term | Adopted normalized exponential gap | Source |
| --- | --- | --- |
| \(U_N^{\rm left}\) | \(1/10000\), before polynomial absorption | [Complete selected-left source](research_mixed_next_three_selected_left_complete_source.md) |
| \(U_N^{\rm near}\) | \(1/20000\), before polynomial absorption | [Complete half-grid/near-half assembly](research_mixed_next_three_half_grid_and_near_half_complete_source.md) |
| \(U_N^{\rm seam}\) | \(1/2000\) | [Top seam-arc removal, Section 2](research_mixed_next_top_seam_arc_removal.md) |

The last source supplies a pointwise selected bound on each arc
before integration. Thus its individual right arc is eligible;
this is not an estimate extracted from the modulus of the signed
sum of the two seam arcs. The exact top denominator and its
minus sign were retained in all three sources.

Put \(L_N=(M_N-\tfrac12)/N\), and define
\[
 \begin{split}
 V_N(L_N)&=i\int_c^H K_N(L_N+ih)\,dh,\qquad
 V_N(1)=i\int_c^H K_N(1+ih)\,dh,\\
 J_N^{\rm grid}&=
       \int_{[L_N,1/2]+ic}K_N
           -\int_{[L_N,1/2]+iH}K_N,\\
 \mathscr R_N^{\rm cl}&=
       \int_{\partial([L_N,1]+i[c,H])}^{\rm CCW}K_N(y)\,dy .
 \end{split}
 \tag{19}
\]
The exact right-rectangle identity is
\[
 \mathscr H_N(1/2)
   =\mathscr R_N^{\rm cl}-V_N(1)+V_N(L_N)-J_N^{\rm grid}.
 \tag{20}
\]
The full periodic-side theorem
[through the deep radial seam, equation (18)](research_mixed_next_three_actual_deep_radial_seam.md)
gives normalized gap \(10^{-16}\) for \(V_N(1)\), including
its removable seam value. The full half-grid assembly gives
gap \(\gamma=10^{-13}\), before polynomial absorption, for
\(V_N(L_N)\) and each grid horizontal separately. At odd
levels the latter are zero; at even levels they retain their
opposite signs and their actual half-grid displacements.
No small-length or deleted-node inference is used.

Consequently (15),(18),(20) are an exact identity with all of
\[
 \mathscr E_N^{\rm old}
 -U_N^{\rm left}-U_N^{\rm near}+U_N^{\rm seam}
 -V_N(1)+V_N(L_N)-J_N^{\rm grid}
 \tag{21}
\]
exponentially smaller than the original action. This reduces
the remaining source to \(\mathscr R_N^{\rm cl}\).

## 4. The old filtered residues and the unfiltered coefficient

The exact residue formula, including the \(+N\) already in
\(K_N\), is
\[
 \mathscr R_N^{\rm cl}
   =\sum_{b=M_N}^{B_N-1}
       \frac{F_N^{\rm mid}(-2,r^b)}{P_b}\,
                              C_{0,N}(r^b,Z_*).
 \tag{22}
\]
There is no additional \(N\) outside this sum.
At these retained nodes the old cardinal projection is zero,
so \(F_N^{\rm mid}=F_N-R_N^a\) at the node. Therefore
\[
 \begin{split}
 \mathscr R_N^{\rm cl}
   &=\mathscr S_N^{\rm all}-\mathcal D_N^{a,\rm rt},\\
 \mathscr S_N^{\rm all}
   &=\frac1{\kappa_N^2N}
       \sum_{b=M_N}^{B_N-1}(-q_N)^b
                              \ell_b(-2)C_{0,N}(r^b,Z_*),\\
 \mathcal D_N^{a,\rm rt}
   &=\sum_{b=M_N}^{B_N-1}
       \frac{R_N^a(-2,r^b)}{P_b}C_{0,N}(r^b,Z_*).
 \end{split}
 \tag{23}
\]
This is [the right paired theorem, equations (17),(21)--(22)](research_mixed_next_right_paired_terminal_insertion.md),
not a new filter. The partial deletion in (23) is the exact
correction required to rewrite the retained filtered node values
as unfiltered coefficients. It is not a second subtraction of
the full transfer correction in (15).

The original positive first-end rectangle bound gives
\[
 |\mathcal D_N^{a,\rm rt}|\le C N^A e^{11N/6}
 \quad\text{for}\quad |Z_*|\le e^{3\pi/20}.
 \tag{24}
\]
It is eligible on every physical subset and retains all outgoing
rows, unlike a bound for a signed total. Its disk contains (2):
\(e^{3\pi/20}>1+9/20>8/7\).
The original normalized comparison has gap \(1/96\).
Alternatively (7) gives the explicit reserve
\[
                  419/200-11/6=157/600>1/96 .
 \tag{25}
\]
Thus (24) is paid with the same original action and no alteration
of an outgoing scalar. No part of this complete correction is
split according to the outgoing index below.

## 5. A disjoint partition of the unfiltered physical sum

For sufficiently large \(N\), partition the retained \(b\)-range
in (23) into
\[
 \begin{split}
 \mathcal B_N^{\rm half}&=\{M_N,\ldots,b_N^{\rm rem}-1\},\\
 \mathcal B_N^{\rm mid}&=\{b_N^{\rm rem},\ldots,Q_N-1\},\\
 \mathcal B_N^{\rm high}&=\{Q_N,\ldots,B_N-1\}.
 \end{split}
 \tag{26}
\]
These sets are pairwise disjoint. Their union is precisely the
old retained range \(\{M_N,\ldots,B_N-1\}\). The inequalities
\(\delta_{\rm ph}\le1/100\) and \(5/6<11/12\) ensure the order
of their endpoints for all sufficiently large levels; the
ceilings and floors in (9)--(10) are not replaced by real
index approximations.

The physical-half-band theorem applies to the full unfiltered
prefix \(G_N=F_N\), with its next factor already attached:
\[
 \sum_{b\in\mathcal B_N^{\rm half}}
 \left|\frac{F_N(-2,r^b)}{P_b}C_{0,N}(r^b,Z_*)\right|
     \le C N^A e^{N(\mathcal M_*-\gamma/2)} .
 \tag{27}
\]
Its full-source hypothesis is equation (10a), or the equivalent
half-grid kernel bound, of the complete vertical assembly.
This removes all outgoing indices at those \(b\)-nodes together.

The [complete high-band theorem](research_mixed_next_right_insertion_actual_high_band.md),
equations (18)--(19), applies to
\(\mathcal B_N^{\rm high}\). It gives normalized gap \(1/200\)
for their entire contribution. Its source budget is
\[
 \frac{1499}{720}+\tau,\qquad
 \frac{419}{200}-\frac{1499}{720}=\frac{47}{3600}>\frac1{100},
 \tag{28}
\]
with all finite tolerances chosen inside the reserve.
This theorem includes every surviving outgoing row and the
original radical/terminal normalization. Its uniform disk
\(|Z|\le8/7\) contains (2).

Only for \(b\in\mathcal B_N^{\rm mid}\), now split the literal
terminating next kernel as
\[
 \begin{split}
 C_{0,N}(r^b,Z_*)&=C_{0,N}^{\rm low}(r^b,Z_*)
                         +C_{0,N}^{\rm rem}(r^b,Z_*),\\
 C_{0,N}^{\rm low}(r^b,Z_*)&=
 \sum_{k=0}^{\min(D-b,k_N^{\rm low})}
       \frac{r^{-bk}p_k(r^b)p_k(Z_*)}{P_k^2},\\
 C_{0,N}^{\rm rem}(r^b,Z_*)&=
 \sum_{k=k_N^{\rm low}+1}^{D-b}
       \frac{r^{-bk}p_k(r^b)p_k(Z_*)}{P_k^2}.
 \end{split}
 \tag{29}
\]
The [complete small-outgoing-index theorem](research_mixed_next_three_small_outgoing_indices.md)
applies to any subset of upper physical nodes, hence specifically
to \(\mathcal B_N^{\rm mid}\). It bounds the low part of (29),
with its coherent \(\ell_b(-2)\) and original
\((\kappa_N^2N)^{-1}(-q_N)^b\), at rate
\[
                419/200-3/1000<\mathcal M_*-3/1000 .
 \tag{30}
\]
No part of (29) is also removed in (27) or (28), because its
\(b\)-range is disjoint from both. Nor is the old correction
(24) split into small and large outgoing rows.

The exact remainder after (27)--(30) is (12).
If desired, its first coefficient can be written without
discarding its internal phases as
\[
 \begin{split}
 \ell_b(-2)&=\sum_{j=0}^{D-b}
       b_{D-b,j}\,\mathcal R_N(c_j)^3\,
                             \mathcal K_{3,N}(-2,c_j),\\
 b_{n,j}&=(-1)^{n+j}
       \frac{2\sin((2j+1)\pi/N)S_n^2}{S_{n-j}S_{n+j+1}},
 \quad c_j=2\cos((2j+1)\pi/N),\quad S_j=|P_j|,\\
 \mathcal R_N(c_j)&=\kappa_N(-1)^j q_N^{j(j+1)} .
 \end{split}
 \tag{31}
\]
The original repeated-root normal and ordinary boundary
observation are those in the exact high-Newton contraction.
Equation (31) is not estimated termwise in this reduction.

## 6. The final error and its exact limitation

Let \(\eta_{\rm actual}>0\) be the adopted number in equation
(21) of the actual lower-half assembly, as used in (15).
One explicit conservative choice is
\[
 \epsilon=\frac14\min\left\{
 \eta_{\rm actual},\ 10^{-16},\ \gamma,\
 \frac1{20000},\ \frac1{2000},\
 \frac1{96},\ \frac1{200},\ \frac{\gamma}{2},\
 \frac3{1000}\right\}>0 .
 \tag{32}
\]
The \(1/10000\) left-top gap exceeds the included
\(1/20000\). Every fixed polynomial prefactor in the finite
source bounds is absorbed within the remaining factor-four
reserve for sufficiently large \(N\). No lower bound on
the difference \(\mathcal M_*-419/200\) is spent: the stated
strict floor (7) already gives all the weaker gaps used here.

Combine (15),(18),(20),(23) and the disjoint partition
(26)--(29). Before estimation,
\(\mathcal T_0[F_N](-2,Z_*)-I_{{\rm geom},N}-\mathscr S_N^{\rm rem}\)
is exactly (21), minus the complete deletion
\(\mathcal D_N^{a,\rm rt}\), plus the physical half-band, the
high band, and the small-\(k\) contribution on
\(\mathcal B_N^{\rm mid}\). All these terms have the stated
bounds. This proves (13).

The scope of the reduction is therefore precise. The nonzero
local geometric integral has survived as an identified term,
and all other contributions except the explicit coherent sum
(12) have been bounded. Equation (13) does not prevent
that remaining sum from canceling the geometric term, or
from having the same exponential rate. It does not identify
either individual Fourier coefficient in (5) with the
geometric integral. No full next-transfer asymptotic, new
knot-family volume identity, or arbitrary-short composition
closure follows without a further comparison for (12).
