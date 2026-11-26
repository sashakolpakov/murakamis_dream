# The geometric construction behind balanced terminal decorations

## 1. A combinatorial starting hypothesis

It is enough to start with an actual connected marked augmented diagram
whose white cellulation is a simple triangulated sphere with at least
four vertices. The matching pairs, cyclic orders and marked MAIN edge
are those of its projection/crossing-disk cut. A positive geometric
certificate need not be supplied independently.

Here is the complete existence argument from
`actual_smoothed_source_capacity_blocks.md`, Sections 4--5, in a form
that makes its presentation independence explicit. Remove one triangular
face \(abc\), prescribe positive radii at its three vertices, and let
\(v\) be the number of remaining interior vertices. The disk has
\(2v+1\) triangles. Give every interior vertex angle demand \(2\pi\),
and pool the three boundary vertices into one destination with demand
\(\pi\), retaining the separate boundary corners.

An interior subset \(S\) touches at least \(2|S|+1\) disk triangles.
To see this, puncture the sphere at a vertex of \(S\). The complementary
simple planar graph on the other interior vertices \(T\) and \(a,b,c\)
has at most \(2|T|+1\) bounded triangular faces. One is the removed
face, so at most \(2|T|\) of the disk's triangles avoid \(S\).
A proper subset containing the pooled boundary destination has strict
slack too: its complement consists only of interior vertices \(T\),
and at most \(2|T|-5\) triangles are wholly supported there when
\(|T|\ge3\), with none when \(|T|\le2\). The full set has equal
supply and demand. The finite transport Hall inequalities are therefore
strict for every proper destination subset. Subtracting a sufficiently
small positive allocation at every corner preserves feasibility of the
remaining transport system. Thus a strictly positive angle assignment
exists.

Maximize the sum of the calibrated triangle entropies, with the fixed
boundary linear terms \(\theta_f\log(1/r_f)\). Their derivative
\(-\log\tan(\theta/2)\) diverges positively at a new zero corner.
Moving toward the strictly positive assignment excludes a boundary
maximum. Strict concavity gives one interior maximum. Its multipliers
satisfy
\[
\tan(\theta_{tf}/2)=k_t l_f,\qquad
k_t=\left(\sum_{f<g\in t}l_fl_g\right)^{-1/2},
\qquad l_f=1/r_f>0.
\tag{1}
\]
The boundary multipliers are the prescribed inverse radii, up to the
one common scale absorbed in the row multipliers. The three boundary
angle sums are positive and total \(\pi\), hence each is less than
\(\pi\).

For each triangle glue the Euclidean center triangle with side lengths
\(r_f+r_g\). Its angles are exactly (1). The total angle at every
interior vertex is \(2\pi\); continuation around that vertex fixes
its center and rotates by \(2\pi\), so has zero translational as
well as rotational holonomy. These loops generate the punctured
disk's holonomy. The development is therefore globally defined. Its
boundary is the convex triangle with the prescribed three side lengths,
traversed once. For a point away from the developed edges, the number
of preimages is its boundary winding number: one inside and zero
outside. Local injectivity extends this across edges and vertices.
The development is an embedding.

Place the radius-\(r_f\) disk at each developed center. In one center
triangle the opposite center edge is covered by its two vertex disks,
both disjoint from the third disk. Their mutual contact lies strictly
outside the third disk, and its two contacts with those disks occur
on the other two center edges. Thus the third disk's sector stops
strictly before the opposite edge. The sectors assemble to full disks
at interior vertices and to the prescribed boundary-disk sectors.
This proves disjoint interiors and excludes unintended contacts,
including across separating triangles.

The circle through a center triangle's three tangency points is its
incircle: its contact distance along a center edge is exactly the
corresponding radius. It is orthogonal to the three vertex circles.
Its disk contains no other packing contact. On the omitted outer
triangle choose the opposite side of its contact circle; all interior
contacts lie in its bounded curvilinear gap. The resulting white and
shaded supporting halfspaces contain every contact, strictly unless
incident. Their exposed faces form the full closed labeled sphere,
so the convex hull has exactly those facets and no additional face.
Every ideal vertex has alternating white/shaded faces and successive
right angles. This constructs the required convex ideal right-angled
polyhedron. The proof did not use a height ordering or a flat plat.

Sending any chosen MAIN contact to infinity turns its adjacent white
circles into two parallel marked lines. Every other disk is finite in
their common strip. Thus the required marked complete packing follows
from the finite combinatorial starting hypothesis.

## 2. Why any finite sequence of insertions remains convex

Fix an old shaded triangular face. Its three incident white disks
are pairwise tangent. Apply an orientation-preserving Möbius map for
this local verification that sends one of the three contacts to
infinity. After a Euclidean similarity the incident disks are the
halfplanes
\[
\operatorname{Im}z\le0,\qquad \operatorname{Im}z\ge2,
\]
and the unit disk centered at \(i\). Choose the right-hand
interstice. The old shaded outward disk is \(\operatorname{Re}z>0\).
The new white disk is the unit disk centered at \(2+i\). Its contacts
with the old three white disks are \(2\), \(2+2i\), and \(1+i\).

The three new shaded outward disks are exactly
\[
|z-1|<1,\qquad |z-(1+2i)|<1,
\qquad \operatorname{Re}z>2.
\tag{2}
\]
They lie inside the old shaded outward disk. The six old/new contact
points are the vertices of an ideal right-angled octahedron attached
along the old face. Its three adjacent white planes coincide with
the old white planes, so those seams disappear as flat seams.

There is no intersection with a remote part of the old polyhedron.
Every bounded shaded disk lies inside its developed center triangle.
Distinct center-triangle interiors are disjoint. A nonincident white
disk is covered, inside the carrier triangle, by the sectors of its own
incident center triangles; its part outside the carrier triangle cannot
meet a bounded shaded disk. For the omitted outer face, all other
contacts and disks lie inside its contact circle and therefore miss
its chosen exterior disk. These facts prove that the old shaded
outward disk is disjoint from every other old shaded disk and every
nonincident old white disk. Möbius normalization preserves this
disjointness. The three incident white disks are already included in
the local model. Consequently every new contact satisfies all retained
old supporting inequalities, strictly when not incident. Conversely
all old contacts outside the replaced face satisfy the new inequalities
because the disks in (2), and the new white disk, occupy the old
interstice side. The old attaching contacts have exactly their stated
new incidences.

The retained and new exposed facets form the boundary of the union
of the old ball and this octahedron along one disk. They make a closed
labeled sphere of supporting faces. Therefore the union is the
intersection of these inward halfspaces and is convex. This verifies
the full certificate, not merely its local dihedral angles or volume.

The same argument applies to either shaded face of any original
crossing circle and to any newly exposed face. A later insertion lies
in a nested chosen interstice and leaves all preceding circles fixed.
Disjoint triangles may be treated in either order. Only finitely many
steps are used, so no limiting accumulation or degenerate face is
being asserted. Cycles elsewhere in the original diagram do not enter
this supporting-halfspace argument.

The normalization used to prove (2) need not preserve the global marked
coordinate: it is one Möbius verification of a labeled local operation,
then transported back. In the actual global marked coordinate the
original protected lines remain fixed. This includes a triangle with
one or two protected line faces; the parallel-line model above treats
the latter directly. The positive Descartes formula for the newly
inserted curvature is unchanged.

## 3. From a matched sphere to an actual knot diagram

Conversely begin with any finite oriented simple triangulated sphere
with at least four vertices and a chosen perfect matching of its cubic
dual. Two matched triangles share one edge, have distinct third vertices,
and form an embedded quadrilateral with four distinct boundary vertices.
Choose disjoint small neighborhoods of the matched dual edges and their
endpoints. Contracting these disks gives a connected planar four-valent
graph. At each disk use the original ordered untwisted pairing
\((0,1),(2,3)\); join the outside terminals by the embedded nonmatching
dual edges. Put the standard perpendicular crossing circle in a disjoint
three-ball neighborhood of each disk. This constructs an augmented
link in \(S^3\), with exactly the prescribed cut graph and disk frames.

Choose a regular height after straightening each local box in its
orientation-preserving frame. The outside arcs give finitely many
ordinary cups and caps and no new crossing. This is the literal
general Morse diagram, not an assumed flat-plat presentation. A MAIN
edge may be chosen for the original reduced mark.

The graph whose vertices are the untwisted main circles and whose
edges are the crossing boxes is connected. Otherwise the union of
boxes and outside arcs would split the connected planar graph.
Choose a spanning tree of this graph and give exactly those boxes
odd parity. Switching one tree edge to the odd pairing joins two
different current circles. Induction along any order of the tree
edges gives one main component, with no internal extra component.
The odd signs are arbitrary. Subsequent full twists preserve this
pairing, and the even terminal fans preserve it as well. This proves
the combinatorial corollary without asserting that every arbitrary
tensor graph is a knot diagram.

## 4. The precise metric completion theorem used after filling

The authoritative general statement is
`general_source_regulator_hyperbolic_equality.md`, Sections 1--5.
Let \(Y\) be the actual complete finite-volume augmented exterior,
with its actual primitive peripheral bases. There is one neighborhood
of its complete framed representation such that every representation
in that neighborhood with parabolic unfilled peripheral groups and
actual small logarithms satisfying
\[
U_e+p_eV_e=-2\pi i
\tag{3}
\]
is the holonomy of a smooth complete hyperbolic metric on the specified
filled exterior. The neighborhood is chosen before the slopes.

Here are the construction and the period check. On a compact truncated
core choose a finite lifted partition of unity \(\eta_{j,\gamma}\).
In the future hyperboloid form
\[
Y_\rho(x)=\sum_{j,\gamma}\eta_{j,\gamma}(x)
 \rho(\gamma)\rho_0(\gamma)^{-1}x,
\qquad
E_\rho(x)=\frac{Y_\rho(x)}{\sqrt{-\langle Y_\rho(x),Y_\rho(x)\rangle}}.
\tag{4}
\]
The sum is future timelike and equivariant. On a compact fundamental
part it is \(C^1\)-close to the identity, hence an oriented local
diffeomorphism for nearby representations.

In a cusp frame sending the selected flag to infinity, write the
peripheral affine action as \(A_\rho(\lambda)z=a_\lambda z+b_\lambda\)
on the original translation lattice \(\Lambda\). A smooth periodic
partition of unity gives
\[
d_\rho(w)=\sum_{\lambda\in\Lambda}\eta(w-\lambda)
 A_\rho(\lambda)(w-\lambda),
\qquad
F_\rho(w,t)=(d_\rho(w),e^{t+\chi_\rho(w)}),
\tag{5}
\]
where \(\chi_\rho\) is the real-linear extension of
\(\log|a_\lambda|\). The first map is a positive local
diffeomorphism and is exactly affine-equivariant; the second is an
equivariant positive local diffeomorphism for the entire cusp tail.
It is \(C^1\)-close to the old development on a compact collar.
Geodesic interpolation with (4) gives a global developing local
diffeomorphism on the original manifold with its ideal ends removed.

At a filled cusp, commuting nontrivial affine multipliers have a common
finite fixed point \(q=b/(1-a)\). Near the complete representation
the original generator translations stay nonzero, so \(|q|\to\infty\).
The developed fundamental parallelogram and fixed generator paths of
\(d_\rho\) remain bounded. Hence they miss \(q\), and equivariance
makes the entire development miss it. On the simply connected link
cover set \(f=\log(d_\rho-q)\). Its invariant differential gives a
complete nonsingular flat metric \(|df|^2\) on the compact torus.
The lifted local isometry is therefore a global Euclidean development,
and its periods form an injective rank-two lattice.

If a fixed generator path has image length at most \(L\) inside
\(|d|\le R\), its logarithmic increment is at most
\(L/(|q|-R)\), tending to zero. Its exponential is the corresponding
peripheral multiplier. Both this increment and the prescribed small
multiplier log tend to zero, so their difference, an integral multiple
of \(2\pi i\), is exactly zero in one fixed neighborhood. The
periods are thus the actual \(U,V\), before multiplication by any
large slope coefficient. This excludes a hidden winding in (3).

Translate \(q\) to zero. The tail contains an entire equivariant
epigraph \(y>A|d|\). Put
\[
R=\operatorname{arsinh}(|d|/y),\qquad
\theta=\operatorname{Im}f,\qquad
X=\operatorname{Re}f+\tfrac12\log(1+y^2/|d|^2).
\]
Direct substitution gives the hyperbolic tube metric
\[
ds^2=dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2.
\tag{6}
\]
The tail contains a full punctured tube. Equation (3) gives angular
period \(-2\pi\) and zero longitudinal period on the primitive
meridian. A complementary primitive curve has nonzero real log period,
because the log lattice has real rank two. Adding \(R=0\) therefore
gives a smooth solid torus, with exactly the original filling slope.
Its affine meridian fixes both \(q\) and infinity and has multiplier
one, so the representation also descends to the filled group.

At an unfilled cusp both multipliers are one. Formula (5) then gives
a translation-equivariant complete Euclidean link and a full horoball
quotient. In our construction the main meridian is noncentral
parabolic throughout; its commuting longitude has multiplier one as
well. Thus the main cusp remains complete and unfilled. The remainder
of the manifold is compact, so the completed metric is finite-volume
and complete. Its universal developing local isometry covers
\(\mathbb H^3\), giving discrete faithful holonomy.

The selected first-charge source solution lies in this fixed framed
neighborhood once all fixed powers are sufficiently long. The common
circle pattern, full collar matrices and selected flags converge to
their original complete values; this is stronger than convergence of
peripheral traces. Consequently (3)--(6) identify the actual smooth
filled \(S^3\) knot complement. The regulator identity then calibrates
the source action to that metric's volume. It does not replace the
completion argument.
