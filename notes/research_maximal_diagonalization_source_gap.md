# A maximal diagonalization has a strict full-source entropy gap

31 October 2026. **analytical research theorem.**
Unpublished. This is an exact local and
global entropy transport on the original face targets. Sections 4--5
prove a structural selection theorem: every finite connected SIMPLE
spherical quadrangulation with four distinct vertices on each of its
R>=2 faces has a simple complete-capacity-maximizing diagonalization,
and every maximizing diagonalization has a uniform sharp non-CROSS gap.
No claim is made that an arbitrarily prescribed diagonalization is
maximizing. Different choices need not give the same original link.

## 1. Literal local transport

Use the original four cyclic faces (x,b,y,c) and its matching diagonal
xy. A LEFT degree row is

    q=(q_x,q_b,q_c,q_y)=(a,b,c,d),
    nu=a+b+d=1-c<=1/2.

Here a,b,c,d denote normalized degrees only. The original sharp
spectral maximum is

    G(q)=f(a)+f(b)+f(d)-f(nu),

where f(0)=f(1/2)=0, f'(t)=log cot(pi t), and
f(1/2-t)=f(t). In particular f>=0 on [0,1/2].

Replace only the matching diagonal xy by bc, keeping the quadrilateral
boundary and its ordered face labels. Its two new triangles are
(b,x,c),(b,y,c); the new port has outer faces b,c and middle faces x,y.
The SAME degrees lie in its closed CROSS domain because a,d<=1/2.
The following explicit CROSS triangle rows preserve every face degree:

    alpha_(b,x,c)=(0,a,1/2-a),
    beta_(b,y,c)=(b,d,1/2-b-d).                         (1)

All entries are nonnegative because nu<=1/2. Their sums are each 1/2,
and their combined b,x,c,y loads are exactly b,a,c,d. No face degree
is moved to another label. Their entropy is

    C(alpha)+C(beta)
      =2f(a)+f(b)+f(d)+f(b+d)
      =G(q)+f(a)+f(b+d)+f(nu).                        (2)

Thus the genuine complete/CROSS entropy h_flip of the flipped port
satisfies

    h_flip(q)>=G(q)+f(nu).                           (3)

For 0<nu<1/2 the displayed gain is strictly positive. The alternative
allocation assigning all original b-load to the first triangle gives
the further valid gain f(d)+f(a+b)+f(nu). At nu=0 and nu=1/2, use the
closed formulas directly; no strictness is asserted merely from (3).
RIGHT is identical after exchanging its overloaded middle and the
other middle. Protected zeros are retained in (1), not approximated.

## 2. Simultaneous flips and original targets

In a diagonalized spherical quadrangulation every shaded triangle
belongs to exactly one recorded port: the matching pairs its two
triangles. Hence the interiors of the quadrilaterals for distinct ports
are disjoint. Assume all quadrilateral faces have four distinct
vertices, and flip any collection I of ports simultaneously. Every
original MAIN edge and all four boundary incidences of each port are
unchanged. The two protected vertices remain distinct and joined by the
same MAIN edge. The new matching edge bc lies inside the old port disk.

The resulting object is a spherical triangular cellulation. It can have
parallel edges if bc was already an edge, and two resulting triangles
can have the same label set. These are distinct cell incidences. No
loop is introduced because the original port has four distinct
white vertices. No actual flat-plat realization of the changed matching
graph is asserted or needed for the following classical capacity bound.

Take a feasible original shared flow q. Let I contain every port where
q has a genuinely overloaded middle; assign either side at a closed
seam consistently if desired. On each unflipped CROSS port, choose
its entropy-maximizing original triangle split. On each flipped port,
use (1), or its RIGHT version. This produces a feasible COMPLETE
triangle flow on the changed cellulation, with the SAME unit ordinary
targets, the SAME protected zeros, and the SAME total supply. Therefore

    sum_e barH(q_e)+sum_(e in I) f(1-q_(e,child))
        <= Phi_complete(D_I; original marks).            (4)

One may retain the larger explicit gains in (2). The right side is the
actual normalized complete angle capacity of the changed cellulation,
not the original Phi_D. At seams, use their actual closed CROSS/Green
agreement; no finite path label is reassigned in a quantum polynomial.

The simple-block construction applies to this classical
capacity, including parallel-edge splitting: if feasible, it is the
sum of the new simple-block polyhedron volumes divided by pi, with zero
from double-triangle blocks. The explicit transported flow already
proves feasibility. Thus (4) is a geometric upper bound with fully
preserved demands, not independent optimization at separate ports.

## 3. The missing comparison for a prescribed chart remains geometric

Equation (4) is valid for every finite quadrangulation in the stated
class and every fixed original MAIN mark. It does NOT prove sum barH<=Phi_D. The flipped cellulation has
new matching edges, and its complete block-volume sum has not been
compared with the original complete volume. The actual old circle
packing does not supply tangency along a newly inserted bc edge.

Nor is this an equality of original quantum sources, or a licensed
change of the original knot/crossing-circle topology. Any claim that
the changed block volume is bounded by Phi_D, or by Phi_D plus the
explicit local gains in (2), requires an additional proof. The new
point is the exact load-preserving, nonnegative entropy comparison;
neither a minimum/maximum exchange nor a sign-cocycle assumption occurs.

## 4. Every nonsimple diagonalization lies strictly below the maximum

Fix ANY finite connected SIMPLE spherical quadrangulation Q, with
R>=2 faces and four distinct boundary vertices in each face. Its
vertices will be white faces and its quadrilateral disks will be
ports. Choose independently one diagonal in each of its R faces.
This gives 2^R labeled triangular cellulations T. Choose any original
MAIN edge uv as mark; it is retained in all of them.

The MAIN graph is bipartite: assign alternating parities around each
quadrilateral, which integrate globally because all facial cycles have
even length. A diagonal joins equal parities; a MAIN edge joins
opposite parities. Thus a repeated edge in any T consists entirely of
diagonals. There are no loops and no repeated MAIN edge.

There exists a simple diagonalization by a purely combinatorial
argument, before any entropy is considered. If two selected diagonals
are parallel, choose their embedded digon and either side. A boundary
diagonal bc belongs to a quadrilateral whose adjacent third vertices
x,y are strictly on opposite sides of the digon. Replacing bc by xy
introduces no repeated edge: an old xy edge would cross the digon.
It removes one repetition of bc. Thus the finite integer sum of
max(0,edge multiplicity-1) strictly decreases. Iterate to obtain a
simple triangulated sphere on the same vertices. This uses no angle
feasibility or chosen radius. All faces still come from the original
four-distinct-vertex quadrilaterals.

Let Phi(T;u,v) denote each chart's complete angle capacity, allowing
-infinity if its fiber is empty. Every nonempty fiber is compact and
has a maximizer. The simple chart just constructed has finite positive
capacity by the simple-sphere packing/angle theorem. Therefore
the largest capacity among the finitely many charts is finite and
attained.

Suppose T has two parallel matching edges joining b,c. They form an
embedded digon. Since the fixed marked vertices u,v are joined by a
MAIN edge, one side of this digon has no marked vertex strictly inside.
Choose that side. If it has v interior vertices, it contains 2v
triangles. Their total supply v equals the total ordinary demand of
those interior vertices, so every b- and c-corner on that side has
load zero in EVERY feasible complete flow.

Take one boundary matching edge e. Its inside triangle is (b,x,c)
and its outside triangle is (b,y,c), where x is strictly inside the
digon and y strictly outside. Both differ from b,c, and x!=y, as the
quad has four distinct vertices. In any maximizing complete flow the
inside triangle is pure x, with load 1/2. Consequently the local
combined degree has q_x=1/2 and the local entropy is exactly the
entropy of its outside triangle: this is the seam value G with child x.

Flip e to xy and use the transport of section 1 at nu=1/2. It preserves
all global demands and does not decrease entropy. Hence the capacity
of the new chart is at least that of T. Strict increase is not needed.
The edge xy did not already occur: an existing embedded edge from x
strictly inside to y strictly outside would cross the digon boundary,
whose only vertices are b,c. Thus this flip removes one occurrence of
a repeated bc edge and introduces no repeated xy edge.

The nonnegative integer sum over unordered vertex pairs of
max(0,edge multiplicity-1) decreases by one. Iterating terminates at
a SIMPLE chart, without decreasing capacity.

In fact the LAST flip in this process increases capacity strictly.
Write the maximizing outside triangle loads, in the order (b,y,c),
as (a,t,d), where a+t+d=1/2. Its inside triangle is pure x. The
explicit new rows in the final simple chart are

    (x,b,y)=(1/2-a,a,0),
    (x,c,y)=(a,d,t).                                    (5)

Their entropy minus the old two-triangle entropy is exactly 2f(a).
If 0<a<1/2 this is positive. If a=0 or a=1/2, one of the two new
triangles has a zero corner at x. The vertex x is ordinary: it lay
strictly inside the mark-free digon. In a SIMPLE marked sphere the
unique complete entropy maximizer is strictly positive at every
allowed ordinary corner, apart from its already fixed singleton
rows, where that ordinary load is 1/2, never zero. Thus the transported
flow in (5) is not a maximizer of the final simple chart. Its capacity
is strictly larger even in this endpoint case.

Consequently every feasible nonsimple chart has capacity strictly
smaller than some simple chart. An infeasible chart is harmless.
EVERY global capacity-maximizing chart is therefore simple. This
argument does not assert that each intermediate digon flip has a
strict gain; strictness at the final simple chart is sufficient.

In particular the maximum equals the maximum over simple charts. Their capacities are the actual labeled polyhedron volumes divided by pi and are independent of the adjacent marked pair, by the packing construction. It follows that the maximum over all diagonalizations is itself independent of which original main edge is marked.

## 5. A sharp global inequality for every maximizing diagonalization

Choose a complete-capacity-maximizing diagonalization D of Q. Section 4
proves that D is simple. Define its sharp piecewise local barH and its
original unit-target fiber exactly as in the exact-G note. Then

    max_(q in original closed NC fiber) sum_e barH(q_e)<Phi_D. (6)

Here is a proof retaining every boundary case. If q has a genuinely
overloaded port with 0<nu=1-q_child<1/2, flip all its overloaded ports.
Equation (4) and flip maximality give

    sum_e barH(q_e)<=Phi_D-sum_(overloaded e)f(nu_e)<Phi_D.

Otherwise all genuinely overloaded rows are pure-child vertices
(nu=0), and every other row is in the closed CROSS domain. If at least
one pure-child row occurs, flip precisely those ports. The transported
complete triangle flow has entropy equal to the original sum barH.
If the new chart is nonsimple, section 4 bounds its capacity strictly
below Phi_D. If it is simple, at a flipped pure-child port BOTH new
triangles are pure at the child. The child is ordinary; at least one
of the other three distinct vertices is ordinary as well, since only
two vertices are protected. Its corner load in the transported flow
is zero. Thus this flow is not the strictly positive ordinary-corner
complete maximizer of that simple chart, and its entropy is strictly
below that chart's capacity, which is at most Phi_D.

Finally suppose there is no genuinely overloaded row. Then every row
is CROSS, and the original closed NC condition means some middle load
equals 1/2. The simple chart's complete entropy optimizer has no such
middle: a protected middle is zero, and an ordinary middle shares its
triangle with at least one positive ordinary outer corner. Both outers
cannot be the protected pair, since their edge is MATCHING while the
protected edge is MAIN. Thus every ordinary middle is strictly below
1/2. Uniqueness of the complete triangle optimizer gives a strict loss
for this seam datum as well.

If the original closed NC fiber is empty, its gap assertion is vacuous.
Otherwise that fiber is compact and barH is continuous, so the
pointwise strict inequality has a uniform positive gap. This proves (6)
using ONLY the complete angle-capacity geometry of simple spheres and
the local exact G. No full-kernel endpoint forest theorem, physical
pure-middle deletion or flat-gap assumption is used in this argument.

For an ACTUAL eligible original flat-plat source D whose white chart
is such a maximizing diagonalization, the conditional
theorem in the exact-G note now gives the full original independently
signed long-filling volume limit, for all fixed sufficiently long twist
vectors, both level parities and the original normalization. No new
spectral-cycle argument is needed for that stated source class.

The geometric hypothesis can equivalently be checked using the actual
block volumes of the finitely many parallel-edge charts. The existence
theorem in section 4 proves that every eligible MAIN quadrangulation
has an ABSTRACT simple maximizing diagonalization and the sharp gap
(6). It does NOT prove
that an arbitrarily prescribed source is maximizing, or that the new
maximizing diagonalization has a literal flat-plat realization with the
same fixed bridge width and independent original twist boxes. That
source realization is a separate issue. No change of the original knot
or equality between different diagonalized quantum sources is asserted.

## Dependencies

The local inputs are the [exact sharp Green spectral maximum](research_sharp_green_spectral_maximum.md), sections 1--5, and the
[absolutely normalized triangle entropy](actual_triangle_entropy_algebraic_balance.md).
The global classical inputs are the [complete angle-capacity and simple-block construction](actual_smoothed_source_capacity_blocks.md), sections 1--5: compact duality,
strict positivity and uniqueness of the simple-sphere optimizer, and
absolute polyhedron-volume normalization. That construction also proves
independence of a simple chart's capacity from its adjacent marked pair.
The stated corollary for an already eligible original flat source uses
section 7 of the exact-G note and its original whole-period dependencies.


The conclusion selects a maximizing diagonalization in a finite family.
It does not assert that every prescribed diagonalization is maximizing,
that different choices define the same link, or that an abstract choice
has a prescribed flat-plat width. A separate actual-source construction
and its analytic/geometric adapters are required to draw a knot-volume
conclusion for the newly selected general diagram.
