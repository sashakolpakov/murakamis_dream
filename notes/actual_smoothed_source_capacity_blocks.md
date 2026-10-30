# Smoothed source capacity, simple blocks and their actual polyhedra

30 October 2026. Independently reviewed and frozen. This concerns the L_1 opposite smoothing,
not deletion of the old white edge xy or an asserted three-manifold JSJ
decomposition. The new source is assumed connected and its two original
marked white vertices u,v are distinct and still joined by their actual
marked MAIN edge. The source white cellulation is a spherical triangular
cellulation, allowing repeated incidences, loops and parallel edges.

## 1. Remove the attainment hypothesis by finite convex duality

Use the [already normalized local entropy](actual_matching_smoothing_angle_capacity.md)

  V(theta)=2 sum_j[Lambda(theta_j/2)+Lambda((pi-theta_j)/2)],
  2pi F(l)=max_(theta>=0,sum theta=pi)(theta.log l+V(theta)).

Marked corners are fixed to zero. Let Theta be the product of the
remaining compact row simplexes (possibly empty), A its finite-face
incidence, and d_f=2pi for each finite face. Define

  H(d)=max{sum_t V(theta_t):theta in Theta,A theta=d},

with H=-infinity when infeasible. Then the literal log-radius capacity
is EXACTLY H(d)/(2pi), even if its positive-radius infimum is not
attained. There is no additive constant.

Proof. H is concave and upper semicontinuous on its compact domain,
by compactness and concavity of V. Weak duality is the local displayed
identity. Conversely separate (d,H(d)+epsilon) strictly from the closed
hypograph of H. The coefficient of the vertical coordinate is positive:
it is nonnegative since the hypograph extends downward; if it were zero,
strict separation would contradict d belonging to the projection.
Normalize that coefficient to one. The resulting finite affine
majorant gives logarithmic radii with capacity at most
(H(d)+epsilon)/(2pi). Let epsilon decrease. If d is outside the
projection, separation in the finite face coordinates and scaling that
separator make the log-radius infimum -infinity instead.

## 2. A loop is infeasible; a two-edge cycle splits exactly

For a triangular disk with a simple m-edge boundary and v interior
vertices, Euler and 3t=2e_internal+m give t=2v+m-2. This uses incidences
with multiplicity and remains true for a one-edge loop or a two-edge
parallel cycle, whose boundary has respectively one or two vertices.

Because u,v are joined by an actual embedded edge, any simple separating
loop or two-edge cycle has a side with NO marked vertex in its interior.
An edge joining strictly opposite sides would cross the cycle. Marked
vertices on the boundary cause no problem.

For a one-edge loop choose that side. It has 2v-1 triangles, with total
available angle (2v-1)pi. Its v interior vertices alone demand 2v pi.
Thus the angle polytope is empty and the capacity is -infinity. This
statement is only about this source capacity; a source vanishing theorem
would additionally retain the finite label/forced-factor support.

For a two-edge cycle with distinct boundary vertices a,b, the chosen
side has 2v triangles. Its interior demands exhaust their entire angle
2v pi. Consequently every a- and b-corner on that side has angle zero.
Identify its two boundary edges to obtain a triangular sphere D_in,
marked at a,b. Identify the same two edges on the other side to obtain
D_out with the original marked pair u,v. The original feasible angle
polytope is EXACTLY the Cartesian product of the two resulting angle
polytopes. The boundary contributions of D_in are zero, so the full
demands on D_out are unchanged, including when a or b was originally
marked. Conversely any pair of such assignments glues to a feasible
original assignment. Entropy is a sum over the unchanged triangles.
Therefore

  Phi(D)=Phi(D_in;a,b)+Phi(D_out;u,v).

The identity includes nonattainment and infeasibility by section1.
The new marks a,b are adjacent along the glued boundary edge, so the
argument iterates. It does not reset an actual quantum mark or assert
factorization of the finite source: it is an exact statement about
the already normalized classical source capacity.

## 3. Terminal blocks and finite positive multipliers

Repeatedly split parallel-edge two-cycles. Each split has a positive
number of triangles on both sides, so the process terminates. If a loop
occurs its block is infeasible. Otherwise the terminal blocks have
simple underlying graphs. A three-vertex sphere consists of two copies
of the same triangle. With its adjacent marked pair a,b the remaining
vertex c receives angle pi in each triangle. Its entropy is zero and

  2F(0,0,l_c)-log l_c=0.

Every other terminal block is a genuine simple triangulated sphere
with at least four vertices. Its graph is 3-connected: deleting one or
two vertices preserves connectivity by rerouting through their cyclic
links (equivalently use the elementary triangulated-sphere argument in
the frozen transverse-rank theorem).

Such a block has a strictly feasible relative angle assignment. Here is
a finite Hall proof rather than a circle-packing existence assumption.
Let there be R finite vertices and 2R triangles. Every triangle has at
least one finite vertex. For a nonempty proper subset S of finite
vertices, put T=finite\S. In the sphere punctured at any vertex of S,
the original triangles supported on T union{u,v} are bounded faces of
a simple planar graph on |T|+2 vertices. There are at most 2|T|-1 such
faces. Hence at least 2|S|+1 original triangles touch S. The required
angle of S is only 2|S|pi. The full finite set gives equality of total
supply and demand. These strict finite Hall inequalities allow a common
small lower bound epsilon>0 on every allowed corner. Singleton rows
(the two uv triangles) are fixed at pi and are understood relatively.

Maximize total V on this compact feasible polytope. An allowed zero
angle cannot occur at a maximizer: moving toward the strictly feasible
assignment gives a positive epsilon log(1/epsilon) contribution at every
new zero corner, also nonnegative at an old pi corner, while all other
contributions have finite first derivative. Thus all nonfixed allowed
angles lie strictly between zero and pi. Finite-dimensional Lagrange
multipliers now give

  tan(theta_tf/2)=k_t l_f, l_f>0.

The row sum pi forces k_t=(sum_(f<g in t)l_f l_g)^(-1/2), including
the two-positive-face rows. These are exactly the local source angles.
They attain the radius capacity. Strict concavity makes the angle
maximizer unique; connectedness of the finite-face adjacency graph
makes its multipliers unique up to common scale. Thus no global
attainment hypothesis is needed for these simple terminal blocks.

## 4. Constructing the simple block's actual circle packing

Here is an elementary construction, including the development step.
It supplies the simple block with its labeled convex polyhedron rather
than inferring geometry from the existence of radius multipliers alone.

Remove one triangular face abc of the simple sphere. Fix three positive
boundary radii r_a,r_b,r_c, hence three mutually externally tangent
boundary disks. The remaining triangulated disk has v interior vertices
and 2v+1 triangles. Give each interior vertex demand2pi and leave the
three boundary demands free, with total pi. Maximize

  sum_t V(theta_t)+sum_(boundary corners tf)theta_tf log(1/r_f).

A strictly positive angle assignment exists by the same finite Hall
argument. Treat the three boundary vertices as one supply destination
of demand pi, retaining their separate corners. An interior subset S
touches at least2|S|+1 disk triangles. Indeed puncture the sphere at a
vertex of S and put T=interior\S. The complementary simple planar
graph has |T|+3 vertices and at most2|T|+1 bounded triangular faces.
The removed boundary face abc is one of them, so at most2|T| are
disk triangles; subtracting from2v+1 gives the asserted strict bound.
A proper subset consisting of the
boundary destination and some interior vertices also has strict Hall
slack: its complement T contains only interior vertices, and triangles
wholly supported on T are bounded faces of a simple planar graph,
at most2|T|-5 when |T|>=3 and none when |T|<=2. The full set has
equal total supply and demand. Thus a common positive lower bound on
all corners is feasible. The entropy boundary derivative argument of
section3 places the maximizer in the open angle simplexes. The fixed
boundary log terms have bounded derivatives and do not alter that
argument. In particular each boundary angle sum is positive; their
sum is pi, so each is strictly less than pi.

Lagrange multipliers now give the same tangent-circle angle formula
with the prescribed boundary radii and positive finite interior radii.
Glue Euclidean triangles with side lengths r_f+r_g. Their angles are
exactly those just obtained. Every interior vertex has total angle2pi.
The disk therefore has a global orientation-preserving Euclidean
development: continuation around each interior vertex has rotation
2pi and zero translation, and such loops generate the punctured disk's
holonomy. Its boundary consists of three straight sides, with positive
angle sums less than pi and the prescribed strict triangle lengths.
It maps once around a convex triangle.

This development is an embedding. Indeed it is locally an
orientation-preserving isometry at every interior point, including
interior vertices. For a point off the developed finite edges, the
number of its preimages is its boundary winding number. That number
is1 inside the boundary triangle and0 outside. Continuity and local
injectivity extend the conclusion across the finite edges and vertices.

Place a disk of radius r_f at every developed vertex. The three disks
in each triangle are mutually externally tangent. The sector of a
vertex disk between that triangle's two incident edges lies inside
the triangle: its opposite center segment is covered by the other
two tangent disks, which are disjoint from the vertex disk. The
separation from that segment is strict: its two pieces lie in the
other disks, their unique mutual contact is strictly outside the
third positive disk, and the third disk's contacts with those disks
lie on the two different incident center edges. Thus it cannot
meet a nonincident triangle or acquire an accidental nonedge contact.
These
sectors assemble to the full disk at an interior vertex because its
angle sum is2pi. At a boundary vertex they assemble to the part of
the fixed boundary disk inside the carrier triangle. Thus different
disks have disjoint interiors, and the only contacts are the actual
triangulation edges. Restoring the omitted outer face gives the exact
labeled sphere packing. Arbitrary separating triangles cause no
problem: the development uses every triangle, not an assumed
three-connected drawing of only part of the graph.

For completeness, its right-angled polyhedron has a direct support
certificate. For each bounded triangle the circle through its three
contact points is its Euclidean incircle: on a center edge fg the
incircle contact is at distance r_f from f. It is orthogonal to the
three vertex disks. Its disk lies in that center triangle and contains
no other packing contact. For the omitted outer triangle take the
opposite side of its contact circle; all interior disks and contacts
lie in its bounded curvilinear gap and hence inside that circle.
Consequently every packing contact lies in all the prescribed inward
white and shaded halfspaces, strictly unless incident to that face.
The convex hull of the contacts has precisely the white cyclic facets
and these shaded triangles: they form the closed labeled sphere of
supporting faces, with no missing face or extra ideal vertex. At each
contact, its two white and two shaded planes have the prescribed
cyclic order and successive right angles. This is the actual convex
ideal right-angled polyhedron Q_block of this labeled block.

## 5. Absolute capacity and independence of the adjacent marked pair

Choose ANY adjacent pair of white vertices in this simple block, and
send their contact to infinity by one orientation-preserving Mobius
map. The two corresponding disks become the opposite marked halfplanes;
all other disks stay bounded and disjoint in their common strip.
Their positive curvatures satisfy the source angle equations, and
therefore attain the capacity with that marked pair. The already
proved actual facet-coning normalization gives

  Phi(block;any adjacent marked pair)=Vol(Q_block)/pi.

It is independent of that pair. There is no source scalar or additive
volume constant: the local normalization V(pi,0,0)=0 and section1's
exact duality fix it. The double-triangle block has capacity0 instead
and is not declared a nondegenerate ideal polyhedron.

Combining this construction with section2 expresses every finite
smoothed capacity in the stated class as a sum of these actual block
polyhedron volumes divided by pi, with zero from double-triangle
blocks. The new pair on a cut block is a geometric/capacity choice;
no original quantum mark has been moved.

## 6. The remaining topology and strict-comparison questions

This does not by itself identify the blocks as the hyperbolic JSJ
pieces of the smoothed marked exterior. That assertion requires the
actual cut gluing, peripheral maps and possible Seifert pieces. Nor
does the decomposition compare their summed capacity strictly with
the original unsmoothed capacity: the L_1 operation merges the opposite
b,c faces, and is not the old white-edge xy contraction. These two
remaining questions are not consequences of circle-packing existence.

Finite-N care: a two-cycle can cut two MAIN edges or two MATCHING edges.
In the latter case retained forced polynomials couple the two sides
away from the odd maximal fold. Thus this capacity product is not a
claimed all-level source product. Degree-two blocks can have zero
capacity while still enforcing exact even-level zeros, as the parallel
Belt examples already demonstrate.

## 7. Focused verification

[The focused audit](../experiments/audit_actual_smoothed_source_capacity_blocks.py) and its
saved results check eight digon LP systems and their separate factors,
five genuine loop cellulations with infeasible demands,474 exact
marked planar Hall cuts with21 independent positive LP assignments,
and158 fixed-boundary Hall cuts with seven positive disk assignments.

Fourteen actual disk developments include tetrahedral, bipyramidal
and separating-triangle stacked spheres, with equal and unequal
boundary radii. The audit checks232 disk pairs,1572 shaded supporting
inequalities,348 white/shaded right angles and42 independent adjacent
mark capacity evaluations. The geometric solve uses floating-point
arithmetic, with maximum residual below3.2e-13; the subsequent entropy
evaluation uses40 digits. Its marked-capacity spread is below2.6e-26.
These are independent numerical diagnostics of the finite construction,
not a numerical substitute for the all-block proof.

A glued two-block example also checks the genuinely nonattained
primal capacity against its exact dual block sum at four diverging
radius scales. The positive primal excess decreases toward zero;
the double-triangle capacity is checked separately. No finite quantum
factorization or strict smoothing loss is tested or inferred.

Independent review: the cluster source reviewer checked the full
convex-duality, loop/digon, strict Hall, developed-disk and supporting
halfspace proofs, and freshly reproduced every audit count and residual.
Root independently checked the entire proof and audit code, including
the fixed-boundary Hall subtraction, strict exclusion of nonedge disk
contacts, actual polyhedron construction and adjacent-mark independence.
Both reviews preserve the distinction between capacity decomposition,
finite quantum factorization, actual JSJ identification and the still
unproved universal strict smoothing comparison.
