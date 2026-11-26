# A guide to the manuscript

[Read the manuscript PDF](../../manuscript/build/main.pdf). The [editable sources and build instructions](../../manuscript/README.md) are available alongside it.

The paper proves the volume conjecture for a specified family of knots built by composing two-strand tangles. It explains the finite quantum invariant, the hyperbolic cells, the estimates needed to control cancellation, and the passage from an augmented link to the final knot complement. This page introduces the construction before giving a route through that proof.

## The knot construction, without the shorthand

Start with two strands in a box whose four endpoints are labeled and kept in order. Insert an integer number of signed half-twists. A positive and a negative count give opposite crossing directions. Turn the box through a quarter-turn; this is the basic piece used in the construction.

Two boxes can be stacked in order, and a constructed box can itself be turned. After finitely many such operations, join the remaining outside endpoints by the prescribed cylindrical closure. Following the strands determines whether this produces a knot or a link. The theorem requires one component, with no closed component hidden inside a box.

The notation in the paper abbreviates these operations:

| Notation | Meaning |
| --- | --- |
| $R^n$ | Two strands with $n$ signed half-twists. |
| $T(F)$ | The quarter-turn of the tangle box $F$, with its endpoint order retained. |
| $h_i(n_i)=T(R^{n_i})$ | The $i$th basic twist piece. Different subscripts carry independent integers. |
| $FG$ | The ordered stack of $F$ and $G$. |
| $C(FG)$ | The prescribed closure of the four outside endpoints of that stack. |

These are operations on actual tangles. The notation does not mean that formal arithmetic with rational fractions has replaced an isotopy argument.

For the paper's main family, first stack two basic pieces. Thereafter one may turn a constructed box, stack two constructed boxes, or attach one additional basic piece on either side. The technical notes call a box obtained by these rules **completed**. This is a recursive name for a class of boxes; it does not mean that a Dehn filling has already been performed. Construct two such boxes $F$ and $G$, then close $FG$. The paper also handles its stated isolated stacks of at least three basic pieces.

## The theorem and its quantifiers

For each fixed permitted construction there is a threshold. Choose the twist integers independently, with either sign, beyond that threshold in absolute value, and choose their parities so that the endpoint pairing gives a knot. Fix all those integers. The theorem then proves

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
=\operatorname{Vol}(S^3\setminus K).
$$

Here $K$ is the resulting knot, $K_N(K)$ is the reduced Kashaev invariant at integer level $N$, and the right side is its hyperbolic complement volume. The limit includes even and odd levels and composite levels. The twist counts do not grow with $N$, and no restriction is imposed on their relative sizes. The threshold may depend on the entire construction.

To analyze the geometry, the proof first places an auxiliary crossing circle around each twist region. The resulting augmented link has a convenient decomposition into ideal hyperbolic cells. Filling an auxiliary circle means attaching a solid torus along the prescribed meridian so as to insert the twists. In the knot theorem **all auxiliary circles are filled**. The cusp of the knot itself remains unfilled. Thus the conclusion is about the knot complement, not a closed three-manifold.

Two companion results extend the paper's recursive family. The [strict-tree theorem](../../notes/actual_conway_all_strict_tree_long_twist_volume.md) proves the estimates for every expression passing a finite angle-feasibility test. The [net-twist theorem](../../notes/actual_conway_net_twist_volume.md) then reduces an arbitrary ordered cylindrical product closure to one of those expressions or to an elementary two-strand braid closure. In the former case, the size condition applies to the combined twist numbers produced by the reduction. The [results chapter](results.md) states that condition and gives an example. The earlier PDF chapters retain their own theorem and proof; the new quantitative chapter is described next.

## A bound independent of the tree size

The new local chapter proves that one sufficient twist threshold
works for every finite ordered circle tree. It starts with the
exact polynomial obtained by evaluating a subtree while retaining
its attaching variable. The proof then establishes its nonzero
value at zero, its normalized real and complex bounds, and the
nonzero leading term of the next trace. Each error is compared
with the current vertex's filling, rather than the total change
from all vertices.

The hypothesis is
\[
                   \max_v\frac{d_v}{d_v^2+n_v^2}\le2^{-120}.
\]
Thus every \(|n_v|\ge2^{119}\) suffices, subject to the knot test,
for any finite number of vertices. This explicit constant is
deliberately coarse. The local chapter includes the full induction
and the geometric path needed to identify its action with the
original complement volume. The earlier summed theorem below
remains a useful alternative with a better numerical constant.

## The quantitative circle-tree chapter

A further chapter treats a different explicit description of the
tangle construction: every vertex of an ordered tree carries an
integer braid, and each child tangle is turned before it is stacked
on the prescribed side of its parent braid. A terminal root gives
the cylindrical closure. The strand pairing must give one knot.

For vertex degree \(d_v\) and crossing power \(n_v\), the condition

\[
 \sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25}
\]

gives the volume limit. It also gives a uniform profile as the
meridian moves by order \(1/N\), with its first correction expressed
by the preferred cusp shape. The [full statement](../../notes/actual_all_circle_quantitative_volume.md)
defines every framing factor and gives numerical sufficient bounds.
Some short powers are allowed at sufficiently high-degree vertices;
the earlier long-twist chapters retain their own construction class.

The chapter illustrates an actual octahedral attachment and explains
why it recovers the original exterior. Positive tetrahedra continue
along the filling path until the primitive cone angle is \(2\pi\).
This constructs the smooth knot complement whose volume appears in
the quantum limit. Appendices E and F contain the full finite-sum, ordered-cut and
geometric-completion proofs, including their face maps, peripheral
words and uniform constants. The companion notes present the same
calculations separately.

## How to read the proof

The first part fixes the invariant normalization and derives the finite algebra of the tangle operations. A color is an integer label in that finite calculation. It is not an additional component of the final knot. The source formula retains values and first derivatives at repeated spectral points, which explains the use of Hermite interpolation. Newton polynomials make the allowed integer indices at a product explicit. These support conditions are kept before taking a continuum limit.

The geometric part associates normalized state variables with angles of ideal pyramids and prisms. An ideal vertex lies at infinity in hyperbolic space. Strict angle inequalities produce genuine cells, and the ordered endpoint data determine their face identifications. A strictly concave angle functional has a unique geometric maximum. The proof then follows actual paths on the cusps to identify the meridian and longitude used for filling.

The source estimates address a different issue: a signed sum can be much smaller than the sum of the absolute values of its terms. The exact reflection formula separates a central contribution from extra terms called aliases. The paper bounds all of those terms while preserving their finite supports. Concavity and supporting tangents reduce two important estimates to finite rational certificates.

![Supporting tangents used to control a single-piece attachment over its entire allowed state region.](../../manuscript/build/figures/attachment-tangents.png)

Near the geometric maximum, a complex asymptotic formula gives an exponential action, a nonzero leading coefficient and a controlled error. The paper calls this a local packet. The estimates outside that neighborhood show why the packet really determines the invariant; locating a critical point by itself would not rule out a missing or canceled contribution.

Finally, the filling transform is evaluated with all its Fourier modes and boundary terms. The marked meridian-longitude convention identifies the real part of its critical action with the volume after filling. This last normalization is what connects the finite invariant to the actual knot constructed at the beginning.

The technical appendices supply the finite algebra, analytic interpolation estimates, certificate details and marked geometric calibration used in this chain. They are intended to make the proof readable without treating links to working notes as substitutes for arguments.

## Reproduce the finite certificates

The quantitative chapter uses `python3 repro/run_research_checks.py curvature-fillings`. The [checks chapter](audits.md#checks-for-the-quantitative-volume-theorem) describes its three programs and their finite scope.

From the repository root, run:

```sh
python3 repro/verify.py --list
python3 repro/verify.py --plan
python3 repro/verify.py --output repro/results
```

The first two commands describe the checks. The third runs them serially, writes fresh results and compares them with the committed reference records. The [reproduction guide](../../repro/README.md) explains the software requirements and outputs; the [proof-input map](../../repro/PROOF_INPUTS.md) locates the written arguments behind each certificate.

These checks use rational bounds with explicit remainders, not a numerical search for maxima. They verify finite arithmetic used in the proof. They do not mechanically verify the topology, the invariant normalization, or every analytic step of the manuscript.

To build the paper and guide, use the commands in the [manuscript source guide](../../manuscript/README.md). The mathematical illustrations are supplied as editable TikZ sources as well as rendered assets. For the attachment diagram above, download the [vector PDF](../../manuscript/build/figures/attachment-tangents.pdf) or the [TikZ source](../../manuscript/figures/attachment-tangents.tex).
