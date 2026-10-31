# Fractional one-sided sectors: the forest and the missing reduction

31 October 2026. **Open research interface.** The structural lemmas below
concern the convex weighted comparison for one fixed actual LEFT/CROSS/RIGHT
pattern. They do not prove its universal capacity bound. The comparison
perspective is distinct from the original Green coefficient entropy.

The [finite-sector cover theorem](general_actual_sector_cover_filling_volume.md)
explains the desired implication for the original invariant. The
[certificate separation](actual_shared_radius_certificate_separation.md)
shows why unrestricted spectator mixtures cannot be assumed harmless.

## 1. Exact network and perspective

Use the original simple-white plat, ordinary demands one and protected
demands zero. At a LEFT port put \(p=b,o=c\); at a RIGHT port put
\(p=c,o=b\). The two outer faces are \(x,y\). Its exact comparison flow is

$$
q_o=1-\frac{t}{2},\qquad(q_x,q_p,q_y)=t\alpha,\qquad
0\le t\le1,\quad\alpha\ge0,\quad\sum\alpha=\frac{1}{2},
\qquad h_{\mathrm{env}}=tC(\alpha).\tag{1}
$$

Here \(C\) is the original half-degree triangle entropy. CROSS retains its
two separate half-supply triangle rows. Equation (1) is equivalently a
supply-one node on the four original faces whose arc to \(o\) has lower
bound \(1/2\). Thus the fixed-sector feasible polytope is an ordinary
bounded bipartite flow polytope, with protected arcs removed.

Scaling by two makes its supplies, demands and lower bounds integral.
The incidence matrix is totally unimodular, so all vertices are
half-integral before scaling. Every one-sided vertex has \(t=0\) or
\(t=1\). In particular the polytope is the convex hull of the feasible
pure-atom patterns. This is a statement about flow vertices, **not**
maximizers of a concave entropy. Concavity has the wrong direction for
an atomwise maximization argument.

## 2. The strict-overload middle graph is an actual rooted forest

Select the ports with \(t<1\), orient their original middle edges
\(p\to o\), and retain their endpoints. Each selected child has
\(q_o>1/2\). Two such edges therefore cannot enter one ordinary face,
and none can enter a protected face.

In the [literal gap presentation](actual_simultaneous_small_circle_face_correspondence.md),
middle edges in an odd gap form a path. Those in an even gap form a cycle
based at the protected exterior \(u\). Different gap paths meet only at
\(u\). An undirected selected cycle would be one of these exterior cycles.
Since its edges each have one head and every indegree is at most one,
every cycle vertex would have indegree one, including \(u\), a
contradiction. Hence every selected component is a tree.

Its indegrees sum to one less than its vertex count, so it has exactly
one root and all arrows point away from that root. If it contains a
protected face, that face is the root. Gap parity makes a component
monochromatic, so it contains at most one protected face and its outer
\(x,y\) faces lie outside the component.

For a component \(T\) with \(\kappa\in\{0,1\}\) protected roots, define

$$
\ell_e=t_e(\alpha_{x,e}+\alpha_{y,e}).
$$

The selected edges contribute \(|E(T)|-\sum_e\ell_e\) to its vertices.
Their total demand is \(|V(T)|-\kappa\). Therefore all remaining
original rows contribute exactly

$$
1-\kappa+\sum_{e\in E(T)}\ell_e.\tag{2}
$$

A pure identity contraction would leave target \(1-\kappa\). The extra
term in (2) is the outer-load compensation required by a fractional leaf
elimination. It cannot be omitted or absorbed into a protected zero target.

## 3. Finite positive KKT equations

Assume a relative-interior maximizer has finite positive ordinary dual
weights \(L_f\). Protected coordinates remain zero. Each active retained
triangle is the unique maximizer \(\alpha(L)\) in the original triangle
Fenchel formula. A genuinely fractional row satisfies

$$
Q(L_x,L_p,L_y)=\frac{1}{2}\log L_o,
\qquad 0<t<1.\tag{3}
$$

The [triangle entropy inequality](actual_triangle_entropy_algebraic_balance.md)
then gives

$$
L_o=\exp\bigl(2Q(L_x,L_p,L_y)\bigr)
       \ge L_x+L_p+L_y.\tag{4}
$$

This is strict when at least two input weights are positive. Thus every
nonzero input curvature is strictly below the overloaded curvature, except
for a monomial retained triangle. Such a triangle has one positive input
face \(f\), zero entropy and \(L_o=L_f\). It can occur only in an original
triangle containing both protected vertices.

The endpoint inequalities have different directions:

$$
\begin{array}{ll}
t=0:&L_o\ge\exp(2Q_{\mathrm{input}}),\\
t=1:&L_o\le\exp(2Q_{\mathrm{input}}).
\end{array}\tag{5}
$$

Consequently a maximal-curvature fractional overload cannot be an input
of another nonmonomial fractional row. It can nevertheless meet CROSS
rows and terminal \(t=1\) fixed-triangle rows: (5) does not give an
ascending-curvature conclusion for those terminal rows. Pure \(t=0\)
rows carry no retained-triangle load. A claim that such a sink has only
CROSS neighbors needs an additional argument.

## 4. The exact condition for lossless elimination

Strict concavity of \(C\) gives an equality criterion for its perspective.
Between two states of positive mass, equality in concavity of
\(tC(\alpha)\) holds precisely when their normalized \(\alpha\)'s agree.
For CROSS, both triangle allocations must agree. Along an affine path in
the mass and weighted-allocation variables, its second variation is

$$
\mathrm d^2[tC(\alpha)]
  =t\,(\mathrm d\alpha)^T D^2C(\alpha)(\mathrm d\alpha).\tag{6}
$$

It is strictly negative when an allowed normalized allocation changes.
A monomial allowed triangle has no normalized variable. The same equality
criterion extends to a mass-zero endpoint by continuity.

At a constrained maximizer, another feasible point of equal or greater
entropy must therefore keep every positive-mass normalized triangle
allocation fixed along their connecting segment. If all endpoint masses
\(t=0,1\) are also kept fixed, the changes \(h_e=\mathrm dt_e\) at
fractional rows must solve the exact original face system

$$
\sum_e h_eD_e=0,\qquad
D_e=\alpha_{x,e}e_x+\alpha_{p,e}e_p+\alpha_{y,e}e_y
                         -\frac{1}{2}e_o.\tag{7}
$$

Thus an angle-changing CROSS compensation incurs a strict entropy cost
at this maximizer. This does not compare the maximizer's value with
\(\Phi_D\); it identifies the condition a lossless same-sector argument
would have to satisfy.

The columns in (7) are usually independent. Their overloaded children are
distinct. Restrict to those face rows and order by \(L_o\). A nonmonomial
fractional column has diagonal entry \(-1/2\), while every off-diagonal
positive entry lies at a strictly smaller curvature. Without monomial
dependency cycles, triangular elimination gives full column rank.

More generally the kernel can only come from directed cycles of monomial
fractional rows with equal curvature. Indeed, interpret \(2\alpha\) as
an input probability vector and reverse the arrows from child to inputs.
Each nonmonomial step strictly decreases curvature; a monomial step
preserves it and has a single successor. A recurrent class of the
restricted substochastic matrix is therefore a deterministic equal-curvature
cycle. Equivalently, eliminate the strict curvature blocks; the remaining
equal-level blocks are deterministic partial transition matrices: several
columns may enter one face. Pruning their transient trees leaves exactly
the recurrent directed cycles. A cycle has zero
entropy and allows a constant mass circulation until one mass reaches
zero or one. After these harmless cycles are removed, (7) is injective.

The rooted middle forest and KKT order therefore do not, by themselves,
provide a lossless leaf reduction. Half-integrality of the flow vertices
does not repair this issue.

## 5. The remaining sufficient lemma

For a fixed sector write \(P_s\) for its original incidence-flow polytope
and \(H_s\) for the sum of its perspectives and triangle entropies. The
universal comparison sought is

$$
\max_{q\in P_s}H_s(q)<\Phi_D
\quad\text{for every nonempty one-sided pattern }s.\tag{8}
$$

The existing pure-pattern, identity and
[fixed-triangle boundary theorems](actual_fixed_triangle_boundary_capacity_gap.md)
control atom patterns. The original endpoint Green theorem does not
control the intervening perspective pointwise.

A sufficient new step would map a fractional maximizer into the original
complete or source-permitted smoothed flow spaces while comparing **total**
entropy and preserving the original face demands. Equation (2) requires
transport between actual opposite-parity outer components. Equations
(6)--(7) show why this cannot simply be declared a feasible lossless motion
inside the same strict sector. A direct quantitative upper inequality could
also suffice, provided it retains the fractional masses and shared targets.

The network, forest and leakage statements hold on the whole closed
polytope. The KKT and curvature claims assume the stated finite positive
multipliers; their existence is not asserted. This research note proves no
new group representation, relative fundamental class, universal sector
bound, or original-invariant asymptotic.

## Review scope

An independent peer reviewed the complete structural derivation, including
the bounded-flow network, exact gap forest and leakage, endpoint KKT
inequalities, strict perspective equality and mass-matrix kernel. The final
wording distinguishes deterministic transition blocks from permutation
blocks; transient monomial trees are pruned before identifying recurrent
cycles. This review does not supply the open inequality (8).
