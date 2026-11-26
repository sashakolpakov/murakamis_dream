# Semantic check of the triangular-boundary scalar module

The files read were the current public-staging copies of
formal/VolumeLogic/TriangularBoundary.lean and its imported
formal/VolumeLogic/ProtectedSum.lean. This is a mathematical binding
check of the nine new theorem statements and their use of the existing
sector definitions. It is not a new kernel execution.

## Binding to the written proof

The Lean variables have the following meanings:

| Lean variable | Mathematical quantity |
|---|---|
| a, c | \(\log a,\log c\), the two retained ordinary middle log weights |
| b | \(\log b\), the common boundary log weight |
| t | \(2T\), twice the removed triangle potential |
| qa, qc | \(2Q_a,2Q_c\), twice the retained triangle potentials |
| rest1, rest2 | Twice the sums of all nonroot input local rates |
| target1, target2 | Twice the complete core and comparison-block target sums |
| phi1, phi2 | \(2\Phi_D,2\Phi_B\) |
| gap1, gap2 | Twice the respective available witness gaps |

Thus \(t-b=2T-\log b=\Delta\) is **undoubled**. A defect of
\(t-b\) in a doubled local rate is exactly the allowed
\(\Delta/2\) in the ordinary rate.

The imported bridge definitions are precisely
\[
2X_{\mathrm{new}}=qa+qc,\quad
2A_{{\mathrm{new}},L}=\max(2c,qa+c),\quad
2A_{{\mathrm{new}},R}=\max(2a,qc+a).
\]
Substituting \(t\) for the singleton parameter of the old protected
definitions gives the correct original core and block rates:
central \(t+qc\), \(qa+t\); left core
\(\max(2c,t+c)\); right block \(\max(2a,t+a)\).
It does not assert that the removed triangle is a singleton.

## Each theorem's role

1. boundary_left_with_defect bounds both branches of the left maximum
   under \(t\le qa+\mathrm{defect}\) and nonnegative defect.
2. boundary_right_with_defect gives the separately checked right version.
3. boundary_bridge_with_defect uses
   \(b\le t,qa,qc\), the simplex-vertex bounds, to choose defect
   \(t-b\) for all three labels. This has exactly the doubled scaling
   above.
4. boundary_bridge_central_block excludes the right output through
   protectedSecondSide=false and uses \(t\le qa\) only for the left
   case. It requires no comparison with qc.
5. boundary_total_with_defect subtracts
   \(target1+target2-2b\), so the ordinary common-boundary target is
   counted once. The result is a loss \(t-b=\Delta\) in doubled
   costs, equivalently \(\Delta/2\).
6. boundary_total_central_block gives the sharp loss \(2(t-b)=2\Delta\)
   in doubled costs.
7. boundary_conditional_action_cancels cancels the doubled conditional
   addition \(2\Delta\) against precisely that sharp target-corrected
   subtraction.
8. boundary_noncentral_block_margin retains the extra \(t-b\) loss.
   Its standalone conclusion does not itself need to discard that
   quantity. Nonnegativity follows from ht in its intended application.
9. boundary_certified_rate splits on the entire block Boolean
   \[
   outsideSecond\ \lor\ protectedSecondSide(s).
   \]
   It does not split on the root alone. A locally central root with a
   noncentral spectator is correctly placed in the noncentral-block
   branch. When the whole block is central, the imported sector-map
   theorem and the output noncentral assumption force the whole core
   to be noncentral. The conditional packing bound and the conditional
   triangle comparison are used only in this branch.

The duplicate target is correctly \(2b=2\log b\), not \(2t=4T\).
Replacing one by the other would eliminate the essential geometric
correction and would not match the source extraction.

## Hypotheses that remain mathematical inputs

The formal final inequality does not require positive gaps, because the
ordered-ring inequality is valid for arbitrary gap values. A strict
source conclusion additionally uses the positive certificate gaps
proved in the written argument. The written construction supplies
coreUpper by choosing either a complete minimizer or a noncentral
witness with a positive gap.

The module does not prove the local spectral-envelope estimates, the
finite shared coefficient identity, the zero-boundary certificate
extension, the disk pressure identity, the Soddy comparison, or the
primitive filling and metric-volume theorem. It checks the scalar
case split and exact target correction once those inputs are supplied.
The Boolean correspondence to whole source strings is provided by the
written sector map; the old imported sector-map lemma verifies that
one induced input is active.

No scaling or binding discrepancy was found in these nine statements.
No Lean source was edited in this check.
