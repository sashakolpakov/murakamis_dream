# Volume asymptotics for trees of crossing circles

[Read the PDF](../../docs/papers/circle-tree-volume.pdf) · [TeX source](main.tex)

This paper proves the volume conjecture for two explicitly described
sets of fixed crossing-circle tree diagrams. Every vertex carries its
own crossing circle, and the ordered tangle closure must give one main
knot with no internal closed component. The diagram and all signed
crossing powers stay fixed while the level $N$ tends to infinity.

There are two sufficient conditions. They have common finite
preliminaries but separate proofs:

- Theorem 1.1 assumes
  $\sum_v d_v/(d_v^2+n_v^2)\le2^{-25}$, where $d_v$ is degree
  and $n_v$ is the signed crossing power. It gives a nonzero leading
  asymptotic at both level parities. Theorem 1.2 also computes the first
  centered meridian correction with error $O(N^{-2})$.
- Theorem 1.3 uses a chosen final vertex and a positive decay parameter
  at every other vertex. The test is the finite set of inequalities
  (7.3), (7.8), (7.9). Corollary 1.4 gives the simpler sufficient
  alternative $d_v\ge2^{28}$ or $|n_v|\ge2^{27}$ at every vertex,
  with the choice made independently. This proof gives the centered
  meridian ratio $1+O(N^{-1})$.

The summed proof evaluates all angular variables jointly. The directed
proof evaluates a subtree as a polynomial in its parent angle and
divides that polynomial by its exact value at zero before continuing.
This normalization avoids repeatedly paying for the same loss in
exponential rate. The final vertex needs no outgoing polynomial bound.
Section 8 gives a star that illustrates this distinction, and a
construction that adds long terminal tangles while keeping arbitrarily
many prescribed short powers at the old vertices. Adding those tangles
can change the knot.

Both proofs keep the full finite polynomial contraction, including
first derivatives at double spectral roots. Fourier-tail and contour
estimates establish a nonzero coefficient for the selected critical
point. The classical primitive-filling theorem then identifies its real
action with the volume of the knot complement.

The exact finite inputs come from
[Exact Newton calculus for tangles with a moving meridian](../meridian-tangles/README.md),
Proposition 6.1, Theorem 7.1 and Proposition 8.1. The strict Conway
analysis supplies only its canonical factorial lemma. The classical
volume equality is Theorem 1.1 of
[Positive octahedra and primitive fillings for trees of crossing circles](../circle-tree-geometry/README.md);
each analytic proof verifies that theorem's quantitative hypothesis.

The meridian statements use $M=q_N^s$ with bounded $|s|<1$. They concern
a shrinking neighborhood of $M=1$. The paper does not prove an
all-orders expansion or a theorem for arbitrary tangles with several
exposed boundary components.

From the repository root:

```sh
python3 tools/build_papers.py circle-tree-volume
python3 -I papers/circle-tree-volume/check.py --output /tmp/circle-tree-volume-check
```

The combined runner executes the summed and directed finite checks,
including rational inequalities, endpoint pairings and comparisons of
the exact recursion with finite-grid evaluation. These checks supplement
the written analytic and geometric proofs.
