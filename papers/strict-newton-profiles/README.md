# Stationary profiles of strict Newton trees

This paper studies arbitrary fixed ordered expressions in elementary Newton pieces, turns and products whose original closed wire constraints have a strict state. It proves exact support and the reduced-junction criterion, the primitive lattice, the interior optimizer with its boundary argument, stationary profile constants, and the quarter bound for every original leaf. The positive-sum limit identifies the optimized action with the rate of the original positive evaluation.

The finite rerooting identities retain all physical leaf labels. They do not assert a tangle isotopy or estimate signed coefficients. Local signed asymptotics, complementary source bounds, the geometric construction and the entire filling sum require separate arguments.

The numbered imports are Newton Proposition 3.2, Theorem 3.3, Proposition 4.1, Lemma 5.2 and equations (4.3), (4.8). The optimizer and profile results use only that finite calculus and its elementary uniform factorial estimate. There is no dependency on the Conway source-bound, quarter-index asymptotics or Conway asymptotics papers.

Build the article in this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The standalone finite checker requires only Python 3's standard library:

```sh
python3 -I papers/strict-newton-profiles/check.py --output /tmp/strict-newton-check
```

It compares the full polynomial quotient and Newton multiplication in exact finite fields, enumerates supports through distinct parenthesizations, and checks rational port identities. The JSON record gives the finite ranges and source hashes. These checks are supplementary to the written all-level and variational proofs. A stale success record is removed before validation, including before rejection of an optimized Python invocation.

The native illustration is [figures/reduced-tree.tex](figures/reduced-tree.tex). The mathematical source files are `main.tex`, `syntax.tex`, `variation.tex` and `profiles.tex`; generated artifacts stay in `build/`.
