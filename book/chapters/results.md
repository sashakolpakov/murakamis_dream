# Equality results and their scope

The project seeks equality for broad classes of hyperbolic knots, with the right side established as the volume of the actual complement. The results below are research proofs recorded and internally reviewed in this repository. They are not claims of external peer review.

## Every strict Conway composition tree

The [strict-tree theorem](../../notes/actual_conway_all_strict_tree_long_twist_volume.md)
now covers every fixed literal \(C(FG)\) that passes the finite strict type
test: leaves have type L, turns exchange L/H and preserve A; the nonempty
products are LL/LA/AA→A and HL/HA→H, and the root pair is AA, AL, AH or LH.
Equivalently, each reduced product hub has at most one flagged original
leaf. Mixtures of flagged and unflagged hubs are included.

For each such presentation there is a finite \(B(\tau)\). Every fixed tuple
of independently signed integer weights with \(|n_i|>B(\tau)\) at every
leaf, and loop-free one-component pairing, gives the original invariant's hyperbolic knot
complement volume limit through all levels. The presentation and twists
are fixed before the quantum limit. The auxiliary crossing circles are
filled; the main knot cusp stays unfilled.

The new [positive probe bound](../../notes/actual_conway_unflagged_core_probe_bound.md)
controls each maximal unflagged component at its actual intrinsic
boundary action. The [spectral propagation theorem](../../notes/actual_conway_mixed_core_spectral_propagation.md)
transports every physical-color loss through that component and restores
angular localization. The [geometric adapter](../../notes/actual_conway_unflagged_probe_geometry.md)
proves that these boundary actions sum to the original complete action.
The exact complementary-color identity restores the original packet;
its primitive marked filling action is the actual knot complement volume.

The [pointed quantum A-period corollary](../../notes/actual_conway_pointed_quantum_a_volume.md)
also writes this limit through a genuine all-level ADO operator, its
finite initial data and bounded quantum-parameter jets. Existence of
the operator was already proved from the finite cut-state source.

The remaining general tasks are presentation coverage beyond this strict
literal class and identification of the selected classical main-meridian
geometric factor with the marked regulator module. No
threshold uniform over growing trees or conclusion for arbitrary short
weights is asserted. The earlier completed-root TeX manuscript retains
its stated theorem. The earlier plat, energy, Fourier and torsor approaches remain available as separate routes to broader classes.


## Weighted trees and the manuscript class

The [weighted-tree theorem](../../notes/actual_conway_weighted_tree_long_twist_volume.md)
is an explicit included family: one independent integer weight per vertex,
arbitrary finite branching and unary chains, and its displayed literal
closure. Its complete augmented volume is \(2v_{\mathrm{oct}}(H-1)\).
The knot limit is the separately calibrated filled critical value.

The [manuscript](manuscript.md) proves the completed-root class generated
by \(hh\), \(T(E)\), \(E_1E_2\), \(hE\), \(Eh\). The strict-tree companion
extends this to all strict mixtures. Root stars and isolated \(C(h^s)\),
\(s\ge3\), remain included. The isolated \(C(hh)\) fails the strict root
test and is not added by the new theorem.

![A mixed source component and its positive norm probe; the probe is a comparison used for an estimate, not an added crossing circle.](../figures/mixed-conway-probe.png)

The [prior-source comparison](../../notes/actual_conway_root_star_prior_source_coverage.md)
records the earlier Fourier cancellation and the one-hub all-odd belt
overlap. None of these source identities classifies knot isotopy types.

## A global source upper bound and the classification of its maxima

The [closed-domain majorant theorem](../../notes/research_global_sharp_coefficient_limsup_majorant.md) now bounds every coefficient of the original spectral numerator, uniformly over all real spectra, closed degree boundaries, both level parities and sampled zeros. Its continuous sharp functional is denoted by $H_\delta(q)$. On the **original** shared flow polytope $\mathcal P_D$, define

$$M_D=\max_{q\in\mathcal P_D,\;\boldsymbol\delta\in[0,1/2]^R}
\sum_e H_{\delta_e}(q_e).$$

Each port supplies one, each ordinary face demands one, and the two protected faces demand zero. Polynomially many original degree arrays then give the uniform upper bound

$$\sup_{\boldsymbol\delta}|S_N(\boldsymbol\delta)|\le e^{N(M_D+o(1))}.$$

This is an upper bound for the actual raw shared numerator. It asserts neither equality of rates nor a nonzero lower asymptotic.

On a certified simple-white diagram, the [full-fiber activation theorem](../../notes/research_full_fiber_sharp_boundary_activation.md) excludes every ordinary zero incidence and every diagonal port at a global maximum. The [stationary classification](../../notes/research_full_fiber_sharp_stationary_classification.md) then gives finite common positive ordinary face weights. Each port is complete strict CROSS at $\delta=0$, a strict pole-straddling LEFT/RIGHT branch at $0<\delta<1/2$, or one of at most two marked cap corners. A cap has two protected zero incidences, $0<\nu<1/2$, and equal remaining ordinary weights. Protected zeros are retained throughout. For a maximum restricted to the closed non-CROSS union with value at least $\Phi_D$, the strict middle margin is now automatic by the seam theorem below.

The [CROSS-degree domination and seam theorem](../../notes/research_sharp_cross_degree_domination_and_seam_gap.md) proves $H_\delta(q)\le h(q)$ for every real spectrum whenever both original middle loads are at most $1/2$. Write $q^{\mathrm{geom}}$ for the actual complete endpoint allocation and set

$$a_D=\min_e\{\tfrac12-q^{\mathrm{geom}}_{e,b},\tfrac12-q^{\mathrm{geom}}_{e,c}\}>0,
\qquad \gamma_D=\frac\pi2 a_D^2.$$

Every seam-only flow has sharp entropy at most $\Phi_D-\gamma_D$. The proof uses strong concavity on the actual latent triangle allocations, projected to the original incidence loads. Compactness then gives a uniform strict overload margin for all high-value non-CROSS candidates and a fixed neighborhood of the seams with an absolute source gap.

For independently sufficiently long fixed signed fillings, the **whole seam-neighborhood period**, with all original charges and endpoint currents, is exponentially negligible relative to the nonzero actual filled-volume all-CROSS period:

$$\frac{I_{\mathrm{seam}}}{I_{\mathrm{CROSS}}}=O_{\mathbf p}(e^{-c_DN}),\qquad c_D>0.$$

Both level parities are included. This removes the seam remainder; the macroscopic, strictly overloaded non-CROSS contribution remains open.

The [elementary odd-cycle theorem](../../notes/research_stationary_noncross_main_cycle_obstruction.md) further proves that every non-CROSS port at such a maximum forces an odd four-cycle on the actual port/face incidence graph. Thus a phase-coherent maximum must be entirely complete CROSS. This is a qualitative sign obstruction, not a quantitative cancellation estimate.

![The uniform original-source upper bound, full-fiber stationary classification, forced odd cycles and the remaining absolute volume comparison.](../figures/sharp-source-boundary-classification.png)

The remaining general step is to turn these forced mismatches into an absolute bound at the complete-volume rate. The [flat-cap counterexample](../../notes/research_flat_cap_no_local_exponential_angular_gap.md) explains one limitation: a locally mismatched alternating cap window can retain a polynomial fraction of its positive envelope. Neither $M_D\le\Phi_D$ nor the full general filling-period bound follows from the classification. The previously proved knot families and conditional certificates below remain unchanged.

## Phase cancellation on regular source windows

The [regular-window theorem](../../notes/research_regular_spectral_window_phase_exclusion.md) proves a phase-sensitive estimate for the actual source, with all four incident weights positive at each selected port and strict interior start/stop maxima. Away from its local alignment,

$$|W_N|\le Ce^{-cN}E_N,$$

where $E_N$ is the original positive window envelope. The [positive two-state tail](../../notes/research_positive_eta_word_transfer.md) handles the outer relative phase. The [four-state source identity](../../notes/research_original_one_sided_four_state_transfer.md) and [analytic switch theorem](../../notes/research_analytic_switching_suppression.md) handle a mismatched middle phase while retaining both boundary terms. The unrestricted source includes the direct $i=j$ path; the disjoint regular windows considered in this estimate exclude it explicitly.

The supported boundary cases now have their own exact proofs. With [one outer face protected](../../notes/research_protected_outer_window_phase_exclusion.md), the active transfer becomes scalar and the three supported phases determine alignment. With [one middle face protected](../../notes/research_protected_middle_window_phase_exclusion.md), the initial row is fixed exactly; only a strict regular stop maximum is needed, and finite row reflection gives the protected-output case. Neither result includes two zero weights or a pole-touching maximum.

The [mixed theorem](../../notes/research_mixed_cross_window_cycle_packing.md) also allows whole CROSS coupons between these windows. Their majorant is $C\log^2(N+1)P_{\mathrm{CROSS},N}(L;0)$, with exponential loss away from equality of all supported phases, uniformly over real spectra. Protected zero incidences have no phase. This majorant is distinct from a moving window's positive envelope.

On the original incidence graph, the [fractional cycle-packing criterion](../../notes/research_regular_window_cycle_packing.md) assigns capacities to the certified local losses. Odd $0/\pi$ cycles force a total loss $\kappa>0$, including cycles that pass through CROSS ports. The unchanged shared coefficient satisfies

$$|\text{original window coefficient}|\le C e^{-\kappa N}
\frac{\prod_e\mathcal E_{e,N}(L)}{\prod_f L_f^{t_f(N)}}.$$

This is a conditional rate certificate at arbitrary fixed width. The local capacities must be certified at one common phase threshold, and the positive quotient's rate minus $\kappa$ must be compared with $\Phi_D$. Universal validity of that comparison, compatible phase systems and coverage of the remaining windows are open.

## From coefficient Cauchy to a shared volume inequality

The [new local energy theorem](../../notes/actual_one_sided_relative_spectral_energy.md) controls **every** one-sided coefficient of the actual spectral numerator, uniformly over the full real spectral interval, both level parities and all degree boundaries. Relative to the positive endpoint coefficient $p_N$, it gives

$$\frac1N\log\frac{\sup_\sigma|a_N(q;\sigma)|^2}{p_N(q)}
\le C(q_x,q_y,\tfrac12-q_x-q_y)+o(1).$$

The proof combines an exact weighted Cauchy inequality with an explicit rearrangement of the spectral angle. Its folded angle has the same uniform distribution as the original angle, so the weighted integral is bounded by a terminal complete-triangle integral. It keeps all unused rows and the odd derivative reference; it does not assume a coefficient limit from a weighted limit.

![Weighted Cauchy, a measure-preserving folded angle, and the remaining shared entropy comparison.](../figures/spectral-energy-rearrangement.png)

The [general shared-flow criterion](../../notes/general_endpoint_conditioned_source_energy.md) combines this bound with the earlier one-sided envelope. Write $h$ for the known endpoint coefficient entropy, $g$ for the triangle energy bound above (and $g=h$ on CROSS), and $h_{\mathrm{env}}$ for the earlier envelope, also equal to $h$ on CROSS. On each original feasible flow set

$$h_{\mathrm{sharp}}=\min\{h_{\mathrm{env}},(h+g)/2\}.$$

If the maximum of $\sum_e h_{\mathrm{sharp}}(q_e)$ over the closed non-CROSS shared-flow set is strictly below $\Phi_D$, the full original invariant has the actual filled-volume limit for independently sufficiently long fixed signed twists. This is a **proved sufficient reduction with an explicit finite-dimensional hypothesis**. The universal entropy inequality is still open. The source's face loads are retained throughout; the two terms are evaluated on the same flow, not independently maximized.

The [protected-outer theorem](../../notes/actual_protected_outer_spectral_energy.md) is sharp: with one outer face zero, the optimized relative-energy rate is exactly $C(w,\tfrac12-w,0)$, where $w$ is the outer degree. The general interior bound needs no new local asymptotic conjecture. What remains is the global comparison with the actual hyperbolic volume.

## A general finite cover of the source sectors

The [finite-sector cover theorem](../../notes/general_actual_sector_cover_filling_volume.md) gives the full original filled-volume limit whenever a finite cover of all non-CROSS source strings has strict shared-radius bounds. Each branch keeps genuine CROSS/LEFT/RIGHT labels and uses one common face vector with the original protected zeros. The diagram, half-twist pattern and independently long signed filling parameters remain fixed before the quantum limit.

This strictly extends the [anchored criterion](../../notes/general_anchored_shared_radius_filling_volume.md). On the **same original seventeen-region marked plat**, an exact rational flow proves that one anchored bound exceeds the complete volume rate by more than $0.025$, for every choice of radii. A refined cover with forty branches has a certified gap greater than $0.04$ below that rate. The [separation theorem](../../notes/actual_shared_radius_certificate_separation.md) and its portable verifier establish both inequalities using rational data and explicit interval errors.

![A coarser certificate fails on an actual source, while forty genuine sector branches pass.](../figures/sector-certificate-separation.png)

Complete-packing balance still implies the anchored criterion. The earlier marked five-region example with word $(1,3,2,1,3)$ fails balance but passes six anchored witnesses. We now have two strict extensions of certificate classes, without claiming an inclusion theorem for unmarked knots with arbitrary alternative presentations.

The [undivided-capacity theorem](../../notes/actual_complete_source_cauchy_capacity_gap.md) also identifies why optimizing one positive torus is insufficient: at a strictly unbalanced complete packing, even level-dependent optimal radii lose an exponential factor. The actual coefficient still has the complete volume rate.

The remaining universal target is precise:

$$\inf_{L>0}\left[\sum_e A_{e,\sigma_e}(L)-\sum_f\log L_f\right]<\Phi_D
\quad\text{for each genuine non-CROSS string }\sigma.$$

This condition would finish the full invariant theorem for every certified diagram where it holds. Its validity for all eligible plats remains open. The unrefined anchored condition is now known to be non-universal. Fractional one-sided comparison flows require a global estimate; their pure endpoints and the [fixed-triangle gap](../../notes/actual_fixed_triangle_boundary_capacity_gap.md) do not settle the intermediate mixtures.

## An explicit full-invariant family at every width $k\geq2$

The [one-end layer theorem](../../notes/general_one_end_layer_long_filling_volume.md) proves the volume limit for a family with $3k-3$ independently long signed twist regions, for **every fixed $k\geq2$**. In conventional braid-generator numbering, take the standard plat closure of

$$\left(\prod_{j=1}^{k-1}\sigma_{2j}^{\alpha_j}\right)
\left(\prod_{j=1}^{k-1}\sigma_{2j+1}^{\beta_j}\right)
\left(\prod_{j=1}^{k-1}\sigma_{2j}^{\gamma_j}\right).$$

Choose the first-layer exponents odd and the other two layers even. This gives one knot component. For each fixed width and retained half-twist sign pattern, sufficiently large absolute full-twist parameters, independently chosen and fixed before $N\to\infty$, give

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
=\operatorname{Vol}(S^3\setminus K).$$

The right side is the actual smooth filled hyperbolic volume. Both level parities are included, with no ratio condition between twist magnitudes. The global remainder is bounded by the balance theorem below.

There is also a subfamily with **minimal bridge number exactly $k$**: require every box exponent to be divisible by $3$, keeping the same odd/even pattern. The [Fox-coloring certificate](../../notes/actual_fox_coloring_exact_plat_bridge.md) gives exactly $3^k$ colorings; a $b$-bridge knot has at most $3^b$. This congruence is needed for the bridge lower bound, not for the volume theorem.

The geometric proof is uniform. Reflection of the actual marked packing reduces its contact heights to

$$ (1+z_{j-1})(1-z_j^2)(1+z_{j+1})=1,\qquad z_0=0,\quad z_{k-1}=1. $$

Here the equation holds at the interior indices $1\leq j\leq k-2$. After $v_j=\log(1+z_j)$, strict convexity gives a comparison principle; the right boundary is $v_{k-1}=\log2$ and is never substituted into the singular interior function. Translated copies of the exact three-node seed $(2/3,4/5,2/3)$ prove $z_j\geq2/3$ when $k\geq4$. The cases $k=2,3$ have exact small packings. For $k\geq3$, the final circle occupies its actual bounded tangency gap; $k=2$ uses its explicit three-unit-circle packing. Together these facts give $e_j/(a_{j-1}+a_j)\leq9/4$ at every relevant port, so the [zero-middle lemma](../../notes/actual_zero_middle_nine_quarter_balance.md) proves strict source balance.

![The earlier reduced width-four packing supplies the exact comparison seed.](../figures/symmetric-plat-balance-seed.png)

This proves a family at each $k\geq2$, rather than all $k$-bridge knots. The earlier reduced-layer family at $k\geq4$ is [preserved separately](../../notes/general_reduced_layer_long_filling_volume.md). The wider complete-radius criterion remains available for other diagrams; the unrestricted conjecture remains open.

## Independent tangle depth at every initial bridge gap

The [simultaneous bridge-gap theorem](../../notes/general_simultaneous_bridge_gap_filling_volume.md) permits a separate fixed depth $m_j\geq0$ at every first-layer bridge gap of the one-end core. Replace its zero-based slot $2j-1$ by

$$ (2j-1,2j)^{m_j}(2j-1),\qquad 1\leq j\leq k-1. $$

The later two layers stay in their original order. The resulting family has

$$ R=3k-3+2\sum_{j=1}^{k-1}m_j $$

independently long signed twist regions. For every fixed width, depth vector and prescribed knot-producing half-twist pattern, sufficiently long fixed fillings have the **full original invariant's actual hyperbolic-volume limit**. The threshold may depend on this whole diagram. Taking new exponents even preserves the original knot parity automatically; more general fixed half-twist patterns are allowed when the resulting permutation gives a knot. The mod-$3$ exponent condition again supplies minimal bridge number exactly $k$.

![Exact square-root-curvature transport inside each original bridge gap.](../figures/each-bridge-gap-chain.png)

The geometry is explicit. In each original empty gap between the exterior line and two disks of curvatures $A\leq B$, insert a chain with

$$ \sqrt{C_n}=\sqrt B+n\sqrt A. $$

The original core disks remain fixed, and the gaps have disjoint interiors. The exact original face sweep verifies that simultaneous insertions have precisely these contacts. New ports have largest middle curvature at most $9/4$ times the sum of their outer curvatures, so the proved entropy bound gives balance. The one-end core's increasing side curvatures verify $A\leq B$ uniformly in width. This supplies arbitrary independent tangle depths across the first layer; it does not classify all $k$-bridge knots or arbitrary plat words.

## Arbitrarily many twist regions at each fixed width

The [marked unit-chain theorem](../../notes/general_marked_unit_chain_filling_volume.md) extends any balanced certified core whose first box has zero-based slot $1$, which uses no slot $0$, and whose first cap is marked. Prepend $(1,2)^m$, assigning each new box its own even signed exponent. The original knot parity and marked cap are retained.

In the actual circle packing, the prefix inserts $2m$ unit disks into an empty component between the two marked lines. Every old disk stays fixed. For $m>0$, all new ports satisfy balance and the changed first core port has a larger balance margin. This proves a closure operation for every $m$, without inferring it from a finite list of packings.

![A marked unit chain adds regions while leaving the core packing unchanged.](../figures/marked-unit-chain-extension.png)

Applied to the every-width core above, this gives **$3k-3+2m$ independently long signed twist regions for every fixed $k\geq2$ and $m\geq0$**. Each fixed diagram has the full original invariant's actual filled-volume limit; its threshold may depend on both $k$ and $m$. The mod-$3$ exponent condition again gives minimal bridge number exactly $k$. The added boxes use the first four physical strands. This is a general closure rule, not coverage of arbitrary multilayer plats.

## A full filling theorem with a finite geometric hypothesis

Take a fixed certified simple-white augmented plat and its original marked complete packing. At each crossing region write the four face curvatures as $(x,b,c,y)$; the two protected curvatures stay exactly zero. Put $A=x+y>0$. The [algebraic balance lemma](../../notes/actual_triangle_entropy_algebraic_balance.md) shows that

$$ (A+b)(A+c)\geq\max\{b^2,c^2\} $$

at every region is sufficient for the [full invariant theorem](../../notes/general_complete_radius_balance_filling_volume.md). The stronger test $|b-c|\leq x+y$ is often simpler to check. All regions use the **same actual complete packing**, with one common scale; separately chosen local radii do not give this certificate.

For each such fixed diagram $D$, there is a threshold $T(D)$ so that every independently signed fixed full-twist vector with $|p_i|>T(D)$, and the prescribed knot-producing parity, satisfies

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_D(\mathbf p))|
=\operatorname{Vol}(S^3\setminus K_D(\mathbf p)).$$

The right side is the volume of the actual smooth filled exterior. The twists are fixed before $N$ grows; no bound on their relative sizes is imposed. This theorem does not assert minimal bridge number, a width-only threshold, or that all certified diagrams pass the test.

The sharper hypothesis is $Q_b(0)+Q_c(0)>\log b,\log c$ for the positive middles, where $Q$ is the original triangle action. Its proof follows three steps. The [entire CROSS period](../../notes/general_all_cross_long_filling_volume.md) has the filled-volume rate, with every Fourier charge and endpoint current controlled. The [global LEFT/RIGHT estimate](../../notes/actual_global_left_weighted_spectral_envelope.md) bounds every surviving one-sided factor strictly below its CROSS rate under balance, at all face phases on the same coefficient torus. Finally, integration by parts on the original whole domains makes the full remainder exponentially smaller than the nonzero CROSS contribution.

**Coverage now includes the explicit family above at every $k\geq2$.** Its recurrence proves actual $Q$-balance uniformly via the zero-middle $9/4$ bound; the stronger product test can fail for this family. Extending to general plat diagrams remains open.

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
