# Volume limits for arborescent knots

[Read the manuscript (PDF)](build/main.pdf).

The paper proves volume limits for two specified constructions of arborescent knots. Both use ordered stacking and quarter-turns of two-string tangles, with the original crossing circles and disk framings retained. Chapter 1 introduces the diagrams and the theorem scopes; native drawings show the actual endpoint connections.

The first theorem permits independently chosen positive or negative twist numbers beyond a construction-dependent threshold in a recursive tangle construction. For a finite ordered tree with a crossing circle at every vertex, the paper also proves explicit sufficient conditions. Write \(d_v\) for a vertex degree and \(n_v\) for its signed half-twist power. One such condition is

\[
 \sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25}.
\]

A different argument proves the volume identity whenever each vertex satisfies

\[
                d_v\ge2^{28}\qquad\text{or}\qquad |n_v|\ge2^{27}.
\]

Thus \(2^{27}\) half twists suffice independently of the number of tangles. The degree alternative permits any fixed short or zero powers at sufficiently large-degree vertices. The full directed criterion is more flexible than this simple consequence: it assigns a separate decay constant to each subtree and distinguishes the vertex evaluated last. The summed test remains useful, for example when \(|n_v|\ge8192\sqrt E\) on a tree with \(E\) edges.

In every theorem the actual strand connections must give one knot, with no internally closed extra component. The diagram and all integer powers are fixed while the root-of-unity level tends to infinity. The limit is the volume of the original knot complement. Only auxiliary crossing circles are filled; the main knot cusp remains complete.

## Reading the proof

Chapters 2–8 develop the first construction. They define the finite invariant, build the augmented hyperbolic metric, control the signed color terms and analyze the oscillatory filling sum. Appendices A–D supply its detailed algebra, estimates, geometry and rational certificates.

Chapters 9–11 treat the quantitative tree conditions. The geometric construction attaches two octahedra per tree edge in the original order and follows their positive deformation to smooth filling. The quantum argument evaluates a subtree as an exact polynomial, retains its value at zero and estimates the polynomial left on the attaching edge. Chapter 11 proves the stronger directed condition and the bound \(2^{27}\). Appendices E–G and K contain the full finite-sum, geometric and recursive proofs. The separate metric condition \(\sqrt{d_v^2+n_v^2}\ge630\) constructs a hyperbolic metric but does not alone prove a quantum limit.

Chapter 12 identifies the preferred geometric longitude selected by the full asymptotic source. It first treats circle trees, then inserts and fills a zero-power crossing circle at an unmarked product junction. Keeping the based boundary maps proves that this operation recovers the original representation. Appendices H–J give the full-source expansion, algebraic rigidity and junction arguments. The selected geometric factor divides the first nonzero classical symbol of every genuine all-level annihilator in the stated full-source classes. The additional directed cases have their proved volume limit and first-order profile; an all-orders shifted-chart extension is needed before adding them to that factor statement.

Chapter 13 explains reproduction. The linked notes provide separately readable versions of the proofs. The older local numerical condition remains in Chapter 10 as an intermediate theorem, with its improvement stated explicitly.

The [net-twist companion theorem](../notes/actual_conway_net_twist_volume.md) treats a broader class of ordered tangle expressions using exact tangle reductions and the strict-tree estimates. Its hypothesis concerns the combined twist numbers left after reduction. The subsequent [closure theorem](../notes/actual_conway_arbitrary_closure_volume.md) also handles cap closures and exact zero sums under its long-surviving-weight condition. These companion results are described in the [results chapter](../book/chapters/results.md); they are distinct from the construction classes developed in this PDF.

## Build the paper

From the repository root, run:

```sh
python3 tools/build_manuscript.py
```

The result is `manuscript/build/main.pdf`. The build also produces standalone previews of the native TikZ figures and a manifest of the TeX, bibliography and PDF hashes. It requires TeX Live or MacTeX with `latexmk` and the packages listed in `main.tex`. Building the paper does not execute the mathematical certificates.

## Check the finite certificates

Run:

```sh
python3 repro/verify.py --output repro/results
```

The verifier checks the rational supporting inequalities and their exact domain coverage. It does not use numerical optimization or numerical sampling as a proof. See `repro/README.md` and `repro/PROOF_INPUTS.md` for the inputs and the separate role of optional finite audits. The continuum estimates and geometric arguments are proved in the manuscript.

For the quantitative circle-tree result, run:

```sh
python3 repro/run_research_checks.py curvature-fillings
```

This group checks symbolic edge identities, finite complex-parameter bounds, and the labeled octahedron attachments and peripheral words. Its finite computations supplement the uniform estimates and topological proofs; they do not replace them.

For the local condition and its geometric criterion, run:

```sh
python3 repro/run_research_checks.py local-tree-fillings
```

This group checks 29 rational constant margins and 48 finite recursion cases. The finite cases compare the exact subtree evaluation with the corresponding finite contraction. They supplement the analytic induction and geometric completion proved in Chapter 10 and Appendix G.

For the stronger directed condition, run:

~~~sh
python3 repro/run_research_checks.py directed-tree-fillings
~~~

This checks exact rational constant inequalities. The uniform estimates and induction are proved in Appendix K.

For the unmarked-junction formulas, run:

~~~sh
python3 repro/run_research_checks.py strict-tree-geometry
~~~

This requires SymPy and checks the local algebra. The based paths and full representation gluing are proved in Appendix J.

## Build the illustrated guide

The guide build is separate from the paper build:

```sh
python3 tools/build_book.py
python3 tools/check_book.py
```

The guide is written to `docs/`, with the paper copied to `docs/papers/conway-composition.pdf`. Building it does not execute research scripts. Pandoc converts its mathematical displays to native MathML; the checker verifies the rendered formulas and local links.
