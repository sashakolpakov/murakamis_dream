# Exact closing-loss retention with plateau boundary strips

Private research proof, 10 November 2026. The synthetic closing edges
are clean and unused by the interior charge allocation when their
protected triples are unselected plateau symbols. Retaining their exact
losses cancels both artificial closing fees. The middle can contain
every original selection, seam and right state, without long plateau
corridors or small cut displacements.

The finite-source application first contracts the terminal variable
exactly. It uses the whole supporting plane for that terminal transform,
not a pointwise bound for the uncontracted product \(C_mH_N\).
Physical boundary strips still have explicit restrictions.

## 1. Actual references and exact closing edges

Use an actual complete-color reference of a fixed positive three/four
word, with safe ordinary cuts \(p,\ldots,q\), \(q\ge p\), from
[the open boundary reduction](research_mixed_open_boundary_comparison_reduction.md).
Keep its original four-symbol rates \(w_j\), labels, tangents and
hybrid heights. Set
\[
\begin{split}
 I&=[p-2,q+1],\\
 T_L&=\{p-2,p-1,p\},\qquad T_R=\{q-1,q,q+1\},\\
 F&=I\setminus(T_L\cup T_R)=[p+1,q-2].
\end{split}
\tag{1}
\]
An interval with reversed endpoints is empty; overlapping protected
symbols are counted once. Require all protected symbols to be
unselected with real coordinates in \(P=[.22,.45]\). Their
displacements need not be small. Symbols in \(F\) are arbitrary
original alphabet states. Outside \(I\), the synthetic configuration
is baseline.

The unchanged six-edge closure is
\[
\begin{split}
 A_p&=\sum_{j=p-3}^{p-1}w_j,\qquad
 E_q=\sum_{j=q+1}^{q+3}w_j,\qquad
 D=-\sum_{j=p-3}^{q+3}w_j,\\
 \sum_{j=p}^{q}w_j&=-A_p-E_q-D.
\end{split}
\tag{2}
\]
Only four closing edges can be nonzero:
\[
 \mathcal C=\{p-2,p-1,q+1,q+2\},\qquad
 e_j=-w_j=-\Re(\phi_j-\Gamma_j)\ge0,\qquad
 \sum_{j\in\mathcal C}e_j=-A_p-E_q.
\tag{3}
\]
They are ordinary unselected PP edges at their original endpoint
heights. For example edge \(p-1\) has stencil
\(p-3,p-2,p-1,p\), all baseline or protected plateau. Although
the inward-facing symbol \(p\) can have an attenuated height
because of a free neighbor, that height does not enter edge \(p-1\):
only its real cutoff enters, and that cutoff is one. The reflected
statement applies on the right. Thus every closing edge in (3)
stays unchanged even when a bad free symbol immediately follows
a protected triple.

For \(i\in F\), keep the original occupation
\[
 p_i=\min\{1,\sigma_i+
     400(\operatorname{clamp}_P x_i-a_i)^2\},\qquad
                         \kappa=\frac1{20000}.
\tag{4}
\]
The safe actual reference satisfies \(.27<a_i<.39\). Hence every
original selected or nonplateau free symbol has \(p_i=1\).

## 2. Retaining the closing losses in the complete charge proof

**Lemma 1.** On the complete original mixed upper envelope,
\[
 \boxed{\quad D\ge -A_p-E_q+\kappa\sum_{i\in F}p_i.\quad}
\tag{5}
\]
All actual-reference heights and all free source alternatives are
retained.

*Proof.* Repeat [full-period occupation](research_mixed_full_period_occupation.md),
retaining the full losses (3) instead of discarding them. The following
checks ensure that no charge is used twice.

Every comparison leaves the protected real coordinates and selections
unchanged. Right clamping, deep-low raising, upper-transition clamping
and minimum-level transport move only the corresponding nonplateau
symbols; seam replacement also acts only on a free symbol. Each
complete four-symbol stencil in (3) contains no free symbol.
Consequently its rate, height and source label stay unchanged
throughout these comparisons. The actual-open synthetic support
and original safety halos remain those of the boundary reduction.

At the final early/plateau/right configuration, an affected plateau
endpoint has an early neighbor. Neither endpoint of an edge in
\(\mathcal C\) has such a neighbor. Section 3 of
[the early charge proof](research_mixed_early_plateau_right_clusters.md)
assigns an early credit only to an affected PP or PR edge. None of
the four closing edges receives or consumes such a credit. The seam
charges and intermediate height changes likewise never use these
unchanged stencils.

Equation (2) of the occupation theorem therefore permits the exact
choice \(L_j=e_j\) on every \(j\in\mathcal C\). On the
other clean PP edges retain the occupation losses as before.
In its final injection, assign an incoming clean PP edge \(j\)
only to a free vertex \(j\in F\) outside
\(Z=N_2(E)\cup N_1(R)\). Those edge indices are disjoint
from \(\mathcal C\), so no closing loss is spent on them.

For free vertices inside \(Z\), the same incidence estimate and
rational reserves give
\[
 |Z|\le17n_E+3n_C,\qquad
 \frac{17}{20000}<\frac1{1000},\quad
 \frac3{20000}<\frac1{500},\quad
 \frac1{20000}<\frac1{4000}.
\tag{6}
\]
Only the free subset of \(Z\) is charged; including protected
vertices in the count only enlarges its upper bound. All original
removed seams lie in \(F\), and the unchanged \(3/1000\)
reserve pays each of their original occupations one. Other
occupations are preserved by the transports, exactly as in the
occupation theorem. The total original synthetic defect is therefore
at most
\[
                   -\sum_{j\in\mathcal C}e_j
                            -\kappa\sum_{i\in F}p_i.
\tag{7}
\]
Equations (2)--(3) prove (5).

If the protected triples overlap or abut, \(F\) is empty and
every synthetic symbol is unselected plateau. Retaining the four
distinct closing losses among the nonnegative ordinary pair losses
proves (5) directly. No large-length or disjoint-block argument is
hidden in this case. \(\square\)

The exact actual-middle consequence is
\[
                         \sum_{j=p}^{q}w_j
                                  \le-\kappa\sum_{i\in F}p_i.
\tag{8}
\]
Its original complex tangents are still included. This is a
calibrated sum, not a bound on unnormalized individual factors.

## 3. Free-only reserved completion

For \(0\le\theta<1\), define
\[
 \widehat D_\theta=D-\theta\kappa\sum_{i\in F}p_i,\qquad
 \widehat V_\theta=\inf_{\text{all free symbols}}\widehat D_\theta.
\tag{9}
\]
This is deliberately different from \(D_\theta\) in
[full-alphabet finite-depth completion](research_mixed_actual_open_full_alphabet_completion.md):
no protected-triple occupation is subtracted here. Lemma 1 gives
\[
 \widehat D_\theta\ge-A_p-E_q+
                 (1-\theta)\kappa\sum_{i\in F}p_i,\qquad
                     \widehat V_\theta\ge-A_p-E_q.
\tag{10}
\]
The same bound holds after pinning additional free symbols.

For literal calibrated boundary rates
\(\mathcal B_L=G_L-A_p\), \(\mathcal B_R=G_R-E_q\),
\[
 \boxed{\quad
 \mathcal B_L+\mathcal B_R-\widehat V_\theta\le G_L+G_R.
 \quad}
\tag{11}
\]
At an individual free configuration, the stronger bound is
\[
 \mathcal B_L+\mathcal B_R-D
                 \le G_L+G_R-\kappa\sum_{i\in F}p_i.
\tag{12}
\]
No separate nonpositivity of the raw boundary rates is asserted.
Their artificial closing fees have been canceled exactly.

For comparison, the full reservation from the finite-depth note
only gives
\[
 D_\theta\ge-A_p-E_q-\theta\kappa
       \sum_{i\in T_L\cup T_R}p_i
       +(1-\theta)\kappa\sum_{i\in F}p_i.
\tag{13}
\]
The protected sum has at most six terms. It must not be omitted
when using that differently defined completion. Its \(p_i\) are
defined by the same original formula (4), now at the protected indices.

## 4. The exact contracted source on fixed boundary plateau strips

Put \(h=m-1\) and use the original terminal-contracted source
\[
\begin{split}
 \mathscr J_{\sigma,N}
 ={}&U_{\epsilon_1,N}(w_L,X_1)
       \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)
       \prod_{j=1}^{h}D_j,\\
 D_j={}&d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}.
\end{split}
\tag{14}
\]
Its scalar is exactly
\(\kappa_N^{m+k_4}N^{m+k_4-1}\). All terminal rows,
its own diagonal weight and all terminal Fourier alternatives
are already summed inside \(\mathcal V\); there is no second
terminal selection in (14).

Choose safe cuts in its ordinary middle. Require every retained
symbol outside \(F\) to be unselected plateau; the free symbols
remain arbitrary. The physical left factor ends at \(p-1\),
whose neighbors are plateau, and the right factor starts at \(q\),
whose neighbors are plateau. Thus all argument heights of the
physical boundary products are their actual fixed heights.

Section 3 of
[contracted boundary collar completion](research_mixed_contracted_boundary_collar_completion.md)
gives the unchanged exact reduction for
\[
\begin{split}
 L_N&=|U_{\epsilon_1,N}|
       \prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|D_j|\ |D_{p-1}|^{1/2},\\
 R_N&=|\mathcal V_{\epsilon_m,N}|
       \prod_{j=q+1}^{h}|C_{\epsilon_j,N}|
       |D_q|^{1/2}\prod_{j=q+1}^{h}|D_j|.
\end{split}
\tag{15}
\]
Its six-edge identity has the same \(D,A_p,E_q\) and
original marginals as (2). Its proof does not use the long
corridors later imposed for its separate pinning and fee payment.

Write \(d_j=x_j-a_j\) and define
\[
 \mathcal Q_\partial=\kappa_*\left(
  2\sum_{j=1}^{p-2}d_j^2+d_{p-1}^2+
  d_q^2+2\sum_{j=q+1}^{h}d_j^2\right),\qquad
                      \kappa_*=\frac1{2500000}.
\tag{16}
\]
Equation (5) of
[the whole unselected plateau theorem](research_mixed_full_unselected_plateau.md)
bounds every complete finite factor in (15), at independent targets
in \(P\) and actual reference heights. Internal halfweights
occur twice and cut halfweights once. Original stationarity cancels
the internal linear terms and the two cut tangents, giving
\[
                              G_L+G_R\le-\mathcal Q_\partial .
\tag{17}
\]
The whole terminal transform plane is used here, not an estimate
of \(|C_mH_ND_m|\) at an unsummed terminal coordinate.

**Theorem 2.** For every \(\tau>0\), sufficiently small fixed
ordinary-color disks give, through both level parities,
\[
 |\mathscr J_{\sigma,N}|
 \le C_{\tau,m}N^{A_{\tau,m}}
    e^{N\{M_{\rm open}+\tau-\mathcal Q_\partial
                              -\kappa\sum_{i\in F}p_i\}}.
\tag{18}
\]
Fixed ordinary-color derivatives satisfy the same rate on smaller
disks, with larger polynomial factors.

*Proof.* Combine the complete boundary planes, the literal
contracted six-edge reduction, and (12). Choose the finitely many
source and color tolerances to sum to \(\tau\). All rows,
aliases, endpoint terms, colors and scalar factors are those of
the original identities. No Fourier factor is divided out.
Cauchy on smaller endpoint color disks proves the derivative
statement with the same arbitrarily prescribed rate tolerance.
\(\square\)

If some free symbol is selected or nonplateau, its occupation is
one. Choose \(\tau<\kappa/4\), then absorb polynomial factors
into another \(\kappa/4\). The sum and integral of all such
new sectors has gap at least \(\kappa/2\). These sectors are
disjoint from the wholly unselected plateau. Adding them to that
already proved contribution preserves its original nonzero Gaussian
coefficient, action, scalar and \(N^{-3/2}\) power, after the
usual fixed color-neighborhood reduction. This is a restricted
source statement: all retained symbols outside \(F\) still
obey the stated plateau conditions.

For example the original conservative cuts \(p=16\),
\(q=m-15\) give \(F=[17,m-17]\) in the \(h=m-1\)
chart. For \(m\ge34\) that free interval is nonempty, while
the first sixteen and last sixteen retained coordinates remain
unselected plateau. The existing safety halo is unchanged.
Shorter words are covered only when the general safe-cut
hypotheses hold; no full short-word conclusion is asserted.

No strict loss at the protected coordinates \(p,q-1\) is
claimed from (16) alone. The wholly plateau region, including those
coordinates, already has its separate complete Gaussian theorem.

## 5. The first collar with arbitrary plateau cut triples

Replace the left boundary conditions of Theorem 2 by the complete
first-collar prefix conditions of
[three-row source assembly](research_mixed_three_row_source_assembly.md),
Section 3, equation (10). These allow every first-pair type,
\(x_1\in[0,\rho]\), its allowed first selection,
\(x_2\in I_{3+\epsilon_2}\) with its original selected or
unselected height path, and independent unselected \(P\)
targets from coordinate three through the cut. Keep the protected
triples unselected in \(P\). All free symbols remain arbitrary.

That source theorem's equation (11) gives
\[
 G_L\le-\delta_{\epsilon_1\epsilon_2},\qquad
                 \min_{\alpha,\beta}\delta_{\alpha\beta}=\frac3{125}.
\tag{19}
\]
Every first-pair height cost and complete selected-weight branch
has already been paid; the cut marginal and halfweight are the
ones in (15). The right contracted plateau boundary has \(G_R\le0\).
Thus
\[
 |\mathscr J_{\sigma,N}|
 \le CN^A e^{N\{M_{\rm open}-3/125+\tau
                                 -\kappa\sum_{i\in F}p_i\}}.
\tag{20}
\]
It has finite gap at least \(3/250\) after one aggregate
tolerance and the polynomial factors. There is no cut smallness,
local opposite-boundary requirement, or long corridor in this
contracted-source version.

For the original uncontracted source, the same conclusion holds
if the right physical boundary lies in its genuine coherent
neighborhood, where \(G_R\le0\) is equation (4) of
[the buffered endpoint theorem](research_mixed_buffered_endpoint_sectors.md).
This strengthens
[the earlier small-cut deduction](research_mixed_first_collar_local_cut_completion.md)
without editing that proof or extending the uncontracted terminal
packet to arbitrary private targets.

If one instead insists on the full reservation in (13), the
first-collar completed inequality loses at most \(6\theta\kappa\).
Its strict sign still follows from
\[
                         6\kappa=\frac3{10000}<\frac3{125}.
\tag{21}
\]
This optional comparison does not identify the two reserved
completions or remove that loss from the neutral plateau theorem.

## 6. The remaining source obstruction

The new region enlarges the wholly unselected plateau and removes
the long-corridor restriction from the unselected-boundary version
of the earlier construction. Its separate selected-terminal variant
is not included here. A bad free symbol may occur immediately after
a protected triple, and it stays in the complete finite source
throughout.

Moving a cut does not automatically put every remote boundary
configuration in this region. Occupation averaging locates a
small plateau block, but does not remove a selected or nonplateau
physical symbol between that block and the endpoint. The prefix
and suffix planes in (17) require every intervening target to lie
in their actual independent domains. In (19) only the two specified
first-collar departures are licensed. Any further earlier bad
prefix symbol remains a different finite-source comparison.

The unchanged original reference heights, selected Fourier
alternatives and safety halos are essential. No new whole
ordinary-color strip, marked composition, knot identification,
arbitrary short-filling theorem or finite-exception conclusion
is inferred.

## Source bindings

| File | SHA-256 |
|---|---|
| research_mixed_full_period_occupation.md | 70cd6262e5737c70ed178cbf88ca69cb6f7d7eb659a493a21673bdd5b2830fec |
| research_mixed_early_plateau_right_clusters.md | f82dfea10cbfa7da907e6f86b2b781e2217c0104479a795aef1a06a669c5bc40 |
| research_mixed_open_boundary_comparison_reduction.md | 5d3f875a6c1a7e0c2c9840c16674dc8ad5921bf0f2312202cb26f278c86c72ce |
| research_mixed_actual_open_full_alphabet_completion.md | d41f2c57b0ee397a24f299f5ffbfb132a1fb78ed1c47423543c56c975da0b782 |
| research_mixed_contracted_boundary_collar_completion.md | c51b656e3f49e00d33e98df508941316a8db0df80a1a38ecd63312adde2786c6 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_buffered_endpoint_sectors.md | 57bd3869f66c188d837da2de109bba6bfd01dc73c16a199e6f8eb26e11b7bb71 |
| research_mixed_first_collar_local_cut_completion.md | f7889661dc3c9a79c31bbc31657211f4bfbafa5264a00231e9438f63b236ba52 |

All direct source proofs were read. No mathematical numerical
evaluation, source replay, import, compilation, test or edit
to a frozen manuscript was used.

