# Reduced Frobenius hubs, strict support, and a positive complete-character kernel

31 October 2026. Internally reviewed source theorem. The calculations use
the full repeated-root algebra, with all independent physical leaf colors
and first normal coefficients. They give a sharp strictness criterion and
an exact recursive source interface. No tangle isotopy is inferred from
an algebraic rerooting.

The flag-free case reduces to source estimates already proved for the
completed grammar and isolated three-leaf closure. The case with one
flagged leaf at every hub is covered by the companion
[decorated-character spectral theorem](actual_conway_decorated_character_spectral_closure.md).
Mixed flagged and unflagged hubs retain a distinct unresolved analytic
operation, specified below. This note itself does not assemble a filling
or knot-volume theorem.

## 1. Source conventions and the exact local tensor

Let \(d=N-1\), \(\mathcal H_N=\mathbb C[z]/(2T_N(z/2)+2)\), and
\(e_r=\widehat B_r\), \(0\le r\le d\). Use the physical turn \(T\),
marked functional \(\phi\), and independent leaves
\[
h_i=T(p_i),\qquad p_i=R^{\epsilon_i}L_{j_i},\qquad
1\le j_i\le N,\quad \epsilon_i\in\{0,\pm1\}.
\]
No two colors or signs are identified. The proved source rules are
\[
\begin{gathered}
Te_r=e_{d-r},\qquad \phi(e_i e_j)=\mathbf1_{i+j=d},\\
e_i e_j=\sum_{r=\max(i,j)}^{i+j}\mu_{i,j,r}e_r,\qquad
\mu_{i,j,r}=
\frac{s_{i+j}s_r}{s_i s_j s_{r-i}s_{r-j}s_{i+j-r}}>0
\quad(i+j\le d),\\
e_i e_j=0\quad(i+j>d),\qquad
s_r=\prod_{t=1}^r2\sin\frac{\pi t}{N},\quad s_0=1.
\end{gathered}\tag{1}
\]
These are the [exact source compiler](actual_conway_single_leaf_source_composition.md),
§1, and the underlying [positive Newton multiplication theorem](actual_positive_newton_multiplication.md).
Their proof is polynomial with multiplicities, so first normal
coefficients are retained.

The symmetric trivalent tensor \(C(i,j,k)=\phi(e_i e_j e_k)\) is the
exact factorial tensor in the [isolated three-leaf source](actual_conway_isolated_three_leaf_long_twist_volume.md),
§1. Its support is
\[
i+j,\ i+k,\ j+k\le d,\qquad i+j+k\ge d.
\tag{2}
\]
Every supported entry is positive. In scaled strict coordinates its
domain is pairwise sums less than one and total sum greater than one.
Thus a product gate with inputs \(x,y\) and output \(z\) is this tensor
with legs \(x,y,1-z\):
\[
\max(x,y)<z<x+y<1.
\tag{3}
\]
This identifies strict support without relying on an equality between
signed scalar sums.

Write \(\mathbf J_{ij}=\mathbf1_{i+j=d}\), so
\(\mathbf J^{-1}=\mathbf J\). Internal propagation with no turn is
\(\mathbf J\); an inserted turn gives \(\mathbf JT=I\). A leaf with
edge parity \(\sigma\) supplies \(T^\sigma h_i\). These conventions
follow by raising the output index of \(C\) with \(\mathbf J\) in (1).

## 2. An exact product-hub support lemma

For \(n\) fixed basis inputs \(e_{i_1},\ldots,e_{i_n}\), the product is
zero unless
\[
i_p+i_q\le d\qquad(p\ne q).
\tag{4}
\]
If (4) holds, its positive support is exactly
\[
\left[\max_p i_p,\ \min\!\left(d,\sum_p i_p\right)\right]\cap\mathbb Z.
\tag{5}
\]
For \(n=1\) this is its singleton support. Necessity of (4) follows by
associating a violating pair first. For sufficiency, use any binary
parenthesization. Each child has the interval (5) inductively. The two
lower endpoints have sum at most \(d\), by (4); the exact interval
compiler therefore gives (5) for the parent. Every coefficient asserted
positive has a positive summand. This proves the result for every
grouping, not merely after choosing a favorable grouping.

Consequently the \(k\)-valent tensor
\(C_k(\mathbf i)=\phi(\prod_p e_{i_p})\) has positive support exactly
\[
\sum_p i_p\ge d,\qquad i_p+i_q\le d\quad(p\ne q).
\tag{6}
\]
For \(k=2\) this is \(i_1+i_2=d\); for \(k\ge3\) it is a nontrivial
positive tensor. Its value is defined by (1), including all scalar
factors, not by a new normalization.

There is a corresponding strict statement with fixed external labels
\(0<x_p<1\). A product of \(n\ge2\) inputs admits strict intermediate
gates with prescribed output \(z\) precisely when
\[
x_p+x_q<1\quad(p\ne q),\qquad
\max_p x_p<z<\min\!\left(1,\sum_p x_p\right).
\tag{7}
\]
This holds for every binary parenthesization. Necessity follows by
following any two leaves to their first common gate: its two input
labels are at least those leaf labels and have sum less than one.
The output is strictly larger than each input and strictly smaller
than their sum, which also gives the remaining inequalities.

For constructive sufficiency, for a child set \(S\) put
\[
L_S=\max_{p\in S}x_p,\qquad
U_S=\min\!\left(1,\sum_{p\in S}x_p\right).
\]
A nonsingleton child can take every value in \((L_S,U_S)\); a singleton
takes its fixed value. At a parent with target \(z\), restrict both
child values below \(z\). Their available sum has lower endpoint
\(L_1+L_2<1\) and upper endpoint
\(\min(U_1,z)+\min(U_2,z)>z\). Both child sets are nonempty because
\(z>L_i\). Thus choose a sum strictly between \(z\) and one. If both
children are singletons, their single sum already lies there. This
gives the strict parent gate and then strict children by induction.

A closed \(k\)-hub, \(k\ge3\), in any resolution into trivalent product
tensors, admits strict internal wires precisely when
\[
\sum_p x_p>1,\qquad x_p+x_q<1\quad(p\ne q).
\tag{8}
\]
Split at any root pairing. The two child intervals from (7), with
singleton exceptions, contain values summing to one: their lower
endpoint sum is less than one, and their upper endpoint sum is greater
than one. This proves sufficiency. Necessity follows from the same
gate inequalities and the final complementary relation. For \(k=2\)
the root pairing is the equality \(x_1+x_2=1\), with no retained gate;
that exception remains separate.

In particular, collapsing or resolving an internal edge with no turn
preserves strict feasibility at the same external labels. This is the
strict-support justification that an appeal to associativity alone
would not supply.

## 3. The reduced unrooted source and its sharp strictness criterion

Start with a literal cylindrical expression \(C(FG)\) with \(H\ge3\)
original leaves. Contract unary turn chains modulo \(T^2=I\) and
suppress the degree-two closing vertex. At each multiplication use
the tensor and metric conventions of §1. This gives an unrooted
trivalent tree with independently labelled physical leaves and turn
parities on its edges.

Collapse every internal edge of parity zero. Adjacent symmetric
tensors contract through \(\mathbf J\) to \(C_k\), by Frobenius
associativity. The resulting tree has product hubs of valence at
least three, all hub-to-hub edges of parity one, and a flag
\(\sigma_i\) on each leaf edge:
\[
\sigma_i=0:\ h_i=T(p_i),\qquad
\sigma_i=1:\ Th_i=p_i.
\tag{9}
\]
The reduced tree is unique up to isomorphism with the original leaf
labels retained: it is obtained by contracting the components of the
zero-parity internal edges. This uniqueness is only for the named
algebraic moves, not a classification modulo every identity of
\(\mathcal H_N\) or every tangle isotopy.

**Strict-hub theorem.** The closed expression has a strict reduced
state if and only if each reduced hub is incident to at most one
flagged leaf.

Necessity follows from (8). Two flagged original leaves have leg labels
\(1-a_i>1/2\) and \(1-a_j>1/2\), violating their pair inequality. The
hub resolution lemma makes this argument independent of the initial
parenthesization.

For sufficiency, first suppose there is a hub-to-hub edge and root
there. Looking toward a parent edge, each hub has at least two other
incident branches. A leaf branch has type \(L=(0,1/2)\) if unflagged
and \(H=(1/2,1)\) if flagged. Inductively, a child hub has product output
of type \(H\) if it contains one flagged leaf, and \(A=(0,1)\)
otherwise: incoming hub branches have types \(T(H)=L\) or \(T(A)=A\),
and cannot supply an \(H\) input. At most one \(H\) input is allowed,
and the exact strict table gives precisely these \(H/A\) outputs.
Across the root \(T\) edge the possible closed pairs are
\[
A/A,\qquad A/L,\qquad H/A,\qquad H/L,
\tag{10}
\]
all strict. These are the original full type intervals, not selected
pointwise labels.

For a single hub, no flag means a product of \(H\ge3\) leaves of type
\(L\); exposing one leaf gives the strict pair \(L/A\). With one flag
expose that leaf, giving \(H/A\). This proves sufficiency. The local
resolution lemma transports the resulting strict state back to the
original syntax.

With two original leaves there is no hub; the only datum is the edge
turn parity. The strict case has parity one and closed pair \(L/H\).
This two-leaf case is separate from the \(H\ge3\) packet and from
knot-component claims.

## 4. Exact recursive interface and the extent of grammar reduction

Choose a flagged leaf at a root hub when one is present. For any other
hub \(v\), let \(Q_v\) be its outgoing coupon after the edge \(T\)
toward its parent. Its exact recursion is
\[
Q_v=
\begin{cases}
T\!\left(p_{i(v)}\prod_w Q_w\prod_l h_l\right),
 &\text{if \(v\) has a flagged leaf \(i(v)\)},\\
T\!\left(\prod_w Q_w\prod_l h_l\right),
 &\text{if \(v\) has no flagged leaf}.
\end{cases}
\tag{11}
\]
Products contain all other incident branches, with original labels.
They have at least one factor in the first case and at least two in
the second. The final scalar at the chosen flagged root is
\[
Z_N=\phi\!\left(p_0\prod_w Q_w\prod_l h_l\right).
\tag{12}
\]
These are exact identities for arbitrary independent colors and half
signs, including all normal directions. The child messages have type
\(L\) in the first case of (11) and \(A\) in the second. These two
operators, rather than arbitrary matrices or a semisimple quotient,
are the compositional spectral interface.

The recursive notation may initially give a closing character with
only one decorated child. This is not an extra \(H\ge3\) boundary case.
Writing \(D_i[E]=T(p_iE)\), self-adjointness gives exactly
\[
\phi(p_0D_1[E])=\phi((Tp_0)p_1E)=\phi(h_0p_1E).
\tag{13}
\]
If \(E=1\), there are exactly two physical leaves and no hub. If \(E\)
is a nonempty product of recursive child coupons, the right side is
rooted at character \(p_1\), with ordinary satellite \(h_0\) and all
factors of \(E\). There are at least two root satellite factors and
hence valence at least three. Every physical color and half sign is
retained. The turn moves across the exposed pairing, not through a
product.

If there are no flagged leaves, root at any internal edge, or split
a single hub into two groups of at least two leaves. Both open sides
belong to
\[
E\ ::=\ hh\ \mid\ T(E)\ \mid\ EE\ \mid\ hE\ \mid\ Eh.
\tag{14}
\]
Thus \(H\ge4\) reduces as a full source to the
[completed/completed-root grammar](actual_arborescent_single_leaf_long_twist_volume.md);
\(H=3\) is the [isolated \(C(hhh)\) case](actual_conway_isolated_three_leaf_long_twist_volume.md).
All independent colors remain. The root cut exists because each side
of an internal edge contains at least two leaves. This is a source
reduction, not a topological move.

A single hub with one flag is the proved root star:
\[
\phi\!\left(p_0\prod_i h_i\right)
=\phi\!\left(h_0T\!\left(\prod_i h_i\right)\right).
\tag{15}
\]
If there is precisely one flagged hub but further hubs, it is
\(C(h_0T(E))\) with a completed child \(E\). Multiple flagged hubs
are governed by (11). In general they do not disappear by the named
Frobenius rerooting, associativity, commutativity and \(T^2\) moves:
those moves preserve the reduced flagged tree. This is an obstruction
to that restricted simplification procedure, not to additional source
identities or to the desired asymptotic theorem.

For example, the two-hub source
\[
\phi\!\left((Th_1)h_2\,T((Th_3)h_4)\right)
\tag{16}
\]
is strict and has one flagged and one unflagged leaf at each hub.
Under the named moves it is neither a flag-free completed-root tree
nor a single-hub root star. This is a structural witness, not a
numerical knot experiment.

The [cap identity](actual_conway_cap_sum_reduction.md)
\[
D(FG)=D(F)D(G),\qquad D=\phi T,
\]
still holds with its separate marked topological interpretation.
It applies when a \(D\)-product is exposed. It is not a rule for
factoring the \(C\)-contractions (11)–(16); no cap factor has been
inserted here.

## 5. A positive complete-character kernel and the fully flagged action

At pure complete colors \(p_i=L_N\), define \(K_N(E)=T(L_NE)\).
Coefficient reversal and the exact complete trace identity give, for
every full Hermite element \(E\),
\[
[e_r]K_N(E)=\phi(e_rL_NE)
 =N\sum_{k=0}^{N-1}e_r(c_k)E(c_k),\qquad
c_k=2\cos\frac{(2k+1)\pi}{N}.
\tag{17}
\]
The trace identity retains the repeated-node multiplicities. It is
not a substitution of a different closure: in \(\phi(L_NF)\) the two
original normal contributions cancel exactly. See the
[root-character contraction](actual_conway_root_character_fourier_contraction.md),
§2, and its [prior squared-kernel identity](actual_outer_color_squared_kernel.md).

For \(r>M=\lfloor d/2\rfloor\), \(e_r\) vanishes at all nodes. Thus
\(K_N(E)\) has degree at most \(M\) and is determined by the finite
kernel
\[
K_N(E)(c_l)=N\sum_{k=0}^{N-1}
 \left[\sum_{r=0}^{M}e_r(c_l)e_r(c_k)\right]E(c_k).
\tag{18}
\]
On the distinct nodes \(c_0,\ldots,c_M\), every \(e_r(c_k)\) is
nonnegative and is zero for \(k<r\). Let \(n_k\) be its multiplicity
in the full grid: two except at the odd simple node, where it is one.
Put \(B_{kr}=e_r(c_k)\) and \(\mathbf D=\operatorname{diag}(n_k)\).
The matrix in (18) is \(NBB^{\mathsf t}\mathbf D\). It is entrywise
nonnegative, self-adjoint and positive definite for the inner product
weighted by \(\mathbf D\), because \(B\) is triangular with nonzero
diagonal. Its symmetric conjugate is the positive Gram matrix
\[
N\mathbf D^{1/2}BB^{\mathsf t}\mathbf D^{1/2}.
\tag{19}
\]

This kernel is not a contraction with polynomial norm. Its exact
exponential size is the useful feature. Let \(c_*=c_M\) and
\[
G_0=g(1/4),\qquad
g(u)=J(2u)-4J(u),\qquad
J(u)=\int_0^u\log(2\sin\pi t)\,dt.
\]
The [uniform Newton estimate](actual_conway_root_star_full_jet_localization.md),
§3, is \(\log e_r(-2)=Ng(r/N)+O(\log N)\), with \(\max g=G_0\).
Consequently
\[
\max_l|K_N(E)(c_l)|
\le \exp\{N(2G_0+o(1))\}\max_k|E(c_k)|.
\tag{20}
\]
For a nonnegative nodal \(E\), keeping \(k=M\) and
\(r=\lfloor N/4\rfloor\) gives
\[
K_N(E)(c_*)\ge \exp\{N(2G_0-o(1))\}E(c_*).
\tag{21}
\]
At odd levels \(c_*=-2\). At even levels \(c_*+2=O(N^{-2})\);
all quarter-index factors stay away from zero, so this changes their
logarithm by \(O(N^{-1})\). The shifts and nodal multiplicities are
therefore harmless at both parities. The tree and its number of
factors are fixed before the limit.

Suppose every reduced hub has exactly one flagged leaf. Root at one
of them. Every nonroot flagged hub is \(K_N\) of a product of its child
messages; every unflagged original leaf is \(h_N=K_N(1)\). All these
messages are nonnegative on the nodal grid by (18). Inductively,
(20)–(21) show that their maximum nodal rate and their \(c_*\) rate
agree and add \(2G_0\) for each \(K_N\) operation. The final scalar is
\(N\sum_kE_{\mathrm{root}}(c_k)\), with no further exponential cost.
There is one \(K_N\) operation for every physical leaf except the
flagged root. Hence the positive complete scalar has the exact
all-level rate
\[
\lim_{N\to\infty}\frac1N\log Z_N(N,\ldots,N)
 =2G_0(H-1).
\tag{22}
\]
This supplies both a lower and an upper bound for the original complete
source. Its equality with the original strict classical action uses
the existing positive coefficient and strict lattice theorem; no
oversized norm has been renamed a geometric action. The
[rigid-spine geometry](actual_conway_rigid_spine_and_flagged_tree_geometry.md)
independently derives the same value from the rigid \(L\) profiles.

At noncomplete colors or with half twists, (11)–(12) remain exact,
but positivity of (17)–(21) is not asserted. The companion
[decorated-character theorem](actual_conway_decorated_character_spectral_closure.md)
proves a full-source spectral class closed under
\[
E\longmapsto T(R^\epsilon L_jE),
\tag{23}
\]
and finite products, at exactly this complete rate. Together with
the source adapter above, this covers the case in which every hub
is flagged. An unflagged hub requires \(E\mapsto T(E)\), the second
case of (11); it is not an instance of (23) with an existing physical
character. Mixed flagged/unflagged trees therefore remain outside
that closure statement.

## 6. Scope and internal review

The finite support lemma, reduced-hub criterion, recursive source
identities and positive complete-character kernel follow from the
recorded exact source. No finite audit or numerical scan is used.
The classification concerns the specified full-source contraction
and its strict support, not all tangle isotopies or knot types.
Transferring a source estimate to a literal knot-volume theorem
additionally uses its original local packet, whole filling transfer
and [marked geometric interface](actual_conway_general_mask_marked_filling.md).

The primary, coherent-source and geometry reviewers independently
read the full proof and returned analytical/source PASS. The exact
one-child rerooting clarification (13) was separately checked in
the preservation review. These are internal reviews, not external
peer review or formal verification. Native mathematical rendering
and relative-link checks are preservation checks; no numerical
asymptotic evidence is used.
