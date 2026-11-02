# Ordered tangle reductions and long net twists

This paper gives actual ordered tangle isotopies and a terminating reduction before applying a long-filling theorem. A cylindrical product closure has parity-independent net label blocks, with parity-dependent rotations and orders. Allowing cap closures and zero sums gives an explicit tree of componentwise connected sums. Every component and every deleted label block is recorded.

The application imports Theorem 1.1 of *Holomorphic source asymptotics and volume limits for strict Conway compositions*. Only the surviving strict-factor weights must be sufficiently large; the original expression and integer assignment are fixed before the level tends to infinity. The hyperbolic criterion uses the explicit long strict and elementary terminal factors. No general prime decomposition, new estimate for short twists, or quantum connected-sum theorem is claimed.

The finite strict type test is the one in *Stationary profiles of strict Newton trees*, Lemma 2.2 and Theorem 2.5. The reduced invariant normalization is *Finite spectral evaluation and uniform filling bounds*, Theorem 10.1, at levels at least three.

Build locally from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Run the supplementary standard-library checks from the repository root:

```sh
python3 -I papers/conway-reductions/check.py --output /path/to/private-output
```

The wrapper removes any old `summary.json` before checking that assertions are enabled. Its record pins the local mathematical and checker sources. It checks exact spatial rotation matrices; endpoint pairings and closed-component counts for sliding, closed turns, cap splitting and zero pieces; and independent incidence partitions against ordered symbolic fusion on bounded trees. Pairings do not classify tangles, so these checks are not substitutes for the collar and sphere isotopies in the written proof. They also do not verify the imported analytic or geometric theorem.

The bibliography distinguishes the classical algebraic/arborescent tangle calculus from this labelled reduction and its application to the inherited volume theorem. The native figures are in `figures/` and compile within the article.
