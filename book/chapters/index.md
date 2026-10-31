# Murakami’s Dream

## Quantum invariants and actual hyperbolic volume

The question driving this project is whether the original quantum invariant of a hyperbolic knot has exponential growth determined by the volume of its complement:

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|=\operatorname{Vol}(S^3\setminus K).$$

We pursue this through the pointed quantum A-structure, exact finite source formulas, positive energies, and hyperbolic angle optimization. The original marked source and peripheral factors stay part of the problem.

The current target allows every fixed bridge width $k\geq2$: start with an essential hyperbolic augmented plat, then put independently sufficiently many signed twists into each designated region. The diagram and twists stay fixed as $N$ grows. The [frontier](frontier.md) separates the exact formulas and geometric certificates already available from the general quantum asymptotic still needed.

**A full-invariant family is now proved at every fixed width $k\geq2$.** The [one-end layer theorem](../../notes/general_one_end_layer_long_filling_volume.md) allows $3k-3$ independently long fixed signed twist regions and gives the actual filled hyperbolic volume. Its congruence subfamilies have minimal bridge number exactly $k$. The wider [balance theorem](../../notes/general_complete_radius_balance_filling_volume.md) applies to every certified diagram satisfying its finite complete-packing condition. The unrestricted conjecture remains open; this construction does not cover all $k$-bridge knots or arbitrary plat diagrams.

The [simultaneous bridge-gap theorem](../../notes/general_simultaneous_bridge_gap_filling_volume.md) now permits a separate depth $m_j$ at every initial bridge gap, giving $3k-3+2\sum_jm_j$ independent twist regions. Exact transport in square-root curvature controls all the added ports. The earlier marked unit-chain extension is its first-gap special case; the full diagram stays fixed during the quantum limit.

The [new coefficient-energy theorem](../../notes/actual_one_sided_relative_spectral_energy.md) now supplies a uniform triangle bound for every one-sided coefficient. Weighted Cauchy and a measure-preserving angle rearrangement reduce the remaining general estimate to an explicit optimization over the original shared face flows. The [combined entropy criterion](../../notes/general_endpoint_conditioned_source_energy.md) gives the full actual-volume limit whenever that optimization has a strict gap; universal validity remains open.

The [finite-sector cover theorem](../../notes/general_actual_sector_cover_filling_volume.md) now permits finer shared-radius bounds on genuine source branches. A rigorously certified seventeen-region example fails the simpler anchored test but passes forty refined branches. The universal question is whether every eligible plat admits strict bounds for all its genuine non-CROSS sectors; that remains open.

![The general route: exact source, local complex amplitudes and a marked geometric branch under a positive gluing certificate; global selection and estimates remain open.](../figures/research-map.png)

## Read the argument in order

The [research library](../library.html) organizes the work by question: equality results, quantum sources, geometry, torsors, Fourier methods, the cube, and the general frontier. Each route gives a main argument, its scope, and supporting notes. The [figure gallery](../figures.md) introduces the main objects visually.

Start with [the equality results](results.md) for the exact knot and link families and their quantifiers. Then read [the mechanism](mechanism.md): what the source formulas do, where weighted Cauchy enters, and why a local scalar estimate does not finish the problem. [The geometry chapter](geometry.md) explains what certifies the volume of the actual complement.

[The current frontier](frontier.md) identifies the remaining general steps. [Notation](notation.md) and [reproducing audits](audits.md) are reference chapters. The searchable archive contains the full technical notes, scripts, and recorded results; it is not a second reading list to complete before understanding the project.

## Where the evidence stands

| Part of the argument | Current scope |
| --- | --- |
| Volume limit of the original invariant | Signed Conway families with mixed seeds $h^s$, $s\geq3$, arbitrary fixed trees and constructible knot patterns, after sufficiently long signed full fillings; isolated $C(h^s)$ for $s\geq4$; specified pretzel and belt-stack families |
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
| General signed long-filled knot equality | Prove the explicit combined entropy gap on original shared flows; uniform local coefficient bounds are now established |

The cube, Fourier, torsor, and alternative approaches are preserved. A failed intermediate estimate is useful evidence about the argument; it is retained beside the corrected scope.

## About this edition

This guide organizes the research snapshot of 31 October 2026. Its chapters explain the current argument; linked technical notes contain the detailed proofs and qualifications. Historical checkpoints remain in the archive and should be read with their dates and later corrections in mind.
