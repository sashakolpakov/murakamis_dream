# Holomorphic source asymptotics and volume limits for Conway closures

This paper proves the nonzero all-level asymptotic and volume limit for a fixed completed-root Conway construction, with independently signed sufficiently long filling integers fixed before the level grows. Both closing boxes must belong to the stated completed grammar; the retained half-twist pairing must give a knot.

The proof supplies the canonical factorial continuation, an exact finite-endpoint recurrence for a signed leaf, an exponentially accurate index interpolation, the nonzero wire and color saddle coefficients, and the full shared Fourier gap. The quantum leaf action is identified with the classical shear potential including its color-dependent constant. Expanding the complete physical integer power into ordinary circles permits use of the real-action whole-filling theorem without changing the knot.

The numbered companion imports are:

- **Newton coefficients and positive sources for Conway tangles:** Proposition 3.2, Theorem 3.3, Proposition 4.1, equation (4.8), Proposition 5.3, and Lemma 6.1.
- **Complementary color bounds for Conway tangle sources:** Theorem 1.1 and the off-window comparison in Section 6.2.
- **Finite spectral evaluation and uniform filling bounds:** Proposition 5.1 for the full crossing and repeated-root normals, and Theorem 10.1 for reduced Kashaev normalization at $N\ge3$.
- **Oscillatory filling sums with independently long twists:** Theorem 1.1, after this paper verifies both analytic hypotheses for the exact even Fourier polynomial and matches its full scalar.
- **Marked deformations and long fillings of Conway closures:** Theorem 1.1 and the explicit cell potential of Section 2.

Build locally with latexmk -pdf -outdir=build main.tex in this folder.

From the repository root, run:

    python3 -I papers/conway-asymptotics/check.py --output /private/tmp/conway-asymptotics-check

The standard-library checker uses two finite fields per level at $N=2,\ldots,12$. It compares direct Newton-polynomial powers and inverses with full Hermite value/normal interpolation, ordinary-circle reconstruction, and the exact midpoint formula. It writes summary.json, with source hashes and explicit limitations. Its 154 power cases and 462 midpoint cases are finite algebra tests; they do not establish the analytic estimates or the volume theorem.
