# The marked metric limit at regular one-square corners

Private written geometry, 16 November 2026.

For the supplied positive cone sequence in the uniform-end theorem,
regular one-square corners do not destroy the marked metric limit.
The proof uses the established end models, middle bounds, volume
comparison and regular injectivity estimate. It constructs compatible
limiting hyperbolic charts and actual diffeomorphisms of compact
truncations. Bounded original dual-spine loops then identify the limit
with the original marking. The limiting maps of flattened tetrahedra
are not used as coordinate charts.

This is a subsequential limit theorem at a specified regular corner.
It does not construct a path to that corner, give a positive ideal
retriangulation, or estimate the original quantum coefficient.

## 1. Hypotheses and the marked conclusion

Retain the supplied sequence of original positive circle-tree metrics
from the pinned end and compact-middle theorems. The exterior, its
finite ideal tetrahedral gluing, original face words, disk-page orders,
carriers and primitive peripheral curves are fixed. In regular original
face coordinates the parameters converge. Every limiting edge is
positive or has one finite regular square corner with the other square
interior. No ideal vertex pair or face triple collides, and no original
face-map denominator vanishes.
In particular the original exterior is connected and has at least
one edge, as in those input theorems.

At each selected end the actual periods are

\[
 U_{v,j}+p_vV_{v,j}=-2\pi i\chi_{v,j},\qquad
 V_{v,j}=2H_{v,j}+2is_{v,j},\qquad
 0<\chi_{v,j}\le1,
 \tag{1}
\]
\[
 \chi_{v,j}\longrightarrow\chi_{v,*}>0,
 \qquad 0<H_0\le H_{v,j}\le H_1,
 \qquad (H_{v,j},s_{v,j})\longrightarrow(H_{v,*},s_{v,*}).
 \tag{2}
\]

The slopes and carriers are fixed. Unselected auxiliary angles are
zero; main cusps remain complete. Let \(M_j\) be the original metric
with its selected cone axes added. The previous results supply:

- disjoint embedded selected tubes of one fixed radius, with metric
  \(dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2\) and the exact
  periods (1), and convergent nondegenerate complete cusp lattices;
- compact filled cores \(C_j\), uniform completed-metric diameter,
  and a uniform embedded positive-volume hyperbolic ball;
- volume comparison at every center and uniform lower bounds for
  small balls a bounded distance from \(C_j\);
- uniform ambient-distance-preserving hyperbolic balls on every
  bounded buffer around \(C_j\) that stays a fixed positive distance
  from the genuine axes.

These are inputs proved in the pinned sources, not conclusions inferred
merely from bounded shape parameters.

**Theorem 1.** After passing to a subsequence, there is a complete
hyperbolic cone metric \(M_*\) on the original marked filled topology.
Its selected cone angles and core periods are the limits in (1)--(2),
and its remaining ends are the original labeled complete cusps.
On suitable compact regular truncations \(K_j\subset M_j\) and
\(K_*\subset M_*\), there are diffeomorphisms

\[
                         f_j:K_*\longrightarrow K_j
 \tag{3}
\]

whose pulled-back metrics converge smoothly to the metric of \(K_*\).
On boundary collars these maps are the explicit maps using the same
marked tube or cusp coordinates and the converging periods.
After one further subsequence their induced original marking is
constant. In a continuously normalized original base frame, the
holonomy of this marked limit is the literal limit of the original
face-word holonomies.
The pulled-back developing maps, with this normalization and the
stabilized marking, converge smoothly on each compact subset of
the universal cover of the original exterior with the selected
axes omitted. The end identifications are the
canonical marked models just specified.

If all \(\chi_{v,*}=1\), \(M_*\) is the smooth complete finite-volume
hyperbolic metric on that original marked filling. For other charges,
the conclusion is a cone metric; discreteness of its holonomy is not
asserted.

## 2. Buffered truncations and finite metric nets

Choose \(r_0>0\) much smaller than the uniform selected tube radius.
Choose the complete cusp cutoffs sufficiently deep that their original
end models extend at least two units of depth to either side of the
chosen depth-zero torus. All choices are fixed for the sequence.
Let \(K_j\) remove the selected open tubes \(R<r_0\) and the
complete cusp regions of depth \(\sigma>0\). Let \(K_j^+\) instead
remove \(R<r_0/2\) and \(\sigma>1\). Both are compact connected
regular manifolds with the original labeled torus boundaries.
They are regarded as metric subsets of \(M_j\) with its ambient
distance, not with their intrinsic path distances.
Connectedness is topological: deleting these standard smaller end
neighborhoods leaves a truncation of the same connected original
exterior, also when a selected axis happens to be smooth.

The inner set lies a uniform positive distance from the outer
boundary. To see this for a selected tube, a path to its axis from
inside the uniform tube has radial length at least \(R\). A path
leaving that larger tube first has still greater length when
\(R\) is small. Thus the model radial coordinate is the actual
distance to that axis on the smaller tubes. In particular a path
from \(R\ge r_0\) to \(R=r_0/2\) costs at least \(r_0/2\).
For a cusp, depth extended by zero outside the cusp is one-Lipschitz,
so the analogous cost is one. The disjoint larger end neighborhoods
give the same separation between different inner end collars.

The sets \(K_j^+\) lie in a fixed bounded buffer of \(C_j\).
They stay at least a fixed positive distance from every genuine
axis and have uniformly bounded diameter. The injectivity theorem
therefore supplies one radius \(a>0\) for actual isometric
hyperbolic balls on a neighborhood of the inner sets. Decrease
\(a\) so that these balls, with several larger concentric buffers,
remain within \(K_j^+\).

Here is the metric compactness argument needed below. For every
\(\varepsilon>0\), a maximal \(\varepsilon\)-separated set in
\(K_j^+\) has uniformly bounded size. The ambient balls of radius
\(\varepsilon/2\) about its points are disjoint. Their volumes
have a common positive lower bound by the adopted comparison and
surviving-ball estimate, because the centers are a bounded distance
from \(C_j\). All these balls lie in one ambient ball of uniformly
bounded radius about the original surviving-ball center. Its volume
is at most the corresponding hyperbolic ball volume. Dividing these
upper and lower bounds proves the assertion. Large values of
\(\varepsilon\) may be replaced by a fixed smaller one.

We recall explicitly the finite-net compactness consequence. Choose
successively finer finite nets with meshes tending to zero, retaining
previous net points, and use their uniform cardinality bounds. After
padding labels if necessary, pass to a subsequence on which every
distance between every pair of labeled net points converges. The
diagonal choice is possible because the diameters are bounded and
there are only countably many such distances. Quotient zero-distance
labels and complete the resulting metric set. The finite-net bounds
make this completion a compact metric space \(X^+\).

Sending a point to a nearby net point at a sufficiently fine mesh
gives correspondences between \(K_j^+\) and \(X^+\) whose distance
distortions and density errors tend to zero. This is the only meaning
of metric convergence used here. It follows directly by first fixing
a net mesh, taking the limit of its finite distance table, and then
letting the mesh tend to zero. By the same construction for subsets,
pass to a further subsequence on which the inner compact sets have
a compact limit \(X\subset X^+\). One may include finitely many
specified points and end-model maps in these subsequences. A compact
metric limit of connected compact sets is connected: a separation
of its two nonempty compact pieces has positive distance and would
separate every sufficiently close approximating set. Thus \(X\)
is connected.

## 3. Full regular balls and the explicit collar limits

We first identify neighborhoods, rather than merely tangent metrics.
If \(p_j\in K_j\) tends to \(p\in X\), choose oriented frames and
isometric charts

\[
                 F_{j,p}:B_{\mathbb H^3}(4a)\longrightarrow K_j^+,
                       \qquad F_{j,p}(o)=p_j,
 \tag{4}
\]

with ambient distance preserved. Such charts follow from the
injectivity theorem after reducing \(a\) by one fixed factor.
It suffices to select centers from one finite \(a/4\)-net of
\(X\), with corresponding \(p_j\); all extractions below are
joint for these finitely many charts. No simultaneous extraction
over an uncountable family of centers is required.
On a countable dense subset of \(\overline B_{\mathbb H^3}(3a)\), compactness
and a diagonal extraction give limiting image points in \(X^+\).
Their exact distances are the model distances, so this map extends
to an isometric embedding \(F_{*,p}\).

It contains the entire \(X^+\)-ball of radius \(2a\) about \(p\).
Indeed approximate a point of that ball by \(q_j\in K_j^+\).
Its distance from \(p_j\) is eventually less than \(3a\), so it
lies in the actual ball (4). Its model preimages have a convergent
subsequence in the closed model ball of radius \(3a\). The limiting
preimage maps to the given point. Conversely model distances from
the center are exact. Thus the smaller model balls are full metric
neighborhoods in \(X^+\), not incomplete chart images.

There is also explicit convergence on each original end collar.
Use the fixed marked coordinates on its compact parameter domain.
For a tube these are \((R,x,y)\), where

\[
 X=2H_{v,j}y,\qquad
 \theta=-2\pi\chi_{v,j}x+2s_{v,j}y,
                    \qquad (x,y)\pmod{\mathbb Z^2}.
 \tag{5}
\]

Use, for example, \(3r_0/4\le R\le5r_0/4\).
For a cusp use its fixed marked translation coordinates and
\(-1/2\le\sigma\le1/2\). Their coefficient metrics converge
smoothly, since the two period vectors converge to an independent
pair. In particular the maps from these fixed compact parameter
domains to \(K_j^+\) are uniformly Lipschitz. Finite nets followed
by continuity give limiting maps into \(X^+\).

These limiting collar maps are embeddings. Inside a larger original
end neighborhood, the intrinsic model distance between two distinct
fixed collar points has a positive limit. A competing ambient path
which leaves that larger neighborhood has length bounded below by
twice the fixed buffer from the smaller collar to its boundary.
Therefore no two distinct collar points can acquire zero limiting
distance. The same buffer argument separates different labeled
collars. Small balls centered in each collar stay within the larger
end model. The full-ball argument used for (4) shows that the
limiting collar has the same local hyperbolic metric and contains
an open neighborhood of its middle torus in \(X^+\).

All transitions between the full hyperbolic balls are hyperbolic
isometries. For precision choose balls much smaller than (4).
Two intersecting small balls and their overlap lie in one of the
larger charts. The change of coordinates preserves distance on
an open set, hence is the restriction of a hyperbolic isometry:
four points in general position determine its Lorentz extension,
and their distances determine all further points. Their orientations
are the limits of the original oriented charts. These transitions
therefore define a smooth hyperbolic atlas near \(X\).
The explicit collar maps are smooth in this atlas, since they are
local hyperbolic isometries from their limiting metrics.

The limit of the inner cores is exactly the region on the inner
side of their middle tori. In a tube collar its condition is
\(R\ge r_0\), and in a cusp collar it is \(\sigma\le0\).
This follows from the explicit collar convergence and can also
be expressed using their convergent signed defining functions.
Away from these collars, an inner-limit point has a neighborhood
whose preimages are entirely inside \(K_j\); otherwise a nearby
boundary point would limit to one of the listed tori. Such points
are interior. Consequently \(X\), with this atlas, is a compact
connected smooth hyperbolic manifold with boundary, which we now
denote by \(K_*\). Its boundaries have exactly the original end
labels. There is no assertion that the ambient distance on a
truncation is its intrinsic path metric.

## 4. Actual diffeomorphisms of the compact cores

Choose finitely many small chart balls covering \(K_*\), together
with larger concentric balls as in (4). Extract the charts jointly
so that their finite collection of transitions converges. This
convergence is smooth: in a common larger chart every transition
is a hyperbolic isometry, its center displacement is bounded, and
its rotational part belongs to a compact orthogonal group. Its
limit is the transition already identified in Section 3. Isometries
converging in these finite parameters converge with every derivative
on compact chart subsets.

For one small limiting chart, define its local candidate map by

\[
                    f_{j,a}=F_{j,a}\circ F_{*,a}^{-1}.
 \tag{6}
\]

On overlaps these candidates differ by a quantity tending to zero
with every derivative in the common larger target chart. They also
send each point to a point corresponding to it in the metric
convergence. Include as further candidates the explicit maps of
the end collars using the same \((R,x,y)\) or cusp coordinates
with the periods at level \(j\). Their local coordinate maps also
converge smoothly to the identity. To verify this last assertion
without deducing derivatives from metric convergence alone, unwrap
a small part of a tube collar. With \(w=X+i\theta\), its explicit
developing map into upper half-space is
\[
             (R,w)\longmapsto
                 (e^w\tanh R,\ e^{\Re w}\operatorname{sech}R).
\]
In a cusp collar the corresponding map is
\((x,y,\sigma)\mapsto(\lambda_{1,j}x+\lambda_{2,j}y,
y_{0,j}e^\sigma)\), in its normalized translation frame.
On the compact local coordinate sets these maps converge with
every derivative. Their change to an overlapping chart in (4)
is a hyperbolic isometry. Its finite parameters converge by the
same distance-and-frame argument used for the chart transitions.
Thus the asserted smooth compatibility follows from the explicit
models as well as the metric limit. Choose a smooth partition of
unity on a neighborhood of \(K_*\), subordinate to these domains,
whose end-collar weight is one near each boundary torus. The end
collars are disjoint. The partition can also have weight one for
a specified base chart on a smaller interior ball.

Here is an intrinsic way to glue the candidates. At a point where
several weights are nonzero, all candidate images lie in one common
larger target chart and are mutually arbitrarily close. Identify
that chart with an open subset of the hyperboloid, and write its
candidate vectors as \(y_{j,a}\). With the partition weights
\(\psi_a\), put

\[
 S_j=\sum_a\psi_a y_{j,a},\qquad
                 f_j=\frac{S_j}{\sqrt{-\langle S_j,S_j\rangle}}.
 \tag{7}
\]

A positive weighted sum of future timelike vectors is future
timelike. The normalized sum lies in their geodesic convex hull,
so it remains in the larger chart. Every change to another common
chart is a Lorentz isometry; it commutes with (7). Thus (7) is
well-defined independently of that choice. It is smooth, and in
the local identifications its derivatives converge to those of the
identity. In particular it is a local diffeomorphism for large \(j\).
The construction is on an open neighborhood of the compact core,
including both sides of its boundary collars.

Near each boundary, (7) is exactly the prescribed end-coordinate
map because its weight is one. It preserves the level defining
the boundary and its inner side. On the remaining compact subset,
the distance from the boundary is positive and metric closeness
puts the image on the correct side for large \(j\). Hence
\(f_j(K_*)\subset K_j\), with every labeled boundary torus
mapped onto its original counterpart.

The maps are globally injective. If injectivity failed for a
subsequence, take \(x_j\ne y_j\) with equal images. Metric
closeness implies \(d_{K_*}^{\rm ambient}(x_j,y_j)\to0\).
After extraction they converge to the same point. They therefore
lie in a common small coordinate neighborhood on which the maps
extend across any boundary and are uniformly \(C^1\)-close to
the identity on a larger convex coordinate ball. On such a ball,
integrating the derivative along a straight segment proves
injectivity once its difference from the identity has norm less
than one. This is a contradiction.

Finally the image of \(K_*\) is compact and hence closed in
\(K_j\). It is open relative to \(K_j\): in the interior this
is the local inverse-function theorem, and at the boundary it is
the exact collar map. Since \(K_j\) is connected, the nonempty
image is all of \(K_j\). Thus (7) gives the diffeomorphisms (3).
The same chart computation proves smooth convergence of their
pulled-back hyperbolic metrics. This proves the topology statement;
it is stronger than merely obtaining local metric balls in a
limit space.

## 5. Bounded original paths fix the marking

We justify that the marking does not drift through these
diffeomorphisms. Choose a basepoint and oriented frame in one
tetrahedron whose limit stays positive. Such a tetrahedron exists
at every allowed edge. The point and frame can be chosen
continuously in its original normalized face chart.

The original ideal triangulation has a finite dual spine carrying
the fundamental group of the exterior. Choose a finite generating
family in its dual one-skeleton, including specified words for all
peripheral curves and base paths when needed. Realize it in each
positive metric as follows. In every face use its intrinsic ideal
triangle incenter. In each tetrahedron choose a continuously
varying interior point, for example the hyperboloid-normalized
positive average of its four face incenters. Join it to these
incenters by the hyperbolic segments in that convex tetrahedron.
The actual face maps identify the shared incenters. These are
the original dual-spine paths and represent the original words.
The required generation can also be seen directly: perturb a loop
away from the codimension-two skeleton, record its finitely many
face crossings, and homotope each piece inside its topological
tetrahedron to the chosen anchor-and-face path. Thus a finite
generating family in the finite dual graph suffices; no metric
limit of that spine is being asserted to be embedded.

All these paths have uniformly bounded length and stay in one
buffered regular truncation. In a normalized tetrahedral frame
their endpoints stay in compact hyperbolic regions, since the face
triples remain distinct. Their geodesic convex hulls are uniformly
compact as well. In every selected vertex frame the projection
of each segment lies in its link triangle. The uniform-end theorem
gives \(|z-q_j|\ge m>0\) there; compactness gives \(y\le Y\).
Therefore

\[
            R=\operatorname{arsinh}(|z-q_j|/y)
                                  \ge\operatorname{arsinh}(m/Y)>0.
 \tag{8}
\]

Complete cusp depths on these finite paths are bounded for the
same reason. Shrink the fixed selected tubes and deepen the cusp
cutoffs once, if necessary, so the paths lie in the interiors of
the chosen \(K_j\). All previous arguments apply with these
new fixed cutoffs. A short connection to the chosen basepoint
inside its positive tetrahedron has the same properties.

In Section 4 choose weight one for the original base chart near
this point. Then \(f_j\) sends the fixed limiting basepoint and
frame to the chosen original basepoint and frame. Pull the original
generating paths back by \(f_j^{-1}\). Their lengths in \(K_*\)
are uniformly bounded, because the pulled-back metrics converge
smoothly. After a subsequence their based homotopy classes are
constant. Here is a direct finiteness justification: in a fixed
compact smooth core with boundary, choose a finite sufficiently
fine net and contractible coordinate neighborhoods, using half-ball
coordinates near the boundary. Partition a loop of bounded length
into a bounded number of short pieces. Replace its vertices by
nearby net points and its pieces by fixed short connecting paths.
Each replacement is a homotopy in one of these neighborhoods.
There are only finitely many resulting finite words in this finite
net graph. Thus only finitely many based classes occur. Equivalently
one may extract uniformly convergent constant-speed loops and use
the same neighborhoods to stabilize their homotopies.

There are finitely many generators, so one subsequence stabilizes
them all. At every level the transported marking is an isomorphism
from the original exterior group to \(\pi_1(K_*)\). Agreement
on a generating set makes this a single fixed isomorphism for all
late levels. Its peripheral words and conjugating base paths are
the retained original ones. The boundary maps in (3) use the exact
marked end coordinates, so the meridian, longitude and primitive
filling slope have not acquired new integral basis changes.

For completeness this is a marking by an actual homeomorphism,
not just an abstract group identification. Choose one sufficiently
late level. Its original cell construction identifies \(K_j\)
with the original topological truncation. Compose that identification
with the diffeomorphism \(f_j^{-1}\). The stabilized group marking
is exactly the one induced by this homeomorphism, including its
boundary curves.

In the fixed base frame, the rational original face matrices
converge because all their denominators remain regular. Thus their
products for every original generator converge to the literal
limiting face-word matrix. On the other hand, smooth convergence
of the pulled-back hyperbolic charts makes their transition products
along each fixed limiting generator converge to its metric holonomy.
The stabilized marking identifies these two products. Therefore
the holonomy of \(K_*\) is the original algebraic limit with its
actual primitive lifts supplied by the end collars.

This gives convergence of developments in one marked atlas,
not only convergence of the holonomy matrices. Normalize the
developing maps at the chosen basepoint and frame and lift \(f_j\)
using the stabilized marking. Continue each local chart along
a fixed chain from the base chart. Every transition in that
chain converges smoothly, so its developed chart does also.
A compact subset of the exterior universal cover is covered by
finitely many such continued charts; their overlaps agree
because they are the actual developments. This proves smooth
convergence on that compact subset. On fixed collars the same
assertion follows from the explicit models in Sections 3--4.
The exterior here omits every selected axis, including any axis
which is smooth at a limiting unit charge. No identification of
regular loci with changing sets of included axes is used.

## 6. Attach the original limiting ends

Attach to each boundary of \(K_*\) the full limiting explicit end
model. Its collar agrees with the metric already constructed there.
For a selected end use (5) with the limiting parameters and add the
axis; its meridian is the original \(\mu_v+p_v\lambda_v\),
with angular period \(-2\pi\chi_{v,*}\), and its complementary
longitude has real period \(2H_{v,*}>0\). For a complete cusp use
its limiting independent translation lattice. The labels and
boundary bases are exactly those fixed in Sections 3 and 5.

The resulting metric is complete: its middle is compact, its cone
axes have been added in their explicit local models, and each
remaining cusp has infinite depth in a complete cusp metric.
Its volume is finite. The compact middle has finite smooth volume;
the finite cone tubes have positive finite lattice periods; and
each complete cusp has exponentially decreasing cross-sectional
area. The marking homeomorphism extends over these ends with the
same peripheral coordinates. This proves Theorem 1.

At limiting unit charges the tube models are smooth. The complete
constant-curvature metric is therefore the hyperbolic metric on the
original smooth filling, by the same complete-development argument
as in the pinned completion proof. At other charges it remains the
specified cone metric. No claim about a positive triangulation of
the limiting middle is needed for either conclusion.

The theorem establishes a marked limit and regular end completion.
A deformation of its marked holonomy to nearby structures is a
separate local construction. Neither such a deformation nor the
limit theorem supplies a nonzero coefficient in the finite quantum
source or a comparison with its other contour pieces.

## Direct sources and readback

- [Uniform original ends](research_regular_corner_uniform_end_tubes.md),
  full original cone/cusp models, second-point separation and marking:
  `904cc289bb829e4a737064e412fc18adb5e95818cc6590219643a7e373460e81`.
- [Compact middle](research_regular_corner_compact_middle_bounds.md),
  actual compact truncations, diameter, surviving ball and finite-cell
  bounds: `d899199d51f0999b912baa128c9ea1c33d3193a22e87ecbde46f67da08638494`.
- [Uniform ball volumes](research_regular_corner_uniform_ball_volumes.md),
  ambient volume comparison, properness and buffered lower bounds:
  `756dac12a3e335b74fddd87f804bb05b44ad3fd40640f3e32e596b98aed78d90`.
- [Regular injectivity](research_regular_corner_injectivity_away_axes.md),
  ambient-isometric balls on the buffered regular region:
  `545b8b063c24968142645e963697b2d81f16a5c9fd17ab93e42ec340124e85e5`.
- [Pointwise marked completion](research_positive_point_marked_completion.md),
  original finite gluing, regular face words, original topological
  marking and the complete-development conclusion:
  `28de22f081e24629ea6d26ad05213301a9bcf5d17d3ae7d00cc9c675a8218887`.

Only written mathematics and source-text/hash inspection are used.
No mathematical program, numerical computation, test or compilation
is used. Frozen source notes and public documents are unchanged.
The author reread the entire final proof. All five full direct
source reads were retained or renewed in this proof sequence,
their used implications were reread, and their pinned hashes
were checked. Independent full peer and root review remain
required before adoption.
