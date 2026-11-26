# Independent read of the fixed-complement representation gap

1 November 2026.

Reviewed md-filled-complement-representation-gap.md, SHA256 691a72d69d72ce7d1dcb1823c20f2a0e0513c25682961cd8238d67fcc9379d3e. The principal review concerns §§2–4; I also checked the stated rigidity dependency and the scope of the regular-full-source consequence against the local sources cited below. No source file was edited and no numerical code was used for this review.

## Finite type and flags

For commuting peripheral \(\mathrm{SL}_2(\mathbb C)\) matrices, the two trace-squared-four equations give exactly central matrices or a common noncentral parabolic fixed point. If one matrix is noncentral, its centralizer supplies the common fixed point of the other. There is no additional loxodromic component hidden in these equations.

Finite semialgebraic connected components and piecewise analytic semialgebraic paths are sufficient. On a noncentral interval the common eigenline is semialgebraic and has one-sided limits in the compact projective line. A central interval may use an arbitrary constant flag; matching its flag to both adjacent limits is not required because the canonical volume is independent of the central-end choice. Bounded unitary frame charts avoid any division by an eigenvalue difference.

## Continuity, including a trivial cusp

In the bounded frames, peripheral translations and the real-linear map \(A(t)\) vary continuously and remain bounded. The map
\[
 f_t(w,y)=g(t)^{-1}(A(t)w,y)
\]
is equivariant even when \(A\) has rank one or zero. The hyperbolic metric gives the stated spatial Lipschitz bound. Finite equivariant geodesic interpolation on the fixed truncated core gives a uniform bound there as well, with almost-everywhere spatial derivative continuity. Thus dominated convergence is justified by the finite volume of the original domain.

At a projectively central peripheral endpoint the translation data vanish, hence \(A=0\). A comparison homotopy between two selected ideal directions can be chosen independent of both torus variables. Its boundary three-volume is zero. This proves equality of the adjacent one-sided limits without assuming continuity of a cross-ratio under simultaneous collisions of developed ideal vertices.

These constructions agree with the canonical integral and choice-independence arguments in regular_critical_values_and_representation_volume_bound.md §1 and general_peripheral_representation_volume_bound.md §2.

## Generic auxiliary idealization

After coning the boundary tori and barycentrically subdividing, a small tetrahedron contains at most one original prescribed cusp vertex. Its other vertices have trivial stabilizer in the domain covering action. Positive-dimensional barycenters have this property independently of the image representation; finite ordinary vertices are free as well. The distinct dimensions in a barycentric flag prevent two vertices of the same small tetrahedron from being forced into one auxiliary orbit.

Choose flags for finitely many auxiliary vertex orbits and extend equivariantly. The unwanted pairwise equalities are proper conditions on those choices, so they can be avoided simultaneously. This works for reducible and trivial image representations as well as for irreducible ones. Four distinct developed flags give cross-ratios outside \(0,1,\infty\), and the condition persists on a sufficiently small parameter interval.

The canonical-volume identification does not require positive or embedded tetrahedra. Start with finite auxiliary vertices, use face-compatible straightening and cancellation, and then move the finitely many vertex orbits to the generic ideal flags. The finite bounded tetrahedron-volume limits give the same sum. Artificial vertex links are spheres; true cusp comparison terms have the vanishing flux already established. This is the auxiliary-vertex argument explicitly present in the regular-critical source.

## The differential argument

The Bloch–Wigner differential in (7) has the correct sign for \(v=\operatorname{Log}(1-z^{-1})\). Edge products telescope and peripheral similarities are one, so their real logarithms vanish and their integer imaginary branches are fixed locally. The face/normal-curve cancellation therefore reduces the differential to zero on each true cusp; artificial spherical links add no first-homology term.

The differential conclusion does not need a nearby complete shape point or the positive-shape centering construction in boundary_regulator_period.md. It applies the underlying linear boundary pairing directly to the real logarithms and their tangent variations. Thus the note's use at arbitrary reducible regular idealized charts does not silently import a complete-holonomy hypothesis.

Volume is consequently locally constant on each analytic path piece. The continuity result joins the constants at the finitely many singular endpoints. Finitely many semialgebraic connected components then imply finitely many volume values.

## Rigidity and source scope

The absolute representation-volume bound and its equality characterization are explicitly separate inputs. I checked their use here, not a new proof of their entire natural-map argument. Once those inputs are granted, removing the two maximal oriented geometric values from the finite value set gives the strict gap for this one fixed manifold. Nothing in this reasoning makes the gap uniform over different fillings or diagram sizes.

The source application agrees with regular_critical_values_and_representation_volume_bound.md §4: it retains all head, Gaussian, and cap variables and the actual integer logarithmic marks. The full stationary equations provide the actual knot-group representation, and the calibrated full regulator identity gives its canonical oriented volume. A constrained LEFT/RIGHT coefficient maximum need not satisfy those equations. The note keeps this distinction, and it separately excludes escaping, singular, and unaccounted current contributions from the asserted source consequence.

I found no mathematical defect in §§2–4 or in that dependency and scope separation. This is an independent read of the supplied proof and local dependencies; it is not a new priority claim or an independent verification of every external bibliographic statement.
