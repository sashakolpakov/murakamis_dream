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

## What remains for the Conway variational limit

The positive Conway theorem already produces an explicit concave sum of ideal-tetrahedron volumes with shared affine angles. What it has not yet supplied in general is a face-pairing certificate showing that these tetrahedra describe the actual compiled diagram complement.

Some compiled expressions have polynomial growth and zero variational maximum. Thus positivity cannot serve as a criterion for hyperbolicity. A useful general extension must state the actual topological and geometric hypotheses under which the source polytope is the complement's angle slice.

The [seam and topology analysis](../../notes/positive_conway_geometric_incidence.md) makes this obstruction explicit. Every final product closure forces three of the formal volume atoms to be flat. Moreover, the turned pure-run subfamily is an iterated meridian-insertion link: an exhibited punctured disk gives an annulus joining distinct cusp tori, excluding a complete finite-volume hyperbolic metric. These are source and topological facts, not deductions from a small quantum invariant. A broader comparison must first reduce the flat seams and state the appropriate topological restrictions.
