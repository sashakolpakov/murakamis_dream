# Nonplateau middle sectors between unselected plateau collars

Research deduction, 6 November 2026. Arbitrary original hybrid states
in the middle of an open word can be estimated when two sufficiently
long unselected plateau collars separate them from its physical
boundaries. The collars absorb the relative pinning fees. This gives
a new nonplateau sector estimate using complete finite factors, not
an estimate of the absolute physical-index contraction. It does not
bound configurations whose defects enter either boundary collar.

No reference, primitive, optimizer, finite-level source or numerical
certificate is evaluated here.

## 1. Contract the terminal variable before taking absolute values

Fix an original mixed positive word of length \(m\), put
\(h=m-1\), and retain its actual open critical reference
\(r_j=a_j+ic_j\). Start with the exact
[reversed-cap contraction](research_mixed_reversed_cap_assembly.md).
For a retained selection \(\sigma\), its literal integrand is
\[
 \begin{split}
 \mathscr J_{\sigma,N}={}&U_{\epsilon_1,N}(w_L,X_1)
   \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
   \mathcal V_{\epsilon_m,N}(w_R,X_h)
   \prod_{j=1}^{h}D_j,\\
 D_j={}&d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j},\qquad
 X_j=e^{-2\pi iz_j}.
 \end{split}
\tag{1}
\]
Selections are permitted only at type-four retained positions.
The original scalar is
\(\kappa_N^{m+k_4}N^{m+k_4-1}\). The finite terminal sum,
including its own selected alternative, is already inside
\(\mathcal V\); it is not selected a second time in (1).

This exact contraction is essential. The terminal theorem bounds
\(\mathcal V\), not the modulus of the uncontracted product
\(C_mH_N\) before its last variable is summed. Thus the argument
below is applied to (1), rather than inserting that theorem into
the uncontracted right modulus of
[the earlier boundary reduction](research_mixed_open_boundary_comparison_reduction.md).

Use the same row-dependent periodic
[hybrid graph](research_mixed_split_cutoff_hybrid_contour.md) on the
retained variables. Its base selected height is \(7/500\).
An optional last retained selection instead has base height
\(1/100\). Missing neighbors have cutoff one. The source in (1)
is Laurent polynomial in its nonzero retained variables, so this
row-dependent choice is still an exact periodic graph deformation
of its complete constant term. On all plateau collars considered
below, every cutoff is one. The terminal-variable contraction and
this retained-variable deformation therefore do not change any
coefficient or ordinary color.

Set \(P=[.22,.45]\). Choose ordinary cuts \(p,\ldots,q\)
so that \(I=[p-2,q+1]\), together with the eight-vertex halo
required by the open-window theorem, is safe. Both cuts are far
from the endpoint factors. The original bulk weights \(w_j\),
their six closing terms \(A_p,E_q\), and compact residual
\(D_I\) are exactly those in
[the open boundary reduction](research_mixed_open_boundary_comparison_reduction.md)
and [the occupation theorem](research_mixed_full_period_occupation.md).
In particular
\[
 D_I\ge\kappa\sum_{j\in I}p_j,\qquad
 \kappa=\frac1{20000},\qquad
 p_j=\min\{1,\sigma_j+400(\operatorname{clamp}_P x_j-a_j)^2\}.
\tag{2}
\]
The reference remains the actual open reference. It is not replaced
by a periodic solution.

## 2. The specified sectors and fixed collar length

Take two disjoint blocks \(G_L,G_R\subset I\), in that order,
each containing \(2d+7\) consecutive symbols. Protect the first
and last three symbols of \(I\), as in Section 4 of
[finite boundary windows](research_mixed_open_finite_boundary_windows.md):
neither block meets these protected triples. Let \(J\) be the
interval strictly between the two blocks. Impose the following
conditions on a sector:

* Every retained coordinate outside \(J\) belongs to \(P\).
* Every retained coordinate outside \(J\) is unselected, except
  possibly the last retained coordinate \(h\).
* In \(J\), real coordinates may occupy the entire original
  period and every type-compatible retained selection is allowed.

Thus the two blocks are unselected plateau blocks, and so are the
physical regions between them and the respective endpoints.
All low, seam, transition, right and selected states in \(J\)
use their original hybrid heights and full upper profiles. No reset
cost is omitted or assigned to the terminal gap.

Write \(\tau=\sigma_h\). If \(\tau=1\), impose the already
completed terminal hypotheses: the last three types are
\((4,4,3+\epsilon_m)\), the incoming retained coordinate is
unselected, and its actual reference belongs to \(K_4\).
Then \(z_h\) has height \(1/100\), and the terminal pair has
raw gap
\[
                         \delta_T=\frac1{2600}.
\tag{3}
\]
For \(\tau=0\), either terminal type and either incoming type
are allowed under the completed unselected plateau theorem.

One explicit collar choice is
\[
 d=352,\quad |G_L|=|G_R|=711,\quad
 q_0=\frac{99}{101},\quad a_d=1000q_0^{2d},\quad
 \kappa_* =\frac1{2500000}.
\tag{4}
\]
The exact rational comparisons in equation (11) and Section 6 of
the finite-boundary theorem give
\[
 \frac95q_0^{352}<\frac1{20},\qquad
 a_{352}<\frac1{1296}<\frac1{20}.
\tag{5}
\]
The inner occupation fee obeys the already proved bound
\[
 c_d:=\frac{81}{2500}a_d<\frac{\kappa}{2}.
\tag{6}
\]
Thus optimizer inactivity and the inner relative-fee condition hold.
Section 4 uses an exact coherent extension edge to pay each outer
fee; it does not require \(a_d<\kappa_*\), which is false for
this choice. No finite-factor curvature is strengthened. The claim concerns words
and chosen cuts for which these two safe blocks exist; it makes no
claim about shorter words by omission.

## 3. Literal boundary closure after the contraction

Split (1) into the allocated ordinary middle and the two moduli
\[
 \begin{split}
 L_N={}&|U_{\epsilon_1,N}|\prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|D_j|\ |D_{p-1}|^{1/2},\\
 R_N={}&|\mathcal V_{\epsilon_m,N}|\prod_{j=q+1}^{h}|C_{\epsilon_j,N}|
       |D_q|^{1/2}\prod_{j=q+1}^{h}|D_j|.
 \end{split}
\tag{7}
\]
These are exact modulus allocations. Each middle edge uses its
original two halfweights. No Fourier factor is divided out, including
at its zeros. The first cap and the terminal transform retain their
entire ordinary-color polynomials.

Let \(M_L,M_R\) be the reference actions of these allocated
products and define
\[
 \begin{split}
 B_{L,N}&=N^{-1}\log L_N-M_L
       +\Re[P_{p,a}(z_{p-1}-r_{p-1})]-A_p,\\
 B_{R,N}&=N^{-1}\log R_N-M_R
       +\Re[P_{q,b}(z_q-r_q)]-E_q.
 \end{split}
\tag{8}
\]
Use \(\log0=-\infty\). The same six-edge identity as before
gives, for any prescribed total finite-source tolerance \(\eta>0\),
\[
 N^{-1}\log|\mathscr J_{\sigma,N}|-M_{\rm open}
 \le B_{L,N}+B_{R,N}-D_I+\eta+O_m(\log N/N).
\tag{9}
\]
Only the literal right boundary product has been regrouped; no bulk
weight, closing term or reference marginal changes. Original internal
stationarity cancels the complex affine terms. The finite bound
includes all bulk aliases and rows through the same complete
occupation/source assembly used in the boundary reduction.

Apply relative triple pinning inside both good blocks. Denote their
outer Dirichlet endpoints by \(u_L,v_R\). All physical boundary
products and the protected closing terms stay fixed. The pinned
residual splits exactly into \(D_L+D_M+D_R\), because three
baseline symbols separate the supports of four-symbol weights.
The two inner fees are paid by (2) and (6). Hence
\[
 \begin{split}
 B_{L,N}+B_{R,N}-D_I
 \le{}&[B_{L,N}-D_L+a_d(u_L-a_{u_L})^2]\\
     &+[B_{R,N}-D_R+a_d(v_R-a_{v_R})^2]
        -\frac\kappa2\sum_{j\in M}p_j^{\rm pin}.
 \end{split}
\tag{10}
\]
This is precisely the proved relative pinning inequality, now for
the contracted boundary moduli (7). Pinning moves only symbols in
the two good blocks. Every symbol in \(J\) is unchanged.

## 4. The outer fees are absorbed by complete source bounds

After pinning, every symbol of either outer component is on its
unselected plateau, except the permitted last selection. The
quadratic supporting planes in equation (5) of
[the whole unselected plateau theorem](research_mixed_full_unselected_plateau.md)
apply to its complete finite cap, ordinary and terminal factors,
with coefficient \(\kappa_*\). On safe coherent plateau edges
the stronger original phase inequality holds, so the same smaller
coefficient may be retained there as well.

The outer fees are paid by coherent synthetic edges, not the
finite factors in (7). To see their exact placement, write
\(G_L=\{g_L,\ldots,g_L+2d+6\}\). Its outer endpoint is
\(u_L=x_{g_L+1}\). The protected first triple gives
\(g_L\ge p+1\), so the edge
\(j=g_L+2\), joining block positions 1 and 2, lies beyond the
literal prefix edges \(j\le p-1\) and before the first pin.
It belongs to the coherent extension in \(D_L\). On the right,
\(v_R=x_{g_R+2d+5}\), and the edge
\(j=g_R+2d+5\) joins block positions \(2d+4,2d+5\).
Since the last protected triple forces the block end to be at most
\(q-2\), this edge has \(j\le q-3\). It lies after the last
pin and before the literal suffix edges \(j\ge q+1\).

Each of these edges and its four-symbol stencil is unselected
plateau, at the original fixed heights. Its original weight is
exactly \(w_j=\Re(\phi_j-\Gamma_j)\). In the identity for
\(B_{L,N}-D_L\), the closing term cancels and the coherent
extension contributes \(\phi_j-\Gamma_j\) once; this is the
algebra of equation (16a) of the finite-boundary theorem. The
right identity is reflected. The identity holds throughout the
plateau extension, not just in a local saddle neighborhood.

For \(e_j=-\Re(\phi_j-\Gamma_j)\), the safe original phase
Hessian is at least \(I/5\); its reference value and gradient
vanish. Thus each chosen edge supplies at least \(1/10\) times
the square displacement of its fee endpoint, independently of its
other endpoint. These edges are counted once and are disjoint from
the selected terminal pair. All other nonpositive coherent costs
and complete finite-factor quadratics may be discarded. Exact
affine cancellation, including the fixed reference triple at the
inner cut, therefore gives
\[
 \begin{split}
 B_{L,N}-D_L
   &\le-\tfrac1{10}(u_L-a_{u_L})^2+\mathfrak e_{L,N},\\
 B_{R,N}-D_R
   &\le-\tau\delta_T-\tfrac1{10}(v_R-a_{v_R})^2+\mathfrak e_{R,N}.
 \end{split}
\tag{11}
\]
For any prescribed aggregate rate tolerance \(\eta>0\), choose
the finitely many factor tolerances, including those in (9), so that
their sum is at most \(\eta\). The corresponding total error
\(\mathfrak e_N\), including \(\mathfrak e_{L,N}\) and
\(\mathfrak e_{R,N}\), satisfies
\(\mathfrak e_N\le\eta+C_{\eta,m}\log N/N\).
An exact finite-level supporting-plane sign is not being asserted.

For \(\tau=1\), use the complete
[terminal kernel](research_mixed_terminal_uniform_kernel_completion.md)
on its last ordinary factor and terminal transform together. Its
sole incoming complex marginal equals the sum of those original
allocated marginals; the internal terminal marginal is zero.
Its incoming halfweight matches the adjoining ordinary factor,
and its selected last integer weight occurs once. It therefore
replaces those two factors by the same affine plane with loss
\(\delta_T\). No quadratic reserve from that pair is used to
pay a collar fee.

The bounds (11) hold uniformly for both real outside colors.
For \(\tau=0\), use the complete
[first-cap](research_mixed_endpoint_real_color_decay.md) and
[terminal](research_mixed_terminal_real_color_decay.md) real-color
planes, discarding their favorable angular losses. For \(\tau=1\),
use instead the selected
[terminal profile real-color lift](research_mixed_terminal_profile_real_color_lift.md).
They also hold on fixed sufficiently small complex color
neighborhoods of the complete colors. The intervening factors have
no ordinary-color dependence.

Combining (5), (10), and (11) proves the calibrated bound
\[
 \begin{split}
 N^{-1}\log|\mathscr J_{\sigma,N}|-M_{\rm open}
 \le{}&-\tau\delta_T-\frac\kappa2\sum_{j\in M}p_j^{\rm pin}\\
      &-\frac1{20}
       \{(u_L-a_{u_L})^2+(v_R-a_{v_R})^2\}+\mathfrak e_N.
 \end{split}
\tag{12}
\]
This is an actual boundary datum on the stated collar sector. It
does not require either separately closed boundary relaxation
\(B_{L,N}\) or \(B_{R,N}\) to be nonpositive.

## 5. New nonplateau sector consequence and its limitation

Let
\[
 b_J(\mathbf q)=\#\{j\in J:\ \sigma_j=1\ \text{or}\ x_j\notin P\}.
\tag{13}
\]
Every counted symbol survives pinning and has occupation one. Thus
(12) has raw loss at least
\[
                  \tau\delta_T+\frac{b_J(\mathbf q)}{40000}.
\tag{14}
\]
In particular, restrict to the part of the specified collar sector
where at least one middle real coordinate lies outside \(P\),
and sum over all type-compatible selections in \(J\). With
\(\tau=0\), its original normalized integral has the bound
\[
                 |E_N^{\rm collar}|\le C N^A
                     e^{N(M_{\rm open}-1/80000)}.
\tag{15}
\]
The same conclusion holds if the complement is defined instead by
\(b_J\ge1\). With the permitted \(\tau=1\), the stronger
finite loss \(1/5200\) follows, regardless of \(b_J\).
Choose all finite-source tolerances once below half of the indicated
raw reserve. The fixed graph Jacobian, integration volume, original
scalar and number of selections change only the polynomial prefactor.
The estimates hold through both parities, over the full real color
square and on small complex color neighborhoods. Fixed color jets
follow on smaller disks without differentiating modulus halfweights.

The nonplateau restriction in (15) is disjoint from every plateau
sector. By contrast, the alternative condition \(b_J\ge1\)
also includes selections with every real coordinate in \(P\).
Those may already belong to an interior-selected plateau sum; an
assembly using that alternative must subtract overlaps or use an
explicit disjoint partition.

## 6. A concrete enlarged partial-source theorem

Fix one pair of admissible collars. Define \(E_N^{(\tau)}\) by
integrating (1), with its original scalar, over precisely the region
specified in Section 2 with at least one \(x_j\), \(j\in J\),
outside \(P\), and summing over all allowed selections in \(J\).
Keep the last selection equal to \(\tau\). Thus every added region
is disjoint from the plateau, and the two values of \(\tau\)
are disjoint retained Fourier sectors.

Without the optional suffix hypothesis, set
\[
 \widehat Z_N=Z_N^{\mathrm{int}}+E_N^{(0)},
 \qquad \gamma=1/80000,
\tag{16}
\]
where \(Z_N^{\mathrm{int}}\) is the original central partial
source in
[central-region boundary colors](research_mixed_central_region_boundary_colors.md).
When the suffix hypothesis holds, one may instead take
\[
 \widehat Z_N=Z_N^{\mathrm{int,last}}+
                  \sum_{\tau\in T}E_N^{(\tau)},
 \quad \varnothing\ne T\subseteq\{0,1\},\quad
 \gamma=\min_{\tau\in T}\gamma_\tau,
 \quad \gamma_0=1/80000,\quad\gamma_1=1/5200,
\tag{17}
\]
using the exact
[last-selected plateau sum](research_mixed_last_selected_plateau_completion.md).
In both formulas the added polynomial has modulus at most
\(CN^A e^{N(M_{\rm open}-\gamma)}\), on small complex color
neighborhoods and over the full real color square.

The integration regions, graphs and selections are independent of
the colors. Hence every added term is an entire polynomial of
separate ordinary degree at most \(N-1\), and this degree bound
also holds for \(\widehat Z_N\). The old partial source has its
original action \(\mathcal W\) and nonzero amplitude \(A\).
Shrink its complex color neighborhood so that
\(\Re\mathcal W>M_{\rm open}-\gamma/2\). The added polynomial
is then exponentially smaller than the old local packet, uniformly
on that neighborhood. Consequently
\[
 \widehat Z_N(w_L,w_R)
 =\kappa_N^{m+k_4}N^{-3/2}A(w_L,w_R)
       e^{N\mathcal W(w_L,w_R)}(1+O(N^{-1})),
 \qquad A(-2,-2)\ne0,
\tag{18}
\]
with the same original normalization, branches and amplitude.
Fixed ordinary-color jets have the corresponding conclusion on
smaller neighborhoods.

For any sufficiently small fixed angular exclusion radius
\(\rho>0\), let \(\delta_\rho>0\) be the old partial source's
real outside-color gap. The triangle inequality gives gap
\(\min(\delta_\rho,\gamma)\) for \(\widehat Z_N\) when
\(\max(|\theta_L|,|\theta_R|)\ge\rho\), where
\(w_j=-2\cos\theta_j\). The degree bound, (18), and this real
gap satisfy Lemma 1 of
[open-source stability](research_mixed_open_source_stability_reduction.md).
Therefore, for some positive \(c,B,t\) and a polynomial prefactor,
\[
 |\widehat Z_N(-2\cos(x_L+iy_L),-2\cos(x_R+iy_R))|
 \le CN^A\exp N\left\{
 M_{\rm open}-c\sum_{j=L,R}(1-\cos x_j)+B\sum_{j=L,R}y_j^2
 \right\},\qquad |y_j|\le t.
\tag{19}
\]
This is a nonzero local packet and quadratic strip estimate for the
explicitly enlarged partial source (16) or (17).

The new states here are arbitrary hybrid middle states, including
outer real tails and their height-reset joins. The restriction is
the two fixed long plateau collars and the unselected physical
boundary regions. No estimate is proved for a bad state entering
those regions, for simultaneous incoming terminal selection, or
for an unproved terminal reference domain. Short words without the
two safe blocks are not settled by this argument. The complete
finite boundary functions and hence whole-source noncancellation
remain open on those remaining states.
