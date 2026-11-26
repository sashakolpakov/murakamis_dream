# A unique main-edge mark and the exact protected-corner normal form

Private written proof, 17 November 2026. A permitted choice of the
original main-edge mark limits the boxes containing both protected
faces to two corner occurrences. This is a combinatorial statement
with an exact full-source consequence. It does not simplify the
remaining attachment or prove a geometric contribution nonzero.

## 1. The original graph has a unique-adjacency main edge

Use the connected complete-colored source of [A], with \(R>0\)
original boxes, their fixed ordered quartets, and arbitrary full
polynomial Casimir coupons with their retained crossings. Suppress
degree-two Morse bends and contract each matching edge inside its
coupon disk. The result is a connected plane graph \(G\) with
\(R\) four-valent vertices and \(2R\) main edges. Loops and multiple
edges are allowed. The matching contraction retains every main edge
and every original face.

Let \(Q\) be the plane dual. Then
\[
 |V(Q)|=R+2,\qquad |E(Q)|=2R.
 \tag{1}
\]
Every face boundary walk of \(Q\) has length four, counted with
multiplicity. For the source tuple \((x,b,c,y)\), its cyclic
boundary order is \((x,b,y,c)\), or the reverse order. Thus it is
the same literal quartet of one original box, with its order recorded.
The graph \(G\) has no bridge: deleting a putative bridge would
leave a component with exactly one odd total incidence, contrary
to the even degrees. Consequently \(Q\) has no loop. It is connected.
It is also bipartite: any simple cycle bounds a union of faces,
and summing their even boundary lengths shows that cycle has even
length. Its colors are the original checkerboard colors; the two
opposite slots of every quartet have the same color.

**Unique-adjacency lemma.** At least two edges of \(Q\) are the
only edges between their respective endpoints.

Indeed let \(s\) be the number of distinct unordered adjacent pairs
and \(t\) the number of pairs of multiplicity one. The simple support
of \(Q\) is connected, so \(s\ge |V(Q)|-1\). Counting multiplicities,
\[
 2R=|E(Q)|\ge 2s-t
       \ge 2(R+1)-t,
 \tag{2}
\]
which gives \(t\ge2\). This counts actual main edges, not a newly
chosen diagonal or matching edge.

Choose one such edge with distinct endpoints \(u,v\). The full
main-edge transport theorem [A] permits exposing this same original
main edge as the marked cap by sphere rerouting and actual turns.
All coupon disks, ordered quartets, and full homogeneous polynomials
\(H_e\) remain unchanged. Therefore the original scalar is exactly
\[
 Z_N=[\prod_{f\ne u,v}L_f^d]\,
       \left.\prod_eH_e(L)\right|_{L_u=L_v=0},
 \quad d=N-1,\quad N\ge3.
 \tag{3}
\]
This is the full source equality of [A], including both parities,
all root Hermite data, original pivots, and separately retained
exterior factors. It is not insertion of a reset mark into an old
internal head, nor equality of projected sectors or absolute bounds.

## 2. Classification of every box containing both protected labels

The colors of \(u,v\) are opposite. Hence if both occur in a
quadrilateral walk, they occupy adjacent slots somewhere in that
walk. That adjacency must use the unique edge \(uv\). Every edge
of a plane graph has exactly two side occurrences in its facial
walks. Thus there are at most two such box occurrences.

There are precisely two possibilities.

* If \(uv\) is not a bridge, its sides belong to two distinct faces
  of \(Q\). Each of these faces is a quadrilateral with four
  distinct vertices, containing \(u,v\) once each in adjacent slots.
  The other two vertices are distinct ordinary faces.
* If \(uv\) is a bridge, both sides belong to the same facial walk.
  Up to cyclic order and reversal it is \(u\,v\,u\,w\) or
  \(v\,u\,v\,w\), where \(w\notin\{u,v\}\). Thus one box has three
  protected slots and one ordinary slot.

Here are the repeated-walk checks. An edge has the same face on
both sides exactly when it is a bridge: a nonbridge belongs to a
simple cycle, whose two sides lie in different complementary regions;
a bridge is traversed out and back in its single incident face.
In the nonbridge case, repeating \(u\) or \(v\) in a four-step walk
would use \(uv\) twice, contrary to the two distinct incident faces.
Repeating the two other slots would give a loop. In the bridge case,
the two remaining steps form an out-and-back walk at one endpoint,
giving the displayed third vertex \(w\). Four protected slots would
traverse the unique edge \(uv\) four times, although it has only two
side occurrences, and are impossible. In particular the connected
graph here has \(R+2\ge3\) vertices.

This classifies boxes containing both protected labels. A different
box may contain neither label, one label once, or one label in both
opposite slots. All those boxes remain in the attachment polynomial,
with repeated incidences substituted literally. The theorem does not
turn an opposite-zero specialization into an adjacent-zero kernel.

For clarity, the two ordinary edges opposite \(uv\) in the nonbridge
case form a graph with at most two edges and no loops. It is a forest,
or its only non-tree component is a two-edge cycle with common
endpoints. The source does not require this graph to be connected.
No assumption of a simple quadrangulation was made.

## 3. The exact source normal form

For arbitrary coupons let \(B_e\) denote the full specialization
of each selected box at its protected slots. Put every other
specialized box, unchanged, in \(A_N\). This gives exactly
\[
 Z_N=[\prod_{\rm ordinary}L_f^d]\,
               A_N(L)\prod_{\rm selected\ boxes}B_e(L).
 \tag{4}
\]
There is no restriction on the valency, degrees, signs, or shared
variables of \(A_N\).

In the bridge case homogeneity gives \(B_e=\alpha_{e,N}L_w^d\).
The scalar \(\alpha_{e,N}\), possibly zero for an arbitrary coupon,
is its actual coefficient. Hence (4) eliminates this face exactly:
\[
 [L_w^d]\,\alpha_{e,N}L_w^d A_N
              =\alpha_{e,N} A_N|_{L_w=0}.
 \tag{5}
\]
If the selected coupon is the literal signed crossing \(R^\sigma\),
\(\sigma=\pm1\), then [H, (10)] gives
\[
 \alpha_{e,N}=
 \begin{cases}
 \lambda_0^\sigma,&\text{the remaining slot is middle},\\
 \lambda_0^\sigma(-q^\sigma)^d,
                       &\text{the remaining slot is outer},
 \end{cases}
 \qquad \lambda_0=q^{d^2/2}
 \tag{6}
\]
on the original square-root lift.

In the nonbridge case, suppose the two selected coupons are literal
signed crossings. Write \(s_e\) for the remaining ordinary middle
face and \(t_e\) for the remaining ordinary outer face. The exact
corner identity [C, (8)] is
\[
 B_e(s_e,t_e)=\lambda_0^{\sigma_e}
        \sum_{j=0}^d\kappa_e^j s_e^{d-j}t_e^j,
 \qquad \kappa_e=-q^{\sigma_e}.
 \tag{7}
\]
The pair symmetries of the original coefficient [H, (10)] cover
all four adjacent protected-slot orders. No value-only
interpolation or forgotten normal is used.

Apply the full-block coefficient reduction [F, Sections 3--4] to
(7), with its entire polynomial attachment. Its elementary step is
\[
 [s^d t^d]\,B_e(s,t)A(s,t,\ldots)
       =\lambda_0^{\sigma_e}[t^d]\,
                         A(\kappa_e t,t,\ldots).
 \tag{8}
\]
Thus each tree component fuses exactly to one face with target \(d\).
The second edge, and every other incident factor, participate in the
displayed substitution; no attachment is first evaluated at a
geometric point. Let \(\epsilon_f\) be the bipartite coloring and
write \(L_f=\epsilon_f w_f\). The ordinary middle and outer colors
are opposite. In these checkerboard face variables, (8) reads
\[
 w_{\rm middle}=q^{\sigma_e}w_{\rm outer},
 \quad\text{equivalently}\quad
 w_{\rm outer}=q^{-\sigma_e}w_{\rm middle}.
 \tag{9}
\]
This finite shift is retained even though its classical limit is
equality.

For a two-edge cycle, reverse an edge if necessary, retaining
\[
 B_d(t,s;\kappa)=\kappa^d B_d(s,t;\kappa^{-1}),
 \quad B_d(s,t;\kappa)=\sum_{j=0}^d\kappa^js^{d-j}t^j.
 \tag{10}
\]
The two-edge internal degree is already \(2d\), so the entire
attachment must have degree zero in its two vertices. Its exact
factor is the retained monomial unit times
\[
 \sum_{j=0}^{N-1}q^{Sj}
       =N\,\mathbf1_{S\equiv0\pmod{2N}},
 \tag{11}
\]
where \(S\) is the signed sum of the two crossing exponents in
the chosen cycle orientation. It is even; the signs in the two
\(\kappa_e\)'s cancel around this even cycle. The scalar factors
\(\lambda_0^{\sigma_e}\) and the units from (10) stay outside (11).
This is exactly the loop rule of [F], not an assumption that the
cycle holonomy is trivial. The attachment is evaluated at zero
in both cycle variables. If the filter is zero, this entire
marked coefficient is zero.

For selected coupons other than literal crossings, (4)--(5) still
hold, but their \(B_e\)'s must be kept as their actual specialized
polynomials. Neither (7) nor the crossing fusion rule is assigned
to an arbitrary Casimir coupon. Likewise expanding a crossing
power into layers requires the actual coefficient convolutions
and their original internal targets.

## 4. What the choice of mark does and does not accomplish

The result supplies a mark for every connected original projection,
without assuming a successful geometric bound at that mark. It
reduces the incidence of boxes containing both protected faces to
the explicitly classified cases, and signed crossing corners then
admit exact fusion against an arbitrary attachment. Boxes with only
one protected label, including repeated opposite occurrences, are
still present. Their source cost has not been estimated.

The weighted identifications (9) are coefficient identities. They
do not by themselves flatten developed tetrahedra, erase a meridian
face transport, identify the reduced polynomial with a smaller knot
source, or prove a selected boundary saddle nonzero. All ordinary
targets and actual attachment factors are retained throughout.
Fixed-root external parameter derivatives commute with the exact
full-source formulas; no genuine-\(q\) continuation is inferred.

## Complete direct sources

All four complete texts and their directly used implications were read.
This proof uses no programs, numerical tests, or public/frozen edits.

| Label | Source | SHA-256 |
|---|---|---|
| A | [Arbitrary original main-edge mark transport](research_arbitrary_main_edge_mark_transport.md) | 7a7c9efdca1e9f7907dc5baf5dfe8ba12e2345ee5f2df2ed94240e95ee69112a |
| H | [Homogeneous full Casimir face source](actual_homogeneous_casimir_face_source.md) | a7d89f310f2cb4193ab73ef49f715198b224d1c3756d84c4cb940d7fa850c2f2 |
| C | [Actual protected cap-turn interface](research_trace_one_mark_and_cap_turn_interface.md) | d1be51d8fcaad2dd4886769ed5e172ceeaff66891c5cb1e46f29917d5ee97e48 |
| F | [Forced full-block source fusion](actual_forced_source_fusion.md) | d1703e448ff328536f1194605dc77273daf85361aa0cd244af834880a1669f76 |
