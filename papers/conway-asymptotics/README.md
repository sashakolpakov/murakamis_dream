# Holomorphic source asymptotics and volume limits for strict Conway compositions

[Read the PDF](../../docs/papers/conway-asymptotics.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

Fix a finite strict Conway tangle construction with at least two crossing
circles, and choose the even/odd strand connections so that its closure
is one knot. Theorem 1.1 proves the volume conjecture when each signed
filling integer is independently sufficiently large in absolute value.
The construction and twists stay fixed while the level tends to infinity
through all integers. Components closed inside a product are included in
the knot test.

Strictness means that the wire constraints admit leaf labels in
$(0,1/2)$, product labels $\max(x,y)<z<x+y<1$, complemented turn
labels, and complementary closing outputs. Elementary or turned
elementary closing children are allowed. Boundary-only presentations
and constructions growing with the level are outside the theorem.

For this fixed construction, the covered assignments have natural
density one in the integer lattice: the assignments with any bounded
coordinate occupy a proportion tending to zero in expanding boxes.
This does not assert density one among distinct knots, or only finitely
many excluded assignments.

## One proof through the pure source

The proof now follows only the strict pure-source route. The entire
integer crossing power, including an odd or negative power, is expanded
exactly in ordinary colored circles. Thus the local asymptotic is needed
only for the positive pure source. A classical shear then identifies
the filling action with the original integer slopes and retained half
twists.

The argument has five steps:

1. The finite Newton algebra solves turn and closing constraints exactly.
   Its remaining wire lattice has fundamental cell volume one, including
   the bounded integer offsets.
2. Canonical factorial interpolation agrees exactly with the finite
   coefficients. The strict positive maximum gives a nonzero local
   source expansion.
3. The full-source bounds control the physical remainder and macroscopic
   color deficits. A second application of the same lattice lemma gives
   the local Fourier expansion; a separate contour estimate gives the
   gap on the rest of the Fourier torus.
4. Fourier--Hermite inversion retains derivatives at repeated roots.
   Parseval bounds the complete filling coefficient vector by
   $2\sqrt N(1+|n|/\sqrt{12})$. The whole oscillatory-sum theorem then
   gives the nonzero leading term.
5. The marked geometric filling theorem identifies its critical action
   with the absolute volume of the specified knot complement.

The local positive sum does not settle cancellation in the oscillatory
filling. The global Fourier gap, whole-sum theorem and metric completion
remain separate parts of the proof. Exact linear corridors can be
contracted before choosing coordinates; no estimate substitutes for
those proof steps.

In the dependency graph, this application joins the strict variational
result, the full-source bounds and the marked geometric filling theorem.
The [ordered-reduction paper](../conway-reductions/README.md) can apply
its conclusion after checking the surviving strict factor and its net
twists.

## Proof inputs

- **Newton calculus and stationary profiles of Conway tangles:**
  Proposition 3.2, Theorem 3.3, Proposition 4.1 and equation (4.8) give
  the exact local algebra. Lemma 6.2 gives the uniform endpoint factorial
  estimate. Lemmas 5.2 and 6.1 supply the strict type test and primitive
  coordinates. Theorem 6.4 supplies the unique strict optimizer and
  negative wire Hessian.
- **Spectral estimates for Conway tangle sources:** Theorem 1.1 gives
  whole-source, macroscopic-color and full-minus-core bounds for three
  or more leaves; Corollary 9.1 handles two leaves. Only their pure
  specialization is used here.
- **Finite spectral evaluation and uniform filling bounds:**
  Proposition 5.1 supplies the crossing values and repeated-root
  derivatives; Theorem 10.1 identifies the reduced normalization with
  Kashaev's invariant for $N\ge3$.
- **Oscillatory filling sums with independently long twists:**
  Theorem 1.1 applies after both local and global Fourier hypotheses
  have been verified and every scalar and endpoint multiplicity matched.
- **Marked geometry of strict Conway compositions:** Theorem 1.3 and
  equations (6.1)–(6.5) supply the classical shear, primitive integer
  filling, smooth metric completion and absolute action-volume equality.

## Exports and source organization

- Theorem 1.1, `ca:main`: the strict full-invariant asymptotic and volume limit.
- Lemma 2.1, `ca:factorial`: canonical factorial interpolation, with its
  exact shifts, reflection and all-order expansion retained.
- The unnumbered finite-lattice saddle estimate in Section 2 applies
  first to the wire sum and then to the color Fourier sum.
- Theorem 3.1, `ca:strict-pure`: the pure window, its physical-source
  remainder and complex color bound.
- Proposition 3.2, `ca:Fourier-theorem`: the local Fourier expansion
  and global spectral gap.
- Section 4 gives full-power Fourier--Hermite inversion, the midpoint
  formula, the filled remainder and the classical action comparison.
- The same section now states shifted Fourier reconstruction and
  Parseval, the coherent full-color error bound and Lemma 4.1 on
  subexponential costs explicitly. The stationary Schur formula is
  written in the proof of Theorem 3.1. These steps need no import
  from the long reference.

The introduction is a separate source file, [introduction.tex](introduction.tex),
so the reference manuscript can include the same proof without copying it.
The canonical factorial lemma remains available to
companion papers that use it independently of the volume theorem.

## Build and finite reproduction

From the repository root, build with
`python3 tools/build_papers.py conway-asymptotics`.
For a local build without publishing the PDF, add `--no-publish`.

The optional standard-library checker is run separately:

    python3 -I papers/conway-asymptotics/check.py --output /private/tmp/conway-asymptotics-check

At levels $N=2,\ldots,12$, it compares direct Newton-polynomial powers
and inverses with full Hermite interpolation, colored-circle
reconstruction and the midpoint identity. It includes composite levels
and the odd-level simple root. Its 154 power cases and 462 midpoint
cases are finite algebra checks. They do not establish contour bounds,
variational theorems, metric completion or the all-level asymptotic.
The input manifest records the current consolidated companion sources.
