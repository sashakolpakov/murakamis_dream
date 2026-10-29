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

The final product gate is forced flat and is removed from the geometric cell list using its exact unit source coefficient. This does not delete a quantum contribution or a link component. The [local cell proof](../../notes/actual_newton_ideal_prism_and_associativity.md) also identifies source associativity with two triangulations of one actual ideal cube.

The [cap-sum reduction](../../notes/actual_conway_cap_sum_reduction.md) goes further: an actual two-punctured separating sphere splits every cap-closed product into componentwise connected sums. The quantum source factors and the angle polytope splits with it. This gives connected sums of theta links with strictly positive rate $4k v_8$, although the whole complement is not hyperbolic for $k\geq2$.

## The maximum now has an algebraic source class

The [algebraic optimizer theorem](../../notes/positive_source_algebraic_volume_period.md) applies to every rational affine ideal-angle problem with positive rational weights. On the smallest face containing the maxima, flat atoms contribute zero. The remaining Hessian is definite after quotienting by the rational directions that leave all nonflat angles unchanged. Exponentiated stationarity then proves that the nonflat shapes are algebraic, including boundary and nonunique maxima.

The [Bloch regulator calculation](../../notes/actual_positive_source_bloch_regulator.md) proves that the conjugate-antisymmetrized shape sum is a rational Bloch class with regulator equal to the source maximum. For the retained cylindrical factors, the new actual cell realization supplies its geometric interpretation. The class comparison takes place after passing to a common finite conjugation-stable number field containing the source shapes and all glued ideal vertex coordinates. The two copies have opposite mirror orientations, producing precisely the shape symbols $[z]-[\overline z]$ of the geometric fundamental chain; no identification with the geometric trace field is claimed.

For every fixed robust positive Conway expression, the proved full-source statement is

$$\lim_{N\to\infty}\frac{2\pi}{N}\log Z_{E,N}
=R_{F_E}(B_E),\qquad B_E=\sum_j([z_j]-[\overline{z_j}])\in B(F_E)_{\mathbb Q}.$$

Here $F_E=\mathbb Q(z_j,\overline{z_j})$ is the conjugation-stable source shape field. The regulator uses the specified complex embedding. For a retained cylindrical factor its value is now proved to be the actual complement volume. The theorem does not yet establish a generic-meridian knot A-operator or volume limits for arbitrary fillings.

The [boundary profile theorem](../../notes/actual_conway_boundary_volume_relation.md) also gives a full limit for every coefficient approaching any output $b\in[0,1]$. On $(0,1)$ its optimizer is unique and analytic, and its boundary conjugate is the actual quadrilateral modulus $\exp(-v'_E(b)/\pi)$. This is a geometric meaning for the source boundary relation; the variable is not yet the knot's peripheral holonomy.
