# Completion audit: full hyperbolic-volume equality for the original source

29 October 2026. The objective is EQUALITY with the actual hyperbolic
volume. An upper bound alone does not satisfy it. The earlier upper-bound
checkpoint is an intermediate result; this audit concerns the complete
equality on the same broad class.

## 1. Statement and unchanged quantifiers

For each fixed odd integer s>=25 there is P_s such that, for every
independently chosen FIXED signed tuple |p_i|>=P_s, the original pretzel
knot with boxes R^(-(2p_i+1)) has

    lim_(N->infinity) (2pi/N)log|<K>_N|=Vol(S^3 minus K).

The invariant and its cut normalization are the original reduced
Kashaev invariant. Both parities and all composite quantum levels are
included. The slopes may have different signs and arbitrarily different
sizes. The width is unbounded across the class, but both it and the
slopes are fixed before N tends to infinity. The threshold may depend
on the fixed width. No statement for arbitrary knots, short slopes,
or widths/slopes growing with N is included.

The standing hyperbolicity assumption can be retained. In fact the
constructed smooth complete metric proves hyperbolicity in this
sufficiently long range. This strengthening is not needed to reduce
or change the original equality target.

## 2. Requirements and authoritative evidence

| Requirement | Evidence and conclusion |
| --- | --- |
| Briefly audit the essential previous ingredients | Section1 of the [Casson--Rivin equality note](actual_long_pretzel_casson_rivin_equality.md) isolates the unchanged finite source, coherent inner elimination, global color gap, exact complex packet, full endpoint/charge analysis and marked representation regulator. |
| Entire original invariant, rather than a selected formal block | The [whole-source theorem](actual_long_pretzel_full_source_survival.md) proves the full asymptotic with D_s(p)!=0. Its global estimate includes every auxiliary color and normal derivative; original framing factors have the verified modulus. |
| Actual source-selected representation and absolute regulator | The [port theorem](actual_pretzel_port_lift_and_geometric_anchor.md), [preferred longitude](actual_mixed_crossing_circle_preferred_longitude.md) and [marked regulator comparison](actual_pretzel_marked_regulator_and_filling_action.md) give Vsrc=Vol(rho_p) on the original filled topology, with its exact peripheral sign and complete oriented anchor. |
| Positive geometric realization of that representation | Sections2--4 of the [geometric completion proof](actual_long_pretzel_geometric_filling_completion.md) construct24s positive partially ideal tetrahedra from the original two polyhedra. Their equivariant deformation verifies all shared faces, exact edge return, angle winding one, spherical finite-vertex links and nonsingular compact similarity cusp links. |
| Smooth primitive filling, not merely scalar slope holonomy | The [primitive-angle proof](actual_long_pretzel_primitive_filling_angle.md) identifies the actual geometric log periods U=-z, V=-2ell and U+pV=-2pi i m, |m|=1. Bounded finite generator paths and the escaping second fixed point exclude hidden integer log windings before multiplication by p. |
| Complete degree-one geometry with no branched or covered end | Sections2--5 of the [tube proof](long_pretzel_equality_critical_audit.md) use the compact flat log-link to obtain its entire plane development and injective period lattice. The actual epigraph is a full tube; primitive angle2pi completes smoothly. The main cusp remains a full horoball quotient. |
| Casson--Rivin extremal identification | Sections2--5 of the [variational proof](actual_long_pretzel_casson_rivin_equality.md) put the source point inside the actual filled-slope positive angle slice. The coisotropic first variation holds for ALL angle tangents and vanishes by the source equations. Strict concavity makes this the unique global maximum, including over the boundary. |
| Gromov-norm comparison reaches equality | The completed metric is on the actual oriented filled manifold. Applying the independently proved [representation-volume inequality](regular_critical_values_and_representation_volume_bound.md) in both directions between it and the specified hyperbolic metric forces equal volumes. This does not assume that an almost-maximal volume is already maximal. |
| Preserve independently signed long slopes and all levels | The source critical point is holomorphic in all inverse slopes near zero. One fixed geometric neighborhood therefore works whenever max_i|1/p_i| is sufficiently small. No ratio between slopes is bounded. The original all-level asymptotic remains unchanged. |

## 3. The actual equality chain

The completed and variational proofs give

    lim_N (2pi/N)log|<K>_N|
      =Vsrc_s(p)
      =D(beta(rho_p))
      =max_(theta in A_p) V_T(theta)
      =Vol(S^3 minus K).

Here A_p uses the filled rotational constraints
Im(U_i+p_iV_i)=-2pi, not the complete UNFILLED cusp constraints.
At the source point ReU_i+p_iReV_i=0, so for every tangent of A_p,

    dV_T=(1/2)sum_i ReV_i d(ImU_i+p_iImV_i)=0.

The main cusp term is zero because its peripheral image is parabolic.
The negative tetrahedral Hessian is positive definite with determinant1.
Thus the source is the unique constrained maximizer. The separate
primitive tube proof ensures that this maximum is realized on the
actual smoothly filled knot, rather than on a branched local structure.

For the customary all-ideal angle presentation, the prior audited
positive ideal-subdivision input is used. The independent finite-center
metric completion proves the final geometric equality without relying
on that optional all-ideal presentation. These dependencies are not
conflated.

## 4. Verification and limits of the checks

The primary agent read the new positive-core, primitive-period and
compact-log/tube proofs against the existing source, port and regulator
statements. Independent reviewers checked the primitive spin and angle,
the complete tube and its degree, the positive-core construction, and
the Casson--Rivin first variation on arbitrary angle tangents. The
source and geometric thresholds were checked for signed unequal slopes.

A fresh primary-agent run of
`experiments/audit_actual_long_pretzel_primitive_filling_angle.py`
passed its exact spin/angle algebra,120 signed core families,32 small-log
calibrations and5 Fermi metric checks. These checks calibrate formulas;
the uniform proof of smooth completion is in the notes, not inferred
from those finite examples. The previous full-source audits and their
precise analytical scope are recorded in the whole-source theorem and
the earlier upper-bound completion audit.

In particular, the new proof does not rely on any of the following
insufficient substitutes: a scalar killed peripheral word; convergence
of filled volumes to V_s; a positive quantum norm without survival;
an arbitrary topological triangulation; or strict concavity without a
verified source point in the correct constrained angle domain.

The evidence establishes full equality for the class in section1.
The general volume conjecture for arbitrary hyperbolic knots remains
outside this theorem, rather than being declared complete by this audit.
