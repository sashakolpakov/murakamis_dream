# Long-filling volume for reduced-layer plats of unbounded bridge number

Independently reviewed theorem, 31 October 2026. Fix $k\geq4$ and signs $\epsilon_j\in\{1,-1\}$ for $1\leq j\leq k-1$. In conventional one-based braid-generator notation, form the standard $2k$-plat of

$$
\beta_k(\mathbf p)=
\left(\prod_{j=1}^{k-1}\sigma_{2j}^{\epsilon_j-2p_{1,j}}\right)
\left(\prod_{j=1}^{k-2}\sigma_{2j+1}^{-2p_{2,j}}\right)
\left(\prod_{j=1}^{k-1}\sigma_{2j}^{-2p_{3,j}}\right).
$$

All products follow the original bottom-to-top order, with $j$ increasing within a layer. There are $3k-4$ independent integer full-twist parameters. Denote the resulting knot by $K_k(\mathbf p)$ and its original normalized root invariant by $\mathcal K_N(K_k(\mathbf p))$, retaining the framing and component conventions of the [original spectral period](general_localized_unit_charge_filling_period.md).

**Theorem.** For every such fixed $k$ and sign pattern there is a threshold $T(k,\boldsymbol\epsilon)$ such that, for every fixed integer vector with all $|p_{r,j}|\geq T(k,\boldsymbol\epsilon)$,

$$
\lim_{N\to\infty}\frac{2\pi}{N}
\log\left|\mathcal K_N(K_k(\mathbf p))\right|
=\operatorname{Vol}\bigl(S^3\setminus K_k(\mathbf p)\bigr).
$$

The twists can have independent signs and magnitudes; they are fixed before $N\to\infty$. The conclusion concerns the full original invariant. The proof below verifies the complete-radius balance hypothesis of the [general full-source filling theorem](general_complete_radius_balance_filling_volume.md) on one actual marked packing for every member of this source family. The comparison includes both level parities and the entire charge sum through that theorem.

The supplied knots have bridge number at most $k$. The congruence subfamily in which every displayed braid exponent is divisible by $3$ has bridge number **exactly $k$**. This additional congruence is used only for the bridge lower bound, not for the volume theorem. Thus the family has unbounded minimal bridge complexity, rather than merely unbounded presentation width.

This explicit construction does not assert balance for every simple-white plat or cover all $k$-bridge knots. Its uniform proof covers $k\geq4$; no balance claim is made here for the analogous reduced width-three word.

## 1. Literal source word, mark, and simple white sphere

Use zero-based adjacent physical slots $0,\ldots,2k-2$. Slot $j$ is the braid
generator usually denoted $\sigma_{j+1}$. The standard bottom and top cup
pairs are $(0,1),(2,3),\ldots,(2k-2,2k-1)$. For $k\geq3$ put

$$
\begin{gathered}
O_k=(1,3,\ldots,2k-3),\qquad E_k^{\mathrm{int}}=(2,4,\ldots,2k-4),\\
D_k=O_kE_k^{\mathrm{int}}O_k,\qquad R=3k-4.
\end{gathered}\tag{1}
$$

These are the original bottom-to-top box slots, without an isotopy,
Markov stabilization, or abstract graph-to-plat adapter. Mark the first
original top cap, on slots $(0,1)$.

Name the exterior $u$, bottom odd-gap regions $a_0,\ldots,a_{k-1}$, and bounded
even-gap regions $e_1,\ldots,e_{k-1}$. The internal middle layer replaces
$a_j$ by $b_j$ for $1\leq j\leq k-2$. Set $b_0=a_0$ and $b_{k-1}=a_{k-1}$, because
there are no boxes in slots $0$ or $2k-2$. All other named regions are distinct.
The original gap sweep gives exactly

$$
\begin{array}{lll}
\text{first }O:&(a_{j-1},u,e_j,a_j),&1\leq j\leq k-1,\\
\text{middle }E:&(e_j,a_j,b_j,e_{j+1}),&1\leq j\leq k-2,\\
\text{final }O:&(b_{j-1},e_j,u,b_j),&1\leq j\leq k-1.
\end{array}\tag{2}
$$

A quartet $(x,b,c,y)$ contributes the actual triangles $(x,b,y),(x,y,c)$.
The protected regions are precisely $u$ and $a_0$. Their edge is MAIN.

The white MAIN edges are $u-a_i$ and $u-b_i$, with the two named endpoint
identifications retained; and $e_j-a_{j-1},e_j-a_j,e_j-b_{j-1},e_j-b_j$,
again retaining the two endpoint identifications. The MATCHING edges
are the two chains $a_{j-1}-a_j$ and $b_{j-1}-b_j$, together with the
internal chain $e_j-e_{j+1}$. For $k\geq3$ no listed edge has equal endpoints,
and there are no parallel edges: the two a/b chains have distinct
interior vertices and share only their two endpoints. Each listed edge
is incident to exactly two of the triangles in (2). At the left end,
for example, $e_1-a_0$ is shared by the first-O output and final-O input
triangles, while $u-a_0$ is shared by their other triangles. The right end
is identical. The remaining $e_j$ MAIN incidences close against the
appropriate middle-E triangle; the remaining $u$ incidences close between
consecutive O boxes. Every matching edge pairs its own original box.

Thus this is the actual simple triangulated sphere, with

$$
V=3k-2,\qquad E=9k-12,\qquad F=6k-8,\qquad V-E+F=2.\tag{3}
$$

The sphere topology and cyclic order are inherited from the original
Morse construction, not inferred only from Euler characteristic. The
[proved simple-block construction](actual_smoothed_source_capacity_blocks.md), §§4–5, therefore supplies the actual labeled convex ideal right-angled
certificate and its two original cut balls. In particular (1) is a
certified source diagram for every $k\geq3$.

## 2. The actual reflection packing and height coordinates

The white sphere has the reflection automorphism $a_i\leftrightarrow b_i$ fixing
$u,a_0,a_{k-1}$, and every $e_j$. It exchanges the first and last layers,
with the original cyclic order reversed. Normalize the marked tangency
$u-a_0$ to infinity, with the white disks $u$ and $a_0$ the outside half-planes
below $Y=0$ and above $Y=2$. All ordinary disks lie inside this strip.

This automorphism is realized by a reflection of the actual packing.
One way to justify the needed uniqueness is the [proved strictly convex marked angle potential](actual_positive_face_coefficient_saddle.md): after fixing the common scale, its ordinary-face
Hessian is a connected positive graph Laplacian. Equivalently, the
maximum-ratio argument for two positive curvature solutions propagates
strictness along every ordinary adjacency until it reaches a fixed
normalization. The normalized radii then determine the contact-center
development uniquely up to a horizontal Euclidean isometry. The
orientation-reversing automorphism preserving both marked lines
individually is therefore a vertical reflection; translate its axis to
$X=0$. Write $a_i$ for both the named disk and its positive curvature when
no confusion results. Then $a_i=b_i$.

Put $L=k-1$. The fixed disks form the actual tangent chain

$$
a_0\ (Y=2),\ e_1,e_2,\ldots,e_L,a_L,\ u\ (Y=0).
$$

Their centers lie on $X=0$. Disjoint interiors, successive tangencies and
the two endpoint lines force their intervals to be ordered strictly
from top to bottom. Write $y_0=2$, and $y_j$ for the contact height between
$e_j$ and the next fixed disk, $1\leq j\leq L$. Consequently

$$
\begin{gathered}
2=y_0>y_1>\cdots>y_L>0,\\
\operatorname{radius}(e_j)=\frac{y_{j-1}-y_j}{2},\qquad
\operatorname{radius}(a_L)=\frac{y_L}{2}.
\end{gathered}\tag{4}
$$

The fixed graph cycle $u-a_0-e_1-\cdots-e_L-a_L-u$ divides the original
white sphere into two triangulated disks: all interior $a_i$ belong to
one disk, all interior $b_i$ to the other. In the consistently oriented
a-side development, the triangles $(a_i,e_i,e_{i+1})$ all lie on the same
side of their downward-directed fixed-chain center edges. Their
original cyclic orders therefore put every $a_i$ on the same side of
$X=0$; one cannot choose these signs separately. The reflection puts
all $b_i$ on the opposite side. Choose the a-side to be $X>0$. Thus for
$1\leq i\leq L-1$ each reflected pair consists of two distinct disks, and the
$a_i$ center is $(X_i,r_i)$ with $X_i>0$, where $r_i$ is its Euclidean radius. These disks are
tangent to $u$ and to $e_i,e_{i+1}$. The first pair is also tangent to the
upper line $a_0$, hence $r_1=1$. The last $a_L$ is the single axis disk.

Elementary squared-distance tangency gives exactly

$$
2r_i=\frac{y_i(y_{i-1}-y_{i+1})}{y_{i-1}-y_i},\qquad
X_i^2=\frac{y_{i-1}y_i(y_i-y_{i+1})}{y_{i-1}-y_i}.\tag{5}
$$

For clarity, a circle of radius $r$ centered at $(X,r)$, tangent to the
axis circle whose bottom/top heights are $U,V$, satisfies $X^2=V(2r-U)$.
Applying this to the two neighboring fixed circles proves (5). No
circle-packing approximation is used.

## 3. Exact scalar recurrence, with its branch fixed by geometry

Define

$$
z_j=\sqrt{1-\frac{y_j}{y_{j-1}}}\quad(1\leq j\leq L),
\qquad z_0=z_{L+1}=0.\tag{6}
$$

All actual $z_j$ lie strictly between $0$ and $1$. I claim

$$
(1+z_{j-1})(1-z_j^2)(1+z_{j+1})=1,
\qquad 1\leq j\leq L.\tag{7}
$$

At $j=1$, $r_1=1$ and $y_0=2$ in (5) imply
$z_2=z_1^2/(1-z_1^2)$, which is (7). At the other end, tangency of
$a_{L-1}$ to $a_L$ at $X=0$ gives $X_{L-1}^2=2r_{L-1}y_L$.
Equation (5) then gives

$y_L=y_{L-2}-\sqrt{y_{L-2}(y_{L-2}-y_{L-1})}$,

where the plus root is excluded by $y_L<y_{L-1}$. Hence
$z_L^2=z_{L-1}/(1+z_{L-1})$, again (7).

For an interior $j$ put $p=z_{j-1}$, $z=z_j$, $w=z_{j+1}$, and $q=1-z^2$.
The positive horizontal coordinates and radii of the two consecutive
right-side disks, normalized by $y_{j-1}$, are

$$
\begin{aligned}
\frac{X_{j-1}}{y_{j-1}}&=\frac zp,&
\frac{X_j}{y_{j-1}}&=\frac{qw}{z},\\
\frac{2r_{j-1}}{y_{j-1}}&=\frac{p^2+(1-p^2)z^2}{p^2},&
\frac{2r_j}{y_{j-1}}&=\frac{q[z^2+qw^2]}{z^2}.
\end{aligned}\tag{8}
$$

Their literal tangency is $(X_{j-1}-X_j)^2=4r_{j-1}r_j$. Substitution
and cancellation of the positive factor $y_{j-1}^2/p^2$ gives

$$
1-2q(1+pw)+q^2(1-p^2)(1-w^2)=0.\tag{9}
$$

The two possible roots are

$$
q=\frac1{(1+p)(1+w)}\qquad\text{or}\qquad
q=\frac1{(1-p)(1-w)}.\tag{10}
$$

The second root is strictly greater than $1$ since $p,w>0$, whereas the
actual height ratio $q$ lies in $(0,1)$. This excludes it before making
any reconstruction or selecting a formal branch. The first root is
precisely (7). The interior proof needs no order assumption on the two
positive horizontal centers beyond the actual tangency.

## 4. A comparison principle gives the uniform 2/3 bound

Set $v_j=\log(1+z_j)$, so $0<v_j<\log2$ and $v_0=v_{L+1}=0$. Define

$$
f(v)=-v-\log(2-e^v).
$$

Equation (7) becomes

$$
f(v_j)=v_{j-1}+v_{j+1}.\tag{11}
$$

On $[0,\log2)$, $f(0)=0$ and

$$
f''(v)=\frac{2e^v}{(2-e^v)^2}>0.
$$

In particular $f(tv)>t f(v)$ whenever $t>1$ and $0<v<tv<\log2$.

For $L=3$ the explicit positive solution is

$$
\begin{aligned}
(z_1,z_2,z_3)&=(2/3,4/5,2/3),\\
(v_1,v_2,v_3)&=(\log(5/3),\log(9/5),\log(5/3)).
\end{aligned}\tag{12}
$$

Direct substitution verifies all three equations and both zero
boundary values. For any $L\geq3$, place this three-node vector at any
three consecutive positions and extend it by zeros elsewhere, calling
the resulting vector $s$. It satisfies

$$
f(s_j)\leq s_{j-1}+s_{j+1}.\tag{13}
$$

including at every zero position next to its support. If some $s_j>v_j$,
let $t=\max_j(s_j/v_j)>1$ and choose an attaining index. There $s_j=tv_j$,
so strict convexity gives $f(s_j)>t f(v_j)$. On the other hand (13) and
the maximal-ratio property give

$$
f(s_j)\leq s_{j-1}+s_{j+1}
\leq t[v_{j-1}+v_{j+1}]=t f(v_j),
$$

a contradiction. Thus $v$ dominates every translated three-node vector.
Every index $1,\ldots,L$ belongs to such a placement, and the smallest
nonzero seed entry is $\log(5/3)$. Therefore for every $k\geq4$,

$$
z_j\geq\frac23\qquad\text{for every }j.\tag{14}
$$

This comparison uses the actual packing solution already constructed
from the source certificate. It does not require a shooting guess or
a new nonlinear existence theorem. It also establishes the bound for
every interior index, not just for the two ends.

## 5. Exact curvature comparison and strict source balance

Let $E_j$ denote the curvature of $e_j$ and $A_i$ the curvature of $a_i$,
with $A_0=0$. From (4),(5), with $p=z_{j-1}$, $z=z_j$, and
$D_0=p^2+z^2-p^2z^2>0$, equation (7) simplifies the two adjacent
curvature ratios to

$$
\frac{A_{j-1}}{E_j}=\frac{p^2z^2}{D_0},\qquad
\frac{A_j}{E_j}=\frac{z^4(1+p)^2}{D_0}.\tag{15}
$$

At $j=1$ the first ratio is $0$ and the second is $z_1^2$ because $r_1=1$;
at $j=L$ the second formula uses the actual endpoint curvature $A_L=2/y_L$.
Thus (15) includes both boundary cases with their original zero/axis
interpretation, not a continued finite-circle formula imposed there.
Adding gives

$$
\frac{A_{j-1}+A_j}{E_j}
=z_j^2\left[1+\frac{2p(1+p)z_j^2}{D_0}\right]
\geq z_j^2\geq\frac49.
$$

Consequently

$$
\frac{E_j}{A_{j-1}+A_j}\leq\frac94.\tag{16}
$$

at every first/final O port, uniformly for all $k\geq4$.

The [zero-middle balance lemma](actual_zero_middle_nine_quarter_balance.md) uses the original
absolutely normalized triangle action $Q$ and proves

$$
Q(x,E,y)+Q(x,0,y)-\log E>\frac1{2500}
\quad\text{if }x+y>0\text{ and }\frac E{x+y}\leq\frac94.\tag{17}
$$

It retains either protected zero outer corner. Its proof is elementary:
at fixed $A=x+y$ the cofactor Perron action increases with $P=xy$; the
worst boundary value at $E/A=9/4$ is
$(2/\pi)\operatorname{Ti}_2(2/3)-\log(3/2)$, which has an exact rational positive lower
bound from four alternating $\operatorname{Ti}_2$ terms and the $\operatorname{atanh}$ series for the logarithm.
Thus every O port passes the actual complete-radius balance condition.

At each internal E port the two middle curvatures are equal,
$A_j=B_j>0$, while both outer curvatures are positive. The original
strict inequality $Q(x,A_j,y)>\tfrac12\log A_j$ gives
$2Q(x,A_j,y)>\log A_j$. Thus every port in the literal diagram (1)
satisfies the balance condition, using one common marked packing.
No independent local radius optimization or entropy min/max exchange
is involved.

## 6. General-theorem coverage, knot parity, and genuine width

The general balanced-diagram long-filling theorem therefore applies
to $D_k$ for every $k\geq4$ and every fixed half-twist pattern. For each
fixed $k$ and source pattern there is a diagram-dependent threshold;
all fixed filling powers beyond it may have independent signs and
magnitudes. The family construction places no comparison constraint
between these powers and no joint growing-twist/level limit.

For knot parity put $\epsilon=+1$ or $-1$ on each box of the first $O$ layer,
and zero on the other boxes. The first-layer zero-based transpositions
$(1\ 2),(3\ 4),\ldots,(2k-3\ 2k-2)$ merge the $k$ initially separate cap cycles
successively; each joins two previously different components. Every
other box has even exponent and trivial endpoint permutation. Thus
the filled main diagram is a knot for every integer full-twist vector.
This is a direct computation on the original cups and slots.

There are genuinely unbounded minimal bridge numbers inside this
family, not merely arbitrarily wide presentations of two-bridge knots.
Require additionally that every actual exponent $n_i=\epsilon_i-2p_i$
be divisible by $3$. This is one residue class of $p_i$ modulo $3$, compatible
with all retained parities and arbitrary independent large signs.
The Fox-coloring crossing operator on ordered strand colors is
$T=\begin{pmatrix}2&-1\\1&0\end{pmatrix}$ over $\mathbb F_3$; $(T-I)^2=0$ and $T^3=I$, for either signed
crossing convention. Every whole box therefore acts identically on
slot colors, though odd boxes still permute strand endpoints. The
$k$ independent adjacent bottom-cup colors survive every top cap, so
the knot has exactly $3^k$ Fox 3-colorings. Any $b$-bridge diagram has at
most $3^b$ such colorings, because colors on its $b$ overpassing bridges
determine every underpassing segment by the crossing rule. Reidemeister
moves preserve colorings, so $b(K)\geq k$; the supplied plat gives $b(K)\leq k$.
Hence $b(K)=k$ for this congruence subfamily. The independent full proof is the [Fox-coloring bridge certificate](actual_fox_coloring_exact_plat_bridge.md).

The congruence condition is used only for this bridge lower bound.
The analytic volume theorem still covers all independently long powers
in the prescribed knot parity. Conversely, this explicit family is
not claimed to exhaust balanced diagrams, all simple-white diagrams,
or all $k$-bridge knots. The present uniform construction covers $k\geq4$;
it makes no balance claim for the reduced $k=3$ word.

## Validation and scope

Root and independent geometry/source reviewers checked the complete proof, including the original slot incidence and mark, the reflection and oriented two-disk development, both height endpoints, the physical recurrence branch, the translated three-node comparison, the exact curvature ratio, the source-normalized balance gap, and the separate knot-parity and bridge arguments. The general statement follows analytically for every fixed $k\geq4$; finite packing samples are not used as its proof.


The [focused exact audit](../experiments/audit_general_reduced_layer_long_filling_volume.py) and [recorded results](../experiments/general_reduced_layer_long_filling_volume_results.json) check the literal original Morse incidences, mark, reflection and knot parity at 38 widths, five symbolic tangency/root/curvature identities, the three rational seed equations, the rational balance bound, and all 44 circle-support pairs and eight port tests of the exact width-four seed. Root independently reviewed the audit code and replayed it with identical results. These finite checks support the source and algebra interfaces; the uniform comparison and the asymptotic invariant theorem are analytical conclusions, not extrapolations from sampled packings.
