# One return cluster and the limits of geometric clamping

Private derivation, 1 November 2026. No published source is changed.

The return tensor has nonpositive classical action, but this alone does not compare a whole contraction with its original complete maximum. The missing issue is the action of the branches attached to its boundary. This note proves a comparison when all return vertices form one high-edge cluster in a trivalent tree with a physical turn on every internal edge. It then gives exact reasons why that proof cannot simply be iterated or applied to a higher-valence multiplication vertex.

The exact tensor and edge convention are those of /private/tmp/md-fixed-newton-return-gates-and-contracted-tensor.md. The classical branch input is the unturned-product derivative theorem in notes/actual_conway_unflagged_probe_geometry.md, Appendix A. All branch profiles below are the original positive profiles, with their additive constants retained. A signed coefficient estimate, or a plateau majorant substituted for a leaf profile, is not part of the hypotheses.

## 1. The action and the precise tree hypothesis

Put
\[
J(u)=\int_0^u\log(2\sin\pi v)\,dv,\qquad
g(a)=J(2a)-4J(a),\qquad 0\le a\le\tfrac12.
\tag{1}
\]
The complete symmetric cubic action is
\[
t(x,y,z)=J(x+y)+J(x+z)+J(y+z)
 -J(x)-J(y)-J(z)-J(x+y+z-1),
\tag{2}
\]
on
\[
x,y,z\ge0,\qquad x+y,\ x+z,\ y+z\le1,\qquad x+y+z\ge1.
\tag{3}
\]
The return action in complementary variables \(a=1-x,b=1-y,c=1-z\) is
\[
\mathcal R(a,b,c)=J(a)+J(b)+J(c)+J(a+b+c)
 -J(a+b)-J(a+c)-J(b+c),
\tag{4}
\]
on \(a,b,c\ge0,\ a+b+c\le1\). Thus its original labels satisfy
\[
x,y,z\in[0,1],\qquad x+y,\ x+z,\ y+z\ge1,\qquad x+y+z\ge2.
\tag{5}
\]
The exact integral identity
\[
\mathcal R(a,b,c)
 =-\pi^2\int_0^a\int_0^b\int_0^c
       \csc^2(\pi(u+v+w))\,dw\,dv\,du.
\tag{6}
\]
shows that this continuous action is nonpositive on its closed domain and strictly negative when all three complements are positive.

Let \(\Gamma\) be a finite trivalent tree. Every internal edge carries an actual quarter-turn, so its two covariant cubic labels are equal. An unturned composition would instead identify complementary labels; such edges are excluded here.

Each external leaf carries an effective original profile \(g(a)+c_\ell\), \(0\le a\le1/2\). The constants \(c_\ell\), possibly supplied by rigid \(L\)-type satellites, are retained. Assume that replacing every vertex by (2) gives an eligible strict positive source, with compact closed state polytope, unique maximum \(F_0\), and a strict maximizing state. In particular every retained cubic pair sum is strictly below one there. The existing complete geometry identifies \(F_0\) with the normalized geometric action of this original source.

Choose a nonempty set of return vertices and use (2) at all other vertices. We restrict to a sector in which all return vertices belong to one connected component of the edges with label greater than \(1/2\). To discuss its closure, record those high edges, allow their labels to equal \(1/2\), and require every unrecorded edge to have label at most \(1/2\).

At an interior return vertex at least two incident labels exceed \(1/2\), by (5). At a complete vertex at most one does, by (3). Thus every high boundary edge of the return component ends in a complete branch, and there are no other return vertices inside that branch. The recorded closed-sector convention retains this combinatorial decomposition at ties.

## 2. The available branch pressure

Cut a high boundary edge immediately outside the return component. The complete vertex on its other side is the last unturned binary product of the branch. If its covariant boundary label is \(z\), its ordinary output is
\[
b=1-z.
\tag{7}
\]
Its two input subtrees have strict type \(L\) or \(A\). Recursively, an unturned product of \(L/A\) inputs has type \(A\), and every further internal edge is a turn, which preserves type \(A\). External leaves have type \(L\). Hence the branch is an unturned product \(A=FG\), rather than an arbitrary type-\(A\) profile with a top turn.

Let \(f_A(b)\) be its optimized original positive action, including all constants. The unturned-product derivative theorem gives
\[
f_A'(b)\ge f_{hh}'(b)>0\quad(0<b<1/2),\qquad
f_A(b)\le f_A(1/2)\quad(0\le b\le1/2).
\tag{8}
\]
Its geometric reason is the unsquared relation at the branch optimizer
\[
Y^2=(B_1-B)(B_2-B)\le(X-B)^2,\qquad B<B_i\le X.
\tag{9}
\]
For \(B=\cot\pi b\), this implies
\[
X\ge X_2(B)=\frac{B+\sqrt{B^2+2}}2,\qquad
f_A'(b)\ge2\log(2X_2(B)^2).
\tag{10}
\]
When \(b<1/2\), \(B>0\) and \(X_2(B)>1/\sqrt2\). Endpoint continuity follows from the compact state polytope.

A branch state not already optimized has action at most \(f_A(b)\). Replacing the entire branch by an optimizer at output \(1/2\) cannot decrease its action. This replacement changes internal labels and physical leaf labels; it is not a variation with other boundary data held fixed.

## 3. The one-cluster comparison

**Proposition.** Under Section 1's hypotheses, every state in the closed one-cluster return sector has action at most \(F_0-\delta_\Gamma\), with \(\delta_\Gamma>0\) depending only on the original complete source. The action is the sum of the complete cubic actions, return actions, and original leaf profiles and constants.

**Proof.** Set every recorded high edge in the return component, including its boundary edges, to \(1/2\). Keep every low edge incident to a return vertex fixed. Reoptimize each high terminal complete branch as in (8). Leave all remaining complete branches and labels unchanged.

The reoptimized branches are disjoint. Two distinct boundary edges cannot enter the same outside component without making a cycle in the original tree. Thus no low interface is prescribed twice and no branch action is counted twice.

Each return vertex has two or three recorded high incident edges. Its new labels are therefore \((1/2,1/2,u)\), \(0\le u\le1/2\), or \((1/2,1/2,1/2)\). Both satisfy (3), and
\[
t(1/2,1/2,u)=g(u)\ge0,\qquad
t(1/2,1/2,1/2)=0.
\tag{11}
\]
Indeed \(J(1/2)=0\) and \(J(2u)=2J(u)+2J(1/2+u)\). Nonnegativity of \(g\) follows from its concavity and zero endpoint values.

The original return action was nonpositive by (6). Thus (8) and (11) construct a feasible all-complete state with at least the original action. This preserves every leaf constant and every interface term; no independent probe pressure is added.

At every replaced vertex an old pair-sum inequality is an equality. The constructed state lies in the compact boundary subset
\[
\mathcal B_\Gamma
 =\{\text{old states with a retained cubic pair sum equal to }1\}.
\tag{12}
\]
This set excludes the unique strict maximizing state. Continuity gives
\[
\delta_\Gamma
 =F_0-\max_{\mathcal B_\Gamma}\mathcal A_0>0.
\tag{13}
\]
This proves the bound, including boundary returns with zero local loss. \(\square\)

The same constant works for all recorded high-edge patterns satisfying this single-cluster hypothesis, of which a fixed tree has finitely many. The cluster may have arbitrary size and branching. This is an action upper bound, not a signed lower bound for the finite quantum contraction.

## 4. Fixed low interfaces cannot replace branch reoptimization

An exact old-cell example shows why the branch hypothesis matters. Hold \(x=1/6\), \(y=1/3\), and take \(z=13/24>1/2\). All inequalities in (3) are strict, and
\[
\partial_z t
 =\log\frac{\sin\pi(x+z)\sin\pi(y+z)}
                 {\sin\pi z\sin\pi(x+y+z-1)}.
\tag{14}
\]
When \(x+y=1/2\), product-to-sum makes the ratio
\(-1-\sin(2\pi x)/\sin(2\pi z)\). At the stated point it is
\[
\frac{\sin(\pi/3)}{\sin(\pi/12)}-1>1,
\tag{15}
\]
because \(\sin(\pi/3)>2\sin(\pi/12)\). Hence \(\partial_z t>0\): decreasing the high label with the low interfaces frozen loses complete-cell action.

With several return clusters, the complete region between clusters can have several boundary edges. Its pressure is a joint boundary function, not the independent one-output profile in (8). The example identifies the gap in clamping each cluster separately without a new joint comparison.

## 5. A higher-valence vertex can return with all exterior labels low

Resolving a higher-valence multiplication vertex into cubic vertices introduces unturned internal edges. These pair complementary labels, whereas Sections 1–3 require equal labels.

At \(N=3\), the low indices are \(0,1\), and
\[
e_1(z)=\frac{1-z}{3},\qquad P_s(z)=z^3-3z+2+\Delta,\qquad
\phi_s(F)=9[z^2]F.
\tag{16}
\]
Ordinary division gives
\[
(1-z)^5=(z^3-3z+2)(-z^2+5z-13)+27(z-1)^2.
\tag{17}
\]
Reducing modulo \(P_s\), dividing by \(3^5\), and applying the trace proves
\[
\boxed{\ \phi_s(e_1*_se_1*_se_1*_se_1*_se_1)=1+\Delta/27.\ }
\tag{18}
\]
All five exterior labels are low, yet the return coefficient is nonzero. It is supplied by the top coefficient of the degree-two quotient in (17). This is a finite algebraic obstruction to a valence-independent high-edge argument, not an exponential or knot counterexample. An all-level version is given in /private/tmp/md-return-support-pruning-and-probe-budget.md.

## 6. An absolute open-profile obstruction

Take the genuine unturned three-leaf expression \(A_3=(hh)h\). Let \(f_2\) be the original positive profile of \(hh\); it is symmetric under \(x\mapsto1-x\), strictly concave, and strictly decreasing for \(x>1/2\).

Fix the ordinary output \(b\) at the last product. Its return inputs satisfy
\[
0\le y\le1/2,\qquad 0\le x\le1,\qquad x+y\ge1+b.
\tag{19}
\]
The return complements are \((1-x,1-y,b)\). Define
\[
\mathcal E_{\mathrm{ret}}(b)
 =\max_{(x,y)\text{ satisfying }(19)}
 \{f_2(x)+g(y)+\mathcal R(1-x,1-y,b)\}.
\tag{20}
\]
At \(b=0\) the return action vanishes. For fixed \(y\), its maximum has \(x=1-y\), because \(x\ge1-y\ge1/2\) and \(f_2\) decreases on the right. Therefore
\[
\mathcal E_{\mathrm{ret}}(0)
 =\max_{0\le y\le1/2}\{f_2(1-y)+g(y)\}
 =F_{C(A_3)}>0.
\tag{21}
\]
This is precisely the original positive cylindrical closing problem, whose strict maximizing pair lies on \(x+y=1\).

For every \(b>0\) with nonempty domain, (19) excludes that maximizing set. Compactness and strict concavity give a strictly smaller maximum of \(f_2(x)+g(y)\), and the return term is nonpositive. Thus
\[
\mathcal E_{\mathrm{ret}}(b)<\mathcal E_{\mathrm{ret}}(0)\qquad(b>0).
\tag{22}
\]
The old output profile \(f_{A_3}(b)\) tends to zero as \(b\downarrow0\): old product support forces every input of this three-leaf tree to zero, where the original leaf and gate actions vanish. For all sufficiently small positive \(b\), it follows that
\[
\max\{f_{A_3}(b),\mathcal E_{\mathrm{ret}}(b)\}
 <\mathcal E_{\mathrm{ret}}(0).
\tag{23}
\]
The enlarged absolute open profile is not nondecreasing on its lower output half. This concerns action maxima; it is not a lower bound for an alternating finite sum. The two-leaf subproduct and the final product are joined by an unturned edge, exactly outside the one-cluster proposition's edge hypothesis. The original derivative theorem cannot be reapplied to such an enlarged return-containing branch.

## 7. What remains

The proposition is a genuine geometric comparison for a nonempty structural class. It retains boundary constraints and all constants, and its compact old-boundary gap handles return states at which the local loss vanishes.

A general proof must handle complete regions with several boundary edges and the complementary identifications inside higher-valence hubs. Local nonpositivity, independent probe budgets, arbitrary fixed-interface monotonicity, and monotonicity of the enlarged absolute branch profile do not supply it. A signed whole-contraction argument may avoid the absolute-profile obstruction, but no such estimate is proved here.
