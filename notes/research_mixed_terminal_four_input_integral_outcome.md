# Three uniform terminal main comparisons on the type-four input disk

Research result and remaining estimate, 6 November 2026.

The fixed [height-integral evaluation](research_mixed_terminal_four_input_integral_budget.md)
encloses all four prescribed main budgets. Three are strictly negative.
On the whole canonical input disk
\[
 D_4=\{|b-(3/10-13i/250)|\le8/125\},\qquad H=1/100,
 \tag{1}
\]
both complete selected-weight alternatives for terminal type three
have a uniform main-phase gap greater than \(1/400\). The forced
alternative for terminal type four has gap greater than \(1/150\).
The terminal-four factorial estimate remains inconclusive.

## 1. The literal comparison and its certified bounds

Keep the original phase, canonical reference, incoming complex affine
tangent, and selected-weight alternatives of
[the joint main comparison](research_mixed_terminal_joint_main_budget.md).
The incoming flag is \(\beta=1\), the terminal flag is
\(\epsilon\in\{0,1\}\), and \(\nu=1\) denotes the factorial
alternative while \(\nu=0\) denotes the forced alternative.
Both alternatives retain the full selected real interval
\(P=[.22,.45]\). The original ordinary and terminal optimizer barriers
are used only as established in the
[symmetric pair-cost theorem](research_mixed_terminal_symmetric_pair_costs.md).

Let \(D_{\epsilon,\nu}\) be that original defect at selected height
\(H\). Its supremum includes every original main target, with the
original internal reference heights. The exact rational upper bounds
in the [fixed evaluation record](../repro/results/research-mixed-terminal-four-input-integral-budget.json)
give the following conservative table:

| Terminal flag \(\epsilon\) | Alternative \(\nu\) | Saved budget is strictly below | Consequence |
|---:|---:|---:|---|
| 0 | 1 | \(-.003281\) | \(\sup D_{0,1}<-1/400\) |
| 0 | 0 | \(-.022498\) | \(\sup D_{0,0}<-1/400\) |
| 1 | 1 | \(.009908\) | no negative comparison from this bound |
| 1 | 0 | \(-.007431\) | \(\sup D_{1,0}<-1/150\) |

Each decimal in the third column is an exact terminating rational
rounded upward from its saved upper endpoint. The positive entry is
an upper estimate, not a positive value attained by an original
target or a counterexample to suppression.

The input-coordinate theorem covers the entire disk (1) with its
original logarithmic branches. The calculation uses its exact common
affine parameter and certified posterior errors, then integrates
interval ranges on sixteen closed height slabs per terminal type.
No parameter subdivision, new root, optimization, or original action
evaluation is involved. The three scalar costs have coefficients
\((2,\nu+1,(3+\epsilon)/2)\).

The evaluation record has SHA256
9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e.
Its exact fixed counts are 96 cotangent boxes, one exponential,
two cosines, two sines, five logarithms, and one \(\pi\) enclosure.
All four budgets are enclosed, and all input hashes are unchanged.

The standalone
[saved-data checker](../experiments/check_mixed_terminal_four_input_integral_budget.py)
reconstructs the common-parameter support witnesses, all 32 slab
weights, the 96 cotangent-endpoint recombinations, all eight scalar
gain functions and their clipped branches, and all four final sums.
Its [audit record](../repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json)
reports `passed` with 515 unchanged bindings and SHA256
cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3.
The analytic elementary endpoints are inherited from
the pinned interval run; the checker makes no analytic callback.

## 2. The unresolved bound and its identifiable loss

For the terminal-four factorial alternative, the saved decomposition
has the following approximate components, displayed only to locate
the loss:
\[
 \begin{array}{c|r}
 \text{term}&\text{saved upper, approximately}\\ \hline
 W-2\pi H&-.0362082171\\
 G_s&.0142153605\\
 G_{a,1}&.0194136726\\
 G_t&.0124867706\\ \hline
 \text{sum}&.0099075867
 \end{array}
 \tag{2}
\]
Thus the problem is not arithmetic failure: every prescribed quantity
is finite. The two largest gain bounds use incompatible extremes of
one common force parameter. Writing
\(\overline I_j=\int_0^1 I_j(\theta)\,d\theta\) and
\(\kappa=\pi\Delta>0\), the exact forces are
\[
 (A_s,A_{a,1},A_t)
   =\kappa(1-\overline I_s,
       3\overline I_a-\overline I_s-\overline I_t-1,
       -1-\overline I_t).
 \tag{3}
\]
The largest positive \(A_s\) uses a lower value of
\(\overline I_s\), while the most negative selected force uses
an upper value of the same quantity. Adding their independent gain
maxima discards this correlation. The
[shared-force vertex lemma](research_mixed_terminal_shared_force_vertices.md)
gives a fixed saved-only way to retain it. No sign from that new
criterion is asserted here.

## 3. Scope

These are uniform canonical main-phase comparisons on \(D_4\).
They retain the original incoming tangent and the complete selected
weight. They are not uniform bounds for all terminal contour
profiles or a complete finite-source theorem. The original
actual-reference, oriented-image and inverse-feasibility hypotheses
remain necessary when a separate finite-source result uses them.
No statement about the type-three external disk or a whole knot
invariant follows from this evaluation.
