# Disjoint endpoint windows and the remaining complete-source obligations

Research deduction and coverage ledger, 6 November 2026. The proved
first-two and last-two comparisons can be multiplied when their
ordinary factors are disjoint. This removes redundant cross-end
casework on the plateau. It does not identify that plateau sum with
the whole open source. The penultimate-only input is the completed
saved-data recombination below; the real-color conclusion separately
uses the original cap and terminal real-color envelope theorems.

## 1. Exact disjoint-window closure

Fix a positive word in types three and four, of length \(m\ge6\),
with final types
\[
 (n_{m-3},n_{m-2},n_{m-1},n_m)
                  =(3+\gamma,4,4,3+\epsilon).
 \tag{1}
\]
Put \(h=m-1\), \(P=[.22,.45]\), and let \(r_j\) be the
original retained critical coordinates. Write the original allocated
action as
\[
       \Phi=L(z_1)+\sum_{j=2}^{h}\phi_j(z_{j-1},z_j)+\Pi(z_h),
       \qquad M=\Re\Phi(\mathbf r).
 \tag{2}
\]
These are the phases, branches and halfweights of the
[complete unselected plateau](research_mixed_full_unselected_plateau.md).
All real targets vary independently in \(P\).

Choose type-compatible sets
\[
 A\subseteq\{1,2\},\qquad
 B\subseteq\{h-1,h\},\qquad
 T\subseteq I_m^{(4)},\qquad
 I_m^{(4)}=\{j:6\le j\le m-5,\ \epsilon_j=1\}.
 \tag{3}
\]
The left selected heights are precisely those of the
[first-two assembly](research_mixed_double_selected_plateau_completion.md),
Section 3. The right selected heights are \(.01\), and the
interior selected heights are \(.014\). Every other retained
height is its original one. No whole-period selected factor is
declared to have a loss without its complete finite-source comparison.

Every choice of \(A\) can be expressed as a prefix containing
the cap and ordinary factors 2 and 3, with full weights at positions
1 and 2 and half the unselected weight at position 3. For first-only
selection, append the unselected third factor to the existing
two-factor bound. For the empty choice use the three unselected
supporting planes. The resulting reference action and marginal are
\[
 M_L=L(r_1)+\phi_2(r_1,r_2)+\phi_3(r_2,r_3),\qquad
                       p_L=\partial_2\phi_3(r_2,r_3).
 \tag{4}
\]
The original stationarity at positions 1 and 2 cancels their
internal tangents. Its raw deficit can be taken to be zero when
\(A\) is empty and at least \(1/3200\) otherwise; the precise
stronger individual deficits are retained in the cited assembly.

Similarly use a suffix containing factors \(h-1,h\) and the
terminal factor, with full weights at \(h-1,h\) and half the
unselected weight at \(h-2\). For last-only selection append the
preceding unselected ordinary factor to the completed terminal bound.
For no right selection use the original unselected supporting planes.
Its action and incoming marginal are
\[
 \begin{split}
 M_R&=\phi_{h-1}(r_{h-2},r_{h-1})
                      +\phi_h(r_{h-1},r_h)+\Pi(r_h),\\
 p_R&=\partial_1\phi_{h-1}(r_{h-2},r_{h-1}).
 \end{split}
 \tag{5}
\]
The available raw deficits are
\[
 d_R(B)=\begin{cases}
 0,&B=\varnothing,\\
 1/2600,&B=\{h\},\\
 1/100,&B=\{h-1,h\},\\
 1/400,&B=\{h-1\},
 \end{cases}
 \tag{6}
\]
where the last line follows from the
[penultimate-only criterion](research_mixed_terminal_penultimate_selected_criterion.md)
and its [completed saved recombination](../repro/results/research-mixed-terminal-penultimate-selected-budgets.json),
SHA-256 `83725f30893cbd7ad8f138f4db5cfbc934072f1c868600784be45c90505965d0`.
All four main budgets are strictly negative; the complete profile
bound is limited by the paid outgoing last-row deficit \(1/400\).
The other lines are proved by the
[last-selection theorem](research_mixed_last_selected_plateau_completion.md)
and [two-selected completion](research_mixed_terminal_two_selected_kernel_completion.md).

**Lemma 1 (disjoint closure).** For every choice in (3) whose
endpoint comparisons are proved, and every \(\eta>0\), the literal
integer-weighted sector integrand has upper rate
\[
 M-d_L(A)-d_R(B)-\frac{|E(T)|}{200}+\eta,
             \qquad E(T)=\bigcup_{j\in T}\{j,j+1\},
 \tag{7}
\]
with a polynomial prefactor. It holds on fixed sufficiently small
complex ordinary-color disks, through both parities and for fixed
color jets on smaller disks.

*Proof.* The left ordinary factors are 2 and 3, while the right
ones are \(h-1=m-2\) and \(h=m-1\). They are disjoint for
\(m\ge6\). The intervening factors are \(4,\ldots,m-3\),
possibly none. All incidences in \(E(T)\) lie in this intervening
set and are handled by the
[interior-selection theorem](research_mixed_interior_selected_plateau.md).
Every remaining ordinary factor uses its unselected tangent bound.

At \(m=6\), the two windows share only the unselected coordinate
\(z_3=z_{h-2}\). Their halves restore its integer weight, and
\(p_L+p_R=\partial_2\phi_3+\partial_1\phi_4=0\) at the
original reference. For larger \(m\), the intervening allocated
factors cancel these boundary marginals by the same original
stationarity equations. Every other internal affine displacement
also cancels, including the selected imaginary displacements.
Thus the total affine reference rate is exactly (2). Every weight
and factor occurs once. Sum the finite-source tolerances to \(\eta\)
and multiply the complete bounds, proving (7). Cauchy's formula is
applied to the original holomorphic integer-weighted source, not a
modulus halfweight. \(\square\)

Integrating over \(P^h\), summing the finitely many permitted
sectors and retaining the original scalar
\(\kappa_N^{m+k_4}N^{m+k_4-1}\) changes only polynomial
prefactors. Every nonempty proved selection has a strict gap.
Consequently this restricted sum retains the original nonzero
unselected packet, its action, normalization and power \(N^{-3/2}\).
This is an exact joining deduction, not an additional scalar test.

## 2. Real colors require their own established source domains

The right comparisons in (6) have the whole-real-color envelope
of the [terminal lift](research_mixed_terminal_profile_real_color_lift.md),
and the unselected terminal bound has the corresponding original
real-color estimate. The new penultimate-only two-factor bound has
no ordinary-color variable and can be adjoined to that
unselected terminal estimate.

If \(1\notin A\), the first cap remains at its original height.
Equation (14) of
[endpoint real-color decay](research_mixed_endpoint_real_color_decay.md)
bounds it by its same allocated tangent for all real left colors.
For \(A=\{2\}\), the selected two-ordinary-factor bound is color
independent, so this cap replacement preserves its gap. Therefore
(7) also holds over the full real color square for these choices.

If \(1\in A\), use instead the
[selected-prefix real-color lift](research_mixed_selected_first_prefix_real_color_lift.md).
It proves the unchanged five-profile cap envelope at the actual
selected heights, including the physical and revived Newton rows.
Its Corollary 2 preserves the original first-only and simultaneous
first-two deficits. Thus (7) holds over the full real color square
for these choices too. This is a separate complete finite-source
input, not a continuation of the near-complete asymptotic or an
application of an unselected-height cap estimate at a changed height.

For the resulting joined restricted sum, its
uniform strict sector gaps and the original unselected real-color
gap give a real outside-color gap by the triangle inequality.
The degree bound and the unchanged local packet then give a fixed
quadratic complex-strip bound by the
[open-source stability lemma](research_mixed_open_source_stability_reduction.md),
Section 1. This applies only to the explicitly joined restricted sum.

## 3. What the endpoint completions cover

All four last-two patterns are available for suffix (1).
After the disjoint joining, the remaining
plateau selections for \(m\ge11\) must meet
\[
                    \{3,4,5\}\cup\{m-4,m-3\}.
 \tag{8}
\]
Only type-four positions can be selected. Every combination meeting
(8), including overlapping selected runs and combinations with the
treated positions, must still be controlled; singleton checks do not
settle those combinations. The third-position parameter cover is
still partial, as recorded in
[its uniform-pass outcome](research_mixed_third_selected_centered_product_boundary_attempt.md).

There are also genuine type and short-length qualifications. For a
general ending, a selected penultimate type four followed by an
unselected own-three ordinary factor is not (1) and is not proved
by the present two-own-four reduction. Last-only selection with a
type-three incoming coordinate is already covered by the separate
[type-three-input completion](research_mixed_terminal_three_input_kernel_completion.md).
At \(m=4,5\), the first-two and last-two windows overlap in
ordinary factors, so Lemma 1 supplies no joint multiplication rule.
Their remaining combinations, and other shorter words, require their
appropriate complete source arguments. They cannot be omitted merely
because there are finitely many such words.

Even a proof of every plateau selection would leave real targets
outside \(P\), their hybrid height-reset and transition regions,
and the associated outer-cycle joins. The
[contracted collar theorem](research_mixed_contracted_boundary_collar_completion.md)
currently permits arbitrary hybrid states only between two safe
unselected plateau blocks of 711 symbols. The boundary-side regions
remain in their specified plateau configurations, with the separate
allowed first-collar and terminal modifications. Defects entering
those blocks or unhandled physical boundary regions are not covered.
The exact reversal theorem transfers a whole source and a collar in
the opposite retained-leg chart; it does not identify missing localized
regions in the original chart.

## 4. The general closure reduction and the finite-exceptions target

The strongest available way to avoid unbounded boundary casework is
[the finite-boundary-window reduction](research_mixed_open_finite_boundary_windows.md).
It bounds the full boundary excess by a finite constant \(K\).
The occupation inequality then implies that every potentially
dangerous configuration has at most
\(\lfloor(K+\eta)/\kappa\rfloor\) bad symbols, with
\(\kappa=1/20000\). Sufficiently long safe intervals consequently
contain two long unselected plateau blocks. Relative triple pinning
reduces their remaining upper rate to two bounded-width *literal
boundary-source* functionals, with the exact tangents and vanishing
relative fees retained. Shorter words form bounded-length complete
source problems.

Thus a many-selected-or-long-buffer dichotomy is already justified
for the safe middle by occupation; it does not require inserting a
plateau-only selected loss into a nonplateau state. The unresolved
step is the calibrated sign and strict complementary loss of those
finite boundary functionals over all their boundary states. A large
norm ceiling is useful for finding the buffers, but cannot replace
that sign. The fixed 711-block theorem proves special boundary data,
not every boundary functional in the general reduction. The required
estimates are uniform in the level, not checks at finitely many levels.

For a complete mixed path source it is enough to prove: (i) the full
complement is exponentially smaller than the geometric packet on a
fixed complex color neighborhood; and (ii) the whole polynomial has
a strict gap outside a small real color neighborhood at the same
calibrated action. The open-source stability lemma then supplies the
quadratic strip estimate. The original positive three/four
[marked geometric germ](research_mixed_geometric_boundary_germ.md)
is already proved, so it is not an additional missing local premise.

Finally, even a complete positive three/four path theorem would not
prove arbitrary short-partial-filling stability. Other fixed short
powers and mixed signs, branching components outside the proved
degree/power criteria, and the original normal and complementary
terms still matter. The
[germ/turn theorem](research_source_germ_truncation_and_turn_remainders.md)
shows why logarithmic local Taylor data alone do not close this gap:
the original turn can promote an input-chart-small remainder to the
leading exponential scale. What is needed is an estimate on the
complement *after* the actual short operation, with a nonzero output
packet at its calibrated geometric action, including every cross-term
at a branch.

Once that stability holds under all required fixed partial fillings,
the [finite-branching lemma](research_finite_exceptions_under_partial_fillings.md)
gives cofiniteness for a fixed template. Intermediate nonhyperbolic
exteriors cannot simply be discarded when their later fillings can
still lie in the final hyperbolic-knot domain. The
[original padding equivalence](research_original_tree_padding_equivalence.md)
must still be respected: one exceptional represented hyperbolic core
can recur on infinitely many assignments of a larger fixed template.
An untreated finite list of cores therefore cannot be substituted for
a finite list of exceptional assignments.
