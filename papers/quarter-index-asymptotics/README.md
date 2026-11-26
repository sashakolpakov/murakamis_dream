# Asymptotics of signed Newton coefficients near the quarter index

[Read the PDF](../../docs/papers/quarter-index-asymptotics.pdf) · [TeX source](main.tex)

A finite signed Newton coefficient satisfies a second-order recurrence.
At scaled index $r/N=1/4$, its characteristic roots have equal modulus
but remain distinct. This paper proves one nonzero holomorphic
asymptotic expression on a fixed neighborhood extending across that
point. Theorem 1.1 distinguishes an exponentially accurate identity on
the integer grid from the asymptotic of its constructed holomorphic
interpolation.

The proof determines the solution from the finite upper endpoint.
Above the quarter index, a contracting ratio recurrence gives its value
and consecutive ratio. A change of basis on a fixed complex domain
makes the coupling between the two components exponentially small.
The propagation interval is then chosen short enough that the
accumulated ratio cannot amplify this error beyond its bound. Both
initial components are kept. An Euler–Maclaurin interpolation of the
selected product preserves its amplitude, action and endpoint
normalization at both parities.

Corollary 5.1 returns to the signed tangle coefficient and proves its
absolute shear-action identity. Corollary 5.2 evaluates a local finite
summation window under explicit lattice, support and Hessian
hypotheses. Neither corollary estimates the contribution outside that
window or proves a filled-invariant volume limit.

The companion inputs are the canonical factorial lemma of
[the strict Conway analysis](../conway-asymptotics/README.md), and the
finite multiplication and crossing identities of
[Newton calculus](../newton-calculus/README.md). The recurrence,
endpoint selection, transport and shear-action identity are proved
here. Costin–Costin provides context for recurrence asymptotics; the
DLMF supplies the Euler–Maclaurin remainder and Bernoulli formulas.

This is a separate local result. The strict Conway volume proof uses its
pure factorial sum and does not depend on this signed quarter-index
analysis.

From the repository root:

```sh
python3 tools/build_papers.py quarter-index-asymptotics
python3 -I papers/quarter-index-asymptotics/check.py --output /tmp/quarter-index-check
```

The standard-library checker compares the finite factorial sum with its
recurrence at both parities, including the terminal row. It also checks
the exact basis-change and two-component transport identities. The
uniform analytic estimates are proved in the manuscript.
