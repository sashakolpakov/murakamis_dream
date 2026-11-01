# Proof inputs and verification scope

The manuscript proves several sufficient volume criteria and two results
with narrower conclusions. All diagrams, integer twist powers and
construction data are fixed before the level tends to infinity. The
full-invariant limits include both parities and composite levels. The
strand-component test, disk framings and normalization are part of each
statement.

| Result | Written proof in the manuscript | Role of finite checks |
| --- | --- | --- |
| Recursive tangle volume theorem | Chapters 2–8, Appendices A–D | Exact rational certificates are finite parts of the stated estimates. |
| Summed, local and directed circle-tree criteria | Chapters 9–11, Appendices E–G and K | Constant and finite-source checks supplement the analytic induction and geometric completion. |
| Decorated planar volume theorem | Chapter 13, Appendix L | Exact fan, orientation and pairing checks supplement the packing and full-source proof. |
| Preferred longitude and selected recurrence factor | Chapter 12, Appendices H–J; directed extension in Chapter 14 and Appendix M | Local matrix identities are checked; global gluing, all-order asymptotics and algebraic rigidity are proved in the text. The factor conclusion assumes an existing all-level annihilator. |
| Uniform finite filling norm | Appendix N | Finite algebra checks supplement the all-level norm proof. An additional exponential source estimate is needed to deduce a new volume class. |
| Geometric contribution for unchanged matched spheres | Appendix O | The entire Fourier period and actual geometric completion are proved. The complementary signed source is not bounded by this theorem. |

The [introduction](../manuscript/sections/01-introduction.tex) states the
scopes, and the [reproduction chapter](../manuscript/sections/09-reproduction.tex)
explains how to run the checks. The programs do not formally verify the
continuum estimates or prove asymptotics from finite samples.

## The recursive tangle theorem

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
infinity. This construction rule remains the hypothesis of that proof.
The broader [strict-tree source theorem](../notes/actual_main_meridian_filled_volume.md)
and its net-twist and closure corollaries keep their separate hypotheses;
the table below records the inputs for the recursive theorem.

The following sources form the written dependency chain. The manuscript
assembles the argument and incorporates the proofs indicated in its
chapter and appendix map. Named lemmas cited from technical companions
remain dependencies; the PDF does not repeat every calculation in those
companions. A reference to an established lemma and a finite program
checking examples of it have different logical roles.

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
$\sum_v d_v/(d_v^2+n_v^2)\le2^{-25}$, with one crossing circle at
each junction of the specified ordered tree, which has at least one edge. The diagram and powers
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

## The local tree theorem

The complete induction is in
[the local message volume theorem](../notes/actual_all_circle_local_message_volume.md).
The [strip lemma](../notes/exact_tree_messages_and_strip_bounds.md)
proves the exact degree bound and the complex continuation of a real
polynomial envelope. The [geometric criterion](../notes/actual_all_circle_vertexwise_geometry.md)
proves the positive filling path independently of the number of
vertices. The previously established ordered cuts and primitive
completion identify the actual knot complement and its volume.

The group local-tree-fillings runs the finite comparisons and
recursion examples described in the reproduction guide. Its
21 analytic and eight geometric checks concern numerical constants.
Its 48 high-precision examples compare different finite trace
evaluations; they are not substitutes for the all-tree induction.

The local quantum condition is
$\max_v d_v/(d_v^2+n_v^2)\le2^{-120}$. The separate metric
criterion $\sqrt{d_v^2+n_v^2}\ge630$ does not by itself prove a
quantum limit. Appendix G contains both arguments with this distinction.

## The directed criterion and all-order profile

Chapter 11 and Appendix K prove the
[directed finite criterion](../notes/actual_all_circle_directed_volume.md).
Each subtree leaves an exact polynomial on its attaching edge, with its
own decay bound. The finite inequalities control every conditional
Fourier contribution and all boundary terms relative to the next critical
value. They imply the simple sufficient alternative
$d_v\ge2^{28}$ or $|n_v|\ge2^{27}$ at every vertex, with the
choice made independently at each vertex. They also prove the construction
that attaches even stacks of long odd terminal pieces to an arbitrary
fixed knot-paired circle-tree core. The additions preserve its endpoint
pairing and can change the knot.

The command
`python3 repro/run_research_checks.py directed-tree-fillings`
checks exact rational comparisons for the constants and stated examples.
It does not test all trees or replace the written induction. Chapter 14
and Appendix M prove the expansion to every finite order on the shifted
meridian charts for all directed certificates. This analytic result is
needed for their recurrence-factor consequence; the first-order profile
alone would not suffice.

## The decorated planar theorem

Chapter 13 and Appendix L contain the complete proof of
[balanced terminal decorations](../notes/actual_balanced_terminal_fan_volume.md).
They begin with a simple triangulated sphere and a perfect matching of
its dual, construct the complete packing, and retain the actual ordered
strands and crossing disks. A finite even terminal decoration makes the
required inequalities strict. All original and added crossing circles
are then filled with independently sufficiently long signed powers.
The resulting knot has the full-invariant volume limit. The diagram is
fixed after decoration; this is not an equality for every unchanged core.

`python3 repro/run_research_checks.py balanced-terminal-fans` checks the
fan recurrence, rational balance estimates, oriented subdivision,
matching and face parity, and literal endpoint pairings. The written
proof supplies the packing existence, uniform source bounds, nonzero
Fourier contribution and smooth primitive completion.

## The preferred longitude and recurrence implication

Appendix H proves the all-order source expansion and its polynomial
degree bounds. Appendix I proves the actual preferred-longitude identity
for circle trees by marked representations and algebraic rigidity.
Appendix J treats unmarked product junctions and the stated reductions.
Appendix M supplies the directed all-orders extension. These proofs use
the original knot complement, exact peripheral factors and the selected
geometric branch.

An all-level annihilator here is a fixed nonzero operator in the meridian
shift, with coefficients rational in the quantum and meridian variables,
which annihilates the actual reduced invariant at every sufficiently
large level. For such an operator, the first nonzero classical symbol
contains the selected geometric factor in the stated source classes.
The theorem assumes the operator; it does not prove recurrence existence,
the full A-polynomial identity or equality of recurrence ideals.

The groups `geometric-characteristic` and `strict-tree-geometry` check
local matrix, transport and elimination identities. They do not replace
the global based-path, regularity, spin-sign or all-order arguments.

## Two narrower conclusions

[Appendix N](../manuscript/sections/N-uniform-filling-bound.tex) proves a
level-independent supremum-norm estimate for the exact filling
functionals, including their repeated-root derivatives. The group
`filling-supremum` checks the finite interpolation and original crossing
identities. The application at the end of the appendix is a proved
implication: a strict exponential estimate for the shared full-minus-CROSS
polynomial, together with a nonzero geometric contribution, transfers to
the filled invariant. The appendix does not supply that shared estimate
for a new class.

[Appendix O](../manuscript/sections/O-morse-geometric-contribution.tex)
proves the analytic and geometric statements for the CROSS contribution
of unchanged simple matched spherical diagrams, with their actual cups,
caps, marks and signed fillings. CROSS denotes the specified central
part of each local polynomial recurrence. Its product is a contribution
to the original exact invariant, not a new topological invariant. The
proof keeps both level parities, the entire Fourier period and the
primitive metric completion. Its volume-rate conclusion is for this
contribution; a strict bound on the complementary signed contribution
remains a separate requirement for a full-invariant theorem.
