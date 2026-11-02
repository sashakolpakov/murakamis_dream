# Strict Conway compositions: proof dependencies and consolidation

This record accompanies the separation of the strict Conway argument into
variational, source-estimate, geometric and asymptotic results. The frozen
374-page reference manuscript is unchanged. The purpose is to make each
import explicit and remove repeated arguments from the route to a volume
limit. The broader moving-meridian and longitude results are separate
extraction tasks.

## The variational result

[Stationary profiles of strict Newton trees](../papers/strict-newton-profiles/main.tex)
is a 14-page account of the finite supports and the positive action.
Strictness refers to the original ordered expression: every leaf index
lies strictly between zero and one half, and every retained product lies
in the interior of its allowed region. The forced closing product is
removed while its complementary-index relation is kept.

The exact support calculation supplies the primitive integer lattice.
The proof then excludes a maximum on every boundary face, rather than
inferring interior existence from a negative Hessian. The strictly
concave action has a unique interior maximum. Fixed-output versions give
boundary profiles, whose constants are retained through their harmonic
addition rule. The same paper proves the elementary positive-sum limit.
It does not use a signed quantum asymptotic or a global hyperbolic metric.

An earlier draft also contained an application to signed core asymptotics.
That section has been removed from this paper. It created an unnecessary
import from source estimates, while the source estimates need the
variational profiles. The classical proof now has only finite-algebra
and factorial inputs. The signed application is preserved in the research
material, rather than being made a prerequisite of its own input.

The support review also corrected a statement in the older
[single-leaf composition note](../notes/actual_conway_single_leaf_source_composition.md).
At odd level \(N=2m+1\), the product of two turned pure leaves forces
both input indices to equal \(m\), but its output occupies every index
from \(m\) to \(2m\). It is not supported only at the last index.
The reference manuscript and earlier Newton paper state only that this
case is confined to boundary inputs; they need no correction on this point.

## Bounds for the whole source

The existing paper has been expanded to
[Spectral estimates for Conway tangle sources](../papers/conway-source-bounds/main.tex),
28 pages. A separate overlapping source draft has been consolidated into
it. Proposition 3.1 and equation (3.16), concerning local signed
coefficients, retain their numbering and proof. Lemmas 4.1 and 5.1 retain
the two rational supporting-plane inequalities. The attachment lemma now
states all its scalar parameter restrictions explicitly.

The new global proof has a different dependency chain from the older
completed-root induction. It first proves a polynomial conditioning bound
for the complete spectral algebra, keeping values and first derivatives
at repeated roots. Its exact Fourier formula includes the derivative
terms, the missing winding term, and the endpoint currents. This gives
the physical-color loss for a circle followed by a turn. A positive
comparison for products between those turns keeps all shared indices.
The supporting-plane inequalities and the absolute profiles then
propagate the estimates to the original closed expression.

Theorem 1.1 gives the whole-source upper rate, a strict loss when a color
stays a fixed fraction below the level, and a bound for the entire
difference between the full source and its core. It covers strict
expressions with at least three leaves and every retained sign.
Corollary 9.1 proves the two-leaf case separately. Its actual finite
source is a pairing of two decorated circle polynomials; its pure rate
is the maximum of twice the leaf action. It is not obtained by silently
extending the hypothesis of Theorem 1.1.

The old open-output Proposition 6.1 is no longer a separate export.
The new array comparison in Theorem 8.2 is used in the global proof, but
is not declared to be the identical statement with a new number. The one
asymptotics-paper citation to the old proof has been replaced by the
needed concavity argument. The new global source proof imports neither
a circle-tree volume theorem nor the signed local recurrence.

The finite replay retains the two supporting-plane certificates and adds
exact quotient-versus-Fourier comparisons, chirp normals, endpoint
repairs and examples invisible to values alone. These checks test the
finite identities. The uniform contour estimates and the comparison
induction remain written proofs.

## The original marked geometry

[Marked geometry of strict Conway compositions](../papers/strict-conway-geometry/main.tex)
is a 17-page classical argument. Four boundary-edge labels record the
individual shaded faces already attached. Their induction proves convex
assembly for every strict expression, including an elementary or turned
closing child. The proof identifies the result with the literal
projection cut, checks full face maps and returns around edges, and
constructs compatible cusp decorations.

The deformation proof retains the original disk meridian and primitive
longitude. Every main cusp stays parabolic. The local face-map and
peripheral calculations are imported from the earlier geometric papers;
their restricted global assembly theorem is not applied to the enlarged
class. The general metric-completion proposition is used only after its
positivity, marking, small-logarithm and unfilled-cusp hypotheses are
verified. A comparison of the same oriented fundamental chain fixes the
absolute volume constant.

The primitive cusp ratio and the filling Jacobian are
\[
 \tau_i=\frac{2ic_i}{1-\epsilon_iic_i},\qquad
 \Phi_{\chi_i\chi_j}(0)=\pi i\tau_i\delta_{ij},\qquad
 DV(0)=-2\pi i\operatorname{diag}(\tau_i).
\]
The older [general-mask note](../notes/actual_conway_general_mask_marked_filling.md)
used a half-sized ratio and a compensating factor in the Jacobian. Its
notation has been corrected to the primitive ratio. The new paper uses
the primitive convention throughout; the existing reference erratum is
unchanged.

The geometric theorem has no quantum asymptotic premise. Its finite
checks cover boundary labels, endpoint pairings and projective
identities. They do not prove convexity, smooth completion or the
absolute volume comparison by sampling.

## The pure source in the volume argument

The revised [20-page asymptotics paper](../papers/conway-asymptotics/main.tex)
uses the full physical
crossing power at each original disk. Its exact expansion in ordinary
colored circles applies to negative and odd powers and retains every
first normal at a repeated root. It permits the analytic calculation to
use the pure source even when the actual knot has odd crossing powers.
This is an algebraic identity inside the original diagram, with the same
reduced cut and framing.

For the pure source, the canonical factorial continuation agrees exactly
with the finite summand on the integer grid. Every strict leaf index is
regular, including one quarter. The primitive lattice and strict Hessian
give the nonzero local Gaussian coefficient. A second finite Fourier
calculation proves a real local phase and a bound on the shared Fourier
polynomial away from zero. These are the hypotheses of the whole-period
filling theorem. The polynomial cost of the exact crossing expansion
keeps the original physical error exponentially smaller after sufficiently
long fixed fillings.

The final geometric comparison uses the actual retained half twist and
an integer primitive slope. An explicit classical shear and Legendre
calculation identify the two actions with their constants. It does not
replace odd powers by half-integral surgery on a different augmented
partner. The signed coefficient expansion and the quarter-index theorem
remain useful separate results; they are not prerequisites of this pure
route. The knot expression and every twist integer are fixed before the
quantum level tends to infinity.

## The actual triangle minimum in Lean

[TriangleMinimizer.lean](../formal-real/TriangleMinimizer.lean) joins the
previous derivative, graph-energy and transport proofs for the actual
supported triangle potential. It proves a vertex lower bound and
multivariate continuity, aggregates a positive half-mass table of corner
loads, and turns its row paths into positive conductance paths. The
result is an attained, unique global minimum after one coordinate is
fixed. Coercivity, strict convexity and the Hessian identity are proved
for this function rather than supplied as assumptions.

Several corners may have the same destination. Their coefficients remain
separate; only the transport loads are aggregated. The prescribed demand
must equal the table's column sum only at free vertices. The difference
at the fixed vertex vanishes on the grounded subspace. Singleton rows,
loops and repeated edges are included.

The remaining application inputs are explicit: the geometric incidence
map, a strictly supported load table with the required columns, and its
row connectivity. The geometric Hall argument producing that table is
still written. The module does not formalize changing supports, nonlinear
deformation, circle development, contour estimates or metric completion.
The optional formal project now contains 48 definitions and 189 theorems.
All 237 declarations occur in the axiom audit, and 24 negative controls
are retained. The saved replay pins all 35 inputs; the eight earlier
mathematical modules and dependency versions are unchanged.

## What the records establish

The [companion hash snapshot](strict-conway-audit-snapshot.json) identifies the source versions read and the
executed finite and formal checks. The paper builds check page limits,
references and typesetting. The dependency graph checks the declared
logical imports. Neither process proves the mathematical statements at
its vertices. The bounded reading records distinguish a full read of an
argument from a check of its interfaces or later editorial changes.

This consolidation covers the complete-meridian strict volume route.
Net-twist and zero-twist topological reductions, all-orders meridian
expansions and preferred-longitude results retain their separate research
accounts. They are not consequences of a leading complete-meridian
asymptotic alone. The unrestricted remainder estimate for general
matched diagrams remains outside the restricted theorem.
