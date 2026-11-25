# Asymptotics of signed Newton coefficients near the quarter index

[Read the PDF](../../docs/papers/quarter-index-asymptotics.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

This paper proves a local analytic theorem for the original finite signed Newton coefficient near index $r/N=1/4$. It continues the source-selected branch across a point where the two characteristic roots have equal modulus but remain distinct.

The proof first constructs an exponentially accurate backward diagonalization on a fixed complex domain. A scalar contraction, proved from the original upper endpoint, supplies the high-index source anchor. The propagation interval is then chosen short enough that every intermediate relative action remains below the conversion barrier. The actual finite coefficient fixes both initial channel amplitudes. A strict cumulative action loss controls the competing channel; the second channel is never discarded. Exponential Euler interpolation preserves the original amplitude and both parity endpoint normalizations.

Exports are:

- Theorem 1.1: the actual quarter-source theorem, with exponential relative grid error and a separate holomorphic leading asymptotic.
- Lemma 2.1: quantitative backward analytic diagonalization, followed by the exact two-channel interaction identity.
- Lemma 3.1: the high-index source selected by its original terminal row, including exponentially accurate interpolation.
- Corollary 5.1: the original signed coefficient and its normalized absolute shear action.
- Corollary 5.2: a local finite-window Gaussian under explicit primitive-lattice, strict-support and Hessian hypotheses.

The companion inputs are **Holomorphic source asymptotics and volume limits for strict Conway compositions**, Lemma 2.1 only; and **Newton calculus and stationary profiles of Conway tangles**, Theorem 3.3, Proposition 4.1 and equation (4.8). The finite telescoping certificate, high-index source selection, transport estimates and absolute shear identity are proved here. No previous Conway manuscript edition is required. Costin–Costin supplies literature context, and the NIST DLMF is cited for the Euler–Maclaurin integral remainder and periodic Bernoulli series.

This paper is a separate local branch of the dependency graph. The enlarged strict Conway volume proof uses its pure factorial source and does not require this signed quarter-index result.

The conclusion is local. It does not estimate omitted aliases or physical-color complements, continue through colliding roots, or prove a whole filled-invariant or volume theorem.

Build in this folder with:

    latexmk -pdf -outdir=build main.tex

Run the bounded standard-library checker from the repository root with:

    python3 -I papers/quarter-index-asymptotics/check.py --output /private/tmp/quarter-index-check

The checker compares the literal finite factorial sum with the rational recurrence at both parities, including its terminal row. Independently chosen rational matrices verify the exact backward conjugation and interaction reconstruction with two nonzero input channels. It records hashes before and after, rejects optimized Python, removes an earlier summary before checking, and writes summary.json. These finite identities are supplementary to the uniform written proof.
