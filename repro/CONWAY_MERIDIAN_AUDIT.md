# Complete Conway geometry and moving-meridian tangle formulas

This record accompanies two papers extracted from the frozen reference
account. The [snapshot](conway-meridian-audit-snapshot.json) records the
versions read and the executed checks. The papers have different
conclusions and neither asserts a new signed filling asymptotic.

| Paper | Conclusion | Further input needed for a filled-invariant volume limit |
| --- | --- | --- |
| [Pyramids, prisms, and complete geometry of Conway closures](../papers/conway-geometry/main.tex) | A complete metric on the augmented complement specified by the completed-root grammar, its absolute volume, and its primitive crossing-circle curves. The positive complete source has that volume rate. | Signed-source estimates, a nonzero whole filling asymptotic and the marked deformation after filling. |
| [Exact Newton calculus for tangles with a moving meridian](../papers/meridian-tangles/main.tex) | The physical partial trace, six oriented turns, crossing polynomials with all repeated-root data, and the entire finite tree contraction. | Uniform estimates for that entire contraction and the geometric interpretation of its selected action. |

## The complete geometric construction

The reading covered all four TeX sources: the cells and theorem in
`main.tex`, convex assembly and the literal projection cut in
`assembly.tex`, the entire face maps in `maps.tex`, and the cusp,
peripheral and connectivity proofs in `completion.tex`.

The positive source supplies the stationary point through Proposition
5.3 of the Newton paper. Its Corollary 5.4 supplies the positive-source
limit; Lemma 6.1 gives the stationary leaf interval. Those three uses
are separate. The geometric construction does not assume a quantum
asymptotic or import a filled-volume theorem.

The local calculations were checked directly. A leaf splits into two
positive tetrahedra. For the prism, the sine rule places the extra
vertex beyond the two specified chords. Its three tetrahedral volume
terms reduce to the product action. The cross-ratios of the entire
ordered input and output quadrilaterals are the exponentials of the
appropriate action derivatives. The stack assignments invert the input
cross-ratios; the full reversal at closure preserves the output one.
Thus the stationary equations give the required whole-face isometries.

The global argument retains several obligations that a local angle
calculation would not settle. Successive attachments remain convex by
the local-convexity and shortest-path argument. The other input face
stays supported after the first child is attached. Original terminals
are consumed in disjoint pairs, so a leaf's shaded triangles do not
collapse. The cyclic boundary orders recover every white-face walk of
the actual projection cut. The entire face maps agree across each
prism, turn and closure; their edge words have identity return.
Finally a common normalization of shaded horocycle segments is
preserved by every pairing, proving cusp completeness without dilation.

The peripheral calculation traces the original curves before evaluating
their matrices. The pure and odd meridian translations and disk
longitude span a parallelogram with the same area as the full cusp.
This proves index one, rather than only showing that the curves commute.
The equality of absolute volumes follows by summing the actual metric
cells, with their fixed tetrahedron-volume normalization.

Two corrections arose during reading. The three interior dihedral
angles at a trivalent ideal vertex sum to pi, not twice pi; the displayed
angles already had the correct sum. Also the positive-source corollary
now states eventual positivity. The source can vanish at a small level,
so positivity at every level was not justified. Both corrections leave
the geometric theorem and the all-sufficiently-large-level limit intact.

The four native illustrations show the ordered tangle operations, the
leaf pyramid, the exact prism boundary construction and the two-rectangle
cusp lattice. The last diagram distinguishes meridian vectors belonging
to different half-twist partners; half a longitude is not asserted to
be an integral curve on the pure cusp.

## The moving-meridian formulas

The algebra starts from the physical matrices at fixed quantum level.
A polynomial residue identity alone would not identify the physical
partial trace. The proof first computes its moments and only then
obtains the top-coefficient functional. The middle total-degree space
generates the entire pair, and its Casimir is cyclic. This proves the
pointwise polynomial commutant even at the additional colliding roots;
constant dimension is not inferred merely from the complete parameter.

The fixed Newton pairing stays anti-diagonal because changing the
spectral polynomial changes only its constant term. The polynomial
quotient in dividing a product of two basis elements has degree at
most N minus two, so that change cannot affect its highest remainder
coefficient. This also gives a holomorphic coefficient extractor.

The physical turn is checked on the full three-strand intertwiner
space. Its calculation retains the endpoint change of basis and the
last-column term of the conjugated Casimir. The endpoint factors cancel
only after both ends have been placed in the same gauge. The proof of
the complete conjugation now checks the exceptional corner entry
directly, where clearing an entry-ratio denominator would not suffice.
The other orientations are obtained with their actual carriers and
monodromy scalar. No derivative at a repeated pair root is discarded.

The crossing formulas specify every normal at the collisions s = 0 and
s = plus or minus one half. Inverse powers use the full quotient unit.
The tree formula pairs covariant legs with H divided by W, sums all
indices and keeps the single physical closing factor H. Changing the
order of contraction preserves the original physical turns; it does
not assign a fresh forward-turn scalar to a reversed edge. The final
quadratic scalar includes negative mixed words and the actual writhe.

The standard nilpotent ribbon-tangle framework remains a literature
input. This extraction does not audit every categorical assertion in
those sources. Its physical normalization, moment, duality, turn and
contraction formulas are proved in the paper. The comparison with the
original Kashaev normalization imports Theorem 10.1 of the finite
spectral paper at N at least three. The finite algebra itself holds
from N = 2. The Newton paper's introduction now states that same scope
for its imported comparison; no finite identity or limit was changed.

## What the formal proof adds

[GroundedConvexity.lean](../formal-real/GroundedConvexity.lean) adds three
definitions and eight theorems. For an actual potential it constructs
the affine segment between two grounded vectors and its one-variable
restriction. Actual first derivatives and an identity for the second
derivative as connected weighted graph energy imply strict convexity.
The module derives the strict Jensen inequality and uniqueness of a
grounded minimum. Combining it with the existing transport coercivity
theorem gives an existing, unique minimum of the same constructed
potential.

The geometric derivative identity, conductance signs and graph
identification remain written inputs. So do feasibility of the positive
transport table and the substitution that pools three fixed boundary
columns. The transport incidence graph and Hessian graph need their
own connectedness hypotheses; the module does not identify them without
proof. It establishes neither geometric development nor smooth
dependence on boundary parameters.

The optional package compiled twenty definitions and seventy-four
theorems, with all ninety-four declarations included in its axiom audit.
The nine dependency pins were unchanged and sixteen negative controls
were rejected. The completed execution was retained only after comparing
all thirty-one recorded source hashes with the publication sources.

## Finite checks and references

The consolidated runner has twelve groups. The new geometry group
checks rational face maps in independent phase variables, all displayed
edge returns and complete peripheral translations, and finite endpoint
pairings. Its controls change a vertex order and an odd meridian. These
identities do not establish convexity, topology or completeness.
The moving-meridian group compares actual representation, crossing and
bending matrices at its explicitly listed finite levels and parameters.
It supplements the written all-level identities; it is not their proof.

The literature check concerns the construction's background and coverage.
The decomposition of fully augmented links and the role of half twists
are described in [Purcell's exposition](https://users.monash.edu.au/~jpurcell/papers/expos-auglinks.pdf).
[Rivin's variational work](https://annals.math.princeton.edu/1994/139-3/p02)
provides the geometric context. The quantum background is referenced to
Akutsu–Deguchi–Ohtsuki, the
[unrolled representation account](https://arxiv.org/abs/1406.0410v3), and
[Geer–Patureau-Mirand–Turaev](https://arxiv.org/abs/0711.4229).
The two papers state their particular ordered constructions and finite
calculations; no novelty claim is based merely on using a polyhedral
decomposition or a nilpotent representation.
