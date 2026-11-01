# Proof inputs and verification scope

The manuscript’s first theorem starts with a four-ended tangle consisting of two strands
encircled by an auxiliary crossing circle, then turns the whole box through
a quarter-turn. Call this elementary piece $h$. Stacking two copies gives
the first allowed larger box. An allowed box may then be turned, stacked
with another allowed box, or extended by attaching one elementary piece
above or below it. The final diagram joins two allowed boxes and connects
the exposed endpoints by the specified cylindrical closure.

The word *completed* in the paper names the boxes built by this rule. It
does not mean that their geometric or analytic properties have already
been established. Both final boxes must satisfy the rule. Chapter 1 gives
the endpoint labels, a drawing of the closure, and the finite check that
the filled diagram has exactly one component.

The theorem fixes this entire construction first. It then permits
independently sufficiently large signed filling integers at its auxiliary
circles. The resulting knot stays fixed while the quantum level tends to
infinity. Later notes extend the theorem to the larger strict-tree class;
the first table below records the inputs for this theorem.

The following sources form the written dependency chain. The manuscript
gives their definitions and arguments in a continuous exposition; the
technical notes preserve the detailed calculations and conventions.

| Step | Detailed source | Computational coverage |
| --- | --- | --- |
| Original invariant and normalization | [Crossing calculation](../notes/kashaev_crossing_and_period_lattice.md), [complete-source normalization](../notes/actual_complete_augmented_source_normalization.md) | No replacement for the written invariant comparison |
| Exact finite algebra, support and lattice | [Source composition](../notes/actual_conway_single_leaf_source_composition.md), [full Newton half-twist transport](../notes/actual_odd_conway_newton_transport.md) | Formula and divisibility arguments in the paper; normal directions remain present |
| Strict optimizer and actual augmented-link geometry | [Geometric composition](../notes/actual_conway_single_leaf_geometric_composition.md), [ordered ideal prism](../notes/actual_newton_ideal_prism_and_associativity.md), [bowtie cut](../notes/actual_conway_bowtie_projection_cut.md) | Written incidence, convexity and cusp proofs |
| Whole-source estimates | [Two-leaf block](../notes/actual_conway_uniform_two_leaf_block_alias_gap.md), [single-leaf comparison](../notes/actual_conway_single_leaf_alias_composition.md), [large-cotangent leaf bound](../notes/actual_conway_algebraic_leaf_alias_certificate.md) | Exact certificate suite checks their finite rational inequalities |
| Selected complex packet | [Signed packet](../notes/actual_odd_conway_complex_color_packet.md), [mixed-source recurrence](../notes/actual_pretzel_mixed_inner_source_wkb.md) | Written uniform error estimates; finite checks do not establish them |
| Primitive peripheral action and absolute volume | [Marked deformation](../notes/actual_odd_conway_marked_peripheral_deformation.md), [source-regulator equality](../notes/general_source_regulator_hyperbolic_equality.md) | Written marked gluing and regulator proof |
| Full invariant after long twisting | [Original-source transfer](../notes/general_original_source_long_filling_transfer.md), [assembled composition theorem](../notes/actual_arborescent_single_leaf_long_twist_volume.md) | Written global remainder and nonzero saddle argument |
| Additional isolated seed closures | [Isolated three-leaf case](../notes/actual_conway_isolated_three_leaf_long_twist_volume.md), [two-or-more-leaf theorem](../notes/actual_arborescent_two_leaf_long_twist_volume.md) | Exact block and rational endpoint checks; separate closure geometry remains part of the proof |

All auxiliary crossing-circle cusps are filled in the final knot case.
The main knot cusp stays unfilled. The resulting volume is therefore
the hyperbolic volume of the knot complement, not a closed surgery
manifold and not the starting augmented-link volume.



## The quantitative circle-tree theorem

Chapter 9 gives the explicit criterion
\(\sum_v d_v/(d_v^2+n_v^2)\le2^{-25}\), with one crossing circle at
each junction of the specified ordered tree. The diagram and powers
are fixed, and the strand pairing must give a knot. Appendices E and F
supply its detailed analytic and geometric proofs.

| Step | Written argument | Computational coverage |
| --- | --- | --- |
| Uniform finite-sum estimate and nonzero first charge | [Quantitative analytic proof](../notes/actual_all_circle_curvature_filling_limit.md), [Newton bounds](../notes/all_circle_uniform_newton_bounds.md) | Four symbolic identities; 990 finite complex samples |
| Original exterior and primitive curves | [Ordered octahedral decomposition](../notes/actual_all_circle_octahedral_decomposition.md) | 128 finite trees compared with the literal strand compiler |
| Positive local geometry and signed seam maps | [Angular octahedra](../notes/actual_all_circle_angular_octahedra.md) | 46 rational identities and seven bounds |
| Smooth primitive filling and absolute volume | [Geometric completion](../notes/actual_all_circle_geometric_completion.md) | Local peripheral and regulator algebra; completeness is proved in writing |
| Preferred longitude and cusp | [Cusp continuation](../notes/actual_all_circle_preferred_cusp.md) | Uses the marked representation comparison and original surgery homology |

The command `python3 repro/run_research_checks.py curvature-fillings`
runs all three programs. Their finite checks supplement the uniform
asymptotic and geometric proofs; they are not a test of the conjecture
by extrapolating a list of knots.
