# Marked geometry of strict Conway compositions

[Read the PDF](../../docs/papers/strict-conway-geometry.pdf) ·
[TeX source](main.tex) ·
[Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

This paper supplies the geometry used in the Conway volume proof. Start
with a fixed ordered recipe for stacking and turning two-strand tangles.
Every elementary piece contains a crossing circle bounding a disk pierced
by two strands. The recipe is strict when its real labels satisfy

\[
 0<a<1/2,\qquad x\longmapsto1-x,\qquad
 \max(x,y)<z<x+y<1,
\]

at leaves, turns and products respectively, with complementary output
labels at the final closure. A worked example and an endpoint diagram
explain these conventions in Section 1.

The paper constructs the complete hyperbolic exterior of this augmented
link. It then fills selected crossing circles along sufficiently long
signed integer slopes, leaving the main cusps complete. A meridian and
the longitude determined by the crossing disk form a primitive basis:
they generate the entire cusp lattice, rather than a proper sublattice.
This matters because a slope equation for a multiple of a meridian would
not establish smooth completion of the intended filling.

## Results and proof

| Result | What it establishes |
| --- | --- |
| Theorem 1.1, `sm:complete` | The complete augmented exterior, its primitive crossing-circle bases and its volume, equal to \(2\pi\) times the maximum of the real tangle action. |
| Theorem 1.2, `sm:marked-deformation` | A nearby family of representations of the same link group, with the prescribed face identifications, complete main cusps and explicitly calculated peripheral logarithms. |
| Theorem 1.3, `sm:fillings` | Independently sufficiently long signed fillings, smooth hyperbolic completion and the absolute critical-action formula for their volumes. |

The construction begins with ideal pyramids at leaves and ideal prisms
at products. Their vertices, faces, dihedral angles and volumes are
computed explicitly. Stationary equations match the ordered
quadrilateral faces. An induction records which of the four boundary
edges remain exposed; it proves that the resulting gluing realizes the
specified tangle recipe, including asymmetric boundary configurations.
Tracing the main strands determines whether the resulting link is a
knot. Components closed inside an intermediate tangle are included in
this test.

The next calculation gives the face isometries and the meridian and
longitude holonomies. Their logarithms are continued from zero at the
complete structure. The primitive filling equation records one angular
turn. Finally, a comparison of the oriented ideal cells with the metric
fundamental chain identifies the volume itself, including its additive
constant. This geometric argument does not assume a quantum asymptotic.

## Results used from other papers

The [Newton calculus paper](../newton-calculus/README.md) supplies the
strict-support test, unique stationary maximum, negative Hessian and
boundary-profile identities: Lemma 5.2, Theorem 6.4, Lemma 7.1 and
Proposition 7.2. The ideal-tetrahedron volume formula is stated in the
text with its flat limit and a reference to Milnor.

The [general circle-pattern paper](../marked-fillings/README.md)
supplies Proposition 6.1 on near-complete metric completion, equation
(7.3) for the volume differential in similarity-logarithm coordinates,
and Section 7.3 on the fundamental-chain comparison. The Conway paper
verifies the topology, face maps, positivity, primitive periods and
complete unfilled cusps required to apply those results. It does not
use the general paper's full matched-sphere construction as a substitute
for this verification.

The [Conway asymptotic paper](../conway-asymptotics/README.md) proves
that its quantum critical action is the classical action constructed
here. Neither paper asserts uniqueness on the whole character variety.

## Build and finite checks

From the repository root:

```sh
python3 tools/build_papers.py strict-conway-geometry
python3 -I papers/strict-conway-geometry/check.py --output /tmp/strict-conway-geometry.json
```

The checker requires SymPy. It tests the endpoint and boundary-edge
bookkeeping, rational face maps, primitive translations and logarithmic
normalizations. Deliberately altered maps and peripheral factors must
fail the corresponding identities. These finite calculations detect
formula errors; the existence, topology, completeness and volume
arguments are written proofs in the paper.
