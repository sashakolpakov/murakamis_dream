# Why the limiting action is the actual knot volume

The volume theorem has two geometric tasks. First, construct the
hyperbolic metric on the complement of the link drawn by the specified
diagram. Second, identify the normalized source action with that metric's
volume. Face labels, orientations and peripheral curves enter both tasks.

Throughout this chapter \(D\) is a fixed diagram. Its **augmented
exterior** \(Y_D\) is obtained by surrounding each recorded twist region
with an auxiliary crossing circle and retaining its specified half twist.
Filling those auxiliary cusps with the recorded integer slopes restores
the signed twist powers and produces the **filled exterior**
\(S^3\setminus K_{\boldsymbol p}\) when the main strands form a knot.
The knot cusp is left unfilled. The complete augmented action is
\[
             \Phi_D=\frac{\operatorname{Vol}(Y_D)}{2\pi}.
\]
A filled quantum asymptotic instead uses the generally smaller value
\(\operatorname{Vol}(S^3\setminus K_{\boldsymbol p})/(2\pi)\).
Here \(N\) denotes the quantum level; all diagram and filling data are
fixed before \(N\) tends to infinity.

For the [strict Conway tree theorem](../../notes/actual_conway_all_strict_tree_long_twist_volume.md),
the geometric construction, nonzero quantum contribution and bound on the
remaining terms are all proved. The planar constructions below also
establish their specified complements and marked deformations. For a
general planar source, proving that the complementary terms are
smaller than the geometric contribution remains a separate estimate. The
[results](results.md) and [frontier](frontier.md) chapters keep those
scopes distinct.

The [first-reading chapter](starting.md) defines the diagram, its
twist boxes and the coefficient extracted from the finite source.
Here the emphasis is on the geometric objects represented by those
variables. A source action is the exponential rate of a specified
coefficient or sum. Calling that action a volume requires both a
geometric realization and its absolute normalization.

## The geometric objects and the required checks

Start with the augmented diagram: each twist region has an auxiliary crossing circle around its two strands. Cutting along the projection sphere and the original crossing disks divides its exterior into pieces with labeled faces. The labels remember exactly how to glue the pieces back. They also remember which curves on each torus end are the original meridian and longitude.

An **ideal vertex** lies at the boundary at infinity of hyperbolic space. A small horosphere about it cuts a Euclidean polygon from each adjacent cell. These polygons are the vertex links. In a complete link complement, the polygons around each end glue to a Euclidean torus. This torus is a cross-section of a **cusp**, the noncompact end of the manifold. Checking only that the dihedral angles sum to \(2\pi\) does not establish cusp completeness; the horospherical polygons must also match with the correct translations.

An **angle structure** assigns positive dihedral angles to the proposed cells while satisfying their internal angle relations and the sum around every glued edge. Its volume is the sum of the cell volumes. The angles still retain the actual incidence equations: two copies of one manifold edge are not independent variables. At an interior maximum, variation in every allowed direction gives the shape-matching equations. The proof must then show that these equations produce the original face pairings and complete ends.

A **developing map** places the lifted cells in hyperbolic space.
Following a based closed path compares its initial and final
placements by an isometry. These isometries form the **holonomy
representation** of the fundamental group. In matrix formulas an
orientation-preserving isometry is represented by a determinant-one
complex \(2\times2\) matrix, up to sign. A **peripheral eigenflag**
is the common invariant line selected for the commuting meridian
and longitude matrices at a torus end. The face maps must transport
that line together with the based paths.

A **marked** construction retains the chosen peripheral curves and their basepaths. This matters after filling. The equation that closes a meridian disk depends on a primitive pair of curves on the torus, not just on an unlabeled complex cusp shape. Replacing a primitive longitude by twice that curve would change the filling problem.

The geometric identification has three parts. The cut identifies the
manifold and its boundary curves. The positive shapes and their return
maps identify a metric on that manifold. Finally, comparison with the
finite source fixes the numerical factor and additive constant in the
action. None of these statements says how much of an oscillating
quantum sum comes from that metric. That last question requires the
nonzero leading term and remainder estimates stated in the analytic
theorems.

## The circle packing for a general planar core

A **simple white triangulation** is a triangulation of the projection
sphere with no loop or repeated edge. Its vertices label white faces of
the cut diagram. The **dual graph** has one vertex for each triangle
and one edge for each shared triangle side. It is cubic because each
triangle has three sides. A **perfect matching** chooses one dual edge
at every dual vertex. Its pairs of triangles become the crossing disks.
The four-sided boundary of a pair records the surrounding strand ends
in cyclic order. This matching and the chosen half twists determine
which main strands join, so the knot condition is a separate component
test.

In these packing formulas, a face label also denotes its **curvature**:
a finite circle of curvature \(a>0\) has radius \(1/a\), and a
marked straight line has curvature zero. Equality of two curvatures
does not identify their circles. For example, in the
[symmetric comparison packing](../figures/symmetric-plat-balance-seed.svg),
\(a_1=b_1\) and \(a_2=b_2\) describe distinct reflected disks.
The labels \(a_3=b_3\) describe the single disk on the symmetry
axis, while \(a_0=b_0\) describe the common upper line. The
face-incidence data, rather than equality of numbers, specify
which labels represent one face.

The [planar decoration theorem](../../notes/actual_balanced_terminal_fan_volume.md)
constructs the geometry of every such labeled simple sphere. Remove
one triangle and prescribe three mutually tangent boundary circles.
Maximize the concave angle function subject to angle sum \(\pi\) in
each triangle and \(2\pi\) at each interior vertex. A finite counting
argument first supplies a strictly positive feasible assignment.
A separate boundary variation compares a putative flat maximizer with
that assignment: the entropy gained at its zero angles excludes a
boundary maximum. Strict concavity then gives one interior maximum,
whose multipliers determine positive circle radii.

Euclidean triangles with side lengths equal to sums of adjacent radii
then develop into one embedded disk. Their angle sums remove interior
holonomy, and the convex triangular boundary gives degree one. This
proves that the circles have precisely the prescribed contacts.
The white-circle planes and the circles through the three contact points
of each triangle bound the required convex ideal right-angled polyhedron.

The angle argument serves a specific purpose. Positive numbers satisfying
the linear angle sums are feasible data for a variational problem;
they do not yet give circles with the required contacts. At its interior
maximum, differentiation supplies the radii, and the development proves
that distant disks do not overlap. This separates existence of an angle
assignment from existence of the prescribed packing. The general
volume-variation method is developed in
[Rivin's work on simplicial surfaces](https://annals.math.princeton.edu/1994/139-3/p02);
the linked simple-sphere proof supplies the boundary counting and
embedding argument for these particular face labels.

A terminal insertion adds the circle in one triangular gap. All old
circles remain fixed. Its three new supporting disks lie inside the old
shaded supporting disk, so the attached octahedron respects every other
face inequality. Repeating the insertion preserves convexity, even when
the original sphere has separating triangles or the tangle connections
have cycles. The two projection copies recover the actual augmented
link, with the original crossing-disk face maps.

For independently sufficiently long fixed fillings, the complete metric
is the starting point for the deformation. At circle \(e\),
let \(\mu_e\) be the disk-framed meridian and \(\lambda_e\) its
complementary primitive longitude. The logarithms \(U_e,V_e\) are
logarithms of their projective similarity multipliers, with the branches
continued from the complete structure. They are twice logarithms of
the corresponding determinant-one eigenvalues. The selected
peripheral logarithms satisfy the primitive equation
\(U_e+p_eV_e=-2\pi i\). The logarithmic cusp development has angular
period \(2\pi\), so its metric completion is a smooth solid torus on
that slope. The main meridian and longitude remain parabolic and the
knot cusp is complete. Thus the final volume is that of the knot
complement; it is generally smaller than the augmented volume.

The logarithmic equation is stronger than its exponential. An equation
\(e^{U_e+p_eV_e}=1\) alone would allow an unnoticed integer multiple of
\(2\pi i\), or a nontrivial parabolic matrix with eigenvalue one.
The [Morse completion proof](../../notes/actual_morse_geometric_contribution.md#7-completing-the-specified-hyperbolic-filling)
follows the actual developed generator paths. At the selected
long-filling point the auxiliary longitude has a multiplier of
nonunit modulus. Its two fixed points give a logarithmic coordinate
on the cusp cover; the original periods in that coordinate make the
filling slope one full angular turn with zero axial displacement.
Adding the core then gives a smooth solid torus. The same boundary
triangulation compares the regulator with the volume of this metric.


## Filling conditions checked at individual circles

For the ordered tree with one crossing circle at every vertex,
let \(d_v\) count the incident octahedral pieces in one projection
half and let \(n_v\) be the signed crossing power. The
[geometric criterion](../../notes/actual_all_circle_vertexwise_geometry.md)
\[
                        \sqrt{d_v^2+n_v^2}\ge630
\]
at each vertex constructs a positive deformation through the full
filling path. The contraction bound is independent of the number
of vertices. The original primitive filling curve has logarithmic
period \(-2\pi i c\), for \(0\le c\le1\). At \(c=1\) it makes
exactly one full turn, and the endpoint is the smooth metric on
the original knot complement. The main knot cusp remains complete.

Write \(\alpha_v\) for the cone angle around an added core and
\(\ell_v\) for its geodesic length. Along the positive deformation,
the Schläfli formula is
\[
                 d\operatorname{Vol}
                    =-\frac12\sum_v\ell_v\,d\alpha_v .
\]
Thus increasing the cone angles decreases the volume. In the path
above, \(\alpha_v=2\pi c\). This is the cone-manifold volume formula
used, for example, by
[Hodgson and Kerckhoff, equation (23)](https://arxiv.org/pdf/math/0204345).
Here existence of the entire path comes from the explicit cell
construction and its stated bound. Its volume constant is fixed
at the complete augmented exterior, which
has two regular ideal octahedra per tree edge. This proves that
the continued action is the actual hyperbolic volume. To obtain
a quantum volume equality one also needs the finite-sum estimate;
the [directed subtree theorem](../../notes/actual_all_circle_directed_volume.md)
supplies it under its stronger finite numerical test. In particular,
it suffices that every vertex independently satisfy
\(|n_v|\ge2^{27}\) or \(d_v\ge2^{28}\), with the original knot
pairing. This proves the actual complement-volume equality.
The summed criterion remains a useful alternative. The geometric
bound \(630\) alone is not a quantum estimate.

## The geometric proof for the explicit degree-and-twist bound

The [quantitative theorem](../../notes/actual_all_circle_quantitative_volume.md)
uses a particularly simple decomposition of the actual exterior.
Each vertex of its ordered tree is a crossing circle, and each tree
edge supplies one octahedron in each projection half. Inserting a
terminal child attaches an octahedron along a shaded crossing-disk
triangle. Reading the four strand joins shows that its other three
shaded faces are exactly the new disk faces. The adjacent white
projection faces join in their original order.

![One octahedron is attached along the shaded triangle of a projection half. Equal labels are identified with opposite boundary orientations. The two vertices O_v and O_w belong to the parent and child crossing circles; A, B, C and D are main-strand ends.](../figures/octahedral-page-attachment.svg)

There are \(E\) octahedra in each half for a tree with \(E\) edges.
The [ordered decomposition proof](../../notes/actual_all_circle_octahedral_decomposition.md)
retains the left and right insertion order, the actual rotations of
child balls, and the single original half twist at each circle. These
data determine the original manifold and its primitive cusp curves.

The [angular formulas](../../notes/actual_all_circle_angular_octahedra.md)
subdivide the pair of octahedra into eight ideal tetrahedra. All shapes
are \(i\) at the complete point and remain positively oriented for
\(|\tau_v|<10^{-2}\). The numerical bound of the theorem puts the
entire path of filling equations inside this chart. Along the path,
the actual primitive slope has logarithmic period \(-2\pi i c\),
with \(0\le c\le1\). Its angular period is therefore \(2\pi c\).

The [completion argument](../../notes/actual_all_circle_geometric_completion.md)
proves that each auxiliary end is a punctured metric tube with these
periods. At \(c=1\), its core is smooth. Attaching these cores performs
the original surgeries, while the main cusp remains complete. The
boundary correction to the complex action cancels the filling term;
the resulting real value is the volume of this knot complement.
The constant is fixed by the complete augmented link, whose volume
is \(2E\,v_8\), where \(v_8\) is the volume of a regular ideal
octahedron.

This argument allows the full meridian logarithm to accumulate one
turn even when each angular variable is small. It is the step needed
for the short powers permitted by the criterion. The
[main-cusp continuation](../../notes/actual_all_circle_preferred_cusp.md)
then compares the marked representations and follows the preferred
longitude to the smooth endpoint.

## The strict-tree construction

The [net-twist reduction](../../notes/actual_conway_net_twist_volume.md) extends the use of this construction. It combines specified twist boxes by actual isotopies, retaining any half-turn of an intervening tangle. When its output is a strict presentation with sufficiently large combined twists, the geometric theorem below gives the output knot exterior its complete metric. The isotopy identifies that exterior with the input knot exterior, so the metric and its volume transfer directly. This comparison is made after the twists are inserted; it does not identify the auxiliary crossing-circle cusps of two different augmented presentations.

A Conway expression is a recorded sequence of two operations on tangles: stack two boxes, or turn one box through a quarter-turn. Its leaves are the original twist regions. The finite strictness test in the theorem is a compatibility test for the positive angles of these operations. It is not a claim that any written tangle expression becomes hyperbolic when its displayed exponents are large.

The geometric pieces follow these operations. Each leaf contributes an ideal quadrangular pyramid, and each retained product contributes an ideal triangular prism. Their volumes agree with the local terms of the complete quantum action. Each quadrilateral gluing face has four ordered ideal vertices. The order specifies which vertex is identified with which when two cells are attached; it is part of the geometry, not just a label for a boundary variable. The metrics of these faces are determined by derivatives of the action. When the full action is stationary under the shared-index constraints, those metrics agree across the actual ordered product faces.

The [general strict-mask geometry theorem](../../notes/actual_conway_general_strict_mask_geometry.md) proves that these pieces assemble with the original cyclic orders. Its *mask* is a four-entry list attached to an ordered quadrilateral: an entry is one when the neighboring face is a shaded crossing-disk face and zero when it is a white projection face. A quarter-turn rotates that list along with the four corners. These entries determine which seams become flat and which remain right-angled after gluing. The proof rules out vertex identifications that would collapse a shaded triangle, checks the edge cycles, and constructs positive rectangular cusp links.

The final identification with the diagram uses the [literal bowtie cut](../../notes/actual_conway_bowtie_projection_cut.md). A bowtie is the pair of triangular faces exposed by one crossing disk. Its four outer corners are joined by the actual main strands of the diagram. Reading those joins in their projection order determines every remaining face. Reversing the cut therefore recovers the original link exterior with its original auxiliary circles. Matching a count of vertices or a total volume would not suffice.

The [marked deformation theorem for the full strict class](../../notes/actual_conway_general_mask_marked_filling.md) extends the complete construction to nearby complex auxiliary colors. Its face maps satisfy the original group relations, including their translational parts. Every main cusp remains parabolic. On an auxiliary cusp it supplies specified logarithms \(U_i,V_i\) of the peripheral multipliers. Here a logarithm includes its chosen branch, so it records a winding that a bare eigenvalue would forget.

Write the actual twist weight as \(n_i=\epsilon_i-2p_i\), with \(\epsilon_i\in\{0,\pm1\}\) recording a retained half twist. The filling equation uses the primitive basis of this actual half-twisted link. For every fixed choice of sufficiently large independent signed \(p_i\), the nearby solution gives a smooth filling of the auxiliary cusp. The main knot cusp is never filled. The action, with its boundary correction, equals the volume of that resulting knot complement. The quantum theorem uses exactly this solution and normalization.

The peripheral deformation viewpoint has its classical foundation in
[Neumann and Zagier, *Volumes of hyperbolic three-manifolds*](https://archive.mpim-bonn.mpg.de/id/eprint/1122/).
The diagram-specific work here determines the primitive words,
the factor of two between multipliers and eigenvalues, and the absolute
constant of the source action. Those choices are retained when applying
the filling equations.

The next sections give further details and explain the older constructions that supplied parts of this argument.

## The full geometric longitude for strict trees

A cusp-shape calculation determines the tangent of a peripheral
curve, but the [strict-tree longitude theorem](../../notes/actual_strict_tree_geometric_characteristic.md)
identifies the entire nearby curve for every covered strict
long-filling construction. A meridian goes once around the
knot. Its preferred longitude follows the knot once with zero
linking number. Choose a local lift of the holonomy to determinant-one matrices.
Let \(M\) be the meridian eigenvalue and \(L\) the preferred-longitude
eigenvalue on the same selected line. The complete lift used here has
\((M,L)=(1,-1)\). These are eigenvalues, unlike the projective
multipliers \(e^{U_e},e^{V_e}\) used at the auxiliary cusps.

Write \(\mathcal E_T\) for the original physical quarter-turn
edges in the tangle expression. If the summation index on such
an edge is \(r_e\), its normalized limit is \(x_e=r_e/N\).
The functions \(x_e(M)\) are the stationary values continued from
the selected filled structure as the main meridian varies.
With \(X_e=e^{2\pi ix_e}\), the formula is
\[
 L(M)=-M^{-w(D)-\sum_i n_i}
       \prod_{e\in\mathcal E_T}
       \frac{M^2-X_e(M)}{1-M^2X_e(M)}.
\]
Here \(w(D)\) is the oriented writhe and \(n_i\) are the
original signed crossing powers. The filling path fixes the
logarithms and selects the branch; algebraic elimination
without that marking would retain other representations.

The preferred longitude changes under auxiliary surgery even though the
main torus is not filled. If \(\lambda_{\mathrm{aug}}\) denotes the
image of the augmented longitude on the filled main torus, then
\[
 \lambda_{\mathrm{fill}}
   =\lambda_{\mathrm{aug}}+
        \left(\sum_e p_e\,\operatorname{lk}(K,C_e)^2\right)\mu_K
\]
in its peripheral homology, with the disk-framed signs of the theorem.
This integral change of basis is one source of the framing exponent
in the formula for \(L(M)\).

![The two parallelograms use the same filled main-cusp lattice. The image of the augmented longitude is replaced by the preferred filled longitude after adding four meridians in the illustrated linking-two surgery.](../figures/main-cusp-longitude-shear.svg)


The extension to a junction without a crossing circle uses
a literal identity box \(R^0\). Add a crossing circle around
its two straight strands and fill the new circle's meridian.
This returns the original tangle. The proof fixes a product
collar, a basepoint and access paths before taking any
representation, so both based puncture loops are preserved
in order. It then compares the full boundary tuples of
matrices. Agreement of one scalar trace would not suffice.

![Meridian filling removes an added circle around a zero-crossing box while preserving the ordered based strand meridians.](../figures/zero-circle-junction.svg)

At a bare product junction the new angular variable has a
nondegenerate stationary point. Eliminating it returns the
original product action and its Hessian. The full system
remains regular when a physical edge has index one half;
the proof does not assume that a folded quadratic equation
has a simple root. The resulting representation factors
through the original filled knot group and agrees with its
marked geometric deformation.

Combining this identification with the full filtered expansion
gives the selected geometric factor of each genuine all-level
annihilator for the covered strict long fillings. Here an
annihilator is a nonzero fixed finite difference operator that
annihilates the whole meridian invariant at every sufficiently
large level; its shift sends \(M\) to \(q_NM\), where
\(q_N=e^{\pi i/N}\).
The corresponding circle-tree result holds under the summed,
local and [directed all-orders hypotheses](../../notes/actual_all_circle_directed_all_orders.md).
Its conclusion identifies the factor belonging to the geometric
meridian–longitude branch. Equality of the full A-polynomial
or of recurrence ideals is a stronger statement.
Marked ambient isotopy carries the intrinsic curve and factor
to the covered net-twist and arbitrary-closure inputs, even
when their auxiliary augmented links differ.

## How the cells and the diagram are identified

The [global Conway geometry theorem](../../notes/actual_positive_conway_hyperbolic_volume.md) supplies the face pairings for every cylindrical factor in its original positive construction. Cylindrical closure joins each lower external strand to the corresponding upper strand. The later strict-mask theorem extends this construction as described above.

The local actions can be written explicitly. Put
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad 0\le t\le1.
\]
For a leaf with normalized index \(0<x<1/2\), set
\[
 g(x)=-2J(x)-2J(1/2-x).
\]
Its ideal quadrangular pyramid has volume \(\pi g(x)\).
For a product with two input indices \(x,y\) and output index \(z\),
the strict domain is
\(\max(x,y)<z<x+y<1\), and its action is
\[
\begin{aligned}
 m(x,y,z)={}&J(x+y)+J(z)-J(x)-J(y)\\
            &-J(z-x)-J(z-y)-J(x+y-z).
\end{aligned}
\]
The multiplication prism has volume \(\pi m(x,y,z)\).
These are the local terms of the original coefficient asymptotic.
The [cell construction](../../notes/actual_newton_ideal_prism_and_associativity.md)
gives the ordered ideal vertices and verifies these volume formulas.
These cells occur in a single projection half. The complete exterior
uses its two specified copies, which accounts for the factor
\(2\pi\) in the normalized complete action \(\Phi_D\).

![An ideal hyperbolic leaf pyramid and multiplication prism. Each blue quadrilateral has the displayed ordered ideal vertices; the two shaded triangles of the leaf retain the crossing-disk pairing. The formulas above give their volumes.](../figures/conway-cells.svg)

For four ideal vertices \(a,b,c,d\) in cyclic order on a circle,
the positive real cross ratio
\[
 \kappa(a,b,c,d)=\frac{(a-b)(c-d)}{(a-d)(b-c)}
\]
determines the ideal quadrilateral up to isometry; use the limiting
formula if a vertex is infinity. A one-step cyclic change of order
replaces \(\kappa\) by its reciprocal. The leaf output satisfies
\(\log\kappa=-g'(x)\), and the three prism faces satisfy
\(\log\kappa(F_x)=-\partial_xm\),
\(\log\kappa(F_y)=-\partial_ym\) and
\(\log\kappa(F_z)=-\partial_zm\).
At a shared variable, stationarity makes the child and parent
derivatives sum to zero. The prescribed stacking map reverses the
corresponding face order, so its isometry condition is precisely
\(\kappa_{\mathrm{child}}\kappa_{\mathrm{parent}}=1\).

Stationarity makes the shared quadrilateral gluing faces isometric under the literal stack maps. A boundary barrier proves that every unforced cell at the maximum is strict. The cells assemble into a convex ideal polyhedron; the actual cylindrical closure leaves only right-angled boundary edges. Reversing the projection and crossing-disk cuts reconstructs the original link. Four-step edge cycles give angle $2\pi$ with identity return, and matched rectangular horosphere links prove cusp completeness. Thus the two-copy volume is the volume of the actual complement.

The [closed bowtie-cut proof](../../notes/actual_conway_bowtie_projection_cut.md) identifies every oriented white and shaded face from the original wires. The reconstruction uses the entire labeled ribbon graph and reversible disk cut. In particular, one open quadrilateral face does not determine the four-punctured boundary of a physical tangle: the other faces and strand joins are also retained. At a leaf crossing circle, the proof gives the primitive cusp shape \(2i\cot(\pi x_i)\), where \(x_i\) is that leaf's complete stationary index.

The final product gate is forced flat and is removed from the geometric cell list using its exact unit source coefficient. This does not delete a quantum contribution or a link component. The [local cell proof](../../notes/actual_newton_ideal_prism_and_associativity.md) also identifies source associativity with two triangulations of one actual ideal cube.

A cap closure joins the two upper endpoints to one another and the two lower endpoints to one another. The [cap-sum reduction](../../notes/actual_conway_cap_sum_reduction.md) exhibits a two-punctured separating sphere that splits a cap-closed product into componentwise connected sums. The quantum source factors and the angle polytope splits with it. In its explicit family of \(k\) theta-link summands, the source \(Z_N\) satisfies
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log Z_N=4k\,v_8.
\]
For \(k\ge2\), this is the sum of the volumes of the hyperbolic
summands; the whole complement has no complete finite-volume
hyperbolic metric. A positive logarithmic growth rate alone
therefore does not establish a knot-complement volume theorem.

## Algebraic shapes and their volume regulator

The [algebraic optimizer theorem](../../notes/positive_source_algebraic_volume_period.md) applies to every rational affine ideal-angle problem with positive rational weights. On the smallest face containing the maxima, flat atoms contribute zero. The remaining Hessian is definite after quotienting by the rational directions that leave all nonflat angles unchanged. Exponentiated stationarity then proves that the nonflat shapes are algebraic, including boundary and nonunique maxima.

The Bloch group packages algebraic tetrahedron shapes together with the relations obtained by changing a triangulation. Its regulator evaluates those shape symbols by the oriented dilogarithm volume. For a shape \(z\notin\{0,1\}\), the
Bloch–Wigner dilogarithm gives the signed volume of the corresponding
ideal tetrahedron. A sum of shape symbols records the tetrahedra with
their orientations; the gluing relations remove its boundary.
[Neumann's extended Bloch-group construction](https://arxiv.org/abs/math/0307092)
also records logarithmic choices needed for the complex
Cheeger–Chern–Simons invariant. Here the real volume regulator is
calibrated on the specified geometric fundamental chain. A
**fundamental chain** is an oriented sum of tetrahedra representing
the manifold once; internal faces cancel under the prescribed gluings.
It records more than an equality between numerical dilogarithm sums.
The [Bloch regulator calculation](../../notes/actual_positive_source_bloch_regulator.md)
proves that the conjugate-antisymmetrized shape sum is a rational
Bloch class with regulator equal to the source maximum. For the
retained cylindrical factors, the cell realization identifies that
class with the chain of the complement. The comparison is made in
a common finite number field containing the source shapes, their
conjugates, and all glued ideal vertices. The mirror orientations
give the symbols \([z]-[\overline z]\); this common field is not
asserted to be the geometric trace field.

For a fixed positive Conway expression \(E\) in that earlier seed-generated grammar, let \(Z_{E,N}\) be its complete quantum sum. Its statement is

$$\lim_{N\to\infty}\frac{2\pi}{N}\log Z_{E,N}
=R_{F_E}(B_E),\qquad B_E=\sum_j([z_j]-[\overline{z_j}])\in B(F_E)_{\mathbb Q}.$$

Here \(z_j\) are the algebraic shapes, \(F_E=\mathbb Q(z_j,\overline{z_j})\) is the number field containing them and their conjugates, \(B(F_E)_{\mathbb Q}\) is the rational Bloch group, and \(R_{F_E}\) is its volume regulator at the specified complex embedding. For a retained cylindrical factor its value is now proved to be the actual complement volume. This regulator argument alone does not identify a generic main-meridian characteristic factor or prove arbitrary short-filling limits. The separate strict-tree longitude theorem above now identifies the selected factor for the covered long-filled knots. Actual all-level quantum A-operators exist by the finite cut-state proof, and the pointed operator-period theorem gives the same volume limit for those knots.

Fixing an output index of an open tangle changes the maximization problem. The resulting function of the scaled output \(b\) is its boundary profile. The [boundary profile theorem](../../notes/actual_conway_boundary_volume_relation.md) also gives a full limit for every coefficient approaching any output $b\in[0,1]$. On $(0,1)$ its optimizer is unique and analytic, and its boundary conjugate is the actual quadrilateral modulus $\exp(-v'_E(b)/\pi)$. This is a geometric meaning for the source boundary relation; the variable is not yet the knot's peripheral holonomy.

## The deformed source has actual peripheral holonomy

In the earlier positive grammar, the [marked deformation theorem](../../notes/actual_conway_marked_peripheral_deformation.md) constructs a representation of the actual link group for the auxiliary-color critical branch. Exact Möbius identities establish every white seam and shaded edge relation, including translations. All main cusps stay parabolic. Let \(\chi_i\) be the scaled auxiliary-color deficit, and let \(\phi(\chi)\) be the selected limiting action. For each auxiliary circle the primitive logarithms are

$$U_i=-2\pi i\chi_i,\qquad V_i=-2\partial_i\phi(\chi).$$

The function \(G=2\pi i\phi\), called a primitive because its derivative is the displayed peripheral one-form, satisfies $dG=\tfrac12\sum_i V_i\,dU_i$, with its constant fixed by the complete fundamental-chain volume. Exponentiated source stationarity gives an algebraic marked peripheral branch; the selected branch is locally a Lagrangian graph: the exterior derivative of that peripheral one-form vanishes on it. This statement concerns the auxiliary peripheral coordinates, with the main cusps held parabolic. The displayed peripheral multipliers are squared SL eigenvalues, and no entire A-polynomial is inferred merely by elimination.

At the original filling saddle, $U_i+p_iV_i=-2\pi i$ holds in the primitive disk marking. The actual nearby representation and the boundary-corrected regulator then identify the full quantum rate with the volume of the correctly filled complement. This applies to every retained robust factor and independently sufficiently long fixed signed integral fillings of any selected auxiliary circles. The component theorem keeps its link-only scope explicit.

## Half twists preserve the marked action through a shear

The [odd-coupon deformation](../../notes/actual_odd_conway_marked_peripheral_deformation.md) changes the shaded face pairings and checks their edge words at general complex parameters. The original odd-link peripheral paths give

$$U_i^\epsilon=U_i^0-\frac{\epsilon_i}{2}V_i^0,\qquad V_i^\epsilon=V_i^0,\qquad G_\epsilon=G_0-\sum_i\frac{\epsilon_i}{8}(V_i^0)^2.$$

These are also the exact derivatives and quadratic correction of the selected finite-source action. Write $M_i=e^{U_i}$ and $L_i=e^{V_i}$ for these auxiliary peripheral multipliers. On the marked double cover $\ell_i^2=L_i$, the half-longitude change becomes the integral monomial map $M_i^\epsilon=M_i^0\ell_i^{-\epsilon_i}$. The source selects the square root and its logarithm. The square root is part of the marked data. Changing it changes the logarithmic branch, so it cannot be discarded when comparing the source and the filling equation. The two possible square roots form a two-point
choice over a fixed nonzero \(L_i\); continuing a logarithm also records
integer multiples of \(2\pi i\). The term *torsor* means that a group
acts freely and transitively on such choices, without a distinguished
choice until a reference is fixed. This square-root cover is different
from the continuous freedom to rescale cusp horospheres, and from the
local Casimir transport curve described in the
[operator discussion](frontier.md#direct-twist-transport-and-the-classical-operator-question).

![Left: a primitive filling slope on a schematic cusp torus. Right: local sheets of the peripheral square-root cover, with the selected branch and integral shear.](../figures/peripheral-torsor.png)

The square is a fundamental domain, not a metric cusp shape. Its amber segments form the single primitive curve $\mu+2\lambda$ after opposite sides are identified. The two sheets on the right are a local picture of $\ell^2=L$; the cover is not asserted to split globally. The selected logarithm retains the primitive filling equation $U+pV=-2\pi i$.

Smooth filling uses the primitive basis of the link with its retained half twists. Substituting a half-integer slope into the pure-link formula would double the primitive rotation angle when denominators are cleared. The actual odd-link construction avoids that error, keeps main cusps parabolic, and fixes the regulator at its complete volume. Together with the full changed-source estimates it yields the [general signed Conway knot and link theorem](../../notes/actual_odd_conway_long_filling_volume.md).

## A second route: circle patterns for general augmented plats

For a connected labeled right-angled augmented plat at any fixed bridge width, the [signed complete-source theorem](../../notes/general_signed_augmented_source_volume.md) identifies the original source rate with the actual complete volume. The [fixed complex core theorem](../../notes/actual_complete_core_complex_packet.md) now gives a nonzero analytic asymptotic for its complete-image external-color term. This construction is independent of the strict-tree recursion; the statements below retain their own hypotheses.

A circle pattern represents the labeled boundary faces by circles or lines at infinity, with the prescribed tangencies. A circle bounds a hyperbolic plane in the upper-half-space model. The two white faces adjacent to the reduced mark are represented by parallel lines; their common strip width fixes the scale. The [marked circle-pattern theorem](../../notes/actual_marked_deformed_circle_pattern.md) solves simultaneously for the remaining centers and radii. The positive face Hessian, followed by rigidity of the triangles of centers, makes the Jacobian invertible. Thus the nearby pattern has exactly the stationary radii of the source action. The selected boundary eigenlines are continued with this pattern.

![The actual marked lines retain their shared width and the selected eigenlines as matching tangencies deform.](../figures/marked-circle-strip.png)

The **crossing-disk collar** is a small neighborhood of a disk
pierced by two main strands. Cutting it exposes an input shaded
triangle and an output shaded triangle. Let their white-circle
curvatures be \((x,b,y)\) and \((x,c,y)\), respectively.
The two outer circles \(x,y\) are shared. The four contacts are
\[
 C_1=x\cap b,\quad C_2=b\cap y,\qquad
 C_0=x\cap c,\quad C_3=c\cap y.
\]
Each intersection here means the prescribed tangency point.
The original untwisted disk pairs \(C_1\) with \(C_0\) and
\(C_2\) with \(C_3\). Those ordered identifications specify the
side map whose primitive multiplier we need.

For a small real deformation parameter \(\delta>0\), the outer
circles meet at two points \(P_+,P_-\). The coordinate
\[
 w=\frac{z-P_+}{z-P_-}
\]
sends them to straight lines through zero. The circles bounding
the two shaded planes become concentric, with radii
\(\rho_b,\rho_c>0\). Their ordered pairing is
\[
 C(w)=R_0w,\qquad R_0=\rho_c/\rho_b,
\]
\[
 C_1\longmapsto C_0,\qquad C_2\longmapsto C_3.
\]
The radii \(\rho_b,\rho_c\) belong to the transformed shaded
circles; they are different quantities from the original white
radii \(1/b,1/c\).

![The crossing-disk collar in the exact configuration x=y=b=c=1 and delta=1/10. Dashed circles bound the shaded planes and are orthogonal to the white circles on their side. The displayed Möbius coordinate turns the prescribed contact pairing into a dilation.](../figures/deformed-circle-collar.svg)

The [primitive collar theorem](../../notes/actual_deformed_circle_primitive_collar.md)
also follows the based meridian path through this map. The auxiliary
meridian uses \(C^{-1}\), so its pure similarity logarithm is
\(-\operatorname{Log}R_0\). The disk-longitude product selects the
eigenpoint \(P_-\), with determinant-one eigenvalue
\(J=-e^{-2\pi i\delta}\). A retained signed half twist
\(\epsilon\in\{0,\pm1\}\) therefore gives
\[
 U=-\operatorname{Log}R_0+2\pi i\epsilon\delta,\qquad
 V=-4\pi i\delta.
\]
The logarithms vanish at the complete point and are continued on
the prescribed branch. At \(\delta=0\), \(R_0=1\) but the matrix
limit of the side map is a nontrivial parabolic translation in
the original coordinate. The theorem retains that limit and
also treats the zero-curvature marked lines.

The [global geometric assembly](../../notes/actual_complete_core_geometric_deformation.md)
checks these maps against the full link-group relations, including
their translations. It identifies the complete-image core's action
with the marked geometric deformation. For complex peripheral
parameters it retains the boundary correction
\(\tfrac12\sum_i\operatorname{Re}U_i\operatorname{Im}V_i\);
for real external deficits that correction vanishes. The local
calculation and the group assembly establish the geometric
contribution. Bounding the remaining reflected-color terms is
the additional step needed for the full invariant; the
[results](results.md) chapter states the families for which that
step is proved.

An identity smoothing replaces a specified crossing-disk coupon by the identity and retains the remaining face identifications. For such a diagram, the [block capacity theorem](../../notes/actual_smoothed_source_capacity_blocks.md) removes the need to assume an attained positive-radius minimum. Here capacity is the infimum of the positive weighted expression used for a coefficient bound. The theorem splits degenerate angle problems along two-edge cycles and constructs each simple block's actual polyhedron. The [block representation and volume theorem](../../notes/actual_smoothed_block_representation_volume.md) then retains the original face pairings and realizes their volume sum as a regulator of the original group. Its deleted meridians lie in the kernel, so the [strict-kernel theorem](../../notes/general_representation_volume_kernel_strictness.md) proves strict loss for every nonempty connected untwisted smoothing with finite capacity. Loop-infeasible cases already have an arbitrarily low capacity bound.

The chain argument uses a controlled finite degeneration: cut corners have a common horospherical height and mutual distance $O(T^{-1})$. A uniform short-edge tetrahedron estimate makes the added volume vanish. Arbitrary ideal vertices merely approaching one another would not justify this step. The [near-maximal-volume corollary](../../notes/general_representation_volume_peripheral_gap.md) also gives uniform gaps from fixed marked peripheral trace conditions; applying those gaps to the remaining quantum color complement is still a source-estimate problem.

Here **representation volume** means the oriented hyperbolic volume
assigned to a homomorphism from the original manifold group to
\(\mathrm{PSL}_2(\mathbb C)\), using an equivariant map and the
prescribed treatment of its cusp ends. It can be defined when the
homomorphism is not discrete or faithful. At geometric holonomy it
equals the metric volume; maximal-volume rigidity restricts when
equality can occur. See
[Francaviglia's construction for cusped manifolds](https://arxiv.org/abs/math/0305275)
and [Francaviglia–Klaff's volume-rigidity theorem](https://arxiv.org/abs/math/0411050).
To use such a theorem for a source term, the source equations must
first produce a representation of the same group with the same
peripheral words. An absolute-value coefficient envelope has no such
interpretation merely because its variables resemble shapes.

## A local tetrahedron is a genuine geometric result

The [local hyperideal theorem](../../notes/actual_four_port_hyperideal_angle_volume.md)
uses six internal representation labels \(j_e\), one for each edge
of a tetrahedron. The exact half-shifted coordinates are
\[
 a_e=\frac{j_e+1/2}{N},\qquad
 \alpha_e=\pi-2\pi a_e.
\]
In the strict geometric domain, \(0<a_e<1/2\) and the three
\(a_e\)'s at each vertex sum to more than one. Equivalently, the
three positive dihedral angles \(\alpha_e\) there sum to less
than \(\pi\). Such a vertex is **hyperideal**: its polar plane
cuts off the end and leaves a geodesic truncation triangle.

The source in this local statement is a positive Racah scalar
\(W_N\) with its four face-normalization factors retained.
If \(\Psi=\lim N^{-1}\log W_N\), the theorem proves
\[
                  \operatorname{Vol}(\text{tetrahedron})=\pi\Psi.
\]
Squaring \(W_N\) doubles its logarithmic action. The proof constructs
the Gram matrix of outward face normals in Lorentz space,
recovers the edge lengths, checks the volume differential and
fixes the constant at an ideal configuration. Boundary values
are continuous volume extensions.
Here Lorentz space is four-dimensional real space with a bilinear
form of signature \((3,1)\). Its hyperboloid model realizes
hyperbolic three-space, and the Gram matrix records the pairwise
Lorentz inner products of the face normals. This is how the
algebraic matrix determines the cell's metric.

![A truncated tetrahedron in a combinatorial projection. Blue triangles indicate polar truncation faces; the hyperbolic metric comes from the Gram matrix.](../figures/truncated-tetrahedron.png)

This is stronger than observing that a factorial action resembles a dilogarithm. It is also local: a collection of such tetrahedra does not automatically form the knot complement.

## The global angle slice carries the topology

An actual ideal triangulation specifies which faces are glued, which tetrahedron edges belong to each manifold edge, and which peripheral curves represent meridians and longitudes. Its angle constraints must retain this incidence.

At a candidate maximum, stationarity must hold in every allowed angle direction. The corresponding shape and length equations must make adjacent cells agree. The resulting developing map must have the intended winding and end behavior. Complete cusps, or the specified filled peripheral equations, are part of the certificate.

The [source-volume certificate](../../notes/source_volume_casson_rivin_certificate.md) keeps these requirements explicit. An algebraic critical point can be isolated and still belong to the wrong component or have the wrong peripheral marking.

## A general certificate through volume maximization

For an ideal tetrahedron, its three positive
dihedral angles \(\alpha,\beta,\gamma\), one for each pair of
opposite edges, have sum \(\pi\), and its
volume is
\[
 \Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma),\qquad
 \Lambda(t)=-\int_0^t\log|2\sin u|\,du.
\]
An ideal triangulation imposes additional linear sums \(2\pi\) around
the manifold edges. These equations define its angle polytope.
Casson and Rivin's variational method recovers the nonlinear shape
equations by differentiating the sum of these volumes.
[Rivin's 1994 paper](https://annals.math.princeton.edu/1994/139-3/p02)
is a primary source for the volume method; the
[proof by Futer and Guéritaud, Theorem 1.2 and §5](https://arxiv.org/pdf/1004.0440)
explains the completeness implication in terms of angle variations.
Their formulation concerns a fixed ideal triangulation of an
orientable manifold with torus boundary. The maximum on the closed
angle polytope can lie on its boundary; an interior critical point
must therefore be established for the triangulation being used.

For an actual marked ideal triangulation with torus vertex links, the [positive gluing criterion](../../notes/general_marked_positive_gluing_certificate.md) gives a direct proof of the Casson–Rivin equivalence: an interior critical point of the ideal-tetrahedron volume function is exactly a complete positive gluing. Strict concavity makes it the unique maximum, including over the closed angle polytope, and its value is the actual complement volume.

The proof keeps the geometry explicit. Lagrange multipliers prescribe one truncated length for each global edge. These lengths determine compatible corner horospheres; the face maps then match them, giving complete flat cusp tori. Conversely, compatible horospheres make the geometric volume stationary under all allowed angle variations.

There is a finite algebraic certificate using positive upper-half-plane phases and positive multiplier variables. The unique optimum has algebraic shapes. Neither its dilogarithm volume nor the original quantum period is asserted to be an algebraic number. Existence of an interior optimum on a proposed triangulation, and selection of its period by the quantum source, remain distinct questions.

For fixed critical shapes, choosing a horosphere at one cusp and then
rescaling it changes the decoration but leaves the hyperbolic metric
unchanged. With \(c\) cusps these independent choices form a torsor
for \((\mathbb R_{>0})^c\): there is one and only one tuple of scales
taking one decoration to another. This accounts for the decoration freedom in the algebraic certificate. It does not yet determine the quantum period, and extending the action to complex scalars requires retaining its sign kernels.

For augmented plats, the [actual matching-graph construction](../../notes/general_augmented_plat_matching_geometry.md) is one way to supply this certificate: a positive labeled right-angled polyhedron gives the marked complete exterior and an explicit positive ideal triangulation. The general gluing criterion does not require that particular polyhedral decomposition or a bound on bridge width.

## The general endpoint action has the actual volume normalization

The original augmented-plat coupon now has an [exact local critical-character map](../../notes/actual_augmented_plat_local_critical_character_map.md). It preserves the whole ordered meridian product, recovers the actual crossing-circle transport and retains both physical degree charts and signed half twists. On a correctly marked stationary branch, the original Fourier coupling gives $d(2\pi i\phi)=\tfrac12\sum_i V_i\,dU_i$ in its specified peripheral convention.

A [generic-framing theorem](../../notes/actual_augmented_plat_regular_geometric_phase_chart.md) places the complete geometric representation in regular charts for every coupon simultaneously. It also solves the unrestricted integral degree-lifting problem. It does not put that candidate into a contributing physical support chamber or choose a contributing Poisson sector.

The [endpoint regulator theorem](../../notes/actual_augmented_plat_endpoint_regulator.md) fixes the absolute constant. The fully normalized q-Hahn action and the original crossing-circle diagram have the same rational wedge. Their Bloch–Wigner regulators agree at a real point and hence throughout the connected regular chart. The original diagram cycle has degree one on each cusp, so its regulator is the actual augmented-link volume. Writing $Y_D$ for the actual augmented-link exterior of the fixed diagram $D$, the full stationary-action identity gives

$$2\pi\operatorname{Re}\phi(0)=\operatorname{Vol}(Y_D).$$

This holds at a regular, correctly marked full geometric critical point; the fixed endpoint channel has purely imaginary logarithm and introduces no residual real contribution. The theorem fixes the geometric candidate's value. A quantum cycle coefficient, a nonzero amplitude and bounds for other contributions remain separate parts of the general conjecture.

The same marked matrices now determine the [channel Hessian](../../notes/actual_augmented_plat_channel_hessian.md), without assuming a deformation theorem. If the endpoint transport is $I+b_iH_i$ with $H_i^2=0$, the actual primitive cusp shape is $\tau_i=(b_i-\epsilon_i/2)^{-1}$. Let $\xi_i$ be the scaled channel variables, $y$ the remaining magnetic variables, and $F$ the full local phase. After the two internal q-Hahn variables are eliminated on their marked critical sheets,

$$\frac{\partial^2 F}{\partial\xi_i\partial\xi_j}=-\delta_{ij}\frac{4\pi i}{\tau_i},\qquad \frac{\partial^2 F}{\partial\xi_i\partial y}=0.$$

Since $\operatorname{Im}\tau_i>0$, this channel block has negative real part. Eliminating those channels gives the color Hessian $\pi i\operatorname{diag}(\tau_i)$, with the factor of two in the transfer convention retained.

The [marked multi-cusp rigidity theorem](../../notes/general_marked_multicusp_gluing_rigidity.md) supplies a direct deformation proof from an actual positive ideal gluing certificate. Positive polarization makes the marked gluing Jacobian invertible; the developing-map inverse retains exact peripheral eigenflags, including infinitesimal data.

The [actual critical-scheme theorem](../../notes/actual_augmented_plat_critical_scheme.md) then reconstructs the whole ordered representation from the stationary magnetic variables and conversely. The magnetic Hessian has exactly two null directions, both from framing. After taking a transverse slice, there is a nearby holomorphic geometric stationary branch, with the displayed peripheral differential and absolute volume anchor. This classical existence statement is general in plat width under the certificate. Selecting it from the original quantum sum is a separate analytic requirement, now met for the specifically proved families but not asserted for every plat.

There is now an explicit [physical framing test](../../notes/actual_augmented_plat_physical_framing_criterion.md) for the domain of the joint kernel theorem. One rank-one projector records the common frame; traces of the original prefix words give finite strict inequalities for every input and output. The theorem distinguishes these inequalities from mere avoidance of algebraic chart poles. The [local sheet test](../../notes/actual_q_hahn_joint_complex_amplitude.md) then checks which characteristic root the finite source selects. Neither test asserts that a common solution or a contributing global cycle always exists.

The [right-angled framing obstruction](../../notes/actual_right_angled_selected_framing_obstruction.md) now rules out an all-central selected common frame for the certified right-angled plats. In the Lorentz model, the white face normals form a convex polyhedron whose facets correspond to the original shaded triangles. Under the oriented geometric strip conditions, the two flags determine a line through its interior. At each facet crossed by that line, a nonnegative relation among the three actual prefix diagonals violates strict physical support. Generic flags cross exactly two facets, so the obstruction involves exactly two local factors at every bridge width. Any two distinct facets can be prescribed, including the pair incident to the original marked physical edge. The [selected-factor corollary](../../notes/actual_augmented_plat_selected_factor_localization.md), using the [full physical packet](../../notes/actual_q_hahn_full_physical_complex_packet.md), now proves that every other ordinary factor is physical and source-selected. The selected square root is continued from the original source; the old pointwise principal-root test is not assumed outside the central domain. The completed contraction and global quantum cycle remain unresolved.

![A schematic section of the white-normal convex polyhedron: the polarization line crosses two facets, locating the two strict physical-support failures.](../figures/two-exceptional-factors.png)

For the complete-circle source, the pair at a crossing-circle matching edge now has an [exact rewrite with four external representation factors](../../notes/actual_matching_edge_marked_four_port_block.md). Its four outside objects are all physical, so the [positive scalar estimate](../../notes/actual_matching_edge_racah_positive_scalar.md) applies to every target channel, independently of bridge width. The original row measure cancels its exponential factorial gauge. In this unrestricted-plat method, the target tensor, the remaining network and the original integration contour still require control; geometric localization alone does not estimate them.

The [finite selected-critical certificate](../../notes/actual_augmented_plat_selected_local_certificate.md) combines the positive gluing, common-frame and local-sheet tests, retaining the original logarithmic characters. When supplied, it identifies the geometric stationary germ with the source-selected local principal phase. At completeness the sheet tests also have an exact interpretation as oriented regions between the two actual disk circles. For other geometric realizations, existence of that simultaneous certificate remains open. For an unrestricted plat, this test alone does not show that the geometric point contributes to the original integration contour.

The same deformation coordinates give a [geometric long-filling corollary](../../notes/general_augmented_plat_long_filling_quantifiers.md) without a quantum input. Write $V_i(U)=U_i t_i(U)$ and set $e_i=1/p_i$ at filled cusps, $e_i=0$ at unfilled ones. The equations $V_i(U)+e_iU_i=-2\pi i e_i$ have an invertible Jacobian at completeness and a solution in one fixed polydisk. Their exact factorization bounds each $|U_i|$ by a constant times $|e_i|$. The existing geometric completion argument therefore applies to all independently long signed slopes. This proves the geometric threshold, while the volume-limit threshold still requires the quantum estimates.

## The local maximum can be the wrong global maximum

The four face-support inequalities alone are insufficient. In the local hyperideal theorem, differentiating the normalized action with respect to a color gives the corresponding edge length. Increasing every color preserves those support inequalities and pushes the maximum to an octahedral boundary configuration.

A manifold saddle therefore requires the actual global edge constraints or additional boundary contributions. This is a concrete obstruction to deriving the complement volume by multiplying separately maximized local estimates.

There is now an exact [geometric interpretation of a native magnetic energy](../../notes/actual_native_magnetic_energy_local_geometry.md). At the folded color, the highest-weight degree block gives four positive ideal tetrahedra forming a convex ideal octahedron, whose maximum is $v_8$. The full boundary operator has the larger rate computed in the [Plancherel theorem](../../notes/actual_matching_edge_magnetic_energy_profile.md). Away from the fold the normalized summands require a signed face term. These are local comparison geometries; placing their cells in the actual complement and matching the remaining phase equations still requires proof.

The [positive radial Fourier obstruction](../../notes/actual_positive_fourier_radial_geometric_obstruction.md) makes the phase issue concrete for the general certified right-angled source. Its retained cycle congruences close particular local momentum characters, including the cup signs and marked charge. They do not supply the real magnetic-coordinate matching equations carried by the discarded coefficient phases. An all-ordinary strict radial reconstruction would contradict the common-frame theorem above. This excludes that proposed geometric assembly, without asserting a strict gap between positive and coherent exponential rates.

## Shared cores explain the cube test

For the certified augmented graph geometry, the actual volume has the form

$$4b\,v_8+2\operatorname{Vol}(Q),$$

where \(Q\) is the supplied positive ideal right-angled central polyhedron and \(b\) counts the prescribed octahedral pieces in that construction. The exact cut, face, and cusp identifications are checked in its theorem. The core is shared by the graph; it is not a sum of independent vertex constants.

The cube is a useful nontrivial example of this phenomenon. Its projected quantum calculations recover the shared core contribution. Extending those estimates to the full source is still a quantum problem, even after the geometric complement has been constructed.
