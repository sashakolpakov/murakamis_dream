# Reproducing and reading the audits

## What is being checked

The repository contains written arguments, exact finite algebra audits, numerical diagnostics, and recorded outputs. These are different kinds of evidence.

An exact symbolic identity can verify a stated algebraic step for independent formal variables. A finite-field counterexample can refute a proposed exact identity when the reduction is valid. A successful list of finite levels alone does not prove a uniform asymptotic theorem. Floating-point growth plots need their own error control before they can support a rigorous estimate.

Each technical note specifies its proof and the narrower role of its audit. The archive keeps scripts and result files accessible together.

## Exact transfers supporting the phase estimate

The new analytic phase argument has two focused finite checks:

```sh
python3 experiments/audit_research_original_four_state_transfer.py
python3 experiments/audit_research_regular_spectral_window_phase_exclusion.py
```

The [four-state audit](../../experiments/audit_research_original_four_state_transfer.py) checks 196 recurrence/path comparisons and 85 exact omitted-half scalar identities across ten levels and both parities. The [window audit](../../experiments/audit_research_regular_spectral_window_phase_exclusion.py) checks 402 exact restricted matrix/path identities for half and full rows, including sampled spectral zeros and zero outer weights. Its equality is sign-adjusted on both sides; the common raw sign is established in the source proof.

These validate finite indexing and retained factors. The original physical-matrix interface is inherited from the previously reviewed numerator formula. The positive transfer, analytic gauge, strict boundary gaps and shared-torus phase exclusion are proved analytically and independently reviewed; these finite checks do not prove their exponential estimates or a global volume bound.

## A focused starting set

From the repository root, install the core research dependencies in an environment of your choice:

```sh
python3 -m pip install -r requirements-core.txt
```

These checks cover the current finite source and variational inputs:

```sh
python3 experiments/audit_actual_general_four_port_single_racah_kernel.py
python3 experiments/audit_actual_supported_racah_common_phase_and_normal_metric.py
python3 experiments/audit_actual_four_port_hyperideal_angle_volume.py
python3 experiments/audit_actual_positive_conway_variational_limit.py
```

Read the corresponding result's `scope` field before interpreting `PASS`. There is no assertion that every historical diagnostic forms a single passing application test suite. Some optional geometry checks require SnapPy, Regina, Sage, or other packages listed by the particular script.

The arbitrary-plat advance has a separate focused set:

```sh
python3 experiments/audit_actual_q_hahn_negative_root_source_polynomial.py
python3 experiments/audit_actual_q_hahn_selected_complex_action.py
python3 experiments/audit_actual_q_hahn_uniform_complex_amplitude.py
python3 experiments/audit_actual_q_hahn_magnetic_complex_corridor.py
python3 experiments/audit_actual_q_hahn_joint_accretive_determinant.py
python3 experiments/audit_actual_q_hahn_joint_complex_amplitude.py
python3 experiments/audit_actual_augmented_plat_local_critical_character_map.py
python3 experiments/audit_actual_augmented_plat_endpoint_regulator.py
python3 experiments/audit_actual_augmented_plat_regular_geometric_phase_chart.py
python3 experiments/audit_actual_augmented_plat_channel_hessian.py
python3 experiments/audit_general_marked_multicusp_gluing_rigidity.py
python3 experiments/audit_actual_augmented_plat_critical_scheme.py
python3 experiments/audit_actual_augmented_plat_physical_framing_criterion.py
python3 experiments/audit_actual_augmented_plat_selected_local_certificate.py
python3 experiments/audit_actual_q_hahn_small_channel_generic_normals.py
python3 experiments/audit_actual_q_hahn_partner_normal_collision.py
python3 experiments/audit_actual_q_hahn_physical_partner_normal_bound.py
python3 experiments/audit_actual_q_hahn_near_fold_complex_partner_bound.py
python3 experiments/audit_actual_matching_edge_racah_positive_scalar.py
python3 experiments/audit_actual_matching_edge_marked_four_port_block.py
python3 experiments/audit_actual_matching_edge_completed_projector_block.py
python3 experiments/audit_actual_matching_edge_native_projector_energy.py
python3 experiments/audit_actual_matching_edge_magnetic_energy_profile.py
python3 experiments/audit_actual_native_magnetic_energy_local_geometry.py
python3 experiments/audit_actual_matching_edge_shrinking_fold_native_energy.py
python3 experiments/audit_actual_q_hahn_fourier_coefficient_variational.py
python3 experiments/audit_actual_matching_graph_shared_cycle_fourier_compiler.py
python3 experiments/audit_actual_matching_graph_positive_fourier_partition.py
python3 experiments/audit_actual_positive_fourier_radial_geometric_obstruction.py
python3 experiments/audit_actual_q_hahn_physical_generic_jet_bound.py
python3 experiments/audit_actual_q_hahn_full_physical_complex_packet.py
python3 experiments/audit_actual_augmented_plat_selected_factor_localization.py
python3 experiments/audit_actual_right_angled_selected_framing_obstruction.py
python3 experiments/audit_general_matching_graph_full_normal_source.py
python3 experiments/audit_actual_planar_three_port_reflection_double.py
```

The root, complex-action and amplitude notes contain their analytical proofs; root finding and large-level comparisons are regressions. The magnetic audit also tests the original finite Casimir equation and the exact joint rational formula, retaining the difference between Gaussian and positive sine binomials. The character and regulator audits check exact rational identities in formal variables. The marked gluing audit uses an actual three-cusp triangulation; the critical-scheme audit checks local inverses and 24 incidence graphs. The reflection and graph audits replay actual finite sources. None of these checks proves the missing general global asymptotic.

The joint determinant audit checks the source polynomial before continuation, its three-term recurrence and positive principal minors. The joint amplitude audit compares the literal finite sum with its determinant and asymptotic, including both derivative corrections at folded channels. The framing audit verifies the stated equivalences and local construction; it does not search for or prove a favorable common frame for every plat.

The generic-normal audits compare the original generic columns and derivatives, including the exact large-partner collision tail and nonzero extra-pole residues. The right-angled obstruction audit checks reflection signs, polarization identities and exact two-facet examples. Its general conclusion rests on the separate proof of the literal Morse-prefix dictionary and convex incidence, not on extrapolating those examples.

## The exceptional-period checks

The current period argument has focused audits for the generic Casimir polynomial, its root location and positive endpoint convolution, the actual inverse-turn character relation, and the full resolvent with its normal poles. The strict-prefix and Green-action audits check original matrix entries and selected logarithms. The rectangle audit verifies the actual primitive words for all three half-twist cases. Each note links its script and recorded output.

The endpoint resolvent proof uses a unitary congruence and exact Schur denominator; it does not claim a Hermitian similarity or a polynomial bound for individual spectral projectors. Numerical rate samples supplement the written asymptotic proofs. None of these local or endpoint checks establishes a contributing contour or the general source asymptotic.

## Rebuilding this guide and its figures

The guide is generated from `book/chapters/` and the published notes. Its static HTML uses native MathML and local CSS and JavaScript; reading it requires no account or external math service.

```sh
python3 tools/build_book.py
python3 tools/check_book.py
python3 -m http.server 8000 --directory docs
```

The build requires Pandoc. TikZ sources and their compiled PNG/PDF figures are retained in `book/figures/`. To regenerate the figures, install a TeX distribution with TikZ and the optional Python package PyMuPDF, then run:

```sh
python3 tools/render_figures.py
python3 tools/build_book.py
```

The main README is deliberately short. The long research log, all existing technical note paths, and audit imports are preserved.

The physical paired-normal audit checks the original Casimir entries, weighted Dirichlet identity, double-node reflection and actual generic derivative. Its polynomial estimate is proved on the physical grid; it is not a complex-neighborhood or whole-source theorem.

The near-fold complex audit retains the full large generic source and checks the resonant recurrence on a small complex circle. Its subexponential theorem requires shrinking scaled channel windows. The matching-edge audits reconstruct the actual generic four-port matrices, pivotal signs, root first jets and original row measure. They retain unequal partner derivatives and do not infer a completed positive matrix norm from the scalar formula.

The full physical packet audit tests the new cone determinant, finite boundary zeros, generic matrix lifts and actual amplitudes outside the old central wedge. The physical generic-jet audit retains both forward and backward q recurrences and nonzero higher divided-pair jets. The localization audit checks the exact low/high flag formulas; its general conclusion is the separately reviewed continuation and geometric argument. None establishes a contributing global cycle.

The completed-projector audit independently checks the categorical norm, full generic operator identities, actual cyclic turn, paired cluster jets and complete original-measure cancellation. It retains the nilpotent contribution and unequal scalar derivatives. Its finite checks support the written identities; they do not bound the native projectors or establish a global volume limit.

The native-energy audit checks the actual generic high-degree adapter, dual measures, residue and completed-projector jets, and exact rank-one norms. The exponential midpoint-energy rate has a written Riemann-sum proof; its numerical sequence only illustrates that proof. The theorem retains the energy rather than asserting polynomial projector norms.

The energy-profile audit checks actual Fourier norms, vanished unused nodes, canonical midpoints, both-parity endpoint source formulas and the selected dilogarithm constant. Its even finite full-norm samples concern the nilpotent operator; the completed projector's rate follows from the separate polynomial comparison. The local geometry audit checks original phases, measures, parity factors and all four tetrahedron shapes, without inferring global phase matching.

The shrinking-fold audit checks the actual source formula outside complete support as well as its endpoint and measures. The coefficient audit checks log-concavity, tilted modes, literal complex-radius normalization and interior coefficient rates. The shared-cycle audit compares against original Morse contractions, including the first-failure zeros, both-parity carrier cancellation, exact Kirchhoff support and marked charge. The resulting global Cauchy comparison remains an upper bound.

The positive-partition audit reconstructs the original endpoint and white scalars, the high-degree Chevalley adapter, and full phase-bearing sums before checking their Cauchy bound. The radial-obstruction audit checks the finite phase derivatives, adapters and cup/mark relation; its general geometric conclusion uses the separately proved common-frame obstruction. Neither audit claims a global rate gap or volume equality.


## The full positive endpoint volume theorem

The half-block audit compares the original numerator coefficients, the positive path recurrence, negative roots, exact extreme coefficients, and the finite Lobachevsky formula. Its finite rate profiles remain diagnostics; the uniform closed-domain limit has a written proof.

The earlier shared-source audit checks 228 original coefficients, 4590 support patterns, 748302 affine-cut conditions, 118 one-level support certificates and 236 eventual-flow tests. Those tests remain relevant to fixed half-label patterns. The full-kernel theorem instead uses every degree-$N-1$ monomial, continuous entropy on the full simplex, and unrestricted integral flow rounding. A separate transfer audit checks 39599 Laurent coefficient comparisons and the path injection used in the central corridor.

The [general endpoint theorem](../../notes/general_fejer_endpoint_source_volume.md) now proves the geometric upper bound as well. Its [structural audit](../../experiments/audit_general_fejer_endpoint_source_volume.py) constructs actual Morse faces at widths two, three and four, retains edge identities through genuine identity smoothing, and finds digon disks from the dual graph independently of the Hall subsets. It checks 41 loopless smoothings, 918 hybrid patterns, 121004 Hall cuts, 716 tight sets and 816 independent positive-arc max-flow tests. The general Hall classification, source reduction and volume comparison have separate written proofs.

The [signed-chain audit](../../experiments/audit_actual_fejer_hybrid_piece_representation.py) checks 270 signed cyclic fans, four repeated-contact fans, 24 actual circle/line tangencies, eight contact triangles and two oriented strip chains. These validate the volume formulas; the original group pairings, degree-one relative chain and compatible cut-disk collapse are analytical arguments. The [serial audit](../../experiments/audit_actual_fejer_serial_coupon_bound.py) compares 3960 original physical entries, including 1290 illegal-total zeros, and 3120 independent coefficient bounds for literal powers of the same ordered-pair coupon.

The [odd regularization audit](../../experiments/audit_actual_fejer_odd_regularized_full_numerator.py) checks the original spectral derivative and the positive comparison used for the odd coupon $V_N(-2)-N^{-2}V_N'(-2)$. The resulting whole-source spectral-jet bound is exact at both parities. These are spectral derivatives at the fixed root, not genuine-$q$ normals. Independent proof/code reviews and fresh redirected replays accompany the new results; finite fixtures do not establish a selected Gaussian cycle, a complementary phase estimate or the general filled-knot asymptotic.


## The full spectral numerator packet

The [full packet theorem](../../notes/general_full_spectral_numerator_geometric_packet.md) is an analytical assembly of exact source identities, relative complex cofactor estimates, a global angular gap and the original shared Cauchy coefficient. Its finite tests are scoped to those inputs; samples do not prove the uniform asymptotic or select the later spectral Gaussian contour.

The [factorization note](../../notes/actual_cross_cofactor_factorization.md) compares the central formulas with the original unused-row path polynomial and retains both parity endpoints and the odd central-skipping term. The [interior adapter audit](../../notes/actual_cross_cofactor_interior_packet.md) checks 1056 row-replaced determinants, 352 independently constructed original q-Hahn matrix node values, 352 sine-product scalars and 960 tail factorizations at 85 digits. The analytic proof separately supplies the exponential interpolation error and discrete saddle estimate for all physical starting rows.

The [protected-middle angular audit](../../notes/actual_cross_cofactor_protected_angular_gap.md) checks 4636 coefficient bounds, 486 complex angular inequalities, 432 actual three-step matrix entries and 16 exact monomer cases. The [marked-action audit](../../notes/actual_cross_cofactor_marked_action.md) compares 24 independent source/cofactor integrals, 17 integral derivatives and 12 literal whole Gauss/collar configurations, together with polarization and Gaussian boundary cancellations. Independent fresh replays reproduce those checks.

The protected-middle relative packet, [nodal rigidity](../../notes/actual_cross_cofactor_interpolant_rigidity.md), [global local-angle theorem](../../notes/actual_cross_cofactor_global_angular_gap.md) and whole-source assembly have full independent analytical reviews. The finite Cauchy--Lagrange and original face-torus arguments carry the asymptotic conclusions. The [direct-power scope](../../notes/fixed_root_direct_power_scope.md) retains all fixed-root spectral derivatives while keeping genuine-$q$ normals separate. Those input audits do not establish global charge dominance or the general filled-knot limit. The later localized contribution is proved by the analytical argument below.


## The localized original filling period

The [localized unit-charge theorem](../../notes/general_localized_unit_charge_filling_period.md) has independent full analytical reviews of the original raw marked prefactor, the finite-level action, both determinant branches, and the actual cube translation with every side current retained. Its proof gives a nonzero relative Gaussian coefficient at both level parities. The [charge comparison](../../notes/general_local_charge_critical_monotonicity.md), applied to that same finite action, bounds the other charges in a fixed finite local box.

No new numerical audit is claimed for this analytical consequence. The exact remainder keeps the finitely many selected charges outside the cube and all other charges on their whole original domains; it does not separately sum remote sharp-cube pieces. The proof does not bound this global remainder or establish the general filled-knot volume limit.

## Whole-domain bounds and the balanced full invariant

The new [large-charge audit](../../notes/actual_whole_domain_large_charge_tail.md) checks original operator entries, both signed Gaussian exponents, and paired endpoint currents. The [diagonal-sector audit](../../notes/actual_global_diagonal_spectral_sector_gap.md) includes removable physical nodes, exact path partitions and sewn polynomial integration-by-parts checks. The [CROSS audit](../../notes/actual_global_cross_spectral_gap.md) checks the start decomposition, rescaled transfer matrices and finite characteristic formulas. All three have independent fresh primary-agent replays agreeing with the recorded results. Their finite checks support exact formulas; the uniform bounds come from the separately reviewed written proofs.

The [whole-CROSS period](../../notes/general_all_cross_long_filling_volume.md), [all-angle LEFT envelope](../../notes/actual_global_left_weighted_spectral_envelope.md), and [complete-radius balance theorem](../../notes/general_complete_radius_balance_filling_volume.md) have full analytical internal reviews. The proofs retain entire-domain remote charge sums and endpoint currents, including both level parities. The elementary [entropy lemma](../../notes/actual_triangle_entropy_algebraic_balance.md) checks the absolute half-degree normalization and all protected-zero cases. These arguments prove a full invariant theorem under the stated balance hypothesis. Those conditional arguments alone do not prove realization. The uniform family construction below now supplies it, without treating numerical experiments as a proof.

## Uniform width and exact bridge number

The [family theorem](../../notes/general_one_end_layer_long_filling_volume.md) has full internal analytical reviews of the literal incidences, packing reflection, both recurrence branches, endpoints, and convex comparison. That proof covers every $k\geq2$; finite packing samples do not justify its coverage. The [zero-middle lemma](../../notes/actual_zero_middle_nine_quarter_balance.md) uses an exact rational lower bound independently recomputed. The [Fox certificate](../../notes/actual_fox_coloring_exact_plat_bridge.md) proves the signed crossing identity, invariance, exact plat count and bridge bound directly. No numerical asymptotic or coverage audit is claimed for these proofs.

The two focused family audits supplement these proofs: the reduced-source audit checks 38 literal widths and the rational comparison seed; the one-end-source audit checks 39 literal widths, the changed linear boundary, and all circle contacts and noncontacts in the exact width-two and width-three packings. Primary-agent fresh replays agree with both recorded outputs. These finite checks do not replace the uniform convex comparison.

## Shared-radius certificates beyond complete-packing balance

The [anchored theorem](../../notes/general_anchored_shared_radius_filling_volume.md) has full internal analytical reviews of the common-face Cauchy bounds, both parity partitions, the fixed complex strip and the entire Fourier remainder. Its explicit example uses six stated rational vectors. Arb interval arithmetic evaluates finite Lobachevsky sums with an explicit uniform tail bound; exact algebra checks the original golden-ratio packing. Root and a separate reviewer freshly replayed the audit. The resulting strict inequalities certify this example, not universal coverage of the criterion.

The [fixed-triangle capacity lemma](../../notes/actual_fixed_triangle_boundary_capacity_gap.md) is analytical: closed strong concavity gives the explicit squared-distance loss, and finite convex separation proves the shared dual formula even without attained positive multipliers. It does not assert the same comparison for fractional identity mixtures.

## A structural extension at arbitrary fixed depth

The [unit-chain theorem](../../notes/general_marked_unit_chain_filling_volume.md) proves the literal prefix dictionary and an exact extension into the empty marked gap. Its proof preserves every old disk and checks all added ports analytically; depth is arbitrary. The focused audit checks 56 original source charts and 12 exact small seed extensions, including 1,084 circle/line support pairs. Root and an independent reviewer freshly replayed it. These finite checks support the source dictionary and geometry, while the proof establishes the unbounded-depth statement.

## Simultaneous insertions at every initial bridge gap

The [simultaneous theorem](../../notes/general_simultaneous_bridge_gap_filling_volume.md) has independent full proof/code reviews and redirected exact replays. Its audit checks 413 nonuniform-depth source charts, seven exact symbolic transport/ratio identities, and 25 joint small packings with 2,333 support checks. The analytical proof establishes the general source induction, disjoint-gap construction, curvature order and all port bounds. The extended diagram retains its own full normalization; no equality of its framing scalar with the core's scalar is asserted.


## Refined sector covers and a rigorous obstruction

The [general finite-cover theorem](../../notes/general_actual_sector_cover_filling_volume.md) has independent full analytical and scope reviews. Its source partition and entire Fourier-remainder transfer use the original shared face targets and both level parities.

The [separation verifier](../../experiments/audit_actual_shared_radius_certificate_separation.py) checks that both certificates use exactly the same original seventeen-port source and mark. An 84-variable rational flow rules out one anchored test by more than $0.025$; an 83-variable complete flow and forty rational radius vectors certify the refined cover by more than $0.04$. All face equations are exact, and Arb evaluations include explicit Fourier-series tails. The public scripts contain no numerical optimizer or private diagnostic inputs.

The [undivided positive-capacity obstruction](../../notes/actual_complete_source_cauchy_capacity_gap.md) is analytical. Its proof establishes coercivity, rules out escaping level-dependent radii, and distinguishes the bound's exponential loss from the actual coefficient's correct volume rate. Finite positive-source normalization and the pure-face entropy values were independently reviewed.


## Uniform coefficient energy and rearrangement

The [protected-outer audit](../../experiments/audit_actual_protected_outer_spectral_energy.py) constructs the physical coproduct Casimir and extracts coefficients by the original finite Fourier transform. It verifies both parity reference factors and exact spectral sampling nodes. Symbolic identities and fixed integral checks supplement the analytical uniform boundary proof.

The [general one-sided audit](../../experiments/audit_actual_one_sided_relative_spectral_energy.py) separately verifies the nonnegative parameter expansion, signed-parameter Cauchy inequalities, interior original coefficients, and the rearrangement identities. The uniform transfer estimate and compact finite-tilt argument are proved analytically, rather than inferred from sampled large levels. Independent readers checked the full local theorem and the conditional shared-flow consequence; no audit claims the remaining global entropy inequality.

Four earlier audit consumers now import the physical `Local` class from its defining public module. The lightweight face compiler remains independent of quantum-only imports. Its tensor-contraction helper is now included explicitly and imported by the ten published consumers. The existing small-circle audit replays with results exactly matching its recorded output.
