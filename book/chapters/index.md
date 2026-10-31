# Murakami’s Dream

## Quantum invariants and actual hyperbolic volume

The question driving this project is whether the original quantum invariant of a hyperbolic knot has exponential growth determined by the volume of its complement:

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|=\operatorname{Vol}(S^3\setminus K).$$

We pursue this through the pointed quantum A-structure, exact finite source formulas, positive energies, and hyperbolic angle optimization. The original marked source and peripheral factors stay part of the problem.

The current target is a theorem about composing **Conway algebraic, or arborescent, tangles**: fix any admissible finite tangle tree, then put independently sufficiently many signed twists into its designated boxes. The diagram and twists stay fixed as $N$ grows. Bridge number is not the organizing parameter. The right side is the knot complement volume; Dehn filling removes auxiliary crossing-circle cusps and leaves the knot cusp unfilled.

**The latest theorem allows any fixed finite weighted Conway tree with at least two vertices.** Put one integer twist weight at each vertex, retain the [displayed ordered recursion and closure](../../notes/actual_conway_weighted_tree_long_twist_volume.md), and choose parities giving a knot. Independently sufficiently large signed weights then give the original invariant's knot complement volume limit. Branching, valence and unary-chain length are unrestricted; the threshold depends on the fixed tree.

The proof controls the original full Hermite source under each character-decorated turn, then uses an exact complementary-color expansion to control all aliases. Its marked filling action is the actual knot complement volume. [Mixed flagged/unflagged source trees](frontier.md) and universal arborescent presentation coverage remain open.

**The manuscript treats completed products, turns and repeated single-leaf attachments.** The [current theorem](../../notes/actual_arborescent_single_leaf_long_twist_volume.md) starts from $hh$ and allows $T(E)$, $E_1E_2$, $hE$ and $Eh$, closing with two completed children. Any finite number and depth of these operations is allowed. Constructible knot parity patterns and independently sufficiently long fixed signed twists give the knot complement volume, through both level parities and composite levels. The earlier isolated seed closures of width at least three remain included; isolated two-leaf closure remains excluded.

The new estimate combines the attached leaf, its original multiplication gate, and the completed child's output tangent. Joint concavity and exact rational inequalities prove a uniform alias loss that survives further attachments. The original complex packet and primitive peripheral action then give the full invariant limit. The [tangle formulation](../../notes/general_arborescent_tangle_volume_target.md) distinguishes this class from the remaining problem: arbitrary root-leaf closures, turned bare leaves, and coverage of all arborescent presentations. The later [general core theorem](../../notes/actual_conway_general_core_packet_and_gap.md) covers every strict knot pattern, and [marked filling geometry](../../notes/actual_conway_general_mask_marked_filling.md) now covers every strict tree. The remaining general source requirement is the nonempty-alias estimate. A [root-star companion theorem](../../notes/actual_conway_root_star_long_filling_volume.md) proves the full limit for $C(h_0T(h_1\cdots h_s))$, $s\ge2$, including mixed pure/odd leaves. Its [overlap with the earlier belt source](../../notes/actual_conway_root_star_prior_source_coverage.md) is recorded explicitly; no new knot classification is claimed.

The earlier plat constructions, complete-packing certificates, weighted Cauchy estimates, Fourier methods and torsor calculations remain in [the equality results](results.md) and [the frontier](frontier.md). They provide other certified families and approaches to the general problem. The current research theorem does not establish the conjecture for all arborescent or all hyperbolic knots, and its internal reviews are not external peer review.

![The general route: exact source, local complex amplitudes and a marked geometric branch under a positive gluing certificate; global selection and estimates remain open.](../figures/research-map.png)

## Read the argument in order

The [Conway composition manuscript](manuscript.md) gives the current theorem
as a detailed paper, with preliminaries, proofs, illustrations and a
reproducibility suite. A [Sphinx edition](https://sashakolpakov.github.io/murakamis_dream/sphinx/)
provides a second documentation format.

The [research library](../library.html) organizes the work by question: equality results, quantum sources, geometry, torsors, Fourier methods, the cube, and the general frontier. Each route gives a main argument, its scope, and supporting notes. The [figure gallery](../figures.md) introduces the main objects visually.

Start with [the equality results](results.md) for the exact knot and link families and their quantifiers. Then read [the mechanism](mechanism.md): what the source formulas do, where weighted Cauchy enters, and why a local scalar estimate does not finish the problem. [The geometry chapter](geometry.md) explains what certifies the volume of the actual complement.

[The current frontier](frontier.md) identifies the remaining general steps. [Notation](notation.md) and [reproducing audits](audits.md) are reference chapters. The searchable archive contains the full technical notes, scripts, and recorded results; it is not a second reading list to complete before understanding the project.

## Where the evidence stands

| Part of the argument | Current scope |
| --- | --- |
| Volume limit of the original invariant | Every fixed weighted tree in the displayed recursion, with independently long integer weights and knot pairing; also every fixed completed tree generated by $hh$, $T(E)$, $E_1E_2$, $hE$, $Eh$, with two completed children at $C(FG)$; also isolated $C(h^s)$ for $s\ge3$. Knot parity and independently long fixed signed twists give the knot complement volume at both parities and composite levels. |
| Exact finite source identities | Original arbitrary-Casimir-coupon source as one homogeneous face coefficient, including disconnected replacements and both parity carries; the complete-circle positive formula is its special case |
| Boundary first-normal defect | An explicit two-insertion formula from the full root channel; finite Plancherel gives polynomial cost $O(N^2)$, without determining the scalar derivative or estimating that channel by the geometric volume |
| Local quantum action | Selected ordinary amplitude on full physical complex compacts; fixed generic jets for all integer-grid physical columns and divided pairs; subexponential complex paired-normal bounds in shrinking channel windows |
| General geometric branch | Under the labeled certificate, the full spectral numerator selects the marked local action with its boundary flags and primitive peripheral words; the unit-fill critical value is the actual filled volume |
| Common geometric framing | Exactly two prescribed physical-support failures for the certified right-angled cut; every other ordinary factor is on the selected full physical packet, at arbitrary bridge width |
| Exceptional matching block | Exact Casimir polynomial and resolvent period; full complex packet and entire CROSS period with the actual filled-volume rate |
| Whole complete source limit | Every connected certified augmented plat with any retained half-twist pattern, at arbitrary fixed width and both level parities; exact face coefficients, a nonzero signed Gaussian and actual polyhedral volume |
| Complete-image external colors | A nonzero asymptotic on a fixed complex neighborhood; its limiting action is the actual marked geometric regulator, with the necessary complex boundary correction |
| Whole mixed source near completeness | Actual representation-volume limit at any set of untwisted varied ports; joint signed/unsigned corridors under finite shared-radius certificates, including disconnected subsets |
| Positive endpoint source at arbitrary width | Complete augmented-volume limit through all even levels under the labeled certificate; strict loss for nonempty identity insertions; odd regularization has the same full entropy and gives exact spectral-derivative bounds at both parities |
| Full spectral numerator near completeness | A nonzero fixed-complex relative asymptotic on the original shared face torus at both parities, retaining the finite action, normalization and repeated-node data |
| Localized original filling period | A nonzero relative asymptotic on a fixed real cube at both parities, including the finite local charge sector and actual filled-volume rate; independently signed twists are fixed before the level limit |
| Explicit full original invariant at every $k\geq2$ | Three layers, $3k-3$ independent twist regions, actual filled volume, exact-bridge subfamilies |
| Full original long-filled invariant under balance | A global remainder gap and the actual filled-volume limit for every fixed certified diagram passing the complete-radius test |
| Full invariant beyond complete-packing balance | Finite genuine-sector covers; exact examples strictly separate balance, anchored and refined certificates |
| General sharp-source upper problem | Uniform closed-domain coefficient bound; full-fiber maxima have finite common weights and classified branches, with an odd source cycle at every non-CROSS port |
| General arborescent knot equality | Core packets and marked filling geometry cover every strict knot pattern; mixed flagged/unflagged alias control and presentation coverage remain open. Fully flagged trees now have the weighted-tree full-source theorem. |

The cube, Fourier, torsor, and alternative approaches are preserved. A failed intermediate estimate is useful evidence about the argument; it is retained beside the corrected scope.

## About this edition

This guide organizes the research snapshot of 31 October 2026. Its chapters explain the current argument; linked technical notes contain the detailed proofs and qualifications. Historical checkpoints remain in the archive and should be read with their dates and later corrections in mind.
