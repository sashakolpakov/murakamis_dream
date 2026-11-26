# Signed cubic bounds when the reference lies outside the target interval

Research deduction, 6 November 2026. The two-selected terminal
criterion permits a forced-weight target interval that need not contain
the reference. In that situation a scalar optimization can have a
negative maximum. Replacing it by zero loses a valid contribution to
the desired exponential gap. This note gives an exact reduction for
an uncertain reference interval, retaining that sign. It uses no
evaluation of a quantum source or of an analytic primitive.

## 1. The scalar quantity to be bounded

Write
\[
 h(x)=\frac{x^2}{4}-\frac{x^3}{6},\qquad h''(x)=\frac12-x.
 \tag{1}
\]
Fix real intervals \(C=[A,B]\) and \(I=[L,R]\) contained in
\([.18,.5]\), and a constant \(K>0\). There is no containment
requirement between \(C\) and \(I\). The reference coordinate
is \(c\in C\), the physical target is \(x\in I\), and the
real force is \(q\). Define
\[
 \begin{split}
 b(x,c)&=h(x)-h(c)-h'(c)(x-c),\\
 f_q(x,c)&=q(x-c)-K b(x,c),\\
 G(q;C,I)&=\max_{c\in C,\,x\in I} f_q(x,c).
 \end{split}
 \tag{2}
\]
The maximum in (2) is signed: zero is an admissible candidate only
when the chosen intervals actually contain a common coordinate.

The [scalar curvature theorem](research_mixed_terminal_cubic_cost_and_response_bounds.md),
equations (1)--(8), proves that an original scalar cost
\(g_y(x)-g_y(c)-g_y'(c)(x-c)\) is at least \(K b(x,c)\)
when \(K\) is one of its admissible curvature coefficients.
A multiplicity in that cost is incorporated into \(K\).
Consequently (2) bounds the original scalar gain uniformly for every
reference in \(C\). The interval between a reference and a target
remains in \([.18,.5]\), even when the two intervals are disjoint.

## 2. Only two edges of the rectangle are needed

**Theorem 1.** For every real \(q\),
\[
 G(q;C,I)=\max\left\{
       \max_{x\in I} f_q(x,B),\quad
       \max_{c\in C} f_q(R,c)\right\}.
 \tag{3}
\]
Thus uncertain references do not require a parameter subdivision.

*Proof.* Put \(\delta=x-c\). The exact remainder is
\[
 b(x,c)=\frac{(1/2-c)\delta^2}{2}-\frac{\delta^3}{6}.
 \tag{4}
\]
Translate the target and reference by the same nonnegative amount
\(t\), remaining inside their intervals. Since \(\delta\)
does not change,
\[
 f_q(x+t,c+t)=f_q(x,c)+\frac{K\delta^2t}{2}.
 \tag{5}
\]
Given any point of the rectangle, take
\(t=\min\{R-x,B-c\}\). Its translated point lies on the
edge \(x=R\) or the edge \(c=B\), and (5) says that its value
is no smaller. Both edges belong to the original rectangle, which
proves equality in (3). This argument includes degenerate intervals
and \(\delta=0\). \(\square\)

The useful feature of (5) is that the same reference determines both
the displacement and the cubic cost. They have not been independently
enlarged. In particular the proof never inserts a zero displacement
into a disjoint target interval.

## 3. Explicit finite candidate sets

For the first edge in (3), differentiate in \(x\):
\[
 \partial_x f_q(x,B)
   =q-\frac K2\left\{(1/2-B)^2-(1/2-x)^2\right\}.
 \tag{6}
\]
Set \(D_x=(1/2-B)^2-2q/K\). The endpoint values at \(L,R\),
together with the values at
\[
                         x=\frac12\pm\sqrt{D_x}
 \tag{7}
\]
when \(D_x\ge0\) and the candidate lies in \(I\), contain the
maximum. Usually only the minus sign can be interior to \(I\).
Keeping both signs also covers a repeated root at \(x=1/2\).

For the second edge,
\[
 \partial_c f_q(R,c)=-q+K(1/2-c)(R-c).
 \tag{8}
\]
Set \(D_c=(R-1/2)^2+4q/K\). The endpoints \(A,B\), together
with
\[
                  c=\frac{R+1/2\pm\sqrt{D_c}}{2}
 \tag{9}
\]
when real and in \(C\), contain this maximum. If a discriminant
is negative, that edge has no stationary candidate. Equations
(6)--(9) follow by solving two quadratic equations. A cubic on a
compact interval attains its maximum at an endpoint or a stationary
point, so these candidate sets prove (3) without numerical optimization.

For rational data these are real algebraic values involving at most
two square roots per force. Rational square-root enclosures and
interval polynomial evaluation can provide upper bounds. If an
enclosure overlaps an endpoint, one may retain the intersection with
the edge; discarding the candidate is justified only when its entire
enclosure misses the edge. Endpoint values must always remain. This
describes how to certify the formula; no new evaluator or numerical
test is run here.

## 4. Force intervals and correlated forces

**Corollary 2.** The function \(q\mapsto G(q;C,I)\) is convex.
For \(q\in[q_-,q_+]\), its exact uniform upper bound is
\[
 \max_{q\in[q_-,q_+]}G(q;C,I)
       =\max\{G(q_-;C,I),G(q_+;C,I)\}.
 \tag{10}
\]

*Proof.* Each function \(f_q(x,c)\) is affine in \(q\).
Taking its supremum over fixed \(x,c\) gives a convex function.
A convex function on an interval is bounded above by the larger
endpoint value; both endpoints are admissible. \(\square\)

More generally let \(u\) range in a finite product of intervals,
and suppose each node force \(q_j(u)\) is affine in each coordinate
of \(u\) separately. Keep fixed center intervals, target intervals
and positive coefficients for all nodes. Then
\[
 \sum_j G_j(q_j(u))
 \le\max_{v\text{ a vertex}}\sum_j G_j(q_j(v)).
 \tag{11}
\]
For each coordinate separately the left side is convex; apply the
one-dimensional endpoint inequality successively. This is the same
shared-force principle as in the
[terminal vertex theorem](research_mixed_terminal_shared_force_vertices.md),
now for signed gains with possibly disjoint target intervals.
Convexity does not require nonnegative function values.

Actual reference coordinates may depend on \(u\). This causes no
problem when their fixed enclosing intervals have already been
proved: each original gain is bounded pointwise by its corresponding
\(G_j\). The replacement can lose correlations between a force and
its center, but never assumes independence of the actual reference.

There is a useful additional inequality when two height changes act
on the same ordinary index. Suppose \(C\cap I\ne\varnothing\).
Convexity of \(h\) gives \(b(x,c)\ge0\); taking a common
coordinate gives \(G(0;C,I)=0\) and \(G(q;C,I)\ge0\).
For opposed forces \(u\le0\le v\), convexity then proves
\[
 G(u+v)\le\max\{G(u),G(v)\}\le G(u)+G(v).
 \tag{11a}
\]
The first inequality holds because \(u+v\in[u,v]\).
More precisely, if \(u+v\ge0\) and \(v>0\),
\(G(u+v)\le (u+v)G(v)/v\); if \(u+v\le0\) and
\(u<0\), then \(G(u+v)\le (u+v)G(u)/u\).
The zero-force cases follow directly.

Thus two opposed forces can be bounded using two copies of the
same scalar gain without splitting its curvature coefficient.
This is an inequality for their combined gain, not a claim that
the original Hessian supplies its curvature twice. It applies to
an ordinary index whose target contains its reference. The
nonnegative step in (11a) must not be used for disjoint forced
intervals, where the gain can be negative.

## 5. An explicit negative bound for a separated forced interval

Suppose \(B<L\), and write \(s=L-B>0\). For all references
and targets, \(\delta=x-c\ge s\) and
\(1/2-c\ge\delta\), because \(x\le1/2\). Equation (4)
therefore gives
\[
                         b(x,c)\ge\delta^3/3.
 \tag{12}
\]
For any force bound \(q\le\bar q\) such that
\(\bar q<Ks^2/3\), it follows that
\[
 \begin{split}
 f_q(x,c)&\le\delta(\bar q-K\delta^2/3)\\
 &\le s(\bar q-Ks^2/3)<0,\\
 G(q;C,I)&\le s(\bar q-Ks^2/3).
 \end{split}
 \tag{13}
\]
For the second inequality, both factors have the stated order:
\(\delta\ge s>0\) and
\(\bar q-K\delta^2/3\le\bar q-Ks^2/3<0\).
This proves a strictly negative contribution without any root
enclosure. It is sufficient rather than necessary; the exact
two-edge formula can be sharper when (13) is unavailable.

## 6. Application and remaining premise

In the [two-selected terminal window](research_mixed_terminal_two_selected_window.md),
the factorial target is \(P=[.22,.45]\). The simultaneous branch
decomposition also permits \([.4,.45]\) for each forced node.
Use (3) for each of the five main costs, or four fixed-transform
costs, with precisely the coefficients and original reference
intervals proved there. Use (11) only after the common force
parameters and their intervals have been justified.

This provides a replacement for the old executable majorant, whose
reference interval must lie inside its target interval. It preserves
a negative forced-node contribution whenever it is proved. The old
nonnegative majorant remains valid on its stated domain and its
saved records are unchanged.

No new terminal sign follows merely from (3) or (13). Uniform bounds
for the actual trial values and correlated forces are still required,
as are all original source-domain and contour hypotheses. In
particular the uniform signs required by the two-selected finite-source
criterion and the short-partial-filling theorem remain to be established.
