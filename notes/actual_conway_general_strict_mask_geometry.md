# Actual complete geometry for all strict Conway source trees

31 October 2026. complete-geometry theorem. This note
extends the original ideal-cell construction to every literal
\(h/T/\mathrm{product}\) expression with a strict reduced cylindrical
state. Four individual edge masks replace the insufficient
pair-symmetric port pattern. The proof retains the actual colored
boundary, terminal identifications, reversible link cut and cusp cycles.

The conclusion concerns the complete augmented-link complement and its
original positive source. It is not a signed-source or long-filling
theorem for the enlarged syntax.

## 1. Statement and the strengthened induction invariant

Let \(F,G\) be arbitrary finite expressions in the original leaf \(h\),
literal ordered turn \(T\), and ordered product. Require the original
reduced wire polytope of \(C(FG)\), after deleting only its forced final
gate, to have a strict state: all leaf labels belong to \((0,1/2)\), and
every retained product obeys
\[
\max(x,y)<z<x+y<1.
\tag{1}
\]
The [exact strict-output compiler](actual_conway_single_leaf_source_composition.md),
§2, assigns each open expression one of the types
\[
L=(0,1/2),\qquad H=(1/2,1),\qquad A=(0,1),\qquad\varnothing.
\]
Here \(h\) has type \(L\); \(T\) exchanges \(L,H\) and fixes \(A\);
the product table is
\[
LL,LA,AA\longmapsto A,\qquad
HL,HA\longmapsto H,\qquad HH\longmapsto\varnothing,
\tag{2}
\]
with reversed input orders included. An empty type remains empty.
Every stated interval is actually attained. Thus the strict cylindrical
root pairs are \(AA,AL,AH,LH\), in either order; \(LL\) and \(HH\) fail.
The two children need not belong to the earlier completed grammar.

**Theorem.** The unique complete positive optimizer builds an actual
convex ideal right-angled polyhedron with the original colored bowtie
ribbon boundary. Its two projection copies, with the original labeled
face pairings, give the actual complete finite-volume augmented-link
complement. All auxiliary components are retained, and the volume is
twice the sum of the retained source-cell volumes.

The open-cell induction keeps more than its angles:

1. An actual three-dimensional convex ideal polyhedron has a supported,
   nondegenerate quadrilateral output \(Q=(C_0,C_1,C_2,C_3)\).
2. Each original leaf retains its two distinct shaded ideal triangles.
   Its apex and four corners remain distinct; those two triangles meet
   only at their original apex.
3. Every nonport edge is right angled and separates WHITE from SHADED.
   Each port edge has one adjacent nonport face, recorded individually.
4. Each port corner is an active original terminal singleton. A consumed
   terminal pair and an auxiliary apex never occur on a later port.
5. Each active corner carries one original shaded sector; an internal
   main vertex carries the two sectors of its paired terminals in their
   original ribbon order.

These statements, including vertex identifications and cyclic orders,
are proved below.

## 2. Exact type data, stationary cells and individual edge masks

The strict-state construction and original nonvertex-flat boundary
barrier apply on each actual open type interval. The retained angle
maps recover all wires, so the optimizer is unique and strict with
negative definite reduced Hessian. Its profile \(f_E(b)\) is analytic
there. The [original derivative identities](actual_conway_strict_leaf_quarter_bound.md)
give the entire ordered-face isometry condition
\[
\kappa_{\mathrm{child}}\kappa_{\mathrm{prism\ input}}=1.
\]
They are used on the actual source-selected branch.

For clarity, the exact port and profile information extends to all
nonempty types. Put
\[
B=\cot(\pi b),\qquad \kappa=e^{-f_E'(b)},\qquad
X^2=\frac{1+B^2}{1+\kappa},\qquad Y^2=\kappa X^2,
\qquad X,Y>0.
\]
Then \(X^2+Y^2-B^2=1\), a turn sends \((B,X,Y)\) to
\((-B,Y,X)\), and strict stationary products have common \(X\) with
\[
B_{\mathrm{out}}=\frac{B_FB_G+X^2-1}{B_F+B_G},
\qquad
Y_{\mathrm{out}}=\frac{Y_FY_G}{B_F+B_G},
\qquad B_F+B_G>0.
\tag{3}
\]
Induction proves
\[
\begin{array}{c|c}
L&(B,X,Y)=(B,B,1),\quad B>0\\
H&(B,X,Y)=(-Y,1,Y),\quad Y>0\\
A&-Y<B<X.
\end{array}
\tag{4}
\]
The leaf and turn cases are immediate. The \(LL,LA,AA\) cases are the
same exact port preservation calculations as in the
[single-leaf geometry theorem](actual_conway_single_leaf_geometric_composition.md),
§2. In an \(HA\) product common \(X=1\), and the \(A\) input has
\(B_A>0\), \(Y_A=B_A\). Writing the \(H\) input as \((-u,1,u)\),
strict support gives \(B_A-u>0\), and (3) yields
\[
B_{\mathrm{out}}=-\frac{uB_A}{B_A-u}
 =-Y_{\mathrm{out}}.
\]
For \(HL\), the \(L\) input at \(X=1\) is \((1,1,1)\), giving the
same calculation. This proves every case of (4).

Since the leaf derivative is \(g'(b)=2\log\cot(\pi b)\), (4) also gives
absolute constants \(c_E\) with
\[
f_E(b)=g(b)+c_E\quad(E:L),\qquad
f_E(b)=g(1-b)+c_E\quad(E:H).
\tag{5}
\]
These are optimized classical profile identities on the whole connected
strict interval, extending continuously to its feasible endpoints.
They are not finite quantum scalar factorizations or tangle isotopies.
No such factorization is used here.

The geometric pattern requires finer data than (4). Number the output
edges \(j=0,1,2,3\) cyclically; edges \(0,2\) are FREE. Let
\(\eta_j=1\) when the adjacent nonport face is SHADED and \(\eta_j=0\)
when it is WHITE. The actual dihedral angles, divided by \(\pi\), are
\[
\theta_j=
\begin{cases}
b-\eta_j/2,&j=0,2,\\
1-b-\eta_j/2,&j=1,3.
\end{cases}
\tag{6}
\]
The mask supports satisfy
\[
L:\ \eta_0=\eta_2=0,\qquad
H:\ \eta_1=\eta_3=0,\qquad
A:\ \eta_j=0\ \text{for all }j.
\tag{7}
\]
Only these support inclusions are asserted: an \(L\) or \(H\) mask can
have one nonzero bit or none.

The bare leaf is the explicit ideal pyramid, with mask \((0,1,0,1)\).
Its four other edges are right, and its shaded triangles are
\((O,C_1,C_2)\) and \((O,C_3,C_0)\). Each output corner carries one
shaded sector. A literal turn rotates the port and mask once and
changes \(b\) to \(1-b\). It changes no face or vertex identification.
It exchanges the \(L/H\) support conditions and preserves the \(A\)
condition.

At a product use the [original ordered prism maps](actual_newton_ideal_prism_and_associativity.md):
\[
\begin{aligned}
F:(C_0,C_1,C_2,C_3)&\longmapsto(v_0,v_1,P,\infty),\\
G:(C_0,C_1,C_2,C_3)&\longmapsto(\infty,P,v_2,v_3).
\end{aligned}
\tag{8}
\]
The prism triangles are WHITE. Write \(p=z-x\), \(q=z-y\),
\(w=1-x-y\). All cells are strictly three-dimensional. The output
mask is exactly
\[
\eta^{\mathrm{out}}
 =(\eta^F_0,\,0,\,\eta^G_2,\,0).
\tag{9}
\]
A child CAP seam has angle \(1-\eta_j/2\). A zero bit gives flat
WHITE/WHITE merging; a nonzero bit gives a right SHADED/WHITE edge.
The shared input edge \(P\infty\) has total angle
\[
w+\left(x-\frac{\eta^F_2}{2}\right)
  +\left(y-\frac{\eta^G_0}{2}\right)
 =1-\frac{\eta^F_2+\eta^G_0}{2}.
\tag{10}
\]
Both bits could be one only for \(HH\), which has no strict state.
Thus this edge is also flat WHITE/WHITE or right SHADED/WHITE.
The output FREE angles are \(p+x-\eta^F_0/2\) and
\(q+y-\eta^G_2/2\); the CAP angles remain \(1-z\).
These are (6) and (9). The type table verifies (7) in every case.

This refinement is necessary. A basic \(H\) lower child and an \(L\)
or \(A\) upper child produce FREE angles \(z-1/2\) and \(z\).
They are unequal; a pair-symmetric \(H\) angle pattern would be false.

All port angles in (6) lie strictly between zero and one on their actual
type intervals. The first attachment is locally convex before the second:
its two FREE seam angles are \(z-\eta^F_0/2\) and
\(1-y-\eta^F_2/2\). A nonzero first bit forces \(x>1/2\), hence
\(z>1/2\); a nonzero second bit forces \(x>1/2\), hence \(y<1/2\).
These angles are positive and at most one. The CAP seams have already
been checked. Equation (10) completes the second-attachment check.

## 3. Convexity, ideal coincidences and all port corners

Position two convex ideal cells on opposite sides of their matching
supported face. In hyperbolic space their intersection is exactly that
face. The finite union is closed, connected and locally convex at every
finite boundary point by the preceding angles. Any two finite points
have a shortest path in the union: a length-bounded minimizing sequence
stays in a compact ambient ball, and constant-speed compactness gives a
limit. Local convexity makes it an ambient geodesic locally, hence the
unique whole geodesic segment. The union is convex. This is the
[original supported-face proof](actual_positive_conway_hyperbolic_volume.md),
applied to the refined angles.

The output remains a genuine supported quadrilateral. Its four edge
angles are strictly positive and nonflat, so no other boundary piece
extends its supporting face through an output edge.

This also excludes accidental ideal coincidences, which an argument
inside hyperbolic space alone would miss. Cells on opposite supporting
sides can have common ideal points only on the ideal circle of the
support plane. A cell has no ideal vertex on that circle other than
its matching quadrilateral's corners: an additional vertex would enlarge
the supporting face past a quadrilateral edge, contradicting its strict
supporting angle. The ideal closure of the quadrilateral itself has
only its four ideal vertices. Therefore only the prescribed face-corner
identifications occur. This applies to the first attachment and to the
second; its remaining input face stays supported and nondegenerate.

Every shaded triangle remains an entire unchanged face. It is never an
attaching port. Its seams are always right, never flat, by the CAP rule
and (9)–(10). Only WHITE pieces merge. No shaded edge is deleted,
subdivided or merged into another shaded face. No leaf apex is ever on
an attaching port, so it stays a separate ideal vertex with its four
original right edges and two shaded sectors.

The output-corner patterns are explicit. At \(C_j\), the adjacent bits
\(\eta_{j-1},\eta_j\) have sum at most one by (7). The two port-edge
angles sum to \(1-(\eta_{j-1}+\eta_j)/2\); every other angle is right.
The Euclidean ideal-link angle sum gives
\[
\begin{array}{c|c|c}
\eta_{j-1}+\eta_j&\text{valence}&\text{cyclic faces}\\
0&4&\mathrm{PORT,WHITE,SHADED,WHITE}\\
1&3&\mathrm{PORT,WHITE,SHADED}
       \ \text{in the recorded cyclic order}.
\end{array}
\tag{11}
\]
Each exposed corner has one original shaded sector. Under (8), an
output corner inherits one child terminal; only the two internal
interface corners combine terminals. A turn rotates their sectors.
This proves the full corner invariant, including the asymmetric cases.

## 4. Exact terminal accounting: no transitive corner collapse

Give each leaf the four original symbols \((i,0),(i,1),(i,2),(i,3)\).
An open expression has exactly four active singleton symbols in its
ordered port. All other terminals are partitioned into disjoint
two-element pairs. A paired symbol is permanently consumed: its vertex
is internal and never appears on a later attaching or output port.
Apices \(O_i\) are separate symbols and never enter this matching.

This holds for a leaf. A turn permutes the active singletons. For a
product of disjoint child trees, (8) consumes exactly
\[
F_2\sim G_1,\qquad F_3\sim G_0,
\]
and leaves \(F_0,F_1,G_2,G_3\) active. It never acts on a previously
consumed pair. Each new pair contains terminals from different child
leaf sets. Thus there are no chains of pair equalities and no classes
with more than two terminals. The six prism vertices implement exactly
these identifications; their fresh names create no additional relation
among old internal vertices. Section 3 excludes extra geometric
identifications.

For \(C(FG)\), either retain these two root interface pairs and close the
remaining four singletons, or delete the forced root prism and use the
entire original closing map
\[
F:C_j\longmapsto G:C_{3-j}.
\tag{12}
\]
This forms all four pairs between the distinct root-child leaf sets.
Both descriptions give the same matching. Every original terminal is
used once in one pair; no pair contains two terminals of one leaf.
Consequently every leaf has four distinct main corner vertices after
closure. Its two original shaded triangles are nondegenerate, distinct,
and meet only at their original apex. This rules out transitive
identification, rather than merely checking each individual gluing.

## 5. The closed sphere and the exact oriented ribbon cut

Root stationarity at complementary labels \(b,1-b\) gives equal ordered
quadrilateral metrics, so (12) is the actual closing isometry. Paired
FREE or CAP angles sum to one minus half their two mask bits.
Two nonzero bits would require \(HH\) on a FREE edge or \(LL\) on a
CAP edge. Neither root pair is strict. All closing seams are therefore
flat WHITE/WHITE or right SHADED/WHITE.

The supported-face argument makes the union an actual convex ideal
polyhedron \(P\). Its boundary is a sphere, every surviving edge is right,
and every such edge belongs to an original shaded triangle. All other
seams merge only white pieces. There is no duplicate shaded edge or
white bigon: distinct shaded faces cannot share an edge because each
such edge has a WHITE side. White faces are actual maximal convex ideal
polygons, with no zero-width or two-edge region.

To identify the original link, use the
[independent literal-wire compiler](actual_conway_bowtie_projection_cut.md).
At leaf \(i\), put shaded triangles
\((O_i,C_{i1},C_{i2})\), \((O_i,C_{i3},C_{i0})\) in the original
oriented chart. At each terminal record the outgoing-next and
incoming-previous shaded neighbors. Product (8) concatenates the two
recorded sectors at each consumed terminal pair; turn rotates the ports;
closure (12) makes the original cylindrical pairs.

These are precisely the metric cell maps and cyclic orders. The refined
masks change which seams remain right edges, without changing terminal
pairings or orientations. Every shaded edge survives and every remaining
seam is WHITE/WHITE flat. The resulting metric boundary is exactly the
original bowtie ribbon graph. All white facial cycles are its complementary
oriented facial walks. One global orientation is retained throughout.

The projection cut is reversible for arbitrary literal syntax here.
Each auxiliary circle remains in its original disjoint leaf box with its
recorded twice-punctured disk. In either projection ball, drilling its
boundary-parallel semicircle and cutting along the same half disk cancel
one handle in that collar. The collars are disjoint. This leaves a ball
with the original ideal main-segment vertices and disk triangles.
Its oriented boundary is the ribbon cellulation just proved.

Match the labeled sphere cellulations and extend over the two balls.
Restoring the original white projection pairings and shaded disk pairings
recovers the actual augmented-link exterior. The construction has degree
one and retains every component. It does not interpret an auxiliary
open quadrilateral port as a physical four-punctured boundary.

## 6. Nondegenerate cusp rectangles and four-step edge cycles

Every ideal vertex of \(P\) has only right incident edges. Its sufficiently
small horosphere section is a finite convex Euclidean polygon with all
angles \(\pi/2\); the angle sum forces four sides. It is a nondegenerate
rectangle. Its supporting faces are distinct and \(P\) has three-dimensional
interior; coincident opposite supporting lines would put \(P\) into a
plane. Every side length is positive. Colors alternate WHITE and SHADED.

Take two oppositely oriented projection copies. A white pairing matches
identically labeled faces across copies. The shaded pair for leaf \(i\)
is glued within each copy by the original rule fixing \(O_i\), mapping
\(C_{i1}\) to \(C_{i0}\), and \(C_{i2}\) to \(C_{i3}\).
These ideal-triangle maps are isometries.

For an edge \(e\) of one shaded triangle, its partner \(e'\) belongs to
the other shaded triangle of the same leaf. They are distinct: those
triangles share only the apex, not an edge. The complete edge cycle has
the four occurrences
\[
e^{(0)},\quad e'^{(0)},\quad e'^{(1)},\quad e^{(1)}
\tag{13}
\]
up to cyclic order. There is no shorter self-gluing return. The shaded
maps are inverse labeled triangle maps, and white maps are the identity
between labeled copies. The cycle returns pointwise on its edge,
with total angle \(2\pi\) and no residual longitudinal translation.

At each ideal vertex, scale its horosphere so the two equal positive
SHADED side lengths are one. Each shaded triangle now has its canonical
three corner segments of length one. All shaded maps preserve these
horospheres; white pairings join identical decorations. Shrink them
uniformly to disjoint cusp neighborhoods. Their rectangles glue without
dilation into compact nonsingular Euclidean surfaces, identified by the
actual link cut as the original cusp tori. The truncated core is compact.
Thus the assembled metric is complete and has finite volume.

Each leaf apex retains its exact local rectangle. The original
[primitive crossing-circle paths](actual_conway_bowtie_projection_cut.md),
§6, therefore remain the actual complete meridian and disk-framed
longitude, with ratio \(2i\cot(\pi a_i)\). This complete marking alone
does not establish a deformed signed-source representation.

## 7. Volume, connected-sum scope and the quantum limitation

Each local cell is attached on the opposite supported side of its face.
The cell adjacency graph is a tree and every cell has positive volume.
With \(\mathcal A_E\) the original dimensionless sum of leaf and
retained gate actions,
\[
\operatorname{Vol}(P)=\pi\max\mathcal A_E,\qquad
\operatorname{Vol}(Y_E^0)=2\pi\max\mathcal A_E.
\tag{14}
\]
The original positive finite source \(Z^0_{E,N}\) has the same rate.
Uniform factorial upper bounds and polynomial state counting give the
upper bound; primitive every-level rounding of the strict optimizer
gives a positive lower term at both parities. Thus
\[
\lim_{N\to\infty}\frac{2\pi}{N}\log Z^0_{E,N}
 =\operatorname{Vol}(Y_E^0).
\tag{15}
\]
All original normal directions and finite source support remain present.

This does not discard the
[cap-connected-sum obstruction](actual_conway_cap_sum_reduction.md).
A cap product \(D(FG)=C(T(FG))\) forces its final product output to zero,
both inputs to zero, and that gate to be flat. Such a diagram has not
been exhibited as a strict root \(C(F'G')\) of the present kind.
The boundary cap reduction retains its two-punctured sum sphere and
gives the sum of piece volumes.

Here the additional information is the explicit complete metric.
A nontrivial sum of already complete cusp pieces would give two
noncommuting longitudes centralizing their common meridian, contrary
to the abelian parabolic centralizer in this metric. Hyperbolicity
has not been inferred merely from positivity of a source rate.
Likewise the rigid \(L/H\) constants in (5) are not interpreted as
finite scalar factors or automatic connected-sum factors.

The theorem above is for the original untwisted complete source.
No extension to arbitrary retained half-twist patterns is claimed by
this note. Their local pairing construction is a separate input.
Nor is a signed packet, global alias bound, or long-filling volume
theorem inferred for the whole enlarged syntax. Strict \(L/H\)
expressions can contain quarter-index leaves; the analytic treatment
of those leaves and the required global source estimates are separate
from this complete geometry.

## Inputs

The proof uses the
[strict-type and rounding theorem](actual_conway_single_leaf_source_composition.md),
the [original stationary ports](actual_conway_strict_leaf_quarter_bound.md),
the [actual ideal prism metrics and ordered maps](actual_newton_ideal_prism_and_associativity.md),
the [supported-face and complete-cusp construction](actual_positive_conway_hyperbolic_volume.md),
and the [independent original bowtie cut](actual_conway_bowtie_projection_cut.md).
Sections 2–6 audit the additional type, mask, ideal-coincidence and
cellulation obligations rather than assuming the older completed-only
scope.
