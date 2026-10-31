# Fractional rows and the obstruction to entropy-preserving covers

31 October 2026. **Open research interface.** The lemmas below concern the
convex weighted LEFT/CROSS/RIGHT comparison on the original marked source.
They disprove an automatic entropy-preserving cover construction. They do
**not** disprove the desired strict fixed-sector capacity bound by complete
volume, or any statement about the original quantum invariant.

The [fractional forest reduction](research_fixed_sector_fractional_forest_reduction.md)
gives the exact flow network and stationary equations. This note isolates
what an unbranched cover would additionally have to achieve. The
[finite-sector cover theorem](general_actual_sector_cover_filling_volume.md)
uses “cover” in a different sense: a finite cover of label patterns by valid
shared-radius estimates, not a topological covering space.

## 1. Projected flows and their entropy

Every original ordinary face has demand one; the two protected faces have
demand zero. CROSS retains its two original triangle rows, each with supply
one half. For a triangle allocation \(a\ge0\), \(\sum a=1/2\), the exact
entropy is

$$
C(a)=\sum_j f(a_j),\qquad
f(s)=\frac{\Lambda(\pi s)+\Lambda(\pi/2-\pi s)}{\pi},
\qquad f''(s)=-\frac{2\pi}{\sin(2\pi s)}\le-2\pi.\tag{1}
$$

Consequently, including closed boundary allocations by continuity,

$$
C(\overline a)-\overline{C(a)}
   \ge \pi\,\overline{\|a-\overline a\|^2}.\tag{2}
$$

This is the normalization of the [fixed-triangle capacity lemma](actual_fixed_triangle_boundary_capacity_gap.md).
At a selected LEFT or RIGHT port let \(o\) be the overloaded ordinary
middle, \(p\) the opposite middle, and \(x,y\) the original outer faces.
The fractional comparison row is

$$
q_o=1-\frac{t}{2},\qquad(q_x,q_p,q_y)=t\alpha,
\qquad0\le t\le1,\quad\sum\alpha=\frac{1}{2},
\qquad h_{\mathrm{env}}=tC(\alpha).\tag{3}
$$

At \(t=0\) this is the pure identity endpoint \(e_o\). At \(t=1\) it is
one retained triangle \(\alpha\) and the pure-middle half triangle
\(e_o/2\). All protected incidences remain zero; the four original faces
are distinct, so \(o\notin\{x,p,y\}\).

For a rational feasible flow choose \(q\) with all \(qt_e\) integral.
Clearing denominators specifies \(qt_e\) retained half-triangle atoms and
\(q(1-t_e)\) identity atoms at each selected port. It does not specify a
cover with closed face stars.

## 2. A necessary cover-realization condition

Allow \(q\) lifts of every face and \(q\) copies of every original coupon
and triangle incidence. At each lifted face require exactly one copy of
each original incident corner. Copies may be assigned to lifts by arbitrary
permutations: no common sheet labeling or trivial monodromy is assumed.
An actual unbranched source cover must also retain the cyclic order, but we
do not impose that additional restriction here.

Require the following conditions:

- Each ordinary lifted face has total load one; every protected lift has
  load zero.
- Every CROSS triangle copy and every retained triangle copy has supply
  one half.
- The mean allocation of a CROSS row is its prescribed \(a_r\). Among
  the \(qt_e\) retained copies of a selected row, the mean is its
  prescribed normalized allocation \(\alpha_e\).
- The two atom counts at every selected port are the prescribed counts
  above.

These are necessary for an unbranched original-source cover representing
the given projected flow. We permit more incidence permutations than a
genuine geometric cover; a failure here cannot be repaired solely by
choosing different source monodromy.

Let \(H\) be the fractional entropy and \(H_{\mathrm{cov}}\) the sum of the
triangle entropies on such a realization. Equation (2) gives

$$
\begin{aligned}
qH-H_{\mathrm{cov}}\ \ge{}&
\pi\sum_{r\ \mathrm{CROSS}}\sum_{s=1}^q
       \|a_{r,s}-a_r\|^2\\
&+\pi\sum_e\sum_{s\ \mathrm{retained}}
       \|\alpha_{e,s}-\alpha_e\|^2.
\end{aligned}\tag{4}
$$

Therefore entropy preservation—or the entropy increase needed to deduce
\(H\le\operatorname{Vol}/q\) from a cover-volume bound—requires every
positive-mass triangle allocation to be identical on all its copies.
Varying angles across sheets cannot increase entropy while preserving the
projected flow.

The original bounded bipartite flow becomes integral after scaling by two,
so it can be decomposed into feasible pure-atom flows. This does not supply
the desired entropy comparison: (4) has the opposite direction. Such a
decomposition can strictly lose entropy.

## 3. Quantitative obstruction at a fractional sink

Suppose a port \(e\) has \(0<t_e<1\), overloaded face \(o\), and no other
fractional row uses \(o\) as a retained-triangle input. Distinct strict
overloads have distinct children, because each contributes more than one
half to a demand-one face. All other load at \(o\) therefore comes from
CROSS triangles or retained triangles of terminal \(t=1\) rows. Let \(M\)
be their number of corner incidences at \(o\). Feasibility forces \(M>0\).

The prescribed mean of these corners sums to \(t_e/2\). At a lift whose
selected atom has state \(s\in\{0,1\}\), exact face closure requires
their sum to be \(s/2\). Their total deviation from their projected values
is \((s-t_e)/2\). Cauchy–Schwarz on these \(M\) corners and (4) yield

$$
\begin{aligned}
qH-H_{\mathrm{cov}}
&\ge\frac{\pi}{M}\sum_{\text{lifts of }o}
                 \left(\frac{s-t_e}{2}\right)^2\\
&=q\,\frac{\pi t_e(1-t_e)}{4M}>0.
\end{aligned}\tag{5}
$$

There are exactly \(qt_e\) state-one copies. The estimate uses only each
lifted star, and permits arbitrary permutations between different face
lifts. Its loss per sheet is independent of \(q\); even asymptotically
lossless atomization is unavailable under these hypotheses.

In particular this applies to a single fractional row. More generally,
draw a dependency arrow from a fractional child used as an input to the
child of the row using it. An acyclic dependency graph has a sink to which
(5) applies.

At a finite positive stationary point, the [exact KKT equations](research_fixed_sector_fractional_forest_reduction.md)
give, for every genuinely fractional row,

$$
L_o=\exp\bigl(2Q(L_x,L_p,L_y)\bigr)
       \ge L_x+L_p+L_y.\tag{6}
$$

The inequality is strict when the input has at least two positive weights.
Nonmonomial dependency arrows strictly increase curvature. If there are
no equal-curvature monomial cycles, the fractional dependency graph is
acyclic and (5) applies. Terminal \(t=1\) rows need not obey this ordering;
their triangle corners are already included among the \(M\) corners.

This does not assert that a global sector maximizer is fractional or has
value above complete volume. It shows that a fractional stationary point's
forest and curvature order do not supply the proposed lossless cover.

## 4. An exact original five-port flow

Use the literal width-three word, in the original compiler's zero-based
slots,

$$
[1,3,2,1,3],\qquad\text{marked top cap }0.
$$

The protected faces are \(\{0,1\}\), the ordinary faces are
\(\{2,3,4,5,6\}\), and the original quartets are

$$
\begin{array}{c|c}
0&(1,0,4,2)\\
1&(2,0,5,3)\\
2&(4,2,6,5)\\
3&(1,4,0,6)\\
4&(6,5,0,3)
\end{array}\tag{7}
$$

The ten triangle rows are distinct, all fifteen edges occur twice, and the
seven vertices form the original simple-white sphere. This is the exact
reduced width-three source in the [shared-radius theorem](general_anchored_shared_radius_filling_volume.md),
not an abstract graph requiring a new plat adapter.

Set only port 3 to RIGHT, with the other four CROSS. For
\(0\le\beta\le1/2\), take \(t_3=2\beta\) and
\(\alpha_3=e_6/2\). Its loads and entropy are

$$
q_4=1-\beta,\qquad q_6=\beta,\qquad h_3=0.\tag{8}
$$

The two CROSS rows of a port are its original \((x,b,y)\) and
\((x,c,y)\), in that order. Their nonzero face loads are

$$
\begin{array}{c|c|c}
\text{port}&\text{first row}&\text{second row}\\ \hline
0&\{2:\tfrac12\}&\{4:\beta,\ 2:\tfrac12-\beta\}\\
1&\{2:\beta,\ 3:\tfrac12-\beta\}&\{3:\tfrac12\}\\
2&\{5:\tfrac12\}&\{6:\tfrac12\}\\
4&\{5:\tfrac12\}&\{6:\tfrac12-\beta,\ 3:\beta\}
\end{array}\tag{9}
$$

Every row has supply one half and is supported on its original triangle.
Equations (8)–(9) give load exactly one at each ordinary face and zero at
both protected faces. Thus the full shared constraints hold. The entropy is

$$
H(\beta)=3C(\beta,\tfrac12-\beta,0).\tag{10}
$$

It is strictly concave, vanishes at both endpoints, and has a unique maximum
on this particular feasible segment at \(\beta=1/4\). There,

$$
t_3=\frac{1}{2},\qquad H(\tfrac14)=\frac{6G}{\pi}>0,\tag{11}
$$

where \(G\) is Catalan's constant. This segment is not asserted to contain
the full fixed-sector maximizer.

At face 4 the other three incidences are the face-4 corners of port 0's
second row and both rows of port 2. Their projected loads are \(1/4,0,0\).
Equation (5) gives at least \(\pi/48\) entropy loss per sheet, for every
cover degree and every incidence permutation.

In this sparse example the loss is even stronger: every admissible
pure-atom realization preserving the projected flow has **zero entropy**.
A nonnegative corner with projected mean zero vanishes on every copy.
Thus both port-2 face-4 corners stay zero, and face-4 closure forces port
0's second row to a triangle vertex. Face-2 closure then forces port 1's
first row to a vertex; face-3 closure forces port 4's second row to a vertex.
All other rows were already monomial. This reasoning is local at each
lifted star and does not require global sheet labels.

Atomization is not empty: the \(\beta=0\) and \(\beta=1/2\) flows form
a feasible two-sheet atomization with average \(\beta=1/4\). Their total
entropy is zero, rather than twice (11). Integral decomposition therefore
exists, but loses entropy in exactly the direction that the proposed
cover-volume comparison would need to preserve.

## 5. The remaining general question

The desired universal statement is still

$$
\max_{\text{original fixed-sector flow}} H_{\mathrm{env}}<\Phi_D.
$$

The example has neither a certified fixed-sector capacity excess nor an
original quantum asymptotic excess. It rules out automatic unbranched cover
atomization that preserves the projected flow without entropy loss.
A different construction must change the projected flow and prove a
compensating global entropy inequality, or allow branching and prove an
appropriate new volume comparison. Summed angles \(2\pi q\) alone do
not provide either condition.

The focused exact check used the original Morse compiler and rational
arithmetic: ten triangle incidences, fifteen paired edges, five rational
flows, forty row sums, thirty-five face targets, and the exact two-endpoint
average. The coefficient \(1/48\) is exact. The entropy and covering
inequalities are analytical; these finite checks are not a proof of a
general covering topology or of the open universal sector bound.

Independent full analytical review and exact-source replay: coherent partner, PASS. The review retains the open universal-capacity scope.
