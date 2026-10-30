# Why the right side is hyperbolic volume

## A local tetrahedron is a genuine geometric result

In the supported four-port theorem, the exact half-shifted color coordinate is

$$a_e=\frac{j_e+1/2}{N},\qquad \alpha_e=\pi-2\pi a_e.$$

The normalized scalar action is identified with the volume of the truncated hyperideal tetrahedron with these dihedral angles. The proof constructs its Lorentzian face Gram matrix, recovers edge lengths, checks the volume differential, and fixes the additive constant by an ideal calibration. Boundary values are continuous volume extensions.

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

## The local maximum can be the wrong global maximum

The four face-support inequalities alone are insufficient. In the local hyperideal theorem, differentiating the normalized action with respect to a color gives the corresponding edge length. Increasing every color preserves those support inequalities and pushes the maximum to an octahedral boundary configuration.

A manifold saddle therefore requires the actual global edge constraints or additional boundary contributions. This is a concrete obstruction to deriving the complement volume by multiplying separately maximized local estimates.

## Shared cores explain the cube test

For the certified augmented graph geometry, the actual volume has the form

$$4b\,v_8+2\operatorname{Vol}(Q),$$

where $Q$ is the supplied positive ideal right-angled core and the precise cut, face, and cusp identifications are checked. The core is shared by the graph; it is not a sum of independent vertex constants.

The cube is a useful nontrivial example of this phenomenon. Its projected quantum calculations recover the shared core contribution. Extending those estimates to the full source is still a quantum problem, even after the geometric complement has been constructed.

## The Conway maximum now builds the actual complement

The [global Conway geometry theorem](../../notes/actual_positive_conway_hyperbolic_volume.md) supplies the missing face-pairing certificate for every retained cylindrical robust factor. A leaf is an ideal quadrangular pyramid. A multiplication gate is a convex ideal triangular prism. Their volumes are exactly the source actions, and their ordered quadrilateral metrics are exponentials of the action derivatives.

![The source's leaf pyramid and multiplication prism. Blue faces are ordered quadrilateral ports; the shaded leaf triangles retain the actual crossing-disk pairing.](../figures/conway-cells.png)

Stationarity makes the shared ports isometric under the literal stack maps. A boundary barrier proves that every unforced cell at the maximum is strict. The cells assemble into a convex ideal polyhedron; the actual cylindrical closure leaves only right-angled boundary edges. Reversing the projection and crossing-disk cuts reconstructs the original link. Four-step edge cycles give angle $2\pi$ with identity return, and matched rectangular horosphere links prove cusp completeness. Thus the two-copy volume is the volume of the actual complement.

The [closed bowtie-cut proof](../../notes/actual_conway_bowtie_projection_cut.md) identifies every oriented white and shaded face from the literal original wires. It corrects an earlier overstatement about open cells: a quadrilateral port alone is not half of the physical four-punctured tangle boundary. The closed reconstruction uses the entire labeled ribbon graph and reversible disk cut. It also gives each complete crossing-circle cusp its primitive shape $2i\cot(\pi x_i)$.

The final product gate is forced flat and is removed from the geometric cell list using its exact unit source coefficient. This does not delete a quantum contribution or a link component. The [local cell proof](../../notes/actual_newton_ideal_prism_and_associativity.md) also identifies source associativity with two triangulations of one actual ideal cube.

The [cap-sum reduction](../../notes/actual_conway_cap_sum_reduction.md) goes further: an actual two-punctured separating sphere splits every cap-closed product into componentwise connected sums. The quantum source factors and the angle polytope splits with it. This gives connected sums of theta links with strictly positive rate $4k v_8$, although the whole complement is not hyperbolic for $k\geq2$.

## The maximum now has an algebraic source class

The [algebraic optimizer theorem](../../notes/positive_source_algebraic_volume_period.md) applies to every rational affine ideal-angle problem with positive rational weights. On the smallest face containing the maxima, flat atoms contribute zero. The remaining Hessian is definite after quotienting by the rational directions that leave all nonflat angles unchanged. Exponentiated stationarity then proves that the nonflat shapes are algebraic, including boundary and nonunique maxima.

The [Bloch regulator calculation](../../notes/actual_positive_source_bloch_regulator.md) proves that the conjugate-antisymmetrized shape sum is a rational Bloch class with regulator equal to the source maximum. For the retained cylindrical factors, the new actual cell realization supplies its geometric interpretation. The class comparison takes place after passing to a common finite conjugation-stable number field containing the source shapes and all glued ideal vertex coordinates. The two copies have opposite mirror orientations, producing precisely the shape symbols $[z]-[\overline z]$ of the geometric fundamental chain; no identification with the geometric trace field is claimed.

For every fixed robust positive Conway expression, the proved full-source statement is

$$\lim_{N\to\infty}\frac{2\pi}{N}\log Z_{E,N}
=R_{F_E}(B_E),\qquad B_E=\sum_j([z_j]-[\overline{z_j}])\in B(F_E)_{\mathbb Q}.$$

Here $F_E=\mathbb Q(z_j,\overline{z_j})$ is the conjugation-stable source shape field. The regulator uses the specified complex embedding. For a retained cylindrical factor its value is now proved to be the actual complement volume. The theorem does not establish a generic-meridian knot quantum A-operator or volume limits for arbitrary short fillings.

The [boundary profile theorem](../../notes/actual_conway_boundary_volume_relation.md) also gives a full limit for every coefficient approaching any output $b\in[0,1]$. On $(0,1)$ its optimizer is unique and analytic, and its boundary conjugate is the actual quadrilateral modulus $\exp(-v'_E(b)/\pi)$. This is a geometric meaning for the source boundary relation; the variable is not yet the knot's peripheral holonomy.

## The deformed source has actual peripheral holonomy

The [marked deformation theorem](../../notes/actual_conway_marked_peripheral_deformation.md) constructs a representation of the actual link group for the auxiliary-color critical branch. Exact Möbius identities establish every white seam and shaded edge relation, including translations. All main cusps stay parabolic. For each auxiliary circle the primitive logarithms are

$$U_i=-2\pi i\chi_i,\qquad V_i=-2\partial_i\phi(\chi).$$

Thus the source primitive $G=2\pi i\phi$ satisfies $dG=\tfrac12\sum_i V_i\,dU_i$, with its constant fixed by the complete fundamental-chain volume. Exponentiated source stationarity gives an algebraic marked peripheral branch; the selected branch is locally a Lagrangian graph in the auxiliary peripheral coordinates, with the main cusps held parabolic. The displayed peripheral multipliers are squared SL eigenvalues, and no entire A-polynomial is inferred merely by elimination.

At the original filling saddle, $U_i+p_iV_i=-2\pi i$ holds in the primitive disk marking. The actual nearby representation and the boundary-corrected regulator then identify the full quantum rate with the volume of the correctly filled complement. This applies to every retained robust factor and independently sufficiently long fixed signed integral fillings of any selected auxiliary circles. The component theorem keeps its link-only scope explicit.

## Half twists preserve the marked action through a shear

The [odd-coupon deformation](../../notes/actual_odd_conway_marked_peripheral_deformation.md) changes the shaded face pairings and checks their edge words at general complex parameters. The original odd-link peripheral paths give

$$U_i^\epsilon=U_i^0-\frac{\epsilon_i}{2}V_i^0,\qquad V_i^\epsilon=V_i^0,\qquad G_\epsilon=G_0-\sum_i\frac{\epsilon_i}{8}(V_i^0)^2.$$

These are also the exact derivatives and quadratic correction of the selected finite-source action. On the marked double cover $\ell_i^2=L_i$, the half-longitude change becomes the integral monomial map $M_i^\epsilon=M_i^0\ell_i^{-\epsilon_i}$. The source selects the square root and its logarithm. This is a concrete torsor carrying the required peripheral information.

![Left: a primitive filling slope on a schematic cusp torus. Right: local sheets of the peripheral square-root cover, with the selected branch and integral shear.](../figures/peripheral-torsor.png)

The square is a fundamental domain, not a metric cusp shape. Its amber segments form the single primitive curve $\mu+2\lambda$ after opposite sides are identified. The two sheets on the right are a local picture of $\ell^2=L$; the cover is not asserted to split globally. The selected logarithm retains the primitive filling equation $U+pV=-2\pi i$.

Smooth filling uses the primitive basis of the **changed link**. Substituting a half-integer slope into the pure-link formula would double the primitive rotation angle when denominators are cleared. The actual odd-link construction avoids that error, keeps main cusps parabolic, and fixes the regulator at its complete volume. Together with the full changed-source estimates it yields the [general signed Conway knot and link theorem](../../notes/actual_odd_conway_long_filling_volume.md).
