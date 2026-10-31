# The actual augmented plat as a cubic graph with a marked perfect matching

30 October 2026. This gives a geometry/topology interface for an arbitrary
fixed 2k-plat, k>=2, rather than only a two-port Conway tree. Its input is
the ACTUAL diagram, its designated crossing boxes and their retained
half twists. The reversible cut produces a plane cubic graph Delta with
a specified perfect matching D. A positive labeled right-angled ideal
rectification certificate for Delta then gives the actual complete
augmented complement, with volume 2 Vol(Q_Delta).

The certificate is an explicit geometric hypothesis. This note does not
prove its existence for every reduced plat, the growing-color source
limit for that plat, or a generic auxiliary deformation from an unmarked
polyhedron. It does identify the correct graph and exactly why the
existing trivalent NC source theorem is only a subclass.
Here k is the supplied plat width; no claim that this presentation
realizes the knot's minimal bridge number is required.

## 1. Start with a literal diagram and its crossing disks

Fix a 2k-plat word together with a disjoint collection of two-strand
crossing boxes covering ALL crossings. The outside strands, original
caps and cups have no remaining crossing. One may first take maximal
twist regions, but the chosen boxes and their order are recorded data.
Put a crossing circle around each box and retain its original twice-
punctured spanning disk. Remove full twists, retaining epsilon_i in
{0,+1,-1} as its half-twist sign. Full twist integers remain recorded
in the peripheral collar marking when they are to be restored.

For the cut first remove these half twists as well; their effects are
restored by the explicit shaded pairings in section 4. The resulting
flat diagram has main arcs in the projection sphere and perpendicular
crossing circles. Let r be the number of crossing disks. Assume every
main component meets at least one of them, so that the pieces outside
the punctures are exactly 2r intervals pairing 4r labeled terminals.
For a nontrivial knot with all its crossings in the designated boxes
this requirement is automatic. An extra circle with no disk incidence
must not be silently discarded.

At disk i choose the four CYCLIC local labels C_i0,...,C_i3 so that
its untwisted strands restore the pairs 0--1 and 2--3. This is a
local crossing-disk chart; it is not an unrecorded permutation of the
global plat endpoints. Its upper half disk has the two sides

    S_i0=(O_i,C_i1,C_i2),
    S_i1=(O_i,C_i3,C_i0).                              (1)

The diagram's actual outside intervals, including all plat cups and
caps, give a perfect matching of the C terminals. Two matched ends
are the two ends of ONE actual main segment. The embedding and cyclic
orders are retained, not just its abstract endpoint permutation.

## 2. Construct Delta and its marked matching without a geometry guess

Give Delta one vertex v_i0 and v_i1 for each pair (1). Add the edge
d_i=v_i0 v_i1 and mark it as a crossing-disk edge. For each actual
outside main segment join the two vertices whose shaded triangles
contain its two terminal labels. The incident edge order at each
vertex is exactly the cyclic order in its triangle (1).

Each vertex has one disk edge and two main-segment edges. Hence Delta
is a plane CUBIC ribbon graph, and

    D={d_i} is a specified perfect matching,
    |V(Delta)|=2r, |E(Delta)|=3r.                     (2)

The embedding follows by contracting the small shaded sectors to
their centers and following the actual planar identity strips. This
operation does not move an endpoint through another endpoint. Loops,
parallel edges or repeated facial walks are recorded if the supplied
diagram produces them. They are not repaired by an arbitrary graph
isomorphism or by changing the knot diagram.

The original bowtie boundary graph is the MEDIAL graph of Delta:

* An ideal vertex x_e corresponds to an edge e of Delta. For e=d_i
  it is O_i, the crossing-circle semicircle. Otherwise it is the
  actual main segment represented by e.
* The three edges incident to v give the shaded triangle T_v.
* The other facial walks are the original white projection regions;
  their edge labels are the face walks of Delta.

This identification follows at a main segment by concatenating its
two oriented shaded sectors, and at O_i by its two half-disk sectors.
These local rotations determine EVERY medial face cycle. If the graph
is a cellular connected sphere embedding, Euler gives r+2 white faces;
the cut then has 3r vertices, 6r edges and 3r+2 faces. These counts are
checks of the labeled ribbon construction, not its topological proof.

## 3. A finite sufficient geometric certificate

The required input Q_Delta is a convex three-dimensional ideal
polyhedron with the following EXACT labeled incidence:

1. Its ideal vertices are distinct points x_e for e in E(Delta).
2. Its shaded faces are triangles T_v, with the three incident edge
   labels in the original cyclic order at v.
3. Its white faces F_f follow the original face walks of Delta.
4. Every edge separates one shaded and one white face, with dihedral
   angle pi/2. All indicated faces and edges are nondegenerate.

A concrete certificate consists of future null vertex lifts, outward
spacelike face normals, their incidence equalities, strict nonincident
supporting inequalities, and the labeled convex-hull face cycles.
Adjacent face normals have zero Lorentz product. Finite incidence and
strict inequalities certify the asserted convex three-dimensional
polyhedron. An unlabeled polyhedron, matching volume or matching cusp
count is not a certificate for this diagram.

This hypothesis automatically excludes degenerate graph data that
cannot be the stated polyhedral boundary. It is uniform in k and r;
there is no restriction to a trivalent source partition or to a
tree of four-port metric cells.

## 4. The actual face quotient, including every half-twist sign

Cut the actual flat augmented complement along its projection sphere.
In each projection ball, each crossing-circle semicircle is boundary
parallel by its original half disk. Drilling it and opening THAT half
disk cancels the introduced handle in the explicit semicircle collar.
The half disks are disjoint, so all cancellations give one cut ball
in each half. Main segments on its boundary give ideal ends and do
not add an interior handle. Its boundary is precisely the labeled
medial sphere of section 2.

By the certificate, this is also the oriented labeled boundary of
Q_Delta. The boundary cell identification extends over the ball by
radial extension after choosing interior points. Take two copies
Q^+,Q^- with opposite abstract orientations. White faces glue across
copies by their original projection labels. At an even disk glue
within each copy, fixing O_i and matching

    C_i1 -> C_i0,       C_i2 -> C_i3.                  (3)

At an odd disk glue across the two copies:

    S_i0+ -> S_i1-: C_i1+ -> C_i3-, C_i2+ -> C_i0-,
    S_i1+ -> S_i0-: C_i3+ -> C_i1-, C_i0+ -> C_i2-.    (4)

In both lines the crossing-circle vertex maps to the same disk's
vertex in the indicated copy. The reverse maps are inverses.

For (4), rotating one side of the twice-punctured disk by ±pi sends
(y,z) to (-y,-z), with the projection line z=0. It exchanges its two
punctures AND the two half disks. This gives exactly (4) for either
sign. The opposite signs retain different collar paths, differing
by one full twist; they are not the same peripheral marking.

Reversing these literal cuts recovers the original augmented plat
exterior. Thus the quotient is the ACTUAL diagram with its original
disk labels, main components and half-twist pattern. No assertion
about all abstract cubic graphs being realized by a chosen plat is
needed: Delta was constructed from that given plat.

## 5. Edge holonomy and complete cusps

Every ideal vertex link of Q_Delta is a rectangle: four right-angled
faces alternate shaded and white there. Its two opposite shaded
sides have equal length. Scale its horosphere so that both have
length one, independently at every ideal vertex. Consequently every
shaded ideal triangle has its canonical length-one horocycle at each
corner. Use the identical decoration in the second copy.

Every prescribed shaded triangle map, including the corner exchange
in (4), preserves these canonical horocycles. White maps preserve the
copied decorations. At each boundary edge the disk partner is distinct
from itself: the two triangles paired along a matching edge share
only their marked vertex O_i. An alternating disk/white cycle has
four pieces, for both (3) and (4), and has total angle 2pi.

Here is also the pointwise holonomy check. The edge cycle fixes its
two ideal endpoints and preserves the chosen horosphere at each.
Its translation/dilation along the edge is therefore zero. Its
rotation angle is the sum of the four right angles, namely 2pi.
An orientation-preserving hyperbolic isometry fixing both endpoints
is determined by these dilation and rotation parameters; the word
is the identity. Thus there is no leftover edge translation hidden
by an angle calculation alone.

After a uniform horosphere shrink, the ideal links glue to finite
Euclidean surfaces with no cone or dilation defect. The actual
link-exterior cut identifies them as cusp tori. Their ends are
complete standard hyperbolic cusps. The remaining part is compact,
so the entire quotient is a complete finite-volume hyperbolic
manifold. Its volume is

    Vol(S^3 minus L_Delta,D^epsilon)=2 Vol(Q_Delta).   (5)

This proves a conditional geometric theorem at EVERY fixed plat width.
The hypothesis is the explicit labeled positive certificate, not an
assertion that a polynomial stationary point must be geometric.

The certificate also gives an actual POSITIVE ideal triangulation.
Choose an ideal vertex a of Q_Delta. Triangulate every face not
containing a by noncrossing diagonals, and subdivide each face that
does contain a by its fan from a. Cone a to every triangle in the
nonincident faces. Convexity makes these tetrahedra tile Q_Delta
with disjoint interiors. Strict supporting inequalities put a
strictly off every nonincident face plane, so each tetrahedron is
nondegenerate with positive orientation. Use the identical face
subdivisions in the second copy. All white subdivisions then match;
shaded faces were already triangles. The actual quotient is therefore
triangulated by positive ideal tetrahedra, with its complete edge
and cusp equations inherited from the metric just proved. This is
a constructive geometric triangulation, not an identification with
a particular factorial source or an independently proposed potential.

## 6. Primitive crossing-circle paths are still local and explicit

At any crossing-circle apex O_i put it at infinity. Its four adjacent
white/shaded planes are vertical; their intersection on a horosphere
is a rectangle. After a Euclidean similarity its other ideal vertices
can be written

    (C0,C1,C2,C3)=(1,E,-1,-E), E=exp(2pi i x),
    0<x<1/2.

This x is a measured local geometric rectangle parameter, NOT yet a
Newton source variable for a general plat. Put c=cot(pi x)>0.
The actual two-white-face longitude and the collar meridians are

    lambda=-2(E+1),
    mu_0=E-1,
    mu_+=-2, mu_-=2E, mu_+-mu_-=lambda.               (6)

The elementary white and disk maps giving these translations are
exactly the local maps (5) in the
[half-partner cusp proof](actual_conway_half_twist_partner_geometry.md).
Their use requires only this rectangle and the original disk pairing,
not a Conway prism decomposition. The parallelogram area of each
(mu,lambda) pair equals the area of the TWO actual cusp rectangles.
Thus these are primitive disk-framed bases, with shapes

    tau_0=2ic, tau_+=2ic/(1+ic), tau_-=2ic/(1-ic).     (7)

The choice of + or - is the recorded geometric collar convention.
Any proposed quantum variable must be calibrated against the actual
braid/loop convention; a cusp Hessian does not select that convention.
Further full twists retain their actual integer meridian shear.

Equations (6)--(7) give the COMPLETE marking. They do not construct
the general plat's mixed-source deformation or identify its action.

The main-component test is also literal. Let sigma be the outside
terminal matching. At disk i let kappa_i be (01)(23) for even parity
and (02)(13) for odd parity, in the cyclic chart of section 1. The
main components are exactly the connected components of the graph
on the 4r terminals with the sigma edges and the kappa edges. Every
vertex has degree two, counting parallel edges, so these are cycles.
After all crossing circles are filled, the result is a KNOT precisely
when this graph is connected. Adding full twists changes neither
kappa nor this criterion. This is an exact test on the supplied
diagram, not a claim that every parity pattern produces a knot.

## 7. The exact relation to the older NC rectified-core theorem

The existing NC theorem starts with a different cubic graph Gamma:
its 2b trivalent cup/cap vertices and its 3b physical EDGE coupons.
Its crossing-circle diagram has the present matching graph

    Delta=Fisher(Gamma).

Namely replace each vertex of Gamma by the triangle of its three
ordered incident slots. The original edges of Gamma become the
matching D; all other edges form those facial triangles. Thus
|D|=3b and Delta\D is a union of 2b facial 3-cycles. The earlier
construction of Q_Gamma plus 2b octahedra produces precisely this
medial Delta boundary. Its formula

    4b v8+2Vol(Q_Gamma)

is consistent with (5), since its half-polyhedron has volume
2b v8+Vol(Q_Gamma).

An arbitrary augmented plat does NOT automatically have this Fisher
structure. Its matching complement can have other cycle lengths or
nonfacial cycles. Even the crossing-circle count r need not be a
multiple of three. For example the actual isolated h^4 compiler has
r=4 and two nonmatching 4-cycles, so it cannot literally be a source
with 3b edge circles and trivalent NC vertices. Its geometry was proved
separately; it is not an instance of that NC theorem by relabeling.

Even facial triangles alone would not certify the existing original
NC source: its black/white ordering and its two noncrossing triple
partitions must also match the actual cups and caps. The graph,
matching, ribbon order and original marked source all matter.

## 8. What replaces a four-port tree in the general plat

The full original quantum source is a planar Morse network of actual
two-strand coupons, cups and caps. A sweep may have 2k active strands;
coupons at different levels can share a physical strand. The finite
operator product is therefore not a product of independently chosen
commuting edge scalars or of unrelated theta evaluations.

On the representation side a cutting sphere disjoint from the crossing
circles and meeting 2m main strands carries the ORDERED puncture
meridians H_1,...,H_(2m), their flags, and H_(2m)...H_1=I, modulo
the actual common frame. A pants decomposition
of that punctured sphere introduces internal curve holonomies and
their gluing frames. Matching their traces alone loses the twist
conjugators. These frames form a centralizer torsor: with ordered
eigenflags the regular semisimple gluing group in PSL(2,C) is
multiplicative, and the noncentral parabolic gluing group is additive.
An SL(2) formulation
also retains its central signs. The original braid word supplies the literal transport,
as in the all-bridge Hurwitz presentation already proved in the repo.

Thus a multiport replacement must preserve those marked sewing data
and the full finite quantum source, including its first normals and
recoupling coefficients. The present graph theorem supplies the actual
complete geometric target. It does not provide the source's selected
period, its nonzero amplitude, its whole-color gap, or the identification
of a general mixed-source action with this marked geometric branch.

## 9. Coverage and the precise existence gap

For coverage only, [Purcell's exposition](https://users.monash.edu/~jpurcell/papers/expos-auglinks.pdf)
already describes fully augmented links by cubic graphs with dimers,
and states hyperbolicity for a nonsplittable prime twist-reduced
diagram with at least two twist regions. The broad geometric-triangulation
statement for sufficiently long fillings also appears in
[Ham--Purcell](https://users.monash.edu/~jpurcell/papers/HamPurcell_GeomTriang.pdf).
No geometric existence or filling proof from those sources is used
in sections 1--8, and no novelty of the cubic/dimer viewpoint is claimed.

Hyperbolicity of the original knot alone does not certify a CHOSEN
plat's augmented skeleton. A nugatory kink can be inserted in the
diagram of the same hyperbolic knot; its designated crossing circle
bounds a disk disjoint from the knot and gives a split added component.
The chosen diagram and crossing regions require their own check.

For the desired all-k-bridge, all-long-twist-regions theorem, the
remaining geometry existence step is therefore explicit: construct
or independently prove the positive labeled Q_Delta certificate for
the actual reduced augmented skeleton. The quantum source/period and
marked mixed-deformation steps are separate. None follows merely
from calling the diagram hyperbolic, prime, or a plat.

## 10. Independent finite checks and their scope

[The executable audit](../experiments/audit_general_augmented_plat_matching_geometry.py)
constructs the original terminal intervals, their cubic marked graph,
and the full ORIENTED medial face cycles in two independent ways.
It checks 87 original Conway/compiler dictionaries, including the
isolated h^s examples for 3<=s<=20, and 21 literal plat diagrams with
2<=k<=8. In every plat case all outside intervals and all upper/lower
caps are retained; no free component is discarded. The 2k-plat
test family has one odd layer joining the k original cap components
in a chain, so the direct terminal test also gives a knot parity
witness at each tested width. These finite checks audit the actual
labels and construction. They do not infer a positive geometric
certificate, twist reduction, or a quantum asymptotic from a graph.

[Recorded results](../experiments/general_augmented_plat_matching_geometry_results.json).

The matching geometry retains the stated positive-certificate hypothesis and Fisher-subclass restriction. It supplies no source asymptotic.