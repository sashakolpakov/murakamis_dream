# Volume asymptotics for trees of crossing circles

[Read the PDF](../../docs/papers/circle-tree-volume.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

This 27-page paper treats a fixed ordered tree of crossing circles whose literal tangle closure is a knot, with no component already closed inside an intermediate tangle. Every product junction carries a crossing circle. The tree, orientations and signed powers are fixed before the level tends to infinity.

The paper gives two independently sufficient conditions for the nonzero leading asymptotic of the reduced zero-framed invariant, through both level parities. The exponent is the volume of the original knot complement, by the primitive metric-completion theorem used with its hypotheses checked.

- **Theorem 1.1** assumes the summed bound `sum_v d_v/(d_v^2+n_v^2) <= 2^-25`. **Theorem 1.2** retains the exact framing scalar and sine quotient and gives the explicit first microscopic meridian correction, with remainder of order `N^-2`.
- **Theorem 1.3** assumes the finite directed inequalities (7.3), (7.8), (7.9), with a chosen final vertex and a positive decay parameter at each nonroot vertex. It proves the leading asymptotic and a centered microscopic meridian ratio `1+O(N^-1)`.
- **Corollary 1.4** gives the sufficient alternative `d_v >= 2^28` or `|n_v| >= 2^27`, chosen independently at every vertex. Corollary 8.1 retains the smaller uniform ratio criterion.

The summed theorem does not serve as a premise for the directed theorem. Their common finite Newton estimates, complex edge sum and exact Fourier trace occupy Sections 2–5. The joint Fourier proof is in Section 6; the normalized subtree induction is in Section 7. Section 8 includes the degree-or-twist construction, its endpoint pairing calculation, and a star showing why the final root must not be required to produce an outgoing decay bound.

The claims concern bounded microscopic meridian parameters `M=q_N^s`, not a fixed neighborhood of `M=1`. Only the summed theorem here proves the explicit first meridian correction. An all-orders expansion, a preferred-longitude calculation, and more general tangles with bare product junctions require separate results.

## Imported statements

| Source | Exact input | Use |
| --- | --- | --- |
| *Exact Newton calculus for tangles with a moving meridian* | Proposition 6.1 and equation (6.4); Theorem 7.1; Proposition 8.1 | Full physical crossing trace, original finite tree contraction and all scalar factors. |
| *Holomorphic source asymptotics and volume limits for strict Conway compositions* | Lemma 2.1 | Canonical sine factorial, reflections and uniform complex expansion. No Conway grammar or volume theorem is imported from that paper. |
| *Positive octahedra and primitive fillings for trees of crossing circles* | Theorem 1.1 | Original primitive smooth filling and absolute action-volume equality when `sqrt(d_v^2+n_v^2) >= 630`; each proof checks this condition and its critical point. |

## Building and finite reproduction

For typesetting, in this directory run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

From the repository root, the combined finite runner is:

```sh
python3 -I papers/circle-tree-volume/check.py --output /tmp/circle-tree-volume-check
```

It invokes the two existing checkers unchanged, with isolated Python, removes old results before launching them, requires both runs to succeed, and checks the recorded input hashes. It covers their exact identities, rational inequalities, endpoint pairings and finite comparisons. It does not certify the uniform estimates, Gaussian induction or geometric theorem by finite samples.

This is the current combined account. The earlier [summed-condition edition](../circle-tree-asymptotics/README.md) and [directed-condition edition](../directed-tree-asymptotics/README.md) remain available for existing citations. Their finite check implementations are retained by the combined runner. Combining the common preliminaries does not merge the two sufficient conditions or strengthen the directed meridian estimate.
