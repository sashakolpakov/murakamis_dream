# Deleting quarter-turn edges in the old positive pressure

Private proof, 1 November 2026. The comparison retains entire
neighboring profiles and all correlations between their incidences.
It does not identify the links before and after deletion.

## 1. The original tree and its complete contraction

Let \(\mathcal G\) be a finite connected ordered tree of bare product
junctions. Each actual junction has full valence at least three,
counting external incidences, and every internal edge is a physical
quarter-turn. External branches carry the old rigid profiles
\(g(a)+c_j\), \(0\le a\le1/2\), with their original constants.
Write \(F(\mathcal G)\) for the full old positive maximum, retaining
the hidden wires in the original ordered product resolutions.

At level \(N\), use the fixed complete Newton basis \(e_0,\ldots,e_d\),
\(d=N-1\), with the complete Frobenius functional \(\phi_0\).
Its exact metric and turn are
\[
        \phi_0(e_i e_j)=\delta_{i+j,d},\qquad
        T_0(e_i)=e_{d-i}.
\tag{1}
\]
These are identities of the full complete algebra, including the
first normals at repeated nodes. A covariant whole-junction tensor
is \(\phi_0(\prod e_{n_j})\). Contracting a physical turn identifies
equal covariant labels at its two ends. An unturned contraction
identifies complementary covariant labels.

For a subset \(S\) of the original internal edges, remove the
quarter-turn from every edge in \(S\), and fuse the resulting
unturned product connections. Denote the resulting ordered tree
by \(\mathcal G/S\). All physical edges outside \(S\) remain
quarter-turns. The external branches and constants are unchanged.

**Theorem.** For every finite edge set \(S\),
\[
                         F(\mathcal G/S)\le F(\mathcal G).
\tag{2}
\]
This holds without a matching assumption on \(S\). Each fused
vertex still has valence at least three and the new positive tree
has its original strict maximum. For a single deleted edge, equality
holds if at least one of its two rooted sides is a single trivalent
junction with two rigid leaf branches. If neither side has that
form, the inequality is strict.

## 2. Exact fusion and the inherited order

The basis dual to \(e_i\) under (1) is \(e_{d-i}\). Thus, for any
two complete polynomials \(A,B\),
\[
 \sum_{i=0}^d\phi_0(Ae_i)\phi_0(e_{d-i}B)=\phi_0(AB).
\tag{3}
\]
Indeed expand \(A=\sum_i\phi_0(Ae_i)e_{d-i}\) and apply
\(\phi_0(\,\cdot\,B)\). This proves (3) in the complete algebra
itself, and makes no distinct-node specialization. Applying it to
the factors at two neighboring junctions fuses precisely their
complementary-index connection into one whole-junction tensor.

In particular, changing one endpoint of an equal-index connection
from \(i\) to \(d-i\) changes that connection into the unturned
pairing in (3). If both endpoints were reflected, the connection
would still have equal labels. For the one-high application below,
each selected edge is reflected at exactly one endpoint.

The order on a fused vertex is the induced ribbon order. Concretely,
take a small oriented regular neighborhood of the two vertex disks
and their connecting band, remove that internal band from the
boundary list, and read the remaining half-edges along the resulting
boundary. No permutation of attached branches is performed. With
a root chosen outside this band, this operation is just substitution
of the child's ordered product into its position in the parent's
ordered product. Associativity flattens that unturned insertion.
The unchanged external branches keep their orders, rotations and
attachments.

Formula (3) proves the positive tensor identity in this induced
order. Its symmetry does not serve as a premise for an isotopy of
arbitrary tangles. Deleting a physical quarter-turn generally
changes the diagram; the theorem compares its positive pressure
with that of the original diagram.

If vertices of valences \(D_1,D_2\ge3\) fuse, the new valence is
\(D_1+D_2-2\ge4\). More generally a connected fused set \(K\)
has valence
\[
                 2+\sum_{v\in K}(D_v-2)\ge3.
\tag{4}
\]
Because the original graph is a tree, contraction creates neither a
cycle nor a duplicated branch. The induced order is also independent
of the order in which the edges of a fixed fused set are contracted:
it is the boundary order of that same regular neighborhood.

The closed old pressure of each fused hub is the maximum over its
prescribed positive binary resolution. The fixed-label arity lemma
constructs this resolution whenever its external labels have pair
sums below one and total above one. For example assigning \(3/8\)
to all physical incidences is strictly feasible at every fused hub.
Hidden unturned wires are then constructed by that lemma, not
assigned \(3/8\). The usual barrier and negative-Hessian arguments
give a unique strict maximum of the fused tree. Thus every stage
of the deletion process remains in the old strict pressure class.

## 3. The exact one-edge pressure comparison

Cut one physical edge in a tree of this class. Root each remaining
side at that incidence. It is an unturned product of at least two
inputs: an external branch is rigid type \(L\), and a branch
through another hub is the physical turn of an unturned type-\(A\)
product, hence again type \(A\). The two rooted profiles, denoted
\(f_A(b),f_B(b)\), retain all their original subtrees and constants.
They are continuous on \([0,1]\), analytic and strictly concave
on \((0,1)\), and have their unique strict constrained states.

The proper product-response inequality gives
\[
        f_X(b)\ge f_X(1-b),\qquad 1/2\le b\le1,
                         \quad X\in\{A,B\}.
\tag{5}
\]
For clarity, this is the original unturned-product inequality, not
an inequality for an arbitrary top-turned profile. At the last
binary product its positive response satisfies
\[
 Y^2=(B_1-B)(B_2-B)\le(X-B)^2,
 \qquad X^2+Y^2-B^2=1,
 \qquad B<B_i\le X.
\tag{6}
\]
Consequently \(X\ge(B+\sqrt{B^2+2})/2\), so
\(f_X'(b)\ge f_2'(b)\), where the two-leaf profile \(f_2\)
is symmetric about half. Integrating from \(1-b\) to \(b\)
proves (5). The comparison is strict for \(b>1/2\) if the last
product has a proper composite child. A rooted side fails to have
such a child exactly when it is one trivalent hub with two rigid
leaf inputs; then its profile is \(f_2+c\), exactly symmetric.
The strict endpoint case follows by continuity and the strictly
increasing difference \(f_X(b)-f_X(1-b)\) for \(b>1/2\).

For the physical turn the covariant labels are equal, so both
ordinary outputs agree. For the deleted turn they are complementary.
The two complete pressures are therefore exactly
\[
\begin{split}
 F_{\mathrm{turn}}&=\max_{0\le b\le1}\{f_A(b)+f_B(b)\},\\
 F_{\mathrm{deleted}}&=\max_{0\le b\le1}
                              \{f_A(b)+f_B(1-b)\}.
\end{split}
\tag{7}
\]
These identities include all internal maximizations; no branch is
replaced by an independent capped norm budget.

If \(b\ge1/2\), the deleted summand is bounded by
\(f_A(b)+f_B(b)\), using (5) for \(B\). If \(b\le1/2\),
it is bounded by \(f_A(1-b)+f_B(1-b)\), using (5) for \(A\).
Thus in both cases it is bounded by a feasible matched summand
with ordinary output \(\max(b,1-b)\). Maximizing proves
\[
                         F_{\mathrm{deleted}}\le F_{\mathrm{turn}}.
\tag{8}
\]

If \(f_B=f_2+c\), the two summands in (7) agree identically;
if \(f_A=f_2+c\), substitute \(b\mapsto1-b\). Hence one
symmetric side gives equality. If neither side is symmetric, the
pointwise comparison is strict away from half. At half, both
derivatives \(f_A'(1/2),f_B'(1/2)\) are strictly positive, so
the matched summand is not maximal there. Compactness now gives
a strict inequality of maxima. This proves the equality assertion.

## 4. Any finite family of deleted turns

Delete the edges in \(S\) successively. After each deletion, (3)
fuses the affected ordered products. Equations (4) and the strict
witness show that the remaining graph is again a tree in the same
class, with precisely the same external rigid profiles and constants.
Every remaining edge is still a physical quarter-turn. Therefore
(8) applies anew, to the actual profiles of that current tree.
It yields
\[
 F(\mathcal G/S)\le F(\mathcal G/S')\le F(\mathcal G)
                         \qquad(S'\subset S).
\tag{9}
\]
The profiles may change after fusion; they are never replaced by
the previous profiles without recomputation. This is why the
argument preserves the correlations between several reflected
incidences, unlike an iteration of a fixed multi-boundary pressure
with other marks held in the wrong response class.

The identity (3) also shows that a restricted reflected sector is
bounded by the full positive contraction of \(\mathcal G/S\).
The hidden complementary labels are summed in the fused tensor;
discarding their original band restrictions only enlarges that
positive upper bound. Equations (2) and (9) then compare its rate
with the original \(F(\mathcal G)\).

## 5. The one-high and several-high sector graph

Here is the precise graph bookkeeping needed for the moving-source
application. Assume the local Fourier difference bound has replaced
a selected moving tensor with exactly one high incidence by its old
tensor with that incidence reflected. All its other incidences are
low. Actual physical turn types prevent two moving equal-color
vertices from being adjacent.

An internal reflected incidence therefore meets a constant old
vertex. A nonzero old whole tensor has at most one strictly high
incidence, by its complete pairwise support. Two selected reflected
edges cannot meet at that old vertex. Nor can two meet at a selected
one-high moving vertex. Thus the selected internal edges form a
matching. Each connects a selected moving vertex and an old vertex;
both endpoints have no other high exterior incidence.

Fuse these edges using (3). Each fused hub has only low exterior
incidences in the original sector, and full valence at least four.
In particular it creates no new high marked interface when other
moving vertices with at least two high incidences are subsequently
removed. Those latter vertices are never fused. They remain
pairwise nonadjacent: no contraction joins two of their vertices,
and a fused vertex is still retained between any such vertices
which shared its endpoints as neighbors.

The remaining old regions therefore still have at most one high
marked incidence per actual old hub. Their low arms retain the full
old correlations. The separate several-high comparison may attach
one \(g\) profile on each low arm and reinsert its half-cardinal
old hub, consuming that profile once. It applies in this fused
tree with its actual valences and inherited orders. Its strict
boundary gap is measured below \(F(\mathcal G/S)\), which is at
most the original \(F(\mathcal G)\) by (2).

If the one reflected high incidence is an original external leaf,
there is no internal edge to fuse. Its original high coefficient
cone has rate \(c_j\). After reflection its low label is \(r\);
the old rigid comparison leaf has rate \(g(r)+c_j\). Introducing
that old leaf is an upper bound because \(g(r)\ge0\), and the
exact loss \(g(r)\) must be retained if a strict estimate is needed.
The original constant is unchanged. This case is distinct from
internal turn deletion.

These observations supply the positive-pressure bookkeeping, not
the local Fourier difference estimate or its uniform error. In
particular pressure equality can occur in (8), so a strict analytic
gap cannot be claimed from deletion alone. The local Fourier-tail
loss or an original strict boundary separation must provide it.

## 6. Which geometric action is the target

The original marked geometry identifies \(F(\mathcal G)\) with
the complete geometric action of the original strict diagram.
The fused tree is a positive comparison calculation. It need not
describe the same link, have the same peripheral marking, or have
the same augmented complement. This proof uses only its strict
pressure and the inequality (2).

Consequently a completed moving-source estimate must continue to
use the original primitive lattice, actual circle colors, marked
crossing powers and filling action when it invokes the existing
source and filling theorems. The final knot-complement volume is
that of the original marked filled diagram. No deleted diagram's
volume is substituted for it.
