# Independent tangle depth at every initial bridge gap

theorem, 31 October 2026. The [one-end plat family](general_one_end_layer_long_filling_volume.md) admits arbitrarily deep, independently chosen tangles at **every** first-layer bridge gap. The construction preserves its original marked cap and all core circle radii. It is checked on the literal source; it does not assert a theorem for arbitrary stacking or arbitrary plat diagrams.

## 1. The all-width, all-depth family

Fix $k\geq2$, put $L=k-1$, and choose any fixed depth vector $\mathbf m=(m_1,\ldots,m_L)$ with $m_j\geq0$. Number adjacent box slots from zero and set $s_j=2j-1$. Replace the $j$th box of the first $O$ layer by

$$
(s_j,s_j+1)^{m_j}s_j.\tag{1}
$$

Process $j=1,\ldots,L$ in its original order, retaining the middle $E^{\mathrm{right}}$ and final $O$ layers. The resulting literal word is

$$
\left[\prod_{j=1}^{L}(2j-1,2j)^{m_j}(2j-1)\right]
(2,4,\ldots,2L)(1,3,\ldots,2L-1),
\qquad R=3k-3+2\sum_{j=1}^{L}m_j.\tag{2}
$$

Products in (2) mean concatenation of slot lists in bottom-to-top order. A slot $s$ is conventional braid generator $\sigma_{s+1}$. Each added pair therefore means two independently powered boxes $\sigma_{2j}^{-2p}\sigma_{2j+1}^{-2q}$. Retain the standard adjacent cups/caps and mark the first original top cap.

The retained original first-$O$ boxes have fixed half twists $\epsilon_j\in\{1,-1\}$. All added boxes and the original middle/final layers have $\epsilon=0$. Every box has its own independent signed integer full-twist parameter. No region is merged, removed or assigned a dependent parameter.

**Theorem.** Every word (2) is an original certified simple-white marked plat, and its actual complete packing satisfies $Q$-balance at every port. Its prescribed parity gives a knot. For every fixed $k$, depth vector and sign pattern, there is a threshold $T(k,\mathbf m,\boldsymbol\epsilon)$ such that every independently signed fixed full-twist vector with all $|p_i|\geq T$ satisfies

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log\left|K_N\!\left(K_{k,\mathbf m}(\mathbf p)\right)\right|
=\operatorname{Vol}\!\left(S^3\setminus K_{k,\mathbf m}(\mathbf p)\right).\tag{3}
$$

This is the full original normalized invariant, both level parities and the entire charge sum, through the [full-source balance theorem](general_complete_radius_balance_filling_volume.md). Depths and twists are fixed before $N$ grows. No comparison between twist magnitudes, or threshold uniform in widths or depths, is asserted. Requiring every actual exponent to be divisible by $3$ gives a subfamily of minimal bridge number exactly $k$; that congruence is not required for (3).

More generally, the same closure works for any balanced certified core with the initial $O$ layer, no slot $0$, the first-cap mark, and ordered actual initial curvatures

$$
0=A_0\leq A_1\leq\cdots\leq A_L.
$$

The one-end cores satisfy strict inequalities, proved below. Neither this order nor balance is asserted for arbitrary initial-layer diagrams.

## 2. Exact simultaneous source dictionary

The original first-$O$ port $j$ is

$$
(a_{j-1},u,e_j,a_j),\tag{4}
$$

where $u$ is exterior, $a_0$ is the protected first-cap face, and $a_j$ is ordinary for $j\geq1$. Set $A=a_{j-1}$ and identify the eventual last face of the local prefix with the old core face $B=a_j$.

For $m_j=m>0$, let $f_0=u$ and let $b^{(0)}$ be the current bottom odd-gap face. Prefix pair $t$ has the exact original quartets

$$
\begin{aligned}
\text{slot }s_j &: (A,f_{t-1},f_t,b^{(t-1)}),\\
\text{slot }s_j+1 &: (f_t,b^{(t-1)},b^{(t)},u),
\qquad1\leq t\leq m.
\end{aligned}\tag{5}
$$

The retained old box becomes

$$
(A,f_m,e_j,b^{(m)}).\tag{6}
$$

Identify old $B$ with $b^{(m)}$. If $m_j=0$, retain (4) unchanged.

These formulas hold simultaneously. Before processing bridge $j$, earlier blocks have changed only gap positions up to $2j-1$. The face there is already the identified old $A$; the current bottom odd gap $2j+1$ has not changed. The even gaps $2j$ and $2j+2$ remain exterior $u$, the latter being exterior outright when $j=L$. The two local slots change only their own gaps. Thus (5) is the [original gap sweep](actual_original_marked_face_coefficient.md); after (6), the current middle gap contains old $e_j$. Induction on $j$ proves the entire first-layer dictionary. Every later core quartet is unchanged under these face identifications. The first marked face is never crossed because slot $0$ is absent.

Introduce symbols $C_{j,n}$ with $C_{j,0}=a_j$. For depth $m$,

$$
\begin{aligned}
b^{(t)}&=C_{j,2(m-t)},& f_t&=C_{j,2(m-t)+1},\\
b^{(0)}&=C_{j,2m},& f_0&=u.
\end{aligned}\tag{7}
$$

Every positive-$n$ symbol is a distinct new source face. In particular the old core disk $a_j$ is preserved as $b^{(m)}$; the original bottom face is now the outermost new chain disk. The same indexing is used by the actual packing.

## 3. An exact chain inside a finite triangular gap

Consider one original empty interstice $(A,u,B)$, with $u$ the baseline halfplane $Y\leq0$. First assume its actual curvatures satisfy $A,B>0$. Put the $A$-contact at $X=0$ and the $B$-contact on the positive side. The old radii are $1/A,1/B$, and the $B$ center is $(2/\sqrt{AB},1/B)$.

Inside this actual bounded curvilinear interstice define, for $n\geq0$,

$$
\begin{aligned}
C_n&=(\sqrt B+n\sqrt A)^2,& r_n&=C_n^{-1},\\
X_n&=\frac{2}{\sqrt A(\sqrt B+n\sqrt A)},& Y_n&=r_n.
\end{aligned}\tag{8}
$$

The $n=0$ disk is old $B$. In the positive coordinate $\sqrt{C/A}$, this is the affine translation $\sqrt{C_n/A}=\sqrt{B/A}+n$. That identity describes the circle-chain construction; it is not an identification with a global quantum torsor or a theorem about its periods.

Every disk is tangent to $u$ and old $A$. Consecutive disks obey

$$
X_n-X_{n+1}=2\sqrt{r_nr_{n+1}},
$$

so their tangencies are exact. For nonconsecutive indices, the squared-distance support slack is

$$
4r_nr_\ell\bigl[(n-\ell)^2-1\bigr]>0.\tag{9}
$$

Each next disk occupies the bounded gap toward the $A/u$ contact, with $0<X_{n+1}<X_n$. This actual contact order selects the sum of square roots in (8); the other algebraic branch is not used. The finite chain remains within the original empty interstice. Other old disks lie outside that face, and the new contact points avoid its three old vertices. Hence the only old finite contacts are with $A$, and with $B$ for $n=1$.

These coordinates describe the existing original gap. They are not an independent conjugation of a local quantum word. In the common marked plane, if the $A$-contact is $X_A$ and $\sigma=\operatorname{sign}(X_B-X_A)$, the actual new horizontal centers are $X_A+\sigma X_n$. Every old disk stays fixed.

For $j=1$, old $A=a_0$ is the upper protected line and its curvature is zero. Use the [exact parallel-line construction](general_marked_unit_chain_filling_volume.md): normalize the lines to $Y=0,2$, so old $B$ has radius $1$, and add $2m$ unit disks in the empty complementary component. Here $C_n=B=1$. No finite-circle expression is divided by $A=0$.

Insert $2m_j$ circles in each original first-$O$ triangular gap using (7)–(8). The original gap interiors are disjoint, including when their boundaries share old edges. The finite new disks remain in those gaps and avoid their old vertices, so different patches cannot overlap or acquire extra contacts. Each old triangular disk is replaced by the literal triangulated disk in (5)–(6), with the same boundary. The new sphere is simple, with exactly the source contact graph and cyclic order. The [proved packing construction](actual_smoothed_source_capacity_blocks.md), Sections 4–5, supplies its actual labeled right-angled certificate. Marked uniqueness identifies this unchanged-core packing with the complete source packing.

## 4. Balance at all new and modified ports

The only order needed is $B\geq A\geq0$. For $A>0$, put $s=\sqrt{B/A}\geq1$, so $C_n/A=(s+n)^2$.

A new odd port has outer curvatures $A,C_n$ for even $n\geq2$. Its positive middles are $C_{n-1},C_{n+1}$, except that the first prefix port replaces the latter by zero. Thus

$$
\frac{\max\{\text{middles}\}}{A+C_n}
\leq\frac{(s+n+1)^2}{1+(s+n)^2}\leq2,\tag{10}
$$

because $2(1+t^2)-(t+1)^2=(t-1)^2\geq0$. A new even port has outers $C_{n+1},0$ and middles $C_n,C_{n+2}$, for even $n\geq0$. Hence

$$
\frac{\max\{\text{middles}\}}{\text{sum of outers}}
=\left(\frac{s+n+2}{s+n+1}\right)^2\leq\frac94.\tag{11}
$$

Here $s+n+1\geq2$. Equivalently,

$$
\frac94-\left(\frac{t+1}{t}\right)^2
=\frac{(t-2)(5t+2)}{4t^2}\geq0\qquad(t\geq2).
$$

Apply the [zero-middle $9/4$ lemma](actual_zero_middle_nine_quarter_balance.md) after replacing the smaller middle by zero. The original $Q$ is nondecreasing in that middle, so (10)–(11) give strict balance at every new port, with gap $>1/2500$. For $A=0$, the parallel-line chain has all positive curvatures equal to $1$ and the same conclusion follows directly.

At the retained old port, only its input middle changes from zero to

$$
C_1=(\sqrt A+\sqrt B)^2\leq2(A+B).\tag{12}
$$

The output middle $E=e_j$ stays fixed. Its new action sum is $Q(A,C_1,B)+Q(A,E,B)$. Against the new target $\log C_1$, use the $9/4$ lemma with $C_1/(A+B)\leq2$ and then monotonicity in $E$. Against the old target $\log E$, use monotonicity in the changed input middle and the old strict balance. This controls both targets without assuming $E\geq1$. It also covers $A=0$, where $C_1=B$. The protected zeros remain exact.

Every later core port retains its weights and gap. The new minimum local margin is at least the smaller of the old minimum and $1/2500$, independently of depths. This does not assert a filling threshold uniform in the number of ports.

## 5. The one-end core has the required curvature order

Normalize its marked lines to $Y=0,2$. Its a-side circles have centers $(X_i,r_i)$ and curvatures $A_i=1/r_i$. The actual cyclic list of contacts on the lower white line is

$$
(a_0,a_1,\ldots,a_L,e_L,b_L,\ldots,b_1),
$$

with the marked contact at infinity and the fixed $e_L$ contact at $X=0$. The embedded complete packing therefore gives $X_1>\cdots>X_L>0$.

For $i<L$, the proved height formulas, with $z=z_i$ and $w=z_{i+1}$, give

$$
\frac{X_i}{r_i}=\frac{2zw}{z^2+w^2-z^2w^2}\leq2,\tag{13}
$$

since the denominator minus $zw$ is $(z-w)^2+zw(1-zw)\geq0$. Tangency gives $X_i-X_{i+1}=2\sqrt{r_ir_{i+1}}$. Its left side is strictly below $X_i\leq2r_i$, so $r_{i+1}<r_i$. Therefore $0=A_0<A_1<\cdots<A_L$. For $k=2$, there is no interior comparison and $A_1>0$ is immediate.

An independent proof uses the already established curvature ratios in the [one-end theorem](general_one_end_layer_long_filling_volume.md), equation (14). For $2\leq j<L$,

$$
\frac{A_j}{A_{j-1}}
=\frac{z_j^2(1+z_{j-1})^2}{z_{j-1}^2}>\frac{16}{9},
$$

using $z_j\geq2/3$ and $0<z_{j-1}<1$. Its last positive-root identity gives $A_L>A_{L-1}$, and the small cases are exact. Thus the order does not depend only on a new reading of the contact diagram.

## 6. Full source, independent twists and bridge number

Every inserted even exponent $-2p$ has identity endpoint permutation. All original odd first-$O$ boxes and other core boxes remain in their original order with their original half twists. The first marked cap is unchanged. Thus the original knot parity persists for arbitrary neighboring depth choices.

The total framing character is that of the extended original diagram. Its exact normalization is retained; it is not identified numerically with the core's character, and no equality of old and new invariants is claimed.

For each fixed width and depth vector, the certificate and balance meet the existing full-source theorem. Its entire spectral and charge argument proves (3) for all independent sufficiently long fixed signed twists, including the $2\sum_jm_j$ new parameters. This is not an inference from local angle volume or a selected contribution alone.

The same proof permits arbitrary fixed added half twists $\epsilon\in\{0,1,-1\}$ **provided the resulting actual endpoint permutation gives a knot**. Their extended framing and peripheral conventions are retained. The white source dictionary and complete packing do not change under these retained half twists. The concrete even additions in (1) are the convenient subfamily that automatically preserves the old knot parity.

If every full exponent is also a multiple of $3$, the [Fox certificate](actual_fox_coloring_exact_plat_bridge.md) counts exactly $3^k$ colors on the standard cup/cap register. The supplied plat then has minimal bridge number exactly $k$. These congruences allow independent large parameters of either sign and preserve the prescribed parity. They are required only for the bridge lower bound.

## Validation and scope

The construction gives arbitrary independent depth at every initial bridge gap; it does not cover arbitrary multilayer plat diagrams or prove a universal balance criterion.

The [focused audit](../experiments/audit_general_simultaneous_bridge_gap_filling_volume.py) and [recorded results](../experiments/general_simultaneous_bridge_gap_filling_volume_results.json) compare the closed dictionary against the original Morse compiler on 413 nonuniform charts, checking 11880 ports, 23760 triangles, 35640 edges, all marks and core permutations. Seven symbolic identities check tangent chains, support and inequalities. Twenty-five exact simultaneous seed packings supply 2333 circle/line supports, 168 new-port bounds and 32 modified targets. These checks supplement the general proof; finite samples do not establish its uniform or quantum conclusion.