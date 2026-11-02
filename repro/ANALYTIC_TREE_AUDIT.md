# Conway and circle-tree asymptotics

This review concerns the two analytic companions extracted after the
finite tangle calculus, complementary-color bound and classical filling
papers. The reference manuscript and its PDF remain unchanged. The
accompanying `analytic-tree-audit-snapshot.json` records the sources and
the bounded checks for this publication.

## Completed Conway closures

[Holomorphic source asymptotics and volume limits for Conway closures](../papers/conway-asymptotics/main.tex)
uses the completed-root construction of the Newton companion. It does
not extend that grammar to every strict Conway tree. The original
endpoint pairing must give one knot; the independently signed filling
integers are fixed before the level grows.

The proof has four analytic steps.

1. A convergent Gamma product fixes the sine-factorial interpolation,
   its reflection, its marked phase and its constant. Summable Stirling
   remainders justify differentiation and contour estimates on fixed
   complex strips.
2. The signed leaf recurrence retains its actual terminal condition.
   Its vanishing final recurrence coefficient removes the artificial
   tail of a continued fraction at both parities. Euler summation with
   a growing truncation gives exponential interpolation accuracy before
   moving any wire contour. The primitive integer lattice and every
   fixed wire offset are retained in the Gaussian density.
3. A second finite sum produces an even Fourier polynomial. Its local
   action is real on real arguments, and an exact cotangent rectangle
   gives a strict bound over the rest of the shared spectral cube.
   Expanding each full physical integer crossing power makes the
   existing whole-sum filling theorem applicable with its stated
   hypotheses, also for odd and negative powers. The finite midpoint
   identity retains the first normal and the half multiplicity at zero.
4. The quantum leaf action agrees with the classical meridian shear.
   Equality of derivatives in the wire coordinate leaves a possible
   function of the color; evaluation at the actual terminal index fixes
   that function. Stationary elimination and the Legendre transform then
   identify the full critical action with the primitive geometric
   filling action, including its constant.

The finite checker independently forms the Newton crossing polynomial,
powers and inverts it by polynomial division, and compares it with
Fourier-Hermite reconstruction and midpoint folding. It uses two finite
fields for each level from 2 through 12: 154 signed integer-power cases
and 462 folded samples. These computations check finite formulas; the
all-level and analytic arguments are written proofs.

## The summed circle-tree condition

[Degree and twist estimates for circle-tree invariants](../papers/circle-tree-asymptotics/main.tex)
proves the entire invariant asymptotic under

\[
 \sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25}.
\]

Here the fixed literal tree has a crossing circle at every vertex,
degree (d_v), and signed physical crossing power (n_v). The original
strand connections must give one knot with no extra internal component.
A zero power is allowed at sufficiently high degree. The proof therefore
cannot be replaced by one requiring a long twist at every vertex.

The full-normal Newton bound controls discarded indices before complex
interpolation. The retained edge sum uses the same canonical factorial
lemma, with its midpoint shifts and nonzero amplitude. The exact angular
trace is expanded on a translated grid. Opposite charges pair to a
coefficient whose first value is exactly one at every parity. Infinite
tails are estimated with the other variables on real integrals or their
physical grids; they are not put on unrelated complex contours. A
separate simultaneous estimate retains the negative Fourier terms on
every connecting face.

The proof distinguishes errors with an additive loss from the complete
action and the relative asymptotic of the first charge. Its quantitative
budget puts all additive errors below that first critical value. The
positive-octahedra theorem supplies the actual smooth metric and its
absolute volume under a weaker geometric threshold. The two actions have
the same edge derivatives and the same complete constant.

The centered meridian theorem retains the exact quadratic framing factor
and the single closing factor. Its (N^{-1}) insertion is evaluated at
the filled edge shapes. The ordinary first Gaussian correction cancels
between numerator and denominator, giving the claimed uniform
(O(N^{-2})) remainder. This is a bounded microscopic meridian theorem;
the preferred-longitude identity and all-orders operator conclusions are
separate results.

The paper's checker verifies four symbolic edge identities, fifteen
outward rational budgets and 990 finite complex-product samples. Its
arctangent and hyperbolic-series bounds retain explicit remainders.
Two negative controls reject altered budget comparisons. The samples
are supplementary to the written uniform estimates.

## Formal differentiation and what remains written

[TriangleLoads.lean](../formal-real/TriangleLoads.lean) proves the
directional derivatives of the actual exponential-weight arctangent
loads. It derives the conductances rather than assuming a Hessian
identity. The pairing is the explicit three-edge energy; assembly uses
one common value at each shared vertex and keeps parallel edges. The
positive-radicand hypothesis includes one-zero triangles. Singleton
loads are separately constant.

The optional real-analysis package now contains 34 definitions and
116 theorems. All 150 declarations are covered by the axiom audit;
20 negative controls and nine dependency pins are checked. The new
module has ten definitions and 24 theorems. The existing six modules,
toolchain and dependency manifest were retained.

Identifying the loads with the gradient of the geometric entropy
potential remains a written input, as do geometric support and
connectivity. The new analytic papers are not formalized contour proofs.
The Lean implication layer does not replace their exact invariant
identification, nonzero asymptotic, full remainder estimate or geometric
volume calculation.

## Remaining extraction

The broader strict-tree construction requires its own normal-form,
boundary-profile, quarter-index and marked-geometry arguments. The
local and directed circle-tree criteria require their additional
conditional subtree estimates. The all-orders moving-meridian,
preferred-longitude and classical-symbol conclusions remain separate
papers. None is inferred from the two narrower companions reviewed here.
