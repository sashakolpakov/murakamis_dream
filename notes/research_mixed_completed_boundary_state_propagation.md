# Propagating completed boundary states across an unrestricted middle

Private research deduction, 10 November 2026. Exact retention of the
four clean closing losses removes the long plateau corridors from
several already completed physical boundary comparisons. The boundary
sources themselves are unchanged. In particular this includes the
previously separate selected-last variant, the uncontracted active
right tail, and the completed two-position terminal selection patterns.

The two exact source charts are stated separately below. Contracting
the terminal coordinate sums its entire finite source; it does not
identify its individual sectors with sectors in the uncontracted chart.

## 1. Original source, cuts and the retained completion

Fix the actual complete-color reference of a fixed positive word
\(n_j=3+\epsilon_j\), \(1\le j\le m\), with the original markings,
lifts and endpoint factors. Put
\[
 k_4=\sum_{j=1}^m\epsilon_j,\qquad
 X_j=e^{-2\pi iz_j},\qquad
 D_j=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j},
 \qquad \sigma_j\in\{0,\epsilon_j\}.
\tag{1}
\]
Use either of the following literal integrands:
\[
\begin{split}
 \mathscr J^u_{\sigma,N}
   &=U_{\epsilon_1,N}(w_L,X_1)
       \prod_{j=2}^{m}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal H_N(w_R,X_m^{-1})\prod_{j=1}^{m}D_j,\\
 \mathscr J^c_{\sigma,N}
   &=U_{\epsilon_1,N}(w_L,X_1)
       \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)
       \prod_{j=1}^{h}D_j,\qquad h=m-1 .
\end{split}
\tag{2}
\]
Their original scalars are, respectively,
\[
 \kappa_N^{m+k_4}N^{m+k_4},
 \qquad
 \kappa_N^{m+k_4}N^{m+k_4-1},\qquad |\kappa_N|=1.
\tag{3}
\]
These are equations (9)--(11) of
[open-word inheritance](research_mixed_open_word_window_inheritance.md)
and equation (13) of
[exact terminal contraction](research_mixed_reversed_cap_assembly.md).
Every terminal row, its own weight, its selections and its ordinary
color have already been summed inside \(\mathcal V\). There is no
remaining selection \(\sigma_m\) in the second line of (2).

Choose safe ordinary cuts \(p,\ldots,q\), \(q\ge p\), in the
chosen chart. Retain exactly the eight-vertex safety halo of
[the open boundary reduction](research_mixed_open_boundary_comparison_reduction.md).
In the contracted chart use the same inheritance condition on its
retained ordinary graph, as in
[contracted boundary collars](research_mixed_contracted_boundary_collar_completion.md).
Set
\[
\begin{split}
 I&=[p-2,q+1],\qquad
 T_L=\{p-2,p-1,p\},\qquad T_R=\{q-1,q,q+1\},\\
 F&=I\setminus(T_L\cup T_R)=[p+1,q-2],\qquad
 P=[.22,.45],\qquad \kappa=1/20000 .
\end{split}
\tag{4}
\]
Reversed intervals are empty; repeated protected symbols are counted
once. Require all symbols in \(T_L\cup T_R\) to be unselected in
\(P\). Their displacements need not be small. Every symbol in
\(F\) may be any original alphabet state. Its original hybrid
height, complete Fourier alternatives and source priority are kept.

The non-plateau or selected departures in a boundary state listed
below must lie outside the protected triples. Its complete source
window must lie in the corresponding physical boundary product.
An unselected incoming target may be shared with the protected
plateau strip, with its original halfweight. No window is divided
through a selected position or through an unproved height transport.

Write \(r_j=a_j+ic_j\) for the original reference. For free symbols
retain
\[
 p_i=\min\{1,\sigma_i+
             400(\operatorname{clamp}_P x_i-a_i)^2\}.
\tag{5}
\]
Let \(A_p,E_q,D\) be the unchanged six-edge closing quantities.
The adopted
[clean-closing theorem](research_mixed_clean_closing_edges_completion.md),
equations (5), (8) and (12), proves
\[
 D\ge -A_p-E_q+\kappa\sum_{i\in F}p_i,\qquad
 \sum_{j=p}^q w_j\le-\kappa\sum_{i\in F}p_i .
\tag{6}
\]
This uses the actual open reference, not a periodic replacement.
The four exact losses on \(p-2,p-1,q+1,q+2\) survive all
preliminary moves and are disjoint from the incoming-edge occupation
charges assigned to \(F\).

Let \(L_N,R_N\) be the literal cut moduli. The left one is the same
in both charts:
\[
 L_N=|U_{\epsilon_1,N}|
        \prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
        \prod_{j=1}^{p-2}|D_j|\,|D_{p-1}|^{1/2}.
\tag{7}
\]
On the right they are
\[
\begin{split}
 R_N^u&=|\mathcal H_N(w_R,X_m^{-1})|
             \prod_{j=q+1}^{m}|C_{\epsilon_j,N}|
                    |D_q|^{1/2}\prod_{j=q+1}^{m}|D_j|,\\
 R_N^c&=|\mathcal V_{\epsilon_m,N}|
             \prod_{j=q+1}^{h}|C_{\epsilon_j,N}|
                    |D_q|^{1/2}\prod_{j=q+1}^{h}|D_j|.
\end{split}
\tag{8}
\]
Each middle factor carries the other two allocated halves. These
are nonnegative modulus identities, including at zeros; no Fourier
factor is divided out.

Using the original baseline actions \(M_L,M_R\), define
\[
\begin{split}
 G_{L,N}&=N^{-1}\log L_N-M_L+
              \Re[P_{p,a}(z_{p-1}-r_{p-1})],\\
 G_{R,N}&=N^{-1}\log R_N-M_R+
              \Re[P_{q,b}(z_q-r_q)] .
\end{split}
\tag{9}
\]
The convention is \(\log0=-\infty\). The two boundary rates in the
six-edge reduction are \(G_{L,N}-A_p,G_{R,N}-E_q\).
The original complex tangents, baseline identity and (6) therefore
give, with one total finite-source tolerance,
\[
 N^{-1}\log|\mathscr J_{\sigma,N}|-M_{\rm open}
 \le G_{L,N}+G_{R,N}
              -\kappa\sum_{i\in F}p_i+\eta+O_m(\log N/N).
\tag{10}
\]
The uncontracted reduction is equation (10) of the open boundary
note; the contracted reduction is equation (9) of the contracted
collar note. Those algebraic identities precede their old corridor
pinning arguments. Equation (6) replaces that later argument.

## 2. Two complete left states

The following left states are valid in either chart, with the same
actual prefix calibration and the literal product (7).

**L0: unselected plateau prefix.** All coordinates \(1,\ldots,p-1\)
are unselected in \(P\), at their original heights. The complete
first-cap and ordinary supporting planes in equation (5) of
[the full unselected plateau theorem](research_mixed_full_unselected_plateau.md)
give
\[
                            G_{L,N}\le \eta+O_m(\log N/N).
\tag{11}
\]
Their quadratic losses can also be retained. The first-cap plane
is a complete source bound at independent targets, not a claim of a
moving relative packet over all of \(P\).

**LC: full first collar.** For first types \((3+\alpha,3+\beta)\),
use the precise source domain from equations (10)--(12) of
[independent first-collar prefixes](research_mixed_first_collar_independent_plateau_middle.md):
\[
\begin{gathered}
 z_1=x_1\in[0,\rho],\qquad
 \sigma_1\in\{0,\alpha\},\qquad
 z_2=y_2+ik,\qquad y_2\in I_{3+\beta},\\
 I_3=[.267,.433],\qquad I_4=[.24,.363].
\end{gathered}
\tag{12}
\]
For \(\beta=0\), coordinate two is unselected and \(k\) lies
between \(c_2\) and zero. For \(\beta=1\), allow either
\(\sigma_2=0,\ c_2\le k\le0\), or
\(\sigma_2=1,\ 0\le k\le7/500\).
Every later prefix target through \(p-1\) is independently
unselected in \(P\) at its original height. The collar width is the
fixed width of those source proofs, chosen before \(N\).

The complete ordinary-cut prefix theorem in Section 3 of
[three-row source assembly](research_mixed_three_row_source_assembly.md)
then gives
\[
 G_{L,N}\le-\Delta_L+\eta+O_m(\log N/N),\qquad
 (\Delta_{00},\Delta_{10},\Delta_{01},\Delta_{11})
       =(3/100,3/125,4/125,4/125).
\tag{13}
\]
The first and second complete selected weights are retained. For
second type four, the changed second-height cost on edge three was
already paid by that prefix theorem; it is not charged again here.
All later heights are unchanged because the second real interval
lies in \(P\). The cut marginal cancels since
\(P_{p-1,b}+P_{p,a}=0\). The same identity proves (11).
Thus (13) has exactly the normalization of (9).

Set \(\Delta_L=0\) for L0. These two states are the left menu used
below. Other proved selected-front windows are not needed for the
corridor-dependent propagation asserted here.

## 3. The uncontracted right menu

Here retain the first line of (2), with \(m\) retained coordinates.

**R0u: coherent unselected right buffer.** The targets
\(q,\ldots,m\) are unselected in a sufficiently small real coherent
neighborhood of their actual references, at their original heights.
Equation (4) of
[buffered endpoint sectors](research_mixed_buffered_endpoint_sectors.md)
gives
\[
                         G_{R,N}\le\eta+O_m(\log N/N).
\tag{14}
\]
The relevant Hessian is the one-ended endpoint Schur form of the
original full conditional kernel, \(\mathcal H_N(w_R,X_m^{-1})\),
and the last diagonal
weight, with the surviving external halfweight counted once.

**RAu: active private terminal tail.** Keep \(q,\ldots,m-1\) in
that sufficiently small unselected coherent neighborhood, and put
\[
 x_m=e\in[1/2,1],\qquad
 \sigma_m\in\{0,\epsilon_m\}.
\tag{15}
\]
Keep the original terminal contour and Fourier alternatives. The
neighboring target has its unchanged reference height; the terminal
right cutoff is one. Corollary 4, equation (21), of the buffered
endpoint theorem gives, at every actual reference of length at least
three,
\[
 G_{R,N}\le-\frac1{5000}-K(e)+\eta+O_m(\log N/N),
 \qquad K(e)=-\int_{1/2}^{e}\log\sin(\pi t)\,dt\ge0 .
\tag{16}
\]
This corollary uses the complete
[remaining ending-type comparisons](research_mixed_terminal_remaining_disk_gaps.md)
and the actual-reference
[coupled three-three comparison](research_mixed_terminal_coupled_disk_gap.md).
The latter holds in a genuine neighborhood of each admissible actual
reference, so a small neighboring target variation is licensed.
No larger independent private-reference rectangle is substituted.

Under the older compact-interior rectangle hypotheses of the buffered
theorem, the stronger \(1/400\) in its equation (5) remains
available. We use only the common \(1/5000\) here. The complete
terminal modulus in (16) is not replaced by an unweighted \(C_m\)
bound or a separate cap norm. Set
\[
 (\Delta_R,K_R)=
 \begin{cases}
 (0,0)&\text{for R0u},\\
 (1/5000,K(e))&\text{for RAu}.
 \end{cases}
\tag{17}
\]
The smallness requirement on the other right-buffer targets remains
essential. No uncontracted full-\(P\) terminal statement is inferred.

## 4. The terminal-contracted right menu

Here retain the second line of (2), with \(h=m-1\). Outside the
explicit selected window, every target from \(q\) to \(h\) is
unselected in \(P\) at its original height. All real targets in a
listed window vary independently over \(P\). The references are
the actual canonical suffix families of the cited sources, with
their original incoming domains \(K_3,K_4\), not arbitrary points
of containing image rectangles.

The following table gives the nonzero selections and a complete
calibrated suffix deficit. Put \(K_R=0\) in this chart.

| State | Required suffix types | Selected retained targets and heights | \(\Delta_R\) |
|---|---|---|---:|
| RPc | Any | None | \(0\) |
| RS3c | \((n_{m-2},n_{m-1},n_m)=(3,4,3+\epsilon)\) | \(h\), height \(1/100\) | \(1/10000\) |
| RS4c | \((n_{m-2},n_{m-1},n_m)=(4,4,3+\epsilon)\) | \(h\), height \(1/100\) | \(1/2600\) |
| RSSc | \((n_{m-3},n_{m-2},n_{m-1},n_m)=(3+\gamma,4,4,3+\epsilon)\) | \(h-1,h\), both height \(1/100\) | \(1/100\) |
| RSPc | Same four-type suffix as RSSc | \(h-1\), height \(1/100\); \(h\) unselected | \(1/400\) |

Here \(\gamma,\epsilon\in\{0,1\}\). The one-selected rows
require \(m\ge3\), and the two-position rows \(m\ge4\), in
addition to the safe-cut and window-placement hypotheses of
Section 1. The statement for each row is
\[
                     G_{R,N}\le-\Delta_R+\eta+O_m(\log N/N).
\tag{18}
\]

For RPc, apply the complete ordinary and terminal supporting planes
from the full unselected plateau theorem. The full terminal plane,
including its own terminal weight and all alternatives, cancels the
last retained marginal. Internal halfweights occur twice, the cut
halfweight once. This proves (18) with zero deficit, and permits
quadratic losses as in the clean-closing theorem.

For RS3c and RS4c, use respectively
[the three-input terminal completion](research_mixed_terminal_three_input_kernel_completion.md)
and
[the uniform four-input terminal completion](research_mixed_terminal_uniform_kernel_completion.md).
Their literal selected-last product is
\[
 |C_{1,N}(X_b,X_a)\mathcal V_{\epsilon,N}(w_R,X_a)
           d_N(X_a)X_a^{-N}|\,|d_N(X_b)|^{\nu/2},
 \quad (b,a)=(z_{h-1},z_h),
\tag{19}
\]
where \(\nu=0\) or \(1\) is the type flag at \(b\).
The incoming height stays actual; the height at \(a\) is \(1/100\).
The original complex incoming marginal and precisely the incoming
halfweight in (19) are retained. Joining the preceding unselected
planes cancels that marginal, ending in the cut tangent of (9).
The source deficits are exactly the two entries in the table.

For RSSc, use equation (3) and Corollary 2, equation (15), of
[the two-selected terminal completion](research_mixed_terminal_two_selected_kernel_completion.md).
The source is
\[
 |C_{1,N}(X_c,X_b)C_{1,N}(X_b,X_a)
       \mathcal V_{\epsilon,N}(w_R,X_a)
       d_N(X_b)X_b^{-N}d_N(X_a)X_a^{-N}|
                                     |d_N(X_c)|^{\gamma/2},
\tag{20}
\]
where \((c,b,a)=(z_{h-2},z_{h-1},z_h)\).
The source's already proved stronger raw deficit is \(1/100\);
no saved-value arithmetic is performed here. Its unique surviving
incoming complex marginal cancels the preceding plane, with the
halfweight allocation in (20), giving (18).

For RSPc, Theorem 1, equation (4), of
[the penultimate-only completion](research_mixed_terminal_penultimate_selected_completion.md)
bounds
\[
 |C_{1,N}(X_c,X_b)C_{1,N}(X_b,X_a)
                 d_N(X_b)X_b^{-N}|
          |d_N(X_c)|^{\gamma/2}|d_N(X_a)|^{1/2}
\tag{21}
\]
with deficit \(1/400\) and two complex marginals. Adjoin the
unselected terminal plane at \(a\), with its other halfweight.
Its derivative cancels the outgoing marginal exactly. The preceding
unselected factors cancel the incoming one and ultimately leave
the original cut tangent in (9). This is the explicit joining
identity (6) in that source. It is not the result of removing a
selection from the two-selected theorem.

All four selected rows retain every ordinary and terminal profile,
physical end row, alias, normal and complete selected-weight
alternative in their source theorems. In particular the selected
height is not identified with the unselected reference height.
The canonical reference identifications retain the original suffix
equations and the external type flag. They are not finite-contour
reversal identities.

## 5. Propagation theorem and finite loss

**Theorem.** Choose either left state L0 or LC, and one right state
from the menu for the chosen chart. Assume their original domains
and the safe-cut compatibility in Section 1. Every free middle
symbol in \(F\) is arbitrary. For every \(\eta>0\), on sufficiently
small fixed ordinary-color disks about \((-2,-2)\), one has
\[
 \boxed{\quad
 |\mathscr J_{\sigma,N}|
 \le C_{\eta,m}N^{A_{\eta,m}}
       \exp N\left\{M_{\rm open}+\eta-\Delta_L-\Delta_R-K_R
                            -\kappa\sum_{i\in F}p_i\right\}.
 \quad}
\tag{22}
\]
The disks and all contour sizes are fixed before \(N\). The result
holds through both level parities and for fixed ordinary-color jets
on smaller disks. Integrating the right side of (22), or taking its
supremum on the specified region, bounds the original restricted
sector sums and integrals after restoring the correct scalar (3).

*Proof.* The boundary inequalities (11), (13), (14), (16) and
(18) concern exactly (7)--(8), with their original calibrated
tangents. Insert the appropriate two inequalities into (10).
Choose their finitely many tolerances and the middle-source
tolerance to total at most \(\eta\). This proves (22).

No boundary argument uses a free middle target: the protected
triples fix all endpoint heights of the cut factors, and the
boundary departures lie outside them. The actual four-symbol
middle rates are the ones in (6). Thus a selected, seam, early,
upper or raw-right free symbol may occur immediately next to a
protected triple. Its old source and charge remain present.

The complete boundary sources have their stated small ordinary-color
neighborhoods, including at ramified complete colors. Take a common
smaller disk for the finitely many factors at the fixed reference.
All integer-weighted finite source factors are holomorphic there.
Cauchy's formula on smaller disks proves the fixed-jet assertion;
no modulus halfweight is differentiated. The original contour
Jacobians are bounded for the fixed word. Summing the finitely many
original alternatives, integrating their fixed domains and inserting
(3) adds only polynomial prefactors. This proves the final assertion.
\(\square\)

Every nonneutral boundary row has \(\Delta_L+\Delta_R\ge\kappa\).
Also every selected or nonplateau free symbol has \(p_i=1\).
Consequently any region in (22) with an active boundary row or at
least one such free symbol has, after allocating the one total
tolerance and absorbing polynomial factors, the common finite gap
\[
                         \kappa/2=1/40000.
\tag{23}
\]
One can instead retain the larger tabulated deficit and the exact
occupation sum. The count of sectors and the polynomial prefactors
may depend on the fixed word; no uniform level threshold for all
word lengths is asserted.

The standard safe cuts \(p=16,\ q=m-15\) give
\(F=[17,m-17]\). For \(m\ge34\) it is nonempty and the listed
short boundary windows are separated from it by the original safety
halos. Shorter words are included only when the general safe-cut and
window conditions hold. If protected triples overlap, \(F\) is
empty and (6) is the direct clean-plateau inequality. The propagation
argument still applies whenever the physical windows fit, without
inventing a missing short-word corridor.

## 6. What is newly paid, and what is still outside

The theorem removes both long plateau corridors and small-cut
requirements from the catalogued boundary comparisons. In particular:

* LC can be paired with RAu on the original uncontracted source.
* Either left state can be paired with either selected-last type on
  the terminal-contracted source, including the optional selected
  terminal-retained variant omitted from the clean-closing theorem.
* Either left state can be paired with RSSc or RSPc, with the entire
  free middle alphabet in place of the previously permitted plateau
  or safe interior-selection middle.

For each combination the only boundary plane used is one already
proved on its stated domain. The new step is the exact cancellation
in (6), which leaves its strict deficit unspent. No local cap
packet is extended to a large independent rectangle by this argument.

The charts in (2) are two exact representations of the source.
The second representation has already summed the private terminal
coordinate and its alternatives. Therefore an RAu sector must not
be added to a contracted RPc or selected-terminal sector as though
they were disjoint. Any construction of a larger restricted
polynomial must first choose one chart and specify disjoint original
regions in that chart.

This catalog does not cover an earlier nonplateau or selected
physical prefix outside LC, an uncontracted right buffer outside
its coherent neighborhood, a contracted suffix target outside \(P\),
or terminal selection patterns not listed in Section 4. In particular
RSPc still requires its unselected final retained factor to have own
type four. Other already completed selected-front windows retain
their own separate source theorems; they have not been included in
the present catalog or declared unproved.

A small occupation cut found deeper inside a word cannot remove
such an earlier boundary departure. Its preceding literal prefix
still needs its own calibrated bound. Neither the missing early
taper nor other remote boundary profiles are inferred from (22).
All actual reference heights, couplings, external markings and
original assignments remain unchanged. There is no whole-source,
new knot-family, arbitrary short-filling, or finite-exception
conclusion.

## Source bindings

| File | SHA-256 |
|---|---|
| research_mixed_clean_closing_edges_completion.md | cc5b75d521fe648ab5aa0974e162de02b14fb814fc628635a1126349df5dfca9 |
| research_mixed_open_boundary_comparison_reduction.md | 5d3f875a6c1a7e0c2c9840c16674dc8ad5921bf0f2312202cb26f278c86c72ce |
| research_mixed_open_word_window_inheritance.md | b00b282d3258a42a4e5b6fe1af41b92d8a2c26cc31709b043a133dc27bbdf0ea |
| research_mixed_reversed_cap_assembly.md | 79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c |
| research_mixed_contracted_boundary_collar_completion.md | c51b656e3f49e00d33e98df508941316a8db0df80a1a38ecd63312adde2786c6 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_first_collar_independent_plateau_middle.md | 5fe7f1f79d25fb39ff8da1ec72f11fdd2b914f36e49710cc1e633cbae614705f |
| research_mixed_buffered_endpoint_sectors.md | 57bd3869f66c188d837da2de109bba6bfd01dc73c16a199e6f8eb26e11b7bb71 |
| research_mixed_terminal_remaining_disk_gaps.md | c8b3a91f4f1ae9932dde77a4d24b5c121bf067b8321f4c08a48e532e238e505f |
| research_mixed_terminal_coupled_disk_gap.md | 823bf80f528094f87301e626fcfd5a38f51ac167e3209d57d2f6bf40bafeecb3 |
| research_mixed_terminal_uniform_kernel_completion.md | 4f37ddd1bb41cef9614aa2f1da2629fa2c8bc8a27fc3b3b8392969075002f195 |
| research_mixed_terminal_three_input_kernel_completion.md | 42d011a41a4ff8d82d3282f44be65ec0fe920206d204eccdae59b8da94e1b8ba |
| research_mixed_terminal_two_selected_kernel_completion.md | abf71739967f9b1964192c3d41bc01cc21f56f39686b16e164ba60d7f2ed4910 |
| research_mixed_terminal_penultimate_selected_completion.md | 3c37d9071087bc0e57703413ba6b14f8bc20c9977703953b423151463498dff5 |

The duplicate search and all direct source proofs were read. This
deduction used no new mathematical numerical evaluation, saved-value
arithmetic, import, compilation, test, or edit to a frozen note.

