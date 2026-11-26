# Balanced circle packings from terminal tangle decorations

[Read the PDF](../../docs/papers/terminal-decorations.pdf) · [TeX source](main.tex)

Start with a fixed simple triangulated sphere whose adjacent triangles
are paired, a nonmatching marked edge, and a half-twist pattern producing
one main knot. Its complete circle packing has two marked parallel lines
of curvature zero and positive curvatures at all other faces.

A terminal is a new crossing-circle tangle inserted immediately before or after an old box in its local stacking coordinate. This paper gives a finite construction that adds crossing-circle tangles
until every original and new region satisfies the strict shared-face
balance inequality. It leaves the old circles fixed, but it generally
changes the knot. Each old region receives an even number of terminals
on each side; odd powers at the new terminals preserve its four-endpoint
pairing and create no additional internal main component.

## Results

- **Theorem 1.2:** the explicit insertion counts produce a simple refined
  matched sphere, keep its mark and old packing, and make every retained
  and added region strictly balanced.
- **Corollary 1.3:** for this fixed decorated diagram and a knot-producing
  parity, independently sufficiently long signed primitive fillings at
  all its crossing circles give the knot-complement volume limit.
- **Propositions 6.1–6.2:** the retained-region and added-region estimates
  verify the construction, including regions incident to a marked line.

A crossing circle bounds the specified twice-punctured disk. A retained
half twist epsilon and disk-framed filling integer p give crossing power
n = epsilon - 2p. Every decoration, power and component pairing is fixed
before the quantum level tends to infinity. The filling threshold depends
on the whole final diagram, with no bound on its finite number of regions.
The theorem does not turn a short filling of the original knot into a
long filling without changing its diagram or knot type.

## What the paper imports

**Proposition 2.1** states the complete interface. The finite source and
normalization come from **Finite spectral evaluation and uniform filling
bounds**, Proposition 4.1, Theorem 9.1, Corollary 9.2 and Theorem 10.1;
its Theorem 1.1 gives the full Hermite filling norm. **Spectral bounds
and asymptotics of Casimir sources**, Theorems 1.1 and 8.1, provides local
sector bounds and the central expansion. **Circle patterns and primitive
fillings of augmented links**, Proposition 2.1, Theorem 1.1 and Corollary
8.1, fixes the packing, primitive filled metric and absolute volume.
**Oscillatory filling sums with independently long twists**, Theorem 1.1,
controls the signed central period.

The direct volume implication uses **Shared face estimates and triangular
gluing for planar link diagrams**, Definition 3.1 and Theorems 1.1 and
4.3: strict balance supplies a certificate. The present paper
proves that its finite geometric modification supplies this hypothesis;
it does not infer a complementary-source estimate from the central
contribution alone.

## Build and finite reproduction

From the repository root:

~~~sh
python3 tools/build_papers.py --no-publish terminal-decorations
python3 -I papers/terminal-decorations/check.py --output /tmp/terminal-decorations-check
~~~

The checker uses integer and rational arithmetic for the recurrence,
count examples, sixteen oriented stellar patches and endpoint components.
Its finite samples supplement the all-real count construction and arbitrary
finite insertion proof. They do not establish a quantum asymptotic or
hyperbolic volume identity by sampling.
