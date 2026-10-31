# Why the limiting action is the actual knot volume

A formula involving dilogarithms is not yet a geometric volume formula. To obtain the volume on the right side of the theorem, the proof must construct the intended manifold, verify its metric, and retain the meridian and longitude used for each filling. This chapter explains those steps and the different roles of the local geometric results.

For the [strict Conway tree theorem](../../notes/actual_conway_all_strict_tree_long_twist_volume.md), all of these steps are proved. The full quantum estimates and the nonzero local contribution are proved as well. The result concerns the actual resulting knot complement, with its main cusp left unfilled. The more general plat constructions discussed later have their own hypotheses; a missing estimate in one of those routes is not a gap in the strict-tree theorem.

## The geometric objects and the required checks

Start with the augmented diagram: each twist region has an auxiliary crossing circle around its two strands. Cutting along the projection sphere and the original crossing disks divides its exterior into pieces with labeled faces. The labels remember exactly how to glue the pieces back. They also remember which curves on each torus end are the original meridian and longitude.

An **ideal vertex** lies at the boundary at infinity of hyperbolic space. A small horosphere about it cuts a Euclidean polygon from each adjacent cell. These polygons are the vertex links. In a complete link complement, the polygons around each end glue to a Euclidean torus. This torus is a cross-section of a **cusp**, the noncompact end of the manifold. Checking only that the dihedral angles sum to \(2\pi\) does not establish cusp completeness; the horospherical polygons must also match with the correct translations.

An **angle structure** assigns positive dihedral angles to the proposed cells while satisfying their internal angle relations and the sum around every glued edge. Its volume is the sum of the cell volumes. The angles still retain the actual incidence equations: two copies of one manifold edge are not independent variables. At an interior maximum, variation in every allowed direction gives the shape-matching equations. The proof must then show that these equations produce the original face pairings and complete ends.

A **marked** construction retains the chosen peripheral curves and their basepaths. This matters after filling. The equation that closes a meridian disk depends on a primitive pair of curves on the torus, not just on an unlabeled complex cusp shape. Replacing a primitive longitude by twice that curve would change the filling problem.

## The strict-tree construction

A Conway expression is a recorded sequence of two operations on tangles: stack two boxes, or turn one box through a quarter-turn. Its leaves are the original twist regions. The finite strictness test in the theorem is a compatibility test for the positive angles of these operations. It is not a claim that any written tangle expression becomes hyperbolic when its displayed exponents are large.

The geometric pieces follow these operations. Each leaf contributes an ideal quadrangular pyramid, and each retained product contributes an ideal triangular prism. Their volumes agree with the local terms of the complete quantum action. Each quadrilateral gluing face has four ordered ideal vertices. The order specifies which vertex is identified with which when two cells are attached; it is part of the geometry, not just a label for a boundary variable. The metrics of these faces are determined by derivatives of the action. When the full action is stationary under the shared-index constraints, those metrics agree across the actual ordered product faces.

The [general strict-mask geometry theorem](../../notes/actual_conway_general_strict_mask_geometry.md) proves that these pieces assemble with the original cyclic orders, including turns and the different boundary edge types. An edge type records whether its face is supplied directly by a leaf crossing disk or by the surrounding projection region. The bookkeeping is needed to prevent a formally matching quadrilateral from being attached to the wrong side. The proof rules out the vertex identifications that would collapse a shaded triangle, checks the edge cycles, and constructs positive rectangular cusp links.

The final identification with the diagram uses the [literal bowtie cut](../../notes/actual_conway_bowtie_projection_cut.md). A bowtie is the pair of triangular faces exposed by one crossing disk. Its four outer corners are joined by the actual main strands of the diagram. Reading those joins in their projection order determines every remaining face. Reversing the cut therefore recovers the original link exterior with its original auxiliary circles. Matching a count of vertices or a total volume would not suffice.

The [marked deformation theorem for the full strict class](../../notes/actual_conway_general_mask_marked_filling.md) extends the complete construction to nearby complex auxiliary colors. Its face maps satisfy the original group relations, including their translational parts. Every main cusp remains parabolic. On an auxiliary cusp it supplies specified logarithms \(U_i,V_i\) of the peripheral multipliers. Here a logarithm includes its chosen branch, so it records a winding that a bare eigenvalue would forget.

Write the actual twist weight as \(n_i=\epsilon_i-2p_i\), with \(\epsilon_i\in\{0,\pm1\}\) recording a retained half twist. The filling equation uses the primitive basis of this actual half-twisted link. For every fixed choice of sufficiently large independent signed \(p_i\), the nearby solution gives a smooth filling of the auxiliary cusp. The main knot cusp is never filled. The action, with its boundary correction, equals the volume of that resulting knot complement. The quantum theorem uses exactly this solution and normalization.

The next sections give further details and explain the older constructions that supplied parts of this argument.

## How the cells and the diagram are identified

The [global Conway geometry theorem](../../notes/actual_positive_conway_hyperbolic_volume.md) supplies the face-pairing certificate for every cylindrical factor in its original positive seed-generated grammar. Here cylindrical closure joins each lower external strand to the corresponding upper strand; it differs from joining the two upper ends to each other and the two lower ends to each other. The later strict-mask theorem extends the geometric construction as described above. A leaf is an ideal quadrangular pyramid. A multiplication gate is a convex ideal triangular prism. Their volumes are exactly the source actions, and their ordered quadrilateral metrics are exponentials of the action derivatives.

![The source's leaf pyramid and multiplication prism. Blue faces are quadrilateral gluing faces with ordered vertices; the shaded leaf triangles retain the actual crossing-disk pairing.](../figures/conway-cells.png)

Stationarity makes the shared quadrilateral gluing faces isometric under the literal stack maps. A boundary barrier proves that every unforced cell at the maximum is strict. The cells assemble into a convex ideal polyhedron; the actual cylindrical closure leaves only right-angled boundary edges. Reversing the projection and crossing-disk cuts reconstructs the original link. Four-step edge cycles give angle $2\pi$ with identity return, and matched rectangular horosphere links prove cusp completeness. Thus the two-copy volume is the volume of the actual complement.

The [closed bowtie-cut proof](../../notes/actual_conway_bowtie_projection_cut.md) identifies every oriented white and shaded face from the literal original wires. It corrects an earlier overstatement about open cells: a quadrilateral gluing face alone is not half of the physical four-punctured tangle boundary. The closed reconstruction uses the entire labeled ribbon graph and reversible disk cut. It also gives each complete crossing-circle cusp its primitive shape $2i\cot(\pi x_i)$.

The final product gate is forced flat and is removed from the geometric cell list using its exact unit source coefficient. This does not delete a quantum contribution or a link component. The [local cell proof](../../notes/actual_newton_ideal_prism_and_associativity.md) also identifies source associativity with two triangulations of one actual ideal cube.

A cap closure joins the two upper endpoints to one another and the two lower endpoints to one another. The [cap-sum reduction](../../notes/actual_conway_cap_sum_reduction.md) goes further: an actual two-punctured separating sphere splits every cap-closed product into componentwise connected sums. The quantum source factors and the angle polytope splits with it. This gives connected sums of theta links with strictly positive rate $4k v_8$, although the whole complement is not hyperbolic for $k\geq2$.

## Algebraic shapes and their volume regulator

The [algebraic optimizer theorem](../../notes/positive_source_algebraic_volume_period.md) applies to every rational affine ideal-angle problem with positive rational weights. On the smallest face containing the maxima, flat atoms contribute zero. The remaining Hessian is definite after quotienting by the rational directions that leave all nonflat angles unchanged. Exponentiated stationarity then proves that the nonflat shapes are algebraic, including boundary and nonunique maxima.

The Bloch group packages algebraic tetrahedron shapes together with the relations obtained by changing a triangulation. Its regulator evaluates those shape symbols by the oriented dilogarithm volume. The [Bloch regulator calculation](../../notes/actual_positive_source_bloch_regulator.md) proves that the conjugate-antisymmetrized shape sum is a rational Bloch class with regulator equal to the source maximum. For the retained cylindrical factors, the new actual cell realization supplies its geometric interpretation. The class comparison takes place after passing to a common finite conjugation-stable number field containing the source shapes and all glued ideal vertex coordinates. The two copies have opposite mirror orientations, producing precisely the shape symbols $[z]-[\overline z]$ of the geometric fundamental chain; no identification with the geometric trace field is claimed.

For a fixed positive Conway expression \(E\) in that earlier seed-generated grammar, let \(Z_{E,N}\) be its complete quantum sum. Its statement is

$$\lim_{N\to\infty}\frac{2\pi}{N}\log Z_{E,N}
=R_{F_E}(B_E),\qquad B_E=\sum_j([z_j]-[\overline{z_j}])\in B(F_E)_{\mathbb Q}.$$

Here \(z_j\) are the algebraic shapes, \(F_E=\mathbb Q(z_j,\overline{z_j})\) is the number field containing them and their conjugates, \(B(F_E)_{\mathbb Q}\) is the rational Bloch group, and \(R_{F_E}\) is its volume regulator at the specified complex embedding. For a retained cylindrical factor its value is now proved to be the actual complement volume. This geometric argument does not identify a generic main-meridian characteristic factor or prove arbitrary short-filling limits. Actual all-level quantum A-operators exist by a separate finite cut-state proof, and the pointed operator-period volume theorem is now established for the covered strict long-twist knots.

Fixing an output index of an open tangle changes the maximization problem. The resulting function of the scaled output \(b\) is its boundary profile. The [boundary profile theorem](../../notes/actual_conway_boundary_volume_relation.md) also gives a full limit for every coefficient approaching any output $b\in[0,1]$. On $(0,1)$ its optimizer is unique and analytic, and its boundary conjugate is the actual quadrilateral modulus $\exp(-v'_E(b)/\pi)$. This is a geometric meaning for the source boundary relation; the variable is not yet the knot's peripheral holonomy.

## The deformed source has actual peripheral holonomy

In the earlier positive grammar, the [marked deformation theorem](../../notes/actual_conway_marked_peripheral_deformation.md) constructs a representation of the actual link group for the auxiliary-color critical branch. Exact Möbius identities establish every white seam and shaded edge relation, including translations. All main cusps stay parabolic. Let \(\chi_i\) be the scaled auxiliary-color deficit, and let \(\phi(\chi)\) be the selected limiting action. For each auxiliary circle the primitive logarithms are

$$U_i=-2\pi i\chi_i,\qquad V_i=-2\partial_i\phi(\chi).$$

The function \(G=2\pi i\phi\), called a primitive because its derivative is the displayed peripheral one-form, satisfies $dG=\tfrac12\sum_i V_i\,dU_i$, with its constant fixed by the complete fundamental-chain volume. Exponentiated source stationarity gives an algebraic marked peripheral branch; the selected branch is locally a Lagrangian graph: the exterior derivative of that peripheral one-form vanishes on it. This statement concerns the auxiliary peripheral coordinates, with the main cusps held parabolic. The displayed peripheral multipliers are squared SL eigenvalues, and no entire A-polynomial is inferred merely by elimination.

At the original filling saddle, $U_i+p_iV_i=-2\pi i$ holds in the primitive disk marking. The actual nearby representation and the boundary-corrected regulator then identify the full quantum rate with the volume of the correctly filled complement. This applies to every retained robust factor and independently sufficiently long fixed signed integral fillings of any selected auxiliary circles. The component theorem keeps its link-only scope explicit.

## Half twists preserve the marked action through a shear

The [odd-coupon deformation](../../notes/actual_odd_conway_marked_peripheral_deformation.md) changes the shaded face pairings and checks their edge words at general complex parameters. The original odd-link peripheral paths give

$$U_i^\epsilon=U_i^0-\frac{\epsilon_i}{2}V_i^0,\qquad V_i^\epsilon=V_i^0,\qquad G_\epsilon=G_0-\sum_i\frac{\epsilon_i}{8}(V_i^0)^2.$$

These are also the exact derivatives and quadratic correction of the selected finite-source action. Write $M_i=e^{U_i}$ and $L_i=e^{V_i}$ for these auxiliary peripheral multipliers. On the marked double cover $\ell_i^2=L_i$, the half-longitude change becomes the integral monomial map $M_i^\epsilon=M_i^0\ell_i^{-\epsilon_i}$. The source selects the square root and its logarithm. The square root is part of the marked data. Changing it changes the logarithmic branch, so it cannot be discarded when comparing the source and the filling equation. This is the concrete peripheral data described as a torsor in the technical note.

![Left: a primitive filling slope on a schematic cusp torus. Right: local sheets of the peripheral square-root cover, with the selected branch and integral shear.](../figures/peripheral-torsor.png)

The square is a fundamental domain, not a metric cusp shape. Its amber segments form the single primitive curve $\mu+2\lambda$ after opposite sides are identified. The two sheets on the right are a local picture of $\ell^2=L$; the cover is not asserted to split globally. The selected logarithm retains the primitive filling equation $U+pV=-2\pi i$.

Smooth filling uses the primitive basis of the link with its retained half twists. Substituting a half-integer slope into the pure-link formula would double the primitive rotation angle when denominators are cleared. The actual odd-link construction avoids that error, keeps main cusps parabolic, and fixes the regulator at its complete volume. Together with the full changed-source estimates it yields the [general signed Conway knot and link theorem](../../notes/actual_odd_conway_long_filling_volume.md).

## A second route: circle patterns for general augmented plats

For a connected labeled right-angled augmented plat at any fixed bridge width, the [signed complete-source theorem](../../notes/general_signed_augmented_source_volume.md) identifies the original source rate with the actual complete volume. The [fixed complex core theorem](../../notes/actual_complete_core_complex_packet.md) now gives a nonzero analytic asymptotic for its complete-image external-color term. This construction is independent of the strict-tree recursion; the statements below retain their own hypotheses.

A circle pattern represents the labeled boundary faces by circles or lines at infinity, with the prescribed tangencies. The [marked circle-pattern theorem](../../notes/actual_marked_deformed_circle_pattern.md) reconstructs the two exceptional boundary faces as parallel lines and solves simultaneously for all finite circle centers and radii. The original positive face Hessian, followed by elementary rigidity of the center triangles, proves that this system has an invertible Jacobian. Its unique nearby solution has exactly the stationary radii of the source action, with one shared strip width and the selected boundary eigenlines retained.

![The actual marked lines retain their shared width and the selected eigenlines as matching tangencies deform.](../figures/marked-circle-strip.png)

The [primitive collar theorem](../../notes/actual_deformed_circle_primitive_collar.md) computes the actual side pairing, selected eigenflag and half-twist shear, including a common marked-line limit. The [global geometric assembly](../../notes/actual_complete_core_geometric_deformation.md) verifies the full original group presentation and identifies the core's limiting action with the marked geometric deformation. For complex meridian logs it retains the boundary correction $\tfrac12\sum_i\operatorname{Re}U_i\operatorname{Im}V_i$; for real external deficits this correction vanishes. For an unrestricted plat, these geometric and local core statements still need bounds on the remaining reflected-color terms before they imply a full filling theorem. Several separately certified plat families and the strict-tree class already have those bounds; see the [results](results.md) and [remaining scope](frontier.md).

![The same crossing-disk collar in two coordinates. On the left, the ordered contact points lie on the input and output circles. A Möbius coordinate sends the two selected eigenpoints to zero and infinity; on the right, the actual side pairing is a dilation. The auxiliary meridian follows its inverse.](../figures/deformed-circle-collar.png)

An identity smoothing replaces a specified crossing-disk coupon by the identity and retains the remaining face identifications. For such a diagram, the [block capacity theorem](../../notes/actual_smoothed_source_capacity_blocks.md) removes the need to assume an attained positive-radius minimum. Here capacity is the infimum of the positive weighted expression used for a coefficient bound. The theorem splits degenerate angle problems along two-edge cycles and constructs each simple block's actual polyhedron. The [block representation and volume theorem](../../notes/actual_smoothed_block_representation_volume.md) then retains the original face pairings and realizes their volume sum as a regulator of the original group. Its deleted meridians lie in the kernel, so the [strict-kernel theorem](../../notes/general_representation_volume_kernel_strictness.md) proves strict loss for every nonempty connected untwisted smoothing with finite capacity. Loop-infeasible cases already have an arbitrarily low capacity bound.

The chain argument uses a controlled finite degeneration: cut corners have a common horospherical height and mutual distance $O(T^{-1})$. A uniform short-edge tetrahedron estimate makes the added volume vanish. Arbitrary ideal vertices merely approaching one another would not justify this step. The [near-maximal-volume corollary](../../notes/general_representation_volume_peripheral_gap.md) also gives uniform gaps from fixed marked peripheral trace conditions; applying those gaps to the remaining quantum color complement is still a source-estimate problem.

## A local tetrahedron is a genuine geometric result

In the local theorem with four external representation labels, the exact half-shifted color coordinate is

$$a_e=\frac{j_e+1/2}{N},\qquad \alpha_e=\pi-2\pi a_e.$$

The normalized scalar action is identified with the volume of the truncated hyperideal tetrahedron with these dihedral angles. The proof constructs the Gram matrix of the outward face normals in the Lorentz model of hyperbolic space, recovers edge lengths, checks the volume differential, and fixes the additive constant by an ideal calibration. Boundary values are continuous volume extensions.

![A truncated tetrahedron in a combinatorial projection. Blue triangles indicate polar truncation faces; the hyperbolic metric comes from the Gram matrix.](../figures/truncated-tetrahedron.png)

This is stronger than observing that a factorial action resembles a dilogarithm. It is also local: a collection of such tetrahedra does not automatically form the knot complement.

## The global angle slice carries the topology

An actual ideal triangulation specifies which faces are glued, which tetrahedron edges belong to each manifold edge, and which peripheral curves represent meridians and longitudes. Its angle constraints must retain this incidence.

At a candidate maximum, stationarity must hold in every allowed angle direction. The corresponding shape and length equations must make adjacent cells agree. The resulting developing map must have the intended winding and end behavior. Complete cusps, or the specified filled peripheral equations, are part of the certificate.

The [source-volume certificate](../../notes/source_volume_casson_rivin_certificate.md) keeps these requirements explicit. An algebraic critical point can be isolated and still belong to the wrong component or have the wrong peripheral marking.

## A general certificate through volume maximization

For an actual marked ideal triangulation with torus vertex links, the [positive gluing criterion](../../notes/general_marked_positive_gluing_certificate.md) gives a direct proof of the Casson–Rivin equivalence: an interior critical point of the ideal-tetrahedron volume function is exactly a complete positive gluing. Strict concavity makes it the unique maximum, including over the closed angle polytope, and its value is the actual complement volume.

The proof keeps the geometry explicit. Lagrange multipliers prescribe one truncated length for each global edge. These lengths determine compatible corner horospheres; the face maps then match them, giving complete flat cusp tori. Conversely, compatible horospheres make the geometric volume stationary under all allowed angle variations.

There is a finite algebraic certificate using positive upper-half-plane phases and positive multiplier variables. The unique optimum has algebraic shapes. Neither its dilogarithm volume nor the original quantum period is asserted to be an algebraic number. Existence of an interior optimum on a proposed triangulation, and selection of its period by the quantum source, remain distinct questions.

For fixed critical shapes, the positive multiplier solutions form a concrete torsor: one independent positive horosphere scale per cusp acts freely and transitively. This accounts for the decoration freedom in the algebraic certificate. It does not yet determine the quantum period, and extending the action to complex scalars requires retaining its sign kernels.

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
