# Newton calculus and stationary profiles of Conway tangles

This 26-page paper combines the exact finite Newton calculus with the
variational theory of arbitrary strict ordered Conway expressions. It gives
one set of conventions and one proof of the shared support, lattice and
concavity arguments. The earlier *Newton coefficients and positive sources
for Conway tangles* and *Stationary profiles of strict Newton trees* remain
available as earlier editions at their original URLs.

The finite calculation retains values and first derivatives at repeated
spectral roots. The positive source is the expression with every auxiliary
circle at complete color and no retained half twists. Its positive-sum limit
is not a statement about the signed filled invariant.

The main results are:

- Proposition 3.2 and Theorem 3.3: the physical Newton turn, marked closure
  and full positive multiplication law, including repeated-root data.
- Proposition 4.1 and equation (4.8): the circle and crossing operators,
  with their actual normalization.
- Theorem 5.5: the reduced-junction criterion for strictness and preservation
  of the full finite source.
- Lemma 6.1 and Theorem 6.4: the primitive wire lattice, interior optimizer,
  negative definite Hessian and positive-source limit at every sufficiently
  large level of either parity.
- Theorems 7.3–7.4 and Corollary 7.5: absolute boundary profiles, harmonic
  response and the action budget at any exposed original leaf.
- Theorem 8.1: the general quarter bound for every original leaf.
- Proposition 9.3, Corollary 9.4 and Lemma 9.5: the completed-root
  specialization and its stronger two-sided leaf bound.

The strict boundary proof includes intersections of product faces and
continuity of optimized profiles at feasible output endpoints. The
completed-root bound is retained because it is stronger than the general
quarter bound and is still used by signed coefficient estimates.

The only companion mathematical inputs are the physical crossing
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

The runner invokes the existing checkers from the two earlier editions;
it does not copy their mathematical implementations. The report contains
both suites, their explicit finite ranges and all input hashes, including
the present paper. These checks detect coefficient, indexing and
normalization errors. They do not replace the all-level or variational
proofs.
