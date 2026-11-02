# Local degree and twist bounds for circle-tree volume limits

This paper proves a full invariant asymptotic and actual hyperbolic volume
limit for fixed literal ordered circle trees whose endpoint tracing gives
one main knot and no internal closed component. Every product junction
carries a crossing circle. The diagram and signed powers are fixed before
the level tends to infinity.

Theorem 1.1 (`dt:main`) uses the finite directed criterion in Section 2.
One chooses a final root and a positive real-decay bound for each outgoing
subtree polynomial. The proof keeps its exact value at zero, all Newton
indices and repeated-root normals. The final root has no outgoing bound.

Corollary 1.2 (`dt:mixed`) gives the sufficient alternative

\[
 d_v\ge2^{28}\quad\text{or}\quad |n_v|\ge2^{27}
 \qquad\text{at every vertex}.
\]

The choice may vary from vertex to vertex; large-degree vertices may keep
zero powers. Corollary 9.1 (`dt:local`) recovers the older condition
\(\max_v d_v/(d_v^2+n_v^2)\le2^{-120}\) directly from this alternative.
Its separate tiny-disk induction is unnecessary here. The summed
criterion is neither assumed nor replaced by a bound depending on the
number of vertices.

The full leading term includes the exact unit scalar, a nonzero constant
through both level parities, and the factor \(N^{3/2}\). The normalized
microscopic main-meridian profile is \(1+O_R(N^{-1})\) for
\(M=q_N^s\), \(|s|\le R<1\). No fixed meridian neighborhood, all-orders
expansion, longitude factor or larger strict Conway grammar is asserted.

## Inputs

- [Moving-meridian Newton calculus](../meridian-tangles/main.tex),
  Proposition 6.1 and equation (6.4), Theorem 7.1, Proposition 8.1:
  crossing/full trace, original tree contraction and exact scalar ledger.
- [Summed circle-tree estimates](../circle-tree-asymptotics/main.tex),
  Lemma 2.1, Sections 3–4 and Section 6.1: unconditional polynomial norms,
  complex edge packet, angular bounds and exact single-grid Fourier
  conversion. Their proofs do not require the summed criterion.
- [Canonical factorial interpolation](../conway-asymptotics/factorial.tex),
  Lemma 2.1: the holomorphic interpolation underlying that edge packet.
- [Circle-tree geometry](../circle-tree-geometry/main.tex), Theorem 1.1:
  the same primitive smooth filling and absolute action-volume equality.
  The directed cutoff forces its degree-and-twist threshold and places
  the restored solution in its uniqueness chart.

The new conditional rectangle estimate and finite-message induction are
written in [kernels.tex](kernels.tex) and [recursion.tex](recursion.tex).
[Applications](applications.tex) give all-degree inequalities, literal
pairings for even stacks of added leaves, and a fixed star illustrating
the root exemption. Added leaves preserve the endpoint pairing; they can
change the knot type.

## Finite reproduction

From the repository root, with Python and mpmath installed:

```sh
python3 papers/directed-tree-asymptotics/check.py \
    --output /tmp/directed-tree-check.json
```

The source-pinned JSON separates exact rational budgets and pairing
identities from high-precision finite recursion comparisons. These checks
do not establish uniform contour estimates, asymptotics or geometry.
