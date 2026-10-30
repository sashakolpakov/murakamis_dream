# Murakami’s Dream

## Quantum invariants, geometric volume, and the missing global argument

The question driving this project is whether the original quantum invariant of a hyperbolic knot has exponential growth determined by the volume of its complement:

$$\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|=\operatorname{Vol}(S^3\setminus K).$$

We pursue this through the pointed quantum A-structure, exact finite source formulas, positive energies, and hyperbolic angle optimization. The original marked source and peripheral factors stay part of the problem.

The current target allows every fixed bridge width $k\geq2$: start with an essential hyperbolic augmented plat, then put independently sufficiently many signed twists into each designated region. The diagram and twists stay fixed as $N$ grows. The [frontier](frontier.md) separates the exact formulas and geometric certificates already available from the general quantum asymptotic still needed.

**The general conjecture remains open in this repository.** The notes contain internally reviewed arguments for specified families, general local identities, and obstructions to proposed extensions. Internal proof review, finite checks, and exploratory calculations are distinguished throughout this guide.

![The three parts of the argument: original source, global growth, and actual hyperbolic geometry.](../figures/research-map.png)

## Read the argument in order

The [research library](../library.html) organizes the work by question: equality results, quantum sources, geometry, torsors, Fourier methods, the cube, and the general frontier. Each route gives a main argument, its scope, and supporting notes. The [figure gallery](../figures.md) introduces the main objects visually.

Start with [the equality results](results.md) for the exact knot and link families and their quantifiers. Then read [the mechanism](mechanism.md): what the source formulas do, where weighted Cauchy enters, and why a local scalar estimate does not finish the problem. [The geometry chapter](geometry.md) explains what certifies the volume of the actual complement.

[The current frontier](frontier.md) identifies the remaining general steps. [Notation](notation.md) and [reproducing audits](audits.md) are reference chapters. The searchable archive contains the full technical notes, scripts, and recorded results; it is not a second reading list to complete before understanding the project.

## Where the evidence stands

| Part of the argument | Current scope |
| --- | --- |
| Original invariant equals actual geometric volume | Signed Conway families with mixed seeds $h^s$, $s\geq3$, arbitrary fixed trees and constructible knot patterns, after sufficiently long signed full fillings; isolated $C(h^s)$ for $s\geq4$; specified pretzel and belt-stack families |
| Exact finite source identities | All auxiliary colors at arbitrary fixed plat width; entire Fourier core and Parseval; general four-port recoupling and typed sewing |
| Local quantum-volume law | Uniform supported scalar asymptotic with an actual hyperideal tetrahedron volume |
| Whole positive source limit | Every robust Conway expression; cylindrical factors have actual hyperbolic volume, while cap products split into geometric factors |
| General knot or graph equality | Uniform complex source asymptotics, physical alias bounds and selection of the actual geometric period remain unresolved |

The cube, Fourier, torsor, and alternative approaches are preserved. A failed intermediate estimate is useful evidence about the argument; it is retained beside the corrected scope.

## About this edition

This guide organizes the research snapshot of 30 October 2026. Its chapters explain the current argument; linked technical notes contain the detailed proofs and qualifications. Historical checkpoints remain in the archive and should be read with their dates and later corrections in mind.
