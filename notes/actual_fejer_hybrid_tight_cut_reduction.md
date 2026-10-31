# Hybrid Fejer flow: all proper tight sets come from permitted digon cuts

31 October 2026. This is a finite incidence
theorem for the ACTUAL loopless white triangular cellulation obtained
after source-preserving identity smoothing. The
[closed local entropy](actual_fejer_half_block_entropy.md) and
[original shared source](actual_fejer_shared_entropy_variational.md)
provide its local functions and literal incidence conventions. It does not replace a
matching/matching Green cut by two independent entropy maxima.

## 1. Literal hybrid network

Let T be a loopless triangular cellulation of the sphere, with R+2
white vertices and 2R triangular cells. Multiple edges remain distinct.
The dual cubic graph has its original perfect matching: each port is
the pair of triangles adjacent to its matching white edge. Keep two
distinct protected white vertices u,v joined by an actual edge. Every
other white vertex has target1; both protected targets are0.

Some ports are tagged CROSS, others GREEN. A CROSS port retains its TWO
triangle nodes, each of supply1/2, incident to that triangle's ordinary
vertices. A GREEN port has ONE node of supply1 and its FOUR original incidences
x,b,c,y: shared outer triangle corners x,y are aggregated once. Distinct
incidences among these four remain parallel arcs if their global face
labels coincide. This is the
hybrid limiting flow used to perturb a fixed cross/strict-one-sided
entropy point. The full supply is R, equal to the ordinary targets.

For a set S of ordinary vertices let C_0(S) be the total supply of the
complete triangle network touching S, and C_H(S) that of the hybrid
network. Directly from the original pair of half-supplies,

    C_H(S)=C_0(S)+(1/2)g(S),                        (1)

where g(S) counts the GREEN ports for which EXACTLY ONE of the two
triangles touches S. In particular merging a pair never lowers a Hall
capacity. The finite flow criterion is C_H(S)>=|S| for every S.

## 2. Complete Hall inequality and the equality case

Take a nonempty proper S among the R ordinary vertices, and put
U=V(T)\S, n=|U|. The induced embedded graph G=T[U] is loopless and
contains the retained protected edge uv. Let p be the number of
original triangular cells wholly supported on U. Each is still an
actual face of G; a triangular face of G enclosing removed vertices
does NOT count in p. Every other original triangle touches S, so

    C_0(S)=(2R-p)/2,
    C_0(S)=|S| iff p=2n-4.                         (2)

Here is a face count which also handles disconnected induced graphs
and isolated vertices. Move one point of S to infinity. Every original
triangle supported on U is bounded in this planar drawing. For a
connected component G_i with n_i>=2 vertices, write f_i for its bounded
faces, e_i for its edges and p_i for its bounded original triangles.
All face boundary walks have length at least2. Euler and edge counting
give

    e_i=n_i+f_i-1,
    2e_i>=3p_i+2(f_i-p_i)+2,
    p_i<=2n_i-4.                                  (3)

The final2 is the outer boundary walk. An isolated vertex contributes
no triangle. If there are c>=1 nontrivial components and a isolated
vertices, summing gives

    p<=2(n-a)-4c<=2n-4.                            (4)

Thus the complete and hybrid Hall inequalities hold. For S empty or
all ordinary vertices they are the trivial zero or total balance;
every triangle has an ordinary corner because it has three distinct
vertices and only u,v are protected.

If S is proper and tight, p=2n-4. Equations (3)--(4) force a=0,c=1:
G is connected. Every face not one of the p original triangles has
boundary walk EXACTLY two edges, including the outer face. Since
proper S implies n>=3, such a two-edge face cannot be one bridge
traversed twice: its next boundary step would continue around the
nontrivial remainder at one of its endpoints. Equivalently a bridge
bounding a complete two-step face walk would make the entire connected
graph a single edge. Consequently these faces are genuine digons
bounded by two DISTINCT parallel original edges.

Every removed S vertex belongs to the interior of one of these digon
faces. Conversely each such non-original face contains removed vertices;
the original cellulation is triangular. Therefore S is precisely the
union of the interior vertex sets of these pairwise interior-disjoint
actual digon disks. Each disk is mark-free in its interior. This
classification uses the induced graph at S, not an assumed preselected
digon decomposition tree.

## 3. Hybrid tightness merges only neighboring holes with the same endpoints

Suppose C_H(S)=|S|. Then (1) and (4) force both C_0(S)=|S| and g(S)=0.
Consider the digon disks from section2. Across an edge on one such
disk's boundary, the inside triangle touches S. If this edge is
MATCHING and its port is GREEN, the other triangle must touch S too,
or that port would contribute to g(S). That other triangle belongs to
a second digon disk on the other side of the SAME boundary edge.
The two digons therefore have the same ordered pair of boundary
vertices. Merge them across that green edge. Their union is again a
digon disk bounded by the two remaining parallel edges.

For clarity, all these mergers can be done at once. The adjacency
graph of the S-digon disks across green matching boundary edges has
degree at most2. Every connected component has a fixed endpoint pair.
It cannot be a cycle for a proper S: a full cyclic family of parallel
edge sectors fills the sphere except those two vertices, so the
connected induced graph G would have only those vertices, contrary
to n>=3. Its components are paths; each merges to one actual digon.
This also proves that an intervening matching edge is removed only
from the description of the separating boundary, not from the source
or from its Green pair.

After merging, every surviving matching boundary edge belongs to a
CROSS port. A MAIN boundary edge never splits a paired triangle node.
The two boundary edges of each resulting digon have the same type:
the disk contains 2v triangular cells for v interior vertices, and
the parity count of their one matching incidence per dual vertex
forces an even number of matching edges to cross its two-edge boundary.
Thus the permitted cuts are exactly

    MAIN / MAIN; or MATCHING / MATCHING with BOTH ports CROSS. (5)

Each resulting disk is individually hybrid-tight. Its 2v triangles
exhaust the demand v of its interior vertices; no green node crosses
its boundary. The original tight set is a union of their interiors.
In particular a general GREEN matching/matching cut has NOT been
declared tight, split, or assigned additive entropy.

The full set S of ordinary vertices is only the redundant total
balance. Its possible U={u,v} one-edge or full-cycle exception does
not force any additional ordinary incidence to vanish.

## 4. Forced zeros and a positive relative-interior witness

For any feasible hybrid flow, a tight S forces every node touching S
to send its entire supply into S. Thus each of its arcs to an ordinary
vertex outside S is zero. Conversely an ordinary incidence arc is
forced zero ONLY this way. One direct proof avoids a nondegeneracy
assumption on the balance matrix. To force a small positive amount
epsilon on an arc n->f, reduce that row supply and the target at f
by epsilon. For any vertex set S containing f, both capacity and
demand decrease equally. For S not containing f but touched by n,
only capacity decreases. Such a constraint obstructs every positive
epsilon exactly when S was tight. The finitely many other inequalities
have positive slack, so a sufficiently small epsilon preserves them.
The ordinary Hall criterion then supplies the remaining flow.

Hence every non-forced ordinary arc is positive in some feasible flow.
Averaging finitely many such flows gives one witness positive on ALL
non-forced ordinary arcs and zero on the forced ones. Redundant face
balances cause no difficulty. Equations (2)--(5) show that all forced
zeros have the precise source-permitted digon origin above.

Inside a MAIN/MAIN tight disk, whole ports remain inside and all
incidences at its boundary white faces are zero. At a permitted
MATCHING/MATCHING cut, its two inside CROSS triangles each have their
two boundary corners zero and their interior middle corner1/2. These
are constant, zero-entropy triangles. Only CROSS pairs are cut, so
their additive C+C data may be retained/repaired across the boundary;
no difference E=C_input-C_output is separated into independent pieces.
The original outside and inside middle degrees are not reset by this
network statement. Geometry and actual face-pairing assembly remain
separate obligations.

These cuts may be iterated as an exact HYBRID flow decomposition. Close
the two sides by identifying their two boundary edges. The inside has
new protected pair a,b and the outside retains its old pair. A MAIN cut
leaves whole port nodes on their original sides. At a permitted matching
cut, retain each of the four original CROSS triangle nodes on its own
side and pair the two nodes on a closed side only as the formal C+C
description. This creates no new physical coupon. The inside boundary
loads are zero by tightness, while every outside boundary demand is
unchanged. Thus the original hybrid feasible polytope is exactly the
Cartesian product of those two piece polytopes, and its entropy is their
sum: every GREEN E factor stays whole and every cut factor was additive
C+C. The closure remains loopless, both marked vertices are adjacent,
and every proper cut strictly reduces the number of triangles on each
side. Iteration terminates. On each resulting piece there is no proper
tight set, so section4 gives positivity on every ordinary allowed arc;
the marked zero-dimensional triangle rows retain their fixed values.

## 5. Consequence for the boundary-regularity argument

At a full-kernel maximum, tag terminal seams CROSS and keep the
remaining strict non-diagonal half ports GREEN. The full continuous-h
theorem permits this limiting description without claiming eventual
feasibility of a newly fixed finite label pattern. The cross variables
are their actual two triangle allocations. A small mixture with the
relative-interior witness of section4 remains cross-admissible; each
green point stays in its own strict half chamber because its original
interval length and upper-endpoint margin are positive.

The proved corner expansions then give a nonnegative epsilon log(1/epsilon)
coefficient at every factor. Any zero ordinary degree or cross-triangle
corner that is NOT structurally forced by (5) is activated and yields
a strict positive gain. Thus such a maximum has no free zeros beyond
those tight digon cuts. This assertion keeps diagonal ports excluded;
their negative epsilon log(1/epsilon) term is not an allowed remainder.

To turn this into a volume bound one must use the actual permitted
cut pieces and their inherited marked flags when constructing finite
positive multipliers and the global relative chain. The present proof
is the complete finite support/witness classification, not an assertion
that independent Green capacities factor across arbitrary digons.

## Scope

The induced-face Euler argument includes disconnected induced graphs, digon faces and the proper-subset exception. The iterative cut uses variational C+C bookkeeping; it is not a finite-coupon replacement.

Geometry additionally target-read the final iterative paragraph and
confirmed its Cartesian flow product, unchanged outside targets,
formal matching parity and termination. This record is scoped to the
finite hybrid theorem and its regularity perturbation.

This finite combinatorial proof has no separate numerical audit. It does
not itself identify a group representation or a relative fundamental
class, and it does not infer a phase-sensitive original filling asymptotic.
The geometric piece assembly and whole-source comparison require their
separate proofs.
