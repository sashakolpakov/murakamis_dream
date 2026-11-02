# Spectral bounds and asymptotics of Casimir sources

This 25-page paper studies a finite polynomial attached to a pair of strands and the coefficients obtained by identifying its variables across a diagram. It brings the uniform local bounds and the shared central-coefficient asymptotic into one account, so that the second proof can use the first directly.

Theorem 1.1 bounds each of the three local degree sectors uniformly over the real spectral interval and all face phases. Its hypotheses allow any fixed zero pattern with positive sum of the two outer face moduli. The proof retains the signs of the interval recurrence, both unused diagonal products, and the odd skipped-row term. The one-sided conclusions are bounds on polynomial values; they do not assert coefficientwise domination.

Theorem 8.1 concerns the central coefficient of a finite simple triangulated sphere with a dual perfect matching and a marked nonmatching edge. The variables at the endpoints of the marked edge are zero. The theorem assumes a stationary positive radius vector for the remaining variables. Under this hypothesis it proves a nonzero holomorphic Gaussian asymptotic and a strict spectral gap, for both parities and all sufficiently large integer levels. The primitive face lattice and the bound on the complementary angular domain are part of its proof.

Section 14 applies these conclusions to the independently stated oscillatory filling theorem. A bound on the complementary degree sectors and a geometric identification of the action are additional inputs to a volume theorem; this paper does not prove either of them.

The two figures show the local path partition and a shared coefficient on a tetrahedral sphere. Their TikZ sources are in `figures/`.

To build the paper from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=build main.tex
```

To run the finite algebra checks from the repository root, with SymPy installed:

```sh
python3 papers/casimir-source-asymptotics/check.py \
  --output repro/results/casimir-source-asymptotics
```

The wrapper invokes the unchanged checks in the two earlier editions. The local check compares the finite matrix polynomial, path partition, central factors, protected-zero identities, and nodal signs at levels 3–6. The central-source check compares cofactors with positive matrix determinants and checks the parity normalization at levels 3–8. These exact finite checks help detect formula errors. The uniform estimates, complex contour arguments, and Gaussian asymptotics have written proofs in the paper.

The earlier editions remain available in `papers/local-coefficients` and `papers/source-asymptotics`, with their original numbering. The new paper retains their labels as source aliases where definitions have been consolidated.
