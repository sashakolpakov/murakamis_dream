# Removing the free vertices by explicit local moves

Private written proof, 17 November 2026. This refines the classical
deletion in [L] into a finite sequence of occurrence-level lune and
bistellar ball replacements. It assigns no quantum tensors to the
moves and makes no positivity assertion about their developed cells.

## 1. Statement and incidence convention

Start with the marked four-cell crossing cellulation supplied by [L].
It has \(4c\) tetrahedra, \(c>0\), free sphere vertices \(P,S\), and the
knot vertex \(K\). Each original tetrahedron contains \(P,S\) once.
The free ends are filled while the following operations are performed.

**Theorem.** There is a finite explicit deletion of \(P\), followed by
\(S\), using only moves of types

\[
                 0\longrightarrow2,\qquad
                 2\longleftrightarrow3,
\]

and exactly one terminal \(4\longrightarrow1\) for each removed vertex.
No new global vertex is introduced. The first stage leaves at most one
\(S\) occurrence in every tetrahedron. The result is a generalized
ideal triangulation of the same knot exterior with its original
peripheral marking. It has at most \(4c\,64^2\) tetrahedra; it need not
be the \(4c\)-tetrahedron output of [L].

Moves are specified on abstract tetrahedron occurrences. For a
\(2\leftrightarrow3\) move, retain its stated internal faces, cut every
other face pairing of the participating tetrahedra, replace the resulting
triangulated bipyramid relative to its entire boundary, and restore all
recorded pairings. A pairing between two other faces of those same
tetrahedra is restored too. Thus the closed bipyramid need not be
embedded in the original quotient. The usual boundary-fixing PL
homeomorphism of the two bipyramid triangulations descends through
these boundary identifications. The participating tetrahedra must be
distinct; that condition is checked below. This is the same incidence
convention used for the relative balls in [L].

## 2. Subdivide a link triangle without a new global vertex

Let \(V\) have sphere link and occur at most once in every tetrahedron.
Write a selected tetrahedron and its link triangle as

\[
                      (V,X,U,Y),\qquad (X,U,Y).
\]

The symbols on the link distinguish edge incidences at \(V\), even
when their other global endpoints agree. Choose the corner \(U\) as
an anchor. Insert the lune of [L, Section 2] at

\[
                        f=VXY,\qquad g=UXY.
\]

These are distinct global face orbits: only \(f\) contains \(V\).
The inserted pair has internal faces \(VXU,VUY\). Its new \(VU\)
edge gives a fresh link vertex \(A\), whose global endpoint is the
same vertex as \(U\). The two new link triangles are \(XAY\).
This lune is legal even if the link edge \(XY\) is a loop: the
incidence-book collar proof in [L] requires distinct face orbits,
not distinct endpoints. The latter requirement there was only for
the closed star of the fresh link vertex to be a disk.

One new triangle \(XAY\) is adjacent across \(XY\) to the old triangle
\(XUY\). Apply \(2\to3\) to their distinct old and new tetrahedra
across \(VXY\). With \(U,A\) temporarily distinguished as abstract
vertices, its output consists of

\[
                       VXUA,\qquad VYUA,\qquad XYUA.       \tag{1}
\]

The other lune tetrahedron remains. Consequently the link replacement
is exactly

\[
                  XUY\quad\longmapsto\quad
                         AXY,\ AXU,\ AUY.                 \tag{2}
\]

Equation (2) is stellar subdivision of that abstract triangle at its
interior. It remains valid if some old link corners coincide: its
boundary occurrences have precisely their former maps. In particular,
the other old/new face pairing \(UXY\leftrightarrow AXY\), if present
between the two participating tetrahedra, is one of the recorded
boundary pairings, not a second face used to define the bipyramid.

The third tetrahedron in (1) omits \(V\); all others contain it once.
The operation adds three global tetrahedra and one link vertex, but
no global vertex. The fresh link vertex can be anchored at any chosen
old corner of the triangle, by choosing the opposite edge for the lune.

## 3. Subdivide link edges and regularize the link

A link edge flip also has a direct realization. Two distinct incident
link triangles \(XUY, XBY\) give tetrahedra sharing \(VXY\).
Their \(2\to3\) move replaces the link diagonal \(XY\) by \(UB\),
with output link triangles \(XUB,YUB\) and the additional tetrahedron
\(XYUB\), which omits \(V\). All other face maps are restored.

For stellar subdivision of an edge \(XY\) with distinct incident
triangle occurrences \(XUY,XBY\), first apply (2) to \(XUY\), with
fresh vertex \(A\). Then flip the old edge \(XY\), now between
\(XAY\) and \(XBY\). The four resulting link triangles are

\[
                         AXU,\ AUY,\ AXB,\ ABY.            \tag{3}
\]

They are exactly the subdivision of the old two triangles at a new
point of \(XY\). The intermediate interior point in (2) and the
edge point in (3) are identified by the boundary-fixing disk
homeomorphism implementing the flip. This operation adds four global
tetrahedra: one lune and two \(2\to3\) moves.

Here is an explicit way to meet the distinct-triangle requirement,
including every self-adjacent edge. First subdivide every original
abstract link triangle by (2). If the two sides of an original edge
formerly belonged to the same triangle, they now belong to distinct
triangles, one for each original edge occurrence. Subdivide every
original edge by (3). A subdivision at another old edge does not
merge these distinct triangle occurrences. The final link is its
barycentric refinement, with vertices corresponding to original
vertices, edges and faces.

This first refinement is a regular triangle cellulation. Each small
triangle has three distinct link vertices, of dimensions \(0,1,2\)
in the old cellulation. Its three edge types are different, so its
closed triangle is embedded, as are its closed edges. This argument
allows loops and repeated boundary incidences in the old triangles.
Distinct small triangles can still have the same vertex set.

Repeat the same face-then-edge refinement. In a regular triangle
cellulation each incidence of one closed cell in another is unique.
The second refinement therefore has one simplex for each strict
chain of cells, with no repeated simplex on the same chain. It is
an ordinary simplicial triangulation of the same sphere. Both rounds
were realized entirely by the moves just specified.

For the \(P\) stage, all new link vertices can be anchored at \(K\).
Initially each link triangle has at most one \(S\) corner, so it has
a \(K\) corner available for (2). The three new link triangles and
the extra tetrahedron in (1) still have at most one \(S\) occurrence.
For (3), choose the fresh vertex \(A\) to have global type \(K\).
Its flip has opposite corners \(A,B\), so its output also has at
most one \(S\). In the face-then-edge procedure one may always use
the fresh face center, already of type \(K\), as the edge-subdivision
anchor. Thus both refinement rounds preserve the required property.

## 4. A disk peeling proof and its three-dimensional moves

Choose any retained link vertex \(A\) whose global endpoint is \(K\).
After Section 3 the link \(L\) is simplicial, its closed star at
\(A\) is a disk, and

\[
                    L=D\cup A*\partial D                 \tag{4}
\]

with \(D\) an ordinary triangulated disk containing no \(A\).

We first prove the disk peeling fact used here. A disk with more than
one triangle has a boundary triangle whose intersection with its
boundary is either one edge with the third vertex interior, or two
adjacent edges. To see this, call an interior edge between boundary
vertices a chord. If there is a chord, choose a side cut off by a
chord whose boundary arc contains the fewest original boundary
edges. Take the triangle on the first edge of that arc. Its third
vertex either is interior to the disk, or is the next vertex of the
arc: any more distant boundary vertex would give a chord cutting
off a shorter arc. In the latter case the triangle has two boundary
edges. If there are no chords, the same conclusion follows from
any boundary edge, except that the whole disk may be one triangle.
The chord separates the disk, so a triangle in its chosen side
cannot have its third vertex on the other boundary arc.

Removing the triangle in either stated case leaves a disk. In the
first case the exposed boundary edge is replaced by the other two
edges through the previously interior vertex. In the second case
the two boundary edges and their intervening vertex are replaced
by the third edge; the interval link of that boundary vertex shows
that it belongs to no remaining triangle. These are disk collar
removals. Induction gives a peeling down to one triangle, with every
intermediate remainder a disk. This proves the needed shelling
without a three-dimensional shellability assumption.

Cut the faces opposite \(V\) as in [L, Section 3]. The initial
abstract ball is \(V*L\). During this peeling maintain

\[
 A*(\text{processed triangles})\ \cup\ V*E\ \cup\ VA*\partial E,
                                                               \tag{5}
\]

where \(E\) is the remaining disk. The following moves realize
each step, relative to the original entire boundary \(L\).

* If \(abc\) has only the boundary edge \(ab\), replace
  \(Vabc,VAab\) by \(Aabc,VAac,VAbc\): this is \(2\to3\).
* If its boundary edges are \(ab,bc\), replace
  \(Vabc,VAab,VAbc\) by \(Aabc,VAac\): this is \(3\to2\).
* For the last triangle \(abc\), replace
  \(Vabc,VAab,VAbc,VAca\) by \(Aabc\): this is \(4\to1\).

The simplicial disk and (5) make all participating tetrahedra
distinct and give exactly the standard local balls. The last
vertex \(V\) has the four-triangle tetrahedral sphere as its entire
link. It is the only vertex removed, and this is the only
\(4\to1\) operation. All earlier changes preserve global vertices.
Restoring the recorded opposite-face pairings is legitimate at
every stage by the boundary-relative convention in Section 1.
The final ball is \(A*D\), with its original boundary maps.

In the \(P\) stage, \(A\) has type \(K\), and every triangle of
\(E\) has at most one \(S\) occurrence. Inspection of the displayed
tetrahedra shows that the peeling preserves this property too.

## 5. Both deletions, size, and marking

Apply Sections 2--4 first to \(P\), choosing \(K\) anchors. There
is an original \(PK\) edge to supply the retained vertex \(A\).
Tetrahedra not meeting \(P\) are untouched at each local step.
Afterwards \(S\) still occurs at most once per tetrahedron, has
its original sphere link, and every other global vertex is \(K\).
Apply the same construction to its incident tetrahedra. Every
anchor and the chosen boundary apex now have type \(K\).

For completeness, a sphere link with \(F\) triangles has \(3F/2\)
edges counted with incidence multiplicity. One barycentric round
adds \(3F+4(3F/2)=9F\) global tetrahedra and changes its triangle
count to \(6F\). Two rounds add \(63F\). The final ball replacement
has fewer tetrahedra than \(V*L\), since it omits the triangles in
the nonempty star of \(A\). If the current global count is \(T\),
then \(F\le T\), by the once-per-tetrahedron condition; the completed
stage has at most \(64T\) tetrahedra. This proves the stated bound.

The lune collars and all ball replacements preserve the truncated
manifold and its boundary links. Filling a free spherical end during
the argument and then absorbing its ball into the region at \(K\)
is precisely the ball-and-tube cancellation in [L]. Thus after both
deletions the sole ideal vertex has the original torus link. The
boundary-fixing PL identifications carry the actual cut, meridian
and blackboard longitude; the original writhe correction still gives
the preferred longitude. The second connecting path is chosen after
the first stage. No identification with a preassigned second tube
is needed, and no peripheral covering factor is introduced.

## 6. Exact scope of the reduction

The theorem reduces the classical move **types** to lenses,
bistellar pentagons and one vertex-removing bubble per free vertex.
It does not identify a marked \(4\to1\) tensor with the numerical
cap--cup evaluation, or assign the original source to four boundary
faces of the final bubble.

There is an additional concrete quantum issue even before that
bubble. In (1), the new global endpoint \(A\) equals the old \(U\).
On the unchanged developed geometric data these two occurrences
can have identical flags, so \(XYUA\) can be identically degenerate.
The classical ball replacement is valid nevertheless. Applying a
quantum pentagon at such a configuration would require its actual
singular source/current transport, not merely its identity on an
invertible regular shape chart. No positivity, selected coefficient,
or full boundary-state transport is proved here.

The complete direct proof source was freshly read at its unchanged pin:

| Label | Source | SHA-256 |
|---|---|---|
| L | [Free sphere vertex lens deletion](research_free_sphere_vertex_lens_deletion.md) | b2309660fabcbb5b196ec5df1c6cecb5e8edb0a7a2255129109e2957102020e0 |

No mathematical programs, numerical experiments, or public/frozen
edits were used.

