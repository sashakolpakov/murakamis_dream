# Equality results and their scope

The project seeks equality for broad classes of hyperbolic knots, with the right side established as the volume of the actual complement. The results below are research proofs recorded and internally reviewed in this repository. They are not claims of external peer review.

## A full filling theorem with a finite geometric hypothesis

Take a fixed certified simple-white augmented plat and its original marked complete packing. At each crossing region write the four face curvatures as $(x,b,c,y)$; the two protected curvatures stay exactly zero. Put $A=x+y>0$. The [algebraic balance lemma](../../notes/actual_triangle_entropy_algebraic_balance.md) shows that

$$ (A+b)(A+c)\geq\max\{b^2,c^2\} $$

at every region is sufficient for the [full invariant theorem](../../notes/general_complete_radius_balance_filling_volume.md). The stronger test $|b-c|\leq x+y$ is often simpler to check. All regions use the **same actual complete packing**, with one common scale; separately chosen local radii do not give this certificate.

For each such fixed diagram $D$, there is a threshold $T(D)$ so that every independently signed fixed full-twist vector with $|p_i|>T(D)$, and the prescribed knot-producing parity, satisfies

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_D(\mathbf p))|
=\operatorname{Vol}(S^3\setminus K_D(\mathbf p)).$$

The right side is the volume of the actual smooth filled exterior. The twists are fixed before $N$ grows; no bound on their relative sizes is imposed. This theorem does not assert minimal bridge number, a width-only threshold, or that all certified diagrams pass the test.

The sharper hypothesis is $Q_b(0)+Q_c(0)>\log b,\log c$ for the positive middles, where $Q$ is the original triangle action. Its proof follows three steps. The [entire CROSS period](../../notes/general_all_cross_long_filling_volume.md) has the filled-volume rate, with every Fourier charge and endpoint current controlled. The [global LEFT/RIGHT estimate](../../notes/actual_global_left_weighted_spectral_envelope.md) bounds every surviving one-sided factor strictly below its CROSS rate under balance, at all face phases on the same coefficient torus. Finally, integration by parts on the original whole domains makes the full remainder exponentially smaller than the nonzero CROSS contribution.

**The remaining coverage problem is geometric.** We need a proved family of these actual marked packings at every fixed width $k\geq2$, or a replacement for balance that controls the remaining sectors. Numerical packing checks are candidates for that proof, not family theorems.

## Complete signed augmented links at arbitrary width

The [general signed source theorem](../../notes/general_signed_augmented_source_volume.md) covers every fixed connected augmented plat carrying a labeled convex ideal right-angled polyhedron for its actual projection and crossing-disk cut. There is no restriction on bridge width, matching graph, or a Conway grammar. For any fixed pattern of retained half twists $\epsilon_i\in\{0,1,-1\}$, the original marked complete-circle source satisfies

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|A_{D,N}^{\boldsymbol\epsilon}|=2\operatorname{Vol}(Q_D)=\operatorname{Vol}(Y_D^{\boldsymbol\epsilon}).$$

Both level parities and composite levels are included. The proof converts the whole finite source into positive face coefficients, proves a global coefficient saddle and an all-channel upper bound at shared geometric radii, and computes the absolute action by coning the actual facets. A uniform relative estimate from the original continuants then sums the retained phases to a nonzero Gaussian coefficient. Every original scalar, support condition and marked measure remains in the identity. The [untwisted proof](../../notes/general_untwisted_augmented_source_volume.md) remains a shorter entry to the positive argument.

This is a complete augmented-link result, including patterns whose main strands form one component. The separate balance theorem above now supplies independently long fillings under its additional finite geometric condition; unrestricted filling coverage remains open. The theorem also requires the labeled geometric certificate; it does not assert that every reduced plat supplies one. The [coverage comparison](../../notes/general_untwisted_augmented_source_literature_coverage.md) credits earlier overlapping link results and checks the parallel-belt parity obstruction.

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

The [polynomial generating-action theorem](../../notes/actual_matching_edge_polynomial_geometric_action.md) now establishes a general local four-parabolic character relation from the actual selected finite-source polynomial. Its exact operator is retained by the [continuant period formula](../../notes/actual_matching_edge_continuant_operator_period.md). The [rectangle theorem](../../notes/actual_matching_circle_rectangle_bound.md) places every actual certified target at or below $-2$. These results apply beyond a named knot family; they still require a contributing coherent period to yield the general volume equality.


For arbitrary fixed plat width, the [complete source compiler](../../notes/actual_augmented_plat_phase_compiler.md), [all-color compiler](../../notes/actual_mixed_augmented_plat_compiler.md), and [entire Fourier core](../../notes/actual_augmented_plat_entire_core_color_packet.md) now give explicit finite formulas retaining the original phases and normal terms. The [geometric certificate](../../notes/general_augmented_plat_matching_geometry.md) supplies the actual complete complement when a positive labeled realization is available. Neither result alone proves a volume asymptotic for arbitrary plats. The [general long-twist conjecture](../../notes/general_augmented_plat_long_twist_target.md) records the intended broader statement and its remaining source estimates.

For the two ends of one crossing-circle matching edge, the [specialized scalar theorem](../../notes/actual_matching_edge_racah_positive_scalar.md) proves a positive finite formula with polynomial fixed generic derivative costs for every target channel. The complete-circle [marked block identity](../../notes/actual_matching_edge_marked_four_port_block.md) cancels the original row normalization. The [completed-projector formula](../../notes/actual_matching_edge_completed_projector_block.md) cancels the target scalar factor too and retains the full normal through regular paired operators and their first derivatives. These are general local results; the native projector and complementary-network estimates needed for a global volume equality remain open.

The [native-energy estimate](../../notes/actual_matching_edge_native_projector_energy.md) bounds all fixed projector derivatives by a polynomial times explicit magnetic energies, for every physical degree and both parities. An exact simple-channel example proves that these energies can grow exponentially. A sharp bound for their joint contraction, with the original wire constraints, remains necessary.

The [exact Fourier energy theorem](../../notes/actual_matching_edge_magnetic_energy_profile.md) computes the full folded boundary rate: $5v_3/\pi$ for the odd simple projector and the even completed pair, in operator and Hilbert–Schmidt norms. The local physical-degree maximum is retained. This is a boundary-cost theorem; it does not give the original network's volume limit.

The [shrinking-fold extension](../../notes/actual_matching_edge_shrinking_fold_native_energy.md) gives this real norm rate for every sequence $j/N\to1/2$. The [complete-circle shared-cycle source formula](../../notes/actual_matching_graph_shared_cycle_fourier_compiler.md) applies at arbitrary fixed width, with bounded integer flows and the original marked Fourier charge. Its [positive local coefficients](../../notes/actual_q_hahn_fourier_coefficient_variational.md) have a uniform interior variational rate. These results retain the global phase and geometry questions.

The [positive partition theorem](../../notes/actual_matching_graph_positive_fourier_partition.md) gives a polynomial-loss Cauchy upper bound for the complete-circle source with all shared constraints retained. Its sharp geometric rate and a matching lower bound remain unproved; the [radial-frame obstruction](../../notes/actual_positive_fourier_radial_geometric_obstruction.md) limits one proposed direct geometric interpretation.

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
