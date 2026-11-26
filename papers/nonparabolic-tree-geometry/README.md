# Nonparabolic holonomy of trees of crossing circles

[Read the PDF](../../docs/papers/nonparabolic-tree-geometry.pdf) · [TeX source](main.tex)

This paper allows the main meridian of an ordered crossing-circle tree
to vary away from its parabolic value. It constructs the representation
of the specified augmented link group, follows its peripheral curves,
and describes the local representations of its smooth fillings.
An eigenline is retained at every cusp; this choice is needed when the
two main-meridian eigenvalues separate.

Theorem 1.1 gives the augmented family with main eigenvalue $M$ and
auxiliary longitude parameters $Q_v$. Its meridian and longitude
similarity logarithms are

$$
U_v=\sum_{e\ni v}\log\frac{Q_v+X_e}{1+Q_vX_e}
       -\epsilon_v\log Q_v,
\qquad V_v=2\log Q_v.
$$

The edge coordinates $X_e$ satisfy the displayed algebraic gluing
relation. Sections 2–4 prove that relation from ideal vertices and face
maps, compare it with explicit four-punctured-sphere matrices, and glue
the blocks in their prescribed order. The half-twist calculation follows
both puncture generators and their eigenlines, rather than using traces
alone.

Proposition 6.1 proves a general local coordinate theorem on a specified
positive ideal triangulation: one primitive peripheral similarity
logarithm at each torus gives coordinates on the decorated representation
space. It includes infinitesimal deformations with exact peripheral
characters. Theorem 1.2 applies this result at a positive smooth filling
whose auxiliary longitudes have distinct eigenvalues. The equations
$U_v+p_vV_v=-2\pi i$ then impose precisely the filled-group relations;
with one main cusp left unfilled, $\log M$ is a local coordinate.

The geometric hypotheses are supplied by
[Positive octahedra and primitive fillings for trees of crossing circles](../circle-tree-geometry/README.md)
when $\sqrt{d_v^2+n_v^2}\ge630$ at every circle, or under its
vertex-dependent refinement. The proof uses the positive augmented
triangulation at that endpoint. It does not require a new positive
triangulation of the filled manifold. The other companion inputs are
the signed meridian convention of the strict Conway geometry paper and
the normal-path intersection calculation of the circle-pattern paper.

The results provide the geometric branch for
[preferred longitudes](../preferred-longitudes/README.md) and
[meridian expansions](../meridian-expansions/README.md). Neither a quantum
asymptotic nor a global preferred-longitude formula is proved here.

From the repository root:

```sh
python3 tools/build_papers.py nonparabolic-tree-geometry
python3 -I papers/nonparabolic-tree-geometry/check.py --output /tmp/nonparabolic-tree.json
```

The checker verifies rational face, character and braid identities,
including alternatives that must fail if a factor or eigenline choice
is changed. The topology, positivity and local-coordinate theorem are
proved in the text.
