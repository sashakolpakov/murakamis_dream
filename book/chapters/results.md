# Equality results and their scope

The project seeks equality for broad classes of hyperbolic knots, with the right side established as the volume of the actual complement. The results below are research proofs recorded and internally reviewed in this repository. They are not claims of external peer review.

## Full original-source equalities

The long pretzel argument covers every fixed odd width $s\geq9$, with independently sufficiently large **fixed signed** twist integers in the recorded diagram convention. The corresponding specified single-cut two-component link result holds at fixed even widths $s\geq10$. Width and slopes are fixed before $N$ tends to infinity. Both level parities are retained. Widths $3,5,7$ are outside the present alias estimate.

The proof combines control of the entire quantum source, a nonzero geometric period, and a separate geometric certificate. Its precise statements and conventions are in the [width extension](../../notes/actual_pretzel_all_width_extension.md) and [source-to-volume proof](../../notes/actual_long_pretzel_casson_rivin_equality.md).

Signed octahedral belt stacks provide another complete family. Every fixed nonempty stack, with arbitrary fixed signs and the specified outer crossing power, has an all-level limit equal to its explicitly constructed complete hyperbolic volume. Any subset of the auxiliary circles can then be filled along independently sufficiently long fixed signed integral slopes. Filling every auxiliary circle gives knots for odd outer crossing power and two-component links for even outer crossing power. The [full filling assembly](../../notes/actual_long_filled_octahedral_belt_stack_volume.md) records the diagram, peripheral slopes, and quantifiers.

The signed marked theta link has original-source limit $4v_8$, with a separate sixteen-tetrahedron angle certificate for the actual four-octahedron complement. This is a complete augmented-link result; it does not include arbitrary fillings or arbitrary graphs. See the [theta geometry and equality](../../notes/actual_marked_theta_link_and_angle_geometry.md).

## General identities with a smaller conclusion

The [general four-port theorem](../../notes/actual_general_four_port_single_racah_kernel.md) evaluates actual inverse recoupling coefficients by one finite Racah sum, with the true normalization and normal terms. It is an exact local identity, not a global growth theorem.

For supported folded colors, the [local hyperideal-volume theorem](../../notes/actual_four_port_hyperideal_angle_volume.md) proves

$$\log W_N=\frac{N}{\pi}\operatorname{Vol}_{\mathrm{ext}}(T)+O(\log N),$$

uniformly across the stated color domain, including boundary sequences. The metric-normalized scalar $W_N$ is essential. The bare factorial sum has a different action. Relevant prior coverage is recorded separately; the local volume relationship is not claimed to be new.

For every fixed expression $E$ in the specified positive Conway class, the [whole-source variational theorem](../../notes/actual_positive_conway_variational_limit.md) proves

$$\lim_{N\to\infty}\frac{2\pi}{N}\log Z_{E,N}=2\max_{P_E}V_E.$$

Here $P_E$ is the exact rational support polytope and $V_E$ a concave sum of ideal-tetrahedron volumes. The source limit is proved. Its identification with the complement's global angle problem remains open in general.

## Cube sectors are kept separate

The cube provides a useful test of shared geometric cores and sewing estimates. The central odd-level sector and the four-rung sum have the stated actual geometric rate. The latter sums all four rung labels while keeping eight cycle labels fixed. Projected chains retain analogous restrictions.

![Cube channels: four blue rungs are summed; eight orange cycle edges remain fixed in the proved four-rung packet.](../figures/cube-channels.png)

Removing these cycle projections, controlling the full invariant, and treating even-level cube growth are unresolved. The [four-rung proof](../../notes/actual_cube_four_rung_positive_source.md) and [projected-chain theorem](../../notes/actual_three_port_cauchy_transport_and_cube_kernel.md) preserve those distinctions. The full-cube computations are diagnostics, not a proof of dominance or cancellation control.
