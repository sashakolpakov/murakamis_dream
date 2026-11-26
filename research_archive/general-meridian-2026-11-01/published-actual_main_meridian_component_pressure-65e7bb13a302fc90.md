# Positive boundary pressures for Conway product trees

A Conway tangle is built by stacking ordered two-string tangles and
applying quarter-turns. Group consecutive products that have no turn
between them into a single product junction. A connected region with
no crossing-circle operator is then a tree of product junctions;
its internal edges are the physical quarter-turns. This note studies
the positive action obtained from the complete Newton contraction of
such a region. The underlying ordered constructions and their strict
angle domains are defined in the [strict-tree theorem](actual_conway_all_strict_tree_long_twist_volume.md).

The results compare entire coupled boundary pressures. Deleting a
turn and fusing its two product junctions cannot increase the complete
positive maximum. Several prescribed high boundary labels can also
be moved simultaneously to one half without decreasing the pressure
which bounds them. An exact half-label identity then reassembles
whole junctions with several high incidences. These comparisons are
used by the [general component estimate](actual_main_meridian_general_component_comparison.md)
and the [Fourier reflection bound](actual_main_meridian_high_fourier_reflection.md).

The comparison trees need not define the same link as the starting
diagram. Their positive maxima are bounded by the starting action.
The marked representation, filling curves and final knot-complement
volume remain those of the starting construction.

## 1. Complete actions, boundary variables and product junctions

Put
\[
\begin{aligned}
 J(u)&=\int_0^u\log(2\sin\pi t)\,dt,\qquad 0\le u\le1,\\
 g(a)&=J(2a)-4J(a),\qquad 0\le a\le\tfrac{1}{2},\\
 m(x,y,b)&=J(x+y)+J(b)-J(x)-J(y)\\
 &\quad-J(b-x)-J(b-y)-J(x+y-b).
\end{aligned}
\tag{1}
\]
The closed domain of a retained multiplication gate is
\[
             \max(x,y)\le b\le x+y\le1.
\tag{2}
\]
Its strict domain has all three inequalities strict. A rigid ordinary
boundary branch has profile \(g(a)+c\); its fixed constant \(c\)
includes any action already accumulated inside that branch. We keep
all such constants throughout.

A **covariant label** at a junction means the label inserted into its
complete trace tensor. If that incidence is used as the ordinary
output of a rooted product, the output is its complement. Thus a
cubic junction has the symmetric action
\[
\begin{split}
 t(x,y,z)&=m(x,y,1-z)\\
 &=J(x+y)+J(x+z)+J(y+z)-J(x)-J(y)-J(z)
                                      -J(x+y+z-1).
\end{split}
\tag{3}
\]
The symmetry follows from \(J(1-u)=-J(u)\). A physical quarter-turn
edge identifies equal covariant labels at its two ends. An unturned
edge inside a binary product resolution identifies complementary
covariant labels. In ordinary rooted coordinates the latter simply
passes a child output into the parent input.

Consider a fixed finite connected tree \(\mathcal G\) of actual
product junctions, each of full valence \(D_v\ge3\), counting its
boundary attachments. All internal edges of \(\mathcal G\) are
physical quarter-turns. At every external incidence place an ordinary
profile \(g+c_j\), except when a boundary label is explicitly fixed.
Choose one original ordered binary resolution of each junction and
retain all its hidden variables. The complete action is the sum of
its gate actions and boundary profiles, on the resulting compact
angle polytope. Its maximum, when all ordinary boundaries are free,
is denoted by \(F(\mathcal G)\).

For a whole junction with prescribed covariant labels
\(a_1,\ldots,a_D\), strict support is exactly
\[
         a_i>0,\qquad a_i+a_j<1\quad(i\ne j),
                         \qquad \sum_i a_i>1.
\tag{4}
\]
The closed support uses nonstrict inequalities. The junction action
\(V_D(a_1,\ldots,a_D)\) is the maximum of the complete positive
gate sum in its fixed resolution. It is continuous on that support.
The next section proves the resolution statement needed here.

## 2. Strict resolutions and uniqueness of the positive maximum

### 2.1. A prescribed association has the same strict output interval

For positive input labels \(a_1,\ldots,a_k\), the exact product
interval is
\[
 a_i+a_j<1\quad(i\ne j),\qquad
       \max_i a_i<b<\min\left(1,\sum_i a_i\right).
\tag{5}
\]
These conditions are necessary and sufficient for strict intermediate
gates at output \(b\), in every prescribed binary association. They
are the fixed-label form of the [ordered product lemma](actual_conway_reduced_hub_source_normal_form.md),
Section 2. Here is its constructive proof.

For a child set \(S\), put
\(L_S=\max_{i\in S}a_i\) and
\(U_S=\min(1,\sum_{i\in S}a_i)\). A composite child has available
outputs \((L_S,U_S)\), by induction; a singleton has its fixed
label. At a parent with target \(b\), restrict both child values
below \(b\). Their lower sum is less than one by the pair condition,
and their upper sum exceeds \(b\) by the total condition. Choose
their sum in \((b,1)\). If both are singletons, their fixed sum is
already in that interval. The two inputs are less than \(b\), so
the parent gate is strict. Repeat down the fixed binary tree.

Conversely, each gate output exceeds both inputs and is less than
their sum. The gate at which any two original inputs first meet
also forces their pair sum below one. These observations prove the
necessity in (5). Exposing the last incidence of a whole junction
makes its ordinary output \(b=1-a_D\); (5) then becomes precisely
(4). The closed statement follows either from the same finite
interval rules or by taking limits. No hidden covariant edge is
treated as a physical equal-label edge in this argument.

Assigning \(3/8\) to all physical edges and ordinary boundaries
satisfies (4) at every unmarked hub. It gives a strict witness after
the hidden unturned labels are constructed by (5). If at most one
boundary at each hub is fixed at half, assign \(3/8\) to all other
physical labels. A marked hub then has largest pair sum \(7/8\)
and total at least \(5/4\); an unmarked hub has largest pair sum
\(3/4\) and total at least \(9/8\). The same construction gives a
strict witness. These margins persist when all fixed half labels
are changed slightly and independently.

### 2.2. The maximum is strict, with a negative definite Hessian

The relevant curvature and boundary facts can be seen directly from
the ideal-tetrahedron atoms. For a positive angle triple with sum one,
write
\[
             \mathcal V(a,b,c)=-\pi[J(a)+J(b)+J(c)].
\tag{6}
\]
Its Hessian is negative definite on the two-dimensional angle plane.
Indeed in coordinates \((a,b)\), minus that Hessian has positive
diagonal entries proportional to
\(\cot\pi a+\cot\pi c\) and
\(\cot\pi b+\cot\pi c\), and positive determinant because
\(\cot\pi a\cot\pi b+\cot\pi b\cot\pi c+
\cot\pi c\cot\pi a=1\).

For a strict gate put
\(p=b-x\), \(q=b-y\), \(r=x+y-b\), and \(w=1-x-y\).
Then the exact three-atom identity is
\[
 \pi m(x,y,b)=\mathcal V(y,x,w)
       +\mathcal V(p,q,2r+w)
       +\mathcal V(p+q,r,r+w).
\tag{7}
\]
All three triples are positive. Zero quadratic form in the first
atom forces \(dx=dy=0\); the second then forces \(db=0\).
The third contributes a nonpositive quadratic form. Thus every
strict gate has a negative definite Hessian in all three labels,
including labels above half. Also
\(g'(a)=2\log\cot\pi a\), so \(g''(a)<0\) for
\(0<a<1/2\).

At a nonvertex-flat atom \((0,a,1-a)\), \(0<a<1\), a segment
into the positive simplex has volume derivative \(+\infty\).
This follows from \(J(tu)=tu\log t+O(t)\). At a vertex-flat
atom the \(t\log t\) terms cancel; positive atoms have finite
derivatives. No negative infinite term can cancel the barrier.

Root the resolved tree at any retained output, or at a prescribed
half boundary if one is present. Output zero forces both product
inputs to zero. Output one either has two interior children summing
to one, giving a nonvertex-flat atom, or lets this endpoint descent
continue through a child. A physical turn exchanges zero and one;
an artificial unturned edge preserves the ordinary endpoint. The
descent follows child edges in a finite tree. It cannot end at an
interior prescribed output or a fixed half terminal. It reaches an
ordinary leaf endpoint, where the inward derivative of \(g\) is
infinite, or an interior pair summing to one. Thus no maximizing
state can have an endpoint wire. With all wires interior, any
remaining equality in (2) supplies a nonvertex-flat atom in (7).
The maximum is strict.

Every free coordinate appears in a retained gate or in an ordinary
leaf term. Summing their Hessians therefore gives a negative definite
quadratic form on the actual independent wire variables. This proves
uniqueness. The same argument includes varying prescribed boundary
labels, since each appears at a gate. The implicit-function theorem
and the negative Schur complement then give an analytic, strictly
concave optimized boundary pressure near a strict constrained state.
Compactness makes this branch the constrained global maximum in a
small boundary neighborhood.

Rooted unturned subtrees used below have strict ordinary output
interval \((0,1)\). To check the induction, a rigid leaf has interval
\((0,1/2)\), a turn preserves the full interval of a composite
subtree, and a product of two leaf or composite inputs can realize
every \(0<b<1\) by choosing inputs less than \(b\), with sum
between \(b\) and one. Formula (5) then resolves all further
products. The boundary argument above applies with that output
fixed. These facts supply the strict analytic profiles used next.

## 3. Response equations and the reflection of one output

Let \(f(b)\) be a strict optimized ordinary-output profile. Define
\[
 B=\cot\pi b,\qquad \kappa=e^{-f'(b)},\qquad
 X^2=\frac{1+B^2}{1+\kappa},\qquad Y^2=\kappa X^2.
\tag{8}
\]
Thus \(X,Y>0\) and \(X^2+Y^2-B^2=1\). A rigid leaf has
\((B,X,Y)=(B,B,1)\). We call a composite response proper when
\(-Y<B<X\).

At a stationary product wire, differentiation of (1) and the sine
difference identities give a common positive \(X\) for both inputs
and the output, with
\[
 B_o=\frac{B_1B_2+X^2-1}{B_1+B_2},\qquad
 Y_o=\frac{Y_1Y_2}{B_1+B_2},\qquad B_1+B_2>0.
\tag{9}
\]
For example the input derivative is
\(m_x=J'(x+y)-J'(x)+J'(b-x)-J'(x+y-b)\);
stationarity says \(\kappa_x=e^{m_x}\). Substitution in (8)
gives (9) and its output derivative. These are the same response
equations as in the [intrinsic probe calculation](actual_conway_unflagged_probe_geometry.md),
Appendix A.

Inputs with \(-Y_i<B_i\le X\) produce a proper product output.
For \(X\ge1\), the quadratic relation and the lower bound force
\(B_i>0\), and
\[
 B_o-X=\frac{(X-B_1)(X-B_2)-1}{B_1+B_2}<0.
\tag{10}
\]
For a rigid input one factor is zero; otherwise it is less than
\(X-\sqrt{X^2-1}\le1\). Also \(B_o>0>-Y_o\).
For \(X<1\), put \(h=\sqrt{1-X^2}\) and write
\(B_i=h\cot\alpha_i\), \(Y_i=h\csc\alpha_i\).
Then \(\alpha_i\ge\arccos X\) and the positive denominator in
(9) gives \(\alpha_1+\alpha_2<\pi\). The output has that sum
as its angle, so it is proper. An artificial unturned edge passes
this response directly. A physical turn sends it to
\((-B,Y,X)\), which is again proper. In the present bare trees a
turned child is always composite; no turn of a rigid leaf is
inserted into this induction.

At the last binary gate of an unturned product, strict support gives
\(B<B_i\le X\). Rearranging (9) yields
\[
 Y^2=(B_1-B)(B_2-B)\le(X-B)^2,
 \qquad X\ge X_2(B):=\frac{B+\sqrt{B^2+2}}2.
\tag{11}
\]
The unsquared factors are positive. Since
\(x\mapsto\log[x^2/(1+B^2-x^2)]\) is strictly increasing,
\[
 f'(b)\ge f_2'(b)=2\log(2X_2(B)^2),
\tag{12}
\]
where \(f_2\) is the genuine two-rigid-leaf product profile without
the additive constants. If either input at the last gate is proper,
all these derivative inequalities are strict.

The identity \(X_2(B)X_2(-B)=1/2\) gives
\(f_2'(1-b)=-f_2'(b)\), and hence
\(f_2(b)=f_2(1-b)\). Integrating (12) proves
\[
             f(b)\ge f(1-b),\qquad 1/2\le b\le1.
\tag{13}
\]
For a rooted bare tree this inequality is strict above half unless
the whole rooted side is one trivalent hub with two rigid external
leaves. Indeed a higher-valence root has a composite child in its
last binary gate, and a branch through another hub is a proper
turned composite child. The exceptional profile is exactly
\(f_2+c\). In the nonexceptional case
\(f'(b)+f'(1-b)>0\), so the strict reflection difference persists
at \(b=1\) by continuity. At half, (12) gives \(f'(1/2)\ge0\),
strictly in the same nonexceptional case.

## 4. Complete physical edge labels are at most half

Cut a physical edge of \(\mathcal G\) and root each side there.
Each side is an unturned product with at least two inputs of the
kind just considered: rigid leaves or physical turns of composite
products. Denote the two complete profiles by \(f_A,f_B\).
If \(z\) is the equal covariant label on the physical edge, its
two ordinary outputs are both \(1-z\). The exact cut pressure is
\[
                       f_A(1-z)+f_B(1-z).
\tag{14}
\]
For \(z>1/2\), both derivatives \(f_A'(1-z),f_B'(1-z)\) are
positive by (12); (14) therefore decreases strictly. At half its
derivative is strictly negative unless both rooted sides are the
exceptional two-leaf product. Thus the complete maximizing label
satisfies
\[
                  0<z_e\le1/2
                 \quad\text{on every physical internal edge}.
\tag{15}
\]
Equality is possible exactly when the entire component is two
trivalent hubs, each with two rigid external leaves. In that case
(14) is \(2f_2(1-z)+c\), whose unique maximum is at half.

Apply this cut argument to each edge of the same original optimizer.
It does not replace neighboring subtrees by independently capped
maxima. In every other fixed tree, all physical internal labels and
all ordinary leaf labels have a compact window inside \((0,1/2)\).
Hidden unturned-resolution labels retain their strict bulk window
inside \((0,1)\) and need not be below half. The exceptional
two-hub internal label can be continued through half within that
bulk window.

## 5. Exact ordered fusion and deletion of any set of turns

Set \(d=N-1\),
\(c_j=2\cos((2j+1)\pi/N)\),
\(S_r=\prod_{j=1}^r2\sin(\pi j/N)\), and
\[
 e_r(v)=S_r^{-2}\prod_{j<r}(c_j-v),\qquad
 P_0(v)=\mathcal T_N(v)+2,
 \quad \mathcal T_N(u+u^{-1})=u^N+u^{-N}.
\tag{16}
\]
The complete functional is
\(\phi_0(F)=(-1)^dN^2[v^d]\operatorname{rem}_{P_0}F\).
Its full Frobenius metric and turn are
\[
        \phi_0(e_i e_j)=\delta_{i+j,d},\qquad T_0(e_i)=e_{d-i}.
\tag{17}
\]
The repeated-node first normals are part of this algebra. Since
\(e_{d-i}\) is the dual basis to \(e_i\),
\[
 \sum_{i=0}^d\phi_0(Ae_i)\phi_0(e_{d-i}B)=\phi_0(AB).
\tag{18}
\]
To prove (18), expand
\(A=\sum_i\phi_0(Ae_i)e_{d-i}\) and apply
\(\phi_0(\,\cdot\,B)\). This is a full algebra identity, not
only an equality of values at distinct eigenvalues.

Reflecting exactly one endpoint of an equal-index physical
connection changes it into the complementary pairing (18). That
pairing fuses two complete product junctions. The induced order is
read along the boundary of a small ribbon neighborhood of the two
vertex disks and their joining band. With a root outside the band,
the child's ordered product is substituted in its original position
in the parent's product. No attached branches are permuted. The
order after several fusions is the boundary order of the same
contracted ribbon neighborhood, independently of the sequence of
edge contractions.

If valences \(D_1,D_2\ge3\) fuse, the resulting valence is
\(D_1+D_2-2\ge4\). A connected fused set \(K\) has valence
\(2+\sum_{v\in K}(D_v-2)\). It is again a product tree of the
same class; contraction creates no cycle or duplicate branch.
Its strict witness and unique maximum follow from Section 2.

For one cut, use the actual two rooted profiles from Section 4.
The complete pressures before and after removing the physical turn
are exactly
\[
\begin{split}
 F_T&=\max_{0\le b\le1}[f_A(b)+f_B(b)],\\
 F_I&=\max_{0\le b\le1}[f_A(b)+f_B(1-b)].
\end{split}
\tag{19}
\]
For \(b\ge1/2\), (13) bounds the second summand by the matched
summand at \(b\). For \(b\le1/2\), apply (13) to \(A\) and
use the matched summand at \(1-b\). Therefore \(F_I\le F_T\).
If one side is \(f_2+c\), symmetry gives equality of maxima.
If neither side is symmetric, the comparison is strict away from
half, while at half the matched summand has positive derivative and
is not maximal. Compactness then gives \(F_I<F_T\).

For any subset \(S\) of physical internal edges, let
\(\mathcal G/S\) be the ordered tree obtained by removing those
turns and fusing their unturned connections. Apply (19) successively
to the actual profiles of each current fused tree. Its rigid
boundary profiles and constants have not changed. This proves
\[
                         F(\mathcal G/S)\le F(\mathcal G).
\tag{20}
\]
No matching hypothesis on \(S\) is needed for this pressure
inequality. Restricted complementary-index sums may be enlarged
to the complete positive sum in (18), so (20) also bounds their
rates. The proof does not hold a multi-boundary pressure fixed while
changing its other couplings.

![A trace-difference upper bound reflects one endpoint; the complementary complete pairing then fuses by an exact algebra identity.](../book/figures/main-meridian-reflected-turn-fusion.svg)

The five exterior branches in the fused example are retained in
their induced order. The first arrow is an upper bound and includes
enlarging a restricted positive index sum; the second arrow is (18).
Deleting a turn compares pressures. It does not identify the two
knot complements.

## 6. Several prescribed high boundaries can be clamped together

Now fix \(r\ge1\) marked covariant boundary labels
\(\mathbf z=(z_1,\ldots,z_r)\), with at most one marked incidence
at each actual whole hub. A mark has no leaf action. All other
boundaries retain their ordinary profiles \(g+c_j\). Let
\(\Psi(\mathbf z)\) be the maximum of this same full resolved
action. At \(\mathbf z_0=(1/2,\ldots,1/2)\), Section 2 gives
a unique strict optimizer and an analytic pressure with negative
definite Hessian. With no marks, no boundary comparison is needed.

The partial derivatives at the all-half point satisfy
\[
                       \partial_{z_i}\Psi(\mathbf z_0)\le0.
\tag{21}
\]
To prove this without differentiating a nonexistent terminal
profile, root the same resolved tree at mark \(i\). Its ordinary
output is half. For any other fixed half terminal, use the positive
response \(\kappa=e^{m_x}\) supplied by its incident strict gate.
Its cotangent is \(B=0\), so \(-Y<B<X\) automatically. This
assigns a response, not a new action or an artificial physical leaf.
Equations (9)–(10) now propagate proper responses through both
unturned and turned edges, exactly as before.

At the final binary product strict support makes both inputs less
than half, so \(B_1,B_2>0\). Its output has \(B=0\), and
\[
       Y^2=1-X^2=B_1B_2\le X^2,
       \qquad \partial_{z_i}\Psi
                           =-\log(X^2/Y^2)\le0.
\tag{22}
\]
Changing the root does not change the pressure: the same cubic
action (3) is symmetric, physical edges still identify equal labels,
and hidden unturned edges still identify complements. Thus (22)
proves every component of (21) for the same constrained problem.

The pressure is jointly concave, since convex combinations of full
feasible states are feasible and the action is concave. For every
feasible \(\mathbf z\ge\mathbf z_0\), its supporting plane gives
\[
                        \Psi(\mathbf z)\le\Psi(\mathbf z_0).
\tag{23}
\]
This includes closed endpoints. Explicitly, with
\(\mathbf v=\mathbf z-\mathbf z_0\ge0\), concavity gives
\[
 \Psi(\mathbf z)-\Psi(\mathbf z_0)
 \le\frac{\Psi(\mathbf z_0+t\mathbf v)-\Psi(\mathbf z_0)}t.
\tag{24}
\]
For small \(t>0\), the right side lies on the analytic strict
branch. Its limit is nonpositive by (21). If \(\mathbf v\ne0\),
the negative definite Hessian makes it strictly negative for small
enough \(t\), unless it was already negative at first order.
Thus (23) is strict away from the all-half boundary.

This is a simultaneous comparison. It asserts neither monotonicity
of one coordinate with other marks held above half nor a simultaneous
reflection inequality \(\Psi(\mathbf z)\le\Psi(1-\mathbf z)\).
The turn-deletion theorem supplies the separate coupled reflection
comparison needed for (20).

## 7. The half-label cardinal identity

For odd \(N=2m+1\), the complete relation has double nodes
\(c_0,\ldots,c_{m-1}\) and the simple node \(c_m=-2\).
The polynomial \(e_m^2\) vanishes with both first jets at every
double node. Also \(S_m^2=N\), and
\[
                        e_m(-2)=1,
                        \qquad \phi_0(e_m^2)=1.
\tag{25}
\]
For example \(P_0=(v+2)\prod_{j<m}(c_j-v)^2\);
\(P_0'(-2)=N^2\) gives the positive numerator value \(N\)
in the first identity. The second follows directly from the top
coefficient of the degree-\(d\) polynomial \(e_m^2\).
Thus this square is the full Hermite projector onto the simple node:
\[
 e_m^2 F\equiv F(-2)e_m^2\pmod{P_0},\qquad
                        \phi_0(e_m^2F)=F(-2).
\tag{26}
\]
There is no missing derivative contribution at a double node.

For \(k\ge2\) and low remaining indices,
\[
       \phi_0\left(e_m^k\prod_j e_{n_j}\right)
                           =\prod_j e_{n_j}(-2).
\tag{27}
\]
Uniform closed sine-factorial estimates give
\(N^{-1}\log e_n(-2)=g(n/d)+O(\log N/N)\) on the low range.
The positive ordered resolution identifies the complete tensor
rate with \(V_D\). Its primitive half-label face can be
approximated at odd levels while preserving all the prescribed
equalities. Taking rates in (27), followed by continuity, proves
\[
 \boxed{\quad
 V_D(\underbrace{\tfrac12,\ldots,\tfrac12}_{k\ge2},
                  x_1,\ldots,x_{D-k})
             =\sum_{j=1}^{D-k}g(x_j),
                 \qquad 0\le x_j\le\tfrac12.
 \quad}
\tag{28}
\]
The real complete action is independent of level parity. Odd levels
calibrate (28); the proof does not assert that an even-level simple
node projector exists. Zero low labels and further half labels are
included because the closed action is continuous and
\(g(0)=g(1/2)=0\).

## 8. Reassembling whole junctions with several high incidences

This final comparison is useful when an absolute tensor bound has
the following local action: each low incidence contributes \(g(x)\),
and each high incidence contributes zero. For the moving Newton
tensor this follows from the high basis polynomial's polynomial
full spectral-jet norm, the low norm rate \(g\), and finite-degree
Chebyshev folding. The [source bounds](actual_main_meridian_source_bounds.md),
Section 3.4, retain those full norms and show that trace extraction
costs only a polynomial factor. No same-index moving/complete
comparison is assumed.

Choose a nonempty set of pairwise nonadjacent whole junctions, each
with at least two high incidences. Bound them by the local action
just described. All other junctions must already have their complete
positive tensors or a justified positive majorant at the same
labels. In particular an uncontrolled moving junction with exactly
one high incidence cannot be left in these old regions. Actual
equal-color moving junctions are nonadjacent across physical turns,
but constant junctions need not alternate with them globally.

Remove the selected junctions. A retained complete hub has at most
one strictly high incidence, since its complete pairwise support
forbids two indices whose sum exceeds \(d\). At every high interface
to a removed junction mark its adjoining old-region boundary. Mark
an original external high input as well, retaining its constant
\(c_j\) and its zero variable cone action. Thus each retained hub
has at most one mark.

At each low arm from a removed junction, place the single profile
\(g(x)\) from its local upper bound on the adjoining old region.
The nonadjacency and the tree condition make this assignment unique.
Keep each ordinary external \(g+c_j\) unchanged. Optimize these
whole old regions and apply (23) jointly to their high marks. Regions
without marks are simply optimized with their ordinary profiles.

Reinsert each removed junction with every high incidence set to half
and with the newly optimized low-arm values. Formula (28) supplies
exactly the sum of the \(g\) profiles already charged on its low
arms. Remove those auxiliary boundary profiles when reinserting
the junction: the same action now comes from that junction itself.
They are consumed once, rather than added again.

For an external low arm, its original \(g(x)+c_j\) remains and
the junction supplies the additional \(g(x)\) already present in
its upper bound. For an external high arm, the variable action was
zero and the replacement leaf has \(g(1/2)=0\). If the entire graph
is one selected junction, this external-arm accounting applies
directly. Zero arms and limiting half labels are covered by (28).

The result is a feasible state of the same complete tree with action
at least the upper action being compared. At least one reinserted
junction has a pair sum equal to one. The finite union of these
closed pair-equality faces misses the original strict optimizer.
Compactness therefore supplies a positive gap
\[
            \mathcal A_{\mathrm{comparison}}
                               \le F(\mathcal G)-\delta,
                             \qquad \delta>0.
\tag{29}
\]
At finite levels normalize these real comparison labels by
\(d=N-1\). The closed support conditions are then exact; switching
between \(n/d\) and \(n/N\) costs only \(O(\log N)\) in the
logarithmic factorial estimates. Polynomially many states and
polynomial tensor factors preserve the strict exponential gap,
at both level parities. The geometric loss can be chosen before a
fixed microscopic parameter radius.

## 9. Combining reflection, fusion and the geometric target

For clarity, the graph facts used when (20) and (29) are combined
are exact. A selected one-high moving difference has one high
physical edge and all other incidences low. Its neighbor is a
constant old vertex, whose nonzero complete tensor has at most one
high incidence. Thus the selected internal edges form a matching.
Reflecting one endpoint and fusing along each such edge leaves only
low exterior incidences on every fused hub. It creates no additional
high mark when the several-high junctions of Section 8 are removed.
Those junctions are never fused and remain pairwise nonadjacent.
The inherited orders, remaining physical turns and all boundary
constants are unchanged.

If a one-high difference instead uses an original external high
index, reflection creates a low index \(r=d-h\). Its actual cone
action was \(c_j\); the complete comparison leaf has
\(g(r/d)+c_j\). The surplus \(g(r/d)\ge0\) is a retained loss,
not a new physical action. At a strict ordinary-leaf optimizer it
is positive; its endpoint cases are controlled by the compact
complement of that optimizer. The Fourier companion proves the
local bounds and the additional strict loss when an internal
deletion has equal pressure.

All of these constructions end with a pressure at most the complete
positive action \(F_0\) of the starting strict tree. The original
complete geometry identifies \(2\pi F_0\) with its augmented volume. The
subsequent wire packet, joint filling saddle, primitive equations
and scalar ledger continue to use the starting tree, including every
physical edge; the comparison fusions are not inserted into that
packet. In the [filled-volume theorem](actual_main_meridian_filled_volume.md)
the actual equation remains \(U_i+p_iV_i=-2\pi i\), with physical
power \(n_i=\epsilon_i-2p_i\). Only auxiliary circle cusps are
filled. The volume on the right is the knot complement of that
original filled diagram, whose main cusp remains unfilled.
