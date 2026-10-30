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
