# Exact source composition with single-leaf Conway attachments

31 October 2026. original-source theorem. For the
completed grammar $E::=hh\mid T(E)\mid EE\mid hE\mid Eh$ and cylindrical
closures $C(FG)$ with **both root children completed**, the exact source
has a strict complete optimizer, a primitive wire lattice, the retained
finite complex packet, and whole-source alias and physical-color gaps at
both parities. No additional individual-leaf condition is required.
All physical colors, original support constraints, Hermite normal data,
phases and normalization are retained.

The proof below includes the exact finite support compiler and the
single-leaf alias induction. Its analytic companion is the
[single-leaf alias composition theorem](actual_conway_single_leaf_alias_composition.md);
the [geometric companion](actual_conway_single_leaf_geometric_composition.md)
retains the actual metric and primitive marked interfaces. The
[assembled long-filling theorem](actual_arborescent_single_leaf_long_twist_volume.md)
states their consequence for the original invariant. Root-leaf closures
with a quarter-index turning point remain a separate regime. These are
literal four-port ribbon sources, not formal rational fractions or
replacement coupons.

## 1. The literal compiler and an exact all-level support recursion

Let h be the original turned complete-circle coupon, T the actual physical
quarter-turn, and FG the original stack. Every copy is an independent box;
its colors, signs, auxiliary circle and original mark are retained. For any
finite expression in h,T,product the source is evaluated in the FULL algebra
$H_N=\mathbb C[z]/(2T_N(z/2)+2)$, $d=N-1$ and $M=\lfloor d/2\rfloor$.
Write $\widehat B_r$ for the actual normalized Newton basis and
$s_r=\prod_{t=1}^r2\sin(\pi t/N)$, with $s_0=1$. The exact rules are

$$
\begin{aligned}
T\widehat B_r&=\widehat B_{d-r},\\
\widehat B_i\widehat B_j
 &=\sum_{r=\max(i,j)}^{i+j}\mu_{i,j,r}\widehat B_r,\\
\mu_{i,j,r}&=\frac{s_{i+j}s_r}
 {s_i s_j s_{r-i}s_{r-j}s_{i+j-r}}>0,\qquad i+j\le d.
\end{aligned}\tag{1}
$$

and the product is zero if i+j>=N. This is polynomial divisibility with
multiplicities: repeated-root normals are not removed. The complete h has
strictly positive coefficients exactly on [0,M].

For every positive pure compiled box, its nonempty finite Newton support is
an INTEGER INTERVAL. If I_F=[l_F,u_F], the exact support compiler is

$$
\begin{aligned}
I_h&=[0,M],& I_{TF}&=[d-u_F,d-l_F],\\
I_{FG}&=\begin{cases}
\varnothing,&l_F+l_G>d,\\
[\max(l_F,l_G),\min(d,u_F+u_G)],&l_F+l_G\le d.
\end{cases}
\end{aligned}\tag{2}
$$

An empty support propagates through both operations. Every index displayed
in (2) has strictly positive coefficient. To verify the product assertion,
let max(l_F,l_G)<=r<=min(d,u_F+u_G). Choose i,j in their original intervals
with i,j<=r and i+j=max(r,l_F+l_G). Such integers exist because
min(u_F,r)+min(u_G,r)>=r, while both upper bounds exceed their respective
lower bounds. The chosen sum is<=d and r lies in [max(i,j),i+j], so (1)
supplies a positive contribution. The reverse inclusion is immediate.
This proves (2) at every level, without a full-support hypothesis or parity
approximation.

The actual closing scalar C_N(F)=phi(F) selects coordinate d; the cap
scalar D_N(F)=phi(TF) selects coordinate zero. Hence exact closed support is
read directly from (2), or for a cylindrical final product from

$$
C_N(FG)=\sum_{r=0}^d f_r g_{d-r}.\tag{3}
$$

All factors here have the existing physical normalization. For changed
leaves T(R^epsilon L_j), use the same finite contraction (1),(3) with their
actual signed core/alias arrays. Positivity and the interval conclusion
are claimed only for the complete pure source; the compiler itself is
valid without positivity.

## 2. An exact strict-state classification, separate from finite support

A strictly realized open output b means all underlying leaf labels lie in
(0,1/2), and every product satisfies

$$
\max(x,y)<z<x+y<1.\tag{4}
$$

Turns impose y=1-x. For arbitrary finite h/T/product syntax, the set of
strictly realized outputs is one of FOUR possibilities:

$$
L=(0,1/2),\qquad H=(1/2,1),\qquad A=(0,1),\qquad \varnothing.
\tag{5}
$$

Here h has type L; T exchanges L,H, fixes A, and preserves emptiness.
The product table is symmetric:

$$
\begin{aligned}
LL&\longmapsto A,& LA&\longmapsto A,& AA&\longmapsto A,\\
HL&\longmapsto H,& HA&\longmapsto H,& HH&\longmapsto\varnothing.
\end{aligned}\tag{6}
$$

If either child has empty strict-state set, so does its parent. This table
is exhaustive, not a necessary-only filter. For LL at any b in (0,1),
choose both inputs a with b/2<a<min(b,1/2). For LA, choose a sufficiently
small L input c and A input b-c/2. The AA case follows by using two inputs
in L. For HL or HA, necessarily b>1/2; choose the H input b-c/2 and the
other input c>0 sufficiently small. HH violates x+y<1. These constructions
also prove every asserted interval is attained.

For a cylindrical final product C(FG), delete only its forced last gate.
A strict reduced state exists exactly when

$$
S_F\cap(1-S_G)\ne\varnothing.\tag{7}
$$

where S is the strict output set. Thus LL and HH fail, while LA, HA, AA,
and LH pass. Neither this classification nor an empty strict-state type
asserts that the finite quantum source vanishes. For example T(h)T(h) has
zero source at even levels. At odd level \(N=2m+1\), both input
indices must equal \(m\), but their product has positive coefficients
at every output index \(m,\ldots,2m=d\), by (2). Thus the inputs
are confined to the boundary even though the output is not supported
at a single index.

The completed grammar used here is

$$
E\ ::=\ hh\ \mid\ T(E)\ \mid\ EE\ \mid\ hE\ \mid\ Eh.
\tag{8}
$$

It may equivalently include any h^s, s>=2, as initial blocks. Every E in
(8) has type A and admits a strict state at EVERY output b in (0,1).
Consequently every fixed C(FG), F,G in (8), has a strict reduced state:
choose both closing outputs1/2. A cylindrical closure with one bare leaf
and one E also has strict states, but has a distinct packet issue in §5.

## 3. Primitive lattice, unique strict optimizer, and complete source

No old all-output finite-support statement is imported. Contract every
turn chain by its exact relation r->d-r. At a cylindrical final product,
eliminate one root input using i+j=d and delete that gate, whose coefficient
is exactly one. The root subtrees are disjoint. Hence no equation2r=d is
created. The remaining unturned wire outputs are free integer coordinates;
all other indices are integer affine functions with coefficients+1 or-1.

If there are H original h leaves, there are H-1 binary products. Removing
the last one leaves H-2 independent product outputs, H leaf outputs, and
one closing relation. Thus the free dimension is

$$
K=2H-3.\tag{9}
$$

Round d times a strict reduced state in these primitive coordinates and
restore eliminated indices exactly. Errors stay bounded for a fixed tree,
whereas each strict inequality has a fixed macroscopic slack. All original
leaf and gate support constraints hold for every sufficiently large N,
at BOTH parities. In particular all leaf indices lie strictly below M;
the even A2 missing top coordinate is irrelevant to this interior argument.
For an arbitrary expression, a prescribed open output must have
r_N/d->b in its ACTUAL strict-output interval S_E. For the completed
grammar (8), S_E=(0,1), so every interior b is allowed. Fix that output
first and round the remaining coordinates in a strict state at r_N/d.

The original leaf/gate factorial bounds are uniform on the closed support
and have O(log N) errors for a fixed tree. The usual leaf atoms
(x,1/2-x,1/2), twice, and three gate atoms are unchanged. Any nonforced
boundary maximum has a nonvertex-flat atom, possibly reached by descending
through endpoint wires and turns. The segment to the constructed strict
state has positive infinite entropy derivative there; no other atom has
negative infinite derivative. Thus the reduced maximum is strict. The
retained angle maps recover all free wires, so strict tetrahedral concavity
gives a negative definite reduced Hessian and a unique optimizer. This is
the original barrier/injectivity proof with the new strict-state construction.

Polynomially many states give the upper limit. Primitive rounding of the
strict maximizer gives a genuine positive single-state lower limit at every
sufficiently large N. The original complete source therefore has its full
positive exponential rate, and fixed-output profiles are analytic:

$$
\lim_{N\to\infty}\frac1N\log Z_N^0=\max\mathcal A,
\qquad f_E(b)=\max_{\text{output }b}\mathcal A_E.\tag{10}
$$

This theorem is about the original positive source, not yet its mixed
whole-source replacement or a new topological volume identification.

## 4. Normal forms and actual topological operations

There are three distinct levels of simplification.

(a) Literal stack associativity merely changes the heights and parentheses
of fixed ordered boxes and is a boundary-preserving tangle isotopy. It
retains every coupon, turn and frame. Flatten consecutive product vertices
into an ORDERED list; do not move any factor through an intervening turn.
This gives a useful actual compiler normal form with alternating product
blocks and turned subexpressions.

(b) In the full source algebra multiplication is commutative and T^2=1.
One may therefore additionally reorder a product block or cancel adjacent
turn operators when computing the scalar, with all mark conventions still
recorded. These source equalities do NOT prove relative-boundary tangle
isotopies for arbitrary boxes. In particular T is not multiplicative, and
there is no valid rule T(FG)=(TF)(TG). The exact Frobenius identity
phi((TF)G)=phi(F(TG)) follows by coefficient reversal, but it too must not
be promoted to an unproved physical tangle move.

For the open positive expression grammar, flattening product blocks,
using source-only commutative reordering, and removing adjacent algebraic
turns gives a syntactic criterion for the OLD
A_s>=2 grammar: every leaf belongs to an unturned product block, and
in each maximal product block the number of direct bare h factors is either
zero or at least two; each turned child must recursively satisfy the same
condition. In particular a lone h or T(h) is not an old completed
expression. The new grammar (8) additionally permits one
bare h beside a completed factor. Thus h T(hh), and chains built by
E_(n+1)=h T(E_n) starting at hh, are new presentations under this restricted
normalization. This is NOT a proof of a new knot isotopy class or of
inequivalence under all possible source identities. Some closed instances
regroup into old grammar: for example C((h T(A2))A2)=C(A3 T(A2)) as a source
scalar. Keep the actual ordered diagram when drawing any geometric claim.

(c) The [existing boundary cap reduction](actual_conway_cap_sum_reduction.md)
has a separate topology proof. With a closing flag C or D, a turn switches the flag; a D-product
splits into its two D-children because

$$
D_N(FG)=D_N(F)D_N(G).\tag{11}
$$

The physical empty collar exhibits the corresponding TWO-punctured sphere
and componentwise connected sum, with the upper/lower cap components and
mark transported. A C-product is retained, not factored. This gives an exact
source and topological boundary reduction for arbitrary boxes, but is not
a JSJ decomposition or an isotopy reducing every new tree to old robust
ones. The entire rational angle polytope also splits at a D-product.

## 5. The precise high-index and packet interface

The original stationary port variables are B=cot(pi b),
X^2+Y^2-B^2=1, X,Y>0. A leaf has (B,X,Y)=(X,X,1). Every completed E in (8)
satisfies -Y<B<X at each interior optimized output. The $A_2$ base and ordinary
completed product/turn steps are proved in the [existing port theorem](actual_conway_strict_leaf_quarter_bound.md)
and the [two-leaf base extension](actual_conway_two_leaf_seed_geometry.md). For
a single leaf attachment to a completed child, stationarity gives common X
and, writing B for the child cotangent,

$$
\begin{aligned}
B_{\mathrm{parent}}&=X-\frac1{X+B},\\
Y_{\mathrm{parent}}&=\frac{Y_{\mathrm{child}}}{X+B},\\
Y_{\mathrm{child}}&=\sqrt{1+B^2-X^2},\qquad X+B>0.
\end{aligned}\tag{12}
$$

This preserves -Y_parent<B_parent<X. If X>=1 this is immediate from B>0
and X^2-1>=0. If X<1, put h0=sqrt(1-X^2), alpha0=arccos X. The leaf has
angle alpha0 in B=h0 cot(alpha); the completed child has beta>alpha0,
and X+B>0 says alpha0+beta<pi. Their sum gives the strict parent inequality.

At completed/completed closure C(FG), the original matching of ports gives
X,Y<1 at both root children. At any product with X<1, every child angle is
at least alpha0, with equality only for a leaf; a completed child's angle
is strictly greater. The bound Y_parent<1 means alpha+beta<pi-alpha0, so
each completed child also has Y<1. Turns exchange X,Y. Hence all completed
ports in the closed grammar have X,Y<1, and every leaf has X<1, i.e. its
Newton coordinate is strictly greater than1/4.

For a direct single attachment, Y_parent<1 and B<X sharpen this to

$$
\frac12<X<1,\qquad \frac1{2X}-X<B<X.\tag{13}
$$

Indeed Y_child<X+B squares to1<2X(X+B), and B<X then forces X>1/2.
The same lower X bound for the leaves in an A2 base follows from its
Y=1/(2X)<1. Thus every leaf of a fixed completed/completed tree has a
positive margin inside (1/4,atan(2)/pi). No uniform margin over all trees
is asserted.

This supplies the exact LOCAL changed-source packet assumptions: fixed
strict high-index window, the original relative exponential interpolation,
primitive dimension (9), and all original affine shifts. Each leaf
contributes N^(1/2), each of H-2 retained gates N^(-3/2), giving summand
N^(3-H). Its Gaussian lattice factor N^(K/2) produces N^(3/2). The changed
leaf and gate derivatives in the original integer-offset amplitude remain
mandatory. At completeness the multiplier is nonzero, and the separately
even color Hessian retains diagonal entries

$$
-\frac{2\pi X_l}{1-\epsilon_l iX_l}.\tag{14}
$$

with negative real part. These are local finite packet facts; the full
mixed source still needs §6.

Root-leaf closures require an explicit exclusion from this automatic
interface. At C(hE), the completed root may have Y=1, and a turn can pass
that equality to X=1 deeper inside. In the exact example C(h T(A_s)),
A_s at X=1 has B_s=Y_s=1/s. The turn gives (-1/s,1/s,1), which matches the
closing leaf with X=1/s. Thus all s inner leaf indices are EXACTLY1/4,
while the remaining leaf is arccot(1/s)/pi. Strict complete states exist,
but the inherited strict-quarter packet cannot simply be quoted. The even
simpler C(h T(h)) has exact scalar sum_r a_r^2 and a unique complete leaf
coordinate1/4. These are source/packet limitations, not asserted topology
or hyperbolicity obstructions. The [isolated $C(A_3)$ theorem](actual_conway_isolated_three_leaf_long_twist_volume.md) is separately proved and
does not justify every root-leaf closure.

## 6. Exact reduction of the mixed gap to one new local dual inequality

Fix the actual closed complete optimizer of C(FG) in (8). For each completed
subtree E let b_E be its optimized output and lambda_E=f'_E(b_E). The useful
inductive statement is, uniformly in every physical color and finite output
r and for EACH specified alias subset S_E,

$$
\left|[\widehat B_r]E_{S_E}\right|
 \le\exp\!\left\{N\left[f_E(b_E)
 +\lambda_E\left(\frac rN-b_E\right)-\delta_{S_E}\right]+o(N)\right\}.
\tag{15}
$$

where delta_empty=0 and delta_nonempty>0. No coefficient lower bound or
sharpness of this envelope is asserted. A2 supplies this statement through
the uniform block lemma. At a turn, exact coordinate reversal
retains it with lambda sign reversed and an O(1) affine exponent cost.
At a product of completed subtrees, their tangents and the concavity of the
actual gate m give the parent's tangent by stationary cancellation; child
gaps add. Every state retains the original i+j<=d constraint.

The only new step is hE. At its actual common-X state let

$$
\begin{aligned}
a&=\frac{\operatorname{arccot}X}{\pi},\qquad
 y=\frac{\operatorname{arccot}B}{\pi},\\
z&=\frac{\operatorname{arccot}(X-1/(X+B))}{\pi},\\
\lambda_c&=2\log(X/Y_{\mathrm{child}}),\\
\lambda_p&=\lambda_c+2\log(X+B).
\end{aligned}\tag{16}
$$

All arccot values lie in(0,1) after division by pi. The parameter region is
exactly (13). The local inequality needed for this induction, proved in §7, is the
strictly positive margin

$$
\begin{aligned}
\Delta(X,B)&=g(a)+\lambda_cy+m(a,y,z)-\lambda_pz\\
 &\quad-\max_D\{k(u)+\lambda_cv+m(u,v,w)-\lambda_pw\}>0,\\
D&=\{(u,v,w):u,v\ge0,\ \max(u,v)\le w\le u+v\le1\}.
\end{aligned}\tag{17}
$$

The actual alias index u is NOT restricted below1/2. The child output v
also retains its whole original interval. The finite kernel and all
normal directions have already been accounted for in (1).

If the new leaf is core, replace k(u) by gtilde(u), u<=1/2. Concavity and
stationarity give equality of that maximum with the pure reference in
(17). Thus a contaminated child transfers its existing gap. If the new
leaf is alias, (17) supplies a gap whether the child is clean or already
contaminated; in the latter case the child gap adds. This proves (15)
inductively once (17) is proved at the finitely many actual attachment
states. The fixed tree needs only positive margins there, not a universal
lower bound throughout the open parameter region.

Finally the two root tangents cancel on the literal i+j=d. The N versus d
shift gives only a fixed O(1) exponent. Summing polynomially many original
states and finitely many sectors produces a whole-source alias gap. The
all-core concave majorant has its unique strict maximum at the actual pure
optimizer; compact outside-window and actual local far-color losses then
give the whole physical-color complement gap. This is the same finite
source-to-packet interface as the block proof, with (17) as its
ONLY new analytic alias obligation. Section7 supplies it. The actual
geometric and marked filling interfaces remain separately sourced; the finite contraction alone
is not a new topological volume proof.

## 7. The exact square certificate discharges the remaining inequality

Write mu=lambda_c and lambda=lambda_p. Define the two exact variational
quantities on the original product tetrahedron D from (17):

$$
\begin{aligned}
P(\mu,\lambda)&=\max_{D,\,u\le1/2}
 \{g(u)+m(u,v,w)+\mu v-\lambda w\},\\
Q(\mu,\lambda)&=\max_D
 \{k(u)+m(u,v,w)+\mu v-\lambda w\}.
\end{aligned}\tag{18}
$$

The pure objective is concave. At the actual point(a,y,z), its three
derivatives vanish by the original stationary equations, so its maximum
is exactly the pure reference in (17). The same is true with gtilde in
place of g: near a>1/4 they agree, and both resulting objectives are
concave. Hence P-Q=Delta(X,B) for the actual slopes.

For 1/2<X<=2/3 and L=1/(2X)-X<B<X, the two slopes belong to
[-2log2,0]. To check this directly, B is positive and

$$
\frac1{4X^2}<Y_{\mathrm{child}}^2<1,\qquad
\log(X^2)<\mu<\log(4X^4)\le\log(64/81)<0.\tag{19}
$$

For lambda(B)=log[X^2(X+B)^2/(1+B^2-X^2)], its derivative has the sign
of 1-X^2-XB, which is positive throughout this region since
1-X^2-XB>1-2X^2>=1/9. At B=L and B=X its limits are log(X^2) and
log(4X^4), respectively. These are both in[-log4,0]. Thus the following
certificate applies to every actual low-X attachment.

The [exact attachment verifier](../experiments/verify_conway_single_leaf_attachment_certificate.py)
imports the unchanged outward rational arithmetic and analytic enclosures
from the [two-leaf verifier](../experiments/verify_conway_two_leaf_block_alias_certificate.py).
Its [fixed rational data](../experiments/conway_single_leaf_attachment_certificate.json)
is a recursively subdivided quadtree of 55 closed dyadic rectangles covering
$(\mu,\lambda)/\log2\in[-2,0]^2$.
Each leaf has a rational pure point p with p_1<1/2 and a rational strict
alias point q, both in D. No optimizer is used by verification.

For H=k+m, concavity gives its global affine upper tangent at q. For each
of the four rectangle corners and each of the FOUR original vertices

$$
(0,0,0),\quad(1,0,1),\quad(0,1,1),\quad(1/2,1/2,1/2).
$$

the verifier checks the lower bound

$$
\begin{aligned}
&g(p_1)+m(p)-[H(q)+\nabla H(q)\mathbin{\cdot}(w-q)]\\
&\qquad+\mu(p_2-w_2)-\lambda(p_3-w_3)>\frac1{1000}.
\end{aligned}\tag{20}
$$

This is880 exact inequalities. Affinity in each slope and in w extends
(20) throughout the entire rectangle times D. The pure point provides a
lower bound for P, while the tangent provides an upper bound for Q.
Recursive four-way subdivision proves full square coverage without gaps;
no sampling or approximate coverage enters the argument.

All interval arithmetic uses outward integer rounding at denominator 10^40. The Machin arctangent, sine Taylor, atanh-log and integrated Euler-sine expansions have exact rational remainders. The imported arithmetic and analytic-function syntax trees are identical to those in the block certificate. The [recorded result](../experiments/conway_single_leaf_attachment_certificate_results.json) gives the least certified rational lower bound:

$$
\frac{55437191760019874892517972684020763373}{10^{40}}
 >\frac1{1000}.\tag{21}
$$

Thus P-Q>1/1000 on the full square, and in particular Delta>1/1000
at every actual attachment with X<=2/3.

For $X\ge2/3$, the [existing exact full-leaf tangent certificate](actual_conway_algebraic_leaf_alias_certificate.md) gives

$$
k(u)\le g(a)+g'(a)(u-a)-\frac1{2500},\qquad 0\le u\le1.
\tag{22}
$$

The tangent of the concave gate m and the identities
g'(a)+m_u=0, mu+m_v=0, m_w=lambda then cancel all three variables.
Consequently Delta>1/2500 also throughout this remaining actual region.
Neither part discards alias indices above half.

The induction (15) is now proved for every fixed completed tree (8).
Every contaminated A2 starts with its known block gap; every newly aliased
single attachment has (20) or (22); an existing child gap passes unchanged
or adds. Turns and all exact closing offsets cost only O(1) in the exponent.
Since the tree is fixed, summing its actual finite sectors gives a positive
whole-source alias margin. Compactness and the actual far-color estimates
then give the entire physical-color complement gap as described in §6.
These are source bounds for all original colors and both parity sequences.
Together with §5 they supply the unchanged finite complex packet and
whole-source hypotheses for the separately verified geometric/filling
interfaces. No additional individual leaf certificate is required.

## 8. Inputs

The original [physical source/compiler](actual_positive_complete_circle_conway_trees.md)
and [positive full-Newton multiplication](actual_positive_newton_multiplication.md)
supply the exact finite operations. The
[two-leaf source proof](actual_conway_two_leaf_seed_source.md), §§1–2,
supplies the predecessor strict-state and rounding arguments. The
[complete geometric proof](actual_positive_conway_hyperbolic_volume.md), §§3–6,
and the port inputs linked above retain the original leaf and prism data.
The local changed source is the
[actual mixed complex packet](actual_odd_conway_complex_color_packet.md).
The induction starts with the
[uniform two-leaf alias lemma](actual_conway_uniform_two_leaf_block_alias_gap.md)
and its [finite block source adapter](actual_conway_two_leaf_block_source_gap.md).

The exact finite support and strict-state tables are proved for arbitrary
$h/T$/product syntax. The all-output, strict-quarter and local-packet
extension, and the automatic mixed gaps proved here, are restricted to
(8) with completed/completed $C(FG)$ closure. The normal-form discussion
distinguishes actual stack isotopy, algebraic scalar identities, and the
separately proved cap connected-sum moves. It does not assert coverage of
all algebraic tangles or knots, or exhibit a new isotopy class. The
root-leaf quarter examples prevent extending the inherited packet from
strict feasibility alone.

The rational certificate uses rigorous function enclosures; no continuum
inequality is inferred from sampled or floating-point tests.
