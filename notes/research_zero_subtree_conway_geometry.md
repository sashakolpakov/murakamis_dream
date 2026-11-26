# Zero meridian fillings and the resulting strict Conway parent

Research theorem and application, 2 November 2026. Setting an original
crossing power to zero removes its integral box as a through identity.
If every selected vertex has original degree at least three, the
result is still a strict Conway construction, with every remaining
circle and its original marking retained. This observation supplies
a direct volume theorem from the existing strict Conway result.

The boundary polynomial of a connected selected component has a
stronger useful interpretation: its primitive Newton phase is the
longitude polarization of the classical potential of that literal
Conway construction. This also works when the former imaginary-angle
edge chart reaches its endpoint. No assertion that the old chart
remains positive at such a fold is needed.

## 1. Deleting the zero boxes without changing the remaining parameters

Use the original ordered circle-tree construction and its disk-framed
crossing-circle boxes \(P_v\). Each original power is
\[
 n_v=\eta_v-2p_v,\qquad
 \eta_v\in\{-1,0,1\},\quad p_v\in\mathbb Z.
 \tag{1}
\]
Let \(S\) be any set of original vertices, each of original degree
at least three, and give all of them power zero. Necessarily
\(\eta_v=p_v=0\) there. This fills the original meridian and
replaces that box by \(R^0\), the through identity. It does not
replace a turned zero box by the through identity: every physical
quarter-turn adjacent to the box remains in its original position.

Choose an original terminal vertex as root. It is outside \(S\).
For a nonroot vertex the word has the form
\[
 W_v=\left(\prod_{w\in I_v^-}T(W_w)\right)P_v
                    \left(\prod_{w\in I_v^+}T(W_w)\right),
 \tag{2}
\]
with its two prescribed ordered child lists. At \(v\in S\),
delete only \(P_v=R^0\). The resulting word is the ordered
product of its \(d_v-1\ge2\) turned children. No child is moved
past another, and none of the remaining powers is collected with
another power.

**Proposition 1.** The resulting marked augmented diagram is a
strict Conway construction. Its auxiliary circles are exactly
the original circles outside \(S\), individually labelled, with
the same carriers, integer coefficients, disk framings and
primitive peripheral curves.

**Proof.** Use the strict type intervals
\[
 L=(0,1/2),\qquad H=(1/2,1),\qquad A=(0,1)
\]
of the [strict Conway geometry paper](../papers/strict-conway-geometry/main.tex).
The physical unturned circle box \(P_v\) has type \(H\), and
its turned elementary box has type \(L\). Half-turns, when needed
to express these boxes in the paper's syntax, are propagated as
actual rotations with their markings carried.

Induct up the rooted tree. A selected nonroot vertex has at least
two children. Each turned child has type \(L\) or \(A\):
an unselected child's output has type \(H\), while a selected
child's output has type \(A\). A product of at least two
\(L/A\) inputs has type \(A\), in every retained ordered binary
resolution. Thus the selected output has type \(A\).

An unselected nonroot vertex has exactly one direct circle box
of type \(H\). All its turned children have type \(L/A\).
Inserting one \(H\) into such a stack gives type \(H\), and
there is never an \(HH\) product. The assertion includes an
unselected leaf, whose word is just its own box.
These are precisely the reduced-stack cases proved in
[the ordered normalization paper](../papers/conway-reductions/normalization.tex).

The terminal root closes its type-\(H\) box against its turned
neighbor, of type \(L\) or \(A\). Both closing pairs are strict.
This proves strictness of the particular resulting expression.

Topologically, meridian filling of a zero-carrier crossing circle
restores its original ball with the through tangle and deletes
that auxiliary component. Inserting the through identity in
(2) and then omitting it is a literal tangle identity in that
ball. Every remaining disk and box lies outside that modification
and keeps its position and label. Reassociation, or propagation
of a physical half-turn to write the syntax, carries those disks
and their ordered endpoint markings. It introduces no new
twists, no sum of neighboring exponents, and no change of a
remaining filling slope. QED.

The degree assumption is used at exactly one place: a selected
nonroot vertex must retain at least two children. At degree two,
a zero box instead produces the known merger of neighboring
powers, whose parameter map has infinite fibers. Proposition 1
does not include that move.

## 2. A direct volume theorem

Fix a marked circle-tree template whose retained parity pattern
has one main component and no internal closed component. Select
any original vertices of degree at least three and set their
powers to zero. Their carriers must be zero; keep every other
original carrier unchanged.

**Corollary 2.** There is a finite threshold, depending on the
fixed diagram and the selected set, such that all independently
sufficiently long fixed signed powers at the remaining original
vertices satisfy Kashaev's original volume identity.

**Proof.** Apply Proposition 1. The resulting strict expression
has the same main link and retains each remaining circle with
the original relation (1). Apply the whole-filling theorem in
[Holomorphic source asymptotics and volume limits for strict Conway compositions](../papers/conway-asymptotics/main.tex)
to this expression and these remaining coefficients.
Its signs and magnitudes may be independent. The original
remaining assignment map is the identity on its labels, so no
exceptional reduced parameter acquires an infinite family of
new preimages through this reduction. The theorem gives both
hyperbolicity and the original zero-framed Kashaev volume limit
through all sufficiently large integer levels. QED.

This is an application of an existing theorem in the repository,
not a new asymptotic technique. It includes arbitrarily large
connected groups of zero powers and adjacent trivalent selected
vertices. It does not handle nonzero short powers, or zero
vertices of degree one or two, or imply the general cofinite
assignment theorem.

## 3. The literal reference expression for one selected component

Let \(S\) now be connected, and let \(b\) be its number of boundary
edges. The tree identity gives
\[
 b=\sum_{v\in S}d_v-2(|S|-1)\ge |S|+2\ge3.
 \tag{3}
\]
Every boundary edge has a different outside endpoint.

Cut the original disk-side interfaces at those endpoints. To
describe the selected region independently, put one elementary
crossing-circle box at each boundary end and close the resulting
tree in the original order. Filling the selected zero circles
deletes only their through boxes, as in Section 1. The remaining
diagram has one boundary circle for each boundary edge, unflagged
product junctions at the selected vertices, and one physical
quarter-turn on each intervening edge.

For a precise rooted description choose one boundary box as root.
Every other boundary box enters as a turned elementary leaf.
Every selected vertex contributes at least two incoming factors
of type \(L/A\), so its output has type \(A\).
Closed turn transfer moves the root turn onto its elementary box.
The closing pair is then \(L,A\). The reference expression is
therefore strict, with \(b\) individually labelled boundary
circles. This uses the actual closed turn isotopy of the
[ordered collar proof](../papers/conway-reductions/moves.tex);
all endpoint permutations and physical rotations are retained.

The exact Newton products, reversals and complementary closing
pair of this expression are those in
[the full zero-subtree boundary theorem](research_all_zero_subtree_newton_packet.md).
Its primitive state space is not a replacement graph. It is the
binary resolution of this literal unflagged expression.

The boundary circles of this reference are a way to close the
separate region. When the region is inserted in the original
tree, cut their distinguished disk seams again and glue the
incoming and outgoing interfaces in their original cyclic order.
The resulting annular sectors belong to the original outside
crossing circles. In particular several selected components
meeting one outside vertex do not create several new filling
parameters there.

## 4. The exact boundary polarization identity

Define the classical mixed-leaf potential
\[
 g(a,\chi)=J(2a)-2J(a)-J(a-\chi)-J(a+\chi),
 \qquad
 J(z)=\int_0^z\log(2\sin\pi w)\,dw.
 \tag{4}
\]
All branches start at a strict real \(0<a<1/2\) and
\(\chi=0\). The original Newton boundary phase is
\[
 B(a,u)=\int_0^a
       \log(2\cos2\pi s+2\cos u)\,ds-2J(a).
 \tag{5}
\]

**Lemma 3.** On a complex neighborhood of these points,
\[
 B(a,u)=\operatorname{stat}_{\chi}
                         [g(a,\chi)+i\chi u].
 \tag{6}
\]
There is no additive constant or unit-phase correction.

**Proof.** The stationary equation is
\[
 \log\frac{\sin\pi(a-\chi)}{\sin\pi(a+\chi)}=-iu.
 \tag{7}
\]
Its unique small solution satisfies
\[
 \tan(\pi\chi)=i\tan(\pi a)\tan(u/2).
 \tag{8}
\]
The derivative of its stationary value with respect to \(u\)
is \(i\chi\). Direct integration in (5) gives
\[
 B_u(a,u)=\frac1{2\pi}
       \log\frac{\cos(\pi a+u/2)}{\cos(\pi a-u/2)}.
 \tag{9}
\]
Equation (8) identifies the ratio in (9) with
\(e^{2\pi i\chi}\). Both logarithms vanish at zero, so
\(B_u=i\chi\) as an equality of their continued branches.
At \(u=0\), both sides of (6) equal
\(g(a)=J(2a)-4J(a)\). This fixes the constant for every
nearby \(a\), proving (6). QED.

Let \(\Phi_0(\boldsymbol\chi)\) be the classical potential of
the strict reference expression, obtained by adding its leaf
potentials (4), its original prism potentials, and eliminating
its internal wires. The strict Hessian theorem makes that
elimination nondegenerate. Its color Hessian is
\(-2\pi\operatorname{diag}(\cot\pi a_\ell^*)\).
Applying (6) at all boundary leaves therefore gives exactly
\[
 W_S(\mathbf u)
    =\operatorname{stat}_{\boldsymbol\chi}
          [\Phi_0(\boldsymbol\chi)+i\boldsymbol\chi\cdot\mathbf u],
 \tag{10}
\]
where \(W_S\) is the stationary phase of the original
primitive Newton boundary polynomial. Both eliminations solve
the same nondegenerate equations; no Fourier approximation is
used in this classical identity.

## 5. Matching the entire boundary maps and the peripheral curves

The strict Conway metric theorem constructs the original
reference exterior at completeness and its marked deformation.
Its pure primitive logarithms are
\[
 U_\ell=-2\pi i\chi_\ell,\qquad
 V_\ell=-2(\Phi_0)_{\chi_\ell}.
 \tag{11}
\]
Equation (10) gives
\[
 U_\ell=-2\pi(W_S)_{u_\ell},\qquad V_\ell=2iu_\ell.
 \tag{12}
\]
These are full small logarithms on the original marked
reference curves.

One must also check that cutting and reinserting a reference
piece respects the whole disk-side interface. At a mixed leaf
write
\[
 E=e^{2\pi ia},\quad T=e^{2\pi i\chi},\quad
 Z=\frac{1+E}{1+T},\quad
 R=\frac{T(1+E)^2}{E(1+T)^2}.
\]
The strict geometry uses the same four white transition matrices
and the same pure shaded map as the circle-tree construction.
Its interface parameter is
\[
 Q=\frac{E-Z}{Z-1}=\frac{ET-1}{E-T}
   =\exp(-g_\chi)=e^{iu},
 \tag{13}
\]
where (7) fixes the logarithm. The complete incoming and outgoing
two-triangle interfaces consequently have the original ratio
tables
\[
 (-Q^{-1},-Q,-Q^{-1}),\qquad
 (-Q,-Q^{-1},-Q),
 \tag{14}
\]
on their prescribed ordered edges. These are precisely
\(\texttt{ctg:pants}\) in the
[circle-tree geometry paper](../papers/circle-tree-geometry/main.tex).
A triangle is fixed by its three labelled vertices; the three
complex ratios then fix the other triangle and its full map.
Thus (14) matches translations and shears, not just angles or
peripheral eigenvalues.

The original boundary puncture matching identifies outgoing
and incoming interfaces by inverse ratios. Reattaching the
sectors therefore gives the literal zero-filled parent, with
the same outside disk seams. The local disk longitudes all
become the same original disk longitude at an outside vertex.
Its meridian traverses the incident sectors once in their
original cyclic order. The sector meridian increments in
(12) add; intermediate frame changes cancel, exactly as in
the original collar concatenation. There is no new longitude
multiple and no new meridian winding.

On the auxiliary cusp torus this operation is particularly
explicit. Cut a reference circle's torus along its original
primitive disk longitude. The result is an annulus. Glue the
annuli in the prescribed cyclic order at an original outside
circle, retaining their original oriented longitude directions.
This restores one torus. Its common longitude and the meridian
which crosses the annuli once form the original primitive basis:
their intersection is one, and neither path is traversed more
than once. The construction assembles sectors of one original
circle; it does not identify independently filled tori.

At completeness these interfaces are the original totally
geodesic twice-punctured disk pages. Use the canonical unit
horocyclic segments on each shaded triangle from
[the strict metric completion proof](../papers/strict-conway-geometry/complete.tex).
Every labelled shaded-face isometry, including the possible
odd seam, preserves that decoration. Thus the cusp rectangles
of the cut pieces glue without dilation into the original
compact Euclidean tori. A common shrinking of their
horospheres gives complete horoball ends. The strict reference
pieces and untouched two-octahedron pieces therefore glue to
a complete positive metric on the original parent after its
selected zero fillings. For small \(\mathbf u\), their
positive cell chains and entire maps continue. Main puncture
products stay parabolic, and the full small peripheral
logarithms are the ones just computed.

If several components share an outside vertex, their
parameters in (13) are the same single \(u_v\).
Their phases and meridian increments are added before any
remaining filling is made. With
\[
 P_0(\mathbf u)=
       \sum_{vw\in E_0}\psi(u_v,u_w)
                    +\sum_C W_C(\mathbf u_{\partial C}),
 \tag{15}
\]
the pure periods are \(U_v=-2\pi(P_0)_{u_v}\),
\(V_v=2iu_v\).

For an original retained carrier \(\eta_v\), its one
distinguished disk seam contributes the original correction.
The strict geometry's shear, followed by (10), changes the
longitude-polarized action by
\[
 P_\eta=P_0+\frac{i}{4\pi}\sum_v\eta_vu_v^2.
 \tag{16}
\]
This can also be checked directly from
\(f_\eta=g-\eta g_\chi^2/(4\pi i)\) and its sheared meridian
coordinate. It is applied once per original outside circle,
not once per incident component. Thus the actual periods are
\[
 U_v=-2\pi(P_0)_{u_v}-i\eta_vu_v,\qquad V_v=2iu_v.
 \tag{17}
\]
For the original integer coefficient \(p_v\), (1) now gives
\[
 U_v+p_vV_v
  =-2\pi\left((P_0)_{u_v}+\frac{in_v}{2\pi}u_v\right).
 \tag{18}
\]
These are exactly the primitive equations of the original
remaining trace phases.

## 6. Absolute volume and the use of the boundary theorem

For each strict reference piece, the complete metric theorem
gives volume \(2\pi\Phi_0(0)=2\pi W_S(0)\). Cutting its
distinguished disk pages and gluing them back to the other
pieces changes no volume. Each untouched tree edge contributes
two regular ideal octahedra. Consequently the complete
zero-filled parent has
\[
                 \operatorname{Vol}(Y')=2\pi P_0(0).
 \tag{19}
\]
This is also the same marked parent identified directly in
Proposition 1. Equation (19) supplies an absolute anchor for
the subsequent small primitive filling deformation; (18)
supplies its original slopes.

The source theorem provides the full holomorphic boundary
expansion with phase \(W_S\), a nonzero amplitude and global
boundary estimates. From (10),
\[
 (W_S)_{u_\ell u_j}(0)
   =-\frac{\tan(\pi a_\ell^*)}{2\pi}\delta_{\ell j}<0
                       \quad(\ell=j).
 \tag{20}
\]
Different components' contributions add at shared free
vertices. Therefore these components can also be used as
inputs to the general long-filling assembly, alongside other
already established boundary pieces. This interface statement
is stronger than the direct application in Corollary 2.

For a regular imaginary-height minimizer it agrees with
[the explicit cone geometry](research_regular_zero_subtree_geometry.md).
For a folded edge, the strict Conway cells supply the
different positive decomposition of the same literal
zero-filled parent. No extension through a degenerate
eight-tetrahedron chart is being assumed.
