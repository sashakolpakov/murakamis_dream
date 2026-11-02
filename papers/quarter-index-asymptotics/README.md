# Asymptotics of signed Newton coefficients near the quarter index

This paper proves a local analytic theorem for the original finite signed Newton coefficient near index $r/N=1/4$. It continues the source-selected branch across a point where the two characteristic roots have equal modulus but remain distinct.

The proof first constructs an exponentially accurate backward diagonalization on a fixed complex domain. It then chooses a shorter propagation interval on which every intermediate relative action is below the conversion barrier. The actual high-index finite coefficient fixes both initial channel amplitudes. A strict cumulative action loss controls the competing channel; the second channel is never discarded. Exponential Euler interpolation preserves the original amplitude and both parity endpoint normalizations.

Exports are:

- Theorem 1.1: the actual quarter-source theorem, with exponential relative grid error and a separate holomorphic leading asymptotic.
- Lemma 2.1: quantitative backward analytic diagonalization, followed by the exact two-channel interaction identity.
- Corollary 4.1: the original signed coefficient and its normalized absolute shear action.
- Corollary 4.2: a local finite-window Gaussian under explicit primitive-lattice, strict-support and Hessian hypotheses.

Numbered companion imports are **Holomorphic source asymptotics and volume limits for Conway closures**, Lemma 2.1, Sections 3.1–3.3 and Proposition 3.1; and **Newton coefficients and positive sources for Conway tangles**, Theorem 3.3, Proposition 4.1 and equation (4.8). The paper proves its new transport estimates directly. Costin–Costin supplies literature context, and the NIST DLMF is cited for the Euler–Maclaurin integral remainder and periodic Bernoulli series.

The conclusion is local. It does not estimate omitted aliases or physical-color complements, continue through colliding roots, or prove a whole filled-invariant or volume theorem.

Build in this folder with:

    latexmk -pdf -outdir=build main.tex

Run the bounded standard-library checker from the repository root with:

    python3 -I papers/quarter-index-asymptotics/check.py --output /private/tmp/quarter-index-check

The checker compares the literal finite factorial sum with the rational recurrence at both parities, including its terminal row. Independently chosen rational matrices verify the exact backward conjugation and interaction reconstruction with two nonzero input channels. It records hashes before and after, rejects optimized Python, removes an earlier summary before checking, and writes summary.json. These finite identities are supplementary to the uniform written proof.
