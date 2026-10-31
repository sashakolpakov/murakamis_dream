# Volume equalities: the families and the hypotheses

The results on this page compare a finite quantum invariant with the volume of the knot or link complement that the diagram actually constructs. For a knot $K$, the principal conclusion is

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
=\operatorname{Vol}(S^3\setminus K).
$$

Here $K_N$ is the reduced Kashaev invariant in the normalization fixed in the proof. The knot is held fixed while the positive integer level $N$ grows. The statements below include both even and odd levels unless a smaller scope is explicitly stated.

There are two main ways to specify the proved families. The Conway construction builds a knot from two-strand tangles according to a finite tree. The plat construction starts with a braid and pairs its endpoints. The hypotheses for these constructions are different, so they are described separately. Later sections explain useful conditional theorems and local identities whose conclusions are smaller than a full knot-volume theorem.

## Arbitrarily many tangles with sufficiently long net twists

Fix an ordered construction from two-strand twist boxes, quarter-turns and stacking, followed by the cylindrical closure of a product of two boxes. Each original twist box has its own integer $n_i$. The number of boxes and the depth of their nesting may be arbitrary, but remain fixed in the theorem.

The [net-twist theorem](../../notes/actual_conway_net_twist_volume.md) gives a finite reduction of this construction. It partitions the original boxes into disjoint groups $B_1,\ldots,B_s$ and assigns each surviving box the sum

$$
W_j=\sum_{i\in B_j}n_i.
$$

The groups depend on the written construction, before the integers are chosen. Moving a twist box past another tangle can rotate that tangle through a half-turn. The reduction records these rotations. Thus the ordered output may depend on the parities of the integers, although the groups and their sums do not.

The output is either a strict presentation of the kind described in the next section, or the closure of a single two-strand braid. The second possibility gives a torus link or knot and is excluded from the hyperbolic conclusion. In the first case, there is a finite threshold $B$ depending on the original construction such that

$$
|W_j|>B\qquad(1\le j\le s)
$$

implies the volume equality above whenever the actual closed link is a knot. The reduction and the type of its output are determined before taking a quantum limit. The twist integers are then fixed, and $N$ tends to infinity through all integer levels. The threshold is uniform over the finitely many parity choices; the magnitudes of the different sums need not be comparable.

For example, let $h(c)$ be a quarter-turned box with $c$ half-twists, and consider

$$
C\bigl(R^a h(c)R^b h(d)\bigr).
$$

Here $R^a$ and $R^b$ are integral braid boxes in the same stack. They can be brought together and replaced by $R^{a+b}$. The standard rational box $h(c)$ is preserved by the half-turn needed during this move. The reduced closing expression has one integral box and the two ordinary boxes $h(c),h(d)$, so it passes the strict test. Its size conditions concern $|a+b|$, $|c|$ and $|d|$. Replacing $a,b$ by $a+2m,b-2m$ leaves the knot and the sum $a+b$ unchanged, even though both written magnitudes can become arbitrarily large. This is why the theorem uses net twists.

![Sliding a twist box past a tangle carries a specified half-turn; adjacent integral twist boxes then combine by addition.](../figures/net-twist-reduction.png)

The knot condition concerns all strands, including any circles already closed inside an intermediate box. Checking only the pairing of its four exposed endpoints can miss such a component. The proof retains the component count. A one-component closed link has no internal closed circle, because that circle would remain separate from the component formed by closing the remaining arcs.

The reduction is an ambient isotopy of the filled link. It therefore preserves the reduced invariant at every level and identifies the knot exteriors. Applying the strict theorem to the output supplies a complete hyperbolic metric; pulling that metric back to the original exterior gives exactly the volume in the equality. The argument compares the filled knots. Their auxiliary augmented links need not be the same.

This gives a theorem for arbitrary fixed ordered cylindrical compositions with sufficiently long net twists, subject to the knot condition and the elementary exception. It does not prove the conjecture for every short-twist arborescent knot. The following extension handles cap closures and exact cancellations explicitly.

## Cap closures and exact cancellations

A cap closure joins the two upper endpoints to each other and the two lower endpoints to each other. Write it as $D(E)=C(TE)$. Unlike a cylindrical closure, a cap closure of a stack can split along a sphere meeting the link in two points:

$$
D(FG)=D(F)\mathbin{\#}D(G).
$$

The two pieces are joined along the components containing the cut arcs. If the input is a knot, both pieces must be knots. A zero twist can expose this operation: the quarter-turn of the zero braid is a cup and a cap, so $C(h(0)Q)=D(Q)$.

![Cutting a cap-closed stack along a sphere meeting its two connecting strands gives the specified cap closures of the lower and upper tangles.](../figures/conway-cap-splitting.png)

The [arbitrary-closure theorem](../../notes/actual_conway_arbitrary_closure_volume.md) repeatedly makes these cuts, combines twists, and removes zero sums. It retains all components and all labels. Its terminal factors are strict presentations, two-strand torus braid closures, or explicit unknots. Every surviving strict weight is still a sum of a disjoint group of original integers. The groups can now change when a sum vanishes. There are only finitely many possibilities for a fixed expression, so one threshold covers them all.

Suppose the original knot is hyperbolic and every surviving strict weight exceeds this threshold in absolute value. Then there is exactly one strict factor, and all other factors are unknots. To see why, take a meridian in each nontrivial factor. Both a hyperbolic factor and a torus-knot factor contain another commuting element outside the cyclic meridian subgroup. Two such factors would produce two elements which commute with the common meridian but not with each other. In a complete hyperbolic knot group this is impossible: the centralizer of a nontrivial parabolic consists of commuting translations. A sole torus factor is excluded by its nontrivial center.

Removing the unknot summands now gives an actual isotopy to the long strict knot. This proves the volume equality for the original complement, as well as the same pointed quantum A-period and Gram limits. It is a broader test for presentations of already covered knot types; the analytic theorem for the strict factor is unchanged.

An optional sufficient condition is especially simple. For every nonempty set $B$ of original boxes, require

$$
\sum_{i\in B}n_i=0
\quad\text{or}\quad
\left|\sum_{i\in B}n_i\right|>B_E.
$$

Then every hyperbolic knot from the chosen expression satisfies the volume equality. In particular, for a fixed integer vector $a$, take $n_i=t a_i$. Every nonzero subset sum has magnitude at least $|t|$, so the conclusion applies to the hyperbolic knots obtained when $|t|>B_E$. The integer $t$ is fixed before $N$ grows. A given ray need not contain hyperbolic knots: the terminal factors determine that topological question.

One can also avoid assuming hyperbolicity in advance. Under the longness condition and the one-component test, the input is hyperbolic exactly when the reduction contains one strict factor and all others are unknots. The elementary factors are explicit: $D(R^s)$ is always an unknot, and the knot $C(R^s)$ is an unknot exactly for $s=\pm1$. The proof supplies a finite criterion; it does not supply numerical values for the analytic thresholds.

## Every strict Conway composition tree

Begin with two strands carrying $n_i$ signed half-twists, denoted by $R^{n_i}$. Turn the box through a quarter-turn $T$ to obtain the basic piece $h_i(n_i)=T(R^{n_i})$. The subscript distinguishes the pieces; their integers are independent. Ordered multiplication $FG$ stacks two boxes, and $C(FG)$ is the prescribed cylindrical closure of their remaining endpoints. The endpoint order, the turns and the closing convention are part of the presentation.

The [strict-tree theorem](../../notes/actual_conway_all_strict_tree_long_twist_volume.md) applies to any fixed expression of this form that passes a finite recursive test. The labels in the test describe possible normalized output states of an open box:

| Label | Interval of strict output states |
| --- | --- |
| L | $(0,1/2)$ |
| H | $(1/2,1)$ |
| A | $(0,1)$ |

These state variables belong to the proof; they are not crossing numbers. Every basic piece starts with label L. A quarter-turn exchanges L and H and leaves A unchanged. At a stack, LL, LA and AA give A, while HL and HA give H; either input order is allowed. HH has no strict state. At the final closure the pair must be AA, AL, AH or LH, in either order. The compiler proves that these rules are equivalent to strict feasibility of the state constraints, rather than merely necessary tests.

For example, each stack of two basic pieces has label A, and closing two such stacks passes. Closing only $h_1h_2$ has root pair LL and fails. A failed test says that this theorem does not apply to that presentation; it is not a counterexample to the volume conjecture.

For every passing presentation $\tau$, there is a finite threshold $B(\tau)$. Choose integers with $|n_i|>B(\tau)$, with either sign and with no restriction on their relative sizes. Follow the strands to check that the resulting endpoint pairing has one component and no internal closed component. Then the resulting knot is hyperbolic and has the volume limit above. The entire presentation and every twist integer are fixed before $N$ tends to infinity. The threshold may depend on the whole tree.

The proof uses auxiliary circles around the twist regions. Filling these circles inserts the chosen twists. All auxiliary circles are filled in the knot conclusion; the knot cusp remains unfilled. Thus the right side is the knot complement volume, not the complete augmented-link volume and not the volume of a closed three-manifold.

The estimate for a general tree must preserve cancellation across large internal components. The [positive probe bound](../../notes/actual_conway_unflagged_core_probe_bound.md) controls such a component without changing its coefficient targets. The [spectral propagation theorem](../../notes/actual_conway_mixed_core_spectral_propagation.md) carries strict losses in the physical color variables through it. The [geometric comparison](../../notes/actual_conway_unflagged_probe_geometry.md) identifies the exponential constants with the action of the original cells. These estimates restore the full signed source from its nonzero local geometric contribution.

![A source component and the positive comparison used to estimate it. The probe is part of the proof, not an extra crossing circle in the knot.](../figures/mixed-conway-probe.png)

The [pointed quantum A-period corollary](../../notes/actual_conway_pointed_quantum_a_volume.md) gives an operator formulation of the same result. A genuine recurrence for the ADO invariant, together with finite initial data, selects the knot's solution. At singular steps it retains a bounded number of derivatives in the quantum parameter. The resulting signed scalar period is exactly the Kashaev invariant and therefore has the same volume limit. This is a statement about that selected scalar, not about a matrix norm or a sum of absolute values.

The same corollary applies to the net-twist theorem: the normalized presentation constructs the same knot and hence the same selected invariant. No equality of two presentation-dependent recurrence operators is required.

## Included tree families and the manuscript

The [weighted-tree theorem](../../notes/actual_conway_weighted_tree_long_twist_volume.md) supplies an explicit construction with one independent integer per vertex, arbitrary fixed branching, and chains of vertices. Its literal closure is specified in the theorem. If $H$ is the number of basic pieces and $v_{\mathrm{oct}}$ the volume of a regular ideal octahedron, its complete augmented exterior has volume $2v_{\mathrm{oct}}(H-1)$. The knot volume is the separately calibrated value after filling; it is not replaced by that complete volume.

The [manuscript](manuscript.md) treats an earlier included family. Start with two-piece stacks, then allow turns, stacks of constructed boxes, and the attachment of one basic piece on either side. The technical name “completed box” refers to this recursive class. Close a stack of two such boxes. The paper gives the detailed proof for that class; the strict-tree theorem extends it to all expressions passing the test above.

Isolated closures $C(h_1\cdots h_s)$ with $s\ge3$ and the proved root-star constructions are included in the later results. The isolated two-piece closure $C(h_1h_2)$ is not added as a limiting case: it fails the strict root test. The [prior-source comparison](../../notes/actual_conway_root_star_prior_source_coverage.md) records overlap between root-star formulas, earlier Fourier cancellation, and the all-odd belt calculation. A scalar source identity alone is not a statement that two tangle diagrams are isotopic.

## An explicit full-invariant family at every width $k\geq2$

A $2k$-strand plat is a braid whose top and bottom endpoints are paired in the standard way. The [one-end layer theorem](../../notes/general_one_end_layer_long_filling_volume.md) gives a family with $3k-3$ twist regions for each fixed $k\ge2$. In standard braid notation, where $\sigma_j$ crosses strands $j$ and $j+1$, the word is

$$
\left(\prod_{j=1}^{k-1}\sigma_{2j}^{\alpha_j}\right)
\left(\prod_{j=1}^{k-1}\sigma_{2j+1}^{\beta_j}\right)
\left(\prod_{j=1}^{k-1}\sigma_{2j}^{\gamma_j}\right).
$$

Choose the first-layer exponents odd and the other two layers even. The endpoint pairing then gives a knot. For each fixed width and retained half-twist sign pattern, independently sufficiently large fixed full-twist magnitudes give the full Kashaev volume limit. Both level parities are included, and the twist magnitudes need not be comparable.

There is also a subfamily whose minimal bridge number is exactly $k$. Require every box exponent to be divisible by three, while retaining the odd/even pattern above. The [Fox-coloring certificate](../../notes/actual_fox_coloring_exact_plat_bridge.md) gives $3^k$ colorings, whereas a knot with $b$ bridges has at most $3^b$. This extra congruence proves the bridge lower bound; it is not needed for the volume theorem.

The geometric estimate is uniform in each fixed width. The circle-packing contact parameters satisfy

$$
(1+z_{j-1})(1-z_j^2)(1+z_{j+1})=1,
\qquad z_0=0,\quad z_{k-1}=1,
$$

at the interior indices $1\le j\le k-2$. A convex comparison argument and the exact seed $(2/3,4/5,2/3)$ give the required curvature bounds. The cases $k=2,3$ use their explicit small packings. The [zero-middle balance lemma](../../notes/actual_zero_middle_nine_quarter_balance.md) converts the bound $9/4$ into the source estimate needed for filling. This proves a family at each bridge number, not all knots of that bridge number. The [earlier reduced-layer family](../../notes/general_reduced_layer_long_filling_volume.md) remains a separate special case.

![The width-four packing supplies a comparison seed for the family at arbitrary fixed width.](../figures/symmetric-plat-balance-seed.png)

## Independent tangle depth at every initial bridge gap

The [simultaneous bridge-gap theorem](../../notes/general_simultaneous_bridge_gap_filling_volume.md) permits an independent fixed depth $m_j\ge0$ at each first-layer bridge gap. In the theorem's zero-based slot convention, replace slot $2j-1$ by the alternating word

$$
(2j-1,2j)^{m_j}(2j-1),\qquad 1\le j\le k-1.
$$

The other two layers keep their order. The resulting diagram has

$$R=3k-3+2\sum_{j=1}^{k-1}m_j$$

twist regions. Each gets an independent sufficiently long fixed signed twist. Taking the new exponents even preserves the original knot parity; other parity choices are allowed when the endpoint permutation gives a knot. The threshold can depend on the entire depth vector. The mod-three condition again supplies the exact bridge number.

The inserted circles occupy disjoint empty gaps in the original packing. If the bounding curvatures are $A\le B$, the chain has $\sqrt{C_n}=\sqrt B+n\sqrt A$. The old disks stay fixed, and the same $9/4$ estimate proves balance at the new crossing regions. This explains why the construction works for arbitrary fixed depths, rather than only for a computed list of examples.

![Circle chains inserted independently in the original bridge gaps.](../figures/each-bridge-gap-chain.png)

## Arbitrarily many twist regions at each fixed width

The [marked unit-chain theorem](../../notes/general_marked_unit_chain_filling_volume.md) is another extension operation. Its input is a balanced core whose first box is in zero-based slot 1, with no slot 0, and with the first cap marked. Prepending $(1,2)^m$ adds $2m$ boxes with independent even signed exponents. These boxes use the first four strands and preserve the knot parity.

Geometrically, the operation inserts unit disks into an empty region between the marked lines while leaving every old disk fixed. The new crossing regions satisfy balance, and the changed first region has a larger margin. Applied to the preceding core, this gives $3k-3+2m$ twist regions for every fixed $k\ge2$ and $m\ge0$. The threshold may depend on both parameters. This is a closure rule for the stated cores, not a theorem about arbitrary multilayer plats.

![The unit-chain insertion adds regions while retaining the original core packing.](../figures/marked-unit-chain-extension.png)

## A full filling theorem with a finite geometric hypothesis

For more general plats, a useful sufficient test is available from the complete circle packing. The diagram must carry the labeled convex ideal right-angled geometry used by its crossing-disk cut; “ideal” means that the vertices lie at infinity. The simple-white condition in the technical theorem is a finite condition on the diagram's white-face cellulation.

At a crossing region, denote the four face curvatures by $(x,b,c,y)$ and put $A=x+y>0$. Curvature is the reciprocal radius, with the marked line faces assigned zero. The [algebraic balance lemma](../../notes/actual_triangle_entropy_algebraic_balance.md) shows that

$$ (A+b)(A+c)\ge\max\{b^2,c^2\} $$

at every region is sufficient for the [complete-radius filling theorem](../../notes/general_complete_radius_balance_filling_volume.md). The stronger test $|b-c|\le x+y$ is often easier. Every region must use the same complete packing; choosing unrelated local radii would not establish the hypothesis.

The sharper form compares the triangle actions $Q_b(0)+Q_c(0)$ with $\log b$ and $\log c$ for positive middle curvatures. It is this sharper test, proved by the zero-middle lemma, that covers the explicit every-width family; the simpler product inequality can fail there.

The proof first evaluates the [entire central filling sector](../../notes/general_all_cross_long_filling_volume.md), called the cross sector in the source decomposition. It then uses the [one-sided spectral estimate](../../notes/actual_global_left_weighted_spectral_envelope.md) to bound the complementary left and right sectors below it. All Fourier charges and endpoint terms are retained. Thus every passing fixed diagram has the full volume limit for independently sufficiently long signed twists. Universal validity of the geometric test is not asserted.

## A global source upper bound and the classification of its maxima

The remaining general-plat problem can be formulated on a finite-dimensional space of shared face loads. A *source* here means the exact finite polynomial or tensor expression for the invariant before its indices are summed. Each crossing-region factor supplies total normalized degree one; each ordinary face demands one, while the two marked faces demand zero. These shared constraints define a compact polytope $\mathcal P_D$ for the fixed diagram $D$.

The [closed-domain majorant](../../notes/research_global_sharp_coefficient_limsup_majorant.md) assigns a continuous upper exponential rate $H_\delta(q)$ to a local load $q$ and real spectral parameter $\delta$. With $R$ crossing regions, set

$$M_D=\max_{q\in\mathcal P_D,\;\boldsymbol\delta\in[0,1/2]^R}
\sum_e H_{\delta_e}(q_e).$$

The full shared numerator satisfies $\sup_{\boldsymbol\delta}|S_N(\boldsymbol\delta)|\le e^{N(M_D+o(1))}$, uniformly through both parities and closed degree boundaries. This is an upper bound, not a matching lower asymptotic.

On a diagram satisfying the geometric certificate, [boundary activation](../../notes/research_full_fiber_sharp_boundary_activation.md) and [stationary classification](../../notes/research_full_fiber_sharp_stationary_classification.md) restrict the possible maxima. The central, or cross, sector has both middle loads at most $1/2$. The left and right sectors overload one middle face. The remaining exceptional cap configurations meet the two marked zero faces. Common positive face weights are recovered at a maximum, and there are at most two such caps.

The [seam theorem](../../notes/research_sharp_cross_degree_domination_and_seam_gap.md) controls the boundary between these sectors. Let $\Phi_D$ be the complete geometric rate and let $a_D>0$ be the smallest deficit of a geometric middle load from $1/2$. Every seam-only flow has rate at most $\Phi_D-\gamma_D$, where $\gamma_D=\pi a_D^2/2$. A fixed seam neighborhood has the same kind of absolute gap, and its whole filling period is exponentially smaller than the nonzero cross period for sufficiently long fixed fillings.

Thus a competing non-cross maximum of value at least $\Phi_D$ must have a uniform positive overload. The [odd-cycle theorem](../../notes/research_stationary_noncross_main_cycle_obstruction.md) forces an incompatible phase cycle at such a region. This excludes a fully phase-coherent non-cross maximum, but does not quantify enough cancellation to prove a general volume bound. The [flat-cap example](../../notes/research_flat_cap_no_local_exponential_angular_gap.md) shows why a universal local exponential angular loss is false. Neither $M_D\le\Phi_D$ nor a general filling theorem follows from this classification alone.

![The global upper problem, its stationary classification, and the remaining comparison with the complete-volume rate.](../figures/sharp-source-boundary-classification.png)

## Phase cancellation on regular source windows

A *window* restricts the starting and ending rows of a local finite transfer. The [regular-window theorem](../../notes/research_regular_spectral_window_phase_exclusion.md) proves a strict exponential loss from phase mismatch when the weights are positive and the relevant maxima stay in the interior. The [positive two-state transfer](../../notes/research_positive_eta_word_transfer.md), [four-state identity](../../notes/research_original_one_sided_four_state_transfer.md), and [analytic switching estimate](../../notes/research_analytic_switching_suppression.md) retain the exact boundary terms needed for this conclusion. The direct diagonal path is present in the full source and is excluded only in the specified disjoint windows.

There are separate proofs when [one outer face](../../notes/research_protected_outer_window_phase_exclusion.md) or [one middle face](../../notes/research_protected_middle_window_phase_exclusion.md) is marked and has weight zero. These do not extend to two zero weights or pole-touching maxima. The [mixed-window theorem](../../notes/research_mixed_cross_window_cycle_packing.md) also allows complete cross factors, whose positive endpoint majorant has only logarithmic polynomial cost.

The [fractional cycle-packing criterion](../../notes/research_regular_window_cycle_packing.md) combines compatible local losses on the shared incidence graph. It gives a loss $e^{-\kappa N}$, with $\kappa>0$, relative to the specified positive majorant. To obtain a volume theorem one must still show that the majorant's rate minus $\kappa$ is below $\Phi_D$, and cover all source windows. A positive loss relative to an oversized upper bound is not by itself an absolute volume bound.

## From coefficient Cauchy to a shared volume inequality

The [one-sided energy theorem](../../notes/actual_one_sided_relative_spectral_energy.md) bounds every one-sided coefficient, uniformly over real spectra, degree boundaries and both parities. If $p_N(q)$ is the positive endpoint coefficient, its weighted Cauchy estimate controls the rate of $|a_N(q;\sigma)|^2/p_N(q)$ by a complete-triangle entropy. The proof uses a folded angle with the same distribution as the original angle and keeps all unused rows and the odd derivative reference.

![The weighted Cauchy estimate and the shared entropy comparison that is still needed.](../figures/spectral-energy-rearrangement.png)

The [shared-flow criterion](../../notes/general_endpoint_conditioned_source_energy.md) combines this energy bound $g$ with the endpoint entropy $h$ and an earlier envelope $h_{\mathrm{env}}$. It uses $h_{\mathrm{sharp}}=\min\{h_{\mathrm{env}},(h+g)/2\}$ on each common feasible flow. If the maximum of the sum of these bounds over the closed non-cross set is strictly below $\Phi_D$, the full long-filling theorem follows. This is a sufficient finite-dimensional condition, not a proved universal inequality. The [protected-outer result](../../notes/actual_protected_outer_spectral_energy.md) identifies the sharp local energy there; the unresolved issue is the global comparison with the original shared demands.

## A general finite cover of the source sectors

The [finite-sector cover theorem](../../notes/general_actual_sector_cover_filling_volume.md) proves the full limit whenever finitely many genuine source-sector branches admit strict shared-radius bounds. Each face has one weight wherever it occurs; different branches may use different common weight vectors. This extends the [anchored criterion](../../notes/general_anchored_shared_radius_filling_volume.md).

The extension is strict for a specified seventeen-region marked plat. An exact rational flow makes every anchored bound exceed the geometric rate by more than $0.025$, whereas forty refined branches give a gap greater than $0.04$ below it. The [separation theorem and verifier](../../notes/actual_shared_radius_certificate_separation.md) establish both statements. A five-region example with word $(1,3,2,1,3)$ separately fails balance but passes six anchored witnesses. These compare certificates on fixed presentations; they do not classify all alternative presentations of the same knots.

![A coarse bound fails on the fixed source, while a refined finite cover succeeds.](../figures/sector-certificate-separation.png)

The [undivided-capacity theorem](../../notes/actual_complete_source_cauchy_capacity_gap.md) explains why optimizing a single positive coefficient torus can lose an exponential factor even when the coefficient itself has the correct rate. The remaining general sector question is whether every relevant non-cross string has a strict optimized shared bound below $\Phi_D$. Pure endpoints and the [fixed-triangle boundary gap](../../notes/actual_fixed_triangle_boundary_capacity_gap.md) do not settle fractional mixtures.

## Complete signed augmented links at arbitrary width

An augmented link retains the auxiliary crossing circles rather than filling them. The [signed augmented-source theorem](../../notes/general_signed_augmented_source_volume.md) applies to every fixed connected augmented plat with a labeled convex ideal right-angled polyhedron $Q_D$ realizing its actual cut and face pairings. It allows any fixed retained half-twist pattern $\epsilon_i\in\{0,1,-1\}$ and proves

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|A_{D,N}^{\boldsymbol\epsilon}|
=2\operatorname{Vol}(Q_D)=\operatorname{Vol}(Y_D^{\boldsymbol\epsilon}).$$

Here $A_{D,N}^{\boldsymbol\epsilon}$ is the marked complete-circle source and $Y_D^{\boldsymbol\epsilon}$ the augmented exterior. The proof uses one shared radius per face, a nonzero coefficient saddle, and an explicit summation of the half-twist phases. The [untwisted proof](../../notes/general_untwisted_augmented_source_volume.md) is a shorter introduction to the positive part of this argument. The theorem requires its geometric certificate; it does not supply one for every plat. The [coverage comparison](../../notes/general_untwisted_augmented_source_literature_coverage.md) explains earlier overlaps and the parallel-belt parity obstruction.

## Earlier Conway, pretzel, belt and cap results

The [arbitrary-width seed construction](../../notes/actual_conway_arbitrary_width_seeds.md) began with stacks $A_s=h_1\cdots h_s$, $s\ge3$, and then allowed turns and stacks of already constructed boxes. The [signed Conway filling theorem](../../notes/actual_odd_conway_long_filling_volume.md) proves the volume limit for its specified closures and any subset of independently long auxiliary fillings. Its parity construction supplies knot-producing choices when all auxiliary circles are filled. That earlier theorem excluded the minimal isolated three-piece closure; the later isolated theorem and strict-tree result now include it. This is a change in coverage, not a change in the hypotheses of the older proof.

For the retained-circle diagrams, the [positive Conway theorem](../../notes/actual_positive_conway_hyperbolic_volume.md) constructs the complete complement and identifies the entire positive source rate with its volume. The [coverage comparison](../../notes/positive_conway_literature_coverage.md) records antecedents. The [pure long-filling theorem](../../notes/actual_conway_long_filling_source_limit.md) permits any subset of long auxiliary fillings, but its pure seed diagrams retain internal main components. Full twists cannot join those components; the signed version changes the pairing and requires its own source estimate.

The earlier [long-pretzel width theorem](../../notes/actual_pretzel_all_width_extension.md) and [source-to-volume proof](../../notes/actual_long_pretzel_casson_rivin_equality.md) cover fixed odd widths at least nine and the specified two-component even widths at least ten. Their particular alias estimate does not cover widths three, five and seven. This is a limitation of that proof, not a statement that every smaller presentation lies outside all later results.

The [signed octahedral belt-stack theorem](../../notes/actual_long_filled_octahedral_belt_stack_volume.md) treats every fixed nonempty stack with its prescribed outer crossing power and arbitrary fixed signs. Any subset of auxiliary circles can be filled along independently sufficiently long signed slopes. After all fillings, odd outer power gives knots and even outer power gives two-component links. The [marked theta calculation](../../notes/actual_marked_theta_link_and_angle_geometry.md) supplies a complete augmented-link equality $4v_8$, where $v_8=v_{\mathrm{oct}}$, with a separate sixteen-tetrahedron geometric certificate. Its complete statement alone is not a theorem about arbitrary fillings or arbitrary graphs.

## General identities with a smaller conclusion

Several approaches begin with the local algebra at a crossing-circle edge. The [generating-action theorem](../../notes/actual_matching_edge_polynomial_geometric_action.md), [continuant period](../../notes/actual_matching_edge_continuant_operator_period.md), and [rectangle bound](../../notes/actual_matching_circle_rectangle_bound.md) identify a finite operator, its local character relation and the range of certified geometric targets. A local character relation still needs a contributing global period before it gives the volume of a knot.

For arbitrary fixed plat width, the [complete compiler](../../notes/actual_augmented_plat_phase_compiler.md), [mixed-color compiler](../../notes/actual_mixed_augmented_plat_compiler.md), and [entire Fourier core](../../notes/actual_augmented_plat_entire_core_color_packet.md) retain the finite phases and derivative terms. The [matching geometry](../../notes/general_augmented_plat_matching_geometry.md) supplies the complete complement under a positive labeled realization. The [general plat target](../../notes/general_augmented_plat_long_twist_target.md) states the further source estimate needed for unrestricted coverage.

Recoupling means changing the order in which local representation factors are paired. The [positive scalar formula](../../notes/actual_matching_edge_racah_positive_scalar.md), [marked block identity](../../notes/actual_matching_edge_marked_four_port_block.md), and [completed-projector formula](../../notes/actual_matching_edge_completed_projector_block.md) fix the normalization of those changes and preserve their first normal derivatives. The [native-energy bound](../../notes/actual_matching_edge_native_projector_energy.md) controls the resulting projectors by explicit magnetic energies, which can themselves grow exponentially. The [Fourier energy profile](../../notes/actual_matching_edge_magnetic_energy_profile.md) gives boundary rate $5v_3/\pi$, with $v_3$ the regular ideal tetrahedron volume; the [shrinking-fold theorem](../../notes/actual_matching_edge_shrinking_fold_native_energy.md) extends it to every sequence approaching the fold. These are local costs, not a volume estimate for their full contraction.

The [shared-cycle formula](../../notes/actual_matching_graph_shared_cycle_fourier_compiler.md) preserves bounded integer flows and the marked Fourier charge. Its [positive local coefficient theorem](../../notes/actual_q_hahn_fourier_coefficient_variational.md) gives an interior variational rate. The [positive Fourier partition](../../notes/actual_matching_graph_positive_fourier_partition.md) yields a Cauchy upper bound with shared constraints, but a sharp geometric rate and matching lower bound for that approach remain open. The [radial-frame obstruction](../../notes/actual_positive_fourier_radial_geometric_obstruction.md) explains one failed geometric interpretation.

The [single-Racah recoupling formula](../../notes/actual_general_four_port_single_racah_kernel.md) is an exact local identity. For its supported folded colors, the [hyperideal-volume theorem](../../notes/actual_four_port_hyperideal_angle_volume.md) identifies the metric-normalized scalar rate as the extended tetrahedron volume divided by $\pi$, uniformly through the stated boundary limits. The normalization matters: the bare factorial sum has a different action. This local volume relation is not asserted to be new.

Finally, the [positive Conway variational theorem](../../notes/actual_positive_conway_variational_limit.md) evaluates the whole positive source as twice the maximum of a concave ideal-tetrahedron volume functional on its exact support polytope. Its cylindrical factors have the geometric interpretation described above. Cap products instead have their exhibited connected-sum decomposition and additive limits; they are not assigned one complete hyperbolic metric.

## Cube sectors are kept separate

The cube calculation tests how local geometric contributions behave under sewing. The central odd-level sector and the four-rung sum have the stated geometric rate. In the latter, four rung labels are summed while eight cycle labels remain fixed. The [four-rung theorem](../../notes/actual_cube_four_rung_positive_source.md) and [projected-chain theorem](../../notes/actual_three_port_cauchy_transport_and_cube_kernel.md) retain these restrictions.

![Four blue rung labels are summed; the eight orange cycle labels remain fixed in the proved calculation.](../figures/cube-channels.png)

Removing the cycle restrictions, controlling the full cube invariant and treating its even-level growth remain open in this route. Numerical cube calculations do not establish dominance or cancellation control. The [frontier chapter](frontier.md) explains how these alternatives relate to the current general questions without treating them as missing steps in the strict-tree theorem.
