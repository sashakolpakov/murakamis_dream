# Removing the two free sphere vertices by a lens and a cone

Private written proof, 17 November 2026. This is a classical, marked
topological construction. It starts with the four-cell crossing
cellulation of [T] and ends with a generalized ideal triangulation of
the original knot exterior. It supplies neither a finite source identity
for the deletion nor positive developed tetrahedra.

## 1. Statement and conventions

Let the oriented knot diagram and its cut be as in [T], with \(c>0\)
crossings. Fill the two free spherical ends of its four-cell
cellulation. Write their vertices as \(P,S\), and write \(K\) for its
remaining ideal vertex. There are \(4c\) tetrahedra; each has exactly one
occurrence of \(P\), one of \(S\), and two occurrences of \(K\).
Occurrences are counted before face pairing.

**Theorem.** Two explicit preparations and ball replacements remove
\(P,S\), introduce no other vertices, and give a generalized ideal
triangulation with \(4c\) tetrahedra. Its truncated manifold is the
original knot exterior, with the original oriented meridian, cut and
longitude carried along. Each preparation inserts two tetrahedra by
the face maps in Section 2; each replacement removes the prepared
sphere vertex and leaves two fewer tetrahedra. The second connecting
edge is chosen after the first replacement, rather than asserted to
be an initially prescribed \(AS\) edge.

Here a generalized ideal triangulation means standard abstract
tetrahedra with paired whole faces whose quotient, minus its ideal
vertices, is the stated manifold. Edges or vertices of an abstract
tetrahedron can be identified in the quotient. This is the same
convention as [T]. The theorem does not assert that the closures of
all quotient simplices are embedded, or that their developed vertices
are distinct. Their open simplices and the truncated local manifold
models are genuine; no flattened tetrahedron is used as a three-cell.

## 2. An incidence-level lens preparation

Suppose \(V\) is a sphere-link vertex occurring at most once in every
tetrahedron. Choose a tetrahedron

\[
                         T=(V,O,U,B).                 \tag{1}
\]

The two faces

\[
             f=(V,O,B),\qquad g=(U,O,B)                \tag{2}
\]

are distinct face orbits: the first contains \(V\), while the second
does not. Specify their occurrences in (1), including the common
edge occurrence \(OB\). The other occurrences in the paired faces
are determined by the original face maps.

Insert two new tetrahedra \(T_+,T_-\), both with the ordered labels
\((V,O,U,B)\). Pair their faces \(VOU\) with one another and their
faces \(VUB\) with one another, matching the displayed labels. Cut
the old pairings at \(f,g\). Attach the \(VOB,UOB\) faces of \(T_+\)
to the two displayed faces of \(T\), and attach those of \(T_-\) to
their former mates, using the original maps there. Thus every old
face pairing not named in (2) remains literal. Orient the inserted
ball consistently with these attachments.

This description is made on disjoint abstract tetrahedra, before
recomputing edge orbits. In particular, if a face contains two
occurrences of one global edge, the whole face map is replaced, not
just one of its printed edge occurrences. The other corners of the
new faces supply the corresponding continuations. A repeated
tetrahedron in an edge's incidence book is not a second tetrahedron
to be removed.

Here is why the operation is topologically legal despite these
repetitions. The normal disk dual to the selected global edge has
disk interior and a boundary walk recording its cyclic incidence
book. Choose boundary points at the two specified occurrences of
\(f,g\), away from the ends of the corresponding dual edges. Join
them by an arc whose interior lies in that disk's interior. Its
image is embedded: its interior lies in the open dual face, and its
endpoints lie on distinct open dual edges because \(f,g\) are distinct.
Other repetitions in the boundary walk are not points of this arc.

A small collar of this arc is the elementary lune insertion. In a
cross-section normal to the original edge, the two selected face
sheets divide the cyclic book into two half-books. Separate those
sheets by a product collar and put one new tetrahedral sector next
to each half-book. The two sectors meet across \(VOU,VUB\). Their
remaining faces are exactly the four attachments just specified.
At an endpoint of the collar the full three-sheet model is retained;
this is why all corners of a repeated face must be paired before
its edge orbits are read. Collapsing the inserted collar recovers
the old local product neighborhood. Conversely opening that collar
gives a homeomorphism of the thickenings relative to their outside
boundary. The same argument applies in truncated vertex collars.
Thus the filled manifold, all vertex links, and its peripheral
marking are preserved. No embeddedness of the entire closed union
\(f\cup g\) was assumed.

This is the usual \(0\to2\) lune move, here with its actual face
incidences specified. Definition 2.3 of the primary coverage source
listed below uses the same incidence-book description and explicitly
allows repeated tetrahedra in that book. No result about the 3D index
or a global move calculus is used.

In the link \(L_V\), the move cuts the selected edge \(OB\) into two
boundary copies and inserts

\[
                         (O,A,B)_+\cup(O,A,B)_-,      \tag{3}
\]

where the two triangles are paired along \(OA,AB\). The new link
vertex \(A\) represents the new \(VU\) edge. If \(O,B\) are distinct
vertices of \(L_V\), (3) is an embedded closed disk: it has interior
vertex \(A\) and a two-edge boundary from \(O\) to \(B\). It is the
entire closed star of \(A\), since only the two new tetrahedra contain
the new \(VU\) edge. No old link vertex has been split or identified.
The symbols \(O,B\) here denote link vertices, not merely global
vertices of the original three-dimensional quotient.

## 3. The same-boundary cone replacement

Retain the hypotheses on \(V\), and perform Section 2 with distinct
link endpoints \(O,B\). Cut open every face opposite \(V\) in its
incident tetrahedra. The resulting complex is exactly

\[
                              V*L_V.                 \tag{4}
\]

It is a PL three-ball because \(L_V\cong S^2\). This assertion uses
the once-per-tetrahedron condition: the face identifications containing
\(V\) are precisely those defining its link, and no opposite face can
be paired with a face containing \(V\). The opposite faces are the
boundary \(L_V\); their original pairings, including pairings between
two such boundary faces, are recorded separately.

Let \(D\) be the closure of the complement of the interior of (3)
in \(L_V\). It is a PL disk, contains no occurrence of \(A\), and

\[
 L_V=D\cup A*\partial D,\qquad
 \partial(A*D)=D\cup A*\partial D=L_V.                \tag{5}
\]

These ball statements concern the realizations of the generalized
triangle complexes. To verify their PL meaning, subdivide their
abstract faces compatibly with all recorded affine face maps; an
iterated barycentric subdivision supplies an ordinary triangulation
of the link and of its two disks. Coning a triangulated sphere or
disk gives the stated PL balls. The identity on their common boundary
is pointwise the identity on every old triangle, including its edge
occurrences. A PL boundary homeomorphism of balls extends over their
interiors: choose ball parametrizations and extend their resulting
boundary map radially, subdividing if necessary. Thus the extension
is compatible with every recorded old boundary pairing.

Replace the ball (4) by \(A*D\) using this boundary-fixing PL
homeomorphism. The auxiliary subdivisions certify the homeomorphism;
they are not vertices to be added to the final cone face-pairing
prescription. Apply exactly the previously recorded boundary face maps
afterwards. A
boundary-fixing homeomorphism descends under arbitrary such boundary
identifications, so no new embedded-star assumption on the other
vertices or faces is needed.

The face-pairing algorithm is explicit. For each triangle of \(D\)
take its cone tetrahedron with apex \(A\). Pair cone faces over an
interior edge of \(D\) by its existing disk adjacency. The base faces
over \(D\), together with the cone faces over its two boundary edges,
are the old boundary \(L_V\); the latter two faces stand for the two
removed triangles (3). Give all of them their old boundary pairings.
There is no additional tetrahedron, face pairing, or scalar convention.

The boundary vertex \(A\) is an occurrence of the existing global
vertex \(U\). Thus \(V\) disappears and no new global vertex remains.
If \(n_V\) tetrahedra met \(V\) before preparation, its prepared link
has \(n_V+2\) triangles and \(D\) has \(n_V\). The replacement therefore
has \(n_V\) tetrahedra.

Topologically this is also the stated ball-and-tube cancellation.
Inside (4), join a small ball about \(V\) to a small boundary cap at
\(A\) along the radial edge \(VA\). Their union with a thin tube is a
ball meeting the outside boundary in a disk. It can be absorbed into
the region at \(U\). The cone replacement is a triangulated version
of this cancellation. The tube is an actual path in the filled
manifold; no developing-map limit is involved.

## 4. Apply the construction first at P and then at S

Start with any original tetrahedron \((P,O,U,S)\). In \(L_P\), the
endpoints \(O,S\) of its selected edge are distinct: their global
endpoint types are \(K,S\). Section 2 therefore produces the required
lens. Every original and inserted tetrahedron still contains \(S\)
exactly once. Every triangle in \(D\subset L_P\) consequently has
exactly one \(S\) corner. The new cone apex \(A\) has type \(K\), so
every tetrahedron after the \(P\) replacement still contains \(S\)
exactly once. There are again \(4c\) tetrahedra and the only vertices
are \(S,K\).

The link \(L_S\) remains a sphere, by the relative homeomorphism in
Section 3. It has an edge with distinct link endpoints. Indeed, if
its triangle and edge counts are \(F,E\), then \(3F=2E\) with
incidences counted with multiplicity, and Euler's identity gives

\[
                         V(L_S)=2+F/2\ge3.            \tag{6}
\]

Its connected one-skeleton must therefore contain a nonloop edge.
Choose one, and one of its incident triangle occurrences. In the
corresponding tetrahedron write that edge as \(OB\) and the third
link corner as \(U\). Apply Sections 2--3 with \(V=S\).

All three other global vertex labels are now \(K\). This causes no
problem: the lens criterion concerns distinct vertices \(O,B\) of
\(L_S\), not distinct global labels, and the face pair in (2) is still
distinct because only one face contains \(S\). A shared global
\(K\!-\!K\) edge is permitted. The complete face-incidence procedure,
including every occurrence of that loop, is the one already proved.
The result has \(4c\) tetrahedra, only the vertex \(K\), and its link
is the original torus. It is therefore a genuine generalized ideal
triangulation of the knot exterior.

The second tube is chosen by this procedure after the first
replacement. No claim is made that it is a fixed original \(AS\)
edge. Both cancellations absorb a free ball along an actual tube
into the retained knot neighborhood. A ball at the free end of such
a tube can be pulled back along the tube, so this operation leaves
the embedded core \(K\) and its tubular-neighborhood isotopy class
unchanged. The relative ball homeomorphisms are isotopic to the
identity relative to their boundaries; this isotopy descends through
the recorded face maps. Hence the cut and the peripheral curves from
[T] are carried to the same marked knot exterior. In particular the
meridian has degree one, the blackboard longitude is retained, and
the same writhe correction gives the preferred longitude. No new
peripheral covering factor is introduced.

## 5. Source and geometric scope

The construction gives a finite, diagram-independent classical
deletion procedure. It also provides the face maps of the resulting
triangulation, rather than merely its manifold type or a rational
Bloch class. Starting from the five-cell version, one first undoes
the relative classical ball replacement of [T, Section 6]. This is
again only a topological step.

Neither the lune insertion nor the cone replacement has been assigned
the original finite quantum tensors and all their source currents
here. An ordinary cap reassociation is not silently substituted for
the original marked cap. Quantizing these specific interfaces, with
the peripheral factors and all normal data retained, remains a
separate problem. The developed flags of the final tetrahedra may
coincide; the proof supplies no positive angle structure, isolated
geometric saddle, or selected-cycle coefficient.

The complete direct proof source was freshly read at the following
unchanged pin:

| Label | Source | SHA-256 |
|---|---|---|
| T | [Crossing-tunnel shadow cellulation](research_crossing_tunnel_shadow_cellulation.md) | e836e8f4bb4fc0c67eeee286d3ad39e372546b369517ef903df8806551841154 |

Primary definition coverage, not an additional proof input:
S. Garoufalidis, C. D. Hodgson, J. H. Rubinstein and H. Segerman,
*1-efficient triangulations and the index of a cusped hyperbolic
3-manifold*, Definition 2.3, pp. 2624--2625,
[published paper](https://msp.org/gt/2015/19-5/gt-v19-n5-p05-p.pdf).
The proof above imports neither its index theorem nor its global
triangulation-move results. No mathematical programs, numerical
experiments, or public/frozen edits were used.
