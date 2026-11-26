# Fractional one-sided comparison flows and the load cost of an entropy lift

This note concerns the actual shared-face comparison problem for a fixed marked simple-sphere source. It does not prove a new full-invariant volume theorem. It isolates two exact facts about the fractional rows that remain even after one has fixed every genuine CROSS, LEFT and RIGHT label.

All ordinary face targets are one; the two protected targets are zero. A local triangle has normalized total load \(1/2\), and its entropy is
\[
 C(\alpha)=\sum_{i=1}^3 f(\alpha_i),\qquad
 f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi},
 \qquad \sum_i\alpha_i=\frac12.
 \tag{1}
\]
The absolute normalization is the one in
[actual_triangle_entropy_algebraic_balance.md](actual_triangle_entropy_algebraic_balance.md).
In particular \(C\) vanishes at a triangle vertex. The shared ordinary variables \(L_f\) are curvatures; put \(h_f=\log L_f\). Protected corners are removed before forming any logarithm.

## 1. A genuine label still contains a fractional comparison

For a LEFT row with ordered faces \((x,b,c,y)\), its proved weighted value envelope is
\[
 A_{\mathrm L}(h)=
 \max\!\left\{h_c,\ Q(e^{h_x},e^{h_b},e^{h_y})+\frac12h_c\right\}.
 \tag{2}
\]
The overloaded middle \(c\) is ordinary, or the actual sector is zero. The exact convex-dual row domain of (2) consists of
\[
 q=t\alpha+\left(1-\frac t2\right)e_c,\qquad
 \alpha_x+\alpha_b+\alpha_y=\frac12,\qquad 0\le t\le1,
 \tag{3}
\]
with entropy \(tC(\alpha)\). This is a comparison flow, not a decomposition of the finite LEFT polynomial. RIGHT interchanges the original middle positions.

The fixed-sector capacity is the maximum of the sum of these perspective entropies and the retained CROSS triangle entropies over the original face equations. This follows from the same compact hypograph separation used in
[actual_fixed_triangle_boundary_capacity_gap.md](actual_fixed_triangle_boundary_capacity_gap.md).
The row perspective is continuous at \(t=0\); the entire domain is compact.
At a feasible target the separating vertical coefficient is positive, so no attainment of a finite shared radius is needed. Infeasibility sends the dual infimum to minus infinity.

Thus branching until every genuine label is fixed does not remove \(t\). It only removes mixtures between different genuine labels. The latter distinction is essential in
[actual_shared_radius_certificate_separation.md](actual_shared_radius_certificate_separation.md).

## 2. The doubled comparison domain is an integral network

Fix one genuine sector. For each selected one-sided row write \(z_f=2t\alpha_f\), so \(\sum_fz_f=t\le1\). Its doubled face load is
\[
 z+(2-t)e_c=2e_c+\sum_{f\in\{x,b,y\}}z_f(e_f-e_c).
 \tag{4}
\]
For every CROSS half-row use \(z=2\alpha\), of total one.

These equations have an ordinary capacitated-flow realization. A CROSS triangle is a supply-one node with arcs to its supported face vertices. A selected one-sided row is a zero-supply intermediate node: an arc from \(c\) to this node has capacity one, and its outgoing arcs go to its supported parent-triangle faces. At each ordinary face prescribe net demand
\[
 2-2\,\#\{\text{selected one-sided rows overloaded at that face}\}.
 \tag{5}
\]
Protected vertices and their incident arcs are absent. The total demands equal the CROSS supplies: each selected row contributes total baseline two, and each CROSS coupon contributes two supply-one triangle nodes.

The map between this network and the comparison loads is exact. The intermediate incoming flow is \(t\); its outgoing flows are the \(z_f\). Every original incidence remains separate, including repeated face labels if they occur in the allowed source. Negative quantities in (5) are simply supplies, not negative arc capacities.

Every vertex of this bounded network-flow polytope is integral. One elementary proof is to suppose an extreme feasible flow has a fractional arc. At every incident node its integer divergence forces another fractional arc. Following the fractional subgraph produces an undirected cycle. An alternating perturbation around that cycle preserves all balances and stays within the integer capacity bounds for both sufficiently small signs, contradicting extremality. Hence \(t\in\{0,1\}\) at every vertex.

This fact does **not** reduce the entropy maximum to those vertices. In \(z,t\) coordinates the row objective is
\[
 t\,C\!\left(\frac{z}{2t}\right),
 \tag{6}
\]
which is concave. Its Jensen inequality gives a lower bound at an interior convex combination, not an upper bound by the endpoint values. Indeed even an ordinary CROSS triangle has zero entropy at every simplex vertex and positive entropy inside. Total unimodularity is therefore a feasibility statement, not the required volume comparison.

## 3. Exact stationarity of an interior fractional row

Suppose a feasible comparison maximum has finite common multipliers \(h_f\), and a selected LEFT row has \(0<t<1\). Stationarity within its supported triangle gives its actual weighted maximizing allocation \(\alpha\). Differentiation in \(t\), with \(\alpha\) fixed at that maximizer, gives
\[
 Q(L_x,L_b,L_y)=\frac12\log L_c.
 \tag{7}
\]
The calibrated triangle inequality is
\[
 Q(L_x,L_b,L_y)\ge\frac12\log(L_x+L_b+L_y),
 \tag{8}
\]
strict when at least two of the supported input weights are positive. Consequently
\[
 L_c>L_x+L_b+L_y.
 \tag{9}
\]
in that nonmonomial case. In particular every supported input has smaller curvature than \(c\).

For a one-positive-input row, equality in (8) is possible: (7) then says that the sole supported input and \(c\) have equal curvature. Such rows cannot be silently included in the strict ordering argument below. Likewise a radius infimum escaping to the boundary does not supply finite multipliers. Those cases remain separate.

For a row with \(t=0\), the one-sided maximizing derivative only gives
\[
 Q(L_x,L_b,L_y)\le\frac12\log L_c;
 \tag{10}
\]
it does not give equality. The same strict ordering still follows if at least two supported inputs are positive. These statements use the concave comparison maximization, not stationary equations of the original signed source.

## 4. Completing the deficient row increases entropy but moves face load

Let \(r\) be any probability vector on the supported parent-triangle corners. Complete (3) to two ordinary half-degree triangle rows by putting
\[
 \widehat\alpha=t\alpha+\frac{1-t}{2}r,\qquad
 \widehat\beta=\frac12e_c.
 \tag{11}
\]
Concavity and nonnegativity of \(C\) give
\[
 C(\widehat\alpha)+C(\widehat\beta)\ge tC(\alpha).
 \tag{12}
\]
The exact change of original face load is nevertheless
\[
 \widehat q-q=\frac{1-t}{2}(r-e_c).
 \tag{13}
\]
No original target may be dropped. In particular choosing the parent middle for \(r\) moves the deficiency along the actual middle edge; choosing either outer moves it along the corresponding actual MAIN edge.

Assume a nonempty collection of rows with \(t<1\) satisfies the strict curvature ordering (9), or its version following (10). Keep every other row, including every CROSS row, unchanged. Then no choices of the \(r\)'s can make the sum of (13) vanish.

To prove this, choose an overloaded face of largest curvature among the selected rows with nonzero deficit. It receives a strictly negative contribution from each row overloaded there. It cannot receive a positive contribution from another selected row: such a row would have a still larger overloaded curvature. Thus the total face defect at this face is negative.

This proof permits several rows overloaded at the same face and needs no pre-existing forest description. It is also unaffected by merging equal-curvature monomial components first, provided every selected nonmonomial row remains strictly descending on that quotient.

Accordingly, acyclicity does not itself complete a fractional perspective flow to a feasible ordinary angle flow. It proves the opposite for this rowwise construction: the retained CROSS rows must also change, and their entropy change must be included.

## 5. A two-row example of the repair cost

The defect is visible in the literal local incidence pattern with one protected outer \(x=0\). Let the top comparison row be LEFT on \((0,b,c,y)\), and let the neighboring complete coupon have triangles \((s,c,y)\), \((s,b,y)\). This is the aligned bipyramidal strip incidence; the common \(y\)-face has its actual total target one.

For \(0<w<1/2\), choose \(t=2w\) and the retained top triangle concentrated at \(y\). The top load is
\[
 q_{\mathrm{top}}=(0,0,1-w,w),\qquad
 tC(\alpha)=0.
 \tag{14}
\]
In the bottom coupon put
\[
 \beta=(0,w,\tfrac12-w)\ \text{on }(s,c,y),\qquad
 \gamma=(0,0,\tfrac12)\ \text{on }(s,b,y).
 \tag{15}
\]
The total pair loads are \(q_b=q_s=0\), \(q_c=q_y=1\), and its comparison entropy is \(2f(w)>0\).

Any replacement by two complete coupons preserving these four total loads has entropy zero. Indeed \(s=b=0\) forces both triangles incident to \(b\) to put their half-unit at \(y\); the target \(q_y=1\) is then exhausted. The two triangles incident to \(c\) must each put their half-unit at \(c\). All four triangle rows are vertices.

Thus there is no local entropy-nondecreasing completion of this two-row block with its entire boundary load held fixed. This is an obstruction to a local replacement rule. It is **not** a global counterexample: an exterior may prohibit these boundary loads, or its complete coupled optimum may exceed this local comparison. The existing original-demand cap notes prove cancellation for a different contracted face arrangement. The present arrangement is calculated directly below.

### An exact signed cancellation in this block

The same block admits a finite calculation that does not take any coefficient limit. Set \(N=2m\), \(d=N-1\), \(M=m-1\), and \(\theta=\pi/N\). Retain the top LEFT numerator at \(\sigma=2\), the bottom CROSS numerator at \(\sigma=-2\), and the original common \(y\)-demand \(d\). Specialize the remaining pair boundary variables \(b=s=0\). The actual coefficient is
\[
 [c^dy^d]\,
 H_{V,\mathrm L}(0,0,c,y;2)\,
 H_{V,\mathrm C}(0,c,0,y;-2)
 =(-1)^d\sum_{k=0}^{M}(-1)^kT_k.
 \tag{16}
\]
All unused factors are included. The top coefficient is
\[
 U_k=\csc^2(\theta/2)
 \prod_{r=1}^k
 \frac{\sin^2(r\theta)}{\sin^2((r+\tfrac12)\theta)}.
 \tag{17}
\]
The bottom path runs from \(d\) to \(k\); since its first outer variable is zero it has only one-step moves. Its positive endpoint coefficient is
\[
 B_k=
 \left(\prod_{r=0}^{k-1}4\cos^2((r+\tfrac12)\theta)\right)
 \left(\prod_{r=k+1}^{d}4\sin^2(r\theta)\right).
 \tag{18}
\]
Consequently \(T_k=U_kB_k>0\), and the exact sine product gives
\[
 T_0=\frac{N^2}{\sin^2(\theta/2)},\qquad
 \frac{T_{k+1}}{T_k}
 =\frac{\cos^2((k+\tfrac12)\theta)}
        {\sin^2((k+\tfrac32)\theta)}.
 \tag{19}
\]
Reflection \(k\mapsto m-2-k\) in the ratios replaces each ratio by its reciprocal. Therefore \(T_{M-k}=T_k\). If \(N\) is divisible by four then \(m\) is even and \(M\) is odd, so the terms in (16) cancel in pairs:
\[
 [c^dy^d]\,
 H_{V,\mathrm L}(0,0,c,y;2)\,
 H_{V,\mathrm C}(0,c,0,y;-2)=0,
 \qquad 4\mid N.
 \tag{20}
\]
In contrast, for \(N\ge24\), the first \(\lfloor N/8\rfloor\) ratios in (19) are at least three: their numerator angles are below \(\pi/6\), and their denominator angles are at most \(\pi/6\). Hence
\[
 \sum_{k=0}^{M}T_k
 \ge \frac{N^2}{\sin^2(\theta/2)}\,3^{\lfloor N/8\rfloor}.
 \tag{21}
\]
This is a finite signed-source calculation with the shared \(y\)-target already extracted. The variables \(b,s\) here are boundary variables specialized to zero load; they are not declared to be the two protected faces of a whole diagram. Thus (20)–(21) do not prove a global gap or give a global counterexample. They show that taking absolute values before this smallest shared contraction can lose an exponential cancellation.

The companion [exact cyclic-transfer note](md-undecorated-bipyramid-exact-cyclic-transfer.md), section 4, retains a general top spectral variable and gives the root-safe two-endpoint telescope. It yields a polynomial bound for this boundary specialization at both level parities. No such bound is yet established with all boundary degrees and both spectra free.

## 6. What remains to prove

The universal fixed-sector perspective inequality is still open in this derivation. A successful proof must do at least one of the following while retaining the original source:

* change the surrounding complete rows and bound their total entropy cost;
* contract a larger actual block before taking absolute values, retaining the shared face demands;
* use a quantitative signed phase estimate that exceeds the comparison-flow excess.

The existing anchored and genuine-sector certificate theorems remain valid, and the balanced terminal construction supplies their hypotheses on the decorated diagram. None of the statements here removes the decorations or proves a full invariant estimate on an arbitrary undecorated sphere.

The full invariant still uses its original Cartan character, sine factors, integer Fourier charges and whole first normal. The comparison-flow discussion neither changes those factors nor identifies a comparison tensor with the invariant.
