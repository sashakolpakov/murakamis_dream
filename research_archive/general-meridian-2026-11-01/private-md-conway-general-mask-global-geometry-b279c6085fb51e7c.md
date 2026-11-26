# Actual complete geometry for strict Conway syntax: the full mask audit

31 October 2026. NEW PRIVATE proof. The earlier input
/private/tmp/md-conway-three-port-types-and-rigid-profiles.md is frozen
(SHA256 66596f79ac27ff829681908d0ac24ae5b1978f1ba67681ea5129f4d33b594503).
No existing note, status file or public file is changed. The argument
below concerns the actual COMPLETE positive-source geometry. It does
not supply a signed high-quarter packet or a new long-filling theorem.

## 1. Statement and the strengthened induction invariant

Let F,G be arbitrary finite literal expressions in the original leaf h,
ordered turn T and ordered product. Require that the original reduced
wire polytope of C(FG), after deleting ONLY its forced final gate, have
a strict state: all leaf labels lie in (0,1/2) and all retained products
satisfy max(x,y)<z<x+y<1. Equivalently, use the already proved source
output types L=(0,1/2), H=(1/2,1), A=(0,1), empty: neither child is empty,
and their root pair is AA, AL, AH or LH, in either order. LL and HH fail.
There is no restriction to the earlier completed grammar.

Claim proved below: its unique complete positive optimizer constructs a
convex ideal right-angled polyhedron with the EXACT original colored
bowtie ribbon boundary. The two original projection balls and original
face pairings give the actual complete finite-volume augmented-link
complement, with all original auxiliary components retained. Its volume
is twice the sum of the retained positive source-cell volumes.

This is an actual geometry claim, not an inference from angle arithmetic.
The required open-cell invariant includes all of the following:

(a) An actual convex, three-dimensional ideal polyhedron with a supported,
    nondegenerate quadrilateral output Q=(C0,C1,C2,C3).
(b) Every original leaf has its two original shaded IDEAL TRIANGLES.
    They remain distinct; the four corners of that leaf and its apex
    remain distinct, and its shaded triangles meet only at that apex.
(c) Every nonport edge is right angled and separates WHITE from SHADED.
    Every port edge has exactly one adjacent nonport face. Its color
    and individual angle are recorded by the four-edge mask below.
(d) Every port corner is an ORIGINAL active terminal singleton. No
    consumed terminal pair, and no auxiliary apex, occurs on the port.
    All other main vertices are permanent disjoint pairs of terminals.
(e) Each active port corner carries exactly one original shaded sector;
    each internal main vertex has the two original shaded sectors of
    its two terminals, in the ordered ribbon concatenation. Each apex
    retains its two original shaded sectors.

The proof tracks all these items, not only (a) and the angles.

## 2. Stationary cells and the exact individual-edge masks

The strict-state construction and old nonvertex-flat barrier apply on
every actual open type interval. Retained angle maps recover all wires,
so the optimum is unique and strict with negative definite reduced
Hessian. The profile is analytic there. The original derivative laws
therefore give entire ordered-quadrilateral isometries at each input:

    kappa_child kappa_prism-input=1.

The source type/port theorem from the frozen input says

    L: (B,X,Y)=(B,B,1), B>0;
    H: (B,X,Y)=(-Y,1,Y), Y>0;
    A: -Y<B<X,

with X²+Y²-B²=1. It is used only for compatible strict type information;
no pair-symmetric geometric angle pattern is assumed for H or L.

Number output edges j=0,1,2,3 cyclically; 0,2 are FREE. Let eta_j=1
when its adjacent nonport face is SHADED and eta_j=0 when WHITE.
The actual dihedral angles divided by pi are

    theta_j=b-eta_j/2          for j=0,2,
    theta_j=1-b-eta_j/2        for j=1,3.           (1)

Masks obey

    L: eta_0=eta_2=0;
    H: eta_1=eta_3=0;
    A: eta_j=0 for all j.                         (2)

The support inclusion is all that is asserted: L/H may have a single
bit or even zero bits. The bare leaf is the explicit ideal pyramid,
with mask (0,1,0,1). Its four other edges are right; its shaded triangles
are (O,C1,C2) and (O,C3,C0). Its output corners each carry exactly one
shaded sector. A turn rotates Q and the mask once, exchanges the FREE/
CAP roles, and changes b to 1-b. It changes no vertex identification,
face or metric. Thus it exchanges the L/H mask support and preserves A.

For a product, use the ORIGINAL maps, in the ORIGINAL orders:

    F:(C0,C1,C2,C3)->(v0,v1,P,infinity),
    G:(C0,C1,C2,C3)->(infinity,P,v2,v3).          (3)

The prism triangles are WHITE. Write p=z-x,q=z-y,w=1-x-y.
All prism and leaf cells are strictly three-dimensional. The output
mask is exactly

    eta_out,0=eta_F,0,  eta_out,1=0,
    eta_out,2=eta_G,2,  eta_out,3=0.              (4)

Every child CAP seam has angle 1-eta_child,j/2. If the bit is zero,
the two incident faces are WHITE and merge flatly. If it is one,
the child SHADED face meets the prism WHITE face at a right angle.
The common input edge P-infinity has total angle

    w+(x-eta_F,2/2)+(y-eta_G,0/2)
      =1-(eta_F,2+eta_G,0)/2.                    (5)

Both bits could be one only for an HH product, which has no strict
state. Thus (5) is likewise either a WHITE/WHITE flat seam or a
SHADED/WHITE right edge. The output FREE angles are
p+x-eta_F,0/2 and q+y-eta_G,2/2, giving (1),(4). The output CAP
angles are the unaltered prism values 1-z. The type table now shows
(2) is preserved in every allowed product. In particular products
with an H child may have unequal opposite FREE angles; the failed
three-pattern simplification is not being reinstated.

Every port angle in (1) lies strictly between 0 and 1 on the actual
type interval. The first attachment is also locally convex before
the second: its two FREE seam angles are z-eta_F,0/2 and
1-y-eta_F,2/2. A nonzero first bit forces x>1/2 and hence z>1/2;
a nonzero second bit forces x>1/2 and hence y<1/2. Thus those angles
are positive and at most one. The CAP seams have already been checked.
After the second attachment, (5) finishes the finite seam check.

## 3. Convexity, ideal coincidences, and all port corners

Here is the geometric global step needed at each attachment. Position
two convex ideal cells on opposite sides of their matching supported
face. In hyperbolic space their intersection is exactly that face. The
finite union is closed, connected and locally convex at every finite
boundary point, by the preceding angle check. Any two finite points
have a shortest path in the union: a length-bounded minimizing sequence
stays in a compact ambient ball, and constant-speed compactness supplies
a limit. Local convexity forces this shortest path to be an ambient
geodesic locally, hence the unique whole geodesic segment. The union
is therefore convex. This is the original supported-face proof, applied
to the refined angles rather than only the old symmetric masks.

The output port remains a genuine supported quadrilateral. Its four
edges have strictly positive nonflat angle in (1). No second boundary
piece can extend that same supporting face through an output edge.
This also excludes an accidental IDEAL coincidence that is invisible
inside hyperbolic space. Indeed, the ideal closures of cells on opposite
supporting sides could intersect only on the ideal circle of their
common support plane. A cell has no ideal vertex on that circle other
than the corners of its matching quadrilateral: any additional such
vertex would enlarge the supporting face past an edge of the quad,
contradicting that edge's strict supporting angle. The ideal closure
of the quad itself has only its four ideal vertices. Thus the only
vertex identifications are exactly the prescribed face-corner maps.
This argument applies first to one child/prism attachment and then to
the other, whose remaining input face stays supported and nondegenerate.

Every shaded triangle stays an entire unchanged face. It is never an
attaching port. A seam incident to it is always RIGHT, never flat,
by (4)–(5) and the CAP rule; only WHITE pieces merge. Thus no shaded
edge is deleted, subdivided, or merged into another shaded face. No
leaf apex is ever on an attaching port, so each remains a separate
ideal vertex with its original four right edges and two shaded sectors.
The supported-face argument prevents all further unintended coincidences.

For completeness the possible output-corner patterns are explicit.
At corner Cj, the two adjacent mask bits eta_(j-1),eta_j have sum at
most one, because (2) supports only one edge parity. The two port-edge
angles sum to 1-(eta_(j-1)+eta_j)/2. All other incident edge angles
are right. The Euclidean ideal-link angle sum gives:

    adjacent bit sum 0: valence 4, PORT/WHITE/SHADED/WHITE;
    adjacent bit sum 1: valence 3, PORT/WHITE/SHADED
                       in the recorded cyclic order.            (6)

There is exactly one original shaded sector at every exposed corner.
This is also immediate under (3): an output corner inherits a single
child terminal; only the two internal interface corners combine two
terminals. A turn rotates, rather than reverses, their ordered sectors.
No new kind of unrecorded port vertex is needed for an H input.

## 4. Exact terminal accounting: no transitive corner collapse

The following combinatorial invariant is separate from convexity and
rules out a possible transitive-identification gap.

Give each leaf four ORIGINAL symbols (i,0),(i,1),(i,2),(i,3). During
compilation, an open expression has exactly four ACTIVE SINGLETON
symbols in its ordered port. All other terminal symbols are partitioned
into disjoint two-element pairs. A paired symbol is permanently
consumed: the corresponding vertex is internal and never appears
on a later attaching/output port. Apices are separate symbols O_i
and never belong to this matching.

This holds for a leaf. A turn merely permutes its four active singletons.
For a product of disjoint child trees, (3) consumes exactly

    F2 with G1,       F3 with G0,

and leaves F0,F1,G2,G3 active. It never acts on any previously consumed
pair. Each newly formed pair contains terminals from DIFFERENT child
leaf sets. Thus the invariant holds inductively. There is no chain of
pair equalities and no equivalence class with more than two terminals.
In the geometric compiler the six prism vertices have precisely these
same identifications; its fresh names do not add a new relation among
old internal vertices. Section 3 excludes extra geometric relations.

For C(FG), one can either keep these two root interface pairs and then
pair the four remaining active terminals cylindrically, or delete the
forced root prism and use the entire closing map

    F:Cj -> G:C_(3-j).                              (7)

The latter forms all FOUR pairs between the distinct root-child leaf
sets. Both descriptions give exactly the same matching. Each original
terminal occurs once in one pair. No pair contains two terminals of
the same leaf: every formation is between disjoint child trees.
Therefore the four corners of any leaf represent FOUR distinct main
vertices even after closure. Its original shaded triangles remain
nondegenerate, distinct, and meet only at their original apex O_i.
This proves the needed assertion without relying on the weaker claim
that each individual gluing joins distinct subtrees.

## 5. The closed right-angled sphere and the exact oriented ribbon cut

Root source stationarity at complementary labels b,1-b gives equal
ordered quadrilateral metrics, so (7) is the original face isometry.
The paired FREE or CAP seam totals are one minus half the sum of the
two paired mask bits. Two ones would require HH on FREE edges or LL
on CAP edges. Neither root pair is strict. Thus every closing seam
is flat WHITE/WHITE or right SHADED/WHITE. The same supported-face
argument makes the union an actual convex ideal polyhedron P. Its
boundary is a sphere, every surviving edge is right angled, and every
such edge belongs to an original shaded triangle. All other seams
merge only WHITE pieces.

There is no hidden duplicate shaded edge or white bigon: P is a
three-dimensional convex ideal polyhedron with genuine triangular
shaded faces and strictly right nonflat edges. Distinct shaded faces
cannot share an edge, since every such edge has a WHITE side. A flat
merge does not delete or identify shaded edges, and §4 prevents a
repeated shaded vertex within a leaf. White faces are actual maximal
convex ideal polygons; none is a zero-width or two-edge region.

To identify the ORIGINAL link rather than merely some polyhedron,
use the independent literal-wire compiler. At each leaf put shaded
triangles (O_i,C_i1,C_i2),(O_i,C_i3,C_i0) in the original oriented
projection chart. At each terminal record its outgoing-next and
incoming-previous shaded neighbors. Product (3) concatenates exactly
the two recorded sectors at each consumed terminal pair; turn rotates
the four ports; closure (7) performs the actual cylindrical pairings.
These are the same maps and cyclic orders used by the metric cells.
The new masks change which edges survive as right edges, not those
terminal pairings or their local orientation. Since every shaded edge
survives and every remaining seam is flat WHITE/WHITE, the final
metric boundary is EXACTLY this bowtie ribbon graph. All white facial
cycles are its complementary oriented facial walks. There is one
single global orientation; individual faces are not independently
reflected to obtain agreement.

The actual projection cut is reversible for this arbitrary literal
syntax. Each auxiliary circle stays in its original disjoint leaf
box with its recorded twice-punctured disk. In either projection ball,
drilling its boundary-parallel semicircle and cutting along that same
half disk cancel one handle in its collar. All collars are disjoint.
The resulting cut is a ball with ideal main-segment vertices and the
recorded disk triangles. Its oriented boundary is the exact ribbon
cellulation just proved. Match these labeled sphere cellulations and
extend over the two balls. Restoring the original white projection
pairings and shaded disk pairings then yields the original augmented
link exterior, with no component deletion, mutation or assumed
four-punctured-boundary interpretation of the auxiliary open port.
The fundamental degree is one.

## 6. Nondegenerate rectangular cusp links and four-step edge cycles

Every ideal vertex of P has only right incident edges. Intersecting
with a sufficiently small horosphere gives a finite convex Euclidean
polygon with every angle pi/2. Its angle sum forces exactly four sides.
It is a NONDEGENERATE rectangle: the incident supporting faces are
distinct and P has three-dimensional interior. Two opposite supporting
lines cannot coincide, since that would put P into a single plane.
Every side has positive length. This excludes a zero-width cusp link,
not merely a formal count of four right angles. Its colors alternate
WHITE and SHADED by §5.

Take the two oppositely oriented projection copies. A white pairing
matches identical labeled faces across copies. The two shaded faces
of each leaf are paired within a copy by the ORIGINAL rule fixing O_i
and mapping C_i1 to C_i0 and C_i2 to C_i3. Such ideal-triangle maps
are isometries. Let e be an edge in one of those shaded faces; its
partner e' lies in the other shaded triangle of the same leaf. They
are distinct because the two triangles share only O_i, not an edge.
The complete edge cycle visits exactly

    e in copy 0, e' in copy 0, e' in copy 1, e in copy 1,

up to cyclic order. Thus there are four distinct edge occurrences,
not a self-gluing with a shorter return. The two shaded maps in the
cycle are inverse labeled triangle maps; the white maps are the
identity between labeled copies. The cycle returns POINTWISE on the
edge. Its angle is 2pi and it has no longitudinal residual translation.

At each ideal vertex, the two opposite SHADED sides of its rectangle
have equal positive lengths. Scale its horosphere to make both equal
one. Every shaded triangle then carries its canonical three corner
segments of length one. All shaded maps preserve these horospheres,
and all white pairings join identical decorations in the two copies.
Uniformly shrink them to disjoint cusp neighborhoods. Their rectangle
links glue without dilation to compact nonsingular Euclidean surfaces.
The reversible actual link cut identifies these as the original cusp
tori. The remaining truncated core is compact. The assembled metric
is therefore complete and of finite volume.

The apex of every original leaf retains its exact local rectangle,
so the previously proved primitive crossing-circle cusp paths and
ratio 2i cot(pi a_i) also remain the actual complete meridian/longitude
marking. This does not, by itself, supply a deformed signed-source
representation or a quarter-index asymptotic packet.

## 7. Volume, cap-sum obstructions, and precise limits

Every local cell is attached on the opposite supported side of its
face. The cell adjacency graph is a tree, and all cells have positive
volume. Hence

    Vol(P)=pi max A_E,
    Vol(original complete augmented exterior)=2pi max A_E.      (8)

The positive full finite source has the same actual rate by the
original uniform factorial upper bound, polynomial number of wire
states and primitive every-level rounding of the strict maximizer.
This is the complete positive source only. No unstable even factor,
normal direction, alias sector, or physical color is deleted.

The argument is not contradicted by the old cap-connected-sum examples.
A cap product D(FG)=C(T(FG)) forces its last product output to zero;
its two inputs are zero and the gate is flat. Such a diagram has NOT
been exhibited as a strict root C(F'G') of the present type. The
boundary cap reduction keeps its two-punctured connected-sum sphere
and gives the sum of component volumes, not a hyperbolic complement.
Here strictness of every retained cell and the explicit complete
metric provide the additional information. If an actual presentation
were a nontrivial connected sum of two already complete pieces along
cusp components, their noncommuting longitudes would centralize the
same meridian, contradicting the abelian parabolic centralizer in this
constructed complete metric. The metric is not deduced from source
positivity alone.

In particular the new L/H profile constants are not interpreted as
finite quantum scalar factors or as automatic connected-sum factors.
The exact N=3 full-normal obstruction in the frozen input still applies.
The refined mask geometry can retain internal volume with a rigid
external profile without such a finite factorization.

The proof above is for the original untwisted complete circle source.
The local complete half-twist partner construction is expected to carry
over because it uses only the original labeled shaded triangles and
rectangular decorations, but it is not needed or newly claimed here.
No general signed high-quarter packet, unrestricted arborescent
long-filling theorem, or arbitrary rational-tangle closure is inferred.
Quarter leaves occur in strict L/H syntax and require separate quantum
analysis.

## Inputs and review status

Source strict-type/rounding theorem:
notes/actual_conway_single_leaf_source_composition.md §§1–3.
Frozen exact port/profile identities:
/private/tmp/md-conway-three-port-types-and-rigid-profiles.md §§1–3.
Actual prism metrics and ordered corners:
notes/actual_newton_ideal_prism_and_associativity.md §§2–4.
Supported-face convexity and old complete-cusp method:
notes/actual_positive_conway_hyperbolic_volume.md §§3–7.
Independent original terminal/ribbon/disk cut and primitive cusp paths:
notes/actual_conway_bowtie_projection_cut.md §§2–6.
Connected-sum scope:
notes/actual_conway_cap_sum_reduction.md.

Author full analytical topology/metric audit complete, pending independent
root/peer review. No numerical test is used as a theorem input. Only this
new private file was written in the current geometry task.
