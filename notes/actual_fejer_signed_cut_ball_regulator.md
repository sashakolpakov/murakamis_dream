# The global signed cut-ball regulator, with the original marked apex

31 October 2026. conditional stationary-stratum lemma. Hypotheses are exactly the
finite-positive-ordinary-radius stationary stratum and signed/cooriented
circle development of [the marked signed-development lemma](actual_fejer_marked_signed_development.md).
This proof does NOT use invariance of an open crossing regulator under
resetting a Gauss frame: that assertion failed the recorded direct test.
The original graph, marking and untwisted shaded pairings stay fixed.

## 1. An elementary cyclic polygon chain identity

Let z_0,...,z_(n-1) lie on one Euclidean circle, in their RECORDED polygon
order, not necessarily its circular order. Choose real arguments phi_j
for the points. Consecutive increments d_j=phi_(j+1)-phi_j may be signed
and may differ by multiples of2pi; close with phi_n=phi_0+2pi w.
Cone an oriented fan triangulation of this polygon to the common ideal
point infinity in upper half-space. Its oriented volume is

  sum_(j=0)^(n-1) Lambda(d_j/2).                       (1)

For an oriented triangle of distinct points on a circle, the usual
ideal-tetrahedron angle formula gives (1): its three oriented half-arcs
are its three angles modulo pi, with the common orientation sign.
Lambda(-a)=-Lambda(a), Lambda(a+pi)=Lambda(a), and
Lambda(pi-a)=-Lambda(a), so the formula is independent of the chosen
argument lifts and holds for either triangle orientation. Sum it over
the fan. Each internal diagonal appears with opposite orientations;
its two Lambda terms cancel EXACTLY. Only the original boundary edges
remain. No convexity or winding-one assumption has been used.

The identity also includes repeated nonadjacent polygon vertices.
First apply the finite fan identity with distinct generic points on
that SAME circle. An edge with coincident endpoints contributes
Lambda(0)=0. Any degenerate fan tetrahedron has zero limiting volume:
its coalescing base points stay on this one circle, so its cross-ratio
with infinity tends to the real axis. Equivalently use the normalized
alternating ideal chain with repeated vertices set to zero. This is
not an arbitrary four-ideal-point collision assertion. For a polygon
on a line, every cone tetrahedron is coplanar with infinity and (1)
has value zero in the limiting line interpretation.

## 2. Apply it to the ONE signed developed circle family

At a finite white vertex f, its actual face polygon consists of the
contact points with its neighboring white circles, in the original
cyclic source order. At a triangle t its two successive contact rays
turn by sigma_t theta_(t,f), modulo2pi. Hence (1) gives its oriented
white-pyramid volume as

  sum_(t at f) sigma_t Lambda(theta_(t,f)/2).          (2)

This works at an overloaded vertex with winding zero just as at a
winding-one vertex. If its generalized middle corner is written
2pi-theta rather than -theta, its Lambda contribution is identical
by pi-periodicity. Thus no integer winding/branch constant is lost.
Both marked white faces are lines through the cone apex and have
zero contribution, matching their zero center angles.

The shaded face of t is the ideal triangle of the three pairwise
contacts of its tangent white circles. For a finite or one-line
triangle its Euclidean angles are (pi-theta_(t,f))/2. Its orientation
in the common plane is sigma_t times the original positive convention.
Consequently coning this original ordered shaded triangle to infinity
gives

  sigma_t sum_(f in t) Lambda((pi-theta_(t,f))/2).      (3)

This elementary contact-angle relation is unchanged by reflection of
a center triangle. A two-line uv triangle contains the apex itself;
its cone has zero volume, and (3) is zero because theta=(0,0,pi).
These are precisely the forced degeneracies allowed here.

Summing (2),(3) for one abstract cut ball gives

  V_ball = (1/2) sum_t sigma_t V(theta_t).             (4)

The developed boundary can overlap or fold. Equation (4) is the volume
of its oriented chain, not the volume of an embedded region.

## 3. Why this is the original representation fundamental chain

Use the TWO literal topological cut balls of the original augmented
projection, with their original white/shaded cellulation and face
permutations. On the first ball map every ideal contact vertex to its
contact point in the ONE developed family. Map white polygon edges
and shaded edges to their geodesics, and triangulate each white face
by a fixed original combinatorial fan. These finite oriented face
chains form a closed boundary cycle: every original edge occurs twice
with opposite orientations, even if developed contacts coincide.
Use the EXISTING labeled convex right-angled certificate to select the
actual abstract triangulation once and for all: fan each incident white
face from the original marked vertex p; triangulate every nonincident
white face compatibly; then cone p to the nonincident triangles. The
certified convex ball proves that this is a degree-one triangulation of
the original ball. Keep that exact labeled abstract chain and merely
change its developed ideal vertices to the signed circle contacts.
Its volume is the cone of the boundary cycle to p=infinity; triangles
already incident to p contribute zero cone terms. No new interior ideal
vertex or new cusp is introduced. Degree one concerns the abstract
original domain only, not its possibly folded developed image.

Use ONE global reflection r_u to map the second ball. Reverse its
abstract orientation together with this orientation-reversing target
reflection, so its volume contribution is the same as (4). Do not
choose independent block, port or face reflections for that ball.

The face pairings agree with the original representation as follows.
On a white face f, the prescribed orientation-preserving map is
r_f r_u; reflection r_f fixes the entire white plane. It therefore
identifies the complete second-ball white polygon chain with the
first-ball chain, including every vertex and the original edge order.
Here are the shaded maps with the actual copy labels and permutation.
All ports in this endpoint source are UNTWISTED. In each original ball
write its two shaded triangles as

  S_0=(O,C_1,C_2), S_1=(O,C_3,C_0).

They pair WITHIN that same ball by O->O, C_1->C_0, C_2->C_3; this is
exactly (3) of [the original matching geometry](general_augmented_plat_matching_geometry.md), not the
across-copy half-twist permutation (4). In the first ball, input A_b
has its fixed flag C_1=x/b contact, input B_b its fixed flag C_2=b/y
contact, and P=B_b A_b its flag O=x/y contact. Equation (5) of the
line adapter gives C A_b C^-1=A_c, C B_b C^-1=B_c, and CP=PC.
Therefore C sends these THREE flags respectively to C_0=x/c contact,
C_3=c/y contact, and O. They are distinct at every permitted finite,
one-line and two-line triangle. The ordered ideal-triangle isometry is
thus exactly C, including its original pointwise permutation.

On the reflected second ball the map is r_u C r_u (composition of
anti-Mobius maps on either side), from r_u S_0 to r_u S_1 with the
SAME three labels. The reverse pairing is its inverse. Thus no shaded
face is silently moved across copies and no independent reflection is
selected for the second map. Its whole ideal face is paired, not only
the common auxiliary fixed point. These are precisely the untwisted
Morse/threading pairings already used to construct the representation.

Hence the two abstract ball chains descend, with THEIR original
multiplicities and orientations, to an equivariant relative fundamental
chain of the original exterior. In particular an immersed white polygon
is not replaced by its image counted once, and an overloaded winding-
zero face is not deleted from the abstract source cellulation.

For completeness this ideal-chain construction has the usual genuine
cusp realization. Each main meridian is NONCENTRAL parabolic: its two
adjacent white circles are distinct and tangent. Its actual longitude
commutes with it, hence belongs in PSL2 to its translation centralizer
and preserves every horosphere at the same contact. At an auxiliary
cusp the ACTUAL two generators are C^-1 and its preferred longitude
P=B_b A_b (with the already recorded harmless central lift). Both are
in the same parabolic translation group at the outer contact. This
remains true if C=I: P is still noncentral because the matching outer
pair is distinct and tangent. Commuting with identity ALONE is not
used to infer any peripheral property. Thus the WHOLE peripheral
subgroup preserves the chosen contact horosphere in every case.

Decorate each contact by the horosphere
of its ordered tangent white pair (normalize the pair to opposite
parallel planes at width1, then take height1). The actual shaded map
carries this decoration: it carries both adjacent white planes,
because each is the unique plane orthogonal to the shaded plane along
the corresponding edge. White reflections carry it as well. Use
finite INCIDENCE corner points on these paired horospheres, truncate,
and attach the original conical cusp tails. The established O(T^-2)
horospherical boundary flux compares this with the ideal chain.
No parabolic cusp vertex is falsely assigned a single fixed finite
point. Only finitely many paired incidence points are used.

Thus representation volume, defined by the original equivariant
relative fundamental class, is

  Vol(rho)=2 V_ball=sum_t sigma_t V(theta_t).          (5)

All boundary/pairing data have been checked at the global chain level.
An individual re-framed open crossing word need not have its former
regulator. Its boundary correction is not discarded or assumed zero
locally; instead (5) computes the sewn fundamental class directly.

## 4. The conditional actual-entropy consequence

At the stationary stratum under discussion, the [proved exact coefficient
identity](actual_fejer_half_block_entropy.md) is C(alpha)=V(2pi alpha)/(2pi). A cross port contributes the
sum of its two C's; a strict left/right Green port contributes their
signed difference, including the forced marked zero limits. These are
the actual local E values, with their absolute normalization. Therefore

  sum_e E_e = (1/(2pi)) sum_t sigma_t V(theta_t)
            = Vol(rho)/(2pi) <= Vol(Y_D)/(2pi).         (6)

The last inequality is the [proved representation-volume bound](general_representation_volume_kernel_strictness.md)
for the actual original hyperbolic exterior. No action constant, reference-flag
normalization or separately chosen regulator has been introduced.

This handles a FULL stationary configuration with finite positive
ordinary radius multipliers and only the forced marked-line
nonregularities. It is not yet the inequality for every maximum W_D.
Additional ordinary zero/infinite multipliers, flat triangles, diagonal
mu=nu, terminal nu=1/2 and other free KKT strata still require their
own limiting or block construction. In particular one cannot silently
change an eventually feasible forest type into a cross type: the exact
finite support can prevent that even when their limiting local entropy
and degree vector coincide.

The cut-ball comparison is on the stated stationary stratum. It does not cover every boundary maximum or select a quantum cycle.