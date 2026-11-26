# Moving-meridian source estimates for strict Conway tangles

[Read the PDF](../../docs/papers/moving-meridian-sources.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

Moving the meridian changes the polynomial relations at product
junctions. A complete trace can consequently vanish at indices where
the deformed trace does not. This paper proves a comparison for the
whole connected region of junctions, rather than a false bound at each
vertex separately. Its elementary example at level three shows the
obstruction, and the reflected-index estimate explains how to overcome it.

The diagram is a fixed strict Conway construction with at least two
crossing-circle sites. The meridian is $M=q^s$, so fixed $s$ describes
a displacement of order $1/N$. Theorem 1.1 restricts the independent
integer states to a rectangle about the positive maximum, bounds the
discarded terms, and proves a holomorphic Gaussian expansion and a
bound on the full real angular cube. Theorem 1.2 applies the crossing
traces for independently sufficiently long fixed signed powers. Their
joint Fourier mode $(1,\ldots,1)$ has nonzero leading coefficient and
larger real action than every competing term. The reduced closure and
framing factors are explicit.

The [meridian-expansion paper](../meridian-expansions/README.md) uses these estimates to derive every finite inverse-level order and a conditional classical equation. The present paper supplies the source analysis, without assuming that later recurrence result.

The proof first retains every value and first derivative in the finite
trace. It then compares the shared maxima after reflecting a high
index and combining its neighboring junctions. Boundary labels fixed
at one half carry no leaf action in this comparison. Finally a common
critical branch compares all retained Fourier modes without a
restriction on the ratios of the filling powers. The companion inputs
are:

- *Exact Newton calculus for tangles with a moving meridian*: Proposition 6.1, equation (6.4), Theorem 7.1 and Proposition 8.1 for the crossing, repeated-root derivatives, finite contraction and framing factors.
- *Newton calculus and stationary profiles of Conway tangles*: Theorem 3.3 for complete positive multiplication; Lemma 5.2 and Theorem 5.5 for strict feasibility; Theorem 6.4 for the positive maximum; Lemma 7.1, Proposition 7.2, Theorems 7.3–7.4 and Corollary 7.5 for the boundary profiles and their additive constants.
- *Spectral estimates for Conway tangle sources*: Lemma 2.1 for complete Hermite conditioning and Lemma 7.2 for the angular estimate. The paper proves the local argument that upgrades the latter's subexponential prefactor to the polynomial bound used here.
- *Holomorphic source asymptotics and volume limits for strict Conway compositions*: Lemma 2.1 for the canonical factorial interpolation and its bulk expansions.

Build locally with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex` in this folder. The native illustration is `figures/reflected-pair.tex`.

Run the finite checker from the repository root:

```sh
python3 -I papers/moving-meridian-sources/check.py --output /tmp/moving-meridian-source-check
```

It uses only the Python standard library and writes `summary.json` to the supplied directory, removing an older summary before validation. Direct monic polynomial division is compared with the finite Fourier formula at levels 2 through 12, including the collision parameters. Separate checks compare literal Newton products with the low/high Laurent formulas, verify the full dual metric and exact fusion, and check the odd projector. These finite checks do not prove the uniform analytic estimates, supported rounding, stationary phase or the whole filling comparison; those are the written proofs.
