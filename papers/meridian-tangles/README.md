# Exact Newton calculus for tangles with a moving meridian

[Read the PDF](../../docs/papers/meridian-tangles.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

Turning a two-strand tangle reverses one strand orientation. Away from
the complete color, that reversal changes the representation and can
change the polynomial relation satisfied by the pair Casimir. This
paper gives coordinates in which the turns, products, crossings and
closure can all be followed without identifying these different
algebras.

The parameter is $M=q^s$, with $q=e^{\pi i/N}$, $N\ge2$ and complex
$|s|<1$. This is a disk in the scaled logarithm $s$; its image in the
$M$-plane shrinks toward one as $N$ grows. It is not a fixed meridian
neighborhood independent of the level.

Theorem 1.1 gives the moving-meridian calculus: the Casimir relation,
full pivotal closing functional, all six physical quarter-turns and
crossing polynomials at repeated roots. The fixed Newton basis retains
both values and first derivatives. The matrices are derived from the
evaluation and coevaluation maps, so the orientation factors are
determined by the tangle convention.

The main later exports are:

- Proposition 3.1: the Casimir polynomial and pivotal moments.
- Lemma 4.1: exact coordinate dualities, including confluent root data.
- Proposition 6.1: the crossing polynomial, its inverse and its
  first derivatives at repeated roots.
- Theorem 7.1: exact ordered-tree contraction. An outgoing boundary
  polynomial has degree at most $N-1$, independent of subtree size.
- Proposition 8.1: the scalar factors from the reduced cut,
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

The example at $N=2$ shows why keeping the two algebras matters: a
product that is zero at $s=0$ becomes a nonzero scalar when $s$ moves.
The tree formula retains that product and every basis index. Subsequent
papers use these finite identities to estimate the whole sum and
compare its growth with hyperbolic volume.

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
