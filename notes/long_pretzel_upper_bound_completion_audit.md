# Completion audit of the original-source upper-bound milestone

**Historical intermediate audit.** The user correctly clarified that
the objective is full hyperbolic-volume equality. That equality is now
proved for the same class by the subsequent geometric completion and
recorded in the [full equality audit](long_pretzel_volume_equality_completion_audit.md).
The upper-bound audit below is retained as a proof dependency, not as
a substitute for the equality objective.

29 October 2026. The milestone was to prove geometric survival OR a
sharp hyperbolic-volume bound for the full original source across a
broad class. The [assembled theorem](actual_long_pretzel_sharp_volume_upper_bound.md)
meets the upper-bound alternative. Full volume-conjecture equality is
not part of this completion claim.

For every fixed odd s>=25 there exists p_s such that, for independently
chosen fixed signed integers |p_i|>=p_s, the original pretzel diagram
with boxes R^(-(2p_i+1)) satisfies, if its knot complement is hyperbolic,

    lim_N (2pi/N)log|<K>_N|=Vol(rho_p)<=Vol(S^3 minus K).

The limit uses the original normalized Kashaev invariant. Both level
parities and composite levels are included. The width is unbounded
over the class but fixed before N tends to infinity. The slopes are
also fixed before that limit; their signs and relative magnitudes are
independent. There is no claim of a uniform simultaneous width/level
limit, of short-slope coverage, or of all-knot coverage.

## Proof dependencies

| Required step | Certificate and scope |
| --- | --- |
| Full original finite source and normalization | [Whole-source theorem](actual_long_pretzel_full_source_survival.md), with all colors, Cartan factors, half weights and marked derivatives. The reduced invariant has the raw source's absolute value; the optional full modified convention keeps its factor i^(N+3)/N. |
| Global control away from the cusp corridor | [Global alias and color gap](actual_pretzel_global_alias_and_colored_source_gap.md), including ordinary colors, the even middle color and every normal term. The explicit strict width inequality holds for all odd s>=25. |
| Exact complex packet and coherent Fourier filling | [Analytic color packet](actual_pretzel_exact_analytic_color_packet.md), [endpoint and charge estimates](actual_filling_source_fourier_endpoint_gap.md), and [corridor survival](actual_pretzel_cusp_corridor_filling_survival.md). These retain paired endpoint currents, the exact zero-charge cancellation and summable high-charge tails. |
| Nonzero leading term for the entire source | [Full-source assembly](actual_long_pretzel_full_source_survival.md): the minimal signed charges add, all other terms have a strict gap for each fixed allowed slope tuple, and D_s(p) is nonzero. |
| Representation of the actual diagram | [Local lift](actual_pretzel_mixed_regular_character_lift.md) and [global port theorem](actual_pretzel_port_lift_and_geometric_anchor.md) verify explicit matrices, group relations and every cap in the actual right-to-left composition order. |
| Preferred peripheral coordinates and filled slope | [Mixed longitude certificate](actual_mixed_crossing_circle_preferred_longitude.md): M=H^(-1/2), lambda=-L^(-1), with no unrecorded meridian shear. Commuting regular semisimple matrices satisfy C P^p=+/-I, so the actual primitive slope is killed in PSL2. |
| Absolute orientation and regulator constant | The port theorem matches every white and shaded face at the complete anchor. The [cap-order audit](actual_pretzel_literal_cap_order_audit.md) verifies the holomorphic reversal F(zeta)=rho^2/zeta, including its joint peripheral inversion. The [marked regulator proof](actual_pretzel_marked_regulator_and_filling_action.md) has the same differential and absolute anchor as the developed fundamental chain. |
| Augmented-to-filled representation volume | The marked regulator proof uses the controlled axis-cusp homotopy of the [general peripheral volume proof](general_peripheral_representation_volume_bound.md), then one compatible finite core-plus-solid-torus chain. Both old boundary vertices and new filling vertices use the same invariant axis. |
| Upper bound by the actual filled volume | The [independent representation-volume argument](regular_critical_values_and_representation_volume_bound.md) proves |Vol(rho)|<=Vol(K) by averaging finite regular tetrahedra. It assumes hyperbolicity of K, not faithfulness of rho or a quantum conjecture. |

## Final calibration issues and their resolution

The literal cap traversal is right to left. Generic noncommuting
physical boxes were checked to prevent commutativity of the special
Casimir source from hiding a reversed order. The complete holomorphic
reversal is orientation preserving; it jointly inverts the auxiliary
meridian and longitude. The corresponding filling slope is inverted
as a whole, consistently with the retained pair of signed source charges.

The representation lift is constructive. It verifies the actual
unrotated threaded half-twist group word, the selected peripheral
eigenflag and the caps. It does not infer a canonical state graph from
nodal R eigenphases or use the trace identity symmetric under U inversion
to choose an orientation. No additional unproved U/Ward calibration
enters the theorem.

The regulator chain is the developed fundamental triangulation of the
actual link complement. Its boundary pairing works for the selected
semisimple auxiliary meridians. The separate unipotent five-dilogarithm
coefficient identity is not being extended without proof. The spin
terms cancel only in the full paired regulator, and the complete anchor
fixes the absolute additive constant.

## Verification

The source and geometric arguments received independent analytical
reviews. Fresh primary-agent runs of the four analytic supporting
audits passed; their exact scope is recorded in section4 of the
whole-source theorem. Controlled analytic Gaussian packets in those
scripts calibrate signs and densities; they are not substituted for
proofs of the actual-source uniform estimates.

Fresh final primary-agent replays also passed:

- `audit_actual_pretzel_port_lift_and_geometric_anchor.py`: exact port
  matrices, six reverse-cap families, seven complete white and both
  shaded face families, and twelve signed filling-spin/Hurwitz cases.
- `audit_actual_pretzel_literal_cap_order.py`: seven original marked
  noncommuting tensor families, six full-cap families and six complete
  holomorphic generator/peripheral families.

Independent final reviewers checked the preferred-longitude and local
character-lift audits as well as the signed unequal-slope quantifiers,
the PSL descent, absolute regulator and finite filling-chain argument.
Finite experiments verify identities and conventions; the linked
analytic arguments supply the asymptotic theorem.

## What remains beyond this milestone

The upper inequality does not prove Vol(rho_p)=Vol(K). A positive
geometric filling/completion argument, or another equality proof, is
still needed for the full volume conjecture for this class. General
hyperbolic or alternating knots remain outside the stated theorem.

The user's Cauchy observation is exact: |bv|^2<=(bG^(-1)b^*)(v^*Gv).
For the complete augmented base, [the explicit weighted Fourier metric](actual_pretzel_coherent_circle_and_period_asymptotic.md#8-the-requested-special-inner-product-is-an-explicit-fourier-norm)
has polynomial dual cost, a separately proved sharp geometric energy
and polynomially small normalized overlap. The filled-knot theorem
above instead uses the whole-source asymptotic and its representation
regulator. It does not assert a sharp metric-energy theorem for
arbitrary source words.
