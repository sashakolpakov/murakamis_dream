# Arbitrary-depth marked unit-chain extensions of balanced plats

Independently reviewed structural theorem, 31 October 2026. A balanced original plat can admit arbitrarily many additional independently twisted regions at the **same fixed bridge width**. The construction below preserves its original marked cap and every old circle radius. It is a literal source operation, not a claim about arbitrary stacking of plats or abstract gluing of matched graphs.

## 1. Hypotheses and full-invariant conclusion

Let $D$ be a fixed original flat $2k$-plat, $k\geq2$, with $R$ ordered crossing regions. Assume:

- Its first zero-based box slot is $1$.
- No box uses slot $0$.
- The first original top cap, on slots $(0,1)$, is marked.
- Its white sphere is simple, carries the actual labeled right-angled certificate, and its one complete marked packing satisfies the [complete-radius balance condition](general_complete_radius_balance_filling_volume.md) at every port.

Retain every original half-twist sign and the original cup/cap conventions. For any integer $m\geq0$, form the literal bottom-to-top word

$$
D^{(m)}=(1,2)^mD.\tag{1}
$$

Each new box has half-twist $\epsilon=0$ and an independent signed integer full-twist parameter $p$, hence actual braid exponent $-2p$. Slot $j$ is conventional braid generator $\sigma_{j+1}$, so the added braid is

$$
\prod_{j=1}^{m}\sigma_2^{-2p_{j,1}}\sigma_3^{-2p_{j,2}}.
$$

No old box is combined, deleted, moved or reinterpreted. The new number of crossing regions is $R+2m$.

**Theorem.** The original marked diagram $D^{(m)}$ is again certified and simple-white, and every port satisfies complete-radius balance. If the original parity gives a knot, the extended diagram still gives a knot. For each fixed $m$, there is a threshold $T(D,m)$ such that every independently signed fixed filling vector with all parameters above that threshold in absolute value satisfies

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log\left|K_N\!\left(K_{D^{(m)},\mathbf p}\right)\right|
=\operatorname{Vol}\!\left(S^3\setminus K_{D^{(m)},\mathbf p}\right).\tag{2}
$$

This is the full original normalized invariant, both level parities and the entire original charge sum, through the general balance theorem. Every twist is fixed before $N\to\infty$; no comparison of their magnitudes is required. The threshold is not asserted to be uniform in $m$.

In particular, the [one-end-layer cores](general_one_end_layer_long_filling_volume.md) $O_kE_k^{\mathrm{right}}O_k$ satisfy these hypotheses. Thus for every fixed $k\geq2$ and every $m\geq0$, (1) supplies $3k-3+2m$ independently long signed twist regions. This is arbitrary depth at fixed width. The added alternating tangle acts on the first four physical strands; the claim does not say that each added layer spans all $2k$ strands.

The case $m=0$ is unchanged. Assume $m\geq1$ in the source patch and balance arguments of Sections 2–4.

## 2. Exact original gap dictionary

The absence of slot $0$ means the bottom odd-gap face $v$ on slots $(0,1)$ remains the first top-cap face. It is the protected face paired with the exterior $u$. Before the first box, every internal even gap belongs to $u$. Hence the first port of $D$ is

$$
(v,u,e,a),\tag{3}
$$

where $a$ is the bottom odd-gap face on slots $(2,3)$. Simplicity makes $e$ an ordinary face distinct from $u,v,a$; $a$ is also ordinary. All other regions and cyclic port orders are those of $D$.

For the prefix, let $a^{(0)}$ be the original bottom face in gap $3$, set $f_0=u$, and let $f_j,a^{(j)}$ be the new faces created by the $j$th pair $(1,2)$. The literal sweep gives

$$
\begin{aligned}
\text{slot }1_j &: (v,f_{j-1},f_j,a^{(j-1)}),\\
\text{slot }2_j &: (f_j,a^{(j-1)},a^{(j)},u),
\qquad1\leq j\leq m.
\end{aligned}\tag{4}
$$

The right outer region at slot $2$ is still $u$: the prefix never crosses the next even gap, whether it is internal for $k>2$ or exterior for $k=2$. Identify the old core face $a$ with $a^{(m)}$. The first core port becomes

$$
(v,f_m,e,a^{(m)}).\tag{5}
$$

Every later core quartet is unchanged under that one face relabeling. The mark remains $u,v$. This is an exact instance of the [original Morse face dictionary](actual_original_marked_face_coefficient.md), without isotopy, stabilization or a change to the quantum marked cap.

## 3. The actual empty gap and complete packing

Normalize the old marked disks as the outside halfplanes below $Y=0$ and above $Y=2$. The original triangle $(v,u,a)$ implies that $a$ is tangent to both lines and has radius $1$. Translate its center to $(0,1)$.

This triangle is one of the two marked-edge triangular interstices. Choose the one global horizontal reflection so it is the empty right complementary component of the marked strip. The unit disk $a$ touches both strip boundaries and separates the strip into left and right components. Every other old finite disk lies in the left component: otherwise the actual triangular interstice would contain another disk or the embedded contact graph would cross its boundary. The right component is therefore empty. This uses the actual labeled embedded packing, not an assumed gap in an arbitrary developed configuration.

Leave every old disk unchanged. For $0\leq j\leq m$, set

$$
\operatorname{center}(a^{(j)})=(4(m-j),1),\qquad
\operatorname{radius}(a^{(j)})=1,
$$

where $a^{(m)}$ is the old disk $a$. For $1\leq j\leq m$, set

$$
\operatorname{center}(f_j)=(4(m-j)+2,1),\qquad
\operatorname{radius}(f_j)=1.\tag{6}
$$

The $2m$ new disks form a chain in the actual empty right component. Consecutive disks are tangent, and nonconsecutive disks have disjoint interiors and no contact. Every new disk touches both marked lines. Only $f_m$ touches an old finite disk, namely $a^{(m)}$. Thus no unintended old/new contact occurs. More explicitly, if another old disk has center $(X,Y)$, then $X<0$. Its squared support slack against a new unit disk at $(s,1)$, $s\geq2$, equals its nonnegative slack against $a$ plus $s^2-2sX>0$.

The triangles in (4)–(5) are exactly the gaps above and below this chain. At the far right, $(v,u,a^{(0)})$ replaces the old unbounded triangle $(v,u,a)$. The other triangle $(v,a,e)$ of the old first port is unchanged. Equivalently, one old triangular disk has been replaced by a triangulated disk with $2m$ additional vertices and the same original boundary. The new source sphere is simple, and the displayed packing realizes precisely its contact graph and cyclic order.

The [proved simple-white packing construction](actual_smoothed_source_capacity_blocks.md), Sections 4–5, supplies its actual labeled right-angled cut balls. Marked uniqueness and contact-center development identify this packing with the normalized complete source packing. Every old ordinary curvature is unchanged; every new curvature equals $1$. No separate radii are chosen for different ports.

## 4. Exact balance at every port

Use the original half-degree triangle action and put

$$
C_0=Q(0,1,1)=\frac{2G}{\pi}>0,\qquad Q(0,0,1)=0,\tag{7}
$$

where $G$ is Catalan's constant. These constants have the [original source normalization](actual_zero_middle_nine_quarter_balance.md).

The first new slot-$1$ port has outer weights $(0,1)$ and middle weights $(0,1)$, hence balance gap $C_0$. Every later new slot-$1$ port has outer weights $(0,1)$ and middle weights $(1,1)$, hence gap $2C_0$. Every new slot-$2$ port has outer weights $(1,0)$ and middle weights $(1,1)$, again gap $2C_0$.

For the modified first core port, the outer curvatures are $v=0$ and $a=1$. Its old middles were $0$ and $E=\operatorname{curvature}(e)>0$. Every finite disk inside the height-$2$ strip has radius at most $1$, so $E\geq1$. Before and after the modification, the largest positive middle logarithm is therefore $\log E$. The old action sum was $Q(0,E,1)$; the new sum is

$$
Q(0,1,1)+Q(0,E,1),\tag{8}
$$

larger by exactly $C_0$. The old strict balance is preserved. All other core ports retain their weights and balance gaps exactly.

The minimum local balance margin of $D^{(m)}$ is at least the smaller of the old minimum margin and $C_0$, independently of $m$. This does not make the analytic filling threshold uniform in $m$: the number of ports, source constants and geometric filling data still depend on the extended diagram.

## 5. Retained phases, knots and bridge number

Every new exponent $-2p$ is even, of either sign, so its endpoint permutation is the identity. The new boxes do not change the original component graph. Every original half twist remains in its original box, and the marked cap remains fixed. These even exponents are independent genuine crossing regions; their trivial endpoint permutation is not an identity on the finite quantum source.

For each fixed extended diagram, its certificate and proved balance let the [full-source theorem](general_complete_radius_balance_filling_volume.md) control the entire one-sided remainder and apply the original all-charge filling theorem. This proves (2), including the original normalization and sufficiently long smooth hyperbolic filling. The conclusion is not inferred from the packing picture alone.

If the original parity gives a knot and all old and new full exponents are additionally divisible by $3$, the [Fox-coloring certificate](actual_fox_coloring_exact_plat_bridge.md) gives exactly $3^k$ colorings. The supplied $2k$-plat then has minimal bridge number exactly $k$. For the new boxes, this condition is $p\equiv0\pmod3$. Every required congruence allows independent arbitrarily large positive and negative parameters. It is used only for the bridge lower bound, not for the volume theorem.

## Validation and scope

The operation applies to every core satisfying the stated hypotheses, not only the one-end template. It does not prove balance for arbitrary multilayer plats or arbitrary marks. It preserves the original protected edge and all old disk coordinates; no generic re-framing invariance is used.

Root and an independent source reviewer checked the exact gap dictionary, actual empty complementary marked gap, circle supports and cyclic order, old first-port replacement, uniform local balance margin, retained half twists and mark, knot parity, Fox condition and nonuniform filling threshold. The focused audit checks finite literal core/depth charts and exact width-two/width-three packing extensions. These checks supplement the general source patch and empty-gap proof; they do not infer the uniform or quantum theorem by sampling.

The [focused exact audit](../experiments/audit_general_marked_unit_chain_filling_volume.py) and [recorded results](../experiments/general_marked_unit_chain_filling_volume_results.json) reproduce 56 original extended charts, 1176 quartets, 2352 triangles, 3528 edges and 56 knot-parity checks, together with 12 exact seed extensions, 1084 circle/line pair supports, 84 new unit-port tests and 12 changed core-port tests. Root and the independent source reviewer read the complete proof and audit code; an independent redirected replay reproduced the exact counts.
