# Complementary color estimates and classical Conway fillings

The two companion papers separate an analytic estimate from a geometric
construction. Their [source snapshot](conway-source-filling-audit-snapshot.json)
records the versions read and the finite and formal checks. The frozen
reference manuscript remains unchanged; its corrected filling Jacobian
is recorded in the [errata](../manuscript/ERRATA.md).

| Paper | Proved conclusion | Additional input for a quantum volume limit |
| --- | --- | --- |
| [Complementary color bounds for Conway tangle sources](../papers/conway-source-bounds/main.tex) | A strict uniform bound for the sum of all sectors containing a complementary term, and for the entire source when a physical color stays away from complete color. | The exact filling transformation and a nonzero asymptotic for the remaining contribution. |
| [Marked deformations and long fillings of Conway closures](../papers/conway-fillings/main.tex) | The actual nearby framed representations, independently long primitive fillings, and their absolute hyperbolic volume. | Identification of the endpoint-normalized quantum action with the classical cell potential. |

Both papers retain the completed/completed closing grammar. Neither
silently imports a later extension to arbitrary strict tangle expressions.
Their proofs were read in full, including the quoted companion statements
and the finite arithmetic used in the first paper. The comparison with
the quantum action remains a distinct dependency in the graph.

## The source estimate

The finite formulas are imported from the Newton companion by proposition
and equation number. They retain the complete polynomial quotient,
including derivatives at repeated roots. The high-color core is separated
from its exact complementary polynomial before the retained half twist
acts. Low colors have zero core. After a half twist the complementary
polynomial can occupy every Newton index, so the comparison uses the
whole multiplication polytope.

The signed core is handled before taking absolute values. Its finite
telescoping identity has a zero lower boundary term and an upper boundary
term that vanishes after the factorial cancellations. This includes the
case in which an uncanceled ratio would be undefined. The terminal value
has modulus one at odd levels and a cosine at even levels.

The matrix estimate bounds both characteristic roots. It uses
Cayley–Hamilton on a fixed block, then approximates each slowly varying
block by its frozen matrix power. The block length is chosen before the
level tends to infinity. Root collisions cause no singular eigenvector
change. A separate factorial bound controls the lower endpoint. The
conclusion has a uniform error tending to zero in the exponential rate;
it does not assert a polynomial prefactor at a collision.

Two local comparisons supply a strict loss. The two-leaf comparison
retains its original multiplication gate. The single-attachment comparison
retains the entire completed child and its boundary tangent. In the latter
case the inequalities for the child and the parent are used separately
to bound the two slopes. Rational supporting planes cover their complete
domains. The arithmetic proof explains the outward enclosures for sine,
logarithm and the log-sine integral, and the recursive rectangle cover.

Propagation adds the supporting planes at the same stationary state, so
internal linear terms cancel. A turn and the closing trace keep the exact
shift by one quantum index; it costs only a bounded factor. Every nonempty
complementary subset inherits a positive loss. Summing all such subsets
proves the bound for the entire difference of sources. A separate
compactness argument and the strict recurrence loss handle colors a fixed
fraction of the level away from complete color.

The certificate wrapper checks the 288 two-leaf inequalities, 880
single-attachment inequalities and the elementary rational leaf margin.
It records source hashes and removes a stale success summary before
rejecting optimized Python execution. These finite calculations do not
replace the recurrence estimate or the induction for arbitrary level.

## The classical filling construction

The classical potential is defined directly from the log-sine cell
functions and the shear determined by each retained half twist. The
complete internal Hessian gives its stationary continuation. Mixed
internal/auxiliary derivatives vanish at completeness, so eliminating the
internal variables leaves the stated diagonal auxiliary Hessian unchanged.
Differentiating the primitive longitude logarithms gives the corrected
factor in the filling Jacobian.

The face maps are rational identities in independent phase variables.
Continuing those identities retains the full maps, rather than only their
cross ratios or traces. Their edge returns give a representation of the
original group. Compatible subdivisions are chosen after assembly in one
complete half-polyhedron and copied to the other. White face pairings
preserve those subdivisions; shaded half-twist faces are already triangles.
The retained tetrahedra stay positive nearby.

The actual peripheral words determine the similarity logarithms. Main
meridians remain nonidentity parabolics, and their commuting longitudes
remain translations. At the auxiliary cusps, the primitive filling
equations are solved in one polydisk of reciprocal slopes. Separate
evenness of the potential gives a direct positive formula for the real
longitude logarithm, valid for either sign and without a ratio restriction
on the slopes.

The application checks the hypotheses of the marked-filling companion's
metric completion theorem. Its logarithmic link calculation identifies
the actual small periods before multiplication by a large slope. The
filled meridian therefore winds once. Adding the axis produces the
original smooth solid torus, while the main cusps remain complete.

The volume calculation uses the Conway potential's differential
one-half times the sum of longitude logarithm times meridian differential.
The opposite polarization in the marked-filling companion requires a
different boundary correction. The complete cell volumes fix the
integration constant. Finally the boundary homotopy retains the original
fundamental chain and has vanishing cusp volume, so its corrected action
equals the absolute volume of the completed metric.

The symbolic checker tests flags, peripheral multipliers, the shear
Hessian, the signed longitude formula and the critical boundary term.
Its deliberately incorrect variants test the factor and sign conventions.
It does not prove metric completeness or the fundamental-chain comparison.

## Formal linear algebra and remaining scope

[GroundedLaplacian.lean](../formal-real/GroundedLaplacian.lean) defines the
actual reduced graph matrix and proves that its quadratic form is the
full edge energy after zero extension at the grounded vertex. Nonnegative
weights and positive-edge connectivity imply a zero kernel. Finite
dimensionality gives an inverse, a nonzero determinant, and a unique
grounded solution for every right-hand side on the other vertices.
The equation at the grounded vertex is not imposed; the result includes
the graph with only one vertex.

The optional formal package now contains 24 definitions and 92 theorems.
All 116 declarations are included in its axiom audit, with nine dependency
pins and eighteen rejected negative controls. The completed execution was
retained after matching all 32 source hashes. This module does not identify
a geometric Hessian, bound an inverse uniformly, or formalize the nonlinear
implicit-function and metric construction arguments.

The new papers do not finish the extraction of the reference manuscript.
The completed-root nonzero local expansion and full oscillatory filling
sum still need their own complete account. The quantitative circle-tree
estimates, broader strict-tangle extensions and moving-longitude results
also remain separate work. The dependency graph records those obligations
without treating a new upper bound or a classical metric as a proof of
the whole quantum limit.
