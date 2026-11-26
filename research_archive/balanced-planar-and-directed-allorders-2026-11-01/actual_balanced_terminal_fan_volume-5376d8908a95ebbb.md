# Balanced terminal decorations and volume limits beyond tangle-operation trees

A crossing circle surrounds two strands and bounds their twice-punctured disk. A terminal decoration inserts another such two-strand piece in an actual product collar on one side of an original crossing disk. The original diagram may have arbitrary cycles; it is not required to be built from a tree of two-strand products.

The starting condition is combinatorial: the actual connected augmented diagram has a simple triangulated white sphere, with its recorded crossing-disk matching and cyclic orders. The proof constructs its positive right-angled geometry, then adds the terminal pieces so that one shared complete circle packing controls every sector of the original quantum source. All data are fixed before the level tends to infinity.


## 1. The theorem and its quantifiers

Let \(D\) be a fixed connected augmented link diagram with the following data.

* Its white triangulation is a simple triangulated sphere, with the original perfect matching of dual triangles and four distinct white vertices at each matched quadrilateral.
* Its simple white sphere has at least four vertices; the positive geometric certificate is constructed below, not imposed separately.
* A strand edge, meaning a nonmatching side in the white triangulation and called MAIN in the source formulas, is marked. The associated two protected white curvatures are zero in the actual marked complete packing.
* The cyclic order, original half-twist frame and disk-framed meridian/longitude at every crossing circle are fixed.
* A parity vector for the original boxes makes their filled main strands a knot, with no internally closed extra component.

There is a finite literal terminal decoration \(\widehat D\) of this diagram with even numbers of new terminal pieces on both sides of each original box such that:

1. The original endpoint pairing and knot condition are preserved when each new terminal power is odd.
2. The refined white sphere is simple, has its actual positive cut certificate, and its one marked complete packing satisfies the strict complete-radius balance inequalities at every old and new crossing circle.
3. There is a threshold \(T(\widehat D)\) such that, for every fixed integer filling vector \(p\) with all \(|p_e|\ge T(\widehat D)\), independently in sign and size, and the recorded retained half twists \(\epsilon_e\in\{-1,0,1\}\), the actual powers \(n_e=\epsilon_e-2p_e\) produce a hyperbolic knot \(K_p\) and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_p)|
       =\operatorname{Vol}(S^3\setminus K_p).
 \tag{T1}
\]
Here \(K_N\) is the original zero-framed reduced complete-color invariant at \(q_N=e^{\pi i/N}\), with its recorded enhanced component convention. Both parities of \(N\) occur. The same logarithmic conclusion holds in the specified full one-cut modified convention after retaining its known polynomial-level conversion.

The diagram, decorations and signed powers are fixed before \(N\). The threshold may depend on the whole decorated diagram; there is no uniform bound over all cores or a growing-diagram limit. The core's original powers are also filled sufficiently long in this theorem. The result is not an assertion for arbitrary short fillings of the core. The decorated knot generally differs from the core knot.


## 2. A simple sphere supplies the actual metric


### A combinatorial starting hypothesis

It is enough to start with an actual connected marked augmented diagram
whose white cellulation is a simple triangulated sphere with at least
four vertices. The matching pairs, cyclic orders and marked MAIN edge
are those of its projection/crossing-disk cut. A positive geometric
certificate need not be supplied independently.

The following construction gives the packing, embedding and supporting halfspaces explicitly, with the calibrated entropy of [the simple-block capacity proof](actual_smoothed_source_capacity_blocks.md). Remove one triangular
face \(abc\), prescribe positive radii at its three vertices, and let
\(v\) be the number of remaining interior vertices. The disk has
\(2v+1\) triangles. Give every interior vertex angle demand \(2\pi\),
and pool the three boundary vertices into one destination with demand
\(\pi\), retaining the separate boundary corners.

A nonempty interior subset \(S\) touches at least \(2|S|+1\) disk triangles.
To see this, puncture the sphere at a vertex of \(S\). The complementary
simple planar graph on the other interior vertices \(T\) and \(a,b,c\)
has at most \(2|T|+1\) bounded triangular faces. One is the removed
face, so at most \(2|T|\) of the disk's triangles avoid \(S\).
A proper subset containing the pooled boundary destination has strict
slack too: its complement consists only of interior vertices \(T\),
and at most \(2|T|-5\) triangles are wholly supported there when
\(|T|\ge3\), with none when \(|T|\le2\). The full set has equal
supply and demand. The finite transport Hall inequalities are therefore
strict for every nonempty proper destination subset. Subtracting a sufficiently
small positive allocation at every corner preserves feasibility of the
remaining transport system. Thus a strictly positive angle assignment
exists.

For an angle triple of sum \(\pi\), use
\[
 \mathcal V(\theta)=2\sum_{j=1}^3
 [\Lambda(\theta_j/2)+\Lambda((\pi-\theta_j)/2)],
 \qquad \Lambda(t)=-\int_0^t\log|2\sin u|\,du .
 \tag{G0}
\]
Its corner derivative is \(-\log\tan(\theta_j/2)\), and its one-corner endpoint value is zero. Maximize the sum of these calibrated triangle entropies, with the fixed
boundary linear terms \(\theta_f\log(1/r_f)\). Their derivative
\(-\log\tan(\theta/2)\) diverges positively at a new zero corner.
Moving toward the strictly positive assignment excludes a boundary
maximum. Strict concavity gives one interior maximum. Its multipliers
satisfy
\[
\tan(\theta_{tf}/2)=k_t l_f,\qquad
k_t=\left(\sum_{f<g\in t}l_fl_g\right)^{-1/2},
\qquad l_f=1/r_f>0.
\tag{G1}
\]
The boundary multipliers are the prescribed inverse radii, up to the
one common scale absorbed in the row multipliers. The three boundary
angle sums are positive and total \(\pi\), hence each is less than
\(\pi\).

For each triangle glue the Euclidean center triangle with side lengths
\(r_f+r_g\). Its angles are exactly (G1). The total angle at every
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

## 3. The original link and a knot parity


### From a matched sphere to an actual knot diagram

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

## 4. The explicit two-sided fan construction


### Why any finite sequence of insertions remains convex

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
\tag{O2}
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
because the disks in (O2), and the new white disk, occupy the old
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

The normalization used to prove (O2) need not preserve the global marked
coordinate: it is one Möbius verification of a labeled local operation,
then transported back. In the actual global marked coordinate the
original protected lines remain fixed. This includes a triangle with
one or two protected line faces; the parallel-line model above treats
the latter directly. The positive Descartes formula for the newly
inserted curvature is unchanged.

### Input and the local geometric operation

Start with a connected augmented diagram whose labeled white
triangulation is a simple triangulated sphere and whose matching pairs
are the original crossing circles. Retain the original marked MAIN
edge and its two protected zero curvatures. Use the actual positive complete packing constructed above. An original crossing circle
has ordered weights

\[
(x,b,c,y),\qquad A=x+y>0,\qquad P=xy,\qquad
\delta=P/A^2\in[0,1/4].                                      \tag{F1}
\]

Its matching edge is \(xy\), and its two shaded triangles are
\((x,b,y)\) and \((x,c,y)\). The letters in (F1) denote circle curvatures,
not independent choices of radii for different source factors.

Stellarly subdivide the first triangle by its positive interstice circle

\[
b_1=A+b+2\sqrt{Ab+P}.                                      \tag{F2}
\]

Retain \(xy\) as the old matching edge and match the other two new
triangles along \(bb_1\). Thus the two resulting crossing circles have unordered
outer/middle pairs

\[
\begin{array}{c|c|c}
 &\text{outer pair}&\text{middle pair}\\ \hline
\text{retained crossing circle}&(x,y)&(b_1,c)\\
\text{new crossing circle}&(b,b_1)&(x,y).
\end{array}                                                   \tag{F3}
\]

Their oriented four-leg frames are inherited from the local disk
insertion, rather than chosen afterwards from this table.

This is a literal terminal-tangle insertion. In the endpoint convention
of [actual_all_circle_octahedral_decomposition.md](actual_all_circle_octahedral_decomposition.md), take the unturned
old box \(P_v=T^{-1}h_v\), with exposed tuple
\((v_3,v_0,v_1,v_2)\). If \(x_1,x_2\) are its two current output
neighbors, inserting \(h_w\) immediately after \(P_v\) replaces

\[
\begin{array}{c|c}
v_1-x_1&v_1-w_1,\quad w_2-x_1\\
v_2-x_2&v_2-w_0,\quad w_3-x_2.
\end{array}                                                   \tag{F4}
\]

The endpoint calculation uses only this framed product collar. The
outside arcs may belong to an arbitrary fixed diagram; they need not
come from a tree. The left insertion replaces \(v_3-x_3\) by \(v_3-w_3,w_0-x_3\), and \(v_0-x_0\) by \(v_0-w_2,w_1-x_0\). It gives the second side without changing the inherited frame.
The octahedron in that reference attaches to precisely the shaded face
being subdivided. Its three other shaded faces give (F3), with the old
and new white boundary cycles fixed by (F4).

All old circles remain fixed. The new disk lies in the chosen
interstice, and the positive Descartes solution is (F2). The supporting
planes and opposite ideal vertices are those of the regular octahedron
attached across the old ideal triangle; this is also the literal
construction in [actual_smoothing_fixed_radius_gap.md](actual_smoothing_fixed_radius_gap.md), Section 3.
Consequently the same complete labeled certificate extends to the new
diagram. This attaches one regular octahedron in each projection copy,
so the augmented volume increases by \(2v_{\mathrm{oct}}\) per insertion.
This geometric statement uses the face attachment, not just its volume.

The protected zeros remain zero. Their marked MAIN edge is a boundary
edge of every subdivision containing it and is not removed. The
formulas include a zero middle and one zero outer curvature. In the
case with two protected lines, (F2) is the corresponding positive
interstice disk between those lines. Since \(A>0\), no three-zero
triangle occurs.

### Exact fan recurrence and even counts

Repeat the operation only at the retained crossing circle, on the same side. Put
\(t_j=\sqrt{Ab_j+P}\). Direct substitution into (F2) gives

\[
t_{j+1}=t_j+A,\qquad
b_j=b+2j\sqrt{Ab+P}+j^2A.                                  \tag{F5}
\]

The positive square root is essential here. Normalize

\[
u=\sqrt{b/A+\delta},\qquad v=\sqrt{c/A+\delta}.
\]

After \(j\) insertions on the first side and \(k\) on the second,

\[
b_j=A[(u+j)^2-\delta],\qquad
c_k=A[(v+k)^2-\delta].                                    \tag{F6}
\]

There are even nonnegative integers \(j,k\) with

\[
U=u+j\ge4,\qquad V=v+k\ge4,\qquad |U-V|\le1.              \tag{F7}
\]

Indeed choose an integer \(m\) nearest \(-(u-v)/2\). Then
\(|u-v+2m|\le1\). Set \(j=2(L+m)\), \(k=2L\), and take the
integer \(L\) large enough to make both counts nonnegative and both
quantities in (F7) at least four. Adding the same even count to both
sides preserves the difference condition.

Give each inserted terminal an odd crossing power. Its turned
four-terminal pairing is the crossing pairing, so an even stack has
the identity pairing and creates no internal component. Hence these
two even fans preserve the original box's four-endpoint pairing. In
particular a specified knot parity pattern of the core remains a knot
pattern. The new fillings may have independently chosen sufficiently
large odd positive or negative powers. This preserves endpoint
connectivity, not the isotopy type of the filled core knot.

### An exact integral for the source-normalized triangle action

Let \(F(x,b,y)\) be the complete triangle action with the original
determinant, beta and half-forced-product normalization. Its exact
entropy definition is

\[
F(x,b,y)=\max_{\alpha_x+\alpha_b+\alpha_y=1/2}
\left\{\sum_j f(\alpha_j)+\alpha_x\log x+
\alpha_b\log b+\alpha_y\log y\right\},                     \tag{F8}
\]

where \(f'(t)=\log\cot(\pi t)\), \(f(0)=f(1/2)=0\), and zero
weights force zero allocation. The complete stationary middle load is

\[
\frac{\partial F}{\partial\log b}
=\frac1\pi\arctan\frac{b}{\sqrt{Ab+P}}.                   \tag{F9}
\]

These are the calibrated identities in
[actual_triangle_entropy_algebraic_balance.md](actual_triangle_entropy_algebraic_balance.md) and
[actual_cross_cofactor_marked_action.md](actual_cross_cofactor_marked_action.md); no additive entropy constant
is available to change.

Homogeneity of (F8) gives
\(F(x,b,y)-\tfrac12\log b=F(x/b,1,y/b)\to0\) as \(b\to\infty\).
For completeness, the vertex allocation to the middle has value zero.
Any maximizing allocations along a sequence with the two outer weights
tending to zero must have their outer allocations tending to zero:
otherwise the bounded continuous entropy cannot offset the negative
log-weight term. Their entropy then tends to zero, proving the upper
limit as well. Integrating (F9) from infinity therefore gives exactly

\[
F(x,b,y)=\tfrac12\log b+R(b),\qquad
R(b)=\frac1\pi\int_b^\infty
\arctan\frac{\sqrt{At+P}}t\,\frac{dt}{t}>0.                \tag{F10}
\]

The integral converges by its \(O(t^{-3/2})\) integrand. It is also
valid when one outer curvature is zero.

Using \(P\ge0\), monotonicity of arctangent, and
\(\arctan z\ge z-z^3/3\) for \(z\ge0\), we obtain

\[
R(b)\ge \frac2\pi\sqrt{A/b}
-\frac2{9\pi}(A/b)^{3/2}.                                \tag{F11}
\]

### Strict balance at the retained crossing circle

Assume (F7), and exchange the two sides if necessary so that
\(U\ge V\). Put \(b'=A(U^2-\delta)\),
\(c'=A(V^2-\delta)\). They are positive. Since
\(w\mapsto 2w-2w^3/9\) is increasing on the range in use,
(F11) and \(\delta\le1/4\), \(U,V\ge4\), give

\[
R(b')+R(c')\ge
\frac2\pi\left(\frac1U+\frac1V\right)
-\frac2{9\pi}\left(\frac1{U^3}+\frac1{V^3}\right)
\ge\frac{643}{180\pi V}.                                 \tag{F12}
\]

For the last inequality use \(U\le V+1\le5V/4\) and
\(V^{-3}\le(16V)^{-1}\). On the other hand,

\[
\frac12\log(b'/c')
=\int_V^U\frac{t}{t^2-\delta}\,dt
\le\frac{64}{63V}.                                      \tag{F13}
\]

The rational bound \(\pi<22/7\) proves

\[
\frac{643}{180\pi}-\frac{64}{63}
>\frac{3347}{27720}>0.                                  \tag{F14}
\]

It follows from (F10)--(F14) that the original retained crossing circle has

\[
F(x,b',y)+F(x,c',y)-\max(\log b',\log c')
>\frac{3347}{27720\min(U,V)}>0.                          \tag{F15}
\]

Thus it satisfies the true complete-radius balance condition, including
the source's exact absolute normalization. The simpler algebraic
sufficient test need not hold here; using it instead of (F10) would lose
the construction.

### Every added crossing circle already balances

At an insertion with current middle \(b\), the new crossing circle has outer sum
\(A'=b+b_1\) and middle pair \((x,y)\). From (F2),

\[
A'\ge A=x+y\ge\max(x,y).
\]

Consequently

\[
(A'+x)(A'+y)\ge\max(x^2,y^2).                            \tag{F16}
\]

The source-normalized entropy inequality
\(F(a,t,d)\ge\tfrac12\log(a+t+d)\), strict when two weights are
positive, shows that (F16) implies the required strict balance for every
positive middle. A zero middle needs no logarithm; its overloaded
one-sided finite sector is absent. Since \(A'>0\), this covers all
protected-zero cases too.

Later fan steps subdivide only the retained crossing circle's triangle. No
previously added crossing circle changes again. Performing the construction at
different original crossing circles likewise preserves their already fixed
curvatures and all previously settled crossing circles. There are finitely many
original crossing circles. Hence the procedure terminates with one actual marked
complete packing in which every crossing circle balances strictly.

The construction therefore proves a geometric realization theorem:
every fixed certified simple-white core has a finite two-sided terminal
decoration, with even fan sizes, preserving its knot endpoint pairing
and original marked edge, whose entire complete packing satisfies the
true radius-balance inequalities. The sizes depend on the original
packing; no uniform count or bridge-width assertion is made.

## 5. The full finite source at both level parities


### The literal insertion

Start with a connected augmented diagram whose labeled white triangulation is a simple sphere and whose matched cubic dual is its actual projection/crossing-disk cut. At a matching side \(xy\), write the triangles as
\[
 (x,b,y),\qquad (y,c,x).
 \tag{S1}
\]
The old box has outer faces \(x,y\), input middle \(b\), and output middle \(c\). A terminal insertion on the first shaded side gives
\[
 (x,b,y)\longmapsto (x,b,w),\ (b,y,w),\ (y,x,w).
 \tag{S2}
\]
The triples in (S1)–(S2) carry the orientation of the original projection sphere. Removing the common side \(bw\) from the first two new triangles leaves the boundary walk \(b\to y\to w\to x\to b\); hence its cyclic quartet is \((b,y,w,x)\). The triangle \((y,x,w)\) and the unchanged neighbor \((y,c,x)\), joined across \(xy\), have boundary walk \(x\to w\to y\to c\to x\). Thus their retained quartet is \((x,w,y,c)\). This derives both frames from their oriented boundaries, not from a reflection symmetry of the entropy.

The old matching side \(xy\) now has input/output middles \(w,c\). The new matching side \(bw\) has the orientation-preserving cyclic quartet \((b,y,w,x)\): its outer faces are \(b,w\), its input middle is \(y\), and its output middle is \(x\). Its signed crossing power is measured in precisely that frame. No reflection of the new coupon is used.

This is a physical insertion, not an arbitrary change of matching. Expose the old box as \(P_v=T^{-1}h_v\), with half-segment tuple \((v_3,v_0,v_1,v_2)\). A terminal child on its right changes exactly
\[
 \begin{array}{c|c}
 v_1-x_1&v_1-w_1,\quad w_2-x_1\\
 v_2-x_2&v_2-w_0,\quad w_3-x_2 .
 \end{array}
 \tag{S3}
\]
On the other side the changes are
\[
 \begin{array}{c|c}
 v_3-x_3&v_3-w_3,\quad w_0-x_3\\
 v_0-x_0&v_0-w_2,\quad w_1-x_0 .
 \end{array}
 \tag{S4}
\]
These are the actual stack and inverse-turn formulas in [the ordered disk decomposition](actual_all_circle_octahedral_decomposition.md), sections 2–3. The formulas use only the two specified strips, and explicitly allow their other ends to lie outside the local ball. They therefore apply inside a non-tree exterior. All other strips remain fixed. The accompanying shaded-sector boundary walk gives precisely (S2). There is no use of \(T^2=1\) on a labeled ball, no movement of a box through its neighbors, and no omission of an odd seam.

An odd two-strand braid has the diagonal pairing \(X=\{(0,2),(1,3)\}\). Its physical quarter-turn preserves this pairing, so every inserted odd terminal still has \(X\) in the exposed product frame used in (S3) or (S4). Two such consecutive factors compose to the through pairing, with no internal closed component: each of the two through arcs is concatenated once. Any even stack therefore preserves the original four external pairings. This argument uses rotations and the actual strip matches; it invokes neither a mirror reflection nor cancellation of the signed braid operators.


### Endpoint support and the new coefficient target

Fix \(N\ge3\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\). Let \(H_f(x,b,c,y)\) be the original homogeneous degree-\(d\) face polynomial of an arbitrary full coupon \(f(\Omega)\). This includes actual signed crossing powers and cleared resolvent numerators, with all repeated-node data.

The local adapter of [actual homogeneous casimir face source](actual_homogeneous_casimir_face_source.md), its equations (6)–(7a), is
\[
 f(\Omega)_{r,s;u,v}
 =N^{-1}q^{-d(r-u)}c^{-d}H_f(x,b,c,y)
 =N^{-1}\frac{H_f(x,b,c,y)}{(bc)^{d/2}} .
 \tag{S5}
\]
The last equality uses the coherent integer face-log lifts of that physical state. No head is independently reduced modulo \(N\). The physical Casimir lowering arrows vanish at their genuine endpoints; hence a modular output with a wrong unwrapped total has zero coefficient before it is interpreted as a physical state. This is valid for every polynomial in the full Casimir, not only for the complete circle.

After (S2), the two local factors in the numerator are exactly
\[
 H_f(x,w,c,y)\,H_g(b,y,x,w).
 \tag{S6}
\]
Here \(g\) is the new coupon in its actual four-leg frame. Equation (S6) identifies the refined source; it does not equate the old and new invariants or posit a multiplicative rule for quarter-turns.

Let \(M_f\) count middle incidences at boxes and \(T_f\) count outside minus inside Morse turns in face \(f\), temporarily restoring the cap at the marked edge. The change of the two quartets gives
\[
 \delta M_b=-1,\qquad \delta M_x=\delta M_y=1,
 \qquad M_w=1,\qquad \delta M_c=0 .
 \tag{S7}
\]
Round the boxes in their actual frames. Each middle passage contributes \(+\pi\) to boundary turning; the outer pair contributes zero. Inside and outside turns contribute respectively \(+\pi\) and \(-\pi\). The boundary winding is one in a bounded face and minus one in the exterior \(a\). Thus
\[
 M_f-T_f=2\quad(f\ne a),\qquad M_a-T_a=-2 .
 \tag{S8}
\]
This is the literal face-boundary turning calculation of [research matched sphere morse source](research_matched_sphere_morse_source.md), section 5. It uses no flat-plat sweep or assumption of constant headcount.

Every old face retains its winding, while \(w\) is a new bounded face. Subtracting (S8), with (S7), gives
\[
 \delta T_b=-1,\qquad \delta T_x=\delta T_y=1,
 \qquad T_w=-1,\qquad \delta T_c=0 .
 \tag{S9}
\]
A local Morse drawing can have one extra cup and one extra cap; additional cancelling Morse pairs do not change (S9). Therefore all old exponents are unchanged, and the new exponent is
\[
 \frac d2(T_w-M_w)=-d .
 \tag{S10}
\]
The new ordinary coefficient target is exactly \(d\), rather than a free boundary condition.

For even \(N\), the face parity cochain differs by one across MAIN edges and by zero across matching sides. Since \(xy\) is matching, \(t_x=t_y\), and the old triangle has \(t_b=t_x+1\). The unique local extension is
\[
 t_w=t_b,\qquad t_w-t_x=t_w-t_y=1\pmod2 .
 \tag{S11}
\]
Thus \(bw\) has zero parity difference, every new MAIN side has difference one, and all old clocks are unchanged. Swapping the order in which the two new middle faces are read does not change these equations: in the actual frame the input is \(y\), the output is \(x\), and \(t_x=t_y\). The original even-level coset is therefore still exactly (S11).

### The physical mark, measure and normals

Keep a MAIN edge outside the insertion as the mark, with adjacent protected faces \(a,b_*\). The spherical whole-source mark transport may expose it as a top cap; it does not replace an internal marked row by an ordinary cap. The regular generic pivot is \((-1)^HK\), specializing to the original \(K^{1-N}\). Its self-duality and equal left/right traces are proved in [research arbitrary main edge mark transport](research_arbitrary_main_edge_mark_transport.md), sections 2–3, for arbitrary Morse presentations.

In literal left-to-right physical order the cup, cap and mark are
\[
 p_{ij}=Nq^{-d^2+di}\mathbf1_{i+j=d},\qquad
 \ell_{ij}=N^{-1}q^{di}\mathbf1_{i+j=d},\qquad
 m_{ij}=N^{-2}q^{dj}.
 \tag{S12}
\]
The marked row is initially unrestricted. The whole-network degree conservation, after the other actual caps act, forces its two heads to sum to \(d\). Only then is its ratio to the ordinary cap
\[
 \frac m\ell=N^{-1}(L_{b_*}/L_a)^d .
 \tag{S13}
\]
The added cup and cap have cancelling powers of \(N\) and cancelling fixed \(q\)-constants. If the refined diagram has \(R'\) boxes, (S5), (S8) and (S13) make its full marked summand
\[
 N^{-R'-1}\,
 \frac{\prod_{e=1}^{R'}H_{f_e}(L_{x_e},L_{b_e},L_{c_e},L_{y_e})}
      {\prod_{f\ne a,b_*}L_f^d}.
 \tag{S14}
\]

The connected spherical graph has \(R'+2\) faces. The conserved integer head lattice identifies primitively with face potentials modulo one common constant. This follows by integrating along dual paths; zero divergence gives independence of the path on the sphere. Bending a physical arc does not change that lattice. After fixing \(L_a\), there are \(R'+1\) independent \(N\)-point grids. Their count cancels the prefactor in (S14). Thus one insertion gives one new coupon factor \(N^{-1}\) and one new grid factor \(N\), with no residual quantum dimension.

The numerator is homogeneous of degree \(dR'\), with nonnegative exponents, though its coefficients can be complex. The grid requires exponent \(d\bmod N\) at all \(R'\) ordinary faces, and zero modulo \(N\) at the other protected face. The ordinary minimum degrees already sum to \(dR'\). Hence no higher alias is possible: every ordinary exponent is \(d\), and both protected exponents are zero. At even levels the remaining coset character is one. The exact refined scalar is therefore
\[
 I_N=\left[\prod_{f\ne a,b_*}L_f^d\right]
 \left.\prod_{e=1}^{R'}H_{f_e}
       (L_{x_e},L_{b_e},L_{c_e},L_{y_e})
 \right|_{L_a=L_{b_*}=0}.
 \tag{S15}
\]

This holds for arbitrary local full polynomials and their spectral parameters. In particular use
\[
 V_N(\sigma;z)=
  \frac{\chi_N(\sigma)-\chi_N(z)}{\sigma-z},\qquad
 \chi_N(z)=\mathcal T_N(z)+2
 \tag{S16}
\]
as a polynomial before setting \(z=\Omega\). It is the actual cleared resolvent at the root and retains the first derivative at every double Casimir node. No value-only interpolation or paired-channel retraction is used.

If an ordinary generic closure is used instead, the full open regular network is a scalar endomorphism of the generic highest-weight object \(V_d\). Its ordinary closure is \((-1)^d[N]_q\) times that scalar. The one genuine normal at the root recovers (S15). No additional normal occurs at the inserted circle or at a separator. This uses the regular physical lift, not a derivative of an arbitrary fixed-root identity.

### The original signed Fourier/Hermite period

Put the literal nonzero fixed signed braid power \(R^{n_e}\) at each refined box, with \(n_e=\epsilon_e-2p_e\) in its own original disk framing. Define the whole spectral numerator
\[
 S_N(\boldsymbol\sigma)=
 \left[\prod_{f\ne a,b_*}L_f^d\right]
 \left.\prod_{e=1}^{R'}H_{V_N(\sigma_e)}\right|_{L_a=L_{b_*}=0}.
 \tag{S17}
\]
Apply the source-independent local full-Hermite crossing functional separately to each box. Multilinearity of the original ordered contraction, not commutation of different boxes, gives
\[
 \begin{split}
 I_{N,\boldsymbol n}={}&
 q^{\frac{d^2}{4}\sum_e n_e}(-i)^{R'}
 \sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^{R'}}
 \left(\prod_e\ell_e\right)(-1)^{(N+1)\sum_e\ell_e}\\
 &\times\int_{[-1/2,1/2]^{R'}}
 \left(\prod_e\sin(2\pi\delta_e)\right)
 S_N(-2\cos(2\pi\boldsymbol\delta))\\
 &\qquad\times
 \exp\!\left\{N\sum_e[\pi i n_e\delta_e^2+2\pi i\ell_e\delta_e]\right\}
 d\boldsymbol\delta .
 \end{split}
 \tag{S18}
\]
This is [research matched sphere morse source](research_matched_sphere_morse_source.md), section 6, now on the literal inserted network. The Cartan scalar, charge weights, parity and endpoint sine factors have not changed. The original matrix identity excludes charge zero. Three integrations by parts on whole intervals give absolute summability, retaining the second-derivative endpoint currents. No constant-headcount assumption occurs.

The exterior framing/component character remains separately recorded. At complete main color it has modulus one. The full one-cut modified convention also retains its specified polynomial-level factor. These source conversions do not change the exponential rate. The invariant in (S18) belongs to the refined filled link, not to the original unrefined core.

## 6. The calibrated complete action and all-CROSS packet

In the analytic sections write \(D=\widehat D\) for the fixed refined diagram and \(R\) for its number of crossing circles (the \(R'\) in (S14)–(S18)). Put \(\Phi_D=\Phi=\operatorname{Vol}(Y_D)/(2\pi)\). At a local crossing circle write \(Q_t(0)=F(x,t,y)\) for the calibrated triangle action; \(Q_t(\delta)\) is its selected angular continuation from the original cofactor action. Let \(C_N=C_N^{\mathrm{raw}}\) be the shared all-CROSS coefficient, including its sign \((-1)^{dR}\). CROSS is selected by polynomial linearity after the full physical source has been identified; it is not declared to be an independent Hopf coupon.


At the actual marked complete packing, put
\[
\Phi=\sum_e[F(x_e,b_e,y_e)+F(x_e,c_e,y_e)]
       -\sum_{f\ne u,v}\log L_f.
\tag{A8}
\]
Every finite circle has total center angle \(2\pi\). Hence it is a
stationary point of (A8). Its positive finite-face Hessian is
nondegenerate after fixing the common scale: the local positive
triangle Hessians identify adjacent finite-face variations, and the
simple sphere remains connected after deleting \(u,v\). The resulting
one-dimensional kernel before scale fixing is exactly common scaling.
This is the proof used in [actual_original_boundary_transverse_rank.md](actual_original_boundary_transverse_rank.md);
Morse cups/caps do not add a face variable or a Hessian equation.

The absolute constant comes from the actual polyhedron, not a local
choice. For a shaded center triangle with angles \(\theta_j\),
\[
2\pi F-\sum_j\theta_j\log L_j
=2\sum_j\left[\Lambda(\theta_j/2)
                  +\Lambda((\pi-\theta_j)/2)\right].
\tag{A9}
\]
The constant is fixed by \(F(x,0,0)=\tfrac12\log x\). Cone the
marked ideal vertex to the nonincident faces of the certified convex
polyhedron. The white and shaded facet contributions are exactly the
two Lobachevsky terms in (A9); internal diagonals cancel. Summing the
actual facets and their \(2\pi\) angle sums proves
\[
2\pi\Phi=2\operatorname{Vol}(Q)=\operatorname{Vol}(Y).
\tag{A10}
\]
The proof is the facet-coning argument in Section 6 of
[actual_original_boundary_stationary_character.md](actual_original_boundary_stationary_character.md), which explicitly
requires only the connected certificate and marked MAIN edge.

### The CROSS local packet and global spectral gap

We prove the all-CROSS estimates on the exact Morse source. The full one-sided remainder is restored separately below. The graph and its presentation are fixed before the level tends to infinity.

Write \(C_N^{\mathrm{raw}}\) for the original all-CROSS marked coefficient,
including its sign \((-1)^{dR}\), where \(d=N-1\). This source has
\(R+2\) faces and exactly \(R\) original degree-\(d\) ordinary targets.
Simplicity and the protected MAIN edge imply that no matching edge has
both protected endpoints. Hence every local outer sum \(x+y\) is
positive. The remaining zero patterns, including a one-variable triangle,
are precisely those already treated in the actual local cofactor proofs.

The [local interpolant rigidity theorem](actual_cross_cofactor_interpolant_rigidity.md)
and its [exactly anchored interpolation](actual_positive_face_exponential_fold_interpolation.md)
therefore apply to every unchanged local polynomial:
\[
 P_{\mathrm{cross},e}
   =N^2\mathcal B_{e,N}
       \bigl(1+O(e^{-\kappa N})\bigr).                 \tag{P1}
\]
This is uniform on a fixed small complex spectral and face neighborhood.
The original maximal-fold anchor, beta factors, forced products,
half-index, and even/odd central formulas are retained. These theorems
are local finite recurrences and interpolation statements; they have
no hypothesis about the number or order of global Morse events.

For the shared angular complement, deleting the two marked vertices
from a simple triangulated sphere leaves a connected ordinary graph.
The elementary link-rerouting argument in the
[original rank theorem](actual_original_boundary_transverse_rank.md)
proves this without a flat-plat assumption. Every surviving edge lies
in an actual triangle with two nonzero face variables. The
[global cofactor angular theorem](actual_cross_cofactor_global_angular_gap.md)
then detects every nonconstant ordinary phase. A one-variable triangle
is retained as a monomial and contributes no false angular constraint.
All other cofactors have their global polynomial endpoint majorant;
the exact central sums cost only polynomial factors. After fixing one
ordinary phase, the common-phase point is the only angular zero.
The active edge rows are primitive \(+1,-1\) differences, so no
additional angular alias is introduced.

The [positive coefficient saddle theorem](actual_positive_face_coefficient_saddle.md),
sections 2–4, uses this same ordinary graph, the exact determinant
pair-trace bounds, and the complete circle angle-force equation. Its
face Hessian is positive definite on the \(R-1\) dimensional common-scale
quotient. The complete exponent is
\(\Phi=\operatorname{Vol}(Y)/(2\pi)\), with the exact source anchor.
No flat gap forest or constant intermediate headcount enters that proof.

Define the finite phase on that original quotient by
\[
 \Psi_N(z,\delta)=\frac1N\sum_e\operatorname{Log}
       \mathcal B_{e,N}(\delta_e;L(z))
     -\frac dN\sum_{f\ \mathrm{ordinary}}\operatorname{Log}L_f(z).
 \tag{P2}
\]
Uniform local convergence and the positive complete Hessian give its
holomorphic saddle, critical value \(A_N\), and face Hessian \(H_N\).
The new finite compiler gives exactly the original Cauchy measure;
the simultaneous phase integrates to one, leaving
\((2\pi)^{-(R-1)}d\theta\). Deforming that actual torus in its annulus,
with local side faces in the angular gap, gives
\[
 C_N^{\mathrm{raw}}(\delta)=
 \frac{(-1)^{dR}N^{2R}e^{NA_N(\delta)}}
 {(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\delta)}}
 \bigl(1+O(N^{-1})\bigr).                            \tag{PH1}
\]
This repeats only sections 1–3 of the
[original shared packet proof](general_full_spectral_numerator_geometric_packet.md).
All finite normalization factors remain in (P2), and the determinant
branch is continued from the positive real Hessian. The estimate is
relative on one fixed complex polydisk and controls all fixed derivatives
on smaller polydisks. It has a nonzero actual source amplitude.

The finite actions are separately even and real on the real chart.
Their limit is the untwisted action \(A_0\) of the original circle collars, with
\[
 A_0(0)=\Phi,\qquad
 A_0''(0)=-2\operatorname{diag}(C_e),\qquad
 C_e=\frac{\pi(T_{b_e}+T_{c_e})}{x_e+y_e}>0.           \tag{P3}
\]
Here \(T_t=\sqrt{(x+y)t+xy}\), evaluated at the actual complete crossing circle. At least one triangle at every crossing circle is nonmonomial: either both
outers are positive, or one protected outer leaves at least one
positive middle. Thus (P3) is strict at every crossing circle. Shrinking the fixed
chart gives the uniform negative real Hessian required by the spectral
Gaussian argument. Half twists are added only through the original
\(n=\epsilon-2p\) functional (S18).

For the global spectral bound, sections 1–3 of the
[global CROSS theorem](actual_global_cross_spectral_gap.md)
use the signed normalized transfer, all starting rows, and a uniform
upper bound on the original unused logarithmic products. Their local
upper action is
\(\max\{Q_b(\delta),\tfrac12\log b\}\), omitting the second branch
when \(b=0\). It decreases strictly away from \(\delta=0\) except for
the stated exact monomial. Every separated spectral crossing circle therefore
has a strict loss in the product of its two triangle cofactors.
The even/odd central sums keep both triangles in each term.

Outside the common ordinary phase neighborhood, the global cofactor
angular bound supplies a gap uniformly for all real spectra. Inside
that neighborhood, the signed transfer proof supplies its fixed complex
face extension: one separated crossing circle gives a strict loss, while all
others stay below their endpoint rates plus arbitrarily small errors.
The graph has finitely many crossing circles, so choose the errors and strip
small enough that their total is less than that loss. This gives,
for every \(\eta>0\), some \(\tau,\gamma>0\) such that
\[
 |C_N^{\mathrm{raw}}(\delta)|\le e^{N(\Phi-\gamma)}
 \quad\text{if}\quad
 \max_e|\operatorname{Re}\delta_e|\ge\eta,
 \qquad |\operatorname{Im}\delta_e|\le\tau,            \tag{PH2}
\]
on the centered real cube for all sufficiently large \(N\).
Every fixed derivative has the same strict rate on a smaller strip.
This is the shared Cauchy sewing of the global CROSS theorem, with
one set of face radii and the original targets throughout.

Thus (PH1) and (PH2) hold for this actual simple-white Morse source. Constants depend on the fixed graph, complete radii, and zero
patterns; no prescribed flat-plat width is required. For a full-source
filling conclusion, the global one-sided gap proved below must restore the
full numerator. No old Fejér smoothing, pure-middle forest, or flat
full-packet restoration was used here.

## 7. The finite first charge contributes


For a fixed closed local cube \(K_b=[-b,b]^R\), define the integral before its outer charge and Cartan factors by
\[
 J_{N,\boldsymbol\ell}=
 \int_{K_b}\left(\prod_i\sin(2\pi\delta_i)\right)C_N(\boldsymbol\delta)
 \exp\!\left\{N\sum_i[\pi i n_i\delta_i^2+2\pi i\ell_i\delta_i]\right\}
 d\boldsymbol\delta .
 \tag{Lpre}
\]
Only finitely many sharply restricted charge terms are summed in this section. The infinite charge tails will be kept on whole original intervals.

The packet retains its actual finite phase \(A_N\), not only its limiting action. Its local interpolant and unique face saddle are real on the real chart and separately even. Consequently
\[
 \partial_iA_N(\boldsymbol\delta)
 =-2\delta_iB_{i,N}(\delta_1^2,\ldots,\delta_R^2),
 \qquad B_{i,N}\longrightarrow B_i,\quad B_i(0)=C_i>0.
 \tag{L0}
\]
After shrinking one fixed chart, \(|B_{i,N}-C_i|\le C_i/8\) and
\(\Re A_N''\) is uniformly negative definite throughout that complex chart. The ordinary-face determinant branch is continued from the positive complete Hessian. The following proof keeps the actual boundary of a fixed real spectral cube.


### Finite-N filling saddles for independent signed twists

There are fixed $b,a,n_0>0$, with $a$ much smaller than $b$, such that the
following holds for every fixed integer vector $\mathbf n$ with $|n_i|\geq n_0$.
There is no condition on ratios $|n_i|/|n_j|$. For positive real charges
satisfying $\ell_i/|n_i|\leq a$ define

$$
\Phi_{N,\boldsymbol\ell}(\boldsymbol\delta)
=A_N(\boldsymbol\delta)+\pi i\sum_i n_i\delta_i^2
+2\pi i\sum_i\ell_i\delta_i.\tag{L5}
$$

It has a unique critical point $\boldsymbol\delta_{N,\boldsymbol\ell}$ in the chosen small
polydisc. Indeed, writing $t_i=\ell_i/n_i$, its equations are precisely

$$
\delta_i=-\frac{t_i}{1+i B_{i,N}(\boldsymbol\delta^2)/(\pi n_i)}.\tag{L6}
$$

Uniform contraction proves existence, uniqueness and holomorphic
parameter dependence, exactly as in the limiting charge lemma. Bounds
on $B_{i,N}$ and their derivatives are uniform in N. Consequently

$$
|\delta_i|\leq 2|t_i|,\qquad
\operatorname{Im}\delta_i
=\frac{\ell_i}{\pi n_i^2}
\frac{\operatorname{Re}B_{i,N}(\boldsymbol\delta^2)}
{\left|1+i B_{i,N}(\boldsymbol\delta^2)/(\pi n_i)\right|^2}>0.\tag{L7}
$$

In particular $\operatorname{Im}\delta_i\leq C\ell_i/n_i^2$. This sign holds for BOTH
signs of $n_i$. All coordinates of the saddle are nonzero when all
$\ell_i>0$. Write $\boldsymbol\delta_*=x_*+iy_*$, with $y_*>0$ componentwise, and put

$$
S_{N,\boldsymbol\ell}=\Phi_{N,\boldsymbol\ell}(\boldsymbol\delta_*),\qquad
Q_{N,\boldsymbol\ell}=-\Phi_{N,\boldsymbol\ell}''(\boldsymbol\delta_*).
$$

Since the Gaussian contributes a purely imaginary diagonal Hessian,
$\operatorname{Re}Q_{N,\boldsymbol\ell}$ is positive definite. No real or complex eigenvalue of Q
vanishes. The spectral determinant root used below is the unique
Gaussian branch on the convex cone of complex symmetric matrices
with positive real part, positive at a positive real matrix. Thus

$$
\int_{\mathbb R^R}e^{-\frac12 t^TQt}\,dt
=\frac{(2\pi)^{R/2}}{\sqrt{\det Q}}.\tag{L8}
$$

This fixes its phase even when the different $n_i$ have different signs.

For fixed $\mathbf n$ and $\boldsymbol\ell$, $\boldsymbol\delta_{N,\boldsymbol\ell}$ and $S_{N,\boldsymbol\ell}$ converge to the
corresponding limiting critical point and value. No convergence rate
is needed and $A_N$ is not replaced by $A_0$ in a relative formula.

### Deformation of the actual restricted real contour

We prove the requisite contour coefficient, rather than postulate it.
Translate $K_b$ coordinate by coordinate to $K_b+i y_*$. Cauchy's theorem
on each rectangle gives equality with the translated integral plus
its oriented side integrals. The exact integrand is entire in $\boldsymbol\delta$;
the packet is only used to estimate it inside the common local chart.
The side integrals are retained in this equality.

Here is a uniform exponential bound for every side. Its points have
$z=x+iv$ with x in $K_b$, at least one $|x_j|=b$, and $0\leq v_i\leq y_{*,i}$.
Separate reality and the real Hessian bound give

$$
\operatorname{Re}A_N(x+iv)\leq A_N(0)-c|x|^2+C|v|^2.\tag{L9}
$$

To see the quadratic, rather than linear, error in v, Taylor-expand
at the real point x: the first term $i\nabla A_N(x)\cdot v$ is imaginary.
The remaining derivatives are uniformly bounded. The real Gaussian
and charge contribution is

$$
-2\pi\sum_i n_i x_i v_i-2\pi\sum_i\ell_i v_i
\leq Cb\sum_i\frac{\ell_i}{|n_i|}.\tag{L10}
$$

The second term is nonpositive. Equation (L7) bounds the first term,
without using a common sign or a bound on slope ratios. Thus every
side has real phase at most

$$
A_N(0)-cb^2+C|y_*|^2+Cb\sum_i|t_i|.\tag{L11}
$$

The critical value satisfies the complementary estimate

$$
\operatorname{Re}S_{N,\boldsymbol\ell}
\geq A_N(0)-C\sum_i|t_i|^2.\tag{L12}
$$

For completeness, $A_N(\boldsymbol\delta_*)-A_N(0)=O(\sum_i|t_i|^2)$.
The critical equations imply $|n_i x_{*,i}+\ell_i|\leq C|\delta_{*,i}|$;
hence the real quadratic-plus-linear phase
$-2\pi\sum_i(n_i x_{*,i}+\ell_i)y_{*,i}$ has the same bound (and in fact a
smaller additional factor $n_{\min}^{-1}$). This proves (L12) without
bounding the large purely imaginary quantity $n_i\delta_i^2$ by its
absolute value.

First fix b within the source chart, then choose a/b sufficiently
small and $n_0$ sufficiently large. Equations (L11)-(L12) give a fixed
$\kappa_b>0$ such that all sides satisfy

$$
\operatorname{Re}\Phi_{N,\boldsymbol\ell}(z)
\leq\operatorname{Re}S_{N,\boldsymbol\ell}-\kappa_b.\tag{L13}
$$

All polynomial prefactors in the all-CROSS packet, bounded sine factors and finite
side volumes preserve this exponential loss. Thus the actual local
real contour has coefficient +1 on its translated horizontal saddle
plane, with only exponentially small side currents.

On that plane $\Phi'$ vanishes at $x_*+iy_*$, and for every real x in $K_b$

$$
\operatorname{Re}\Phi_{N,\boldsymbol\ell}(x+iy_*)
\leq\operatorname{Re}S_{N,\boldsymbol\ell}-c|x-x_*|^2.\tag{L14}
$$

Indeed the real part of its real-coordinate Hessian is $\operatorname{Re}A_N''$,
which is uniformly negative definite along the entire segment. The
critical point stays a fixed distance from the cube boundary because
$|x_*|\leq2a$ much less than b. This proves the requisite local and
nonlocal estimates on the translated restricted contour. It does
not say anything about the original contour outside $K_b$.

### Relative asymptotic and its nonzero coefficient

Define

$$
a_N(\boldsymbol\delta)
=\frac{\prod_i\sin(2\pi\delta_i)}{\sqrt{\det H_N(\boldsymbol\delta)}}.
$$

The holomorphic Gaussian estimate on (L14), using (L8), yields

$$
J_{N,\boldsymbol\ell}
=(-1)^{dR}\sqrt{2\pi}\,N^{R+1/2}
\frac{a_N(\boldsymbol\delta_{N,\boldsymbol\ell})}{\sqrt{\det Q_{N,\boldsymbol\ell}}}
 e^{N S_{N,\boldsymbol\ell}}
\left[1+O_{\mathbf n,\boldsymbol\ell}(N^{-1})\right].\tag{L15}
$$

The error in the full packet is holomorphic and uniformly $O(N^{-1})$;
Cauchy bounds, or direct Gaussian integration of that error, preserve
(L15). The ordinary Taylor Gaussian error is $O(N^{-1})$, since its odd
first correction integrates to zero; replacing the cube by the full
real Gaussian changes the answer exponentially. The exact side
integrals in (L13) are likewise exponentially small relative to (L15).
Constants may depend on the fixed slopes and charges. No joint
large-twist/large-level error estimate is asserted.

The power and constant follow directly from the two actual integrals:

$$
N^{2R}(2\pi N)^{-(R-1)/2}(2\pi/N)^{R/2}
=\sqrt{2\pi}\,N^{R+1/2}.\tag{L16}
$$

There is no undetermined stationary multiplier. Every sine in (L15)
is nonzero: $\delta_{*,i}$ is nonzero by (L6) and lies in a small disk with
no other zero of $\sin(2\pi\delta_i)$. Both determinant roots are units.
For each fixed $\mathbf n$ and $\boldsymbol\ell$ the coefficient in (L15) converges to a
nonzero number. Therefore the local integral is nonzero for all
sufficiently large N.

Let $U_{N,\mathbf n;b}$ denote the sum of the original contributions in the original Fourier period
with $\ell_i\in\{+1,-1\}$, each restricted to $K_b$. Reflection of one
coordinate $\delta_i\mapsto-\delta_i$ changes $J_{N,\boldsymbol\ell}$ by a minus sign
and also changes $\prod_i\ell_i$ by a minus sign. $S_N$ and the quadratic
phase are separately even, and the parity character is unchanged.
Thus all $2^R$ sign choices contribute exactly equally. With
$S_{N,\mathbf1}$, $\boldsymbol\delta_{N,\mathbf1}$, $Q_{N,\mathbf1}$ defined above,

$$
\begin{aligned}
U_{N,\mathbf n;b}
={}&q^{\frac{d^2}{4}\sum_i n_i}(-2i)^R\sqrt{2\pi}\,N^{R+1/2}\\
&\quad\times\frac{\prod_i\sin(2\pi\delta_{N,\mathbf1,i})}
{\sqrt{\det H_N(\boldsymbol\delta_{N,\mathbf1})}\sqrt{\det Q_{N,\mathbf1}}}
 e^{N S_{N,\mathbf1}}\left[1+O_{\mathbf n}(N^{-1})\right].
\end{aligned}\tag{L17}
$$

The parity cancellation is literal:

$$
(-1)^{(N+1)R}(-1)^{dR}=(-1)^{2NR}=1.
$$

Equation (L17) holds through both level parities and arbitrary
independent signs of the sufficiently long fixed $n_i$. The remaining
$q$ scalar has modulus one and is kept exactly. This proves a nonzero
contributing localized original unit-charge period, not merely the
existence of the corresponding critical point.

### Enlargement to the finite local charge sector

For fixed $\mathbf n$ let $L_i=\lfloor a|n_i|\rfloor$, with $n_0$ enlarged so $L_i\geq1$.
Restrict the original period (S18) to $K_b$ and to $0<|\ell_i|\leq L_i$. This is a finite set after
the twists are fixed. The exact finite version of the monotonicity
calculation applies to $A_N$, because the even phase factorization and $\operatorname{Re}B_{i,N}>0$ hold:

$$
\partial_{\ell_i}\operatorname{Re}S_{N,\boldsymbol\ell}
=-\frac{2\ell_i}{n_i^2}
\frac{\operatorname{Re}B_{i,N}}
{\left|1+iB_{i,N}/(\pi n_i)\right|^2}.
$$

After the same fixed shrink, for every positive charge in this box,

$$
\operatorname{Re}S_{N,\mathbf1}-\operatorname{Re}S_{N,\boldsymbol\ell}
\geq\sum_i\frac{C_i}{2n_i^2}(\ell_i^2-1).\tag{L18}
$$

The harmless constants can be decreased if needed to make this
inequality uniform in all large N. If any nonunit positive charge
exists, the right side has a strictly positive minimum $\eta_{\mathbf n}$ over
that finite set. Formula (L15), the exact charge factors $\prod_i\ell_i$,
and the independent sign symmetry imply that the entire restricted
local charge sector equals (L17) with an additional relative
$O_{\mathbf n}(e^{-\eta_{\mathbf n}N})$ error (or after a smaller $\eta_{\mathbf n}$). If all $L_i=1$,
there are no extra local charges. There is no comparison of an
infinite charge sum and no assertion about charges near an alias.

## 8. Every other Fourier charge is controlled


### Basic bounds, endpoint identities, and parameter choices

The local packet and real concavity bound near zero, together with the shared global spectral gap outside a smaller fixed cube, imply

$$
\sup_{\boldsymbol\delta\ \mathrm{real}}|C_N(\boldsymbol\delta)|
\leq e^{N(\Phi_D+e_N)},\qquad e_N\longrightarrow0.\tag{C5}
$$

Polynomial Bernstein on each cosine variable yields, for any fixed $T$,

$$
|C_N(\boldsymbol\delta)|
\leq\exp\!\left[N(\Phi_D+e_N)+2\pi d\sum_i|\operatorname{Im}\delta_i|\right],
\qquad |\operatorname{Im}\delta_i|\leq T.\tag{C6}
$$

This is a bound for the whole shared polynomial; no factorwise positive-radius majorant is used. For source derivatives, apply Cauchy to (C6) in the required variables. Gaussian derivatives are evaluated separately on real spectator coordinates, avoiding any unwanted large-twist exponential cost.

If a source factor $Z$ is an arbitrary entire polynomial in the $\sigma_i$, its product with $\prod_i\sin(2\pi\delta_i)$ and the fixed Gaussian satisfies

$$
\left.B\right|_{\delta_j=\pm1/2}=0,\qquad
\left.\partial_j B\right|_{\delta_j=1/2}
=\left.\partial_j B\right|_{\delta_j=-1/2}.\tag{C7}
$$

The first derivative is solely the derivative of the sine: the two cosines are both $-1$, the spectral argument is $2$ at both ends, and the Gaussian endpoint value is $e^{\pi iNn_j/4}$. These facts remain true after arbitrary derivatives in other variables, including when one different coordinate is held complex. Thus three integrations by parts give exactly

$$
\begin{aligned}
\int_{-1/2}^{1/2}B e^{2\pi iN\ell_j\delta_j}\,d\delta_j
=(2\pi iN\ell_j)^{-3}\biggl\{
&\left[\partial_j^2B e^{2\pi iN\ell_j\delta_j}\right]_{-1/2}^{1/2}\\
&-\int_{-1/2}^{1/2}\partial_j^3B e^{2\pi iN\ell_j\delta_j}\,d\delta_j
\biggr\}.
\end{aligned}\tag{C8}
$$

The second-derivative endpoint difference is retained. Repeating (C8) over any spectator subset gives at most $3^{R-1}$ boundary/integral terms. Fixed source Cauchy bounds and real Gaussian derivatives cost at most $C_{\mathbf n}N^3$ per differentiated variable; these powers cancel the $N^3$ denominators. After the actual charge factors, every spectator coordinate supplies $|\ell_j|^{-2}$.

Choose a small fixed outer cube $K_B=[-B,B]^R$ inside the fixed local packet chart. Choose $a>0$ much smaller than $B$ so the localized contribution theorem applies uniformly for all positive charges $\ell_i/|n_i|\leq a$. Next choose $0<b<a/4$, with $K_b$ inside the same chart. All these constants depend only on $D$. Below $n_0$ will be enlarged finitely many times, independently of ratios among the $|n_i|$.

### The infinite far-charge union is exponentially small

Use (PH2) at $\eta=1/4$. Choose $\tau>0$ sufficiently small that the source and all required spectator derivatives have a strict bound $e^{N(\Phi_D-\gamma_e)}$ at

$$
\delta_i=\pm\frac12+iv,\qquad 0\leq v\leq\tau.
$$

with every other coordinate real or in a fixed Cauchy neighborhood of radius $\tau$. This uses the separated endpoint coordinate, regardless of the other real coordinates. Shrink $\tau$ and $\gamma_e$ once if needed.

For a positive far charge $\ell_i$, shift its whole interval upwards by $i\tau$, keeping all other integrations on their whole real intervals. Write

$$
B_i(z;\boldsymbol\delta_{\mathrm{other}})
=\sin(2\pi z)e^{\pi i n_iNz^2}C_N(z,\boldsymbol\delta_{\mathrm{other}}).
$$

The exact pair of endpoint currents is

$$
\begin{aligned}
B_i(1/2+iv)-B_i(-1/2+iv)
={}&2i\sinh(2\pi v)\sinh(\pi n_iNv)\\
&\quad\times e^{\pi i n_iN(1/4-v^2)}
 C_N(1/2+iv,\boldsymbol\delta_{\mathrm{other}}).
\end{aligned}\tag{C9}
$$

The other sine/Gaussian factors remain outside this equality. Multiplying the actual Fourier character leaves the endpoint parity $(-1)^{\ell_i}$. Its modulus is one. Both vertical sides were retained; the paired factor vanishes quadratically at $v=0$.

For the paired vertical contribution, apply (C8) in every spectator coordinate. The strict endpoint strip bound and source Cauchy estimates then give, after all original charge weights, an upper bound

$$
C_{\mathbf n}|n_i|N\ell_i\,e^{N(\Phi_D-\gamma_e)}
\left(\prod_{j\ne i}|\ell_j|^{-2}\right)
\int_0^\tau v^2 e^{-2\pi N(\ell_i-|n_i|/2)v}\,dv.\tag{C10}
$$

Here $|\sinh(2\pi v)\sinh(\pi n_iNv)|\leq C|n_i|Nv^2e^{\pi|n_i|Nv}$. No oscillatory-sine substitution is made. For $\ell_i>|n_i|/2+D$, with $D\geq1$, the integral is at most $C/[N^3(\ell_i-|n_i|/2)^3]$. Consequently summing (C10) over this far coordinate and all nonzero spectator charges is bounded by a polynomial factor times $e^{N(\Phi_D-\gamma_e)}$. The exact estimate

$$
\sum_{\ell>M}\frac{\ell}{(\ell-|n|/2)^3}
\leq C\left[D^{-1}+(|n|+1)D^{-2}\right].\tag{C11}
$$

makes the summability explicit. Constants may depend on the fixed $\mathbf n$.

For the upper horizontal contribution, apply the same spectator integrations by parts. Source Cauchy from (C6), in a fixed radius-$\tau$ neighborhood of the spectators, has exponential cost at most $2\pi R\tau N$. The shifted sine is bounded, while the bad-coordinate Gaussian and Fourier factors cost exactly at most

$$
e^{\pi|n_i|N\tau-2\pi\ell_iN\tau}.
$$

Thus the weighted horizontal contribution is bounded by

$$
C_{\mathbf n}\ell_i\left(\prod_{j\ne i}|\ell_j|^{-2}\right)
\exp\!\left\{N\left[\Phi_D+e_N+2\pi R\tau
-2\pi\tau(\ell_i-|n_i|/2)\right]\right\}.\tag{C12}
$$

Choose a fixed $D$ large enough that $2\pi\tau D>2\pi R\tau+2\gamma_e$, and set

$$
M_i=\left\lceil\frac{|n_i|}{2}+D\right\rceil.\tag{C13}
$$

The geometric tail of $\ell_i$ times (C12) is exponentially bounded by $\Phi_D-\gamma_e$ after a harmless decrease of $\gamma_e$ and all large N. Both signs of the far charge obey the same estimate, either by downward shifts or the exact separate-evenness/reflection identity.

Therefore, for some fixed $\gamma_\infty>0$,

$$
\sum_{\substack{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^R\\
\exists i:\ |\ell_i|>M_i}}
\left|\mathcal I_{N,\boldsymbol\ell}^{\mathrm{cross}}\right|
\leq C_{\mathbf n}\operatorname{poly}(N)e^{N(\Phi_D-\gamma_\infty)}.\tag{C14}
$$

Here $\mathcal I_{N,\boldsymbol\ell}^{\mathrm{cross}}$ denotes the full weighted charge term in (S18). Use the union bound over $i$; multiple far coordinates cause no issue. Every other coordinate was summed on its whole original domain after (C8). Finite-N absolute convergence and the displayed dominating series justify all summations. No partial-far exterior with uncontrolled $R$ powers appears: the hypothesis used is the shared all-CROSS endpoint gap, valid for arbitrary real spectator spectra. This is the stronger input missing from the local operator-tail argument.

### The finite charges outside the local scaled box

The remaining set $0<|\ell_i|\leq M_i$ is finite after $\mathbf n$ is fixed. Suppose at least one coordinate $i$ has $|\ell_i|/|n_i|>a$. Reflect charge signs if necessary; the source is separately even, so absolute estimates are unchanged and assume $\ell_i>0$.

On the original real domain outside $K_b$, the shared global spectral gap gives rate $\Phi_D-\gamma_b$. The Gaussian and Fourier factors there have modulus one. No contour estimate is needed for this finite-charge portion.

Inside $K_b$, shift only coordinate $i$ upward by

$$
t_i=\frac{b}{|n_i|}.\tag{C15}
$$

All actual side currents of this small rectangle are retained. The packet and its real-action Taylor bound give, uniformly for $x$ in $K_b$ and $0\leq v\leq t_i$,

$$
\operatorname{Re}A_N(x+iv e_i)
\leq A_N(0)-c|x|^2+Cv^2.\tag{C16}
$$

Reality makes the first Taylor term purely imaginary. The Gaussian-plus-Fourier contribution in this coordinate is

$$
-2\pi n_ix_iv-2\pi\ell_iv
\leq-2\pi|n_i|(a-b)v\leq0.\tag{C17}
$$

On the horizontal translate, $v=t_i$, this costs at least $2\pi b(a-b)$, while the source error is at most $Cb^2/n_0^2$. On either vertical side $|x_i|=b$, (C16) gives at least $cb^2$ loss, and (C17) is nonpositive. Enlarge $n_0$ so $C/n_0^2$ is small. Then the horizontal and both sides have a fixed strict gap $\gamma_{\mathrm{bad}}>0$ below $\Phi_D$, independently of slope ratios. The packet's amplitudes contribute only polynomial factors.

Together with the exterior $K_b$ bound, every such bounded bad charge is exponentially small. There are finitely many of them, so their whole sum obeys the same strict rate with a fixed-n prefactor. No infinite sharp-cube series has been split.

### Finite local charges and the actual unit contribution

It remains to consider the finite set with all $|\ell_i|/|n_i|\leq a$. On the real domain outside the larger $K_B$, the shared global spectral gap gives a fixed loss $\gamma_B$. Inside $K_B$ apply the [localized original contour theorem](general_localized_unit_charge_filling_period.md) to the packet (PH1), using the preceding local argument with its cube parameter set to $B$. It retains the exact side currents, the finite action, the Gaussian determinant branch and all sine/charge/parity factors.

For positive charges the finite critical values satisfy

$$
\operatorname{Re}S_{N,\mathbf1}-\operatorname{Re}S_{N,\boldsymbol\ell}
\geq\sum_i\frac{C_i}{2n_i^2}(\ell_i^2-1).\tag{C18}
$$

All sign-unit choices contribute exactly equally. Every other charge in this finite local box has a positive fixed-n gap. The all-unit local contribution is precisely the first-charge formula above, with its $O_{\mathbf n}(N^{-1})$ relative error and nonzero limiting amplitude. The half twists are included once through $n_i=\epsilon_i-2p_i$.

The limiting unit loss from $\Phi_D$ is $O_D(\sum_i|n_i|^{-2})$. Enlarge the diagram-dependent $n_0$ until this loss is less than one quarter of the minimum of $\gamma_\infty$, $\gamma_{\mathrm{bad}}$, $\gamma_b$ and $\gamma_B$. Also require $a n_0\geq1$ so the unit charge lies in the local box. Since $S_{N,\mathbf1}$ tends to its limiting value, all complementary bounds above are then exponentially smaller than $e^{N\operatorname{Re}S_{N,\mathbf1}}$ for large N. The smallest nonunit gap in (C18) may depend on the fixed vector $\mathbf n$, but remains positive. Combining the finite local sector, bounded bad charges and the absolutely bounded infinite union proves the first-charge asymptotic.

The exact critical volume identity identifies

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|I_{\mathrm{cross}}|
=\operatorname{Vol}(\text{the actual smooth filled exterior}).\tag{C19}
$$

There is no uniform joint growing-twist/level error assertion: the twists are fixed first, while the threshold applies to arbitrary independent signs and magnitudes.

## 9. Restoring the full invariant under balance

At every crossing circle put \(X_e=Q_{b_e}(0)+Q_{c_e}(0)\). The fan proof established \(X_e>\log b_e\) when \(b_e>0\) and \(X_e>\log c_e\) when \(c_e>0\). It also gives \(Q_t(0)>\frac12\log t\) for each positive middle. These are inequalities at the one actual complete marked packing.


### Every sector containing a one-sided crossing circle has a global spectral gap

The [exact path partition](actual_cross_cofactor_factorization.md) is disjoint at both parities. For $N=2m$, LEFT has $j\leq m-1$, CROSS has $i\leq m-1$ and $j\geq m$, and RIGHT has $i\geq m$. For $N=2m+1$, LEFT has $j\leq m-1$, CROSS has $i\leq m\leq j$, and RIGHT has $i\geq m+1$. The odd central zero-step path belongs to CROSS exactly once.

At a fixed crossing circle, the [global weighted LEFT theorem](actual_global_left_weighted_spectral_envelope.md) bounds the actual absolute value, at arbitrary face phases and every real spectral value, by the rate

$$
L_e=\max\left\{\log c,Q_b(0)+\frac12\log c\right\},\qquad c>0.\tag{B3}
$$

If $c=0$, the finite LEFT polynomial vanishes identically because its $c$ exponent is at least $\lfloor N/2\rfloor>0$. Similarly, the RIGHT rate is

$$
R_e=\max\left\{\log b,Q_c(0)+\frac12\log b\right\},\qquad b>0,\tag{B4}
$$

and the RIGHT polynomial vanishes exactly when $b=0$. The strict balance inequality and \(Q_t(0)>\tfrac12\log t\) give $L_e<X_e$ and $R_e<X_e$ whenever the corresponding sector survives. This also resolves the protected monomial exception: if one triangle has $t=0$ and $xy=0$, the sector overloading that zero middle is absent, while the opposite surviving sector uses the strict triangle inequality for its positive middle. If both middles vanish, both one-sided sectors vanish exactly.

The [global CROSS coefficient comparison](actual_cross_cofactor_factorization.md), Section 8, bounds its value on the same face torus by rate $X_e$, with only a polynomial or logarithmic prefactor. Thus the whole local full numerator is bounded by rate $X_e$, and any chosen LEFT or RIGHT factor supplies a fixed strict loss. Since $D$ is fixed, the minimum of its finitely many surviving one-sided gaps is positive. If none survives, the remainder is identically zero and the subsequent conclusion is immediate.

Take any original path sector with at least one one-sided crossing circle and CROSS, LEFT or RIGHT assigned elsewhere. The value bounds are uniform over the original common face Cauchy torus. The same marked target extraction therefore gives, for some $\gamma>0$ and all sufficiently large $N$,

$$
|Z_{\mathrm{sector}}(\sigma_1,\ldots,\sigma_R)|
\leq e^{N(\Phi_D-\gamma)},\tag{B5}
$$

uniformly on the entire real spectral cube $[-2,2]^R$, at both parities. Here $\sum_eX_e$ minus the original ordinary log-radius targets is exactly $\Phi_D=\operatorname{Vol}(Y_D)/(2\pi)$, by the calibrated complete source. The protected variables stay zero throughout. No infimum of a sum of local maxima or independent-radius capacity equality is used.

There are only $3^R-1$ such sectors. Their sum is exactly the full shared numerator minus its all-CROSS part. Thus (B5) also holds for that remainder, after reducing $\gamma$. It is a polynomial of spectral degree at most $d$ in each variable. Multivariate cosine Bernstein extends (B5) to a sufficiently thin fixed complex $\delta$ strip, at cost $\exp[2\pi d\sum_i|\operatorname{Im}\delta_i|]$. Reducing the strip height and $\gamma$ gives the same strict gap there.

### Entire original Fourier remainder and the full invariant

Apply the [whole-domain three-integration-by-parts lemma](actual_global_diagonal_spectral_sector_gap.md), Section 4, to the remainder polynomial. The original sine factors vanish at both endpoints, first derivatives match, and the second-derivative endpoint current is retained. Source derivatives use the fixed strip; Gaussian derivatives are taken only on the real cube. Summing all nonzero original charges with their actual weights and parity gives

$$
|I_{\mathrm{full}}-I_{\mathrm{cross}}|
\leq C_D\prod_i(1+|n_i|)^3e^{N(\Phi_D-\gamma')},\tag{B6}
$$

for a fixed $\gamma'>0$. No infinite sharp-cube charge series is split. All framing and component scalars remain the original ones.

The [entire all-CROSS period theorem](general_all_cross_long_filling_volume.md) supplies a nonzero relative filling asymptotic for every fixed independently signed sufficiently long integer vector $n_i=\epsilon_i-2p_i$. Its unit critical rate tends to $\Phi_D$ as $\min_i|n_i|$ tends to infinity, with loss $O_D(\sum_i n_i^{-2})$. Choose a diagram-dependent threshold so this loss is less than $\gamma'/2$ and all existing geometric and analytic filling thresholds hold. Then (B6) is exponentially smaller than the complete all-CROSS asymptotic. Thus

$$
\frac{I_{\mathrm{full}}}{I_{\mathrm{cross}}}
=1+O_{\mathbf n}(e^{-c_{\mathbf n}N}),\tag{B7}
$$

and

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|I_{\mathrm{full}}|
=\operatorname{Vol}(\text{the actual smooth filled exterior}).\tag{B8}
$$

The same conclusion holds after multiplying by the separately recorded original normalization characters and nonzero polynomial-level factors. For the prescribed parity yielding a knot, this is the corresponding full original knot invariant, not a chosen spectral contribution. It does not assert that a given $2k$-plat has minimal bridge number $k$.

The quantifiers are: for this fixed decorated diagram satisfying the balance inequalities, there exists $T(D)$ such that every independently signed fixed filling vector with all $|p_i|\geq T(D)$, in the prescribed parity convention, has (B7)–(B8) as $N\to\infty$. No bound on ratios $|p_i|/|p_j|$ is needed. There is no joint growing-twist/level estimate or uniform threshold over different diagrams or widths.

## 10. The original primitive geometric action


### Primitive geometry on the refined Morse diagram

The geometric verification also uses the actual Morse presentation,
not a hidden flat-plat replacement. From the stationary radii, solve
the marked line-circle equations with matching inversive distances
\(\cos(2\pi\delta_e)\). Their Jacobian is invertible by the same
finite-face Hessian and elementary triangle motion argument. This
gives one common nearby pattern with the original two marked lines.

For each white face let \(\mathcal R_f^\pm\) be its two
holomorphic reflection matrices, with
\(\mathcal R_f^-\mathcal R_f^+=I\). At an actual Morse slice
with regions \(F_0,\ldots,F_k\), set
\[
H_j=\mathcal R_{F_j}^+\mathcal R_{F_{j-1}}^-,\qquad
H_j\cdots H_1=\mathcal R_{F_j}^+\mathcal R_{F_0}^-.
\tag{U13}
\]
Shared wire ends have the same regions and therefore the same based
head. At cups/caps the first and last regions agree, giving the full
inverse-pair relation. The prescribed shaded collar sends both
ordered input puncture generators to their output generators, while
preserving their product \(P=BA\). The source-selected eigenvalue is
\(J=-e^{-2\pi i\delta}\), and the primitive collar ratio is
\[
R_0=E_bE_c/D,\qquad
U=-\log R_0-\epsilon\log(-J),\qquad
V=2\log(-J)=-4\pi i\delta.
\tag{U14}
\]
The matrix collar is the regular full divided difference
\[
C=I+\frac{R_0-1}{J-J^{-1}}(P-J^{-1}I).
\tag{U15}
\]
Its value at the parabolic complete point is retained, not replaced
by the scalar eigenratio one. The auxiliary meridian follows
\(C^{-1}\), and the original signed half twist is the full Hurwitz
word with \(P^{-1}-I\). The ordered contacts, not just traces,
fix these choices. The common marked-line limit supplies every zero
face case. These are the local identities in
[actual_deformed_circle_primitive_collar.md](actual_deformed_circle_primitive_collar.md).

Equations (U13)--(U15) verify all shared wires, cups/caps, drilled
threading and half-twist relations in the actual Morse van Kampen
presentation, exactly as in
[actual_complete_core_geometric_deformation.md](actual_complete_core_geometric_deformation.md), Section 2. Matching
graph cycles introduce no extra free conjugating frame because the
reflections were chosen on one global pattern. At zero this is the
complete representation of the refined link, from its own cut
certificate. Marked positive-gluing rigidity identifies the nearby
family as that same geometric germ.

For the ordinary-face stationary action
\[
A_\epsilon(\boldsymbol\delta)=
 \operatorname{crit}_{\text{finite faces}}
 \left\{\sum_e(Q_{b_e}+Q_{c_e})-
 \sum_{f\ne u,v}\log L_f+\pi i\sum_e\epsilon_e\delta_e^2\right\},
\tag{U16}
\]
the primitive identities give \(\partial_eA_\epsilon=U_e\).
The complete anchor is the actual augmented volume computed above. The same marked regulator calculation
therefore gives
\[
2\pi\operatorname{Re}A_\epsilon
=\operatorname{Vol}(\rho)
-\tfrac12\sum_e\operatorname{Im}U_e\operatorname{Re}V_e.
\tag{U17}
\]
At the first-charge critical point of the original period (S18),
\[
U_e+p_eV_e=-2\pi i.
\tag{U18}
\]
For independently sufficiently long fixed fillings this is the
primitive smooth-filling branch of the actual refined exterior.
The boundary term in (U17) cancels the original Gaussian/linear
filling terms exactly. Hence the exponential rate is the volume of
that actual filled complement. There is no comparison-diagram
substitution and no inference from a formal critical value alone.

## 11. Completing the actual filled metric


### The precise metric completion theorem used after filling

The authoritative general statement is
[general_source_regulator_hyperbolic_equality.md](general_source_regulator_hyperbolic_equality.md), Sections 1--5.
Let \(Y\) be the actual complete finite-volume augmented exterior,
with its actual primitive peripheral bases. There is one neighborhood
of its complete framed representation such that every representation
in that neighborhood with parabolic unfilled peripheral groups and
actual small logarithms satisfying
\[
U_e+p_eV_e=-2\pi i.
\tag{M3}
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
\tag{M4}
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
\tag{M5}
\]
where \(\chi_\rho\) is the real-linear extension of
\(\log|a_\lambda|\). The first map is a positive local
diffeomorphism and is exactly affine-equivariant; the second is an
equivariant positive local diffeomorphism for the entire cusp tail.
It is \(C^1\)-close to the old development on a compact collar.
Geodesic interpolation with (M4) gives a global developing local
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
large slope coefficient. This excludes a hidden winding in (M3).

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
\tag{M6}
\]
The tail contains a full punctured tube. Equation (M3) gives angular
period \(-2\pi\) and zero longitudinal period on the primitive
meridian. A complementary primitive curve has nonzero real log period,
because the log lattice has real rank two. Adding \(R=0\) therefore
gives a smooth solid torus, with exactly the original filling slope.
Its affine meridian fixes both \(q\) and infinity and has multiplier
one, so the representation also descends to the filled group.

At an unfilled cusp both multipliers are one. Formula (M5) then gives
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
peripheral traces. Consequently (M3)--(M6) identify the actual smooth
filled \(S^3\) knot complement. The regulator identity then calibrates
the source action to that metric's volume. It does not replace the
completion argument.


## 12. Exact reproduction and limits

The script [audit_actual_balanced_terminal_fans.py](../experiments/audit_actual_balanced_terminal_fans.py) reproduces the polynomial recurrence, rational balance margin, oriented stellar matching and even coset, and literal quarter-turn/stack endpoint pairings. It uses integer and rational arithmetic. It does not test or replace the analytic asymptotic, full source identity or hyperbolic metric proof.

The old and new powers are all independently sufficiently long and fixed before the level. There is no claim for the undecorated core, short core powers, a growing family, or a uniform threshold over different diagrams. No restriction to arborescent cores or prescribed minimum bridge number is used. The actual refined complement is the volume target.

The cyclic matching-source channels remain in the shared coefficient. Their bound uses the true common-radius balance, not a scalar kernel product on a graph with cycles. No moving-main profile, shifted microscopic expansion or annihilator-factor statement is supplied.
