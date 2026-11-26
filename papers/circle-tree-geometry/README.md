# Positive octahedra and primitive fillings for trees of crossing circles

[Read the PDF](../../docs/papers/circle-tree-geometry.pdf) · [TeX source](main.tex)

This paper constructs hyperbolic metrics for a specified class of augmented
link diagrams. The diagram is built from an ordered tree: every vertex
has a crossing circle, and every edge describes a quarter-turn attachment
of two-strand tangles. The branch order, crossing disks and endpoint
labels are retained. The tree alone does not determine the link.

Write $d_v$ for the degree at a vertex and $n_v$ for the crossing power
restored by filling its circle. Theorem 1.1 proves that
$\sqrt{d_v^2+n_v^2}\ge630$ at every vertex is sufficient for a smooth,
complete hyperbolic filling. This allows a short or zero power at a
vertex of large degree. The strand connections must still be checked to
determine whether the remaining main link is a knot.

The proof begins with the topology. Each tree edge gives one octahedron
on each side of the projection plane. Explicit ideal vertices then give
eight positive tetrahedra per edge block and determine the face maps.
A contraction argument solves the filling equations uniformly in the
number of vertices. The meridian and disk longitude are traced through
the cells, including the two signs of a retained half twist.

For cone angle $2\pi c$, these curves have continued logarithmic periods

$$
U_v=-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v,
\qquad V_v=2i\tau_v,
\qquad U_v+p_vV_v=-2\pi i c,
\quad n_v=\epsilon_v-2p_v.
$$

The proof establishes the full periods, rather than just their
exponentials. At $c=1$ the primitive filling slope makes exactly one
angular turn, so its metric completion is smooth. The volume is the
absolute critical value of the stated classical potential. Corollary 6.1
bounds the core lengths and volume loss; Theorem 7.1 permits different
parameter radii at different vertices.

The only specialized companion input is the peripheral-volume
differential from Section 7 of
[Circle patterns and primitive fillings of augmented links](../marked-fillings/README.md).
The topology, deformation, primitive winding and metric completion are
proved here. A quantum volume limit requires the additional finite-sum
analysis in [Volume asymptotics for trees of crossing circles](../circle-tree-volume/README.md).

From the repository root:

```sh
python3 tools/build_papers.py circle-tree-geometry
python3 -I papers/circle-tree-geometry/check.py --output /tmp/circle-tree-geometry-check.json
```

The checker verifies the finite block identities, primitive multiplier
formulas and rational bounds. The topological and analytic arguments
remain written proofs in the paper.
