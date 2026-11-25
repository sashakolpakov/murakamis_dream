# Exact Newton calculus for tangles with a moving meridian

[Read the PDF](../../docs/papers/meridian-tangles.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

This paper proves finite operator identities when the main meridian is
$M=q^s$, with $q=e^{\pi i/N}$ and $|s|<1$. The integer $N\ge2$ is the
level. The two strand orientations carry different ordered modules and
Casimir quotients; the calculation keeps those types distinct.

Theorem 1.1 gives the moving-meridian calculus: the Casimir relation,
full pivotal closing functional, all six physical quarter-turns and
crossing polynomials at repeated roots. The fixed Newton basis retains
both values and first derivatives. Its paired sine products and quadratic
orientation scalars are derived from the actual bending maps.

The main later exports are:

- Proposition 3.1: the Casimir polynomial and pivotal moments.
- Lemma 4.1: exact coordinate dualities, including confluent root data.
- Proposition 6.1: the physical crossing polynomial, its inverse and its
  full repeated-root normals.
- Theorem 7.1: exact ordered-tree contraction. An outgoing boundary
  polynomial has degree at most $N-1$, independent of subtree size.
- Proposition 8.1: the scalar ledger for the original reduced cut,
  crossing exponents, orientations and zero-framing correction.

The complete-color calibration uses [Newton calculus and stationary
profiles of Conway tangles](../newton-calculus/README.md), Proposition 3.2
and equation (4.8). Canonical polynomial reduction and the enhanced
normalization use [Finite spectral evaluation and uniform filling
bounds](../filling-bounds/README.md), Propositions 2.1–2.2 and Theorem 10.1.
The Kashaev identification in the latter theorem applies for $N\ge3$.
The nilpotent and unrolled ribbon-tangle literature supplies the framework;
the moving coordinate, turn, crossing and closing calculations are proved
in this paper.

These are exact finite identities. They supply no large-level source
estimate, noncancellation theorem or hyperbolic volume comparison.

Build from the repository root:

~~~sh
python3 tools/build_papers.py meridian-tangles
~~~

With NumPy installed, run the bounded exact checker separately:

~~~sh
python3 -I papers/meridian-tangles/check.py --output /tmp/meridian-tangle-check
~~~

It constructs the physical modules, coproducts, crossings and bending
maps over finite fields, then compares them with the polynomial,
six-turn and tree formulas. It records its finite parameter cases and
source hashes in summary.json. These checks detect finite algebra errors;
the all-level identities have written proofs in the paper.
