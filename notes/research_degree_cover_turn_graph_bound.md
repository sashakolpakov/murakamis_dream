# A degree bound on one incidence of every turn

Fix a level \(N\ge2\), put \(m=\lfloor N/2\rfloor\), and use
the original algebra, trace, turn and Newton basis of [T].
Let \(H\) be a fixed finite set of independent paired variables
\(x_h\), partitioned into edges \(\{h,h'\}\).
Other ordinary variables \(\boldsymbol\xi\) remain free.

Let \(F_N(\mathbf x;\boldsymbol\xi)\) be a joint polynomial.
Assume that on each edge at least one of its two incidences
satisfies
\[
                         \deg_{x_h}F_N\le m.                 \tag{1}
\]
There is no degree restriction at the opposite incidence.
Dependence on all other variables may be correlated. Only
variables used by the prescribed traces are reduced in the
original algebra; the free parameters are not reduced.

The original turn contraction is
\[
 Z_N(\boldsymbol\xi)=
 \left(\prod_{h\in H}\phi_N^{(x_h)}\right)
 \left[F_N(\mathbf x;\boldsymbol\xi)
       \prod_{\{h,h'\}}K_N(x_h,x_{h'})\right].               \tag{2}
\]

## Exact formula and proof

Let \(u_N\), its component functionals \(\mathcal E_i\), and
\(B_N\) be the short physical data and coefficient adapter of
[T, equations (4)--(8)]. Thus, for every full original class,
\[
 (a_0(f),\ldots,a_m(f))^t=B_Nu_N(f),\qquad
 \Gamma_N=B_N^tB_N.
\]
At odd levels the data are values at all distinct physical
nodes. At even levels they are the \(m\) physical values and
the ordinary first derivative at the last double node.

**Proposition.** With the exact normalizations of (2),
\[
 Z_N=
 \sum_{\mathbf i\in\{0,\ldots,m\}^{H}}
 \left(\prod_{\{h,h'\}}\Gamma_N(i_h,i_{h'})\right)
 \left(\prod_{h\in H}\mathcal E_{i_h}^{(x_h)}\right)F_N .
                                                               \tag{3}
\]
All fixed free-variable derivatives commute with this identity.
In particular the contraction costs only a polynomial in \(N\)
relative to the maximum of the displayed joint physical data.

To prove it, expand \(F_N\) in the tensor Newton basis after
canonical reduction in its paired variables. Each edge in (2)
sets its two Newton indices equal, because
\(\phi_N(e_rTe_s)=\delta_{rs}\).
By (1), terms whose edge index exceeds \(m\) vanish at that
edge. This holds simultaneously on every edge, regardless of
the correlations among its coefficient tensors.
All surviving indices therefore lie in \(0,\ldots,m\).
The adapter \(B_N\) is valid for those coefficients even at
the unrestricted incidence. Apply it in every variable.
The independent coefficient extractions commute and give (3).

There are \((m+1)^{|H|}\) terms, and every entry of \(\Gamma_N\)
is polynomially bounded by [T, equation (14)]. This proves the
upper bound. There is no assertion about an inverse bound or
a nonzero value of the contracted scalar.

Loops pair two distinct incidences of the same joint tensor;
the same proof applies to them. No product decomposition of
\(F_N\) is required. A multiplication that destroys (1) must
be checked before this proposition can be used.

## Marked vertices and prescribed crossing insertions

Suppose \(F_N\) is the product of compiled vertex tensors.
A/B vertices in [T] have degree at most \(m\) at every port.
It is therefore sufficient that those marked vertices form
a vertex cover: every edge has at least one marked endpoint.
Unmarked vertex tensors may have full degree and arbitrary
joint short physical data.

For untwisted edges the compiled graph is the actual original
kernel graph with its A/B insertions. Each compiled endpoint
contributes one turn, and sewing contributes a third;
\(T^3=T\) restores the original edge. This is an exact source
identity, not an estimate or a change of invariant.

For an oriented insertion \(\phi_N(R^kf\,Tg)\), a sole low
incidence must be the \(g\) incidence. Its index still truncates
the edge sum. Multiplication on the opposite incidence has
the exact short-data matrix \(U_{k,N}\) of [T], and the edge
matrix becomes \(U_{k,N}^t\Gamma_N\).
It has polynomial size for fixed signed \(k\).
If the sole low incidence is instead multiplied by \(R^k\),
its degree need not remain low; that case is not included.

Bounds on the unmarked tensors or a remaining exterior are
still needed to use (3) at a specified geometric action.
Neither (3) nor the vertex-cover condition proves a joint
leading coefficient, a parent-volume comparison, or the
volume identity after arbitrary short fillings.

## Direct source

[T] [Low-degree physical jets and coherent turn graphs](research_low_degree_coherent_turn_graph_bound.md),
SHA256 43071efb1c5b88db76fa5cce8656675d6350d7b4d79931bb5008b085157293e8.
The entire direct proof and every implication used here were read
at this matching pin. Only written mathematics and text operations
were used.
