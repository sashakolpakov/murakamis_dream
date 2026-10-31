# Long-twist volume limits for knots built from tangles

[Read the manuscript (PDF)](build/main.pdf).

The paper proves the volume conjecture for a specified family of arborescent knots with sufficiently many twists in each designated region. Chapter 1 explains the construction geometrically: start with two-strand tangles surrounded by crossing circles, stack and turn the boxes, and join the final endpoints by a cylindrical closure. It then gives the precise recursive rule and the theorem. A native drawing shows the actual endpoint connections.

The theorem fixes the finite construction and a parity pattern giving a knot. It permits independently chosen positive or negative filling integers beyond a construction-dependent threshold. These integers remain fixed while the root-of-unity level tends to infinity. All auxiliary circles are filled; the knot cusp remains unfilled. The conclusion is the volume of that knot complement. The paper does not classify all arborescent knot presentations.

Chapters 2–3 define the finite invariant and derive its angle maximization problem. Chapter 4 constructs the complete augmented hyperbolic metric. Chapters 5–6 control the signed color terms and prove a holomorphic asymptotic for the finite sum. Chapters 7–8 identify the peripheral filling curves and evaluate the full oscillatory filling transform. Detailed algebraic, analytic, geometric and certificate arguments appear in the appendices. Technical terms such as color, source, core, alias and packet are defined in Chapter 1 and again where their formulas are introduced.

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

## Build the illustrated guide

The guide build is separate from the paper build:

```sh
python3 tools/build_book.py
python3 tools/check_book.py
```

The guide is written to `docs/`, with the paper copied to `docs/papers/conway-composition.pdf`. Building it does not execute research scripts. Pandoc converts its mathematical displays to native MathML; the checker verifies the rendered formulas and local links.
