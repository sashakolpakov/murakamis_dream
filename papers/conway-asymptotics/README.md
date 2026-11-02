# Holomorphic source asymptotics and volume limits for strict Conway compositions

[Read the PDF](../../docs/papers/conway-asymptotics.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

Theorem 1.1 proves the nonzero asymptotic of the full reduced Kashaev invariant and its actual knot-complement volume limit for each fixed strict Conway presentation with at least two original crossing circles. Every filling integer is independently signed, sufficiently long, and fixed before the integer level tends to infinity. The actual main-strand component test counts components closed inside products as well as at the final closure.

Strictness means that the original wire constraints admit leaf labels in $ (0,1/2) $, strict product labels $ \max(x,y)<z<x+y<1 $, complemented turn labels, and complementary closing outputs. Bare or turned elementary closing children are allowed. Boundary-only presentations and constructions growing with the level are outside the theorem.

The full-volume proof uses the exact pure factorial source at every strict leaf index. The paper proves its finite wire-window expansion, primitive lattice amplitude, real Fourier action, whole spectral-cube gap, and full integer-power Hermite/midpoint conversion. A direct classical shear identifies the critical action with the primitive filling of the original odd or even partner. No half-integral surgery is assigned to the pure algebraic partner.

In the dependency graph, this is the application that joins the strict variational result, the full-source bounds and the marked geometric filling theorem. The [ordered-reduction paper](../conway-reductions/README.md) can apply its conclusion after checking the surviving strict factor and its net twists.

The separately retained signed results have their original scope: Proposition 3.1 treats high-index signed leaves, and Theorem 4.1 gives the signed packet for the completed-root grammar. They are not premises of the enlarged strict pure-source route.

## Numbered imports

- **Newton calculus and stationary profiles of Conway tangles:** Proposition 3.2, Theorem 3.3, Proposition 4.1 and equation (4.8) give the exact local algebra; Lemma 6.2 gives the uniform endpoint factorial estimate. Lemmas 5.2 and 6.1 give the strict type test and primitive integer coordinates with all-level feasible approximation. Theorem 6.4 gives the unique strict optimizer and negative definite wire Hessian. The completed-root signed packet separately uses Proposition 9.3 and the stronger leaf bound of Lemma 9.5.
- **Spectral estimates for Conway tangle sources:** Theorem 1.1 for the full-source, physical-color and full-minus-core bounds at three or more leaves; Corollary 9.1 for exactly two leaves. The main volume proof uses their pure specialization. Proposition 3.1 is used separately in the older signed completed-root packet.
- **Finite spectral evaluation and uniform filling bounds:** Proposition 5.1 for the full crossing and repeated-root normals, and Theorem 10.1 for reduced Kashaev normalization at N≥3.
- **Oscillatory filling sums with independently long twists:** Theorem 1.1, after the present paper verifies both hypotheses for the exact even Fourier polynomial and matches every scalar and endpoint multiplicity.
- **Marked geometry of strict Conway compositions:** Theorem 1.3 and equations (6.1)–(6.5) for the classical shear, primitive original filling, smooth metric completion and absolute action-volume equality.

## Exports and their numbering

- Theorem 1.1, ca:main: enlarged strict full-invariant asymptotic and volume limit.
- Lemma 2.1, ca:factorial: unchanged canonical factorial interpolation.
- Proposition 3.1, ca:shear: unchanged high-index signed action identity.
- Theorem 4.1, ca:packet-theorem: retained completed-root signed packet.
- Theorem 4.2, ca:strict-pure: strict pure-window and physical-source comparison.
- Proposition 4.3, ca:Fourier-theorem: strict real local Fourier expansion and global spectral gap; previously numbered 4.2.
- Section 5 retains the full-power and midpoint equations. Its final action adapter now uses the direct strict classical potential.

## Build and finite reproduction

From the repository root, build with `python3 tools/build_papers.py conway-asymptotics`.

From the repository root, run:

    python3 -I papers/conway-asymptotics/check.py --output /private/tmp/conway-asymptotics-check

The standard-library checker uses two finite fields per level at N=2,…,12. It compares direct Newton-polynomial powers and inverses with full Hermite value/normal interpolation, ordinary-circle reconstruction, and the exact midpoint formula. It writes summary.json, with source hashes and explicit limitations. Its 154 power cases and 462 midpoint cases are finite algebra checks. They do not establish contour bounds, variational theorems, geometric completion or the all-level asymptotic.
