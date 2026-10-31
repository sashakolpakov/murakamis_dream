# Reproducing and reading the audits

## What is being checked

The repository contains written arguments, exact finite algebra audits, numerical diagnostics, and recorded outputs. These are different kinds of evidence.

An exact symbolic identity can verify a stated algebraic step for independent formal variables. A finite-field counterexample can refute a proposed exact identity when the reduction is valid. A successful list of finite levels alone does not prove a uniform asymptotic theorem. Floating-point growth plots need their own error control before they can support a rigorous estimate.

Each technical note specifies its proof and the narrower role of its audit. The archive keeps scripts and result files accessible together.

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
