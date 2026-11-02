# Volume limits for long alternating-generator three-braids

[Read the PDF](../../docs/papers/three-braids.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

Fix an even number $m\ge6$ of factors in the closed three-strand braid

$$
\sigma_2^{n_0}\sigma_1^{n_1}\sigma_2^{n_2}\cdots\sigma_1^{n_{m-1}}.
$$

Theorem 1 says that, for each fixed $m$, there is a finite threshold
$B_m$ such that independently chosen signed integers $|n_j|>B_m$ give
the Kashaev volume limit whenever the braid's permutation is a 3-cycle.
That permutation condition says its closure is one knot. All powers
are fixed before the level tends to infinity. The limit includes both
parities and composite levels; the generators alternate, while the
crossing signs may be chosen independently.

The work specific to this family is the identification of its original
crossing disks with a matched bipyramid, an explicit circle packing,
and three common choices of face weights. Their inequalities control
all complementary terms for every fixed even $m\ge6$. The argument
uses the same weight for every occurrence of a shared face; estimating
isolated factors with unrelated weights would not prove this bound.

The following current companion papers supply the common foundations:

| Paper | Input used here |
| --- | --- |
| [Finite spectral evaluation and uniform filling bounds](../filling-bounds/README.md) | Theorem 1.1 gives the filling norm; Theorem 9.1, Corollary 9.2 and Theorem 10.1 give the exact original coefficient and invariant normalization. |
| [Spectral bounds and asymptotics of Casimir sources](../casimir-source-asymptotics/README.md) | Theorems 1.1 and 8.1 give the local sector bounds and the nonzero central expansion; Section 14 fixes the central filling normalization. |
| [Oscillatory filling sums with independently long twists](../oscillatory-fillings/main.tex) | Theorem 1.1 evaluates the whole oscillatory sum once its local and global source hypotheses hold. |
| [Circle patterns and primitive fillings of augmented links](../marked-fillings/main.tex) | Theorem 1.1 gives the original primitive completion and its absolute volume. |

Those imported analytic and geometric proofs are not reproduced in this
14-page application. Its own global comparison is the additional step
that makes the central contribution determine the rate of the full
invariant. The theorem gives no threshold uniform in a growing number
of factors, and no assertion for powers growing with the quantum level.

## Build and finite checks

From the repository root:

```sh
python3 tools/build_papers.py three-braids
python3 repro/check_cyclic_source_constants.py
```

The second command reproduces the rational constant bounds. The proof
for every fixed even number of factors is written in the paper; the
script does not infer it from a finite sample of lengths.
