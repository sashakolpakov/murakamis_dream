# An exact bridge-number certificate for odd-prime-divisible plat boxes

elementary certificate, 31 October 2026. This result is independent of the source asymptotics and circle-packing balance condition. It identifies exact-bridge congruence subfamilies when the prescribed plat parity gives a knot. Geometric balance must be established separately.

## 1. Fox colors and the signed crossing map

Fix an odd prime $p$ and work over $\mathbb F_p$. A Fox coloring assigns a field element to each diagram arc between undercrossings. At a crossing, if $a$ is the overstrand color and $b,c$ are the two understrand colors, the condition is

$$
b+c=2a.\tag{1}
$$

All colorings, including the $p$ constant colorings of a knot, are counted. The rule is unoriented and unchanged on reversing a strand orientation.

Follow a braid in its actual geometric slot order. Choose the positive crossing convention in which an incoming ordered pair $(a,b)$ becomes $(2a-b,a)$. Its matrix and inverse are

$$
\begin{aligned}
T&=\begin{pmatrix}2&-1\\1&0\end{pmatrix}=I+A,
&A&=\begin{pmatrix}1&-1\\1&-1\end{pmatrix},\qquad A^2=0,\\
T^{-1}&=\begin{pmatrix}0&1\\-1&2\end{pmatrix}=I-A.
\end{aligned}\tag{2}
$$

The opposite naming convention interchanges $T$ and $T^{-1}$ and has the same consequence. For every signed integer $e$,

$$
T^e=I+eA.\tag{3}
$$

This follows by the binomial formula for $e\geq0$ and the exact inverse $I-A$ for negative $e$. Thus $p\mid e$ implies $T^e=I$ over $\mathbb F_p$. At a crossing on slot $j$, embed this two-by-two block in the identity on the other slots; the same identity holds there.

This is an identity on the ordered color register, not on strand labels. The underlying endpoint permutation remains the transposition of the two slots when $e$ is odd. In particular, $T^p=I$ for odd $p$ does not make the tangle an identity tangle or a permutation identity.

## 2. Coloring invariance, including constant colorings

The local rules give bijections of coloring sets under all three Reidemeister moves, keeping exterior colors fixed.

For type I, (1) forces the new short arc to have the old arc's color, so the extension is unique. For type II, write $s_a(b)=2a-b$. The strand passing under the other twice undergoes $s_a$ twice, and $s_a^2=I$; its intermediate color is uniquely determined. For type III, the exact identity

$$
s_a\circ s_b=s_{s_a(b)}\circ s_a.\tag{4}
$$

follows by evaluating both sides on $c$: both give $2a-2b+c$. This is the crossing-rule relation for the two three-crossing arrangements, and every intermediate color is uniquely determined from the exterior data. It proves the local bijection, with all orientation versions covered because (1) is unoriented and $s_a$ is its own inverse.

Thus the number $\operatorname{Col}_p(K)$ is invariant under diagram moves for the same unframed knot. The bijections preserve constant colorings, so counting all colors introduces no diagram-dependent convention. The usual Reidemeister characterization of diagrams of the same knot is the underlying diagram-equivalence fact used here.

## 3. Exact count for the supplied standard plat

Consider a standard $2k$-plat whose genuine crossings all lie in specified adjacent-strand boxes $\sigma_{j_i+1}^{e_i}$. Here the physical slots are numbered from $0$, so slot $j$ is the conventional generator $\sigma_{j+1}$. Use the standard adjacent cup and cap pairs

$$
(0,1),(2,3),\ldots,(2k-2,2k-1)
$$

in the same geometric slot order. Assume every $e_i$ is divisible by $p$. There are no extra uncontrolled crossings outside these boxes; any such crossings would have to be included in the color propagation separately.

At one end each cup forces its two colors equal. The initial register is exactly

$$
(a_0,a_0,a_1,a_1,\ldots,a_{k-1},a_{k-1}),
\qquad(a_0,\ldots,a_{k-1})\in\mathbb F_p^k.\tag{5}
$$

Every full box acts as the identity by (3), even though its physical endpoint permutation can be nontrivial. The opposite register is again (5), so all standard cap constraints hold automatically. These are topological arc constraints; the quantum marked-cap matrix does not modify the underlying diagram or its Fox coloring rule.

Propagation through the actual braid is invertible and uniquely fixes every intermediate arc color. Conversely, every coloring restricts to one register (5). Hence the count is exactly

$$
\operatorname{Col}_p(\text{plat})=p^k.\tag{6}
$$

No strand permutation is dropped: the register uses geometric slot positions at each horizontal section. One must not propagate colors by the bare permutation after already applying the crossing matrices.

The link component count is separate. If $\tau$ maps lower slot labels to upper labels, pull the upper adjacent matching back by $\tau$. The union of the lower matching $M$ and $\tau^{-1}M\tau$ is a two-colored $2$-regular multigraph on the $2k$ lower endpoints. Its cycles are precisely the plat components. Thus the prescribed parity yields a knot exactly when this graph is connected. Only $e_i$ modulo $2$ enters $\tau$.

## 4. Any knot with bridge number $b$ has at most $p^b$ colorings

Take a diagram with $b$ overpassing bridges. Its overpasses have no undercrossings and carry $b$ individual colors. Every underpass starts at an endpoint of an overpass. Starting with that known endpoint color, follow the underpass: at each crossing the overpass color $a$ is already known, and (1) updates the traveling color by $c\mapsto2a-c$. All underpass arc colors are therefore determined by the $b$ chosen overpass colors. At their opposite endpoints the remaining matching conditions may impose restrictions, but never create an additional choice. Restriction to the overpasses is injective, so

$$
\operatorname{Col}_p(K)\leq p^b.\tag{7}
$$

This also covers the one-bridge unknot with no crossings. A geometric $b$-bridge presentation has its usual diagram with $b$ overpasses, so (7) applies to the minimal bridge number. Conversely, the supplied $2k$-plat is a $k$-bridge presentation: keep its braid monotone and use its $k$ caps as the only maxima. Its knot therefore has bridge number at most $k$.

If the component test in Section 3 gives a knot $K$, invariance, (6), and (7) imply

$$
p^k=\operatorname{Col}_p(K)\leq p^{\operatorname{br}(K)},
\qquad\operatorname{br}(K)\geq k,
\qquad\boxed{\operatorname{br}(K)=k}.\tag{8}
$$

The conclusion is minimal bridge number, not only a supplied plat width.

## 5. Compatibility with the actual signed filling parameters

In the original source convention the full box exponent is

$$
e_i=n_i=\epsilon_i-2P_i,
$$

where $\epsilon_i$ is the fixed half-twist parity and $P_i$ is the signed integer full-twist parameter. Since $p$ is odd, $2$ is invertible modulo $p$. The condition $p\mid n_i$ is precisely

$$
P_i\equiv\epsilon_i/2\pmod p.\tag{9}
$$

It does not change $n_i\bmod2$ or the prescribed component permutation. Each congruence class contains arbitrarily large positive and negative $P_i$, independently at every box. It is therefore compatible with any fixed parity pattern already proved to give a knot and any independently sufficiently long signed-twist threshold. The prime $p=3$ already suffices.

For example, the [simple-white family's component-parity construction](general_simple_white_plat_class.md), Section 3, can be combined with (9): the first $O$ layer has odd exponents and the other boxes even; its width-two example uses the stated first-slot odd exponent. The [balanced reduced-layer family](general_reduced_layer_long_filling_volume.md) establishes the separate geometry for $k\geq4$. In its congruence subfamilies, this coloring argument certifies minimal bridge number exactly $k$. The analytic volume theorem itself has no extra congruence restriction.

## Validation and scope

The Fox certificate does not imply circle-packing balance.