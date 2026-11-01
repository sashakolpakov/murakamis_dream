# An octahedral decomposition for ordered trees of crossing circles

1 November 2026.

A crossing circle surrounds two strands of a link and bounds a disk
punctured by them. Cutting along the projection regions and these
disks opens the augmented link exterior into two balls. For the
ordered tangle constructions considered here, each ball can be
assembled from octahedra, with one octahedron for each edge of the
tangle-operation tree. The proof identifies every boundary vertex
and face, so it also identifies the original meridians and disk
longitudes after the pieces are joined.

The tangles have two strings and four ordered endpoints. Their
operations are vertical stacking, quarter-turns in the projection
plane, and the specified cylindrical closure. Every product junction
in the reduced operation tree carries an original crossing circle;
there are no junctions without a circle. The tree, the order of its
branches, and all endpoint frames are retained throughout.
Faces created by opening crossing disks are called shaded faces;
the pieces of the projection regions are called white faces.

This is the topological input for the
[quantitative volume theorem](actual_all_circle_quantitative_volume.md).
The [angular cell calculation](actual_all_circle_angular_octahedra.md)
provides positive shapes for its octahedra, and the
[completion theorem](actual_all_circle_geometric_completion.md)
uses the path supplied by the
[analytic filling criterion](actual_all_circle_curvature_filling_limit.md).
The present proof concerns the augmented exterior before filling.

## 1. The actual ordered object and the statement

At each vertex \(v\) of a finite tree put an original two-strand
crossing-circle tangle \(P_v\). It retains the crossing
\(R^{\epsilon_v}\), where \(\epsilon_v\in\{-1,0,1\}\), and its
auxiliary component bounds the original twice-punctured disk.
Every edge is an actual quarter-turn between two ordered product
junctions. There are no product junctions without their own original
circle. Terminal circles are included as vertices of degree one.
The tree has at least one edge.
Write \(T\) for the actual quarter-turn, \(C\) for the cylindrical
closure, and \(R\) for one positive braid crossing in the original
ordered terminal frame.

The product order, the four endpoint frames, every rotation of a child
ball, and every original disk orientation are part of the data. A
representative recursive description has
\[
 W_v=P_v\prod_{w\text{ child of }v}T(W_w).
\tag{1}
\]
The product here is in its specified order. At the closing sphere one
may use the actual collar move to expose a root circle. A double turn
then leaves its actual half-turn decoration on the affected subtree;
it is not replaced by the scalar identity \(T^2=1\). The relevant moves
are the literal closed-turn and cyclic collar isotopies in
[the original ordered tangle moves](actual_conway_net_twist_volume.md), equations (14)--(18).
Their four collar sectors, and any reversal of the child order, are
retained. Thus (1), with those transported frames, describes the
original all-circle ordered operation tree. It does not introduce a
commutativity move on open two-tangles.

For clarity, the literal root adapter is
\[
 C\!\left(h_0T(E)\right)
 =C\!\left((TP_0)T(E)\right)
 \simeq C\!\left(P_0\,T^2(E)\right)
 =C\!\left(P_0\,\tau(E)\right).
\tag{1a}
\]
Here \(\tau\) is the actual half-turn of the ball. If
\(E=L_1\cdots L_k\), then
\(\tau(E)=\tau(L_k)\cdots\tau(L_1)\), and
\(\tau(TW)=T\tau(W)\). Thus the adapter reverses the displayed root
order and transports every child frame; it does not suppress this
rotation. The two-leaf case of (1a) is the base used below.

More generally the original circle coupon can occur between two
ordered lists of child factors in a nonroot junction. Keep that
position:
\[
 W_v=\left(\prod_{w\in I_v^-}T(W_w)\right)P_v
          \left(\prod_{w\in I_v^+}T(W_w)\right).
\tag{1b}
\]
The lists record the cut at the parent edge in the original cyclic
order. The left-insertion version of the calculation below handles
this form without moving \(P_v\) through a child. Reassociation of a stack
and transport of genuine turn-chain rotations put the literal
circle-only tree in this form. At the root only the actual cyclic
closed-collar move is used to choose its cutting position.

Write \(E\) for the number of tree edges, \(V=E+1\) for the number of
circles, and \(d_v\) for the number of edges incident to circle \(v\).
The exterior admits the following labeled cut:

* There is one pair of octahedral balls per original tree edge.
* At a circle \(v\), its incident edge blocks are joined in the original
  cyclic order. There are \(d_v\) disk-side pages, and exactly one of their
  cyclic seams retains the original disk identification and its
  \(\epsilon_v\) crossing. All other page seams are the untwisted labeled
  identity seams supplied by the ordered insertion.
* Cutting open those distinguished disk seams and the projection
  faces gives two balls. Each is a tree of \(E\) octahedra attached along
  \(E-1\) triangular faces. Its remaining boundary has exactly the two
  original shaded triangles of every crossing circle and the original
  white face cycles.

Here an octahedron means the explicitly labeled topological cell.
The [angular charts](actual_all_circle_angular_octahedra.md) give its
positive shapes. The topological proof does not require the union
of several cells to be convex.

## 2. How endpoint pairings determine the cut

Use the closed-cut convention of
[the projection and crossing-disk cut](actual_conway_bowtie_projection_cut.md), sections 2--4. For the
turned elementary leaf \(h_v=T(P_v)\), label its four physical half-segments
\[
 (v_0,v_1,v_2,v_3)
 =(\text{lower left},\text{lower right},
   \text{upper right},\text{upper left}).
\tag{2}
\]
A quarter-turn cyclically shifts this tuple. A lower factor \(F\) followed
by an upper factor \(G\) joins \(F_2\) to \(G_1\) and \(F_3\) to \(G_0\), leaving exposed
\((F_0,F_1,G_2,G_3)\). Cylindrical closure joins positions 0 to 3 and 1
to 2. These are actual empty joining strips in the projection plane.

One ideal vertex is assigned to each paired main segment and one
vertex \(O_v\) to each original crossing-circle semicircle. The two
shaded triangles of a leaf are
\[
 (O_v,v_1,v_2),\qquad (O_v,v_3,v_0),
\tag{3}
\]
where a half-segment in this display denotes the main-segment vertex
containing it. Around \(O_v\) the cyclic order is \((v_0,v_1,v_2,v_3)\). At a
main-segment vertex the two shaded corner sectors concatenate in the
order of the actual planar joining strip. These sectors determine all
white face cycles by the usual boundary walk. In particular the full
oriented boundary ribbon graph follows from the literal matching;
matching only face or component counts would not suffice.

This endpoint construction records the reversible projection/disk cut. Drilling
a boundary-parallel auxiliary semicircle and then opening its recorded
half disk restores a ball. The disjoint leaf boxes permit this for all
circles. White faces reglue by their actual projection labels. The two
shaded faces reglue by the original disk map, including the retained
half twist. The proof of that cut uses no quantum source identity.

For the next local calculation it is useful to use an inverse turn:
\[
 P_v=T^{-1}(h_v),\qquad
 \text{its exposed tuple is }(v_3,v_0,v_1,v_2).
\tag{4}
\]
This is an exact physical identity by the definition of \(h_v\). It avoids
using \(T^2=1\) on an arbitrary physical tangle.

## 3. One terminal insertion is exactly one octahedron

Suppose the unturned \(P_v\) occurs at the beginning of its specified
local stack. In the current full diagram, let \(x_1\) and \(x_2\) be the
half-segments matched to \(v_1\) and \(v_2\) outside that box. Insert a new
terminal child \(h_w\) immediately after \(P_v\). The literal product rule
changes precisely the following two matches:
\[
 \begin{array}{c|c}
 \text{before}&\text{after}\\ \hline
 v_1\! -\! x_1&v_1\! -\! w_1,\quad w_2\! -\! x_1\\
 v_2\! -\! x_2&v_2\! -\! w_0,\quad w_3\! -\! x_2.
 \end{array}
\tag{5}
\]
All other half-segment matches are unchanged. This remains true if
\(x_1\) or \(x_2\) is in a nested factor or outside the local ball: the
replacement only uses the two exposed output strips of \(P_v\).

Name the old two vertices \(C=(v_1,x_1)\), \(B=(v_2,x_2)\), and name the
new internal vertices \(D=(v_1,w_1)\), \(A=(v_2,w_0)\). The outside vertices
\(C\) and \(B\) are now represented respectively by \((w_2,x_1)\)
and \((w_3,x_2)\). Attach the octahedron with vertices
\[
             (O_v,O_w,A,B,C,D).
\tag{6}
\]
and equatorial cycle \((A,B,C,D)\). Its four shaded triangles are
\[
 (O_v,B,C),\quad (O_v,D,A),\quad
 (O_w,D,C),\quad (O_w,B,A).
\tag{7}
\]
Glue the first one to the old shaded face \((O_v,C,B)\). The two
orientations are opposite, as required for joining oriented balls.
The old face disappears. The second triangle in (7) is exactly the
new \(v\) face in (3), and the last two are exactly the new \(w\) faces.
The other shaded face of \(v\) is untouched.

The four white triangles are the complementary octahedral faces.
Along the three edges of the glued triangle, their unions with the
old white pieces are precisely the new white regions. One can verify
this directly: at each of \(B,C,O_v\) remove the two glued
shaded sectors and concatenate the remaining sectors; their order
is exactly the planar strip substitution (5). The new vertices \(A,D\)
carry the new identity strips in that same order. Thus every remaining
shaded sector and every cyclic vertex order agrees with the endpoint
construction. Following these sectors around each white face therefore
gives the same boundary cycle.

Perform the same attachment in the other projection copy. This
adds exactly one two-octahedron edge block and introduces one new
original circle. It neither identifies two old circles nor inserts a
circle at the attachment seam.

The calculation also proves the inverse operation: remove a terminal
edge block, restore the deleted triangular face, and undo (5). The
original diagram loses that terminal child and otherwise retains its
actual strand connections and order.

There is also an explicit left-insertion version, needed for (1b).
Inserting \(h_w\) immediately before \(P_v\) changes
\[
 \begin{array}{c|c}
 v_3\! -\! x_3&v_3\! -\! w_3,\quad w_0\! -\! x_3\\
 v_0\! -\! x_0&v_0\! -\! w_2,\quad w_1\! -\! x_0.
 \end{array}
\tag{7a}
\]
This is the same octahedral attachment on the other shaded face
\((O_v,v_3,v_0)\). The two formulas are direct applications of the
same lower-output/upper-input stack rule. They retain the physical
rotation of each tangle and all its endpoint labels.

## 4. Why this covers every ordered tree

Start with one actual tree edge. The two-leaf matching gives exactly
the octahedral boundary (7), in both projection copies. This is
[the labeled two-circle block](actual_reflected_two_circle_octahedral_base.md), after the
recorded endpoint-frame rotation. Its proof is a disk/projection cut,
not an equality of two scalar sources.

For a general tree, choose a terminal vertex as root and start with
its unique incident edge. Expose that root by the actual closed-collar
moves from section 1, retaining all transported frames and orders.
The initial root then has no further children to insert; at the other
endpoint the only existing edge is its parent edge. At each vertex
add the children on the right of \(P_v\) in reverse
final order, always immediately after \(P_v\). Add the children on its
left in their final order, always immediately before \(P_v\). This is a
construction of the specified word, not a permutation of an existing
word: successive insertions produce exactly the two ordered lists
in (1b), including the special case (1). A new child initially has
only its own crossing-circle tangle; its
children are subsequently inserted inside its own ball. Its actual
quarter-turn carries the whole local insertion, including the two
projection sides and all four endpoint labels. Any previously recorded
half-turn or input/output reversal similarly carries the complete
insertion and its order. It does not remove the frame decoration.

Induction now gives exactly the original recursive word and its full
boundary ribbon graph. Every step glues a ball along a triangular disk,
so each projection copy stays a ball. There are \(E-1\) attachments after
the initial octahedron. The shaded face count is
\[
                   4E-2(E-1)=2V.
\tag{8}
\]
The count is only a consistency check: the insertion proof has already
identified each of these two faces with its particular original
circle and each main-segment vertex with its literal pair.

The equality of oriented ribbon graphs gives a label-preserving
homeomorphism of the final boundary spheres. Extend it over the balls
by a ball extension. All original white and disk-face pairing maps
are matched, hence the quotient is the original link exterior.
This is stronger than an identification of the unmarked manifold:
the main arcs, individual auxiliary circles, disk sides, and their
specified collar paths are preserved.

The extra triangular interfaces provide the promised pages. In the
whole exterior an upper interface triangle and its lower partner form
a two-triangle, thrice-punctured sphere. The ends are the same original
circle and its two physical main punctures. Its compactification is a
twice-punctured spanning disk for that circle. These pages are obtained
from the explicit cell subdivision and the preceding homeomorphism;
we did not assume that a single original disk cut somehow creates
all \(d_v\) pages. The insertion order places the pages consecutively
in exactly the original cyclic order at that circle. There are \(d_v-1\)
new seams there, plus the original distinguished disk seam.

## 5. Retained half twists and reversed disk frames

First perform the projection construction with the disk cuts open.
A retained crossing changes their regluing, not the half-segment
compiler of the open cut. At each v keep its original distinguished
seam throughout all insertions. Its original disk map is used once,
after the untwisted page attachments. Thus no crossing is distributed
among several edges, and no crossing is silently added at a new seam.

For \(\epsilon_v=0\) the original pure disk map pairs the two sides within
the same projection copy. For \(\epsilon_v=+1\) or \(-1\) use its actual odd
pairings: the punctures exchange and the two projection copies are
permuted as in the original A,B disk maps. The signs +1 and -1 have
their distinct primitive meridian words even though their endpoint
permutation has the same parity. The explicit collar permutation is
also recorded in [the original half-twist collar](actual_balanced_octahedral_belt_stack_volume.md),
section 3a. A full twist changes the peripheral marking and must not
be discarded simply because its endpoint permutation is trivial.

A physical rotation or reflection of a disk frame transports its
puncture labels, its two pages, and its chosen meridian and longitude
together. Apply the insertion table in that transported frame.
In particular a reversal that exchanges the projection copies is
applied to both halves of every incident block. There is no use of
an arbitrary puncture permutation justified only by the rigidity of
an abstract thrice-punctured sphere.

These conventions cover the original signed and reversed diagrams.
The local geometric block may be relabeled by these same actual
rotations. Its shape formula is not used to determine the topology.

## 6. Exact primitive peripheral concatenation

Fix one auxiliary circle \(v\) and orient its original disk-framed
longitude \(\lambda_v\) and meridian \(\mu_v\) as in the original marked
leaf theorem. After the page cut, a small cusp torus of \(v\) consists
of \(d_v\) annular sectors, one from each incident edge block. Every
page boundary on this torus is the same primitive disk-longitude
class. A small meridian crosses these sectors once in their cyclic
order. The insertion (5) subdivides one such transverse passage into
two consecutive passages; it neither winds the meridian a second
time nor changes its longitude class.

This can also be read as a face-word statement. Each insertion
replaces one original disk-face passage by two passages separated
by the new triangular interface. In the final word all internal
interface changes of coordinates occur in inverse consecutive pairs.
After eliminating them, the retained word is the original disk
meridian. Its ordered factors are one endpoint passage for each
incident block, followed at the distinguished seam by the single
original half-twist correction. This is a statement about the
actual marked loop before evaluating its holonomy.

Use the [local angular chart](actual_all_circle_angular_octahedra.md), with common
oriented longitude variable \(\tau_v\) at all pages of this circle. Its
incoming/outgoing edge-ratio tables give exactly the inverse seam
maps with the just-established puncture matching. In one edge block
its small pure meridional increment is
\[
 u_{v,e}=-2\pi\,\partial_{\tau_v}\psi_e,
 \qquad V_v=2i\tau_v.
\tag{9}
\]
This is the local primitive word, not an arbitrary logarithm of its
multiplier. The longitude conjugates to the same element on all
pages. Whenever it is loxodromic, its two fixed points are therefore
carried to the same two marked points. In a coordinate with one at
infinity and the other at \(q\), integrate \(d\log(z-q)\). The coordinate
changes telescope in the concatenated path; the integral is the
sum of the local increments (9). At the complete value it is the
continuous limit of this equality.

The original disk words fix the half-twist correction unambiguously.
In the notation of the marked-leaf theorem, the pure meridian has
multiplier \(\rho\), and the two odd primitive words have multipliers
\(\rho Q\) and \(\rho/Q\). Write \(\nu\) for the local leaf response,
so \(Q=e^{-\nu}=e^{i\tau_v}\) and \(\nu=-i\tau_v\).
The physical \(R^{-1}\) tangle uses the first word and \(R\) uses
the second. Thus the single retained crossing contributes
\(\epsilon_v\nu=-i\epsilon_v\tau_v\), or equivalently
\(-\epsilon_vV_v/2\). Consequently the actual continued primitive logs
are
\[
 U_v=-2\pi\sum_{e\sim v}\partial_{\tau_v}\psi_e
                   -i\epsilon_v\tau_v,
 \qquad V_v=2i\tau_v.
\tag{10}
\]
The original proof of these primitive words is
[the original marked face maps](actual_conway_general_mask_marked_filling.md), sections 5--6,
including its equations (15)--(18). The two-rectangle cusp lattice
there certifies their primitivity. Our page insertion preserves those
same paths; it does not choose a new rational meridian slope.

In particular the integral in (10) is not reset to a principal
logarithm after several pages. Each summand follows its local small
branch, and the actual concatenated loop retains their full sum.
This is precisely where a large total logarithm can occur while every
individual block stays in its small positive chart.

Along the continuous first-charge equations, with charge \(c\in[0,1]\),
\[
 \partial_{\tau_v}\Psi
       +\frac{i n_v}{2\pi}\tau_v=ic,
 \qquad \Psi=\sum_e\psi_e,
 \qquad n_v=\epsilon_v-2p_v,
\tag{11}
\]
(10) gives the exact original primitive filling word
\[
                       U_v+p_vV_v=-2\pi i c.
\tag{12}
\]
At \(c=1\) this is one primitive turn. This calculation identifies
the word and its continued logarithm. The
[completion proof](actual_all_circle_geometric_completion.md)
verifies the positive-cell and nonsingular cusp-link conditions
along the path and deduces the smooth complete filling.

## 7. From the cut to the geometric filling

This proof applies to the actual ordered circle-only tree, with all
its inherited frames and disk collars. It does not assert such a
cut for an arbitrary scalar tensor network, for arbitrary branching
of six independent boundary slots, or for a graph with cycles. It
uses neither commutativity of pair-algebra polynomials nor equality
of source actions. No auxiliary component is filled or deleted in
the topological identification.

The explicit terminal substitution (5), its ribbon-face realization
(7), and the primitive path concatenation supply the ordered
topological identification. The
[local angular charts](actual_all_circle_angular_octahedra.md)
give the positive cells and their full complex seam ratios. The
[analytic criterion](actual_all_circle_curvature_filling_limit.md)
constructs the charge path, and the
[geometric completion](actual_all_circle_geometric_completion.md)
proves that its endpoint is a smooth complete metric on the stated
filled topology.
