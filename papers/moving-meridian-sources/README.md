# Moving-meridian source estimates for strict Conway tangles

This paper proves the source comparison needed when the main meridian moves by order $1/N$. It retains arbitrary fixed strict bare components, both level parities, repeated-node normal data, all original crossing powers and all shared edge targets.

Theorem 1.1 constructs the original finite wire packet and proves its holomorphic local Gaussian and full real-angular strip bound. Theorem 1.2 evaluates the entire filling sum for independently long fixed signed powers, with a nonzero joint first charge and the exact reduced-cut and framing scalars. It is an analytic source theorem; preferred-longitude identification and all-orders recurrence consequences are separate results.

The new estimates are the whole low trace, reflected high-index trace, coupled pressure comparison, simultaneous half-boundary reassembly and the strict Fourier loss at equality saddles. The proof uses the following numbered companion inputs:

- *Exact Newton calculus for tangles with a moving meridian*: Proposition 6.1, equation (6.4), Theorem 7.1 and Proposition 8.1 for the physical crossing, normals, original contraction and scalar ledger.
- *Newton calculus and stationary profiles of Conway tangles*: Theorem 3.3 for exact complete positive multiplication; Lemma 5.2 and Theorem 5.5 for strict syntax; Theorem 6.4 for the original optimizer; Lemma 7.1, Proposition 7.2, Theorems 7.3–7.4 and Corollary 7.5 for stationary response and absolute branch budgets.
- *Spectral estimates for Conway tangle sources*: Lemma 2.1 for complete Hermite conditioning and Lemma 7.2 for the angular estimate. The paper proves the local argument that upgrades the latter's subexponential prefactor to the polynomial bound used here.
- *Holomorphic source asymptotics and volume limits for strict Conway compositions*: Lemma 2.1 for the canonical factorial interpolation and its bulk expansions.

Build locally with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex` in this folder. The native illustration is `figures/reflected-pair.tex`.

Run the finite checker from the repository root:

```sh
python3 -I papers/moving-meridian-sources/check.py --output /tmp/moving-meridian-source-check
```

It uses only the Python standard library and writes `summary.json` to the supplied directory, removing an older summary before validation. Direct monic polynomial division is compared with the finite Fourier formula at levels 2 through 12, including the collision parameters. Separate checks compare literal Newton products with the low/high Laurent formulas, verify the full dual metric and exact fusion, and check the odd projector. These finite checks do not prove the uniform analytic estimates, supported rounding, stationary phase or the whole filling comparison; those are the written proofs.
