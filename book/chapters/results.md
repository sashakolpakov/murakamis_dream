# Equality results and their scope

The project seeks equality for broad classes of hyperbolic knots, with the right side established as the volume of the actual complement. The results below are research proofs recorded and internally reviewed in this repository. They are not claims of external peer review.

## Full original-source equalities

The Conway results start with a crossing-circle box, turn it by a quarter turn, and call the resulting piece $h$. Stack $s$ such pieces to form a seed $A_s=h^s$. The [arbitrary-width extension](../../notes/actual_conway_arbitrary_width_seeds.md) allows every fixed $s\geq3$, including mixtures of widths. Build larger tangles by stacking previously built tangles or rotating them by a quarter turn $R$, retaining every auxiliary crossing circle. The grammar $E::=A_s\mid RE\mid EE$ records those operations. A cylindrical closure joins corresponding top and bottom endpoints around the outside; cap closure instead pairs endpoints on each end.

The [signed Conway filling theorem](../../notes/actual_odd_conway_long_filling_volume.md) now gives a knot and link result across arbitrary finite branching and turn depth. Take a cylindrical closure $C(FG)$ with both children robust. Independently retain a positive half twist, a negative half twist, or no half twist at every leaf, then fill any subset of crossing circles with sufficiently long fixed signed integral full twists. The full original invariant satisfies

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(L)|=\operatorname{Vol}(S^3\setminus L).$$

For **every such expression**, a constructive parity assignment joins the main strands into one component; filling every auxiliary circle then gives knots. Both level parities and composite levels are included. No fixed diagram width is imposed, but the diagram and slopes remain fixed before the limit. The width extension also covers isolated closures $C(h^s)$ for $s\geq4$. The minimal $C(h^3)$ remains excluded from this mixed-color filling theorem. The result does not identify the grammar with all alternating or all arborescent knots.

The proof keeps the entire changed source, including the aliases introduced by half twists. Its selected action is the calibrated primitive of the actual marked peripheral branch, and the filling equation uses the primitive meridian of the changed link. This establishes the volume of the intended filled complement.

The [cylindrical positive Conway theorem](../../notes/actual_positive_conway_hyperbolic_volume.md) covers arbitrary finite branching and turn depth in this grammar. After the exact cap-sum boundary reduction, every retained cylindrical factor has a complete hyperbolic complement and

$$\lim_{N\to\infty}\frac{2\pi}{N}\log Z_{E,N}
=2\max_{P_E}V_E=\operatorname{Vol}(S^3\setminus L_E).$$

This uses the whole original source at both parities and composite levels. Its geometric proof constructs the actual link complement from ideal pyramids and prisms and verifies complete cusps. These are retained-circle links. The long-filling extension is stated below; arbitrary short fillings and coverage of every alternating link are not asserted. The [coverage comparison](../../notes/positive_conway_literature_coverage.md) records relevant antecedents without substituting external proofs.

The long pretzel argument covers every fixed odd width $s\geq9$, with independently sufficiently large **fixed signed** twist integers in the recorded diagram convention. The corresponding specified single-cut two-component link result holds at fixed even widths $s\geq10$. Width and slopes are fixed before $N$ tends to infinity. Both level parities are retained. Widths $3,5,7$ are outside the present alias estimate.

The proof combines control of the entire quantum source, a nonzero geometric period, and a separate geometric certificate. Its precise statements and conventions are in the [width extension](../../notes/actual_pretzel_all_width_extension.md) and [source-to-volume proof](../../notes/actual_long_pretzel_casson_rivin_equality.md).

Signed octahedral belt stacks provide another complete family. Every fixed nonempty stack, with arbitrary fixed signs and the specified outer crossing power, has an all-level limit equal to its explicitly constructed complete hyperbolic volume. Any subset of the auxiliary circles can then be filled along independently sufficiently long fixed signed integral slopes. Filling every auxiliary circle gives knots for odd outer crossing power and two-component links for even outer crossing power. The [full filling assembly](../../notes/actual_long_filled_octahedral_belt_stack_volume.md) records the diagram, peripheral slopes, and quantifiers.

The signed marked theta link has original-source limit $4v_8$, with a separate sixteen-tetrahedron angle certificate for the actual four-octahedron complement. This is a complete augmented-link result; it does not include arbitrary fillings or arbitrary graphs. See the [theta geometry and equality](../../notes/actual_marked_theta_link_and_angle_geometry.md).

## Long fillings of the Conway links

For every retained cylindrical robust Conway factor, the [long-filling theorem](../../notes/actual_conway_long_filling_source_limit.md) proves the full original-invariant limit equals the actual filled hyperbolic volume. Any subset of auxiliary circles may be filled along independently sufficiently long fixed signed integral slopes. Both parities and composite levels are included. The proof controls every source color and constructs the actual marked peripheral representation, including its absolute regulator.

These pure fillings always remain links: each pure seed $h^s$ has $s-1\geq2$ internal main components that full twists cannot join. The signed-coupon theorem above changes the strand pattern and supplies the required new source proof, giving the broader knot subfamily. It does not alter this component obstruction for the pure diagrams.

## General identities with a smaller conclusion

For arbitrary fixed plat width, the [complete source compiler](../../notes/actual_augmented_plat_phase_compiler.md), [all-color compiler](../../notes/actual_mixed_augmented_plat_compiler.md), and [entire Fourier core](../../notes/actual_augmented_plat_entire_core_color_packet.md) now give explicit finite formulas retaining the original phases and normal terms. The [geometric certificate](../../notes/general_augmented_plat_matching_geometry.md) supplies the actual complete complement when a positive labeled realization is available. Neither result alone proves a volume asymptotic for arbitrary plats. The [general long-twist conjecture](../../notes/general_augmented_plat_long_twist_target.md) records the intended broader statement and its remaining source estimates.

For the two ends of one crossing-circle matching edge, the [specialized scalar theorem](../../notes/actual_matching_edge_racah_positive_scalar.md) proves a positive finite formula with polynomial fixed generic derivative costs for every target channel. The complete-circle [marked block identity](../../notes/actual_matching_edge_marked_four_port_block.md) cancels the original row normalization. The [completed-projector formula](../../notes/actual_matching_edge_completed_projector_block.md) cancels the target scalar factor too and retains the full normal through regular paired operators and their first derivatives. These are general local results; the native projector and complementary-network estimates needed for a global volume equality remain open.

The [native-energy estimate](../../notes/actual_matching_edge_native_projector_energy.md) bounds all fixed projector derivatives by a polynomial times explicit magnetic energies, for every physical degree and both parities. An exact simple-channel example proves that these energies can grow exponentially. A sharp bound for their joint contraction, with the original wire constraints, remains necessary.

The [general four-port theorem](../../notes/actual_general_four_port_single_racah_kernel.md) evaluates actual inverse recoupling coefficients by one finite Racah sum, with the true normalization and normal terms. It is an exact local identity, not a global growth theorem.

For supported folded colors, the [local hyperideal-volume theorem](../../notes/actual_four_port_hyperideal_angle_volume.md) proves

$$\log W_N=\frac{N}{\pi}\operatorname{Vol}_{\mathrm{ext}}(T)+O(\log N),$$

uniformly across the stated color domain, including boundary sequences. The metric-normalized scalar $W_N$ is essential. The bare factorial sum has a different action. Relevant prior coverage is recorded separately; the local volume relationship is not claimed to be new.

For every fixed expression $E$ in the specified positive Conway class, the [whole-source variational theorem](../../notes/actual_positive_conway_variational_limit.md) proves

$$\lim_{N\to\infty}\frac{2\pi}{N}\log Z_{E,N}=2\max_{P_E}V_E.$$

Here $P_E$ is the exact rational support polytope and $V_E$ a concave sum of ideal-tetrahedron volumes. The cylindrical factors now have the actual geometric interpretation above. Cap products retain their exhibited connected-sum decomposition, with additive limits; they are not asserted to have one complete hyperbolic metric.

## Cube sectors are kept separate

The cube provides a useful test of shared geometric cores and sewing estimates. The central odd-level sector and the four-rung sum have the stated actual geometric rate. The latter sums all four rung labels while keeping eight cycle labels fixed. Projected chains retain analogous restrictions.

![Cube channels: four blue rungs are summed; eight orange cycle edges remain fixed in the proved four-rung packet.](../figures/cube-channels.png)

Removing these cycle projections, controlling the full invariant, and treating even-level cube growth are unresolved. The [four-rung proof](../../notes/actual_cube_four_rung_positive_source.md) and [projected-chain theorem](../../notes/actual_three_port_cauchy_transport_and_cube_kernel.md) preserve those distinctions. The full-cube computations are diagnostics, not a proof of dominance or cancellation control.
