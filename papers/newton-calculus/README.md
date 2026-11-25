# Newton calculus and stationary profiles of Conway tangles

[Read the PDF](../../docs/papers/newton-calculus.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

This paper starts with a two-strand operator and follows its Newton
basis indices through a fixed sequence of tangle stacks and quarter-turns.
The finite formulas give a sum over integer states. When every auxiliary
circle has complete color and no half twists are retained, its nonzero
terms are positive. The second part of the paper determines which
expressions admit an interior real state, proves that their action has a
unique interior maximum, and calculates the response of that maximum to
a prescribed output label.

The finite calculation retains values and first derivatives at repeated
spectral roots. The positive source is the expression with every auxiliary
circle at complete color and no retained half twists. Its positive-sum limit
is not a statement about the signed filled invariant.

This is a common foundation for the [strict source bounds](../conway-source-bounds/README.md), [strict geometric construction](../strict-conway-geometry/README.md), and [moving-meridian source estimates](../moving-meridian-sources/README.md). Each uses specific finite or variational statements; the signed filling analysis and geometric volume comparison are not premises of this paper.

The main results are:

- Proposition 3.2 and Theorem 3.3: the diagrammatic Newton turn, marked closure
  and full positive multiplication law, including repeated-root data.
- Proposition 4.1 and equation (4.8): the circle and crossing operators,
  with the stated normalization.
- Theorem 5.5: the reduced-junction criterion for strictness and preservation
  of the full finite source.
- Lemma 6.1 and Theorem 6.4: independent integer state coordinates, the interior maximum,
  negative definite Hessian and positive-source limit at every sufficiently
  large level of either parity.
- Theorems 7.3–7.4 and Corollary 7.5: absolute boundary profiles, harmonic
  response and a decomposition of the maximum at any exposed leaf.
- Theorem 8.1: the general quarter bound for every original leaf.
- Proposition 9.3, Corollary 9.4 and Lemma 9.5: the completed-root
  specialization and its stronger two-sided leaf bound.

The strict boundary proof includes intersections of product faces and
continuity of optimized profiles at feasible output endpoints. The
bound for the recursive subclass in Section 9 is stronger than the
general quarter bound. It places each elementary label strictly between
one quarter and $\arctan(2)/\pi$, giving a compact interior neighborhood for
the subsequent estimates with complex coefficients.

The companion mathematical inputs are the crossing
identification and enhanced reduced normalization from *Finite spectral
evaluation and uniform filling bounds*, Proposition 5.1 and Theorem 10.1.
The complete pair commutant, turn, trace, color coefficients, support,
variational maximum and stationary profiles are proved here. Moving-meridian
identities, complementary signed-source estimates and marked hyperbolic
geometry belong to their separate papers.

Build the PDF from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

From the repository root, run both finite reproduction suites with one
command. NumPy and SymPy are required by the physical-matrix suite.

```sh
python3 papers/newton-calculus/check.py --output /tmp/newton-calculus-check
```

The runner invokes [check_finite.py](check_finite.py) for the physical
matrices and [check_profiles.py](check_profiles.py) for support and
stationary-parameter identities. The report contains both suites, their
explicit finite ranges and the current paper's input hashes. These checks detect coefficient, indexing and
normalization errors. They do not replace the all-level or variational
proofs.
