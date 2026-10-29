# The actual closed Conway cut from its bowtie ribbon graph

29 October 2026. This supplies a direct CLOSED-diagram identification
for the complete Conway geometry. It also corrects an overstatement
in the earlier explanation of the open cells: the quadrilateral port
of a single leaf pyramid must not simply be called half of the
physical four-punctured tangle boundary. The closed identification
can and should be proved without that assertion.

The proof below reconstructs the actual projection cut from literal
main-wire connections and the original crossing disks. It compares
EVERY colored face cycle and its ribbon order with the stationary
polyhedron. Matching only component counts or volume is not used.

## 1. Why the open-port description needs qualification

For a leaf pyramid the port is Q=(C0,C1,C2,C3), while its shaded
faces are (O,C1,C2) and (O,C3,C0). Restoring the crossing disk pairs
C1 with C0 and C2 with C3. In particular it identifies the two CAP
edges of Q within each copy. The two FREE edges are joined across
copies through the white faces. The two remaining quadrilateral
faces consequently have four paired edges and TWO ideal vertex
classes. Their compactification has Euler characteristic 2-4+2=0;
it is not the usual two-quad cellulation of a four-punctured sphere,
whose four punctures remain four distinct vertices.

Thus an open metric port is useful auxiliary cut data. Its ordered
cross ratio and its gluing identities are valid, but those facts do
not identify it by itself with the physical four-punctured boundary
or determine that boundary's full holonomy representation. In
particular one cannot infer a deformed peripheral representation
from port cross-ratio matching alone.

This observation does NOT give a counterexample to the closed
hyperbolic-volume theorem. The closed theorem has the following
independent projection-cut proof, which avoids the open-port claim.

## 2. Compile the original main segments without using prisms

Expand the robust expression into h leaves, actual turns and stacks.
At leaf i label its four main half-segments

    C_i0 bottom-left, C_i1 bottom-right,
    C_i2 top-right, C_i3 top-left.

These are the pieces from the leaf's crossing-disk punctures to
its four physical ports. Its two original main arcs join 0 to 1
and 2 to 3, each crossing its own disk once. The half-segments on
opposite sides of that puncture are kept DISTINCT in the projection
polyhedron; the shaded face pairing will restore the main arc.

An open expression has four exposed, still unpaired half-segments.
The literal rules for these four labels are:

* A turn replaces (C0,C1,C2,C3) by (C1,C2,C3,C0).
* In a lower F, upper G stack, pair F2 with G1 and F3 with G0.
  The four exposed labels become (F0,F1,G2,G3).
* The final cylindrical closure pairs C0 with C3 and C1 with C2.

Each pairing joins exactly the two ends of one actual main segment
between successive crossing disks. A structural induction shows
that each exposed label is still unpaired, and every removed label
is paired exactly once. Therefore a closed expression with H leaves
has 2H such segment pairs, not an unspecified equivalence relation
deduced from a quantum polynomial.

Make one ideal vertex for each paired segment, and one further
vertex O_i for each upper crossing-circle semicircle. At leaf i
place the two SHADED triangles

    (O_i,C_i1,C_i2),       (O_i,C_i3,C_i0).         (1)

Here each C now denotes its actual paired-segment vertex. These
are the original two sides of that leaf's half crossing disk.
Their six edges are the complete bowtie at that leaf. All pairings
are the physical identity wires, with no auxiliary circle omitted.

## 3. Ribbon order determines all white faces

Use the orientation of the original projection sphere. At O_i the
cyclic neighbor order is (C_i0,C_i1,C_i2,C_i3). Both shaded triangles
in (1) have their displayed positive cyclic order in the local
projection chart.

At an outer corner of a shaded triangle, list its outgoing next
neighbor followed by its incoming previous neighbor. This ordered
pair records the shaded sector; the complementary sector is white.
When an actual identity segment joins two such corners, concatenate
their two ordered shaded sectors. This is the cyclic order at the
resulting four-valent vertex. It follows by taking a thin planar
regular neighborhood of the actual joining arc: the two shaded
sectors remain on its two sides and the white sectors connect
through the two sides of that neighborhood. No strand crosses
another during this contraction.

Consequently the source's literal planar matching gives a complete
oriented ribbon graph, including every shaded sector. A facial walk
arriving along the dart (u,v) leaves v along the neighbor preceding
u in that cyclic order. The walks (1) are exactly the shaded faces;
all the remaining walks are WHITE faces. Thus all white polygons
are fixed by the actual diagram, not guessed from face counts.

The graph is embedded in the original projection sphere: quarter-
turns rotate its charts, and products join the two matching ports
by the two actual disjoint identity wires. This construction records
nesting and cyclic order as well as abstract incidence. An unembedded
graph or a linking matrix would not supply the same information.

## 4. This is the genuine cut of the closed link exterior

Put the compiled untwisted main diagram in its projection sphere.
Every auxiliary circle is the original small perpendicular circle
with its recorded twice-punctured spanning disk. Those disks lie
in disjoint leaf boxes, and remain disjoint under every actual
turn and stack.

In each projection ball, the upper or lower semicircle of an
auxiliary component is boundary parallel by its literal half disk.
Drill these disjoint semicircles and cut along those same half
disks. This returns a ball: drilling one boundary-parallel arc
introduces one handle, and opening its recorded bridge disk cancels
that handle in the explicit collar of the arc. The collars are
disjoint, so this cancellation can be performed for all arcs.
The main segments lie on the projection boundary; removing their
small neighborhoods makes ideal ends and does not add an interior
handle to this cut ball.

The ideal vertices of the cut ball are precisely the upper
semicircles O_i and the main segments between disk punctures.
Flattening each half disk exposes exactly its two triangles (1).
At its punctures, the main-segment sides occur in the order of
section 3. The remaining boundary pieces are the original planar
projection regions, whose cycles are exactly the white facial
walks of that ribbon graph.

This gives a reversible cut with all faces labeled. The two balls
glue across white faces by their projection labels. Within each
ball, the two shaded faces of disk i are paired fixing O_i and
matching C_i1 to C_i0 and C_i2 to C_i3. These restore the two
original arcs through that disk. Reversing all cuts therefore
recovers the ACTUAL original link exterior, with its retained
auxiliary circles and component/mark paths.

## 5. The stationary polyhedron has exactly this ribbon boundary

The geometric construction uses the same local shaded triangles
(1). At a product its explicit prism maps are

    F:(C0,C1,C2,C3) -> (v0,v1,P,infinity),
    G:(C0,C1,C2,C3) -> (infinity,P,v2,v3).

They make precisely the two segment pairings F2=G1 and F3=G0,
and leave exposed corners (F0,F1,G2,G3). A turn cyclically rotates
these exposed labels. The final face gluing j->3-j makes the
remaining cylindrical pairings, exactly as in section 2.

The right/flat angle table proves that every edge not belonging
to a shaded leaf triangle is a flat WHITE/WHITE seam and is
removed when those two white pieces are merged. No edge of a
shaded triangle is removed. Hence the final nonflat boundary graph
is precisely the union of the leaf bowties (1) under the actual
segment pairings. The local orientation check in the displayed
prism maps concatenates the shaded sectors exactly as in section 3;
the maps are the left/right identity stack, not a reflection of
one selected child or an unrecorded mutation. Flat white merging
does not change any remaining cyclic order.

Therefore the geometric polyhedron and the actual projection cut
have the SAME oriented ribbon graph, the SAME two shaded triangles
for every disk, and the SAME complete list of white face cycles.
Their boundaries are labeled cellulations of a sphere. A map of
the matched cells extends over the two balls by radial extension
after choosing interior points. Together with the matched white
and shaded gluing maps, this gives a homeomorphism of the assembled
geometric manifold to the actual link exterior. This is the closed
topological identification needed by the volume theorem.

The independent audit below implements section 2--3 directly from
the original wires, WITHOUT constructing any prism. It then compares
every colored face cycle with the separately implemented stationary
cell compiler. This is a stronger check than component counts or
the numbers 3H,6H,3H+2; the proof itself is the local ribbon-order
argument and reversible disk cut above.

## 6. Every actual crossing-circle cusp is explicitly marked

The closed-cut identification also gives a general complete-cusp
formula. The apex O_i retains the four original neighbors of its
leaf pyramid, even after all white merges. In its original local
upper-half-space coordinate they are

    C0=1, C1=E, C2=-1, C3=-E,
    E=exp(2pi i x_i), 0<x_i<1/2.

On a horosphere at O_i=infinity these form a rectangle. Its FREE
(white) sides have length W=2sin(pi x_i); its CAP (shaded) sides
have length H=2cos(pi x_i). The complete cusp has TWO rectangles,
one from each projection ball. Their original disk and projection
pairings give the primitive lattice

    mu=E-1,     lambda=-2(E+1),
    tau_geom=lambda/mu=2i cot(pi x_i).             (2)

One direct path check fixes the marking. The meridian is the
inverse shaded map, fixing O and sending C3 to C2 and C0 to C1.
Thus at completeness it is exactly z->z+(E-1). The longitude crosses the bottom white
face to the other copy and returns through the top white face.
Its translation is -2(E+1). This runs along the two sides of the
original crossing disk, and is its disk-framed preferred longitude.
It traverses those sides once, not twice. The parallelogram has
area 2WH, the total area of the two rectangles, so these paths
form a primitive peripheral basis.

The sign convention agrees with a positive imaginary cusp shape.
Equation (2) is a statement about ACTUAL crossing-circle meridians
and longitudes. The Newton wire x_i is used to compute their shape;
it is not itself renamed as a meridian logarithm. In the general
source filling convention phi_titi(0)=2pi i tau_packet,i, the
packet parameter is HALF this geometric ratio:

    tau_packet,i=i cot(pi x_i),
    dV_i/dU_i=2 tau_packet,i=tau_geom,i.

Matching this Hessian is a useful necessary check, but a full
deformed marked representation must still be supplied before the
general quantum filling transfer can identify filled volumes.

Audit: [literal bowtie ribbon faces and complete cusp paths](../experiments/audit_actual_conway_bowtie_projection_cut.py)
and [results](../experiments/actual_conway_bowtie_projection_cut_results.json).
This repairs the closed cut interpretation; it does not assert that
the single open quadrilateral port is a physical four-punctured
boundary, or that arbitrary deformed port matches already solve
the full peripheral gluing equations.

Independent internal reviews: the local-cell and coherent-source
agents separately read the full closed ribbon and disk-cut argument
and the primitive cusp marking, and reported PASS. The coherent-source
agent also independently replayed the strengthened 69-case audit.
The audit additionally fixes one global sphere
orientation and compares every oriented face cycle and every vertex
cyclic order, rather than allowing independent reversal of faces.

Primary-agent analytical review checked the direct closed disk cut, actual segment matching, oriented ribbon induction, and primitive cusp marking. Fresh replay passed all 69 oriented face/rotation comparisons. The former open-port overstatement has been replaced in the complete geometry note; no deformed representation is inferred from this correction.
