# Positive octahedra and primitive fillings for trees of crossing circles

[Read the PDF](../../docs/papers/circle-tree-geometry.pdf) ·
[TeX source](main.tex)

An ordered tree of crossing-circle tangles determines the diagrams in
this paper. Every vertex has its own crossing circle, every tree edge
is a physical quarter-turn attachment, and the order of the factors and
the original crossing disks are retained. The tree has at least one
edge. The theorem concerns this literal construction, rather than all
strict Conway presentations.

Let $d_v$ be a vertex degree, let $\epsilon_v$ be its retained half-twist
choice, and let $p_v$ be its disk-framed filling integer. Put
$n_v=\epsilon_v-2p_v$ and $L_v=\sqrt{d_v^2+n_v^2}$.
Theorem 1.1 constructs the positive cone deformation and smooth
hyperbolic endpoint when $L_v\ge630$ at every vertex. The degree
alternative allows an internal vertex to have a short or zero crossing
power. The original strand connections determine whether the endpoint
is a knot complement.

## What is proved

Proposition 2.1 identifies the ordered projection cut with two octahedra
per tree edge and records the original primitive peripheral paths.
Lemma 3.1 gives a positive eight-tetrahedron chart and its full face
maps. The charge equations then have a unique solution in the stated
polydisk, with the sign needed for geometric completion.

For cone angle $2\pi c$, the auxiliary periods satisfy

\[
 U_v=-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v,\qquad
 V_v=2i\tau_v,\qquad U_v+p_vV_v=-2\pi i c.
\]

The proof retains these full logarithms. At $c=1$ the primitive filling
meridian makes one turn and the completed metric is smooth. The action
is calibrated at the complete regular octahedra, and comparison of the
same fundamental chain fixes its absolute volume. Corollary 6.1 bounds
the core lengths and volume loss. Theorem 7.1 gives a more flexible
finite criterion with different parameter radii at different vertices.

The sole specialized companion input is the local peripheral-volume
differential from Section 7 of
[Circle patterns and primitive fillings of augmented links](../marked-fillings/README.md).
The ordered topology, positive path, primitive winding and completion
are proved here. This geometric theorem supplies no estimate of an
oscillatory quantum sum; the circle-tree volume paper proves that
separate analytic assertion under its own hypotheses.

## Build and finite checks

From the repository root:

~~~sh
python3 tools/build_papers.py circle-tree-geometry
python3 -I papers/circle-tree-geometry/check.py --output /tmp/circle-tree-geometry-check.json
~~~

The checker requires SymPy and runs the two specified exact block and
vertexwise-constant programs with temporary output paths. It also checks
the full primitive multiplier dictionary. Its finite identities and
rational constants support the written proof; they do not replace the
cut topology, contraction argument, metric completion or chain comparison.
