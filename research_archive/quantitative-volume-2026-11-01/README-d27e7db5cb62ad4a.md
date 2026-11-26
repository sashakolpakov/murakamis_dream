# Volume limits for arborescent knots

[Read the manuscript (PDF)](build/main.pdf).

The paper proves volume limits for two specified constructions of arborescent knots. Both use ordered stacking and quarter-turns of two-string tangles, with the original crossing circles and disk framings retained. Chapter 1 introduces the diagrams and the two theorem scopes; native drawings show the actual endpoint connections.

The first theorem permits independently chosen positive or negative twist numbers beyond a construction-dependent threshold in a recursive completed-box construction. The second gives an explicit condition for a finite ordered tree with a crossing circle at every vertex. If a vertex has degree $d_v$ and signed crossing power $n_v$, the condition is

$$
\sum_v\frac{d_v}{d_v^2+n_v^2}\le 2^{-25}.
$$

For a tree with $E$ edges, requiring every $|n_v|\ge8192\sqrt E$ suffices. The same test also permits short or zero powers at sufficiently large-degree vertices. In both theorems the strand pairings must give a knot, and the entire diagram and its integer powers remain fixed while the root-of-unity level tends to infinity. Only the auxiliary circles are filled. The limit is the volume of the original knot complement; the main knot cusp remains complete. Neither theorem classifies all arborescent knot presentations.

Chapters 2–8 prove the first theorem: they define the finite invariant, construct the augmented metric, control signed color terms, identify the primitive filling curves and evaluate the oscillatory filling transform. Chapter 9 develops the quantitative tree theorem. Its geometric construction attaches two octahedra per tree edge in the original cyclic order and follows a positive deformation to smooth filling. It also gives the uniform main-meridian profile of the reduced ADO invariant, retains the exact framing factor, and identifies the first correction with the preferred cusp shape. Chapter 10 explains reproduction. Appendices A–D supply the detailed algebraic, analytic, geometric and rational-certificate arguments for the first theorem. Appendix E contains the complete quantitative finite-sum proof, with the uniform Newton estimates, complex contours and charge-tail bounds. Appendix F contains the full ordered octahedral construction, positive shape calculations, primitive-period completion, volume calibration and preferred-cusp proof. The linked notes provide separately available versions of these arguments.

The [net-twist companion theorem](../notes/actual_conway_net_twist_volume.md) treats a broader class of ordered tangle expressions using exact tangle reductions and the strict-tree estimates. Its hypothesis concerns the combined twist numbers left after reduction. The subsequent [closure theorem](../notes/actual_conway_arbitrary_closure_volume.md) also handles cap closures and exact zero sums under its long-surviving-weight condition. These companion results are described in the [results chapter](../book/chapters/results.md); they are distinct from the two constructions developed in this PDF.

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

## Build the illustrated guide

The guide build is separate from the paper build:

```sh
python3 tools/build_book.py
python3 tools/check_book.py
```

The guide is written to `docs/`, with the paper copied to `docs/papers/conway-composition.pdf`. Building it does not execute research scripts. Pandoc converts its mathematical displays to native MathML; the checker verifies the rendered formulas and local links.
