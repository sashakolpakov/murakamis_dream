# Volume equality after combining the net twists of an ordered Conway tree

31 October 2026.

A written tangle construction may contain several twist boxes whose signed counts add to a much smaller number. Large individual counts therefore do not give a meaningful geometric condition until these combinations have been identified. This note gives an explicit normalization by isotopies of the ordered tangles. Its surviving weights are sums over disjoint sets of the original boxes.

The new argument is topological. Once the resulting strict presentation has sufficiently long net twists, the [volume theorem for strict Conway trees](actual_conway_all_strict_tree_long_twist_volume.md) supplies the analytic limit. That theorem's estimates are an input here, not re-proved below. Every comparison of knot complements is made after filling the twist regions; no tangle isotopy is inferred from a scalar identity of quantum sources.

## 1. The construction and the conclusion

A box contains a two-strand tangle with four specified endpoints. In the diagram plane, label them (0,1,2,3), starting at the lower left and proceeding through the lower right, upper right and upper left. Let $R^n$ be the standard integral two-strand braid with $n$ signed half-twists. Let $T$ be the specified quarter-turn of the box in its diagram plane. A basic piece is

\[
                         h_i(n_i)=T(R^{n_i}).                 \tag{1}
\]

Each occurrence has its own label $i$, and each label occurs once. Products stack boxes in the stated order. Such compositions may close an additional circle inside a box; every such circle is retained. The cylindrical closure $C$ connects the two bottom endpoints to the corresponding top endpoints by the prescribed empty outside arcs. We first consider a fixed finite expression

\[
                              \mathcal E=C(FG).                    \tag{2}
\]

Turns, ordered products and the pieces (1) are the only operations in $F,G$. There are $m\ge2$ original labels. No condition on the signs, sizes or nonvanishing of the integers is needed for the topological normalization.

The distinction between a *formal piece* and its evaluated tangle is useful. A formal piece has a nonempty set $B\subseteq\{1,\ldots,m\}$ attached to it and integer weight

\[
                             W_B=\sum_{i\in B}n_i.           \tag{3}
\]

It remains a named piece even if a particular assignment makes $W_B=0$. Keeping this record is a bookkeeping choice, not a claim that a zero-twist rational tangle is geometrically nondegenerate.

Fix the original parity vector

\[
                   e=(e_1,\ldots,e_m),\qquad n_i\equiv e_i\pmod2.
                                                               \tag{4}
\]

**Ordered normalization theorem.** The ordered expression (2) determines a partition into nonempty disjoint sets

\[
                 \{1,\ldots,m\}=B_1\sqcup\cdots\sqcup B_s.   \tag{5}
\]

For each parity vector (4), a deterministic finite procedure gives exactly one of the following two outputs. The partition (5) is the same for every parity vector; only the recorded orders of subexpressions can depend on the parities.

* A fixed strict literal Conway presentation $\sigma_e=C(F_eG_e)$, with $s\ge2$ formal pieces of weights $W_{B_1},\ldots,W_{B_s}$.
* The integral braid closure $C(R^{n_1+\cdots+n_m})$.

For every integer assignment satisfying (4), the input filled link is ambient isotopic in the oriented $S^3$ to the indicated output link. The statement includes assignments with zero original weights, zero intermediate sums, or zero final sums. Every box order and every rotation introduced by the isotopy is recorded in the output. No reflection of $S^3$, arbitrary mutation, or permutation of unrelated tangle factors is used.

Here *strict* is a property of the literal formal presentation. Give $h$ type $L$; a turn exchanges $L,H$ and fixes $A$. Products obey

\[
 LL,LA,AA\longmapsto A,\qquad HL,HA\longmapsto H,
 \qquad HH\longmapsto\varnothing,                         \tag{6}
\]

with either order allowed in each listed pair. The permitted closing pairs are $AA,AL,AH,LH$, in either order. In the angle calculation underlying the strict theorem, these three types correspond to output intervals $L:(0,1/2)$, $H:(1/2,1)$ and $A:(0,1)$. Here the table is used as an explicit finite test on the written construction. The strictness test makes no assertion about the complete geometry of a particular short or zero numerical filling. Geometry is supplied by the separate long-twist theorem when its numerical hypotheses hold.

Let $K_N$ be the reduced enhanced Kashaev invariant with the normalization of [the strict-tree volume theorem](actual_conway_all_strict_tree_long_twist_volume.md).

**Net-weight volume theorem.** For every fixed input (2) there is a finite $B(\mathcal E)$ with this property. Apply the ordered normalization at the parity vector of a fixed integer assignment. Suppose its output is strict, the filled diagram has exactly one link component, counting any circles already closed inside its subexpressions, and

\[
                         |W_{B_j}|>B(\mathcal E)\quad(1\le j\le s).
                                                               \tag{7}
\]

Then the input knot is hyperbolic and

\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_{\mathcal E}(\mathbf n))|
       =\operatorname{Vol}(S^3\setminus K_{\mathcal E}(\mathbf n)).    \tag{8}
\]

The expression and the entire integer assignment are fixed before $N$ tends to infinity. The limit includes both parities and composite levels. The bound is independent of the signs and relative magnitudes of the final sums. It does not require any lower bound on the original individual weights.

If the input is already assumed to be a hyperbolic knot, the elementary output is impossible. Thus, for such an input, (7) is the only additional size condition in this theorem. Appendix A explains separately what can be done when final sums vanish; they are not silently removed in the theorem just stated.

## 2. Actual rotations and the twist-sliding isotopy

Use spatial coordinates $(x,y,z)$, with $z$ the stack axis and $y$ perpendicular to the diagram plane. Three proper rotations of a box will occur:

\[
 \begin{aligned}
 \rho(x,y,z)&=(-x,-y,z),\\
 \kappa(x,y,z)&=(x,-y,-z),\\
 \tau(x,y,z)&=(-x,y,-z).
 \end{aligned}                                             \tag{9}
\]

Their permutations of the four endpoints are, respectively,
$(01)(23),(03)(12),(02)(13)$. The last rotation is the physical planar half-turn $T^2$. Direct composition of the spatial rotations gives

\[
 \begin{aligned}
 \rho(FG)&=\rho(F)\rho(G),&
 \kappa(FG)&=\kappa(G)\kappa(F),&
 \tau(FG)&=\tau(G)\tau(F),\\
 \rho(TF)&=T\kappa(F),&
 \kappa(TF)&=T\rho(F),&
 \tau(TF)&=T\tau(F).
 \end{aligned}                                             \tag{10}
\]

The standard integral braid $R^n$ is fixed by each of these half-turns. This can be seen in its usual symmetric spatial drawing. The reversal of a coordinate in the projected drawing is accompanied by reversal of depth, so the integer crossing sign is retained. Consequently every $h_i(n_i)$ is fixed as well. Pushing a rotation through an expression using (10) therefore changes specified product orders but leaves every leaf weight unchanged. It neither duplicates a leaf nor introduces a minus sign in (3).

The twist-sliding move is

\[
                     R^a F\simeq \rho^a(F)R^a.            \tag{11}
\]

relative to the four outside endpoints. Here and below $\simeq$ denotes an actual unframed ambient isotopy, carrying any marked point and any ribbons that have been recorded.

For completeness, put $F$ in a smaller round cylinder inside its box, leaving two empty strand collars above and below. In cylindrical coordinates $(r,\phi,z)$, choose cutoffs $\eta(r),\xi(z)$ equal to one on the smaller cylinder and zero near the outside boundary. The maps

\[
       (r,\phi,z)\longmapsto
       (r,\phi+t\pi\eta(r)\xi(z),z),\qquad 0\le t\le1,    \tag{12}
\]

are homeomorphisms, and form an isotopy fixed on the outside boundary. At $t=1$, the inner tangle has undergone $\rho$. The two end collars have acquired inverse half-twist braids. Choosing the sign of the angle to agree with $R$, and applying the same construction to $\rho(F)$, proves (11) for $a=1$. The reverse isotopy proves $a=-1$, and iteration gives all integers. In particular (11) is valid at $a=0$. Internal closed components move with the inner cylinder and do not affect the argument.

Adjacent integral boxes satisfy

\[
                              R^aR^b\simeq R^{a+b}.       \tag{13}
\]

Opposite crossings cancel by Reidemeister II; equal signs concatenate. Equations (11) and (13) allow integral boxes separated by arbitrary ordered factors to be collected at one end of their common stack. The factors that they cross acquire the displayed $\rho$ rotations. This is not the assertion that arbitrary two-tangles commute.

All sliding decorations depend only on the parities of the moved powers. Since a moved power is always a sum of a specified set of original weights, its parity is determined by (4).

![The two local moves used in the normalization. Sliding a twist past a tangle retains the indicated rotation of that tangle; adjacent integral boxes combine by adding their signed weights. The outside endpoints and ordered attachments are retained.](../book/figures/net-twist-reduction.png)

## 3. The closing sphere and moving a turn through it

The actual convention for $C(FG)$ joins

\[
 F_2\!\leftrightarrow G_1,\quad F_3\!\leftrightarrow G_0,
 \quad F_0\!\leftrightarrow G_3,\quad F_1\!\leftrightarrow G_2.
                                                               \tag{14}
\]

The first two pairs are the stack interface and the last two are the cylindrical closing arcs. They are the empty planar arcs of the original construction, not a four-punctured-sphere gluing specified only by its point permutation.

Straighten this collar while retaining its four planar sectors. In round coordinates on the two tangle balls the resulting sphere gluing is

\[
                  h(x,y,z)=(x,y,-z),\qquad h(i)=3-i.     \tag{15}
\]

This reflection is orientation reversing on the boundary sphere. It is different from the proper rotation $\kappa$, even though they have the same permutation of the four displayed endpoints. If $T_t$ is rotation in the diagram plane through the appropriate angle $t\pi/2$, then

\[
                              hT_th^{-1}=T_t^{-1}.       \tag{16}
\]

Apply $T_t$ to one ball and $T_t^{-1}$ to the other. Equation (16) says that the maps agree on their identified boundaries. They extend over the balls and give an ambient isotopy of the glued $S^3$, starting at the identity. At $t=1$, this proves

\[
 C((TF)G)\simeq C(F(TG)),\qquad
 C((TF)(TG))\simeq C(F\tau(G)).                           \tag{17}
\]

The actual half-turn in the second identity must be retained and expanded by (10). This argument would fail for a gluing collar with an additional boundary Dehn twist; (14) and its empty arcs are essential.

We also use the cyclic move

\[
                               C(FG)\simeq C(GF).        \tag{18}
\]

Place the two stack intervals successively in the standard unknotted solid torus $D^2\times S^1$ and move the choice of cutting section past the first interval. Translation in the circle direction gives the required isotopy, carrying the marked point with it. It extends to the standard ambient $S^3$. This cyclic move does not permute factors in an open stack. Ordinary reassociation of a stack only changes the heights of its boxes and is also relative-boundary isotopy.

## 4. A terminating symbolic normalization

The procedure never tests whether a weight is numerically zero. Every operation is performed on the formal labeled boxes.

First shorten all chains of turns. Replace $T^2$ by the actual $\tau$, push $\tau$ through the remaining subtree by (10), and resolve it on the standard leaves. Flatten consecutive ordered products by associativity. At this stage the expression has maximal ordered stacks of at least two factors; their factors have one of the forms

\[
                    h(B),\qquad Th(B)=R^{W_B},\qquad T(P),
                                                               \tag{19}
\]

where $P$ is another maximal stack. A displayed integral box in (19) is called a *direct integral factor*. This is only a description of its position in the ordered stack.

Choose a deepest maximal stack that has at least two direct integral factors. Collect all of them at its right end by (11), retaining the rotations of every intervening factor. Fuse them using (13). The resulting integral factor is named $Th(B)$, where $B$ is the union of their disjoint label sets. Its weight is the sum (3). Convert all $\rho,\kappa,\tau$ decorations back to ordered expressions with (10), shorten new turn chains and flatten new adjacent products. Repeat.

A rotated direct integral factor remains direct integral. A rotated ordinary leaf remains an ordinary leaf. A rotated turned stack remains a turned stack, with perhaps reversed order inside it. Thus the procedure never hides an integral factor by pretending that a rotated arbitrary tangle is unchanged.

Every fusion reduces the number of formal weighted leaves by at least one. It does so even when the new sum evaluates to zero: the new box remains a single recorded box. Between fusions, shortening turns removes unary vertices and flattening removes product vertices; propagating a rotation creates neither new leaves nor new turns. Thus this procedure terminates.

When no further fusion is possible, each maximal stack has at most one direct integral factor. An induction from its deepest children proves:

* Every factor other than a direct integral factor has type $L$ or $A$.
* A maximal stack with no direct integral factor has type $A$.
* A maximal stack with one direct integral factor has type $H$.

Indeed the factors $T(P)$ have type $A$ when $P$ has type $A$, and type $L$ when $P$ has type $H$. Multiplying $L/A$ factors gives $A$; inserting the one $H$ factor gives $H$. Any ordered binary resolution of such a stack respects (6), since it cannot create a product of two $H$ factors. The lower bound of two factors in a maximal stack is used here.

If all factors of a maximal stack have fused into one, that remaining factor is an integral box. Suppressing the now unary product vertex therefore cannot leave a lone arbitrary turned stack. This observation will also control the closing root.

## 5. The final root and the fixed output template

Starting from (2), the root remains a product unless all of its factors fuse into one integral box. In the latter case the answer is the elementary closure, and the procedure stops.

Otherwise let $k\ge2$ be the number of factors in the normalized maximal root stack. There is at most one direct integral factor.

If $k\ge3$, the closing pair is strict. With no integral factor, expose one $L/A$ factor against the product of the remaining $k-1$ factors, which has type $A$. With one integral factor, use the cyclic move (18) to expose it against the product of the other factors. The closing pair is then $HA$. All orders inside the two factors remain the recorded ones.

For $k=2$, every pair is permitted except $LL$. A type-$L$ factor is literally $T(U)$, where $U$ is either one integral box or a stack with exactly one direct integral factor. This includes the ordinary leaf $h(B)=T(R^{W_B})$. Therefore the remaining failure has the form

\[
             C((TU)(TV))\simeq C(U\tau(V)).              \tag{20}
\]

Flattening the right-hand side exposes exactly two direct integral factors, one from each displayed part. Their other factors are of type $L$ or $A$. Collect and fuse the two integral factors using (11)–(13), with the precise rotations retained. This reduces the number of formal weighted leaves. Normalize again.

The argument uses no nonzero-weight hypothesis. If the fused sum is zero, its named box $R^0=Th(0)$ remains in the stack. If there are other factors, it still occupies the one direct-integral position for the formal type test. If there are no other factors, the output is the elementary $C(R^0)$. We do not remove this box, expose a cap, or infer a nondegenerate geometric filling from it.

Every return from (20) makes a fusion, so the entire root procedure terminates after at most $m-1$ fusions. When it stops, it has either a strict closing pair or the single integral closure. Every operation preserves or unions the disjoint label sets. They therefore give the partition (5); in the single-box case their union is all original labels.

Fix a deterministic choice whenever several deepest stacks are available, for example the first in the current ordered traversal. The only numerical information used by the procedure is the parity in a rotation $\rho^{W_B}$. All these parities are fixed by (4). It follows inductively that the visited ordered trees, the unions of label sets, and the final expression are identical for every integer assignment in that parity class. Numerical zero tests, which would have invalidated this inference, have deliberately been omitted.

### Reading the net-weight groups without choosing parities

The partition can be found before any integers or parities are assigned. The following finite graph is a record of the tangle operations, not a new knot projection or an identification of quantum tensors.

Remove the final closing product in $C(FG)$ and join the output ends of $F$ and $G$. Represent each remaining product by a trivalent vertex. Put a bit on each edge equal to the number of quarter-turns on that edge modulo two. For this bookkeeping, the basic piece $h_i=T(R^{n_i})$ includes one turn on its leaf edge, and the end of that edge is the labeled integral box $R^{n_i}$. Contract every internal edge whose bit is zero. For $m\ge3$, this produces a tree of product junctions of valence at least three, with bit one on every internal edge. A leaf with bit zero is a direct integral leaf at its junction; a leaf with bit one is an ordinary turned leaf.

At each junction $v$, put all its direct integral labels in a single block $I_v$, if this set is nonempty. Each ordinary leaf is a singleton block. These sets give (5). Replacing each nonempty $I_v$ by one integral leaf can lower a junction's valence. A newly two-valent junction necessarily has one fused integral leaf and one other incidence. If that incidence is an internal turn edge, suppress the junction and send its integral leaf through that turn: the neighboring junction receives an ordinary leaf. Its valence is unchanged, and it receives no new direct integral label. Thus no second round of unions is needed.

There are two small endings. A two-valent junction whose other incidence is an ordinary leaf is the strict mixed two-leaf closure. A one-valent junction consists of a sole integral leaf and is the entire connected tree, giving the elementary closure. If two newly two-valent junctions are connected by a turn edge, suppressing either gives the same mixed two-leaf closure. For an input with just two leaves, let $a,b\in\{0,1\}$ be their turn bits relative to their integral boxes. Equal bits give the one block $\{1,2\}$; unequal bits give two singleton blocks and the strict mixed closure.

Here is why this graph describes the actual normalization rather than only a source identity. The rotations (10) reverse some orders but preserve every edge's turn parity and every leaf label. Associativity joins product vertices across a zero-bit edge. Moving a turn through the closing sphere preserves the total bit on that unrooted edge. In the failed $LL$ root (20), the two displayed turns have total bit zero; the product regions on its two sides already belong to the same contracted junction. Their exposed integral factors therefore belong to one prescribed block. The physical slides can gather these factors in their ordered stack, with all rotations retained.

One can also expose any chosen junction at the closing sphere: use associativity and cyclicity along the path to it, moving each encountered turn across the sphere by (17). This moves existing sibling tangles in their recorded order; it does not permute arbitrary satellites. Gather one junction's full block before proceeding to the next. A two-valent suppression is then precisely the closed-turn move carrying its integral box into an ordinary leaf at its neighbor. These are the actual isotopies already proved above.

Consequently the graph's blocks are fixed independently of the original integer parities. The parities only choose the rotations of the surviving ordered subexpressions. The earlier termination proof still applies to this prescribed schedule.

This proves the ordered normalization theorem. It is stronger than a normalization restricted by the nonvanishing of every intermediate subset sum.

## 6. Peripheral curves, marked evaluation and framing

The isotopies above are orientation preserving on $S^3$. They carry the link itself, all its components, and any chosen marked point. In a knot case the output consequently has exactly the same component as the input. An endpoint calculation can test this, but it must retain both the pairing of the four exposed endpoints and the number of circles already closed inside each box. At a product, trace the joined strands, add each new closed circle to that count, and retain the new exposed pairing. A turn only permutes the exposed endpoints. At closure, add the cycles formed by the closing arcs. The total, not merely the exposed closing cycle, must be one. This test is fixed throughout a parity class.

In particular, a knot output has no internal closed component in any proper subtree. Such a circle has no endpoint through which a later operation could connect it to the rest. The remaining arcs still have the four external endpoints and form at least one more component when the entire diagram is closed. An internal circle would therefore contradict the one-component hypothesis. This verifies the internal-component condition in the strict-template theorem.

Restrict an isotopy to the complement of a small transported tubular neighborhood of the knot. This gives an orientation-preserving homeomorphism of exteriors. A meridian is transported because it bounds a disk meeting the core once. After orienting the knot and carrying that orientation, its preferred longitude is also transported: it is the primitive longitude of linking number zero. In particular, an unrecorded extra meridional power is not inserted into the preferred longitude by the normalization.

The auxiliary crossing circles used to prove the long-filling theorem for the output are a separate matter. Several filled input twist boxes can become one output box. We do not assert that their unfilled augmented links are homeomorphic, identify their individual cusp meridians, or replace several independent circle colors by one color before filling. The comparison is between the already filled knots. The output strict template supplies its own actual auxiliary circles, primitive fillings and marked geometric calibration.

There is also no need to equate two raw blackboard-framed tensor contractions. An ambient isotopy transports any ribbon, but the transported ribbon may differ by integral self-twists from the standard ribbon chosen when drawing the output. The invariant $K_N$ in (8) is the reduced knot invariant with its prescribed framing normalization, so isotopic unframed knots have the same $K_N$. The chosen point remains on the unique knot component; the reduced one-cut invariant does not depend on where that component is cut.

Even when raw framed evaluations are used as intermediate expressions, the difference cannot affect the rate. At complete color $d=N-1$, the actual twist scalar is

\[
                 \theta_d=q^{-d^2/2},\qquad q=e^{\pi i/N},
                 \qquad |\theta_d|=1.                    \tag{21}
\]

A change of integral ribbon framing is an integer power of this scalar, by the original normalization theorem. That integer may depend on the fixed diagram and fixed weights; its modulus is nevertheless one at every $N$. The separate modified-dimension convention, if used, has its original factor $\eta_N/N$, where $\eta_N=i^{N+3}$; the same convention must be used on both sides, and it is not created or removed by this normalization.

Thus the finite topological invariant, or the absolute value of its specified raw normalization, is preserved. No derivative or confluent coefficient of an unfilled colored source has been discarded to reach this conclusion. Those source data are simply not the object being identified here.

In particular, if $\sigma_e$ is the strict output and $\mathbf W=(W_{B_1},\ldots,W_{B_s})$, the normalized knot invariants satisfy the exact identity

\[
             K_N(K_{\mathcal E}(\mathbf n))
                 =K_N(K_{\sigma_e}(\mathbf W)),\qquad N\ge2.
 \tag{21a}
\]

This follows for the based reduced evaluation as well: cutting the unique knot component gives an intertwiner of the complete color. Its distinct weight spaces and the nonzero adjacent raising and lowering maps force that intertwiner to be scalar. Transporting the cut therefore introduces no new normalization. This argument is not permission to move a mark to a different component of a link.

For hyperbolic outputs, transport the complete hyperbolic metric along the exterior homeomorphism. This produces a complete finite-volume hyperbolic metric on the input exterior of exactly the same volume. Consequently the geometric identification in (8) is with the input knot complement, not with a comparison diagram's unrelated augmented volume.

## 7. The threshold and the elementary alternative

For each original parity vector $e$, the procedure gives a single structural output. If it is strict, let $B_e$ be the threshold of that strict literal presentation from [the strict-tree volume theorem](actual_conway_all_strict_tree_long_twist_volume.md). There are at most $2^m$ such outputs. Taking the maximum of their finite thresholds, and increasing it to at least $2$, gives a finite $B(\mathcal E)$. If there are no strict outputs, take $B(\mathcal E)=2$; the non-elementary part of the theorem is then empty.

For a fixed assignment with strict output and (7), that theorem constructs the smooth complete metric on the output knot exterior and proves its all-level invariant limit. Section 6 identifies both the knot invariant and that metric volume with the input. This proves (8). The output knot condition follows from the assumed one-component input, rather than from an assumed equality of source scalars.

In the original filling convention, write

\[
 n_i=\epsilon_i-2p_i,\qquad
 W_B=\epsilon_B-2p_B,\qquad
 p_B=\sum_{i\in B}p_i+
           \frac{\epsilon_B-\sum_{i\in B}\epsilon_i}{2},  \tag{22}
\]

where $\epsilon_B\in\{0,1\}$ has the parity of the sum. The last correction is an integer fixed by the chosen parities. Thus the theorem concerns independently long *net* filling slopes, with a fixed parity offset. It is not a condition that all original $p_i$ be independently large. Within a final block, equal signs prevent cancellation; arbitrary independent signs do not.

The integral output is the usual $(2,s)$ torus braid closure. It is a knot only when $s$ is odd. For $s=\pm1$ it is an unknot. For odd $|s|\ge3$, its torus decomposition gives the group

\[
                       \langle a,b\mid a^2=b^{|s|}\rangle.
                                                               \tag{23}
\]

The common element is central and has nonzero image in the abelianization, so it is not the identity. A finite-volume hyperbolic knot group has trivial center: a central element commutes with the rank-two peripheral parabolic group, hence is a parabolic translation fixing that cusp point; centrality would then force the whole group to fix that point, which is incompatible with a finite-volume hyperbolic three-manifold. The cyclic unknot group is also not such a group. Thus an elementary output cannot be a hyperbolic knot. No quantum asymptotic for torus knots is needed to exclude it from the hyperbolic corollary.

Finally, a condition on all written weights cannot replace (7). Inside any integral box,

\[
                         R^a\simeq R^{a+2k}R^{-2k}.      \tag{24}
\]

Both written magnitudes can be made arbitrarily large while their net is the fixed $a$, with the same original knot. This holds even when that knot is hyperbolic. It explains the net-weight hypothesis without providing a counterexample to any volume-conjecture equality.

## 8. A worked reduction, including a cancelling pair

Write $h_j=T(R^{n_j})$. Consider the actual ordered diagram

\[
 K=C\!\left(
       R^{n_1}R^{n_2}h_3\,
       T(R^{n_4}R^{n_5}h_6)
       \right).
 \tag{25}
\]

It is an expression in the original pieces because $R^{n_i}=Th_i$. Each of its two displayed stacks contains a pair of direct integral boxes. Set

\[
                   a=n_1+n_2,\qquad b=n_4+n_5.
 \tag{26}
\]

Adjacent braid cancellation alone gives

\[
                    K\simeq C\!\left(R^a h_3 T(R^b h_6)\right).
 \tag{27}
\]

The four net blocks are $\{1,2\},\{3\},\{4,5\},\{6\}$. To check strictness, $R^b h_6$ has type $HL$, hence type $H$; its turn has type $L$. The product $h_3T(R^b h_6)$ has type $A$, and the outer pair is $HA$. Thus, if the actual closure is a knot, a fixed lower bound on $|a|,|b|,|n_3|,|n_6|$ gives the volume equality for this input diagram.

The cancellation issue is visible without numerical examples. Taking $n_1=M+a$ and $n_2=-M$ makes both written twist counts arbitrarily large while leaving $a$ fixed. The theorem tests $a$, not the two written magnitudes.

If $a=0$, formula (27) still holds, with its identity box retained. Removing that identity is an optional further reduction. The physical closing-sphere move and cyclicity give

\[
 \begin{aligned}
 C\!\left(h_3T(R^b h_6)\right)
   &\simeq C\!\left(R^{n_3}\tau(R^b h_6)\right)\\
   &=C\!\left(R^{n_3}h_6R^b\right)
     \simeq C\!\left(R^{n_3+b}h_6\right).
 \end{aligned}
 \tag{28}
\]

The middle equality uses the actual reversal
$\tau(R^b h_6)=h_6R^b$; it does not erase a half-turn on an arbitrary box. The final step moves the last integral box around the cylindrical closure and fuses adjacent braids. The surviving groups are now $\{3,4,5\}$ and $\{6\}$, with the zero block $\{1,2\}$ removed. If these two new weights are long and the closure is a knot, the strict two-leaf theorem applies. This is a further theorem on that zero wall, not a replacement for the fixed four-block normalization valid for all assignments.

## 9. The pointed quantum \(A\)-period gives the same limit

The net-weight theorem also applies to the exact reconstruction from a recurrence operator. Fix a knot covered by (7), with all integer weights fixed, and write $V=\operatorname{Vol}(S^3\setminus K)$. The [pointed quantum \(A\)-period theorem](actual_conway_pointed_quantum_a_volume.md) supplies the following algebraic input for this same knot.

Choose once and for all a genuine nonzero annihilator
$P(q,M,\mathsf S)$ of its reduced ADO family, with
$\mathsf S M=qM\mathsf S$. Here $\mathsf S$ is the recurrence shift, not the tangle quarter-turn. The marked meridian is $M=-qx$, where $x$ is the raw exponential color; the complete color at $q_N=e^{\pi i/N}$ has $M=1$. Fix the initial vector $c_0(q)$ from the finite window of ordinary color polynomials prescribed by the pointing theorem. These polynomials select the knot's solution of the recurrence.

Let $r_N(q)$ be the corresponding companion-matrix row that propagates this initial vector to color $N$. For all sufficiently large levels, in particular beyond the fixed initial window, the pointed period is

\[
 \mathscr P_N(P,c_0)
   =\operatorname{CT}_{t=0}
      \bigl[r_N(q_N(1+t))c_0(q_N(1+t))\bigr]
   =K_N(K).
 \tag{29}
\]

The constant term is taken after multiplying the full Laurent germs, so poles of individual companion steps can cancel. The required number of derivatives of the fixed initial polynomials is bounded by the fixed operator, independently of $N$. These are exact reconstruction statements, not estimates derived from a companion-matrix norm. Combining (29) with (8) gives

\[
 \lim_{N\to\infty}\frac{2\pi}{N}
           \log|\mathscr P_N(P,c_0)|=V.
 \tag{30}
\]

There is a positive formulation as well. The pointed theorem constructs a positive determinant ratio $\mathscr G_N(P,j_0)$ from the Gram matrix of the finite recurrence system with its initial conditions. Its exact value is
$\sum_{j=j_0}^{N}|C_j(q_N)|^2$, where $C_j$ is the ordinary reduced color-$j$ invariant of this knot. The terms with $j<N$ have a polynomial total bound for a fixed braid presentation, whereas the complete term is $|K_N(K)|^2$. Hence

\[
 \lim_{N\to\infty}\frac{\pi}{N}\log\mathscr G_N(P,j_0)=V.
 \tag{31}
\]

For the full one-cut modified evaluation, keep the actual peripheral factor

\[
 d_N(M)=i^{N+3}\frac{M-M^{-1}}{M^N-M^{-N}},\qquad
 d_N(1)=\frac{i^{N+3}}{N},\qquad
 \mathcal N_N(K;1)=\frac{i^{N+3}}{N}\mathscr P_N(P,c_0).
 \tag{32}
\]

The value at $M=1$ is the removable value of the whole function. It does not assign a new modified dimension to each fused twist box and does not change the exponential limit.

An annihilator computed from the normalized presentation can differ from one computed from the input presentation. With each operator's own fixed initial data, (29) reconstructs the same knot invariant. Equality of these selected scalar periods does not assert equality of the operators, recurrence ideals, companion matrices or unpointed modules. Identifying a selected classical \(A\)-polynomial factor is also a separate problem.

## Appendix A. Optional reduction on a final zero-sum wall

The main theorem keeps every box symbolically, including evaluated zero boxes. It therefore remains a valid isotopy statement on a wall $W_B=0$, but the longness condition (7) fails there. One must not apply the strict long-filling theorem to a zero net weight.

There is a separate, explicit topological reduction available on such a wall. Set $D(E)=C(TE)$; this is the cap closure of $E$, joining its upper endpoints to each other and its lower endpoints to each other. A zero ordinary piece is $h(0)=T(R^0)$, the cup-cap tangle, not the through-identity tangle.

A chosen leaf of any cylindrical product closure can be exposed as $C(h_iQ)$. To prove this, follow its path to the root. Associativity and (18) move each sibling into the other factor. When the path crosses a turn, use the first identity in (17) to transfer that turn to the other factor. Each step shortens the path to the chosen leaf, retains every sibling exactly once, and records every resulting order. If the chosen leaf is zero, this gives

\[
                        C(h(0)Q)\simeq D(Q).             \tag{33}
\]

There is no deletion of an extra closed component in (33). Its two arcs are precisely the two caps in $D(Q)$. A lone zero leaf is handled directly by the elementary closures below.

At a cap-closed root the rules are

\[
             D(TF)=C(\tau F),\qquad
             D(FG)=D(F)\mathbin{\#}D(G).                 \tag{34}
\]

The second formula is a componentwise connected sum with specified components: the component containing the upper cap of $F$ is joined to the component containing the lower cap of $G$. An empty horizontal collar between the two boxes gives a sphere meeting the link exactly in its two interface arcs. Cutting along that sphere and capping the punctures gives exactly the two displayed cap closures. Thus (34) is a topological splitting along a two-punctured sphere; it is not a Conway mutation along a four-punctured sphere. Component labels and the mark must be retained.

Run the symbolic normalization separately on each resulting cylindrical product factor. If a final weight is zero, apply (33) again. The elementary endings are

\[
 \begin{array}{ll}
 C(R^s)=\text{the }(2,s)\text{ braid closure},&D(R^s)=\text{an unknot},\\
 C(h(s))=D(R^s),&D(h(s))=C(R^s).
 \end{array}                                             \tag{35}
\]

The unknot assertion uses the end cap to remove the successive curls in the unframed diagram; their ribbon twists, if retained, are recorded separately. At $s=0$, $C(R^0)$ is the two-component unlink, not a discarded unit.

This specialized procedure terminates. Fusion and numerical-zero removal each decrease the total number of live weighted leaves. Between these events, (34), turn shortening and stack flattening remove vertices from the finite expression forest. The context operation for (33) moves existing turns and siblings but does not copy them. The result is a finite tree of componentwise connected sums of strict factors with nonzero final weights, elementary braid closures and unknots. Surviving and deleted label blocks partition the original labels.

Unlike the main symbolic output, the specialized decomposition can change when additional subset sums vanish. Its structure is fixed by the original parities and the zero/nonzero pattern of the finitely many subset sums. It remains a finite normalization, not a prime or JSJ decomposition. The source identity for a cap closure is not needed to prove this decomposition, and no invariant multiplicativity or volume additivity is being inferred merely from the notation in (34).

A direct useful corollary requires no further classification: if this displayed decomposition has one strict knot factor whose net weights exceed its threshold, and all other factors are unknots, the input is isotopic to that strict factor and (8) follows. This corollary covers some final zero-sum walls. A general assertion about the quantum rate of several nontrivial factors, or about short remaining weights, is outside the result proved here.

## Appendix B. General root turns and cap closures

For a more general input $C(E)$ that was not initially written as a product closure, or for an input $D(E)$, first process its outermost operations. A top turn changes $C(TF)$ to $D(F)$, while $D(TF)$ is the first formula in (34), retaining the physical half-turn. A cap-closed product splits by the second formula in (34). A cylindrical product is treated by Sections 4–5. A single integral or rational box is treated by (35).

This preliminary root reduction is structural and does not test numerical weights. Its two-punctured spheres may already produce several factors even when no sum vanishes. In contrast, for the original input (2), the symbolic procedure never creates a cap closure: the root can become unary only by fusing all its direct integral factors into one integral box. That is why the main theorem has exactly one output for each parity rather than an unrecorded connected-sum collection.

The same explicit one-strict-factor-and-unknots corollary applies to a general root. Without that condition, the decomposition itself is the topological conclusion. No claim of hyperbolicity is made for a connected sum of nontrivial factors.

## Inputs and scope

The local geometric moves are given in full in Sections 2–3. Their original endpoint convention is the one in [the ordered stack and closing construction](actual_conway_bowtie_projection_cut.md), §2. The component labels in the cap splitting are those of [the cap-closure splitting theorem](actual_conway_cap_sum_reduction.md), §2. The [reduced-junction source construction](actual_conway_reduced_hub_source_normal_form.md) has compatible graph bookkeeping. Its commutative Frobenius identities are not premises of this topological proof.

The asymptotic input is the theorem for every strict literal presentation in [the strict-tree volume theorem](actual_conway_all_strict_tree_long_twist_volume.md). Its original marked representation and smooth completion are supplied by [the marked deformation and filling theorem](actual_conway_general_mask_marked_filling.md); the present argument transports their already filled knot complement, rather than rebuilding the unfilled cusp dictionary after fusion. The unit framing statement is equation (2) of [the complete-color normalization theorem](actual_complete_augmented_source_normalization.md).

The result is therefore a genuine extension from strict presentations to presentations that *normalize* to a strict template with long net weights. It does not assert a threshold on unreduced individual twists, identify the distinct augmented exteriors before filling, equate independent circle colors, or prove the short-twist conjecture for all arborescent knots. Those distinctions are part of the theorem, not omissions from its normalization algorithm.

The [literature comparison](positive_conway_literature_coverage.md#7-ordered-compositions-with-long-net-twists) records related primary statements and their knot, invariant and level restrictions. It is a coverage check; no external proof is used in the reduction above.
