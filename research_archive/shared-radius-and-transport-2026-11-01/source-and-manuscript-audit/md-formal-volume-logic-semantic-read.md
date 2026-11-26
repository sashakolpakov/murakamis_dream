# Semantic read of the finite Lean kernels

This read covers the working-tree versions of
formal/VolumeLogic/FiniteSupport.lean,
formal/VolumeLogic/FiniteAlgebra.lean,
formal/VolumeLogic/RateComparison.lean, and formal/README.md.
The accompanying manifest records their hashes. It includes the two
new strict-gap wrapper theorems. I did not rerun Lean or the axiom
inspection. No public files were edited.

## 1. Conclusion

The declarations correctly encode the finite implications they state.
I found no wrong parity cutoff, reversed product choice, lost sign in
the cleared Hermite formula, or vacuous hypothesis producing a false
mathematical conclusion.

The README accurately limits the formal result. It leaves the actual
source adapter, Chebyshev root data, analytic estimates, nonzero
contribution, primitive geometry and volume identity as written inputs.
It also distinguishes theorem parameters from trusted axioms. An
axiom scan is therefore not described as proving all the premises.

My initial read identified a description issue: the numerical margins
in nonempty_sector_gap and filled_rate_gap were not assumed positive,
although the prose discussed strict gaps. Their algebraic conclusions
were valid. The author has now added sector_strictly_below and
filled_remainder_strictly_below with explicit positive-margin
hypotheses, and clarified the README. These additions resolve the
issue. The README also now separates the analytic range \(0<t<1\)
from the weaker \(t\ge0\) needed by the scalar flattening comparison.

## 2. FiniteSupport

three_supports uses the genuine middle powers \(i,t\) and the total
support \(i+t\le N-1\). It exhausts the central and two one-sided
regions and proves that the two strict one-sided alternatives do not
overlap. Its additional validity at small nonphysical natural-number
values is harmless.

left_endpoint_cutoff assumes \(N\ge2\) and \(j<N\), so natural
subtraction \(N-1-j\) is the actual complementary degree. It correctly
identifies the left range \(j<\lfloor N/2\rfloor\).
central_endpoint_even gives \(i<m,\ j\ge m\) at \(N=2m\).
central_endpoint_odd gives \(i\le m,\ j\ge m\) at \(N=2m+1\).
Thus the odd middle row is assigned to the central piece, as required
by the original numerator decomposition.

protected_moment_degree retains
\(M=\lfloor N/2\rfloor-1\) and proves \(i+j\le N-2\).
This is only a finite degree bound. It does not prove moment
positivity, an inverse-Gram estimate, or a protected source theorem.
The README does not claim those conclusions.

## 3. FiniteAlgebra

horner uses ascending coefficients. The recurrence for
dividedDifference gives, for example,
\(a_1+a_2(z+w)\) from \(a_0+a_1z+a_2z^2\).
The difference identity holds in arbitrary commutative rings,
including rings with nilpotents, without dividing by \(z-w\).
annihilating_root_identity correctly adds the explicit polynomial-root
hypothesis. This is the scalar algebra behind a resolvent numerator;
it is not yet a quotient trace theorem or a physical matrix adapter.

double_root_jet_identity substitutes
\[
 v_0=h_0q,\qquad v_1=h_0p+h_1q
\]
and proves the denominator-cleared formula for \(f_0p+f_1q\).
It retains the nilpotent term \(f_1q\). The actual Hermite application
still needs the Chebyshev values of \(h_0,h_1\) and \(h_0\ne0\)
before division. The README states this separation.

nonemptySecondChoices has exactly the required recursion: select the
first entry now and a second one later, or select the second entry
now and any suffix. Hence tensor_grid_subtraction removes precisely
the all-evaluation term. Repeated equal entries in a list still count
as distinct coordinates, as the tensor application requires.

productDifference telescopes as
\[
 (a-b)\prod a_{\mathrm{tail}}
 +b\left(\prod a_{\mathrm{tail}}-\prod b_{\mathrm{tail}}\right).
\]
It never divides by a potentially zero factor. The commutative-ring
setting is appropriate for scalar source coefficients and makes no
claim that neighboring physical crossing matrices commute.

## 4. RateComparison, including the new wrappers

doubled_flattening_gain reduces to
\(t(h-t\,\mathrm{energy})\ge0\).
Its hypotheses are exactly sufficient for that implication.
It does not establish the preceding entropy or Hessian estimates.
strict_weak_balance_gain adds \(t>0\) and \(h>0\); the doubled
gain is at least \(th>0\), so this is a genuine strict conclusion.

total_nonnegative and nonempty_sector_gap correctly preserve a
supplied numerical margin after adding nonnegative losses.
sector_strictly_below now adds \(0<\mathrm{gap}\) and concludes
strictly below \(\phi\), with the desired nonempty-sector semantics.

filled_rate_gap combines
\[
 2\,\mathrm{actionDrop}<\mathrm{sourceGap},\qquad
 \phi-\mathrm{actionDrop}\le\mathrm{filledRate}
\]
to obtain
\[
 2(\phi-\mathrm{sourceGap})
       <2\,\mathrm{filledRate}-\mathrm{sourceGap}.
\]
The new filled_remainder_strictly_below explicitly assumes
\(\mathrm{sourceGap}>0\), and correctly concludes
\(\phi-\mathrm{sourceGap}<\mathrm{filledRate}\).
No source exponential bound, nonzero leading term, or geometric
calibration is hidden as a conclusion of this scalar algebra.

## 5. Remaining formalization boundary

These kernels guard meaningful finite steps: natural-number cutoffs,
normal terms, tensor subtraction and scalar budget arithmetic.
Their compilation does not by itself verify the enclosing analytic
or topological arguments.

The next connected step identified by the README is appropriate:
define the polynomial quotient and top-coefficient trace, prove
\(\tau(FV)=F(\Omega)\), derive the local Hermite formula, and connect
it to the actual crossing jets. This would link the existing divided
difference and cleared jet identities to Appendix N's finite functional.

The review is semantic and read-only. The author's reported Lean
compilation and axiom inspection were not repeated, and no finite
experimental result is used as a proof of an analytic input.
