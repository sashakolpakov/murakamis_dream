# Residual adjacencies after a full mixed three/four component theorem

Research deduction, 5 November 2026. This is a conditional consequence
for the original integer assignments of one fixed marked circle tree.
It specifies what a full mixed three/four boundary theorem would remove
from the partial-filling induction. It does not assume that the current
retained-contour sector theorems already give that full theorem. No
numerical computation or manuscript change is used.

## 1. The precise additional input

Let \(T=(V,E)\) be a finite original ordered circle tree with an edge,
original degrees \(d_v\), and fixed carriers \(\eta_v\). Retain its
physical turns, disk longitudes, orientations, reduced cut, and the
original relation
\[
                       n_v=\eta_v-2p_v,\qquad p_v\in\mathbb Z.
 \tag{1}
\]
Let \(\mathcal D\) be its hyperbolic knot assignments satisfying
\(d_v+|n_v|>2\) at every vertex. This is the domain of the existing
[isolated-vertex boundary theorem](research_isolated_vertex_coverage_and_assembly.md).
It is an explicit restriction of the present deduction, not a removal
of the other assignments from the finite-exception goal.

Use the following additional hypothesis, denoted \(\mathrm M\).

For every fixed positive word in \(\{3,4\}\), the literal two-boundary
polynomial has its nonzero holomorphic geometric packet near complete
ordinary boundary colors, a calibrated whole real-boundary gap, and
the original marked geometric boundary germ. The latter includes the
continued primitive periods, ordered gluing maps, selected cores,
absolute volume anchor, and persistence under small outside angles.
The same conclusions for a simultaneous reversal of all signs follow
by the original coefficient conjugacy, with its geometric mirror.

These are exactly the analytic and marked premises in
[the mixed stability reduction](research_mixed_open_source_stability_reduction.md),
Section 3. Its local-packet plus real-gap lemma supplies the required
quadratic complex-strip bound; it is not a new hypothesis about a
larger norm. A complete-color scalar asymptotic, the cyclic trace
theorem, or the full unselected plateau sector alone is not
\(\mathrm M\).

For an edge \(uv\), call its two assigned powers compatible when
\[
 d_u=d_v=2,\qquad
 \{n_u,n_v\}\subset\{3,4\}
 \quad\hbox{or}\quad
 \{n_u,n_v\}\subset\{-3,-4\}.
 \tag{2}
\]
The degree requirement applies to both alternatives. All degrees here
are those of the original tree, not the degree inside a selected
subgraph.

## 2. A component condition checked by its selected edges

**Lemma 1.** Under \(\mathrm M\), fix any proper set \(S\subset V\)
and its allowed powers, with \(d_v+|n_v|>2\) for every \(v\in S\).
Suppose every edge of the induced subgraph \(T[S]\)
has compatible assigned powers. There is a finite threshold \(B(S,n_S)\)
such that independently sufficiently long remaining original powers
give the original Kashaev volume identity.

To prove the assertion, examine a connected component \(C\) of \(T[S]\).
A singleton is covered by the isolated-vertex theorem, because its
original degree and fixed power satisfy the defining condition of
\(\mathcal D\). If \(C\) has an edge, (2) gives original degree two
at every vertex of \(C\). Thus \(C\) is a path. The common sign
propagates across its edges and all its powers have magnitude three or
four. If \(k=|C|\), its number of edges meeting the complement is
\[
       \sum_{v\in C}d_v-2|E(C)|=2k-2(k-1)=2.
 \tag{3}
\]
The two outside vertices are distinct: otherwise the path and those
two edges would make a cycle in the original tree. The component is
therefore precisely a two-boundary path to which \(\mathrm M\)
applies.

Now use the exact component assembly in
[componentwise stability](research_componentwise_short_filling_stability.md),
Section 2. Every edge is retained once; different components share
only unfilled ordinary boundary variables. Their literal polynomials
are multiplied without quotient reduction in a free variable. Their
nonzero local amplitudes multiply, and each remaining vertex receives
a strict angular loss and negative complete-boundary Hessian from an
original incidence. The polynomial degree may be a fixed multiple of
\(N-1\), as allowed by the long-filling theorem.

If \(r\) vertices remain free, the original tree edge count gives
initial level power \(N^{-3(r-1)/2}\), and their full traces add
\(N^{3r/2}\). This gives the original nonzero \(N^{3/2}\) coefficient.
Choose the threshold inside the finitely many component and geometric
boundary neighborhoods. The marked primitive slopes and absolute
action then give the volume of the original final knot, with all
carriers and framings retained. This is the assembly already proved
in the cited stability reduction, now with a condition on selected
edges that ensures every component is eligible. \(\square\)

## 3. Finite residual edge records

**Theorem 2.** Under \(\mathrm M\), there is a finite list
\(\mathcal F_T\) of triples \((uv,a,b)\), where \(uv\in E\) and
\(a,b\) are fixed allowed powers, such that:

1. Every triple in the list is incompatible in the sense of (2).
2. Every assignment in \(\mathcal D\) not certified by Lemma 1 and
   its finite partial-filling induction satisfies \(n_u=a,n_v=b\)
   for at least one triple in \(\mathcal F_T\).

In particular, the same conclusion holds for any assignment in
\(\mathcal D\) at which the volume identity fails.

Start with no fixed coordinates. At a node \((S,n_S)\) whose selected
edges are compatible, Lemma 1 gives a finite threshold. Every assignment
not covered there must have a free coordinate of bounded absolute
value. Branch over the finitely many choices of that coordinate and
its allowed value, keeping the original parity from (1). If all
selected edges remain compatible, continue. Otherwise record one
new incompatible edge and its two values and stop that branch.

The depth is at most \(|V|\). A branch cannot end with every coordinate
fixed while all its selected edges are compatible: the original finite
tree has a degree-one vertex, and its incident edge would violate (2).
Thus every followed uncertified assignment reaches a recorded edge.
The tree of choices and its list of records are finite. No uniform
threshold over all partial assignments has been taken. This proves
the theorem. \(\square\)

This sharpens the
[earlier independent-set residual-edge reduction](research_finite_short_patterns_and_exceptional_dimension.md):
none of the residual records now consists of an adjacent same-sign
three/four pair of original degree-two vertices. The number of
successive compatible short vertices is unrestricted. The condition
is also compositional at the graph level: joining two such path
components by another compatible selected edge leaves an eligible
path; disjoint unions preserve eligibility.

If \(d=|V|\), the corresponding number of uncertified surgery
assignments in \(|p_v|\le H\), within \(\mathcal D\), is at most
\[
                    |\mathcal F_T|(2H+1)^{d-2}.
 \tag{4}
\]
The exponent is unchanged from the independent-set theorem; the
new conclusion removes a specified family of edge records, rather
than claiming another codimension improvement. Other proved
component theorems may remove further records from this finite list.
An incompatible record is not a claimed counterexample.

## 4. Why the original degree condition matters

A path inside a selected subgraph need not be a two-boundary source:
an original degree-three vertex has a third boundary, while an
original terminal vertex has only one. The distinction can already
be seen exactly at a pendant end.

Let \(v_N(w)=(e_0(w),\ldots,e_{N-1}(w))^T\), \(A_n=JM^n\), and
\[
 c_{0,N}=2\cos(\pi/N),\qquad
 Z_{\mathbf n,N}(w_L,w_R)
       =v_N(w_L)^TA_{n_1}\cdots A_{n_k}v_N(w_R).
 \tag{5}
\]
The literal Newton definition gives \(e_0(c_{0,N})=1\) and
\(e_j(c_{0,N})=0\) for every \(j\ge1\). Thus, with \(\mathbf e_0\)
the coefficient column of the unit polynomial,
\[
 v_N(c_{0,N})=\mathbf e_0,\qquad
 Z_{\mathbf n,N}(w,c_{0,N})
       =v_N(w)^TA_{n_1}\cdots A_{n_k}\mathbf e_0.
 \tag{6}
\]
The right side is the exact rooted pendant source, in its indicated
order: multiplication by \(R^n\) followed by the physical turn has
matrix \(A_n\). For \(k=1\) it is the familiar \(T(R^n)\).
Equation (6) holds in the full original algebra, not just its
semisimple values; evaluating the untouched free variable retains
all its ordinary derivatives.

But the substituted boundary color tends to \(+2\), not the complete
ordinary color \(-2\). In angular coordinates \(w=-2\cos\theta\),
it is \(\theta=\pi-\pi/N\). Hypothesis \(\mathrm M\)'s local packet
therefore does not apply there. Its whole-boundary upper gap is an
upper bound calibrated to the two-boundary action; it supplies neither
the pendant action nor a nonzero pendant coefficient at this
level-dependent color. This is why an original degree-one endpoint
cannot be included in Lemma 1 by simply calling its selected
component a path.

The existing isolated terminal theorems cover every \(|n|\ge2\),
and several particular pendant compositions have their own proofs.
Equation (6) identifies the additional boundary evaluation needed for
a general pendant word; it does not replace those source proofs.
Similarly, isolated nonzero powers five or six are already covered
by [the all-power degree-two theorem](research_all_nonzero_degree_two_fillings.md).
Their genuinely adjacent compositions require more than those
isolated packets. The
[finite-kernel closure theorem](research_finite_two_boundary_kernel_closure.md)
currently inserts a sufficiently long trace between arbitrary short
kernels.

Finally, the theorem above does not handle assignments outside
\(\mathcal D\), all residual incompatible records, or arbitrary
branching short components. The exact zero/unit moves retain their
original affine parameter fibers. In particular the
[strict-padding and core-fiber obligation](research_finite_exceptions_under_partial_fillings.md)
is unchanged. The full per-template finite-assignment conclusion
does not follow from Theorem 2.
