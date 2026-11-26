# How the short-filling theorems reduce the remaining parameter set

Research note, 3 November 2026. This note concerns original integer
filling assignments of one fixed marked template. It does not count
knot types. The finite-exception problem remains open.

The independent-set assembly theorem has a useful consequence that
does not require a uniform threshold over all fixed short powers.
On its stated domain, every still untreated assignment lies in one
of finitely many sets obtained by fixing the powers at two adjacent
vertices. This is stronger than the original long-twist criterion,
whose untreated set includes entire slices with just one fixed power.
The remaining two-coordinate slices are nevertheless infinite when
the template has more than two vertices.

## 1. A finite branching lemma

Let \(G=(V,E)\) be a fixed finite graph with at least one edge. Write
\(d=|V|\). For each vertex \(v\), let \(D_v\subseteq\mathbb Z\) be a
set of allowed values, and let \(D\subseteq\prod_{v\in V}D_v\) be any
domain of complete assignments. A property \(P(\mathbf n)\) is
defined for \(\mathbf n\in D\).

Suppose that whenever \(I\subset V\) is independent and
\(\mathbf a\in\prod_{v\in I}D_v\), there is a finite nonnegative
integer \(B(I,\mathbf a)\) such that
\[
 \mathbf n\in D,\qquad n_v=a_v\ (v\in I),\qquad
 |n_w|>B(I,\mathbf a)\ (w\notin I)
 \quad\Longrightarrow\quad P(\mathbf n).
 \tag{1}
\]
Independence means that no edge of \(G\) has both endpoints in \(I\).
The empty set is allowed in (1). No uniformity in \(I,\mathbf a\)
is assumed.

**Proposition.** There is a finite set
\[
 \mathcal F\subseteq
 \{(uv,a,b):uv\in E,\ a\in D_u,\ b\in D_v\}
 \tag{2}
\]
such that every assignment in \(D\) for which \(P\) fails satisfies
\[
                  n_u=a,\qquad n_v=b
 \tag{3}
\]
for at least one triple in \(\mathcal F\).

**Proof.** Start at the empty partial assignment. At a node
\((I,\mathbf a)\) with \(I\) independent, an assignment for which
\(P\) fails must have a free coordinate \(w\notin I\) satisfying
\[
                  |n_w|\le B(I,\mathbf a).
 \tag{4}
\]
Branch over every such coordinate and every allowed integer value
in the finite interval in (4). Extend the partial assignment by
that coordinate and value. If the extended set remains independent,
repeat the procedure. Otherwise, choose an edge whose endpoints
have just both become fixed, record its two values in \(\mathcal F\),
and end that branch.

The procedure has finite branching and depth at most \(d\), because
one new coordinate is fixed at each step. A branch cannot finish
with every coordinate fixed while its fixed set is independent:
the whole graph has an edge. A node with no allowed short values
contains no failing assignment. Thus every branch followed by a
failing assignment ends at a recorded edge, proving (3).
The whole tree, and hence \(\mathcal F\), is finite. \(\square\)

Let \(C\) be the largest absolute value appearing in \(\mathcal F\),
with \(C=0\) when \(\mathcal F\) is empty. A useful, slightly weaker
form of the conclusion is
\[
 \{v:|n_v|\le C\}\text{ is independent}
       \quad\Longrightarrow\quad P(\mathbf n).
 \tag{5}
\]
The construction of \(C\) uses only finitely many thresholds from
(1). It does not take a supremum over all short fillings.

## 2. Application to the original circle trees

Fix an original marked circle tree and its strand, carrier and
framing conventions. Let \(d_v\) be the original degree of vertex
\(v\), and let \(\eta_v\in\{-1,0,1\}\) be its fixed carrier. The
integer surgery coefficient \(p_v\) and crossing power \(n_v\) obey
\[
                         n_v=\eta_v-2p_v.
 \tag{6}
\]
The parity pattern is fixed before varying any powers. Restrict to
the original assignments that give hyperbolic knots.

For each \(v\), choose \(D_v\) among the powers for which the
[isolated-vertex theorem](research_isolated_vertex_coverage_and_assembly.md)
has been proved, retaining the parity in (6). Its independent-set
assembly gives precisely (1), with \(P\) the original Kashaev volume
identity through all sufficiently large integer levels. The empty
independent set uses the original long-filling theorem. Therefore
the proposition applies without another analytic estimate.

In particular, the conclusion is already unconditional for every
fixed path with at least two vertices, with
\[
 \begin{cases}
 |n_v|\ge2,&v\text{ is an endpoint},\\
 n_v\ne0,&v\text{ is an internal vertex},
 \end{cases}
 \tag{7}
\]
and the prescribed parities. All nonzero degree-two powers have
their full two-boundary theorem, and all terminal powers of
magnitude at least two have their full one-boundary theorem.
No bound on the number of vertices is imposed, although \(C\)
may depend on the path.

The exhaustive interval run and its independent archive check
have now completed successfully. Together with the analytic
unbounded-range proof, the isolated-vertex theorem therefore
allows exactly
\[
                         d_v+|n_v|>2
                         \qquad(v\in V).
 \tag{8}
\]
at every original vertex. Thus the proposition applies to every
fixed original circle tree with at least one edge on the domain
(8), with its prescribed parities. The
[coverage theorem](research_isolated_vertex_coverage_and_assembly.md)
records the written proof and the complete certificate.

Condition (7), or its tree version (8), is a restriction on this
corollary. It is not a reason to discard other hyperbolic filling
assignments from the finite-exception goal. In particular, a
degree-two zero filling must be handled with its original parameter
fibers retained.

## 3. A quantitative consequence and its limitation

For the original surgery box \(|p_v|\le H\), a fixed power at a
vertex fixes exactly one surgery coefficient by (6). Each member
of \(\mathcal F\) therefore leaves at most
\((2H+1)^{d-2}\) assignments in that box. Hence
\[
 \#\{\text{untreated assignments in the stated domain and box}\}
       \le |\mathcal F|(2H+1)^{d-2}.
 \tag{9}
\]
Here “untreated” means outside the proved sufficient conclusions,
not a demonstrated failure of the conjecture. The finite branching
argument may equivalently be applied with \(P\) meaning membership
in those proved conclusions; it then bounds precisely that
untreated set.

The original all-long condition gave an \(O(H^{d-1})\) upper bound.
Equation (9) improves this to \(O(H^{d-2})\) on the stated domain.
For \(d=2\), it is a finite bound, consistent with the existing
[two-circle theorem](research_two_circle_finite_exceptions.md).
For \(d>2\), it still allows infinitely many untreated assignments.
It gives no density statement about knot types ordered by crossing
number.

The remaining analytic task is now located more precisely. One
must replace independent-set hypothesis (1) by estimates for fixed
connected short-filled regions with all their unfilled boundary
variables retained. Separate estimates at their vertices do not
provide the estimate of the joined source. If the corresponding
long-remainder theorem holds for every proper fixed partial
assignment, the
[finite-exception lemma](research_finite_exceptions_under_partial_fillings.md#3-a-finite-exception-lemma-for-one-template)
ends only at fully fixed tuples and gives finitely many exceptions.
The adjacent-block theorem needed for that conclusion has not
been proved here.
